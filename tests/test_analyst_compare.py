import json

import pytest

from analyst_fakes import FakeClient
from canary.analyst import __main__ as cli
from canary.analyst.compare import compare_models
from canary.analyst.facts import build_fact_sheet
from canary.analyst.writer import RefusalError, cost_usd
from test_analyst_writer import _memo

CERTS = (3, 110)
OPUS, SONNET = "claude-opus-5-5", "claude-sonnet-5-5"


@pytest.fixture
def memos(analyst_ctx, tmp_path):
    sheets = {c: build_fact_sheet(analyst_ctx, c, replay_dir=tmp_path / "none") for c in CERTS}
    good = {c: _memo(s) for c, s in sheets.items()}
    bad = {c: _memo(s, rank_text="999,999") for c, s in sheets.items()}
    return good, bad


def test_compare_counts_and_cost(analyst_ctx, memos, tmp_path):
    good, bad = memos
    # opus: both pass first try; sonnet: cert 3 needs a retry, cert 110 passes first try
    client = FakeClient([good[3], good[110], bad[3], good[3], good[110]])
    out = tmp_path / "cmp"
    rep = compare_models(analyst_ctx, client, models=(OPUS, SONNET), certs=CERTS, out_dir=out,
                         replay_dir=tmp_path / "none")
    o, s = rep["models"][OPUS], rep["models"][SONNET]
    assert (o["passed_first_try"], o["passed_after_retry"], o["failed"]) == (2, 0, 0)
    assert (s["passed_first_try"], s["passed_after_retry"], s["failed"]) == (1, 1, 0)
    assert o["input_tokens"] == 2000 and o["output_tokens"] == 1000
    assert s["input_tokens"] == 3000 and s["output_tokens"] == 1500
    assert o["cost_usd"] == pytest.approx(2 * cost_usd(OPUS, 1000, 500))
    assert s["cost_usd"] == pytest.approx(3 * cost_usd(SONNET, 1000, 500))
    assert len(list((out / OPUS).glob("*.md"))) == 2 and len(list((out / SONNET).glob("*.md"))) == 2
    assert json.loads((out / "compare.json").read_text()) == rep
    m = [x for x in rep["memos"] if x["model"] == SONNET and x["cert"] == 3][0]
    assert m["attempts"] == 2 and m["ok"] and m["path"].startswith(str(out / SONNET))


def test_one_failure_does_not_abort(analyst_ctx, memos, tmp_path):
    good, _ = memos
    client = FakeClient([RuntimeError("api down"), good[110]])
    rep = compare_models(analyst_ctx, client, models=(OPUS,), certs=CERTS, out_dir=tmp_path / "c",
                         replay_dir=tmp_path / "none")
    assert rep["models"][OPUS]["failed"] == 1 and rep["models"][OPUS]["passed_first_try"] == 1
    bad = [x for x in rep["memos"] if x["cert"] == 3][0]
    assert not bad["ok"] and bad["path"] is None and "RuntimeError: api down" in bad["errors"][0]


def test_cli_compare(monkeypatch, analyst_ctx, memos, tmp_path, capsys):
    good, _ = memos
    client = FakeClient([good[3], RefusalError("no")])
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: client)
    monkeypatch.setattr("canary.analyst.compare.CASE_STUDY_CERTS", (3, 110))
    monkeypatch.setattr(cli, "REPLAY_DIR", tmp_path / "none")
    rc = cli.main(["compare", "--models", OPUS, "--out", str(tmp_path / "c")])
    out = capsys.readouterr().out
    assert rc == 0 and "2 calls" in out and "first try" in out and ".md" in out


def test_cli_compare_bad_models(monkeypatch, analyst_ctx, tmp_path, capsys):
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    assert cli.main(["compare", "--models", " , ", "--out", str(tmp_path)]) == 2


def test_compare_served_model_usage_on_error_and_replay_dir(analyst_ctx, memos, tmp_path, monkeypatch):
    from analyst_fakes import fake_message

    good, bad = memos
    served = fake_message(json.dumps(good[3]), model=SONNET)
    client = FakeClient([served, bad[110], RefusalError("no")])
    seen = []
    import canary.analyst.compare as cmp

    real = cmp.write_memo
    monkeypatch.setattr(cmp, "write_memo", lambda *a, **k: (seen.append(k["replay_dir"]), real(*a, **k))[1])
    rep = compare_models(analyst_ctx, client, models=(OPUS,), certs=CERTS, out_dir=tmp_path / "c",
                         replay_dir=tmp_path / "rd")
    assert seen == [tmp_path / "rd"] * 2
    by = {m["cert"]: m for m in rep["memos"]}
    assert by[3]["served_model"] == SONNET and by[3]["ok"]
    assert not by[110]["ok"] and by[110]["served_model"] == OPUS
    # 110: one bad memo spent tokens before the retry refused; that spend is counted
    o = rep["models"][OPUS]
    assert o["input_tokens"] == 2000 and o["output_tokens"] == 1000
    assert o["cost_usd"] == pytest.approx(cost_usd(SONNET, 1000, 500) + cost_usd(OPUS, 1000, 500))
