"""Ask Canary lookup tools and the per-visit fact ledger."""

import json
import re

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


# ---- the answer checker accepts natural sentences built from tool facts -----------------------------------------

def _check(led, text, ids):
    from canary.analyst.checker import _check_sentence
    from canary.analyst.sections import Section
    spec = Section("outcome", "Outcome", "hindsight", "", True)
    return _check_sentence("outcome", spec, {"text": text, "cites": ids}, led.facts)


def _ids(led, out, label=None):
    return [f["id"] for f in out["facts"] if label is None or f["label"] == label]


@pytest.mark.parametrize("text", [
    "Silicon Valley Bank failed on March 10, 2023.",
    "Silicon Valley Bank failed on Mar 10, 2023.",
    "Silicon Valley Bank failed in March 2023.",
])
def test_failure_date_spellings_pass_after_find_bank_and_profile(real_data, text):
    led = FactLedger()
    assert _check(led, text, _ids(led, find_bank(led, "silicon valley"))) == []
    led = FactLedger()
    assert _check(led, text, _ids(led, bank_profile(led, 24735))) == []


def test_stopped_reporting_year_is_checkable(fixture_data):
    led = FactLedger()
    out = bank_profile(led, UNSCORED)
    assert _check(led, "Union Trust stopped reporting in 2007.", _ids(led, out, "Status")) == []


def test_watchlist_n_of_m_passes(real_data):
    led = FactLedger(); out = watchlist(led)
    r = out["rows"][0]
    text = f"{r['name']} ranked {r['rank']:,} of {r['n_banks']:,} banks."
    assert _check(led, text, r["fact_ids"] + _ids(led, out, "Banks ranked that quarter")) == []


def test_three_years_concentration_passes_and_unsupported_fails(real_data):
    led = FactLedger(); out = bank_profile(led, 24735)
    ids = _ids(led, out, "Loan growth over three years, %")
    assert _check(led, "Loans grew 953.0% over three years.", ids) == []
    assert _check(led, "Loans grew 777.0% over three years.", ids) != []


def test_bad_range_errors_before_issuing_facts(real_data):
    led = FactLedger()
    assert "error" in bank_profile(led, 24735, start="soon")
    assert not led.facts


def test_watchlist_share_matches_the_model():
    """Task 2: the flag rule the chat states is the model's own WATCHLIST_SHARE."""
    metrics = pytest.importorskip("canary.model.metrics")
    from canary.dashboard.chat_facts import WATCHLIST_SHARE_PCT
    assert WATCHLIST_SHARE_PCT == pytest.approx(metrics.WATCHLIST_SHARE * 100)


def test_run_tool_logs_the_type_of_an_unexpected_error(monkeypatch, caplog):
    from canary.dashboard import chat_facts

    def boom(ledger, **kw):
        raise ZeroDivisionError("secret detail")
    monkeypatch.setitem(chat_facts._TOOLS, "canary_facts", boom)
    with caplog.at_level("WARNING", logger=chat_facts.__name__):
        out = run_tool(FactLedger(), "canary_facts", {})
    assert out == {"error": "canary_facts failed: ZeroDivisionError."}
    assert any("canary_facts" in r.getMessage() and "ZeroDivisionError" in r.getMessage() for r in caplog.records)
    assert not any("secret detail" in r.getMessage() for r in caplog.records)


# ---- smoke-test fixes (2026-11-21): the exact sentences the paid smoke test's checks rejected --------------------

FLAG_RULE = "Flag rule: share of banks flagged each quarter"
MISSED_2023 = "Year the three large US banks Canary did not flag in time collapsed"
CRISIS_YEARS = "Years most training failures came from (the 2008 crisis)"
TRAIN_YEARS = "Training data: bank reports from these years"
TEST_YEARS = "Test years: failures and reports scored"
HORIZON = "Score horizon: failing within the next four quarters"


def _label_id(led, label, cert=None):
    return next(f.id for f in led.facts.values()
                if f.label == label and (cert is None or led.bank_of.get(f.id, (None,))[0] == cert))


def _case_ids(led, cert):
    return [i for i, f in led.facts.items() if led.bank_of.get(i, (None,))[0] == cert]


def _chat_check(led, text, ids):
    """The chat's full answer check (chat._check: scale-anchor phrases, citation checker, wording, links)."""
    from canary.dashboard.chat import _check as chat_check
    return chat_check({"sections": [{"key": "answer", "paragraphs": [
        {"sentences": [{"text": text, "cites": list(ids)}]}]}]}, led)


def _latest_ids(led):
    return [_label_id(led, f"Latest {x}") for x in
            ("National rank (1 = highest score)", "Banks ranked that quarter", "Percentile (100 = highest risk)")]


def test_percentile_scale_anchor_passes(real_data):
    """Cause 1: the scale anchor "100 = highest risk" may be repeated beside the percentile."""
    led = FactLedger(); canary_facts(led)
    assert _chat_check(led, "Canary's last score for Silicon Valley Bank was for December 31, 2022, when it ranked "
                            "3,494 of 4,773 banks, at the 26.8% percentile (100 is highest risk).",
                       _case_ids(led, 24735)) == []
    assert _chat_check(led, "On that date it ranked 246 of 4,773 banks scored, which is a percentile of 94.9%, where "
                            "100 means the highest risk.", _case_ids(led, 57053)[1:]) == []
    led = FactLedger(); bank_profile(led, 24735)
    assert _chat_check(led, "In that quarter it ranked 3,494 of 4,773 banks, a percentile of 26.8%, where 100 means "
                            "the highest risk.", _latest_ids(led)) == []


def test_rank_scale_anchor_passes_after_watchlist(real_data):
    """Cause 1: the scale anchor "1 = highest score" may be repeated beside the rank."""
    led = FactLedger(); out = watchlist(led, state="TX")
    r = out["rows"][0]
    assert (r["name"], r["rank"], r["n_banks"]) == ("Transpecos Banks Ssb", 6, 4313)
    ids = [r["fact_ids"][2]] + _ids(led, out, "Banks ranked that quarter")
    assert _chat_check(led, "Its national rank is 6, where 1 is the highest score, out of 4,313 banks ranked that "
                            "quarter.", ids) == []


def test_report_percentile_scale_anchor_passes(real_data):
    led = FactLedger(); bank_report(led, 24735)
    pct = next(f for f in led.facts.values() if f.label == "Percentile (100 = highest risk)")
    assert _chat_check(led, f"Its percentile was {pct.display}, where 100 means the highest risk.", [pct.id]) == []


def test_label_digits_never_pass_as_a_banks_rank_or_percentile(real_data):
    """Fix round 1 (review probes): a label's scale anchor or window size is not a figure about the bank."""
    led = FactLedger(); out = watchlist(led, state="TX")
    r = out["rows"][0]
    name, rank = r["fact_ids"][0], r["fact_ids"][2]
    n = _label_id(led, "Banks ranked that quarter")
    assert _chat_check(led, "Transpecos Banks Ssb ranked 1 of 4,313 banks that quarter.", [name, rank, n])  # a1
    assert _chat_check(led, "Transpecos Banks Ssb is the No. 1 riskiest bank in the country.", [name, rank])  # a2
    assert _chat_check(led, "Transpecos Banks Ssb ranked 1, where 1 is the highest score.", [name, rank])
    led = FactLedger(); bank_profile(led, 24735)
    ids = _latest_ids(led)
    assert _chat_check(led, "Its percentile was 100.", [ids[2]])  # a5
    assert _chat_check(led, "In that quarter it ranked 1 of 4,773 banks, a percentile of 26.8%.", ids)  # a6
    led = FactLedger(); bank_profile(led, 628)
    assert _chat_check(led, "Jpmorgan Chase Bank Na ranked 1 of 4,313 banks in the latest quarter, a percentile of "
                            "100.", [_label_id(led, "Bank name")] + _latest_ids(led))  # a9
    led = FactLedger(); bank_report(led, 24735)
    driver = next(f.id for f in led.facts.values() if f.label.startswith("Driver up #1"))
    assert _chat_check(led, "Silicon Valley Bank was the #1 riskiest bank in the country.", [driver])  # a10
    # a11/a12 (the percentile-scale and comparison-window facts) carry "100" and "8" in the written report's own
    # forms, from the analyst pipeline, not from their labels; import_report adds no label digit to them.
    report = {f["label"]: f["forms"] for f in data.report(24735)["facts"]}
    for f in led.facts.values():
        added = set(f.forms) - set(report[f.label])
        assert all(re.fullmatch(r"(?:19|20)\d\d", x) or not re.search(r"\d", x) for x in added), (f.label, added)


def test_a_number_in_no_cited_fact_still_fails(real_data):
    led = FactLedger(); canary_facts(led)
    assert any("'50' is not supported" in e for e in
               _chat_check(led, "It ranked 3,494 of 4,773 banks, where 50 means the middle.", _case_ids(led, 24735)))


def test_anchor_errors_quote_the_original_sentence(real_data):
    led = FactLedger(); out = watchlist(led, state="TX")
    text = "Transpecos Banks Ssb ranked 1, where 1 is the highest score."
    [err] = _chat_check(led, text, [out["rows"][0]["fact_ids"][2]])
    assert f'sentence "{text}"' in err and "'1' is not supported" in err


def test_label_wording_that_is_not_a_figure_is_not_a_form():
    """Project phase names and the post-hoc label's '2023' are wording, not figures (the checker ignores the
    post-hoc label in text the same way)."""
    from canary.analyst.facts import POSTHOC_LABEL
    led = FactLedger()
    phase = led.add("First flag quarter (Phase 3 lead-time rule)", "2022-03-31", "Q1 2022", [], "t")
    posthoc = led.add(f"Rank ({POSTHOC_LABEL})", 5, "5", ["5"], "t")
    assert "3" not in phase.forms and "2023" not in posthoc.forms
    # only years and spelled spans: never a scale anchor, a window size or a driver number
    rank = led.add("National rank (1 = highest score)", 6, "6", ["6"], "t")
    window = led.add("Comparison window: the prior 12 quarters (at least 8 with a value), 2016-2024", 1, "x", [], "t")
    driver = led.add("Driver up #1: a ratio", 0.5, "0.5", [], "t")
    assert "1" not in rank.forms and "#1" not in driver.forms
    assert {"12", "8"}.isdisjoint(window.forms) and {"2016", "2024"} <= set(window.forms)


def test_background_years_are_facts_and_pass(real_data):
    """Cause 2: the years in canary_facts' own story are facts the answer can cite."""
    led = FactLedger(); canary_facts(led)
    assert _check(led, "Canary did not flag any of the three large US banks that collapsed in 2023 in time.",
                  [_label_id(led, MISSED_2023)]) == []
    assert _check(led, "Canary's model was built mostly on the 2008 crisis, when banks failed from bad loans.",
                  [_label_id(led, CRISIS_YEARS)]) == []
    crisis = led.facts[_label_id(led, CRISIS_YEARS)]
    assert {"2008", "2012", "2008-2012", "2008 to 2012"} <= set(crisis.forms)
    assert _check(led, "Canary was trained on bank reports from 2001 to 2014 and tested on 2016 to 2024.",
                  [_label_id(led, TRAIN_YEARS), _label_id(led, TEST_YEARS)]) == []
    assert _check(led, "The score ranks banks by risk of failing within a year.", [_label_id(led, HORIZON)]) == []
    horizon = led.facts[_label_id(led, HORIZON)]
    assert horizon.display == "four quarters" and "4" not in horizon.forms
    assert _check(led, "The score covers failing within the next four quarters.", [horizon.id]) == []
    # a background year still needs its fact: 2009 is in no canary_facts fact
    assert _check(led, "Most of those failures came in 2009.", [_label_id(led, CRISIS_YEARS)]) != []


def test_every_number_in_canary_facts_text_has_a_fact(real_data):
    from canary.analyst.checker import _norm, _tokens
    led = FactLedger(); out = canary_facts(led)
    forms = {_norm(x) for f in led.facts.values() for x in f.forms}
    text = " ".join([out["how_it_works"], out["why_2023_missed"], *out["case_studies"]])
    missing = [t.raw for t in _tokens(text) if t.norm not in forms]
    assert missing == []


def test_training_years_match_the_model():
    dataset = pytest.importorskip("canary.model.dataset")
    from canary.dashboard import chat_facts
    assert chat_facts.TRAIN_REPORT_YEARS[1] == dataset.TRAIN_END.year
    assert chat_facts.TEST_YEARS == (dataset.TEST_START.year, dataset.TEST_END.year)


def test_watchlist_issues_the_flag_rule(real_data):
    """Cause 3: after only a watchlist lookup, the 2% flag rule is citable."""
    led = FactLedger(); watchlist(led, state="TX")
    rule = led.facts[_label_id(led, FLAG_RULE)]
    ref = FactLedger(); canary_facts(ref)
    want = ref.facts[_label_id(ref, FLAG_RULE)]
    assert (rule.value, rule.display) == (want.value, want.display) == (2, "2%")
    assert "2" not in rule.forms  # "2%" only: a bare 2 would pass as a rank
    assert _check(led, "The watchlist covers the riskiest 2% of banks Canary ranks, so it is a list of banks flagged "
                       "for closer attention, not a prediction that any bank will fail.", [rule.id]) == []


# ---- fix round 3: the number of rows a capped list shows is a fact --------------------------------------------------

def test_failures_rows_shown_is_a_fact(real_data):
    """Q7 of the second paid smoke run."""
    led = FactLedger(); out = failures(led, year=2010)
    assert (out["total"], len(out["rows"])) == (157, 25)
    first, last = out["rows"][0]["fact_ids"][2], out["rows"][-1]["fact_ids"][2]
    ids = [_label_id(led, "Number of failed banks in this list"), _label_id(led, "Failures shown in this list"),
           first, last]
    assert _check(led, "The list shows 25 of those failures, sorted by date, from October 22, 2010 to December 17, "
                       "2010.", ids) == []


def test_watchlist_and_find_bank_rows_shown_are_facts(real_data):
    led = FactLedger(); out = watchlist(led)
    shown = led.facts[_label_id(led, "Banks shown in this list")]
    assert shown.value == len(out["rows"])
    led = FactLedger(); out = find_bank(led, "first")
    shown = led.facts[_label_id(led, "Matches shown in this list")]
    assert shown.value == len(out["matches"])
