"""Showcase set (spec 5.1) and its batch run: ~130 notes in one Message Batches job (half price),
then every failure is retried one by one through the normal path (with fallbacks).
"""

import json
import logging
import time
from datetime import date
from pathlib import Path

import pandas as pd

from canary.analyst.context import Context
from canary.analyst.facts import build_fact_sheet
from canary.analyst.outcome import AFTER_WINDOW_START, default_as_of
from canary.analyst.sections import all_sections
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

EST_INPUT_TOKENS = 3500  # per bank, fact sheet and prompt (a real request is ~13.5k characters)
EST_OUTPUT_TOKENS = 2000  # per bank


def _as_dt(d: date) -> pd.Timestamp:
    return pd.Timestamp(d)


def showcase_banks(ctx: Context, model_dir: Path, replay_dir: Path) -> list[tuple[int, date, str]]:
    """(cert, as_of, group). First group wins: case study, test miss, test catch, after window,
    latest watchlist, false alarm."""
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
    for cert in sorted(now["cert"].astype(int)):
        add(cert, latest, "latest_watchlist")

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


def run_showcase(ctx: Context, client, model: str, out_dir: Path, report_path: Path,
                 poll_seconds: int = 60, *, banks: list[tuple[int, date, str]] | None = None,
                 model_dir: Path = Path("data/model"), replay_dir: Path = Path("data/replay")) -> dict:
    banks = banks if banks is not None else showcase_banks(ctx, model_dir, replay_dir)
    meta = {custom_id(c, d): (c, d, g) for c, d, g in banks}
    requests, early = [], {}
    for cert, as_of, group in banks:
        try:
            sheet = build_fact_sheet(ctx, cert, as_of, replay_dir=replay_dir)
        except ValueError as exc:
            early[custom_id(cert, as_of)] = str(exc)
            continue
        params = build_request(sheet, all_sections(sheet.outcome.kind), model)
        requests.append({"custom_id": custom_id(cert, as_of), "params": params})

    first: dict[str, dict] = {}   # custom_id -> parsed memo from the batch
    why_retry: dict[str, str] = dict(early)
    totals = {"in": 0, "out": 0, "cost": 0.0}
    if requests:
        batch = client.messages.batches.create(requests=requests)
        while client.messages.batches.retrieve(batch.id).processing_status != "ended":
            time.sleep(poll_seconds)
        for item in client.messages.batches.results(batch.id):
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
            except (RefusalError, TruncatedError, ValueError, StopIteration) as exc:
                why_retry[cid] = f"batch result unusable: {exc}"
        for r in requests:
            if r["custom_id"] not in first and r["custom_id"] not in why_retry:
                why_retry[r["custom_id"]] = "no batch result"

    entries = []
    for cid, (cert, as_of, group) in meta.items():
        entry = {"cert": cert, "as_of": as_of.isoformat(), "group": group, "ok": False, "attempts": 0,
                 "path": None, "errors": [], "source": "batch" if cid in first else "retry"}
        try:
            res = write_memo(ctx, cert, as_of, client=client, model=model, out_dir=out_dir,
                             first_memo=first.get(cid), replay_dir=replay_dir)
        except Exception as exc:  # one bank must never abort the run or lose the report
            entry["errors"] = [f"{type(exc).__name__}: {exc}"]
            if cid in why_retry:
                entry["errors"].insert(0, why_retry[cid])
            entry["attempts"] = 1
            log.warning("showcase: cert %s failed: %s", cert, exc)
        else:
            totals["in"] += res.input_tokens
            totals["out"] += res.output_tokens
            totals["cost"] += res.cost_usd
            entry.update(ok=res.ok, attempts=res.attempts + (1 if cid not in first else 0),
                         path=str(res.path) if res.path else None, errors=res.errors)
        entries.append(entry)

    report = {
        "model": model,
        "banks_total": len(entries),
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
