from datetime import date

import pandas as pd

from canary.analyst.checker import check_memo
from canary.analyst.concentration import CONCENTRATION_KEY, LEAD, ConcentrationResult
from canary.analyst.facts import PERCENTILE_SCALE_LABEL, Fact, FactSheet
from canary.analyst.outcome import Outcome
from canary.analyst.pipeline import (
    AGENT_SECTIONS, ANALYST_INSTRUCTION, agent_sections, agent_sheet, build_agent_request,
)
from canary.analyst.sections import sections_for
from canary.analyst.writer import SYSTEM_PROMPT, SHARED_RULES

AS_OF = date(2022, 12, 31)


def _f(id, label, value, display, kind=None, feature=None):
    return Fact(id, label, AS_OF, value, display, [display], False, "src", feature, kind)


def make_sheet(code_only=()):
    facts = [
        _f("F1", "Bank name", "X Bank", "X Bank"),
        _f("F2", "Certificate number", 1, "1"),
        _f("F3", "As-of quarter", "2022-12-31", "2022-12-31"),
        _f("F4", "National rank (1 = highest score)", 5, "5"),
        _f("F5", "Banks ranked that quarter", 4000, "4,000"),
        _f("F6", "Percentile (100 = highest risk)", 99.0, "99.0%"),
        _f("F7", PERCENTILE_SCALE_LABEL, 100, "0 to 100"),
        _f("F8", "On the watchlist", "yes", "flagged"),
        _f("T1", "Equity trend", 1.5, "1.5%", "trend_change", "eq"),
        _f("P1", "Equity peer median", 9.1, "9.1%", "peer_median", "eq"),
        _f("D1", "Driver up", 0.7, "0.7", None, "eq"),
    ]
    o = Outcome("quiet", False, None, None, None, True, AS_OF)
    empty = pd.DataFrame()
    conc = ConcentrationResult(AS_OF, "rbc_2006", 120.0, 310.0, 60.0)
    return FactSheet(1, "X Bank", AS_OF, o, facts, empty, empty, "", [s.key for s in sections_for_keys(o)],
                     set(code_only), {CONCENTRATION_KEY: conc})


def sections_for_keys(o):
    class _S:  # sections_for only reads outcome.kind and code_only
        outcome = o
        code_only = set()
    return sections_for(_S)


def ids(sheet):
    return [f.id for f in sheet.facts]


def test_trend_subset_has_trend_and_identity_facts_only():
    s = make_sheet()
    sub = agent_sheet(s, "trend")
    assert ids(sub) == ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "T1"]
    assert ids(s) == [f.id for f in s.facts] and len(s.facts) == 11  # original untouched
    assert sub is not s and sub.facts is not s.facts


def test_peer_subset():
    sub = agent_sheet(make_sheet(), "peer")
    assert ids(sub) == ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "P1"]


def test_analyst_sheet_unchanged():
    s = make_sheet()
    assert ids(agent_sheet(s, "analyst")) == ids(s)


def test_agent_sections_split():
    s = make_sheet()
    assert [x.key for x in agent_sections(s, "trend")] == ["trends"]
    assert [x.key for x in agent_sections(s, "peer")] == ["peers"]
    keys = [x.key for x in agent_sections(s, "analyst")]
    assert "trends" not in keys and "peers" not in keys and CONCENTRATION_KEY not in keys
    assert keys == ["summary", "warning_signs", "score", "what_next"]
    s2 = make_sheet(code_only={"trends"})
    assert agent_sections(s2, "trend") == []
    assert [x.key for x in agent_sections(s2, "peer")] == ["peers"]


def test_specialist_request_schema_only_its_section():
    s = make_sheet()
    req = build_agent_request(s, "trend", "claude-opus-5-5")
    enum = req["output_config"]["format"]["schema"]["properties"]["sections"]["items"]["properties"]["key"]["enum"]
    assert enum == ["trends"]
    assert req["system"].startswith("You are Canary's trend agent")
    assert SHARED_RULES in req["system"]
    msg = req["messages"][0]["content"]
    assert "T1" in msg and "P1" not in msg and "D1" not in msg
    assert "peers" not in msg.split("Write this section")[1]
    assert build_agent_request(s, "peer", "m")["system"].startswith("You are Canary's peer agent")
    assert build_agent_request(s, "analyst", "m")["system"] == SYSTEM_PROMPT


def test_specialist_retry_appends_errors():
    req = build_agent_request(make_sheet(), "trend", "m", errors=["bad"], previous={"sections": []})
    assert [m["role"] for m in req["messages"]] == ["user", "assistant", "user"]
    assert "bad" in req["messages"][2]["content"]


MEMO = {"sections": [{"key": "trends", "paragraphs": [{"sentences": [
    {"text": "Equity changed by 1.5% over the year.", "cites": ["T1"]}]}]}]}


def test_analyst_request_contains_specialist_text_and_instruction():
    s = make_sheet(code_only={"peers"})
    req = build_agent_request(s, "analyst", "m", specialist_memos={"trend": MEMO})
    msg = req["messages"][0]["content"]
    assert ANALYST_INSTRUCTION in msg
    assert "The trend, peer and concentration sections are written by other agents or code" in msg
    assert "Equity changed by 1.5% over the year." in msg and "T1" in msg.split("Equity changed")[1]
    assert LEAD in msg
    assert "code-only" in msg and "peers" in msg.split("code-only")[1]
    enum = req["output_config"]["format"]["schema"]["properties"]["sections"]["items"]["properties"]["key"]["enum"]
    assert "trends" not in enum and "peers" not in enum


def test_specialist_cite_outside_subset_rejected():
    s = make_sheet()
    memo = {"sections": [{"key": "trends", "paragraphs": [{"sentences": [
        {"text": "Drivers were 0.7 in size.", "cites": ["D1"]}]}]}]}
    secs = agent_sections(s, "trend")
    assert check_memo(memo, s, secs) == []  # full sheet knows D1 ...
    assert check_memo(memo, agent_sheet(s, "trend"), secs) != []  # ... the subset does not


def test_analyst_can_cite_specialist_fact():
    s = make_sheet()
    secs = agent_sections(s, "analyst")

    def memo(cites):
        sents = [{"text": "Equity changed by 1.5% over the year.", "cites": cites}]
        return {"sections": [{"key": k, "paragraphs": [{"sentences": sents}] if k == "summary" else []}
                             for k in ("summary", "warning_signs", "score", "what_next")]}
    assert check_memo(memo(["T1"]), s, secs) == []
    assert check_memo(memo([]), s, secs) != []
