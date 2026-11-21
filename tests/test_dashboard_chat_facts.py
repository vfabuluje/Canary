"""Ask Canary lookup tools and the per-visit fact ledger."""

import json

import pytest

from canary.dashboard import data
from canary.dashboard.chat_facts import (
    TOOL_SPECS, FactLedger, bank_profile, bank_report, canary_facts, failures, find_bank, run_tool, watchlist,
)
from tests.dashboard_fixtures import REAL_DATA, write_fixture_data

UNSCORED = 9      # Union Trust Co, stopped reporting 2007
NO_REPORT = 35    # scored, no written report


@pytest.fixture
def real_data(monkeypatch):
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(REAL_DATA))


@pytest.fixture
def fixture_data(tmp_path, monkeypatch):
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(write_fixture_data(tmp_path)))


def test_ids_continue_across_tools(real_data):
    led = FactLedger()
    a = find_bank(led, "silicon valley")
    b = bank_profile(led, 24735)
    ids = [f["id"] for f in a["facts"]] + [f["id"] for f in b["facts"]]
    assert ids == [f"F{i}" for i in range(1, len(ids) + 1)]


def test_svb_profile_last_rank(real_data):
    led = FactLedger(); out = bank_profile(led, 24735)
    disp = {f["label"]: f["display"] for f in out["facts"] if f["quarter"] == "2022-12-31"}
    assert "3,494" in disp.values() and "4,773" in disp.values()
    rank = next(f for f in led.facts.values() if f.value == 3494)
    assert {"3,494", "3494", "#3,494"} <= set(rank.forms)


def test_failures_2023_lists_all_five(real_data):
    out = failures(FactLedger(), year=2023)
    assert {r["cert"] for r in out["rows"]} == {8758, 24735, 25851, 57053, 59017}


def test_watchlist_state_filter_and_cap(real_data):
    out = watchlist(FactLedger(), state="TX")
    assert all(r["state"] == "TX" for r in out["rows"]) and len(out["rows"]) <= 25
    assert "error" not in watchlist(FactLedger(), quarter="Q4 2022")


def test_bank_report_is_slim_and_reids(real_data):
    led = FactLedger(); led.add("x", 1, "1", ["1"], "t")
    out = bank_report(led, 24735)
    assert set(out["facts"][0]) == {"id", "label", "quarter", "display", "hindsight"}
    assert out["facts"][0]["id"] == "F2"
    assert "note_md" not in json.dumps(out)
    assert len(json.dumps(out)) < 40_000
    assert led.bank_of["F2"] == (24735, "Silicon Valley Bank")


def test_canary_facts(real_data):
    led = FactLedger(); out = canary_facts(led)
    assert any(f["display"] == "21" for f in out["facts"])
    assert out["how_it_works"] and out["why_2023_missed"]


def test_unscored_and_no_report_and_bad_input(fixture_data):
    led = FactLedger()
    assert "note" in bank_profile(led, UNSCORED) and "2007" in bank_profile(led, UNSCORED)["note"]
    assert "error" in bank_report(led, NO_REPORT)
    assert "error" in bank_profile(led, 999999999)
    assert "error" in watchlist(led, quarter="1999-03-31")
    assert "error" in run_tool(led, "write_memo", {})
    assert "error" in run_tool(led, "bank_profile", {"cert": "x"})
    assert "error" in run_tool(led, "bank_profile", {"nope": 1})
    json.dumps(run_tool(led, "bank_profile", {"cert": 24735, "start": None, "end": None}))


def test_ledger_round_trips_state():
    led = FactLedger(); led.add("Rank", 5, "5", ["5"], "t", cert=1, bank="A")
    back = FactLedger.from_state(json.loads(json.dumps(led.to_state())))
    assert back.facts.keys() == led.facts.keys() and back.bank_of == led.bank_of
    assert back.add("n", 1, "1", [], "t").id == "F2"


def test_tool_specs_are_strict_and_closed():
    assert {t["name"] for t in TOOL_SPECS} == {"find_bank", "bank_profile", "bank_report", "failures", "watchlist", "canary_facts"}
    for t in TOOL_SPECS:
        sch = t["input_schema"]
        assert t["strict"] and sch["additionalProperties"] is False
        assert set(sch["required"]) == set(sch["properties"])
