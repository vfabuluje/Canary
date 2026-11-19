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
from canary.analyst.pipeline import (
    AGENT_SECTIONS, AGENTS, AgentResult, agent_sections, build_agent_request, run_agent,
)
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

# Dry-run estimate (derivation in runbooks/analyst.md). Output tokens per call type; the old single-call
# figure was 5,700 (Phase 5c live memo: 11,292 output over 2 calls, adaptive thinking included). Input is
# estimated from the real request size; CHARS_PER_TOKEN is calibrated on the 5b SVB request (22,979 chars,
# 22,571 measured input). The per-agent constants are placeholders until the calibration memo.
EST_OUTPUT_TOKENS_BY_AGENT = {"trend": 5700, "peer": 5700, "analyst": 5700}  # calibrated in Task 6
EST_ANALYST_SPECIALIST_CHARS = 6000  # calibrated in Task 6: placeholder text per specialist section in the analyst request
RETRY_SHARE_BY_AGENT = {"trend": 0.16, "peer": 0.16, "analyst": 0.16}  # calibrated in Task 6 (5b: 10 of 61 memos retried)
CHARS_PER_TOKEN = 2.4  # calibrated on the SVB 2022-03-31 request (22,979 chars); 3.5 would under-count ~30%
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


def _placeholder_memo(key: str) -> dict:
    """A specialist memo of typical length (EST_ANALYST_SPECIALIST_CHARS), only to size the analyst request."""
    text = "x" * EST_ANALYST_SPECIALIST_CHARS
    return {"sections": [{"key": key, "paragraphs": [{"sentences": [{"text": text, "cites": []}]}]}]}


def _placeholder_memos(sheet) -> dict[str, dict]:
    return {a: _placeholder_memo(AGENT_SECTIONS[a]) for a in SPECIALISTS if agent_sections(sheet, a)}


def estimate_run(ctx: Context, banks: list[tuple[int, date, str]], model: str,
                 replay_dir: Path | None = None) -> dict:
    """Dry-run estimate from the actual requests (no API calls), per round and per call type.

    Round 1 = the real trend and peer requests; round 2 = the real analyst requests built with placeholder
    specialist sections (EST_ANALYST_SPECIALIST_CHARS each). Output is EST_OUTPUT_TOKENS_BY_AGENT per call.
    Both rounds are priced at the batch rate (half). The retry allowance is per call type: RETRY_SHARE_BY_AGENT
    of that agent's calls, each resending about RETRY_INPUT_FACTOR x the average request, at full price.
    A bank that cannot be built is priced at the average request of the others, for every call type.
    Returns {rounds: {1|2: {requests, input, output, cost, by_agent}}, retries: {agent: {calls, input, output,
    cost}}, input, output, cost (batch total), retry_cost, total}.
    """
    sizes: dict[str, list[int]] = {a: [] for a in AGENTS}
    unbuilt = 0
    for cert, as_of, _group in banks:
        try:
            sheet = build_fact_sheet(ctx, cert, as_of=as_of, replay_dir=replay_dir)
        except ValueError:
            unbuilt += 1
            continue
        for a in SPECIALISTS:
            if agent_sections(sheet, a):
                sizes[a].append(request_tokens(build_agent_request(sheet, a, model)))
        sizes["analyst"].append(request_tokens(
            build_agent_request(sheet, "analyst", model, _placeholder_memos(sheet))))
    by_agent: dict[str, dict] = {}
    for a in AGENTS:
        n = len(sizes[a]) + (unbuilt if sizes[a] else 0)
        n_in = sum(sizes[a]) + (round(unbuilt * sum(sizes[a]) / len(sizes[a])) if sizes[a] else 0)
        n_out = EST_OUTPUT_TOKENS_BY_AGENT[a] * n
        by_agent[a] = {"requests": n, "input": n_in, "output": n_out, "cost": cost_usd(model, n_in, n_out) / 2}
    rounds = {}
    for rnd, agents in ((1, SPECIALISTS), (2, ("analyst",))):
        parts = {a: by_agent[a] for a in agents}
        rounds[rnd] = {k: sum(v[k] for v in parts.values()) for k in ("requests", "input", "output", "cost")}
        rounds[rnd]["by_agent"] = parts
    retries = {}
    for a in AGENTS:
        n = by_agent[a]["requests"]
        calls = round(RETRY_SHARE_BY_AGENT[a] * n)
        r_in = round(RETRY_INPUT_FACTOR * by_agent[a]["input"] * calls / n) if n else 0
        r_out = EST_OUTPUT_TOKENS_BY_AGENT[a] * calls
        retries[a] = {"calls": calls, "input": r_in, "output": r_out, "cost": cost_usd(model, r_in, r_out)}
    batch = sum(r["cost"] for r in rounds.values())
    retry_cost = sum(r["cost"] for r in retries.values())
    return {"rounds": rounds, "retries": retries, "input": sum(r["input"] for r in rounds.values()),
            "output": sum(r["output"] for r in rounds.values()), "cost": batch, "retry_cost": retry_cost,
            "total": batch + retry_cost}


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


class ResumeError(RuntimeError):
    """`--resume` cannot continue from the saved state (nothing was changed)."""


class RunStopped(Exception):
    """Raised from `_before_call` / `_round_boundary` to stop the run cleanly (spending limit, spec 6.1).
    It propagates out of `run_showcase`; everything finished is already saved. `spent` and `limit` are USD."""

    def __init__(self, message: str, spent: float = 0.0, limit: float | None = None) -> None:
        super().__init__(message)
        self.spent, self.limit = spent, limit


def _zero_spend() -> dict:
    return {"batch": 0.0, "direct": 0.0, "input": 0, "output": 0}


class _Run:
    """One showcase run: the two rounds, the saved progress and the report numbers.

    Saved next to the report: `<report>.state.json` (batch ids per round, spend per round, per-agent
    status) and `<report>.progress/` (round results as collected, each agent's checked result and trace,
    each finished bank's report entry). Resume reads these and redoes nothing that is saved.
    """

    def __init__(self, ctx, client, model, out_dir, report_path, poll_seconds, banks, replay_dir, trace_dir,
                 state: dict, max_cost: float | None = None) -> None:
        self.ctx, self.client, self.model = ctx, client, model
        self.max_cost = max_cost
        self.out_dir, self.report_path, self.poll_seconds = out_dir, report_path, poll_seconds
        self.banks, self.replay_dir, self.trace_dir = banks, replay_dir, trace_dir
        self.state = state
        self.progress = Path(report_path).with_suffix(".progress")
        self.entries: dict[str, dict] = {}
        self.unfinished: set[str] = set()  # banks with an agent that raised: reported, but redone on resume
        self._mem: dict[tuple[str, str], tuple] = {}  # results not saved to disk (the agent raised)
        self._live: list = []
        self._todo2: list = []
        self._spec_ok: dict = {}
        self._cur_tokens: dict[str, int] = {}  # agent -> input tokens of the request now being run
        self._cur_trace: list | None = None  # trace of the agent now being run (its direct spend so far)

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
        if (base, agent) in self._mem:
            return self._mem[(base, agent)]
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
            if requests and not any(r["custom_id"] in collected for r in requests):
                raise ResumeError(f"batch {batch_id} has none of the {len(requests)} round {rnd} requests; "
                                  "it is not this run's batch (no calls were made)")
            self._write_file(f"round{rnd}_batch", collected)
        if not self.state.get(f"round{rnd}_collected"):
            sp = self._spend(rnd)
            for e in collected.values():
                sp["batch"] += e.get("cost", 0.0)
                sp["input"] += e.get("in", 0)
                sp["output"] += e.get("out", 0)
            self.state[f"round{rnd}_collected"] = True
            self.state[f"round{rnd}_requests"] = len(collected)
            self.save()
        return collected

    # -- one agent --------------------------------------------------------------------------
    def _run_agent(self, rnd: int, base: str, sheet, agent: str, first: dict | None,
                   specialist_memos: dict | None = None) -> AgentResult:
        """Check one agent's batch result (or make its first call directly), retry once at full price,
        and save the outcome. This is the one place a full-price call can start (spending-limit check
        point); the round boundary is `_round_boundary`."""
        trace: list = []
        raised = False
        memo = first.get("memo") if first else None
        self._cur_trace = trace
        if self.max_cost is not None:  # size the call the limit check may have to price
            self._cur_tokens[agent] = request_tokens(build_agent_request(sheet, agent, self.model,
                                                                         specialist_memos))
        try:
            res = run_agent(sheet, agent, client=self.client, model=self.model, specialist_memos=specialist_memos,
                            first_memo=memo, trace=trace, before_call=self._before_call)
        except RunStopped as exc:
            sp = self._spend(rnd)  # calls made before the stop were paid for
            u = _usage_of(exc)
            sp["direct"] += u.get("cost_usd", 0.0)
            sp["input"] += u.get("input_tokens", 0)
            sp["output"] += u.get("output_tokens", 0)
            self.save()
            raise
        except Exception as exc:  # one agent must never abort the run or lose the report
            # A model-side final error (refusal, cut off, unparseable) is final: saved as failed below, and
            # resume does not pay for it again. Anything else (transport, unexpected) stays resumable.
            raised = not isinstance(exc, (RefusalError, TruncatedError, ValueError))
            u = _usage_of(exc)  # calls made before the exception still cost money
            errors = [f"{type(exc).__name__}: {exc}"]
            if first and first.get("why"):
                errors.insert(0, first["why"])
            res = AgentResult(agent, ok=False, attempts=max(1, len(trace)), errors=errors,
                              input_tokens=u.get("input_tokens", 0), output_tokens=u.get("output_tokens", 0),
                              cost_usd=u.get("cost_usd", 0.0), served_model=u.get("model"))
            log.warning("showcase: %s %s failed: %s", base, agent, exc)
        finally:
            self._cur_trace = None
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
        source = "batch" if memo is not None else "direct"
        self.state.setdefault("agents", {}).setdefault(base, {})[agent] = {
            "ok": res.ok, "spend": batch_cost + res.cost_usd}
        self.save()  # spend first: a crash before the progress file means the agent is redone, and repaid
        if raised:
            # Not saved as finished: resume tries this agent again (at most one repeated call).
            self._mem[(base, agent)] = (res, trace, source)
            self.unfinished.add(base)
        else:
            self._write_file(f"{base}-{agent}", {"result": asdict(res), "trace": trace, "source": source})
        return res

    # -- spending limit (spec 6.1) ----------------------------------------------------------
    def spent(self) -> float:
        """Everything paid so far: batch (half price) and direct (full price) spend of every round."""
        return sum(v["batch"] + v["direct"] for v in self.state["spend"].values())

    def _stop(self, why: str, spent: float) -> RunStopped:
        return RunStopped(f"stopped at spending limit (${spent:.2f} spent of ${self.max_cost:.2f}): {why}",
                          spent=spent, limit=self.max_cost)

    def _round2_projection(self) -> tuple[float, float]:
        """(batch cost, retry allowance) projected for round 2, in USD.

        Batch cost = round 1's actual batch spend per request, times the number of analyst requests, times
        the analyst/specialist ratio: the estimated cost of an average analyst request (its real size,
        EST_OUTPUT_TOKENS_BY_AGENT output) over that of an average specialist request, both at the same
        price basis. Retry allowance = RETRY_SHARE_BY_AGENT["analyst"] of the analyst calls, each resending
        RETRY_INPUT_FACTOR x its request, at full price."""
        n2 = len(self._todo2)
        r1 = self.state["spend"].get("round1") or _zero_spend()
        n1 = self.state.get("round1_requests") or 0
        per_request = r1["batch"] / n1 if n1 else 0.0
        spec = [cost_usd(self.model, request_tokens(build_agent_request(b[4], a, self.model)),
                         EST_OUTPUT_TOKENS_BY_AGENT[a])
                for b in self._live for a in SPECIALISTS if a in self._requested[b[3]]]
        an_in = [request_tokens(build_agent_request(b[4], "analyst", self.model, self._spec_ok[b[3]]))
                 for b in self._todo2]
        avg_in = sum(an_in) / len(an_in) if an_in else 0.0
        analyst = cost_usd(self.model, avg_in, EST_OUTPUT_TOKENS_BY_AGENT["analyst"])
        ratio = analyst / (sum(spec) / len(spec)) if spec else 1.0
        retries = round(RETRY_SHARE_BY_AGENT["analyst"] * n2)
        retry = retries * cost_usd(self.model, RETRY_INPUT_FACTOR * avg_in, EST_OUTPUT_TOKENS_BY_AGENT["analyst"])
        return per_request * ratio * n2, retry

    def _round_boundary(self, rnd: int) -> None:
        """Called only before a round's batch is created (never for one already paid for). Checks the
        spending limit before round 2: spent + projected round 2 (batch + retry allowance) over the limit
        stops the run. Round 1 is not checked (nothing to project from; the limit guards what follows)."""
        if self.max_cost is None or rnd != 2:
            return
        spent = self.spent()
        batch, retry = self._round2_projection()
        if spent + batch + retry > self.max_cost:
            raise self._stop(f"round 2 is projected at ${batch:.2f} batch + ${retry:.2f} retry allowance, "
                             f"total ${spent + batch + retry:.2f}", spent)

    def _before_call(self, agent: str, attempt: int) -> None:
        """Called immediately before every full-price (direct) call. Stops the run if spent so far, plus
        this agent's direct spend not yet recorded, plus this call's estimated cost, is over the limit."""
        if self.max_cost is None:
            return
        spent = self.spent() + sum(t.get("cost_usd", 0.0) for t in (self._cur_trace or ())
                                   if t.get("source") == "direct")
        tokens = self._cur_tokens.get(agent, 0) * (1 if attempt == 1 else RETRY_INPUT_FACTOR)
        est = cost_usd(self.model, tokens, EST_OUTPUT_TOKENS_BY_AGENT[agent])
        if spent + est > self.max_cost:
            raise self._stop(f"the {agent} call (try {attempt}) is estimated at ${est:.2f} full price", spent)

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
                             replay_dir=self.replay_dir, trace_dir=self.trace_dir, prior=prior, prior_trace=trace,
                             before_call=self._before_call)
        except RunStopped:
            raise
        except Exception as exc:
            entry["errors"].append(f"{type(exc).__name__}: {exc}")
            log.warning("showcase: cert %s failed: %s", cert, exc)
        else:
            entry.update(ok=res.ok, path=str(res.path) if res.path else None)
        if not any((base, a) in self._mem for a in AGENTS):
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

        self._live = live
        # Round 1: trend and peer requests (a code-only specialist has none).
        todo = [(b, a) for b in live for a in SPECIALISTS if a in self._requested[b[3]]
                and self._load_agent(b[3], a) is None]
        if todo:
            if not self.state.get("round1_batch_id"):
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
        self._todo2, self._spec_ok = todo2, spec_ok
        if todo2:
            if not self.state.get("round2_batch_id"):
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
                 resume: str | None = None, trace_dir: Path = Path("data/analyst/traces"),
                 max_cost: float | None = None) -> dict:
    """Run the showcase in two batch rounds. With `resume=BATCH_ID` (either round's id), no finished round
    is created or paid again: saved results are reused, a batch that exists is polled and collected (the bank
    list and model come from the state file when it names that batch). The report is always written,
    partial if something escapes."""
    state = read_state(report_path) if resume is not None else None
    if resume is not None:
        if state is None:
            raise ResumeError(f"--resume {resume}: no state file at {state_path(report_path)}; nothing changed")
        ids = {state.get(k) for k in ("batch_id", "round1_batch_id", "round2_batch_id")} - {None}
        if resume not in ids:
            raise ResumeError(f"--resume {resume}: the state file names {sorted(ids)}; nothing changed")
        if state.get("complete") or not state.get("round1_batch_id"):
            raise ResumeError(f"--resume {resume}: that state is complete or from the old single-batch run "
                              "(no round1_batch_id); it cannot be resumed. Delete the state file to start a new run")
        banks = [(int(c), date.fromisoformat(d), g) for c, d, g in state["banks"]]
        model = state.get("model", model)
        state.setdefault("spend", {})
        state.pop("stopped", None)  # a resumed run starts un-stopped (it may be stopped again)
    else:
        state = {"batch_id": None, "round1_batch_id": None, "round2_batch_id": None, "spend": {},
                 "created_at": datetime.now().isoformat(timespec="seconds"), "model": model, "complete": False}
        banks = banks if banks is not None else showcase_banks(ctx, model_dir, replay_dir)
        state["banks"] = [[c, d.isoformat(), g] for c, d, g in banks]
        shutil.rmtree(Path(report_path).with_suffix(".progress"), ignore_errors=True)  # nothing stale carries over
    run = _Run(ctx, client, model, out_dir, report_path, poll_seconds, banks, replay_dir, trace_dir, state,
                 max_cost=max_cost)
    error = None
    stopped = False
    try:
        run.run()
        # Only now are both rounds fully used: results collected and every bank written or retried.
        if state.get("round1_batch_id"):
            state["complete"] = not run.unfinished
            run.save()
    except RunStopped:
        stopped = True
        state["stopped"] = "spending limit"
        state["complete"] = False
        run.save()
        raise
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
            "complete": error is None and not stopped and not run.unfinished,
            "stopped": "spending limit" if stopped else None,
            "max_cost": max_cost,
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
