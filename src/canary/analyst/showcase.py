"""Showcase set (spec 5.1) and its batch run: ~130 notes in one Message Batches job (half price),
then every failure is retried one by one through the normal path (with fallbacks).
"""

import json
import logging
import time
from datetime import date, datetime
from pathlib import Path

import pandas as pd

from canary.analyst.context import Context
from canary.analyst.facts import build_fact_sheet
from canary.analyst.outcome import AFTER_WINDOW_START, default_as_of
from canary.analyst.sections import sections_for
from canary.analyst.writer import (
    PRICES,
    RefusalError,
    TruncatedError,
    build_request,
    cost_usd,
    parse_response,
    write_memo,
)
from canary.model.train import CASE_STUDY_CERTS

log = logging.getLogger(__name__)

# Measured averages per call from the 2026-11-17 live Opus comparison (adaptive thinking adds output tokens).
EST_INPUT_TOKENS = 7300  # per bank
EST_OUTPUT_TOKENS = 3200  # per bank
RETRY_TRIES = 5  # retrieve/results calls: tries before a transient API error is re-raised
RETRY_BASE_SECONDS = 2.0  # backoff 2, 4, 8, 16 s


def _as_dt(d: date) -> pd.Timestamp:
    return pd.Timestamp(d)


def showcase_banks(ctx: Context, model_dir: Path, replay_dir: Path,
                   watchlist_top: int | None = None) -> list[tuple[int, date, str]]:
    """(cert, as_of, group). First group wins: case study, test miss, test catch, after window,
    latest watchlist, false alarm. With `watchlist_top`, the latest watchlist group takes only the
    best-ranked N flagged banks (banks claimed by an earlier group do not count toward N)."""
    scored = ctx.scored
    banks = ctx.banks
    known = set(banks["cert"])
    latest = ctx.latest_quarter

    def last_report(cert: int) -> date:
        return default_as_of(ctx, cert)

    picks: list[tuple[int, date, str]] = []
    seen: set[int] = set()

    def add(cert: int, as_of: date, group: str) -> None:
        if cert in seen or cert not in known:
            return
        seen.add(cert)
        picks.append((cert, as_of, group))

    for cert in CASE_STUDY_CERTS:
        add(cert, last_report(cert) if cert in known else latest, "case_study")
    misses = pd.read_csv(replay_dir / "test_misses.csv")["cert"].astype(int).tolist()
    for cert in misses:
        add(cert, last_report(cert) if cert in known else latest, "test_miss")
    caught = json.loads((model_dir / "metrics.json").read_text())["caught_certs"]
    for cert in caught:
        add(int(cert), last_report(int(cert)) if int(cert) in known else latest, "test_catch")

    late = banks[banks["failure_date"] > _as_dt(AFTER_WINDOW_START)]
    for cert in late["cert"].astype(int):
        rows = scored[(scored["cert"] == cert) & scored["quarters_until_failure"].between(1, 4)]
        if not rows.empty:
            add(cert, last_report(cert), "after_window")

    now = scored[(scored["report_date"] == _as_dt(latest)) & scored["flagged"].astype(bool)]
    ordered = now.sort_values("rank")["cert"].astype(int).tolist() if watchlist_top is not None \
        else sorted(now["cert"].astype(int))
    added = 0
    for cert in ordered:
        if watchlist_top is not None and added >= watchlist_top:
            break
        n = len(picks)
        add(cert, latest, "latest_watchlist")
        added += len(picks) - n

    on_watchlist = set(now["cert"].astype(int))
    fa = pd.read_csv(replay_dir / "top_false_alarm_banks.csv")["cert"].astype(int).tolist()
    for cert in fa:
        if cert in seen:
            continue
        flagged = scored[(scored["cert"] == cert) & scored["flagged"].astype(bool)]
        if cert in on_watchlist:
            add(cert, latest, "false_alarm")
        elif not flagged.empty:
            add(cert, flagged["report_date"].max().date(), "false_alarm")
    return picks


def estimate_cost(n_banks: int, model: str) -> float:
    """Dry-run estimate at the batch (half) price."""
    return cost_usd(model, EST_INPUT_TOKENS * n_banks, EST_OUTPUT_TOKENS * n_banks) / 2


def custom_id(cert: int, as_of: date) -> str:
    return f"{cert}-{as_of:%Y%m%d}"


def state_path(report_path: Path) -> Path:
    """Where the batch id is saved as soon as the batch exists (next to the report)."""
    return Path(report_path).with_suffix(".state.json")


def read_state(report_path: Path) -> dict | None:
    path = state_path(report_path)
    return json.loads(path.read_text()) if path.exists() else None


def _write_state(report_path: Path, state: dict) -> None:
    path = state_path(report_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2))


def _transient(exc: BaseException) -> bool:
    try:
        import anthropic
    except ImportError:  # pragma: no cover - the analyst extra is installed wherever this runs
        return False
    if isinstance(exc, anthropic.APIConnectionError):  # includes timeouts
        return True
    status = getattr(exc, "status_code", None)
    return isinstance(exc, anthropic.APIStatusError) and (status in (408, 409, 429) or (status or 0) >= 500)


def _retry(fn, *args):
    """fn(*args), retried with backoff on transient API errors; re-raised after RETRY_TRIES tries."""
    for attempt in range(1, RETRY_TRIES + 1):
        try:
            return fn(*args)
        except Exception as exc:
            if attempt == RETRY_TRIES or not _transient(exc):
                raise
            wait = RETRY_BASE_SECONDS * 2 ** (attempt - 1)
            log.warning("showcase: %s (try %d of %d); retrying in %.0fs", exc, attempt, RETRY_TRIES, wait)
            time.sleep(wait)


def _usage_of(exc: BaseException) -> dict:
    u = getattr(exc, "usage", None)
    return u if isinstance(u, dict) else {}


def run_showcase(ctx: Context, client, model: str, out_dir: Path, report_path: Path,
                 poll_seconds: int = 60, *, banks: list[tuple[int, date, str]] | None = None,
                 model_dir: Path = Path("data/model"), replay_dir: Path = Path("data/replay"),
                 resume: str | None = None) -> dict:
    """Run the showcase batch. With `resume=BATCH_ID`, no batch is created: that batch is polled and
    collected (its bank list and model come from the state file when it names the same batch).
    The report is always written, partial if something escapes."""
    state = read_state(report_path) if resume else None
    if state is not None and state.get("batch_id") == resume:
        banks = [(int(c), date.fromisoformat(d), g) for c, d, g in state["banks"]]
        model = state.get("model", model)
    banks = banks if banks is not None else showcase_banks(ctx, model_dir, replay_dir)
    meta = {custom_id(c, d): (c, d, g) for c, d, g in banks}
    entries: list[dict] = []
    totals = {"in": 0, "out": 0, "cost": 0.0}
    run = {"batch_id": resume, "error": None}
    try:
        _run_batch(ctx, client, model, out_dir, report_path, poll_seconds, banks, meta, replay_dir, resume,
                   entries, totals, run)
        # Only now is the batch fully used: results collected and every bank written or retried.
        st = read_state(report_path)
        if run["batch_id"] and st is not None and st.get("batch_id") == run["batch_id"]:
            _write_state(report_path, {**st, "complete": True})
    except BaseException as exc:
        run["error"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        report = {
            "model": model,
            "batch_id": run["batch_id"],
            "complete": run["error"] is None,
            "error": run["error"],
            "banks_total": len(meta),
            "banks_done": len(entries),
            "written": sum(e["ok"] for e in entries),
            "failed": sum(not e["ok"] for e in entries),
            "input_tokens": totals["in"],
            "output_tokens": totals["out"],
            "cost_usd": totals["cost"],
            "banks": entries,
        }
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2))
    return report


def _run_batch(ctx, client, model, out_dir, report_path, poll_seconds, banks, meta, replay_dir, resume,
         entries, totals, run) -> None:
    requests, early = [], {}
    for cert, as_of, group in banks:
        try:
            sheet = build_fact_sheet(ctx, cert, as_of, replay_dir=replay_dir)
        except ValueError as exc:
            early[custom_id(cert, as_of)] = str(exc)
            continue
        params = build_request(sheet, sections_for(sheet), model)
        requests.append({"custom_id": custom_id(cert, as_of), "params": params})

    first: dict[str, dict] = {}   # custom_id -> parsed memo from the batch
    why_retry: dict[str, str] = dict(early)
    if requests:
        if resume:
            batch_id = resume
            log.info("showcase: resuming batch %s", batch_id)
        else:
            batch_id = client.messages.batches.create(requests=requests).id
            run["batch_id"] = batch_id
            log.info("showcase: created batch %s (%d requests); resume with --resume %s",
                     batch_id, len(requests), batch_id)
            _write_state(report_path, {
                "batch_id": batch_id, "created_at": datetime.now().isoformat(timespec="seconds"),
                "banks": [[c, d.isoformat(), g] for c, d, g in banks], "model": model, "complete": False})
        while _retry(client.messages.batches.retrieve, batch_id).processing_status != "ended":
            time.sleep(poll_seconds)
        for item in _retry(client.messages.batches.results, batch_id):
            cid, res = item.custom_id, item.result
            if res.type != "succeeded":
                why_retry[cid] = f"batch result {res.type}"
                continue
            msg = res.message
            i, o = msg.usage.input_tokens, msg.usage.output_tokens
            served = msg.model if msg.model in PRICES else model
            totals["in"] += i
            totals["out"] += o
            totals["cost"] += cost_usd(served, i, o) / 2  # batch is half price
            try:
                first[cid] = parse_response(msg)
            except (RefusalError, TruncatedError, ValueError) as exc:
                why_retry[cid] = f"batch result unusable: {exc}"
        for r in requests:
            if r["custom_id"] not in first and r["custom_id"] not in why_retry:
                why_retry[r["custom_id"]] = "no batch result"

    for cid, (cert, as_of, group) in meta.items():
        entry = {"cert": cert, "as_of": as_of.isoformat(), "group": group, "ok": False, "attempts": 0,
                 "path": None, "errors": [], "source": "batch" if cid in first else "retry",
                 "served_model": None}
        try:
            res = write_memo(ctx, cert, as_of, client=client, model=model, out_dir=out_dir,
                             first_memo=first.get(cid), replay_dir=replay_dir)
        except Exception as exc:  # one bank must never abort the run or lose the report
            entry["errors"] = [f"{type(exc).__name__}: {exc}"]
            if cid in why_retry:
                entry["errors"].insert(0, why_retry[cid])
            entry["attempts"] = 1
            u = _usage_of(exc)  # calls made before the exception still cost money
            totals["in"] += u.get("input_tokens", 0)
            totals["out"] += u.get("output_tokens", 0)
            totals["cost"] += u.get("cost_usd", 0.0)
            entry["served_model"] = u.get("model")
            log.warning("showcase: cert %s failed: %s", cert, exc)
        else:
            totals["in"] += res.input_tokens
            totals["out"] += res.output_tokens
            totals["cost"] += res.cost_usd
            entry.update(ok=res.ok, attempts=res.attempts + (1 if cid not in first else 0),
                         path=str(res.path) if res.path else None, errors=res.errors, served_model=res.model)
        entries.append(entry)
