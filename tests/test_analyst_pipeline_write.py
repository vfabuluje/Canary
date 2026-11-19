"""write_memo as a three-call pipeline (trend, peer, analyst) with traces. No network: FakeClient."""

import json

import pytest

from analyst_fakes import FakeClient, fake_agent_memo, fake_agent_memos, fake_message
from canary.analyst import tools
from canary.analyst.facts import build_fact_sheet
from canary.analyst.pipeline import agent_sections
from canary.analyst.render import note_path
from canary.analyst.writer import DEFAULT_MODEL, RefusalError, cost_usd, write_memo

FULL = 100      # trend, peer and analyst all get a call
NO_PEER = 3     # peers is code-only: two calls

TRACE_KEYS = {"agent", "attempt", "request", "response_text", "checker_errors", "input_tokens",
              "output_tokens", "cost_usd", "served_model", "source"}


def _sheet(ctx, cert, tmp_path):
    return build_fact_sheet(ctx, cert, replay_dir=tmp_path / "none")


def _run(ctx, cert, tmp_path, responses, **kw):
    client = FakeClient(responses)
    res = write_memo(ctx, cert, client=client, out_dir=tmp_path / "banks", replay_dir=tmp_path / "none",
                     trace_dir=tmp_path / "traces", **kw)
    return res, client


def _enum(call):
    return call["output_config"]["format"]["schema"]["properties"]["sections"]["items"]["properties"]["key"]["enum"]


def _bad(memo):
    """A memo that fails the checker: a number with no cite."""
    memo["sections"][0]["paragraphs"][0]["sentences"].append({"text": "It was 987654 times worse.", "cites": []})
    return memo


def test_three_calls_in_order(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    res, client = _run(analyst_ctx, FULL, tmp_path, fake_agent_memos(sheet))
    assert res.ok and res.attempts == 1 and len(client.calls) == 3
    assert _enum(client.calls[0]) == ["trends"] and _enum(client.calls[1]) == ["peers"]
    assert _enum(client.calls[2]) == [s.key for s in agent_sections(sheet, "analyst")]
    assert [c["system"].split(".")[0] for c in client.calls] == [
        "You are Canary's trend agent", "You are Canary's peer agent", "You are Canary's risk analyst"]
    assert set(res.agents) == {"trend", "peer", "analyst"} and not any(a.skipped for a in res.agents.values())
    # the analyst saw both specialists' text
    user = client.calls[2]["messages"][0]["content"]
    assert "The trends section reads calmly." in user and "The peers section reads calmly." in user


def test_specialist_text_verbatim_in_note(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    memos = fake_agent_memos(sheet)
    trend_text = "Equity thinned out quarter after quarter, in plain words."
    peer_text = "Against similar banks it looked unremarkable."
    memos[0]["sections"][0]["paragraphs"][0]["sentences"][0]["text"] = trend_text
    memos[1]["sections"][0]["paragraphs"][0]["sentences"][0]["text"] = peer_text
    res, _ = _run(analyst_ctx, FULL, tmp_path, memos)
    assert res.ok
    note = res.path.read_text()
    assert trend_text in note and peer_text in note
    assert res.agents["trend"].memo == memos[0] and res.agents["peer"].memo == memos[1]
    assert "The summary section reads calmly." in note


def test_code_only_specialist_skipped(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, NO_PEER, tmp_path)
    assert "peers" in sheet.code_only
    res, client = _run(analyst_ctx, NO_PEER, tmp_path, fake_agent_memos(sheet))
    assert res.ok and len(client.calls) == 2
    assert _enum(client.calls[0]) == ["trends"] and "peers" not in _enum(client.calls[1])
    assert res.agents["peer"].skipped and res.agents["peer"].ok and res.agents["peer"].attempts == 0
    assert "peers" in client.calls[1]["messages"][0]["content"]  # the analyst is told it is code-only


def test_specialist_retry_then_ok(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    trend, peer, analyst = fake_agent_memos(sheet)
    res, client = _run(analyst_ctx, FULL, tmp_path, [_bad(fake_agent_memo(sheet, "trend")), trend, peer, analyst])
    assert res.ok and len(client.calls) == 4
    assert res.agents["trend"].attempts == 2 and res.agents["peer"].attempts == 1 and res.attempts == 2
    assert "987654" in client.calls[1]["messages"][-1]["content"]  # the retry carries the checker errors
    assert res.first_errors and all(e.startswith("[trend] ") for e in res.first_errors)
    assert res.errors == []


def test_specialist_fails_twice_no_analyst_call_no_note(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    path = note_path(tmp_path / "banks", sheet.name, FULL)
    path.parent.mkdir(parents=True)
    path.write_bytes(b"existing note, do not touch")
    bad = lambda: _bad(fake_agent_memo(sheet, "peer"))  # noqa: E731
    trend = fake_agent_memo(sheet, "trend")
    res, client = _run(analyst_ctx, FULL, tmp_path, [trend, bad(), bad()])
    assert not res.ok and res.path is None and len(client.calls) == 3  # no analyst call
    assert not any("risk analyst" in c["system"] for c in client.calls)
    assert path.read_bytes() == b"existing note, do not touch"
    assert res.errors and all(e.startswith("[peer] ") for e in res.errors)
    assert "analyst" not in res.agents
    assert res.attempts == 2


def test_analyst_fails_twice_no_note(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    trend, peer, _ = fake_agent_memos(sheet)
    bad = fake_agent_memo(sheet, "analyst", rank_text="999,999")
    res, client = _run(analyst_ctx, FULL, tmp_path, [trend, peer, bad, bad])
    assert not res.ok and res.path is None and len(client.calls) == 4
    assert not (tmp_path / "banks").exists() or not any((tmp_path / "banks").iterdir())
    assert any(e.startswith("[analyst] ") and "999,999" in e for e in res.errors)


def test_trace_written(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    memos = fake_agent_memos(sheet)
    res, client = _run(analyst_ctx, FULL, tmp_path, memos)
    f = tmp_path / "traces" / f"{FULL}_{sheet.as_of.isoformat()}.json"
    data = json.loads(f.read_text())
    calls = data["calls"]
    assert data["ok"] is True and [c["agent"] for c in calls] == ["trend", "peer", "analyst"]
    for c, kw, memo in zip(calls, client.calls, memos):
        assert TRACE_KEYS <= set(c) and c["source"] == "direct" and c["attempt"] == 1
        assert c["request"]["messages"] == kw["messages"] and c["request"]["model"] == DEFAULT_MODEL
        assert json.loads(c["response_text"]) == memo and c["checker_errors"] == []
        assert c["input_tokens"] == 1000 and c["output_tokens"] == 500
        assert c["cost_usd"] == pytest.approx(cost_usd(DEFAULT_MODEL, 1000, 500))
        assert c["served_model"] == DEFAULT_MODEL


def test_trace_written_on_failure(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    bad = _bad(fake_agent_memo(sheet, "trend"))
    res, _ = _run(analyst_ctx, FULL, tmp_path, [bad, bad])
    data = json.loads((tmp_path / "traces" / f"{FULL}_{sheet.as_of.isoformat()}.json").read_text())
    assert data["ok"] is False and [(c["agent"], c["attempt"]) for c in data["calls"]] == [("trend", 1), ("trend", 2)]
    assert data["calls"][0]["checker_errors"] and data["calls"][1]["checker_errors"]
    # and when a call raises
    with pytest.raises(RefusalError):
        _run(analyst_ctx, FULL, tmp_path, [fake_agent_memo(sheet, "trend"), fake_message("", stop_reason="refusal")])
    data = json.loads((tmp_path / "traces" / f"{FULL}_{sheet.as_of.isoformat()}.json").read_text())
    assert [c["agent"] for c in data["calls"]] == ["trend", "peer"] and data["ok"] is False


def test_batch_first_memo_traced_as_batch(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    trend, peer, analyst = fake_agent_memos(sheet)
    res, client = _run(analyst_ctx, FULL, tmp_path, [peer, analyst], first_memos={"trend": trend})
    assert res.ok and len(client.calls) == 2
    data = json.loads((tmp_path / "traces" / f"{FULL}_{sheet.as_of.isoformat()}.json").read_text())
    assert [c["source"] for c in data["calls"]] == ["batch", "direct", "direct"]
    assert res.input_tokens == 2000  # the batch memo's cost is the caller's to count


def test_usage_summed_and_on_exception(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    res, _ = _run(analyst_ctx, FULL, tmp_path, fake_agent_memos(sheet))
    assert res.input_tokens == 3000 and res.output_tokens == 1500
    assert res.cost_usd == pytest.approx(3 * cost_usd(DEFAULT_MODEL, 1000, 500))
    assert res.agents["peer"].input_tokens == 1000
    with pytest.raises(RefusalError) as info:  # refusal in the peer call: trend + peer usage reported
        _run(analyst_ctx, FULL, tmp_path, [fake_agent_memo(sheet, "trend"), fake_message("", stop_reason="refusal")])
    u = info.value.usage
    assert u["input_tokens"] == 2000 and u["output_tokens"] == 1000
    assert u["cost_usd"] == pytest.approx(2 * cost_usd(DEFAULT_MODEL, 1000, 500)) and u["model"] == DEFAULT_MODEL
    with pytest.raises(RuntimeError) as info:  # an API error in the analyst call: earlier calls' usage
        _run(analyst_ctx, FULL, tmp_path, [*fake_agent_memos(sheet)[:2], RuntimeError("down")])
    assert info.value.usage["input_tokens"] == 2000


def test_ask_write_memo_tool_uses_pipeline(analyst_ctx, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)  # the tool writes to ./banks
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    client = FakeClient(fake_agent_memos(sheet))
    out = json.loads(tools.write_memo_tool(analyst_ctx, client, DEFAULT_MODEL, FULL))
    assert out["ok"] is True and out["errors"] == [] and out["attempts"] == 1 and len(client.calls) == 3
    assert out["path"].startswith("banks/")
    assert (tmp_path / out["path"]).exists()


def test_before_call_fires_per_direct_call_and_can_stop(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, FULL, tmp_path)
    memos = fake_agent_memos(sheet)
    seen = []
    res, client = _run(analyst_ctx, FULL, tmp_path, memos, before_call=lambda a, n: seen.append((a, n)))
    assert res.ok and len(client.calls) == len(seen) == 3
    assert [a for a, _ in seen] == ["trend", "peer", "analyst"] and all(n == 1 for _, n in seen)

    def stop(agent, attempt):
        if attempt == 2:
            raise RuntimeError("limit")

    client = FakeClient([memos[0], memos[1], _bad(fake_agent_memo(sheet, "analyst"))])
    with pytest.raises(RuntimeError, match="limit"):
        write_memo(analyst_ctx, FULL, client=client, out_dir=tmp_path / "b2", replay_dir=tmp_path / "none",
                   trace_dir=tmp_path / "t2", before_call=stop)
    assert len(client.calls) == 3  # the retry call was never made
