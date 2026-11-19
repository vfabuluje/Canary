"""Showcase set (spec 5.1) and its batch run, in two Message Batches rounds (half price): round 1 holds
the trend and peer requests; once those are collected, checked and retried one by one (full price, with
fallbacks), round 2 holds one analyst request per bank whose specialists passed. Progress is saved after
each step so `--resume` never pays for a finished round or a finished bank again.
"""

import json
import logging
import re
import shutil
import time
from collections import Counter
from dataclasses import asdict
from datetime import date, datetime
from pathlib import Path

import pandas as pd

from canary.analyst.context import Context
from canary.analyst.facts import build_fact_sheet
from canary.analyst.outcome import AFTER_WINDOW_START, default_as_of
from canary.analyst.pipeline import AGENTS, AgentResult, agent_sections, build_agent_request, run_agent
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

# Dry-run estimate (derivation in runbooks/analyst.md). Phase 5c live memo: 11,292 output over 2 calls, so
# about 5,650 per call, rounded to 5,700 (adaptive thinking included). Input is estimated from the real
# request size; CHARS_PER_TOKEN is calibrated on the 5b SVB request (22,979 chars, 22,571 measured input).
EST_OUTPUT_TOKENS = 5700  # per call (per bank first try, and per retry)
CHARS_PER_TOKEN = 2.4  # calibrated on the SVB 2022-03-31 request (22,979 chars); 3.5 would under-count ~30%
RETRY_SHARE = 0.6  # share of banks retried (5b showcase: 37 of 61 needed a retry)
RETRY_INPUT_FACTOR = 2.0  # a retry resends the request plus the rejected memo: about 2x the first input
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


def request_tokens(request: dict) -> int:
    """Input tokens estimated from the size of the built request."""
    return round(len(json.dumps(request)) / CHARS_PER_TOKEN)


def estimate_run(ctx: Context, banks: list[tuple[int, date, str]], model: str,
                 replay_dir: Path | None = None) -> dict:
    """Dry-run estimate from the actual requests (no API calls). Batch price (half) for the first tries;
    the retry allowance is priced at the full, non-batch rate."""
    sizes = []
    for cert, as_of, _group in banks:
        try:
            sheet = build_fact_sheet(ctx, cert, as_of=as_of, replay_dir=replay_dir)
        except ValueError:  # a bank that cannot be built is priced at the average of the others
            continue
        sizes.append(request_tokens(build_request(sheet, sections_for(sheet), model)))
    n_in = sum(sizes) + round((len(banks) - len(sizes)) * (sum(sizes) / len(sizes))) if sizes else 0
    n_out = EST_OUTPUT_TOKENS * len(banks)
    retries = round(RETRY_SHARE * len(banks))
    retry_in = round(RETRY_INPUT_FACTOR * n_in * retries / max(len(banks), 1))
    retry_out = EST_OUTPUT_TOKENS * retries
    first = cost_usd(model, n_in, n_out) / 2
    retry = cost_usd(model, retry_in, retry_out)
    return {"input": n_in, "output": n_out, "cost": first, "retries": retries, "retry_input": retry_in,
            "retry_output": retry_out, "retry_cost": retry, "total": first + retry}


def custom_id(cert: int, as_of: date, agent: str | None = None) -> str:
    """Bank key `cert-YYYYMMDD`; with an agent, the batch request id `cert-YYYYMMDD-agent`."""
    base = f"{cert}-{as_of:%Y%m%d}"
    return f"{base}-{agent}" if agent else base


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


_SECTION = re.compile(r"section '(\w+)'")


def _section_tally(entries: list[dict]) -> dict[str, int]:
    """First-attempt checker errors counted by memo section (one count per error)."""
    c: Counter = Counter()
    for e in entries:
        for err in e.get("first_errors") or []:
            m = _SECTION.search(err)
            c[m.group(1) if m else "other"] += 1
    return dict(c.most_common())


def _usage_of(exc: BaseException) -> dict:
    u = getattr(exc, "usage", None)
    return u if isinstance(u, dict) else {}


SPECIALISTS = ("trend", "peer")


def _zero_spend() -> dict:
    return {"batch": 0.0, "direct": 0.0, "input": 0, "output": 0}


class _Run:
    """One showcase run: the two rounds, the saved progress and the report numbers.

    Saved next to the report: `<report>.state.json` (batch ids per round, spend per round, per-agent
    status) and `<report>.progress/` (round results as collected, each agent's checked result and trace,
    each finished bank's report entry). Resume reads these and redoes nothing that is saved.
    """

    def __init__(self, ctx, client, model, out_dir, report_path, poll_seconds, banks, replay_dir, trace_dir,
                 state: dict) -> None:
        self.ctx, self.client, self.model = ctx, client, model
        self.out_dir, self.report_path, self.poll_seconds = out_dir, report_path, poll_seconds
        self.banks, self.replay_dir, self.trace_dir = banks, replay_dir, trace_dir
        self.state = state
        self.progress = Path(report_path).with_suffix(".progress")
        self.entries: dict[str, dict] = {}

    # -- saved state ------------------------------------------------------------------------
    def save(self) -> None:
        """Persist the state once the first batch exists (a run that never submitted leaves no file)."""
        if self.state.get("round1_batch_id"):
            _write_state(self.report_path, self.state)

    def _spend(self, rnd: int) -> dict:
        return self.state["spend"].setdefault(f"round{rnd}", _zero_spend())

    def _file(self, name: str) -> Path:
        return self.progress / f"{name}.json"

    def _write_file(self, name: str, data) -> None:
        self.progress.mkdir(parents=True, exist_ok=True)
        self._file(name).write_text(json.dumps(data, default=str))

    def _read_file(self, name: str):
        path = self._file(name)
        return json.loads(path.read_text()) if path.exists() else None

    def _load_agent(self, base: str, agent: str):
        d = self._read_file(f"{base}-{agent}")
        return None if d is None else (AgentResult(**d["result"]), d["trace"], d["source"])

    # -- one batch round --------------------------------------------------------------------
    def _collect(self, rnd: int, requests: list[dict]) -> dict[str, dict]:
        """Create (unless this run already has) the round's batch, wait for it, and return
        custom_id -> {memo, why, served, in, out, cost}. Collected results are saved, so a finished
        round is never fetched or paid again. Spend is added exactly once per round."""
        key = f"round{rnd}_batch_id"
        collected = self._read_file(f"round{rnd}_batch")
        if collected is None:
            batch_id = self.state.get(key)
            if batch_id:
                log.info("showcase: resuming round %d batch %s", rnd, batch_id)
            else:
                batch_id = self.client.messages.batches.create(requests=requests).id
                self.state[key] = batch_id
                if rnd == 1:
                    self.state["batch_id"] = batch_id
                log.info("showcase: created round %d batch %s (%d requests); resume with --resume %s",
                         rnd, batch_id, len(requests), self.state.get("round1_batch_id"))
                self.save()
            while _retry(self.client.messages.batches.retrieve, batch_id).processing_status != "ended":
                time.sleep(self.poll_seconds)
            collected = {}
            for item in _retry(self.client.messages.batches.results, batch_id):
                cid, res = item.custom_id, item.result
                if res.type != "succeeded":
                    collected[cid] = {"memo": None, "why": f"batch result {res.type}"}
                    continue
                msg = res.message
                i, o = msg.usage.input_tokens, msg.usage.output_tokens
                served = msg.model if msg.model in PRICES else self.model
                c = cost_usd(served, i, o) / 2  # batch is half price
                entry = {"memo": None, "why": None, "served": served, "in": i, "out": o, "cost": c}
                try:
                    entry["memo"] = parse_response(msg)
                except (RefusalError, TruncatedError, ValueError) as exc:
                    entry["why"] = f"batch result unusable: {exc}"
                collected[cid] = entry
            self._write_file(f"round{rnd}_batch", collected)
        if not self.state.get(f"round{rnd}_collected"):
            sp = self._spend(rnd)
            for e in collected.values():
                sp["batch"] += e.get("cost", 0.0)
                sp["input"] += e.get("in", 0)
                sp["output"] += e.get("out", 0)
            self.state[f"round{rnd}_collected"] = True
            self.save()
        return collected

    # -- one agent --------------------------------------------------------------------------
    def _run_agent(self, rnd: int, base: str, sheet, agent: str, first: dict | None,
                   specialist_memos: dict | None = None) -> AgentResult:
        """Check one agent's batch result (or make its first call directly), retry once at full price,
        and save the outcome. This is the one place a full-price call can start (spending-limit check
        point); the round boundary is `_round_boundary`."""
        trace: list = []
        memo = first.get("memo") if first else None
        try:
            res = run_agent(sheet, agent, client=self.client, model=self.model, specialist_memos=specialist_memos,
                            first_memo=memo, trace=trace)
        except Exception as exc:  # one agent must never abort the run or lose the report
            u = _usage_of(exc)  # calls made before the exception still cost money
            errors = [f"{type(exc).__name__}: {exc}"]
            if first and first.get("why"):
                errors.insert(0, first["why"])
            res = AgentResult(agent, ok=False, attempts=max(1, len(trace)), errors=errors,
                              input_tokens=u.get("input_tokens", 0), output_tokens=u.get("output_tokens", 0),
                              cost_usd=u.get("cost_usd", 0.0), served_model=u.get("model"))
            log.warning("showcase: %s %s failed: %s", base, agent, exc)
        batch_cost = 0.0
        if memo is not None and first:
            batch_cost = first.get("cost", 0.0)
            for t in trace:
                if t["source"] == "batch":
                    t.update(input_tokens=first.get("in", 0), output_tokens=first.get("out", 0),
                             cost_usd=batch_cost, served_model=first.get("served"))
            if res.attempts == 1 and res.served_model == self.model:
                res.served_model = first.get("served") or res.served_model
        sp = self._spend(rnd)  # batch spend was counted when the round was collected
        sp["direct"] += res.cost_usd
        sp["input"] += res.input_tokens
        sp["output"] += res.output_tokens
        self._write_file(f"{base}-{agent}", {"result": asdict(res), "trace": trace,
                                             "source": "batch" if memo is not None else "direct"})
        self.state.setdefault("agents", {}).setdefault(base, {})[agent] = {
            "ok": res.ok, "spend": batch_cost + res.cost_usd}
        self.save()
        return res

    def _round_boundary(self, rnd: int) -> None:
        """Called before a round's batch is submitted (and after round 1's checks and retries)."""

    # -- one bank ---------------------------------------------------------------------------
    def _finish(self, cert: int, as_of: date, group: str, base: str) -> None:
        """Write the note (or, if an agent failed, only the trace) from the saved agent results."""
        loaded = {a: self._load_agent(base, a) for a in AGENTS}
        prior, trace, agents = {}, [], {}
        for a in AGENTS:
            got = loaded[a]
            if got is None:
                agents[a] = {"ok": False, "attempts": 0, "first_errors": [], "source": None}
                if a in SPECIALISTS and a not in prior and not self._needs(base, a):
                    prior[a] = AgentResult(a, ok=True, skipped=True)
                    agents[a] = {"ok": True, "attempts": 0, "first_errors": [], "source": "code"}
                continue
            res, tr, src = got
            prior[a] = res
            trace += tr
            agents[a] = {"ok": res.ok, "attempts": res.attempts, "first_errors": res.first_errors, "source": src}
        results = [(a, loaded[a][0]) for a in AGENTS if loaded[a] is not None]
        entry = {"cert": cert, "as_of": as_of.isoformat(), "group": group, "ok": False,
                 "attempts": max((r.attempts for _, r in results), default=0), "path": None,
                 "errors": [f"[{a}] {e}" for a, r in results for e in r.errors],
                 "source": "batch" if all(agents[a]["source"] in ("batch", "code") for a in AGENTS) else "retry",
                 "served_model": next((r.served_model for _, r in reversed(results) if r.served_model), None),
                 "first_errors": [f"[{a}] {e}" for a, r in results for e in r.first_errors], "agents": agents}
        try:
            res = write_memo(self.ctx, cert, as_of, client=self.client, model=self.model, out_dir=self.out_dir,
                             replay_dir=self.replay_dir, trace_dir=self.trace_dir, prior=prior, prior_trace=trace)
        except Exception as exc:
            entry["errors"].append(f"{type(exc).__name__}: {exc}")
            log.warning("showcase: cert %s failed: %s", cert, exc)
        else:
            entry.update(ok=res.ok, path=str(res.path) if res.path else None)
        self._write_file(f"{base}-entry", entry)
        self.entries[base] = entry

    def _needs(self, base: str, agent: str) -> bool:
        return agent in self._requested.get(base, ())

    # -- the run ----------------------------------------------------------------------------
    def run(self) -> None:
        self._requested: dict[str, set] = {}
        live = []  # (cert, as_of, group, base, sheet)
        for cert, as_of, group in self.banks:
            base = custom_id(cert, as_of)
            done = self._read_file(f"{base}-entry")
            if done is not None:
                self.entries[base] = done
            try:
                sheet = build_fact_sheet(self.ctx, cert, as_of, replay_dir=self.replay_dir)
            except ValueError as exc:
                self.entries[base] = {"cert": cert, "as_of": as_of.isoformat(), "group": group, "ok": False,
                                      "attempts": 0, "path": None, "errors": [str(exc)], "source": "retry",
                                      "served_model": None, "first_errors": [], "agents": {}}
                continue
            self._requested[base] = {a for a in SPECIALISTS if agent_sections(sheet, a)}
            if base not in self.entries:
                live.append((cert, as_of, group, base, sheet))

        # Round 1: trend and peer requests (a code-only specialist has none).
        todo = [(b, a) for b in live for a in SPECIALISTS if a in self._requested[b[3]]
                and self._load_agent(b[3], a) is None]
        if todo:
            self._round_boundary(1)
            requests = [{"custom_id": custom_id(b[0], b[1], a), "params": build_agent_request(b[4], a, self.model)}
                        for b, a in todo]
            batch = self._collect(1, requests)
            for b, a in todo:
                first = batch.get(custom_id(b[0], b[1], a)) or {"memo": None, "why": "no batch result"}
                self._run_agent(1, b[3], b[4], a, first)

        spec_ok = {}
        for cert, as_of, group, base, sheet in live:
            results = {a: self._load_agent(base, a) for a in SPECIALISTS if a in self._requested[base]}
            if all(r[0].ok for r in results.values()):
                spec_ok[base] = {a: r[0].memo for a, r in results.items()}
            else:
                self._finish(cert, as_of, group, base)  # a specialist failed: no analyst call, no note

        # Round 2: one analyst request per bank whose specialists passed.
        eligible = [b for b in live if b[3] in spec_ok]
        todo2 = [b for b in eligible if self._load_agent(b[3], "analyst") is None]
        if todo2:
            self._round_boundary(2)
            requests = [{"custom_id": custom_id(b[0], b[1], "analyst"),
                         "params": build_agent_request(b[4], "analyst", self.model, spec_ok[b[3]])} for b in todo2]
            batch = self._collect(2, requests)
            for b in todo2:
                first = batch.get(custom_id(b[0], b[1], "analyst")) or {"memo": None, "why": "no batch result"}
                self._run_agent(2, b[3], b[4], "analyst", first, spec_ok[b[3]])
        for cert, as_of, group, base, sheet in eligible:
            self._finish(cert, as_of, group, base)


def run_showcase(ctx: Context, client, model: str, out_dir: Path, report_path: Path,
                 poll_seconds: int = 60, *, banks: list[tuple[int, date, str]] | None = None,
                 model_dir: Path = Path("data/model"), replay_dir: Path = Path("data/replay"),
                 resume: str | None = None, trace_dir: Path = Path("data/analyst/traces")) -> dict:
    """Run the showcase in two batch rounds. With `resume=BATCH_ID` (either round's id), no finished round
    is created or paid again: saved results are reused, a batch that exists is polled and collected (the bank
    list and model come from the state file when it names that batch). The report is always written,
    partial if something escapes."""
    state = read_state(report_path) if resume else None
    ids = {state.get(k) for k in ("batch_id", "round1_batch_id", "round2_batch_id")} - {None} if state else set()
    if state is not None and resume in ids:
        banks = [(int(c), date.fromisoformat(d), g) for c, d, g in state["banks"]]
        model = state.get("model", model)
        state.setdefault("round1_batch_id", state.get("batch_id"))
        state.setdefault("spend", {})
    else:
        state = {"batch_id": resume, "round1_batch_id": resume, "round2_batch_id": None, "spend": {},
                 "created_at": datetime.now().isoformat(timespec="seconds"), "model": model, "complete": False}
        banks = banks if banks is not None else showcase_banks(ctx, model_dir, replay_dir)
        state["banks"] = [[c, d.isoformat(), g] for c, d, g in banks]
        shutil.rmtree(Path(report_path).with_suffix(".progress"), ignore_errors=True)  # nothing stale carries over
    run = _Run(ctx, client, model, out_dir, report_path, poll_seconds, banks, replay_dir, trace_dir, state)
    error = None
    try:
        run.run()
        # Only now are both rounds fully used: results collected and every bank written or retried.
        if state.get("round1_batch_id"):
            state["complete"] = True
            run.save()
    except BaseException as exc:
        error = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        entries = [run.entries[b] for b in (custom_id(c, d) for c, d, _ in banks) if b in run.entries]
        spend = {k: {**v, "total": v["batch"] + v["direct"]} for k, v in state["spend"].items()}
        for k in ("round1", "round2"):
            spend.setdefault(k, {**_zero_spend(), "total": 0.0})
        passed = {a: sum(e["agents"].get(a, {}).get("ok", False) and not e["agents"][a]["first_errors"]
                         and e["agents"][a]["source"] != "code" for e in entries) for a in AGENTS}
        report = {
            "model": model,
            "batch_id": state.get("round1_batch_id"),
            "round1_batch_id": state.get("round1_batch_id"),
            "round2_batch_id": state.get("round2_batch_id"),
            "complete": error is None,
            "error": error,
            "banks_total": len(banks),
            "banks_done": len(entries),
            "written": sum(e["ok"] for e in entries),
            "failed": sum(not e["ok"] for e in entries),
            "first_try_passed": sum(e["ok"] and not e.get("first_errors") for e in entries),
            "first_try_passed_by_agent": passed,
            "first_error_sections": _section_tally(entries),
            "input_tokens": sum(v["input"] for v in spend.values()),
            "output_tokens": sum(v["output"] for v in spend.values()),
            "cost_usd": sum(v["total"] for v in spend.values()),
            "spend_by_round": spend,
            "banks": entries,
        }
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2))
    return report
