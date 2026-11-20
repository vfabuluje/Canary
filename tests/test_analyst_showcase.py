import json
from datetime import date
from types import SimpleNamespace

import pandas as pd
import pytest

from analyst_fakes import FakeClient, fake_agent_memo, fake_message
from canary.analyst import __main__ as cli
from canary.analyst.facts import build_fact_sheet
from canary.analyst.sections import all_sections
from canary.analyst.showcase import run_showcase, showcase_banks
from canary.analyst.writer import PRICES, RefusalError, TruncatedError, cost_usd



@pytest.fixture
def tmp_model_dir(tmp_path):
    d = tmp_path / "mdir"
    d.mkdir()
    (d / "metrics.json").write_text(json.dumps({"caught_certs": [3, 24735]}))
    return d


@pytest.fixture
def tmp_replay_dir(analyst_ctx, tmp_path):
    d = tmp_path / "rdir"
    d.mkdir()
    s = analyst_ctx.scored
    old_cert = 110  # force: flagged once in the past, not at the latest quarter
    rows = s[s["cert"] == old_cert].index
    s.loc[rows, "flagged"] = False
    s.loc[rows[-5], "flagged"] = True
    pd.DataFrame({"cert": [24735, 57053, 59017, 2], "report_date": ["2022-12-31"] * 4}).to_csv(
        d / "test_misses.csv", index=False)
    latest = s[(s["report_date"] == pd.Timestamp(analyst_ctx.latest_quarter)) & s["flagged"].astype(bool)]
    wl = int(latest["cert"].iloc[0])
    pd.DataFrame({"cert": [old_cert, wl, 101], "institution_name": "X", "quarters_flagged": 5}).to_csv(
        d / "top_false_alarm_banks.csv", index=False)
    return SimpleNamespace(path=d, old_cert=old_cert, wl=wl)


def _mark_after_window(ctx, cert=101):
    ctx.banks.loc[ctx.banks["cert"] == cert, "failure_date"] = pd.Timestamp("2026-09-30")
    idx = ctx.scored[ctx.scored["cert"] == cert].index[-1]
    ctx.scored.loc[idx, "quarters_until_failure"] = 1


def test_groups_and_dedup(analyst_ctx, tmp_model_dir, tmp_replay_dir):
    _mark_after_window(analyst_ctx)
    out = showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path)
    groups = {c: g for c, _, g in out}
    assert len(groups) == len(out)  # each cert once
    assert [groups[c] for c in (24735, 57053, 59017)] == ["case_study"] * 3
    assert groups[2] == "test_miss" and groups[3] == "test_catch"
    assert groups[101] == "after_window"
    latest = analyst_ctx.scored[(analyst_ctx.scored["report_date"] == pd.Timestamp(analyst_ctx.latest_quarter))
                                & analyst_ctx.scored["flagged"].astype(bool)]["cert"]
    for c in latest:
        assert groups[int(c)] in ("latest_watchlist", "after_window", "test_catch", "test_miss", "case_study")
    assert groups[tmp_replay_dir.wl] == "latest_watchlist"
    assert groups[tmp_replay_dir.old_cert] == "false_alarm"
    as_of = {c: d for c, d, _ in out}
    assert as_of[3] < date(2019, 12, 31) and as_of[101] == analyst_ctx.latest_quarter


def test_past_false_alarm_on_latest_watchlist_uses_latest(analyst_ctx, tmp_model_dir, tmp_replay_dir):
    out = {c: (d, g) for c, d, g in showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path)}
    d, g = out[tmp_replay_dir.wl]
    assert d == analyst_ctx.latest_quarter and g == "latest_watchlist"
    d, g = out[tmp_replay_dir.old_cert]
    s = analyst_ctx.scored
    last_flag = s[(s["cert"] == tmp_replay_dir.old_cert) & s["flagged"].astype(bool)]["report_date"].max()
    assert g == "false_alarm" and d == last_flag.date()


def _flag_latest(ctx, n=6):
    """Flag n more banks at the latest quarter, so the watchlist has several banks."""
    s = ctx.scored
    at = s["report_date"] == pd.Timestamp(ctx.latest_quarter)
    s.loc[at & s["cert"].isin(s.loc[at, "cert"].astype(int).head(n + 3)), "flagged"] = True


def _watchlist_ranked(ctx):
    s = ctx.scored
    now = s[(s["report_date"] == pd.Timestamp(ctx.latest_quarter)) & s["flagged"].astype(bool)]
    return now.sort_values("rank")["cert"].astype(int).tolist()


def test_watchlist_top_keeps_best_ranked(analyst_ctx, tmp_model_dir, tmp_replay_dir):
    _flag_latest(analyst_ctx)
    ranked = _watchlist_ranked(analyst_ctx)
    full = showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path)
    claimed = {c for c, _, g in full if g != "latest_watchlist" and c in ranked}
    free = [c for c in ranked if c not in claimed]
    assert len(free) > 2
    out = showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path, watchlist_top=2)
    wl = [c for c, _, g in out if g == "latest_watchlist"]
    assert wl == free[:2]


def test_watchlist_top_none_is_unchanged(analyst_ctx, tmp_model_dir, tmp_replay_dir):
    assert (showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path, watchlist_top=None)
            == showcase_banks(analyst_ctx, tmp_model_dir, tmp_replay_dir.path))


def test_cli_watchlist_top_dry_run(analyst_ctx, tmp_model_dir, tmp_replay_dir, capsys, monkeypatch):
    _flag_latest(analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: pytest.fail("client constructed"))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    rc = cli.main(["showcase", "--dry-run", "--watchlist-top", "2", "--model-dir", str(tmp_model_dir),
                   "--replay-dir", str(tmp_replay_dir.path)])
    out = capsys.readouterr().out
    assert rc == 0 and out.count("\tlatest_watchlist") == 2


def test_estimate_constants_and_calibration():
    from canary.analyst import showcase
    assert showcase.EST_OUTPUT_TOKENS_BY_AGENT == {"trend": 2400, "peer": 2400, "analyst": 5000}
    assert showcase.EST_ANALYST_SPECIALIST_CHARS == 2600
    assert showcase.RETRY_SHARE_BY_AGENT == {"trend": 0.16, "peer": 0.16, "analyst": 0.30}
    assert showcase.CHARS_PER_TOKEN == 2.4 and showcase.RETRY_INPUT_FACTOR == 2.0
    assert not hasattr(showcase, "EST_INPUT_TOKENS") and not hasattr(showcase, "EST_OUTPUT_TOKENS")
    # the SVB request (22,979 chars) maps to about 9,570 input tokens
    assert showcase.request_tokens({"x": "a" * (22979 - 8)}) == round(22979 / 2.4)


def test_estimate_run_per_round_and_call_type(analyst_ctx, tmp_replay_dir):
    from canary.analyst import showcase
    from canary.analyst.writer import cost_usd
    from canary.analyst.pipeline import agent_sections
    banks = [(100, date(2026, 6, 30), "x")] * 2
    est = showcase.estimate_run(analyst_ctx, banks, "claude-opus-5-5", tmp_replay_dir.path)
    sheet = build_fact_sheet(analyst_ctx, 100, date(2026, 6, 30), replay_dir=tmp_replay_dir.path)
    n_spec = 2 * sum(bool(agent_sections(sheet, a)) for a in ("trend", "peer"))
    r1, r2 = est["rounds"][1], est["rounds"][2]
    assert set(r1["by_agent"]) == {"trend", "peer"} and set(r2["by_agent"]) == {"analyst"}
    assert r1["requests"] == n_spec and r2["requests"] == 2
    assert r1["output"] == n_spec * 2400 and r2["output"] == 2 * 5000
    assert r1["cost"] == pytest.approx(cost_usd("claude-opus-5-5", r1["input"], r1["output"]) / 2)
    assert r2["cost"] == pytest.approx(cost_usd("claude-opus-5-5", r2["input"], r2["output"]) / 2)
    # the analyst request carries placeholder specialist text, so it is larger than a specialist request
    assert r2["input"] / 2 > r1["input"] / max(n_spec, 1)
    ret = est["retries"]
    assert {a: ret[a]["calls"] for a in ret} == {"trend": 0, "peer": 0, "analyst": 1}  # round(0.16 * 2), round(0.30 * 2)
    assert est["total"] == pytest.approx(r1["cost"] + r2["cost"] + est["retry_cost"])


def test_estimate_run_retry_allowance_per_agent(analyst_ctx, tmp_replay_dir):
    from canary.analyst import showcase
    from canary.analyst.writer import cost_usd
    banks = [(100, date(2026, 6, 30), "x")] * 25
    est = showcase.estimate_run(analyst_ctx, banks, "claude-opus-5-5", tmp_replay_dir.path)
    for agent, rnd in (("trend", 1), ("peer", 1), ("analyst", 2)):
        a = est["rounds"][rnd]["by_agent"][agent]
        r = est["retries"][agent]
        if not a["requests"]:  # a code-only specialist for this bank
            assert r["calls"] == 0
            continue
        assert a["requests"] == 25 and r["calls"] == round(showcase.RETRY_SHARE_BY_AGENT[agent] * 25)
        assert r["output"] == r["calls"] * showcase.EST_OUTPUT_TOKENS_BY_AGENT[agent]
        assert r["input"] == round(2.0 * a["input"] / 25 * r["calls"])
        assert r["cost"] == pytest.approx(cost_usd("claude-opus-5-5", r["input"], r["output"]))
    assert est["retry_cost"] == pytest.approx(sum(r["cost"] for r in est["retries"].values()))


def test_dry_run_prints_rounds_and_total(analyst_ctx, tmp_model_dir, tmp_replay_dir, capsys, monkeypatch):
    monkeypatch.setattr(cli, "make_client", lambda: pytest.fail("client constructed"))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    rc = cli.main(["showcase", "--dry-run", "--model-dir", str(tmp_model_dir),
                   "--replay-dir", str(tmp_replay_dir.path)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "round 1" in out and "round 2" in out and "estimated total with retries" in out
    for agent in ("trend", "peer", "analyst"):
        assert f"retry allowance ({agent})" in out
    rc = cli.main(["showcase", "--dry-run", "--max-cost", "0.01", "--model-dir", str(tmp_model_dir),
                   "--replay-dir", str(tmp_replay_dir.path)])
    assert rc == 0 and "spending limit $0.01" in capsys.readouterr().out


# ---- batch run (two rounds) -------------------------------------------------------------

BANKS = [(100, date(2026, 6, 30), "latest_watchlist"), (101, date(2026, 6, 30), "latest_watchlist"),
         (102, date(2026, 6, 30), "latest_watchlist"), (103, date(2026, 6, 30), "latest_watchlist")]
CERTS = (100, 101, 102, 103)
AS_OF = date(2026, 6, 30)
FULL = cost_usd("claude-opus-5-5", 1000, 500)  # one fake call's usage at full price


def _sheet(ctx, tmp_path, cert):
    return build_fact_sheet(ctx, cert, AS_OF, replay_dir=tmp_path / "none")


def _agents_for(ctx, tmp_path, cert):
    """Agents with a request for this bank, in call order (a code-only specialist has none)."""
    from canary.analyst.pipeline import AGENTS, agent_sections

    sheet = _sheet(ctx, tmp_path, cert)
    return [a for a in AGENTS if agent_sections(sheet, a)]


def _agent_of(kw) -> str:
    text = kw["messages"][0]["content"]
    if "Sections written by other agents" in text:
        return "analyst"
    return "trend" if "- trends (" in text else "peer"


class BatchClient(FakeClient):
    """FakeClient plus messages.batches for two rounds.

    `outcomes` maps cert -> 'ok'|'errored'|'expired'|'refusal'|'bad'; `agent_outcomes` maps (cert, agent) to
    the same and wins. Direct (retry) calls answer from `direct[(cert, agent)]` (a list, popped), else with a
    good memo for that agent. Batch ids are batch_<first_id>, batch_<first_id + 1>, ...
    """

    def __init__(self, ctx, tmp_path, outcomes=None, direct=None, polls=2, agent_outcomes=None, first_id=1):
        super().__init__([])
        self.ctx, self.tmp_path, self.polls = ctx, tmp_path, polls
        self.outcomes = outcomes if outcomes is not None else {c: "ok" for c in CERTS}
        self.agent_outcomes = agent_outcomes or {}
        self.direct = {k: list(v) for k, v in (direct or {}).items()}
        self.first_id = first_id
        self.created, self.events, self.result_calls = [], [], []
        self.polled: dict[str, int] = {}
        self.beta.messages.create = self._direct
        self.messages = SimpleNamespace(batches=SimpleNamespace(
            create=self._create, retrieve=self._retrieve, results=self._results))

    def _bid(self, index):
        return f"batch_{self.first_id + index}"

    def _create(self, requests):
        self.created.append(requests)
        bid = self._bid(len(self.created) - 1)
        self.events.append(("create", bid))
        return SimpleNamespace(id=bid, processing_status="in_progress")

    def _retrieve(self, batch_id):
        self.polled[batch_id] = self.polled.get(batch_id, 0) + 1
        ended = self.polled[batch_id] >= self.polls
        if ended and ("ended", batch_id) not in self.events:
            self.events.append(("ended", batch_id))
        return SimpleNamespace(id=batch_id, processing_status="ended" if ended else "in_progress")

    def _direct(self, **kw):
        self.calls.append(kw)
        cert = int(kw["messages"][0]["content"].split("(cert ")[1].split(")")[0])
        agent = _agent_of(kw)
        queue = self.direct.get((cert, agent))
        item = queue.pop(0) if queue else fake_agent_memo(_sheet(self.ctx, self.tmp_path, cert), agent)
        if isinstance(item, BaseException):
            raise item
        msg = fake_message(json.dumps(item))
        msg.model = kw["model"]
        return msg

    def _results(self, batch_id):
        self.result_calls.append(batch_id)
        out = []
        for req in reversed(self.created[int(batch_id.split("_")[1]) - self.first_id]):  # any order
            cert, _, agent = req["custom_id"].split("-")
            kind = self.agent_outcomes.get((int(cert), agent), self.outcomes[int(cert)])
            model = req["params"]["model"]
            if kind == "ok":
                memo = fake_agent_memo(_sheet(self.ctx, self.tmp_path, int(cert)), agent)
                res = SimpleNamespace(type="succeeded", message=fake_message(json.dumps(memo), model=model))
            elif kind == "refusal":
                res = SimpleNamespace(type="succeeded", message=fake_message("", stop_reason="refusal", model=model))
            elif kind == "bad":
                res = SimpleNamespace(type="succeeded", message=fake_message(json.dumps({"sections": []}), model=model))
            else:
                res = SimpleNamespace(type=kind)
            out.append(SimpleNamespace(custom_id=req["custom_id"], result=res))
        return iter(out)


def _batch_cost(client) -> float:
    """Half price for every batch request whose result carried usage (the fake sends 1000/500 for those)."""
    n = 0
    for index, reqs in enumerate(client.created):
        for r in reqs:
            cert, _, agent = r["custom_id"].split("-")
            if client.agent_outcomes.get((int(cert), agent), client.outcomes[int(cert)]) in ("ok", "refusal", "bad"):
                n += 1
    return n * FULL / 2


def _run(ctx, tmp_path, client, banks=BANKS, **kw):
    kw.setdefault("trace_dir", tmp_path / "traces")
    return run_showcase(ctx, client, "claude-opus-5-5", tmp_path / "banks", tmp_path / "report.json",
                        poll_seconds=0, banks=banks, replay_dir=tmp_path / "none", **kw)


def test_two_rounds_created(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path)
    rep = _run(analyst_ctx, tmp_path, client)
    assert len(client.created) == 2
    r1 = {r["custom_id"] for r in client.created[0]}
    r2 = {r["custom_id"] for r in client.created[1]}
    want1 = {f"{c}-20260630-{a}" for c in CERTS for a in _agents_for(analyst_ctx, tmp_path, c) if a != "analyst"}
    assert r1 == want1 and r2 == {f"{c}-20260630-analyst" for c in CERTS}
    # round 2 was created only after round 1 ended
    assert client.events.index(("ended", "batch_1")) < client.events.index(("create", "batch_2"))
    # analyst requests carry the checked specialist text; no batch request sets fallbacks
    for r in client.created[1]:
        text = r["params"]["messages"][0]["content"]
        assert "Trend agent's section (checked, do not rewrite)" in text or "trends" in _sheet(
            analyst_ctx, tmp_path, int(r["custom_id"].split("-")[0])).code_only
    assert any("The trends section reads calmly." in r["params"]["messages"][0]["content"]
               for r in client.created[1])
    assert all("fallbacks" not in r["params"] for rd in client.created for r in rd)
    # no direct call, every call at half price, nothing counted twice
    assert client.calls == []
    assert rep["written"] == 4 and rep["failed"] == 0 and len(list((tmp_path / "banks").glob("*.md"))) == 4
    n = len(r1) + len(r2)
    assert rep["cost_usd"] == pytest.approx(n * FULL / 2)
    assert rep["input_tokens"] == 1000 * n and rep["output_tokens"] == 500 * n


def test_specialist_failure_excludes_bank_from_round2(analyst_ctx, tmp_path):
    bad = {"sections": []}
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "trend"): "bad"},
                         direct={(101, "trend"): [bad]})
    rep = _run(analyst_ctx, tmp_path, client)
    assert not any(r["custom_id"].startswith("101-") for r in client.created[1])
    assert len(client.created[1]) == 3
    assert len(client.calls) == 1  # the one retry of 101's trend; no analyst call for 101
    by = {b["cert"]: b for b in rep["banks"]}
    assert not by[101]["ok"] and by[101]["agents"]["trend"]["ok"] is False
    assert by[101]["agents"]["analyst"]["attempts"] == 0 and by[101]["path"] is None
    assert any("[trend]" in e for e in by[101]["errors"])
    assert rep["written"] == 3 and rep["failed"] == 1
    assert (tmp_path / "traces" / "101_2026-06-30.json").exists()
    assert len(list((tmp_path / "banks").glob("*.md"))) == 3


def test_retries_are_direct_calls(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad", (101, "analyst"): "bad"})
    rep = _run(analyst_ctx, tmp_path, client)
    assert len(client.calls) == 2  # one retry per failed first try, both direct with fallbacks
    assert all(c.get("fallbacks") == "default" for c in client.calls)
    assert all(len(c["messages"]) == 3 for c in client.calls)  # the request, the rejected memo, the errors
    assert rep["written"] == 4
    # retries at full price, batch first tries at half; the retry replaces nothing already counted
    assert rep["cost_usd"] == pytest.approx(_batch_cost(client) + 2 * FULL)
    assert rep["spend_by_round"]["round1"]["direct"] == pytest.approx(FULL)
    assert rep["spend_by_round"]["round2"]["direct"] == pytest.approx(FULL)


def test_report_per_agent(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad", (101, "analyst"): "bad",
                                                                (102, "peer"): "errored"})
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert set(by[100]["agents"]) == {"trend", "peer", "analyst"}
    t = by[100]["agents"]["trend"]
    assert t["ok"] and t["attempts"] == 2 and t["first_errors"] and t["source"] == "batch"
    a = by[101]["agents"]["analyst"]
    assert a["ok"] and a["attempts"] == 2 and a["first_errors"] and "missing section" in a["first_errors"][0]
    if "peer" in _agents_for(analyst_ctx, tmp_path, 102):
        p = by[102]["agents"]["peer"]
        assert p["ok"] and p["attempts"] == 1 and p["first_errors"] == [] and p["source"] == "direct"
    assert by[103]["agents"]["analyst"] == {"ok": True, "attempts": 1, "first_errors": [], "source": "batch"}
    tally = rep["first_try_passed_by_agent"]
    assert set(tally) == {"trend", "peer", "analyst"}
    n_trend = sum("trend" in _agents_for(analyst_ctx, tmp_path, c) for c in CERTS)
    assert tally["trend"] == n_trend - 1 and tally["analyst"] == 3
    assert rep["first_error_sections"]["trends"] >= 1 and rep["first_error_sections"]["summary"] >= 1
    assert set(rep["spend_by_round"]) == {"round1", "round2"}
    assert rep["cost_usd"] == pytest.approx(sum(v["total"] for v in rep["spend_by_round"].values()))


def _break_round2_results(client):
    """Round 2's results download breaks (after round 1 is done and round 2 is created)."""
    real = client._results

    def results(bid):
        if bid == "batch_2":
            raise RuntimeError("results download broke")
        return real(bid)

    client.messages.batches.results = results
    return real


def test_resume_after_round1(analyst_ctx, tmp_path):
    first = BatchClient(analyst_ctx, tmp_path)
    real_create = first.messages.batches.create

    def create(requests):
        if first.created:
            raise RuntimeError("round 2 create broke")
        return real_create(requests)

    first.messages.batches.create = create
    with pytest.raises(RuntimeError):
        _run(analyst_ctx, tmp_path, first)
    st = json.loads((tmp_path / "report.state.json").read_text())
    assert st["round1_batch_id"] == "batch_1" and st.get("round2_batch_id") is None and st["complete"] is False
    spent_round1 = json.loads((tmp_path / "report.json").read_text())["cost_usd"]
    assert spent_round1 == pytest.approx(len(first.created[0]) * FULL / 2)

    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    real2 = second._results
    second.messages.batches.results = lambda bid: real2(bid) if bid == "batch_2" else pytest.fail("round 1 refetched")
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert len(second.created) == 1  # only round 2 was submitted
    assert {r["custom_id"].rsplit("-", 1)[1] for r in second.created[0]} == {"analyst"}
    assert second.result_calls == ["batch_2"]
    assert rep["written"] == 4 and rep["complete"] and rep["round1_batch_id"] == "batch_1"
    assert rep["round2_batch_id"] == "batch_2"
    # round 1 spend carried over once, round 2 added: nothing paid or counted twice
    assert rep["cost_usd"] == pytest.approx((len(first.created[0]) + len(second.created[0])) * FULL / 2)
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is True


def test_resume_mid_round2(analyst_ctx, tmp_path):
    first = BatchClient(analyst_ctx, tmp_path)
    real = _break_round2_results(first)
    with pytest.raises(RuntimeError):
        _run(analyst_ctx, tmp_path, first)
    st = json.loads((tmp_path / "report.state.json").read_text())
    assert st["round1_batch_id"] == "batch_1" and st["round2_batch_id"] == "batch_2"
    assert not list((tmp_path / "banks").glob("*.md"))

    second = BatchClient(analyst_ctx, tmp_path)
    second.created = first.created  # the batches exist on the server
    second.messages.batches.create = lambda **kw: pytest.fail("a batch was created on resume")
    second.messages.batches.results = lambda bid: real(bid) if bid == "batch_2" else pytest.fail("round 1 refetched")
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_2")  # either round's id resumes the run
    assert rep["written"] == 4 and rep["complete"]
    n = len(first.created[0]) + len(first.created[1])
    assert rep["cost_usd"] == pytest.approx(n * FULL / 2) and second.calls == []


def test_resume_skips_banks_already_written(analyst_ctx, tmp_path):
    first = BatchClient(analyst_ctx, tmp_path)
    import canary.analyst.showcase as showcase

    real_write = showcase.write_memo
    done = []

    def write_then_stop(ctx, cert, *a, **k):
        if len(done) == 2:
            raise KeyboardInterrupt
        done.append(cert)
        return real_write(ctx, cert, *a, **k)

    showcase.write_memo = write_then_stop
    try:
        with pytest.raises(KeyboardInterrupt):
            _run(analyst_ctx, tmp_path, first)
    finally:
        showcase.write_memo = real_write
    second = BatchClient(analyst_ctx, tmp_path)
    second.created = first.created
    second.messages.batches.create = lambda **kw: pytest.fail("a batch was created on resume")
    second.messages.batches.results = lambda bid: pytest.fail("results fetched again")
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert rep["written"] == 4 and len(rep["banks"]) == 4 and second.calls == []
    n = len(first.created[0]) + len(first.created[1])
    assert rep["cost_usd"] == pytest.approx(n * FULL / 2)


def test_partial_batch_failures_retried(analyst_ctx, tmp_path):
    outcomes = {100: "ok", 101: "errored", 102: "expired", 103: "refusal"}
    client = BatchClient(analyst_ctx, tmp_path, outcomes)
    rep = _run(analyst_ctx, tmp_path, client)
    assert len(client.created) == 2
    n_spec = sum(len(_agents_for(analyst_ctx, tmp_path, c)) - 1 for c in CERTS)
    assert len(client.created[0]) == n_spec and len(client.created[1]) == 4
    ids = {r["custom_id"] for r in client.created[0]} | {r["custom_id"] for r in client.created[1]}
    assert f"100-20260630-analyst" in ids and "103-20260630-trend" in ids
    # every failed batch result (errored, expired, refusal) is redone as a normal call with fallbacks
    expect = sum(len(_agents_for(analyst_ctx, tmp_path, c)) for c in (101, 102, 103))
    assert len(client.calls) == expect
    assert all(c.get("fallbacks") == "default" for c in client.calls)
    assert rep["written"] == 4 and rep["failed"] == 0
    assert len(list((tmp_path / "banks").glob("*.md"))) == 4
    assert json.loads((tmp_path / "report.json").read_text())["written"] == 4
    # cost: batch results that carried usage (ok, refusal) at half price, every redo at full price
    assert rep["cost_usd"] == pytest.approx(_batch_cost(client) + expect * FULL)


def test_still_failing_listed_in_report(analyst_ctx, tmp_path):
    from canary.analyst.writer import RefusalError

    bad = {"sections": []}
    # 101: bad analyst batch memo -> retry also bad; 102: analyst batch errored -> its direct call refuses
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "bad", (102, "analyst"): "errored"},
                         direct={(101, "analyst"): [bad], (102, "analyst"): [RefusalError("no")]})
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["written"] == 2 and rep["failed"] == 2
    failed = {b["cert"]: b for b in rep["banks"] if not b["ok"]}
    assert set(failed) == {101, 102}
    assert failed[101]["errors"] and "no" in " ".join(failed[102]["errors"])
    assert failed[101]["path"] is None and failed[102]["path"] is None
    assert json.loads((tmp_path / "report.json").read_text())["failed"] == 2


def test_dry_run_makes_no_calls(analyst_ctx, tmp_model_dir, tmp_replay_dir, capsys, monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "make_client", lambda: pytest.fail("client constructed"))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    rc = cli.main(["showcase", "--dry-run", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path)])
    out = capsys.readouterr().out
    assert rc == 0 and "banks" in out and "estimated cost" in out and "false_alarm" in out
    assert "retry allowance" in out and "estimated total with retries" in out


def test_unexpected_retry_error_does_not_abort_run(analyst_ctx, tmp_path):
    import anthropic

    err = anthropic.APIConnectionError(request=SimpleNamespace(method="POST", url="https://x"))
    ao = {(c, "analyst"): "errored" for c in (100, 101, 102)}
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes=ao,
                         direct={(100, "analyst"): [RuntimeError("boom")], (101, "analyst"): [err]})
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert len(by) == 4 and rep["written"] == 2 and rep["failed"] == 2
    assert not by[100]["ok"] and "RuntimeError" in " ".join(by[100]["errors"])
    assert not by[101]["ok"] and "APIConnectionError" in " ".join(by[101]["errors"])
    assert by[102]["ok"] and by[103]["ok"]
    assert json.loads((tmp_path / "report.json").read_text())["failed"] == 2


def test_missing_batch_result_is_retried(analyst_ctx, tmp_path):
    cert = next(c for c in CERTS if "trend" in _agents_for(analyst_ctx, tmp_path, c))
    client = BatchClient(analyst_ctx, tmp_path)
    orig = client._results
    client.messages.batches.results = lambda bid: iter(
        [r for r in orig(bid) if r.custom_id != f"{cert}-20260630-trend"])
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["written"] == 4 and len(rep["banks"]) == 4
    assert len(client.calls) == 1  # the missing round-1 result, redone directly
    by = {b["cert"]: b for b in rep["banks"]}
    assert by[cert]["source"] == "retry" and by[cert]["agents"]["trend"]["source"] == "direct"


# ---- final-review fixes ----------------------------------------------------------------

def test_state_file_written_with_batch_id(analyst_ctx, tmp_path):
    from canary.analyst.showcase import state_path

    client = BatchClient(analyst_ctx, tmp_path)
    rep = _run(analyst_ctx, tmp_path, client)
    st = json.loads(state_path(tmp_path / "report.json").read_text())
    assert state_path(tmp_path / "report.json") == tmp_path / "report.state.json"
    assert st["batch_id"] == "batch_1" == st["round1_batch_id"] and st["round2_batch_id"] == "batch_2"
    assert st["model"] == "claude-opus-5-5" and st["created_at"]
    assert st["banks"] == [[c, "2026-06-30", "latest_watchlist"] for c in CERTS]
    assert st["complete"] is True
    assert st["agents"]["100-20260630"]["analyst"]["ok"] is True
    assert rep["batch_id"] == "batch_1" and rep["complete"] is True
    assert rep["round1_batch_id"] == "batch_1" and rep["round2_batch_id"] == "batch_2"
    assert all(b["served_model"] == "claude-opus-5-5" for b in rep["banks"])


def test_resume_makes_no_create_call(analyst_ctx, tmp_path):
    """A hand-written state naming both rounds' batches: nothing is created, both are only collected."""
    client = BatchClient(analyst_ctx, tmp_path)
    specs = [(c, a) for c in CERTS for a in _agents_for(analyst_ctx, tmp_path, c) if a != "analyst"]
    client.created = [[{"custom_id": f"{c}-20260630-{a}", "params": {"model": "claude-sonnet-5-5"}} for c, a in specs],
                      [{"custom_id": f"{c}-20260630-analyst", "params": {"model": "claude-sonnet-5-5"}} for c in CERTS]]
    (tmp_path / "report.state.json").write_text(json.dumps({
        "batch_id": "batch_1", "round1_batch_id": "batch_1", "round2_batch_id": "batch_2",
        "created_at": "2026-11-17T10:00:00", "model": "claude-sonnet-5-5", "complete": False,
        "banks": [[c, "2026-06-30", "latest_watchlist"] for c in CERTS]}))
    create_calls = []
    client.messages.batches.create = lambda **kw: create_calls.append(kw)
    rep = run_showcase(analyst_ctx, client, "claude-opus-5-5", tmp_path / "banks", tmp_path / "report.json",
                       poll_seconds=0, replay_dir=tmp_path / "none", resume="batch_1",
                       trace_dir=tmp_path / "traces")
    assert create_calls == [] and sum(client.polled.values()) >= 2
    assert rep["written"] == 4 and rep["batch_id"] == "batch_1" and rep["model"] == "claude-sonnet-5-5"
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is True


def test_transient_retrieve_error_then_success(analyst_ctx, tmp_path, monkeypatch):
    import anthropic

    from analyst_fakes import api_status_error
    from canary.analyst import showcase

    sleeps = []
    monkeypatch.setattr(showcase.time, "sleep", lambda s: sleeps.append(s))
    client = BatchClient(analyst_ctx, tmp_path, polls=1)
    errs = [anthropic.APIConnectionError(request=SimpleNamespace(method="GET", url="https://x")),
            api_status_error("InternalServerError", 500)]
    real = client._retrieve

    def flaky(batch_id):
        if errs:
            raise errs.pop(0)
        return real(batch_id)

    client.messages.batches.retrieve = flaky
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["written"] == 4 and rep["complete"]
    assert sleeps[:2] == [showcase.RETRY_BASE_SECONDS, showcase.RETRY_BASE_SECONDS * 2]


def test_retrieve_gives_up_and_partial_report_written(analyst_ctx, tmp_path, monkeypatch):
    import anthropic

    from canary.analyst import showcase

    monkeypatch.setattr(showcase.time, "sleep", lambda s: None)
    client = BatchClient(analyst_ctx, tmp_path)
    calls = []

    def down(batch_id):
        calls.append(batch_id)
        raise anthropic.APIConnectionError(request=SimpleNamespace(method="GET", url="https://x"))

    client.messages.batches.retrieve = down
    with pytest.raises(anthropic.APIConnectionError):
        _run(analyst_ctx, tmp_path, client)
    assert len(calls) == showcase.RETRY_TRIES
    rep = json.loads((tmp_path / "report.json").read_text())
    assert rep["complete"] is False and rep["batch_id"] == "batch_1" and "APIConnectionError" in rep["error"]
    assert rep["banks_total"] == 4 and rep["banks_done"] == 0
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is False


def test_auth_error_not_retried(analyst_ctx, tmp_path, monkeypatch):
    from analyst_fakes import api_status_error
    from canary.analyst import showcase

    monkeypatch.setattr(showcase.time, "sleep", lambda s: pytest.fail("retried a non-transient error"))
    client = BatchClient(analyst_ctx, tmp_path)
    client.messages.batches.retrieve = lambda bid: (_ for _ in ()).throw(api_status_error("AuthenticationError", 401))
    with pytest.raises(Exception, match="api error"):
        _run(analyst_ctx, tmp_path, client)


def test_failed_retry_usage_counted(analyst_ctx, tmp_path):
    from canary.analyst.writer import RefusalError

    # 101's analyst batch memo is bad; its retry raises -> nothing extra to count
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "bad"},
                         direct={(101, "analyst"): [RefusalError("no")]})
    rep = _run(analyst_ctx, tmp_path, client)
    n = len(client.created[0]) + len(client.created[1])
    assert rep["input_tokens"] == 1000 * n
    # the bad retry memo's tokens survive a later failure: retry returns a bad memo (tokens counted)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "errored"},
                         direct={(101, "analyst"): [{"sections": []}, {"sections": []}]})
    rep = _run(analyst_ctx, tmp_path, client)
    n = len(client.created[0]) + len(client.created[1]) - 1  # the errored result had no usage
    assert rep["input_tokens"] == 1000 * n + 1000 * 2  # two direct analyst calls for 101 (first, retry)
    by = {b["cert"]: b for b in rep["banks"]}
    assert not by[101]["ok"] and by[101]["served_model"] == "claude-opus-5-5"


def test_cli_refuses_unfinished_batch_and_resumes(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch,
                                                  tmp_path, capsys):
    report = tmp_path / "rep.json"
    (tmp_path / "rep.state.json").write_text(json.dumps({"batch_id": "b9", "banks": [], "model": "m",
                                                        "complete": False, "created_at": "x"}))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: pytest.fail("client constructed"))
    args = ["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
            "--report", str(report)]
    assert cli.main(args) == 1
    assert "--resume b9" in capsys.readouterr().err
    seen = {}

    def fake_run(*a, **k):
        seen.update(k)
        return {"written": 0, "failed": 0, "banks_total": 0, "cost_usd": 0.0, "banks": []}

    monkeypatch.setattr("canary.analyst.showcase.run_showcase", fake_run)
    monkeypatch.setattr(cli, "make_client", lambda: object())
    assert cli.main(args + ["--resume", "b9"]) == 0
    assert seen["resume"] == "b9"


def test_cli_showcase_create_api_error_exits_1(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch,
                                               tmp_path, capsys):
    from analyst_fakes import api_status_error

    client = BatchClient(analyst_ctx, tmp_path, {})

    def create(requests):
        raise api_status_error("AuthenticationError", 401, "invalid x-api-key")

    client.messages.batches.create = create
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: client)
    report = tmp_path / "rep.json"
    rc = cli.main(["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
                   "--report", str(report), "--out", str(tmp_path / "banks")])
    assert rc == 1 and "Claude API call failed (AuthenticationError)" in capsys.readouterr().err
    assert json.loads(report.read_text())["complete"] is False


def test_failed_collection_blocks_plain_rerun_resume_works(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch,
                                                            tmp_path, capsys):
    """R15: state is complete only after every bank is processed; a plain rerun is refused until then."""
    from canary.analyst import showcase

    monkeypatch.setattr(showcase.time, "sleep", lambda s: None)
    banks = BANKS
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr("canary.analyst.showcase.showcase_banks", lambda *a, **k: banks)
    report = tmp_path / "rep.json"
    args = ["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
            "--report", str(report), "--out", str(tmp_path / "banks")]
    monkeypatch.setattr(cli, "REPLAY_DIR", tmp_path / "none")
    monkeypatch.chdir(tmp_path)  # the traces default to a relative path
    client = BatchClient(analyst_ctx, tmp_path)
    real_results = client._results

    def broken(batch_id):
        raise RuntimeError("results download broke")

    client.messages.batches.results = broken
    monkeypatch.setattr(cli, "make_client", lambda: client)
    with pytest.raises(RuntimeError):
        cli.main(args)
    st = json.loads((tmp_path / "rep.state.json").read_text())
    assert st["batch_id"] == "batch_1" and st["complete"] is False
    capsys.readouterr()
    assert cli.main(args) == 1  # plain rerun refused: no second paid batch
    assert "--resume batch_1" in capsys.readouterr().err and len(client.created) == 1
    client.messages.batches.results = real_results
    rc = cli.main(args + ["--resume", "batch_1"])
    assert len(client.created) == 2  # round 1 was not created again; only round 2 was
    assert json.loads((tmp_path / "rep.state.json").read_text())["complete"] is True
    assert json.loads(report.read_text())["complete"] is True and rc in (0, 1)
    assert cli.main(args + ["--dry-run"]) == 0


def test_interrupted_retry_loop_keeps_state_incomplete(analyst_ctx, tmp_path, monkeypatch):
    import canary.analyst.showcase as showcase

    calls = []

    def interrupt(*a, **k):
        calls.append(1)
        raise KeyboardInterrupt

    monkeypatch.setattr(showcase, "write_memo", interrupt)
    client = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(KeyboardInterrupt):
        _run(analyst_ctx, tmp_path, client)
    assert calls and json.loads((tmp_path / "report.state.json").read_text())["complete"] is False


def test_first_attempt_errors_recorded(analyst_ctx, tmp_path):
    """Why a first try failed is kept per bank, with a per-section tally, so retry rates can be explained."""
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "bad"})
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert by[100]["first_errors"] == []
    assert by[101]["first_errors"] and all("missing section" in e or "no text" in e for e in by[101]["first_errors"])
    assert all(e.startswith("[analyst]") for e in by[101]["first_errors"])
    assert rep["first_try_passed"] == sum(1 for b in rep["banks"] if b["ok"] and not b["first_errors"]) == 3
    assert rep["first_error_sections"]["summary"] >= 1


# ---- review fixes: resume safety, before_call hook, round boundary ----------------------

def _stop_after_round1(ctx, tmp_path, **kw):
    """A first run that dies when round 2's batch would be created; returns the client and its spend."""
    first = BatchClient(ctx, tmp_path, **kw)
    real_create = first.messages.batches.create

    def create(requests):
        if first.created:
            raise RuntimeError("round 2 create broke")
        return real_create(requests)

    first.messages.batches.create = create
    with pytest.raises(RuntimeError):
        _run(ctx, tmp_path, first)
    return first


def test_typo_resume_id_refused_and_touches_nothing(analyst_ctx, tmp_path):
    from canary.analyst.showcase import ResumeError

    _stop_after_round1(analyst_ctx, tmp_path)
    prog = tmp_path / "report.progress"
    before = sorted(p.name for p in prog.iterdir())
    state_before = (tmp_path / "report.state.json").read_text()
    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    with pytest.raises(ResumeError, match="batch_TYPO"):
        _run(analyst_ctx, tmp_path, second, resume="batch_TYPO")
    assert sorted(p.name for p in prog.iterdir()) == before
    assert (tmp_path / "report.state.json").read_text() == state_before
    assert second.created == [] and second.calls == []


def test_resume_without_state_refused(analyst_ctx, tmp_path):
    from canary.analyst.showcase import ResumeError

    with pytest.raises(ResumeError, match="no state file"):
        _run(analyst_ctx, tmp_path, BatchClient(analyst_ctx, tmp_path), resume="batch_1")


def test_old_single_round_state_refused(analyst_ctx, tmp_path):
    from canary.analyst.showcase import ResumeError

    (tmp_path / "report.state.json").write_text(json.dumps({
        "batch_id": "batch_1", "created_at": "x", "model": "claude-opus-5-5", "complete": True,
        "banks": [[c, "2026-06-30", "latest_watchlist"] for c in CERTS]}))
    client = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(ResumeError, match="old single-batch|complete"):
        _run(analyst_ctx, tmp_path, client, resume="batch_1")
    assert client.calls == [] and client.created == [] and client.result_calls == []
    (tmp_path / "report.state.json").write_text(json.dumps({
        "batch_id": "batch_1", "complete": False, "model": "m", "banks": []}))
    with pytest.raises(ResumeError, match="round1_batch_id"):
        _run(analyst_ctx, tmp_path, client, resume="batch_1")


def test_batch_with_none_of_the_requested_ids_aborts(analyst_ctx, tmp_path):
    from canary.analyst.showcase import ResumeError

    client = BatchClient(analyst_ctx, tmp_path)
    client.messages.batches.results = lambda bid: iter([SimpleNamespace(
        custom_id=f"{c}-20260630", result=SimpleNamespace(type="errored")) for c in CERTS])
    with pytest.raises(ResumeError, match="none of"):
        _run(analyst_ctx, tmp_path, client)
    assert client.calls == []  # no fall-through to full-price calls
    assert not (tmp_path / "report.progress" / "round1_batch.json").exists()


def test_cli_resume_error_exits_1(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: BatchClient(analyst_ctx, tmp_path))
    rc = cli.main(["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
                   "--report", str(tmp_path / "rep.json"), "--out", str(tmp_path / "banks"), "--resume", "nope"])
    assert rc == 1 and "no state file" in capsys.readouterr().err


def test_before_call_fires_once_per_direct_call_never_for_batch(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import _Run

    seen = []
    real = _Run._before_call
    monkeypatch.setattr(_Run, "_before_call", lambda self, agent, attempt: (seen.append((agent, attempt)),
                                                                           real(self, agent, attempt))[1])
    # 100 trend: bad batch memo -> retry (1 direct); 101 analyst: errored batch -> redo (1 direct, passes)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad", (101, "analyst"): "errored"})
    _run(analyst_ctx, tmp_path, client)
    assert len(client.calls) == 2 and len(seen) == 2
    assert sorted(seen) == [("analyst", 1), ("trend", 2)]


def test_before_call_raising_stops_without_a_call(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import RunStopped, _Run

    def stop(self, agent, attempt):
        raise RunStopped("limit")

    monkeypatch.setattr(_Run, "_before_call", stop)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"})
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, client)
    assert client.calls == []
    assert not (tmp_path / "report.progress" / "100-20260630-trend.json").exists()
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is False


def test_round_boundary_not_called_for_a_created_round(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import _Run

    first = BatchClient(analyst_ctx, tmp_path)
    real = _break_round2_results(first)
    with pytest.raises(RuntimeError):
        _run(analyst_ctx, tmp_path, first)
    calls = []
    monkeypatch.setattr(_Run, "_round_boundary", lambda self, rnd, requests=None: calls.append(rnd))
    second = BatchClient(analyst_ctx, tmp_path)
    second.created = first.created
    second.messages.batches.results = lambda bid: real(bid)
    _run(analyst_ctx, tmp_path, second, resume="batch_2")
    assert calls == []  # both batches already existed
    # a fresh run does call it, once per round
    calls.clear()
    _run(analyst_ctx, tmp_path, BatchClient(analyst_ctx, tmp_path))
    assert calls == [1, 2]


def test_resume_after_direct_retries_does_not_recall_or_recount(analyst_ctx, tmp_path):
    first = _stop_after_round1(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"})
    assert len(first.calls) == 1  # the retry of 100's trend, paid at full price
    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert second.calls == []  # nothing from round 1 was called again
    assert rep["written"] == 4
    n = len(first.created[0]) + len(second.created[0])
    assert rep["cost_usd"] == pytest.approx(n * FULL / 2 + FULL)  # the retry counted once
    assert rep["spend_by_round"]["round1"]["direct"] == pytest.approx(FULL)
    by = {b["cert"]: b for b in rep["banks"]}
    assert by[100]["agents"]["trend"]["attempts"] == 2


def test_raised_agent_is_not_saved_so_resume_retries_it(analyst_ctx, tmp_path):
    import anthropic

    err = anthropic.APIConnectionError(request=SimpleNamespace(method="POST", url="https://x"))
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "analyst"): "errored"},
                         direct={(100, "analyst"): [err]})
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert not by[100]["ok"] and "APIConnectionError" in " ".join(by[100]["errors"])
    assert rep["complete"] is False
    st = json.loads((tmp_path / "report.state.json").read_text())
    assert st["complete"] is False
    assert not (tmp_path / "report.progress" / "100-20260630-analyst.json").exists()
    assert not (tmp_path / "report.progress" / "100-20260630-entry.json").exists()
    second = BatchClient(analyst_ctx, tmp_path, first_id=3)
    second.created = client.created
    second.messages.batches.create = lambda **kw: pytest.fail("created a batch")
    rep2 = _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert rep2["written"] == 4 and len(second.calls) == 1  # only 100's analyst, via its saved errored result
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is True


# ---- spending limit (Task 4) ------------------------------------------------------------

@pytest.fixture
def round1_unpriced(monkeypatch):
    """The fake calls cost far less than the per-agent constants; tests of the later limit checks let
    round 1 through the (separately tested) round 1 check."""
    from canary.analyst.showcase import _Run

    monkeypatch.setattr(_Run, "_round1_projection", lambda self, requests: (0.0, 0.0))

def _stopped_state(tmp_path):
    return json.loads((tmp_path / "report.state.json").read_text())


def test_no_limit_runs_through(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"})
    rep = _run(analyst_ctx, tmp_path, client)  # max_cost defaults to None
    assert rep["written"] == 4 and rep["complete"] and not rep.get("stopped")


def test_huge_limit_runs_through(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"})
    rep = _run(analyst_ctx, tmp_path, client, max_cost=1000.0)
    assert rep["written"] == 4 and rep["complete"] and not rep.get("stopped")


def test_stop_before_round2_when_projected_over_limit(analyst_ctx, tmp_path, round1_unpriced):
    from canary.analyst.showcase import RunStopped

    client = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped) as ei:
        _run(analyst_ctx, tmp_path, client, max_cost=0.1)  # round 1 costs 0.056; round 2 projects well above 0.1
    assert len(client.created) == 1 and client.calls == []  # no round-2 batch, no direct call
    rep = json.loads((tmp_path / "report.json").read_text())
    assert rep["stopped"] == "spending limit" and rep["complete"] is False
    assert rep["cost_usd"] == pytest.approx(len(client.created[0]) * FULL / 2)
    st = _stopped_state(tmp_path)
    assert st["stopped"] == "spending limit" and st["complete"] is False and st["round2_batch_id"] is None
    assert st["spend"]["round1"]["batch"] == pytest.approx(rep["cost_usd"])
    assert ei.value.limit == 0.1 and ei.value.spent == pytest.approx(rep["cost_usd"])
    assert "spending limit" in str(ei.value)
    assert not list((tmp_path / "banks").glob("*.md"))


def test_stop_before_retry(analyst_ctx, tmp_path, round1_unpriced):
    from canary.analyst.showcase import RunStopped

    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"})
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, client, max_cost=0.1)  # a full-price retry (~0.15 est) would pass 0.1
    assert client.calls == []  # the retry was never made
    rep = json.loads((tmp_path / "report.json").read_text())
    assert rep["stopped"] == "spending limit" and len(client.created) == 1
    assert not (tmp_path / "report.progress" / "100-20260630-trend.json").exists()
    assert _stopped_state(tmp_path)["complete"] is False


def test_stop_between_two_retries_saves_what_finished(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import RunStopped, _Run

    real = _Run._before_call
    n = {"k": 0}

    def second_call_stops(self, agent, attempt):
        n["k"] += 1
        if n["k"] == 2:
            raise RunStopped("stop", spent=0.0, limit=0.0)
        real(self, agent, attempt)

    monkeypatch.setattr(_Run, "_before_call", second_call_stops)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad", (101, "trend"): "bad"})
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, client)
    assert len(client.calls) == 1  # 100's retry was made and paid; 101's was not
    st = _stopped_state(tmp_path)
    assert st["spend"]["round1"]["direct"] == pytest.approx(FULL)
    assert (tmp_path / "report.progress" / "100-20260630-trend.json").exists()
    assert not (tmp_path / "report.progress" / "101-20260630-trend.json").exists()


def test_resume_after_limit_stop_with_higher_limit(analyst_ctx, tmp_path, round1_unpriced):
    from canary.analyst.showcase import RunStopped

    first = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, first, max_cost=0.1)
    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    second.messages.batches.results = lambda bid: pytest.fail("round 1 refetched") if bid == "batch_1" \
        else BatchClient._results(second, bid)
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_1", max_cost=1000.0)
    assert len(second.created) == 1  # only round 2 was submitted
    assert {r["custom_id"].rsplit("-", 1)[1] for r in second.created[0]} == {"analyst"}
    assert rep["written"] == 4 and rep["complete"] and not rep.get("stopped")
    assert rep["cost_usd"] == pytest.approx((len(first.created[0]) + len(second.created[0])) * FULL / 2)
    st = _stopped_state(tmp_path)
    assert st["complete"] is True and not st.get("stopped")


def test_resume_with_same_low_limit_stops_again_without_paying(analyst_ctx, tmp_path, round1_unpriced):
    from canary.analyst.showcase import RunStopped

    first = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, first, max_cost=0.1)
    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, second, resume="batch_1", max_cost=0.1)
    assert second.created == [] and second.calls == []
    assert json.loads((tmp_path / "report.json").read_text())["cost_usd"] == pytest.approx(
        len(first.created[0]) * FULL / 2)


def test_round2_limit_checked_only_before_creating_it(analyst_ctx, tmp_path):
    first = BatchClient(analyst_ctx, tmp_path)
    real = _break_round2_results(first)
    with pytest.raises(RuntimeError):
        _run(analyst_ctx, tmp_path, first)  # round 2 exists and is paid for
    second = BatchClient(analyst_ctx, tmp_path)
    second.created = first.created
    second.messages.batches.results = lambda bid: real(bid)
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_2", max_cost=0.01)  # tiny limit, nothing left to buy
    assert rep["written"] == 4 and not rep.get("stopped")


# ---- R2: model-side final errors, empty resume, stop inside the writer, CLI -------------

@pytest.mark.parametrize("exc", [RefusalError("declined"), TruncatedError("cut off"), ValueError("not json")])
def test_model_side_final_error_is_saved_as_failed(analyst_ctx, tmp_path, exc):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"},
                         direct={(100, "trend"): [exc]})
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert not by[100]["ok"] and len(client.calls) == 1
    assert (tmp_path / "report.progress" / "100-20260630-trend.json").exists()
    assert rep["complete"] is True and _stopped_state(tmp_path)["complete"] is True
    from canary.analyst.showcase import ResumeError
    second = BatchClient(analyst_ctx, tmp_path, first_id=3)
    with pytest.raises(ResumeError):  # complete: the failed agent is final, never paid for again
        _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert second.calls == [] and second.created == []


def test_transport_error_stays_unfinished(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "bad"},
                         direct={(100, "trend"): [RuntimeError("boom")]})
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["complete"] is False
    assert not (tmp_path / "report.progress" / "100-20260630-trend.json").exists()


def test_resume_empty_string_refused_and_state_kept(analyst_ctx, tmp_path):
    from canary.analyst.showcase import ResumeError

    _stop_after_round1(analyst_ctx, tmp_path)
    before = (tmp_path / "report.state.json").read_text()
    prog = tmp_path / "report.progress"
    names = sorted(p.name for p in prog.iterdir())
    with pytest.raises(ResumeError):
        _run(analyst_ctx, tmp_path, BatchClient(analyst_ctx, tmp_path, first_id=2), resume="")
    assert (tmp_path / "report.state.json").read_text() == before
    assert sorted(p.name for p in prog.iterdir()) == names


def test_cli_resume_empty_string_exits_1(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: object())
    rc = cli.main(["showcase", "--resume", "", "--model-dir", str(tmp_model_dir),
                   "--replay-dir", str(tmp_replay_dir.path), "--report", str(tmp_path / "r.json")])
    assert rc == 1 and "error" in capsys.readouterr().err


def test_finish_passes_before_call_and_reraises_stop(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import RunStopped, _Run

    seen = {}
    import canary.analyst.showcase as sc

    def fake_write(ctx, cert, as_of, **kw):
        seen["bc"] = kw.get("before_call")
        raise RunStopped("stop", spent=1.0, limit=0.5)

    monkeypatch.setattr(sc, "write_memo", fake_write)
    client = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, client)
    assert seen["bc"] is not None and getattr(seen["bc"], "__func__", None) is _Run._before_call
    assert json.loads((tmp_path / "report.json").read_text())["stopped"] == "spending limit"


def test_cli_catches_stop_prints_resume_and_exits_nonzero(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch,
                                                          tmp_path, capsys):
    from canary.analyst.showcase import RunStopped

    report = tmp_path / "rep.json"
    (tmp_path / "rep.state.json").write_text(json.dumps({"batch_id": "b1", "round1_batch_id": "b1", "banks": [],
                                                        "model": "m", "complete": False, "created_at": "x"}))

    def fake_run(*a, **k):
        raise RunStopped("limit", spent=3.5, limit=3.0)

    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr("canary.analyst.showcase.run_showcase", fake_run)
    monkeypatch.setattr(cli, "make_client", lambda: object())
    rc = cli.main(["showcase", "--resume", "b1", "--max-cost", "3", "--model-dir", str(tmp_model_dir),
                   "--replay-dir", str(tmp_replay_dir.path), "--report", str(report)])
    cap = capsys.readouterr()
    assert rc == 1
    assert "stopped at spending limit ($3.50 spent of $3.00)" in cap.err + cap.out
    assert "--resume b1" in cap.err + cap.out


def test_cli_passes_max_cost(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch, tmp_path):
    seen = {}

    def fake_run(*a, **k):
        seen.update(k)
        return {"written": 0, "failed": 0, "banks_total": 0, "cost_usd": 0.0, "banks": []}

    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr("canary.analyst.showcase.run_showcase", fake_run)
    monkeypatch.setattr(cli, "make_client", lambda: object())
    args = ["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
            "--report", str(tmp_path / "r.json")]
    cli.main(args + ["--max-cost", "17"])
    assert seen["max_cost"] == 17.0
    cli.main(args)
    assert seen["max_cost"] is None


# ---- final-review fixes -------------------------------------------------------------------

def _notes(tmp_path):
    d = tmp_path / "banks"
    return sorted(d.glob("*.md")) if d.exists() else []


def test_stop_in_round2_retry_still_writes_finished_banks(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import RunStopped, _Run

    real = _Run._before_call
    stop = {"on": True}

    def before(self, agent, attempt):
        if stop["on"] and agent == "analyst":
            raise RunStopped("stop", spent=0.0, limit=0.0)
        real(self, agent, attempt)

    monkeypatch.setattr(_Run, "_before_call", before)
    first = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(103, "analyst"): "bad"})
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, first)
    assert len(_notes(tmp_path)) == 3  # 100, 101, 102 passed and are written; 103 is waiting for its retry
    rep = json.loads((tmp_path / "report.json").read_text())
    assert rep["written"] == 3 and rep["banks_done"] == 3 and rep["stopped"] == "spending limit"
    stop["on"] = False
    second = BatchClient(analyst_ctx, tmp_path, first_id=3)
    second.messages.batches.results = lambda bid: pytest.fail("a finished round was refetched")
    rep = _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert len(second.calls) == 1 and second.created == []  # only 103's analyst retry; nothing else redone
    assert rep["written"] == 4 and rep["complete"] and len(_notes(tmp_path)) == 4


def test_stop_handler_finishes_banks_whose_analyst_is_saved(analyst_ctx, tmp_path, monkeypatch):
    from canary.analyst.showcase import RunStopped, _Run

    real_before, real_finish = _Run._before_call, _Run._finish
    seen = {"skipped": False}

    def before(self, agent, attempt):
        if agent == "analyst":
            raise RunStopped("stop", spent=0.0, limit=0.0)
        real_before(self, agent, attempt)

    def finish(self, cert, as_of, group, base):
        if cert == 100 and not seen["skipped"]:  # as if bank 100's note had not been written in the loop
            seen["skipped"] = True
            return
        real_finish(self, cert, as_of, group, base)

    monkeypatch.setattr(_Run, "_before_call", before)
    monkeypatch.setattr(_Run, "_finish", finish)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "bad"})
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, client)
    from canary.analyst.render import note_path
    assert note_path(tmp_path / "banks", _sheet(analyst_ctx, tmp_path, 100).name, 100) in _notes(tmp_path)
    assert json.loads((tmp_path / "report.json").read_text())["written"] == 1


def test_resume_inherits_saved_max_cost(analyst_ctx, tmp_path, round1_unpriced):
    from canary.analyst.showcase import RunStopped

    first = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped):
        _run(analyst_ctx, tmp_path, first, max_cost=0.1)
    assert _stopped_state(tmp_path)["max_cost"] == 0.1
    second = BatchClient(analyst_ctx, tmp_path, first_id=2)
    with pytest.raises(RunStopped):  # no --max-cost: the saved limit still applies
        _run(analyst_ctx, tmp_path, second, resume="batch_1")
    assert second.created == [] and second.calls == []
    assert json.loads((tmp_path / "report.json").read_text())["max_cost"] == 0.1
    third = BatchClient(analyst_ctx, tmp_path, first_id=2)
    rep = _run(analyst_ctx, tmp_path, third, resume="batch_1", max_cost=1000.0)  # explicit value overrides
    assert rep["written"] == 4 and rep["max_cost"] == 1000.0 and _stopped_state(tmp_path)["max_cost"] == 1000.0


def test_cli_stop_line_names_max_cost(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch, tmp_path, capsys):
    from canary.analyst.showcase import RunStopped

    (tmp_path / "rep.state.json").write_text(json.dumps({"batch_id": "b1", "round1_batch_id": "b1", "banks": [],
                                                        "model": "m", "complete": False, "created_at": "x"}))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr("canary.analyst.showcase.run_showcase",
                        lambda *a, **k: (_ for _ in ()).throw(RunStopped("limit", spent=3.5, limit=3.0)))
    monkeypatch.setattr(cli, "make_client", lambda: object())
    cli.main(["showcase", "--resume", "b1", "--max-cost", "3", "--model-dir", str(tmp_model_dir),
              "--replay-dir", str(tmp_replay_dir.path), "--report", str(tmp_path / "rep.json")])
    err = capsys.readouterr().err
    assert "--resume b1 --max-cost" in err and "saved $3.00 limit" in err


def test_round1_over_limit_stops_before_create(analyst_ctx, tmp_path, capsys):
    from canary.analyst.showcase import RunStopped

    client = BatchClient(analyst_ctx, tmp_path)
    with pytest.raises(RunStopped) as ei:
        _run(analyst_ctx, tmp_path, client, max_cost=0.05)  # 8 real-size requests are priced well above this
    assert client.created == [] and client.calls == [] and "round 1" in str(ei.value)
    assert ei.value.spent == 0.0 and ei.value.limit == 0.05
    assert not (tmp_path / "report.state.json").exists()
    rep = json.loads((tmp_path / "report.json").read_text())
    assert rep["stopped"] == "spending limit" and rep["cost_usd"] == 0.0
    assert "submitting" not in capsys.readouterr().out


def test_round1_projection_matches_estimate_run(analyst_ctx, tmp_path):
    from canary.analyst import showcase
    from canary.analyst.showcase import _Run, estimate_run

    est = estimate_run(analyst_ctx, BANKS, "claude-opus-5-5", tmp_path / "none")
    run = _Run(analyst_ctx, None, "claude-opus-5-5", tmp_path, tmp_path / "r.json", 0, BANKS, tmp_path / "none",
               tmp_path, {"spend": {}})
    reqs = []
    for cert, as_of, _g in BANKS:
        sheet = _sheet(analyst_ctx, tmp_path, cert)
        for a in showcase.SPECIALISTS:
            from canary.analyst.pipeline import agent_sections, build_agent_request
            if agent_sections(sheet, a):
                reqs.append({"custom_id": showcase.custom_id(cert, as_of, a),
                             "params": build_agent_request(sheet, a, "claude-opus-5-5")})
    batch, retry = run._round1_projection(reqs)
    assert batch == pytest.approx(est["rounds"][1]["cost"])
    assert retry == pytest.approx(est["retries"]["trend"]["cost"] + est["retries"]["peer"]["cost"], rel=0.02)


def test_round1_within_limit_prints_counts_then_runs(analyst_ctx, tmp_path, capsys):
    client = BatchClient(analyst_ctx, tmp_path)
    rep = _run(analyst_ctx, tmp_path, client, max_cost=1000.0)
    out = capsys.readouterr().out
    assert f"{len(BANKS)} banks; submitting round 1 with {len(client.created[0])} requests" in out
    assert rep["written"] == 4


def test_round2_sizing_failure_does_not_crash_the_run(analyst_ctx, tmp_path, monkeypatch):
    import canary.analyst.showcase as sc

    real = sc.request_tokens

    def sizing(request):
        if "Sections written by other agents" in json.dumps(request):
            raise RuntimeError("cannot size")
        return real(request)

    monkeypatch.setattr(sc, "request_tokens", sizing)
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(101, "analyst"): "bad"})
    rep = _run(analyst_ctx, tmp_path, client, max_cost=1000.0)
    assert rep["written"] == 4 and rep["complete"]


def test_round2_projection_never_zero_when_round1_paid_nothing(analyst_ctx, tmp_path, monkeypatch):
    import canary.analyst.showcase as sc
    from canary.analyst.showcase import RunStopped, _Run

    monkeypatch.setitem(sc.RETRY_SHARE_BY_AGENT, "analyst", 0.0)  # the retry allowance must not hide it
    monkeypatch.setattr(_Run, "_before_call", lambda self, agent, attempt: None)
    monkeypatch.setattr(_Run, "_round1_projection", lambda self, requests: (0.0, 0.0))
    client = BatchClient(analyst_ctx, tmp_path, outcomes={c: "errored" for c in CERTS})  # round 1 paid nothing
    with pytest.raises(RunStopped) as ei:
        _run(analyst_ctx, tmp_path, client, max_cost=0.2)  # the 8 direct calls cost ~0.11 of it
    assert len(client.created) == 1 and "round 2" in str(ei.value)


def test_unusable_batch_results_are_traced_and_counted(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path, agent_outcomes={(100, "trend"): "refusal", (101, "trend"): "errored"})
    rep = _run(analyst_ctx, tmp_path, client)
    st = _stopped_state(tmp_path)
    p100 = json.loads((tmp_path / "report.progress" / "100-20260630-trend.json").read_text())
    batch = [t for t in p100["trace"] if t["source"] == "batch"]
    assert len(batch) == 1 and "unusable" in batch[0]["error"] and batch[0]["cost_usd"] == pytest.approx(FULL / 2)
    assert st["agents"]["100-20260630"]["trend"]["spend"] == pytest.approx(FULL / 2 + FULL)  # batch + retry
    p101 = json.loads((tmp_path / "report.progress" / "101-20260630-trend.json").read_text())
    errored = [t for t in p101["trace"] if t["source"] == "batch"]
    assert len(errored) == 1 and "errored" in errored[0]["error"] and errored[0]["cost_usd"] == 0.0
    assert st["agents"]["101-20260630"]["trend"]["spend"] == pytest.approx(FULL)
    calls = json.loads((tmp_path / "traces" / "100_2026-06-30.json").read_text())["calls"]
    assert any(t["source"] == "batch" and "unusable" in t.get("error", "") for t in calls)
    assert rep["written"] == 4


def test_batch_create_has_sdk_retries_off(analyst_ctx, tmp_path):
    client = BatchClient(analyst_ctx, tmp_path)
    opts = []
    client.with_options = lambda **kw: (opts.append(kw), SimpleNamespace(messages=client.messages))[1]
    _run(analyst_ctx, tmp_path, client)
    assert len(client.created) == 2 and opts == [{"max_retries": 0}] * 2


def test_calibrated_constants():
    from canary.analyst import showcase
    assert showcase.EST_ANALYST_SPECIALIST_CHARS == 2600
    assert showcase.RETRY_SHARE_BY_AGENT == {"trend": 0.16, "peer": 0.16, "analyst": 0.30}
    assert showcase.CHARS_PER_TOKEN == 2.4


def test_cli_round1_stop_says_rerun_not_resume(analyst_ctx, tmp_model_dir, tmp_replay_dir, monkeypatch,
                                               tmp_path, capsys):
    from canary.analyst.showcase import RunStopped

    def fake_run(*a, **k):
        raise RunStopped("limit", spent=0.0, limit=1.0)

    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: object())
    monkeypatch.setattr("canary.analyst.showcase.run_showcase", fake_run)
    rc = cli.main(["showcase", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path),
                   "--report", str(tmp_path / "rep.json"), "--max-cost", "1"])
    err = capsys.readouterr().err
    assert rc == 1 and "nothing was paid" in err and "RE-RUN" in err and "--resume BATCH_ID" not in err
