import json
import math
from types import SimpleNamespace

import pytest

from analyst_fakes import FakeClient, fake_message
from canary.analyst import __main__ as cli
from canary.analyst import agent, tools
from canary.analyst.writer import DEFAULT_MODEL, EFFORT, MAX_TOKENS, RefusalError
from canary.model.metrics import WATCHLIST_SHARE


def test_find_bank_by_city_failed_only(analyst_ctx):
    hit = json.loads(tools.find_bank(analyst_ctx, "city24735"))
    assert [b["cert"] for b in hit] == [24735]
    assert hit[0]["failure_date"] == "2023-03-31" and hit[0]["city"] == "City24735"
    assert hit[0]["first_report"] == "2001-03-31"
    # an open bank has no city, so a city query never reaches it
    assert json.loads(tools.find_bank(analyst_ctx, "nowhere")) == []


def test_find_bank_by_cert_and_name(analyst_ctx):
    by_cert = json.loads(tools.find_bank(analyst_ctx, "100"))
    assert [b["cert"] for b in by_cert] == [100] and by_cert[0]["city"] is None
    assert by_cert[0]["failure_date"] is None
    by_name = json.loads(tools.find_bank(analyst_ctx, "bank 101"))
    assert [b["cert"] for b in by_name] == [101]
    assert json.loads(tools.find_bank(analyst_ctx, "bank", state="ZZ")) == []


def test_find_bank_caps_at_10(analyst_ctx):
    assert len(json.loads(tools.find_bank(analyst_ctx, "bank"))) == 10


def test_find_bank_failed_year(analyst_ctx):
    got = json.loads(tools.find_bank(analyst_ctx, "bank", failed_year=2023))
    assert {b["cert"] for b in got} == {24735, 57053, 59017}


def test_get_bank_facts_ok_and_bad_as_of(analyst_ctx):
    ok = json.loads(tools.get_bank_facts(analyst_ctx, 3))
    assert ok["outcome"] and ok["facts"][0]["id"] == "F1"
    assert set(ok["facts"][0]) == {"id", "label", "quarter", "display", "window"}
    bad = json.loads(tools.get_bank_facts(analyst_ctx, 3, "2015-01-01"))
    assert "error" in bad
    assert "error" in json.loads(tools.get_bank_facts(analyst_ctx, 3, "not-a-date"))
    assert "error" in json.loads(tools.get_bank_facts(analyst_ctx, 999999))


def test_list_watchlist_size(analyst_ctx):
    got = json.loads(tools.list_watchlist(analyst_ctx))
    n = int((analyst_ctx.scored["report_date"] == analyst_ctx.scored["report_date"].max()).sum())
    assert len(got) == math.ceil(round(n * WATCHLIST_SHARE, 9))
    assert set(got[0]) == {"cert", "name", "rank"} and got[0]["rank"] == 1
    assert "error" in json.loads(tools.list_watchlist(analyst_ctx, "1999-01-01"))


def test_write_memo_tool_errors_returned(analyst_ctx):
    out = json.loads(tools.write_memo_tool(analyst_ctx, FakeClient([]), DEFAULT_MODEL, 3, "2015-01-01"))
    assert "error" in out
    refused = FakeClient([fake_message("", stop_reason="refusal")])
    out = json.loads(tools.write_memo_tool(analyst_ctx, refused, DEFAULT_MODEL, 3))
    assert "error" in out and "refused" in out["error"]


def test_make_tools_names(analyst_ctx):
    ts = agent.make_tools(analyst_ctx, FakeClient([]), DEFAULT_MODEL)
    assert [t.name for t in ts] == ["find_bank", "get_bank_facts", "list_watchlist", "write_memo"]
    for t in ts:
        props = t.to_dict()["input_schema"]["properties"]
        assert "ctx" not in props and "client" not in props and "model" not in props


def test_ask_uses_tool_runner(analyst_ctx):
    client = FakeClient([fake_message("Bank 3 failed in 2019.")])
    assert agent.ask("What happened to bank 3?", analyst_ctx, client) == "Bank 3 failed in 2019."
    kw = client.runner_calls[0]
    assert kw["model"] == DEFAULT_MODEL and kw["max_tokens"] == MAX_TOKENS
    assert kw["system"] == agent.SYSTEM and kw["output_config"] == {"effort": EFFORT}
    assert kw["messages"] == [{"role": "user", "content": "What happened to bank 3?"}]
    assert len(kw["tools"]) == 4


def test_ask_refusal(analyst_ctx):
    client = FakeClient([fake_message("", stop_reason="refusal")])
    assert "can't help" in agent.ask("x", analyst_ctx, client)


def test_cli_ask(analyst_ctx, monkeypatch, capsys):
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    client = FakeClient([fake_message("the answer")])
    monkeypatch.setattr(cli, "make_client", lambda: client)
    assert cli.main(["ask", "who is on the watchlist?", "--model", "claude-sonnet-5-5"]) == 0
    assert "the answer" in capsys.readouterr().out
    assert client.runner_calls[0]["model"] == "claude-sonnet-5-5"


def test_get_bank_facts_window(analyst_ctx):
    from datetime import date

    out = json.loads(tools.get_bank_facts(analyst_ctx, 3, "2018-03-31"))
    windows = {f["window"] for f in out["facts"]}
    assert windows == {"as_of", "hindsight"}
    fail = next(f for f in out["facts"] if f["label"] == "Failure date")
    assert fail["window"] == "hindsight"
    assert next(f for f in out["facts"] if f["label"] == "Bank name")["window"] == "as_of"


def test_list_watchlist_uses_flagged_rows(analyst_ctx):
    import pandas as pd

    s = analyst_ctx.scored
    latest = s["report_date"] == pd.Timestamp(analyst_ctx.latest_quarter)
    s.loc[latest, "flagged"] = False
    pick = s[latest].sort_values("rank").index[[2, 5]]  # not the top ranks
    s.loc[pick, "flagged"] = True
    got = json.loads(tools.list_watchlist(analyst_ctx))
    assert [b["cert"] for b in got] == [int(c) for c in s.loc[pick].sort_values("rank")["cert"]]


def test_ask_passes_max_iterations_and_sums_usage(analyst_ctx):
    from types import SimpleNamespace

    from analyst_fakes import _Runner
    from canary.analyst.writer import cost_usd

    turns = [fake_message("", stop_reason="tool_use", input_tokens=100, output_tokens=10),
             fake_message("final answer", input_tokens=200, output_tokens=20)]
    for t in turns:
        t.model = DEFAULT_MODEL

    class Runner(_Runner):
        def __iter__(self):
            yield from turns

    client = FakeClient([])
    client.beta.messages.tool_runner = lambda **kw: (client.runner_calls.append(kw), Runner(turns[-1]))[1]
    text, usage = agent.ask_with_usage("q", analyst_ctx, client)
    assert text == "final answer"
    assert client.runner_calls[0]["max_iterations"] == 10
    assert usage["input_tokens"] == 300 and usage["output_tokens"] == 30
    assert usage["cost_usd"] == pytest.approx(cost_usd(DEFAULT_MODEL, 300, 30))


def test_ask_stopped_at_max_iterations(analyst_ctx):
    client = FakeClient([fake_message("partial", stop_reason="tool_use")])
    assert agent.ask("q", analyst_ctx, client) == "partial\n" + agent.STOPPED_LINE


def test_cli_ask_prints_usage(analyst_ctx, monkeypatch, capsys):
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: FakeClient([fake_message("the answer")]))
    assert cli.main(["ask", "q"]) == 0
    out = capsys.readouterr()
    assert "the answer" in out.out and "1,000 in / 500 out tokens" in out.err and "$" in out.err


def test_cli_ask_api_error_exits_1(analyst_ctx, monkeypatch, capsys):
    import anthropic

    err = anthropic.APIConnectionError(request=SimpleNamespace(method="POST", url="https://x"))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    client = FakeClient([])

    def boom(**kw):
        raise err

    client.beta.messages.tool_runner = boom
    monkeypatch.setattr(cli, "make_client", lambda: client)
    assert cli.main(["ask", "q"]) == 1
    err_out = capsys.readouterr().err
    assert "Claude API call failed (APIConnectionError)" in err_out and len(err_out.strip().splitlines()) == 1
