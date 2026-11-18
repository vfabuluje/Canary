import json
from datetime import date
from types import SimpleNamespace

import pandas as pd
import pytest

from analyst_fakes import FakeClient, fake_message
from canary.analyst import __main__ as cli
from canary.analyst.facts import build_fact_sheet
from canary.analyst.sections import all_sections
from canary.analyst.showcase import run_showcase, showcase_banks
from canary.analyst.writer import PRICES, cost_usd

from test_analyst_writer import _memo


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


def test_estimates_are_measured_averages():
    from canary.analyst.showcase import EST_INPUT_TOKENS, EST_OUTPUT_TOKENS
    assert (EST_INPUT_TOKENS, EST_OUTPUT_TOKENS) == (7300, 3200)


# ---- batch run ------------------------------------------------------------------------

BANKS = [(100, date(2026, 6, 30), "latest_watchlist"), (101, date(2026, 6, 30), "latest_watchlist"),
         (102, date(2026, 6, 30), "latest_watchlist"), (103, date(2026, 6, 30), "latest_watchlist")]


class BatchClient(FakeClient):
    """FakeClient plus messages.batches. `outcomes` maps cert -> 'ok'|'errored'|'expired'|'refusal'|'bad'."""

    def __init__(self, ctx, tmp_path, outcomes, responses=(), polls=2):
        super().__init__(list(responses))
        self.ctx, self.tmp_path, self.outcomes, self.polls = ctx, tmp_path, outcomes, polls
        self.created, self.retrieved = [], 0
        self.messages = SimpleNamespace(batches=SimpleNamespace(
            create=self._create, retrieve=self._retrieve, results=self._results))

    def _create(self, requests):
        self.created.append(requests)
        return SimpleNamespace(id="batch_1", processing_status="in_progress")

    def _retrieve(self, batch_id):
        self.retrieved += 1
        return SimpleNamespace(id=batch_id, processing_status="ended" if self.retrieved >= self.polls else "in_progress")

    def _results(self, batch_id):
        out = []
        for req in reversed(self.created[0]):  # any order
            cert = int(req["custom_id"].split("-")[0])
            kind = self.outcomes[cert]
            if kind == "ok":
                sheet = build_fact_sheet(self.ctx, cert, date(2026, 6, 30), replay_dir=self.tmp_path / "none")
                res = SimpleNamespace(type="succeeded", message=fake_message(json.dumps(_memo(sheet)), model=req["params"]["model"]))
            elif kind == "refusal":
                res = SimpleNamespace(type="succeeded", message=fake_message("", stop_reason="refusal"))
            elif kind == "bad":
                res = SimpleNamespace(type="succeeded", message=fake_message(json.dumps({"sections": []})))
            else:
                res = SimpleNamespace(type=kind)
            out.append(SimpleNamespace(custom_id=req["custom_id"], result=res))
        return iter(out)


def _good(ctx, tmp_path, cert):
    return _memo(build_fact_sheet(ctx, cert, date(2026, 6, 30), replay_dir=tmp_path / "none"))


def _run(ctx, tmp_path, client, banks=BANKS, **kw):
    return run_showcase(ctx, client, "claude-opus-5-5", tmp_path / "banks", tmp_path / "report.json",
                        poll_seconds=0, banks=banks, replay_dir=tmp_path / "none", **kw)


def test_partial_batch_failures_retried(analyst_ctx, tmp_path):
    outcomes = {100: "ok", 101: "errored", 102: "expired", 103: "refusal"}
    client = BatchClient(analyst_ctx, tmp_path, outcomes,
                         responses=[_good(analyst_ctx, tmp_path, c) for c in (101, 102, 103)])
    rep = _run(analyst_ctx, tmp_path, client)
    assert len(client.created) == 1 and len(client.created[0]) == 4
    ids = {r["custom_id"] for r in client.created[0]}
    assert ids == {f"{c}-20260630" for c in (100, 101, 102, 103)}
    assert "fallbacks" not in client.created[0][0]["params"]
    assert len(client.calls) == 3  # three normal retries, with fallbacks
    assert all(c.get("fallbacks") == "default" for c in client.calls)
    assert rep["written"] == 4 and rep["failed"] == 0
    assert len(list((tmp_path / "banks").glob("*.md"))) == 4
    assert json.loads((tmp_path / "report.json").read_text())["written"] == 4
    # cost: 2 batch results with usage (ok, refusal) at half price + 3 retries at full price
    full = cost_usd("claude-opus-5-5", 1000, 500)
    assert rep["cost_usd"] == pytest.approx(2 * full / 2 + 3 * full)
    assert rep["input_tokens"] == 5000 and rep["output_tokens"] == 2500


def test_still_failing_listed_in_report(analyst_ctx, tmp_path):
    from canary.analyst.writer import RefusalError

    outcomes = {100: "ok", 101: "bad", 102: "errored", 103: "ok"}
    bad = {"sections": []}
    # 101: bad batch memo -> check fails -> retry call also bad; 102: retry refuses (raises)
    client = BatchClient(analyst_ctx, tmp_path, outcomes, responses=[bad, RefusalError("no")])
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["written"] == 2 and rep["failed"] == 2
    failed = {b["cert"]: b for b in rep["banks"] if not b["ok"]}
    assert set(failed) == {101, 102}
    assert failed[101]["errors"] and "no" in " ".join(failed[102]["errors"])
    assert json.loads((tmp_path / "report.json").read_text())["failed"] == 2


def test_dry_run_makes_no_calls(analyst_ctx, tmp_model_dir, tmp_replay_dir, capsys, monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "make_client", lambda: pytest.fail("client constructed"))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    rc = cli.main(["showcase", "--dry-run", "--model-dir", str(tmp_model_dir), "--replay-dir", str(tmp_replay_dir.path)])
    out = capsys.readouterr().out
    assert rc == 0 and "banks" in out and "estimated cost" in out and "false_alarm" in out


def test_unexpected_retry_error_does_not_abort_run(analyst_ctx, tmp_path):
    import anthropic

    err = anthropic.APIConnectionError(request=SimpleNamespace(method="POST", url="https://x"))
    outcomes = {100: "errored", 101: "errored", 102: "errored", 103: "ok"}
    client = BatchClient(analyst_ctx, tmp_path, outcomes,
                         responses=[RuntimeError("boom"), err, _good(analyst_ctx, tmp_path, 102)])
    rep = _run(analyst_ctx, tmp_path, client)
    by = {b["cert"]: b for b in rep["banks"]}
    assert len(by) == 4 and rep["written"] == 2 and rep["failed"] == 2
    assert not by[100]["ok"] and "RuntimeError" in " ".join(by[100]["errors"])
    assert not by[101]["ok"] and "APIConnectionError" in " ".join(by[101]["errors"])
    assert by[102]["ok"] and by[103]["ok"]
    assert json.loads((tmp_path / "report.json").read_text())["failed"] == 2


def test_missing_batch_result_is_retried(analyst_ctx, tmp_path):
    outcomes = {100: "ok", 101: "ok", 102: "ok", 103: "ok"}
    client = BatchClient(analyst_ctx, tmp_path, outcomes, responses=[_good(analyst_ctx, tmp_path, 102)])
    orig = client._results
    client.messages.batches.results = lambda bid: iter(
        [r for r in orig(bid) if not r.custom_id.startswith("102-")])
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["written"] == 4 and len(rep["banks"]) == 4
    assert len(client.calls) == 1
    assert {b["cert"]: b["source"] for b in rep["banks"]}[102] == "retry"


# ---- final-review fixes ----------------------------------------------------------------

def test_state_file_written_with_batch_id(analyst_ctx, tmp_path):
    from canary.analyst.showcase import state_path

    outcomes = {c: "ok" for c in (100, 101, 102, 103)}
    client = BatchClient(analyst_ctx, tmp_path, outcomes)
    rep = _run(analyst_ctx, tmp_path, client)
    st = json.loads(state_path(tmp_path / "report.json").read_text())
    assert state_path(tmp_path / "report.json") == tmp_path / "report.state.json"
    assert st["batch_id"] == "batch_1" and st["model"] == "claude-opus-5-5" and st["created_at"]
    assert st["banks"] == [[c, "2026-06-30", "latest_watchlist"] for c in (100, 101, 102, 103)]
    assert st["complete"] is True
    assert rep["batch_id"] == "batch_1" and rep["complete"] is True
    assert all(b["served_model"] == "claude-opus-5-5" for b in rep["banks"])


def test_resume_makes_no_create_call(analyst_ctx, tmp_path):
    outcomes = {c: "ok" for c in (100, 101, 102, 103)}
    first = BatchClient(analyst_ctx, tmp_path, outcomes)
    first.created.append([{"custom_id": f"{c}-20260630", "params": {"model": "claude-sonnet-5-5"}}
                          for c in (100, 101, 102, 103)])  # the earlier run's batch
    (tmp_path / "report.state.json").write_text(json.dumps({
        "batch_id": "batch_1", "created_at": "2026-11-17T10:00:00", "model": "claude-sonnet-5-5", "complete": False,
        "banks": [[c, "2026-06-30", "latest_watchlist"] for c in (100, 101, 102, 103)]}))
    create_calls = []
    first.messages.batches.create = lambda **kw: create_calls.append(kw)
    rep = run_showcase(analyst_ctx, first, "claude-opus-5-5", tmp_path / "banks", tmp_path / "report.json",
                       poll_seconds=0, replay_dir=tmp_path / "none", resume="batch_1")
    assert create_calls == [] and first.retrieved >= 1
    assert rep["written"] == 4 and rep["batch_id"] == "batch_1" and rep["model"] == "claude-sonnet-5-5"
    assert json.loads((tmp_path / "report.state.json").read_text())["complete"] is True


def test_transient_retrieve_error_then_success(analyst_ctx, tmp_path, monkeypatch):
    import anthropic

    from analyst_fakes import api_status_error
    from canary.analyst import showcase

    sleeps = []
    monkeypatch.setattr(showcase.time, "sleep", lambda s: sleeps.append(s))
    outcomes = {c: "ok" for c in (100, 101, 102, 103)}
    client = BatchClient(analyst_ctx, tmp_path, outcomes, polls=1)
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
    client = BatchClient(analyst_ctx, tmp_path, {c: "ok" for c in (100, 101, 102, 103)})
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
    client = BatchClient(analyst_ctx, tmp_path, {c: "ok" for c in (100, 101, 102, 103)})
    client.messages.batches.retrieve = lambda bid: (_ for _ in ()).throw(api_status_error("AuthenticationError", 401))
    with pytest.raises(Exception, match="api error"):
        _run(analyst_ctx, tmp_path, client)


def test_failed_retry_usage_counted(analyst_ctx, tmp_path):
    from canary.analyst.writer import RefusalError

    outcomes = {100: "ok", 101: "bad", 102: "ok", 103: "ok"}
    client = BatchClient(analyst_ctx, tmp_path, outcomes, responses=[RefusalError("no")])
    rep = _run(analyst_ctx, tmp_path, client)
    # 4 batch results at half price; the 101 retry raised before returning usage -> nothing extra
    assert rep["input_tokens"] == 4000
    client = BatchClient(analyst_ctx, tmp_path, {100: "ok", 101: "errored", 102: "ok", 103: "ok"},
                         responses=[{"sections": []}, RefusalError("no")])
    rep = _run(analyst_ctx, tmp_path, client)
    assert rep["input_tokens"] == 3000 + 1000  # the bad retry memo's tokens survive the refusal
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
    outcomes = {c: "ok" for c in (100, 101, 102, 103)}
    client = BatchClient(analyst_ctx, tmp_path, outcomes)
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
    assert len(client.created) == 1  # resume created nothing
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
    client = BatchClient(analyst_ctx, tmp_path, {c: "ok" for c in (100, 101, 102, 103)})
    with pytest.raises(KeyboardInterrupt):
        _run(analyst_ctx, tmp_path, client)
    assert calls and json.loads((tmp_path / "report.state.json").read_text())["complete"] is False
