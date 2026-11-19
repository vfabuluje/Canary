from datetime import date

import pandas as pd

from canary.analyst.checker import check_memo
from canary.analyst.facts import Fact, FactSheet
from canary.analyst.peers import (
    PEER_KEY, READING_HIGH, READING_HIGH_TOO, READING_LOW, READING_TYPICAL,
)
from canary.analyst.sections import Section

AS_OF = date(2022, 12, 31)


def _f(id, label, value, forms, feature=None, kind=None):
    return Fact(id, label, AS_OF, value, str(value), forms, False, "src", feature, kind)


def _sheet():
    facts = [
        _f("V1", "Equity value", 12.0, ["12.0%"], "eq", "peer_value"),
        _f("N1", "Equity national pct", 98.2, ["98.2%"], "eq", "peer_nat_pct"),
        _f("D1", "Equity national direction", "unusually high", [], "eq", "peer_nat_dir"),
        _f("P1", "Equity peer pct", 62.3, ["62.3%"], "eq", "peer_pct"),
        _f("M1", "Equity peer median", 9.1, ["9.1%"], "eq", "peer_median"),
        _f("R1", "Equity reading", READING_LOW, [], "eq", "peer_reading"),
        _f("V2", "Loans value", 3.0, ["3.0%"], "ln", "peer_value"),
        _f("P2", "Loans peer pct", 40.0, ["40.0%"], "ln", "peer_pct"),
        _f("R2", "Loans reading", READING_TYPICAL, [], "ln", "peer_reading"),
        _f("R3", "Cards reading", READING_HIGH_TOO, [], "cc", "peer_reading"),
        _f("R4", "Typical reading eq", READING_TYPICAL, [], "eq", "peer_reading"),
        _f("D2", "Loans national direction", "unusually low", [], "ln", "peer_nat_dir"),
        _f("R5", "High reading eq", READING_HIGH, [], "eq", "peer_reading"),
        _f("S1", "Summary fact", 7, ["7"]),
    ]
    empty = pd.DataFrame()
    return FactSheet(1, "X Bank", AS_OF, None, facts, empty, empty, "", ["summary", PEER_KEY])


SECTIONS = [Section("summary", "Summary", "as_of", "", True), Section(PEER_KEY, "Peers", "as_of", "", True)]


def run(text, cites, key=PEER_KEY):
    other = "summary" if key == PEER_KEY else PEER_KEY
    memo = {"sections": [
        {"key": key, "paragraphs": [{"sentences": [{"text": text, "cites": cites}]}]},
        {"key": other, "paragraphs": []},
    ]}
    return check_memo(memo, _sheet(), SECTIONS)


def test_correct_sentence_passes():
    text = ("Equity was 12.0% of assets, at the 98.2% national percentile, unusually high nationally, "
            "the 62.3% mark among peers, and unusually low among its peers.")
    assert run(text, ["V1", "N1", "D1", "P1", "R1"]) == []


def test_contrast_with_typical_passes():
    text = "Loans were unusually low nationally, yet typical for its peer group."
    assert run(text, ["D2", "R2"]) == []
    assert run("Loans were unusually low nationally, yet typical among its peers.", ["D2", "R2"]) == []


def test_two_ratios_readings_rejected():
    errs = run("Equity was unusually low among its peers and cards unusually high among its peers too.",
               ["R1", "R3"])
    assert any("give one ratio per sentence when stating its peer reading" in e for e in errs)


def test_other_ratio_fact_with_reading_rejected():
    errs = run("Equity was unusually low among its peers; loans were 3.0%.", ["R1", "V2"])
    assert any("give one ratio per sentence when stating its peer reading" in e for e in errs)


def test_two_ratio_values_without_reading_allowed():
    assert run("Equity was 12.0% and loans were 3.0%.", ["V1", "V2"]) == []


def test_typical_reading_rejects_unusual_among_peers():
    for t in ("Equity was unusual among its peers.", "Equity was unusually high among its peers.",
              "Equity was unusually low among its peers."):
        assert any("among its peers" in e for e in run(t, ["R4"])), t


def test_high_reading_rejects_opposites():
    assert run("Equity was unusually low among its peers.", ["R5"])
    assert run("Equity was typical for its peer group.", ["R5"])
    assert run("Equity was unusually high among its peers.", ["R5"]) == []


def test_low_reading_rejects_high_among_peers():
    errs = run("Equity was high nationally but unusually high among its peers.", ["D1", "R1"])
    assert errs


def test_national_direction_rejects_opposite():
    assert run("Equity was unusually low nationally.", ["D1"])
    assert run("Equity was unusually high nationally.", ["D1"]) == []
    assert run("Equity was unusually high nationally, unusually low among its peers.", ["D1", "R1"]) == []
    assert run("Loans were unusually high nationally.", ["D2"])


def test_risky_and_prediction_rejected():
    assert any("prediction language" in e for e in run("Equity looks risky.", []))
    assert any("prediction language" in e for e in run("This is riskier.", []))
    assert any("prediction language" in e for e in run("Equity would have warned us.", []))


def test_rules_do_not_fire_elsewhere():
    assert run("Equity looks risky and was unusually low among its peers.", [], key="summary") == []
    assert run("Equity was unusually high among its peers.", ["R4"], key="summary") == []
