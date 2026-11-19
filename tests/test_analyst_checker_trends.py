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
        _f("R1", "Rank phrase", "the model rated it safer than a year earlier", ["a year"], None, "trend_rank_phrase"),
        _f("R3", "Rank phrase riskier", "the model rated it riskier than a year earlier", ["a year"], None, "trend_rank_phrase"),
        _f("R2", "Rank phrase same", "about the same as a year earlier", ["a year"], None, "trend_rank_phrase"),
        _f("A2", "AFS lo", 1.0, ["1.0%"], "afs", "trend_lo"),
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
    assert any("give one ratio per sentence" in e for e in errs)


def test_htm_value_and_contribution_with_afs_contribution_rejected():
    errs = run("Held-to-maturity losses were 48.4% with a contribution of -0.164, and the other was 0.300.",
               ["H1", "H4", "A4"])
    assert any("give one ratio per sentence when stating its contribution or direction" in e for e in errs)


def test_two_ratio_direction_sentence_gets_one_ratio_message():
    errs = run("Held-to-maturity losses pushed the score down, while available-for-sale losses pushed "
               "the score up.", ["H1", "H5", "A1", "A5"])
    assert len(errs) == 1 and "give one ratio per sentence" in errs[0]


def test_two_ratio_ranges_without_contribution_allowed():
    assert run("Held-to-maturity losses ranged from -11.7% to 6.6%, and available-for-sale from 1.0% to 5.0%.",
               ["H2", "H3", "A2", "A1"]) == []


def test_contribution_without_ratio_figure_rejected():
    errs = run("The contribution was -0.164.", ["H4"])
    assert any("without that ratio's value or range" in e for e in errs)


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


def test_rank_phrase_safer_rejects_riskier():
    errs = run("The model rated it riskier than a year earlier.", ["R1"])
    assert any("riskier" in e for e in errs)
    assert run("The model rated it safer than a year earlier.", ["R1"]) == []


def test_rank_phrase_riskier_rejects_safer():
    errs = run("The model rated it safer than a year earlier.", ["R3"])
    assert any("safer" in e for e in errs)


def test_rank_phrase_same_rejects_both():
    assert run("It was about the same as a year earlier.", ["R2"]) == []
    for w in ("riskier", "safer"):
        assert run(f"The model rated it {w} than a year earlier.", ["R2"])


def test_rank_phrase_not_cited_not_checked():
    assert run("The model rated it riskier than before.", []) == []


def test_one_ratio_error_still_runs_rank_phrase_check():
    errs = run("Held-to-maturity losses at 48.4% pushed the score up, and the model rated it riskier than "
               "a year earlier.", ["H1", "H5", "A1", "R1"])
    assert any("give one ratio per sentence" in e for e in errs)
    assert any("says 'riskier'" in e for e in errs)


def test_contribution_message_wordings():
    errs = run("The contribution was -0.164.", ["H4"])
    assert any("cites a contribution without that ratio's value or range" in e for e in errs)
    errs = run("Losses were 48.4% and the contribution was 0.300.", ["H1", "A4"])
    assert any("give one ratio per sentence" in e for e in errs)
