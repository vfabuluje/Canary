from datetime import date

import pandas as pd
import pytest

from canary.analyst.checker import check_memo
from canary.analyst.facts import Fact, FactSheet
from canary.analyst.sections import Section
from canary.analyst.trends import TREND_KEY

AS_OF = date(2022, 12, 31)


def _f(id, label, value, forms, feature=None, kind=None):
    return Fact(id, label, AS_OF, value, str(value), forms, False, "src", feature, kind)


def _sheet():
    facts = [
        _f("H1", "HTM value", 48.4, ["48.4%"], "htm", "trend_value"),
        _f("H2", "HTM lo", -11.7, ["-11.7%"], "htm", "trend_lo"),
        _f("H3", "HTM hi", 6.6, ["6.6%"], "htm", "trend_hi"),
        _f("H4", "HTM contribution", -0.164, ["-0.164"], "htm", "trend_contribution"),
        _f("H5", "HTM direction", "pushed the score down", [], "htm", "trend_direction"),
        _f("H6", "HTM change 1q", 41.8, ["+41.8", "41.8", "+42", "42"], "htm", "trend_change_1q"),
        _f("A1", "AFS value", 5.0, ["5.0%"], "afs", "trend_value"),
        _f("A4", "AFS contribution", 0.3, ["0.300"], "afs", "trend_contribution"),
        _f("A5", "AFS direction", "pushed the score up", [], "afs", "trend_direction"),
        _f("S1", "Summary fact", 7, ["7"]),
    ]
    empty = pd.DataFrame()
    return FactSheet(1, "X Bank", AS_OF, None, facts, empty, empty, "", ["summary", TREND_KEY])


SECTIONS = [Section("summary", "Summary", "as_of", "", True), Section(TREND_KEY, "Trends", "as_of", "", True)]


def run(text, cites, key=TREND_KEY):
    other = "summary" if key == TREND_KEY else TREND_KEY
    memo = {"sections": [
        {"key": key, "paragraphs": [{"sentences": [{"text": text, "cites": cites}]}]},
        {"key": other, "paragraphs": []},
    ]}
    return check_memo(memo, _sheet(), SECTIONS)


def test_contrast_sentence_passes():
    text = ("Losses on bonds held to maturity rose to 48.4% of equity, far above the prior range of "
            "-11.7% to 6.6%, yet the model's contribution for that ratio was -0.164, which pushed the score down.")
    assert run(text, ["H1", "H2", "H3", "H4", "H5"]) == []


def test_htm_value_with_afs_contribution_rejected():
    errs = run("Held-to-maturity losses were 48.4% and the other ratio's contribution was 0.300.", ["H1", "A4"])
    assert any("pairs a contribution with a different ratio's figures" in e for e in errs)


def test_contribution_without_ratio_figure_rejected():
    errs = run("The contribution was -0.164.", ["H4"])
    assert any("pairs a contribution" in e for e in errs)


def test_opposite_direction_rejected():
    errs = run("Held-to-maturity losses pushed the score up.", ["H1", "H5"])
    assert len(errs) == 1 and "pushed the score down" in errs[0]


def test_opposite_direction_for_up_label_rejected():
    errs = run("Unrealized losses pulled the score down.", ["A1", "A5"])
    assert len(errs) == 1 and "pushed the score up" in errs[0]


def test_contribution_uses_direction_fact_label():
    errs = run("The contribution was -0.164 and it raised the score.", ["H1", "H4"])
    assert any("pushed the score down" in e for e in errs)


@pytest.mark.parametrize("phrase", ["predicted", "an early warning", "would have caught",
                                    "should have flagged", "a sign of failure"])
def test_prediction_phrases_rejected(phrase):
    errs = run(f"The ratio moved, {phrase} it.", [])
    assert any("uses prediction language" in e for e in errs)


def test_change_as_percent_rejected():
    errs = run("Losses rose 41.8% in one quarter.", ["H6"])
    assert any("41.8%" in e and "not supported" in e for e in errs)


def test_change_as_pp_ok():
    assert run("Losses rose +41.8 pp.", ["H6"]) == []


def test_unicode_minus_ok():
    assert run("The prior low was −11.7%.", ["H2"]) == []


def test_rules_only_in_trend_section():
    assert run("The bank predicted it.", [], key="summary") == []
