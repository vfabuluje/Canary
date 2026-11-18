from datetime import date

import pandas as pd
import pytest

from canary.analyst.checker import check_memo, extract_tokens
from canary.analyst.facts import Fact, FactSheet, date_forms
from canary.analyst.outcome import Outcome
from canary.analyst.sections import Section


def _fact(id, label, value, forms, quarter=None, hindsight=False):
    forms = list(forms) + (date_forms(quarter) if quarter else [])
    return Fact(id, label, quarter, value, str(value), forms, hindsight, "src")


def _sheet():
    facts = [
        _fact("F1", "Bond losses share", 0.9812, ["98.1%", "98%", "0.98"], date(2022, 12, 31)),
        _fact("F2", "Rank", 7, ["7", "#7", "7th"], date(2022, 12, 31)),
        _fact("F3", "Assets", 1.2e9, ["$1.2 billion", "1.2 billion"]),
        _fact("F4", "Failure date", "2023-03-10", [], date(2023, 3, 10), hindsight=True),
        _fact("F5", "Contribution", -0.1234, ["-0.123", "0.123"], date(2022, 12, 31)),
    ]
    empty = pd.DataFrame()
    return FactSheet(1, "X Bank", date(2022, 12, 31), None, facts, empty, empty, "", ["summary", "outcome"])


SECTIONS = [
    Section("summary", "Summary", "as_of", "", True),
    Section("outcome", "Outcome", "hindsight", "", True),
]


def _memo(text, cites, key="summary", other=True):
    secs = [{"key": key, "paragraphs": [{"sentences": [{"text": text, "cites": cites}]}]}]
    if other:
        secs.append({"key": "outcome", "paragraphs": []} if key == "summary" else {"key": "summary", "paragraphs": []})
    return {"sections": secs}


def run(text, cites):
    return check_memo(_memo(text, cites), _sheet(), SECTIONS)


def test_passes_when_numbers_match_cited_facts():
    assert run("Bond losses were 98% of equity.", ["F1"]) == []


def test_number_not_in_cited_fact():
    errs = run("Bond losses were 97% of equity.", ["F1"])
    assert len(errs) == 1
    assert "97%" in errs[0] and "Bond losses were 97%" in errs[0] and "summary" in errs[0]


def test_number_without_cites():
    errs = run("Bond losses were 98% of equity.", [])
    assert len(errs) == 1 and "no cites" in errs[0]


def test_no_number_no_cites_ok():
    assert run("This bank looks fragile.", []) == []


def test_unknown_id():
    errs = run("Bond losses were 98% of equity.", ["F1", "F99"])
    assert len(errs) == 1 and "F99" in errs[0]


def test_hindsight_fact_in_as_of_section():
    errs = run("Its last day was 2023-03-10.", ["F4"])
    assert len(errs) == 1 and "hindsight" in errs[0]


def test_hindsight_fact_ok_in_hindsight_section():
    memo = _memo("It failed on 2023-03-10.", ["F4"], key="outcome")
    assert check_memo(memo, _sheet(), SECTIONS) == []


@pytest.mark.parametrize("text", ["as of 2022-12-31", "in Q4 2022", "on December 31, 2022", "in 2022"])
def test_date_forms_pass(text):
    assert run(text, ["F1"]) == []


def test_uncited_year_fails():
    errs = run("in 2023", ["F1"])
    assert len(errs) == 1 and "2023" in errs[0]


def test_bare_four_digit_token_may_match_a_cited_form():  # controller ruling, round 1
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "Count", 2023, ["2,023", "2023"]))
    assert check_memo(_memo("in 2023", ["F6"]), sheet, SECTIONS) == []
    assert len(check_memo(_memo("in 2024", ["F6"]), sheet, SECTIONS)) == 1


def test_year_range_not_negative_number():
    assert extract_tokens("the 2016-2024 results") == ["2016", "2024"]


def test_extract_tokens_forms():
    assert extract_tokens("$1.2 billion, 1,234 banks, 98.1%, 2.5x, #7, 7th, +0.123, -0.5") == [
        "$1.2 billion", "1234", "98.1%", "2.5x", "#7", "7th", "+0.123", "-0.5"]
    assert extract_tokens("On December 31, 2022 and Q4 2022 and 2022-12-31.") == [
        "december 31, 2022".replace(",", ""), "q4 2022", "2022-12-31"]


def test_other_forms_pass():
    assert run("Assets were $1.2 billion, rank #7 (7th).", ["F2", "F3"]) == []
    assert run("Pushed down by -0.123 and 0.123.", ["F5"]) == []


def test_number_only_from_other_sentences_fact_fails():
    assert len(run("Rank was 7.", ["F1"])) == 1


def test_missing_and_unexpected_section():
    memo = {"sections": [{"key": "summary", "paragraphs": []}, {"key": "bogus", "paragraphs": []}]}
    errs = check_memo(memo, _sheet(), SECTIONS)
    assert any("outcome" in e and "missing" in e for e in errs)
    assert any("bogus" in e and "unexpected" in e for e in errs)


def _rank_sheet(value, q, forms):
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "Rank", value, forms, q))
    return sheet


def test_comma_count_equal_to_year_passes_against_rank_fact():
    sheet = _rank_sheet(2023, date(2023, 12, 31), ["2,023", "2023", "#2,023", "#2023"])
    sheet.facts.append(_fact("F7", "Banks", 4773, ["4,773", "4773"]))
    assert check_memo(_memo("It ranked 2,023 of 4,773 banks.", ["F6", "F7"]), sheet, SECTIONS) == []
    assert check_memo(_memo("It ranked #2,023.", ["F6"]), sheet, SECTIONS) == []
    assert check_memo(_memo("It ranked 2,023.", ["F6"]), sheet, SECTIONS) == []


def test_comma_number_not_accepted_as_year():
    sheet = _rank_sheet(1500, date(2019, 12, 31), ["1,500", "1500", "#1500"])
    assert len(check_memo(_memo("It ranked 2,019.", ["F6"]), sheet, SECTIONS)) == 1
    assert check_memo(_memo("in 2019", ["F6"]), sheet, SECTIONS) == []


def test_unicode_minus():
    pos = _fact("F6", "ROA", 5.0, ["5.0%", "+5.0%"])
    neg = _fact("F7", "ROA", -5.0, ["-5.0%"])
    sheet = _sheet()
    sheet.facts += [pos, neg]
    assert len(check_memo(_memo("ROA was −5.0%.", ["F6"]), sheet, SECTIONS)) == 1
    assert check_memo(_memo("ROA was −5.0%.", ["F7"]), sheet, SECTIONS) == []
    assert extract_tokens("2016–2024") == ["2016", "2024"]


@pytest.mark.parametrize("text", ["5bn", "1.5× cover", "10 bps", "3.5 trillion", "US$1.2 billion"])
def test_unknown_units_fail(text):
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "x", 5, ["5", "1.5", "10", "3.5", "1.2"]))
    assert len(check_memo(_memo(f"It was {text}.", ["F6", "F3"]), sheet, SECTIONS)) == 1


def test_times_sign_equals_x():
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "x", 1.5, ["1.5x"]))
    assert check_memo(_memo("Cover was 1.5×.", ["F6"]), sheet, SECTIONS) == []


@pytest.mark.parametrize("text", ["Q3-2022", "Q3 of 2022", "2022Q3", "September 2022", "in Q3"])
def test_wrong_quarter_or_month_fails(text):
    assert len(run(text, ["F1"])) == 1


@pytest.mark.parametrize("text", ["Q4 2022", "Q4-2022", "Q4 of 2022", "2022Q4", "December 2022", "in Q4", "in December"])
def test_right_quarter_or_month_passes(text):
    assert run(text, ["F1"]) == []


def test_wrong_year_with_quarter_fails():
    assert len(run("Q4 2023", ["F1"])) == 1


def test_posthoc_label_year_not_checked():
    from canary.analyst.facts import POSTHOC_LABEL

    sheet = _sheet()
    sheet.facts.append(_fact("F6", f"Run-risk rank ({POSTHOC_LABEL})", 42, ["42", "#42"],
                             date(2022, 12, 31), hindsight=True))
    text = f"On the run-risk rank ({POSTHOC_LABEL}), the bank was #42."
    assert check_memo(_memo(text, ["F6"], key="outcome"), sheet, SECTIONS) == []
    # Only the exact label is exempt: a stray 2023 elsewhere is still rejected.
    errs = check_memo(_memo(f"In 2023 the {POSTHOC_LABEL} put it at #42.", ["F6"], key="outcome"), sheet, SECTIONS)
    assert len(errs) == 1 and "'2023'" in errs[0]


# ---- final-review fixes ----------------------------------------------------------------

def _posthoc_sheet():
    from canary.analyst.facts import POSTHOC_LABEL

    sheet = _sheet()
    sheet.facts.append(_fact("F6", f"Run-risk rank ({POSTHOC_LABEL})", 42, ["42", "#42"],
                             date(2022, 12, 31), hindsight=True))
    return sheet, POSTHOC_LABEL


def test_posthoc_fact_requires_label_in_sentence():
    sheet, label = _posthoc_sheet()
    errs = check_memo(_memo("On run risk the bank was #42.", ["F6"], key="outcome"), sheet, SECTIONS)
    assert len(errs) == 1 and "post-hoc" in errs[0]
    ok = f"On the run-risk rank, a {label}, the bank was #42."
    assert check_memo(_memo(ok, ["F6"], key="outcome"), sheet, SECTIONS) == []


def test_posthoc_label_with_wrong_number_still_fails():
    sheet, label = _posthoc_sheet()
    errs = check_memo(_memo(f"On the run-risk rank, a {label}, the bank was #41.", ["F6"], key="outcome"),
                      sheet, SECTIONS)
    assert len(errs) == 1 and "#41" in errs[0]


def _lead_sheet(q, words):
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "Lead time in quarters before failure", q, [str(q), *words], hindsight=True))
    return sheet


@pytest.mark.parametrize("text,ok", [("Canary flagged it four quarters ahead.", False),
                                     ("It was Two quarters early.", False), ("Flagged a quarter ahead.", True),
                                     ("Flagged one quarter ahead.", True), ("flagged one year ahead", False),
                                     ("Flagged an quarter ahead.", True)])
def test_spelled_lead_time_must_match(text, ok):
    sheet = _lead_sheet(1, ["one", "one quarter", "a quarter"])
    errs = check_memo(_memo(text, ["F6"], key="outcome"), sheet, SECTIONS)
    assert (errs == []) if ok else len(errs) == 1


def test_spelled_lead_time_matching_passes_and_counts_ignored():
    sheet = _lead_sheet(4, ["four", "four quarters"])
    assert check_memo(_memo("Canary flagged it four quarters ahead.", ["F6"], key="outcome"), sheet, SECTIONS) == []
    assert run("The model lists five drivers.", []) == []
    errs = run("It was flagged four quarters ahead.", [])
    assert len(errs) == 1 and "no cites" in errs[0]
    assert extract_tokens("an quarter, A year, three Quarters") == ["a quarter", "a year", "three quarters"]


@pytest.mark.parametrize("text", ["It had a 3% chance of failing.", "The probability of failure was low.",
                                  "Its likelihood of failing rose.", "A 12.5% chance applies."])
def test_probability_phrasing_rejected_anywhere(text):
    for key in ("summary", "outcome"):
        errs = check_memo(_memo(text, ["F1", "F2"], key=key), _sheet(), SECTIONS)
        assert any("probability" in e for e in errs), (key, errs)


@pytest.mark.parametrize("text", ["The bank failed soon after.", "It collapsed.", "The bank was closed by regulators.",
                                  "It was seized."])
def test_failure_words_rejected_in_as_of_sections(text):
    errs = run(text, [])
    assert len(errs) == 1 and "as-of" in errs[0]
    assert check_memo(_memo(text, [], key="outcome"), _sheet(), SECTIONS) == []


@pytest.mark.parametrize("text", ["The bank was not flagged.", "It was on the watchlist and ranked high.",
                                  "Deposits were closely watched.", "The model failsafe held.",
                                  "Losses on bonds held to maturity were large."])
def test_ordinary_as_of_prose_passes(text):
    assert run(text, []) == []


@pytest.mark.parametrize("text,ok", [("in FY2022", True), ("in FY2021", False), ("in FY 2022", True),
                                     ("in Dec 2022", True), ("in Dec. 2022", True), ("in Sept 2022", False),
                                     ("in Sep. 2022", False), ("on december 31, 2022", True),
                                     ("in september 2022", False), ("in Jan 2022", False)])
def test_fiscal_years_and_month_abbreviations_checked(text, ok):
    errs = run(text, ["F1"])
    assert (errs == []) if ok else len(errs) == 1


def test_month_tokens_extracted_and_may_ignored():
    assert extract_tokens("in Sept and Dec. and march and FY2022") == ["sept", "dec", "march", "fy2022"]
    assert extract_tokens("It May rise; it may rise.") == []
    assert len(run("in Sept", ["F1"])) == 1 and run("in Dec.", ["F1"]) == []


def test_negated_probability_wording_allowed():
    assert run("The score is not a probability of failure.", []) == []
    assert len(run("The score is a probability of failure.", [])) == 1


def test_label_spelled_span_becomes_a_form(analyst_ctx):
    from canary.analyst.facts import build_fact_sheet

    sheet = build_fact_sheet(analyst_ctx, 3)
    growth = next(f for f in sheet.facts if f.label.startswith("Bank: asset growth over the past four quarters"))
    assert "four quarters" in growth.forms
    secs = [Section("summary", "Summary", "as_of", "", True)]
    text = f"Asset growth over the past four quarters was {growth.display}."
    memo = {"sections": [{"key": "summary", "paragraphs": [{"sentences": [{"text": text, "cites": [growth.id]}]}]}]}
    assert check_memo(memo, sheet, secs) == []


@pytest.mark.parametrize("text", ["the bank has no chance of failing.", "never a chance of failure here.",
                                  "Its percentile was 26.8%, so there is not a 26.8% chance of failing.",
                                  "There is not a chance of failure.", "It is not the 5% chance of failure."])
def test_r15_only_the_exact_disclaimer_is_exempt(text):
    sheet = _sheet()
    sheet.facts.append(_fact("F6", "Percentile", 26.8, ["26.8%", "26.8"]))
    errs = check_memo(_memo(text, ["F6"]), sheet, SECTIONS)
    assert any("probability of failure" in e for e in errs), errs


@pytest.mark.parametrize("text", ["The score is not a probability of failure.",
                                  "The score is not the likelihood of failing.", "It is not a probability of failing."])
def test_r15_disclaimer_passes(text):
    assert run(text, []) == []
