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
