from dataclasses import replace
from datetime import date

import re

import numpy as np
import pandas as pd
import pytest

from canary.analyst import sections
from canary.analyst import trends as trends_mod
from canary.analyst.checker import check_memo
from canary.analyst.facts import build_fact_sheet
from canary.analyst.render import render_note
from canary.analyst.sections import sections_for
from canary.analyst.trends import (
    TREND_KEY,
    TREND_SECTION,
    TREND_SENTENCE,
    RatioTrend,
    TrendResult,
    TrendSpecialist,
    render_trends,
)
from canary.analyst.writer import write_memo
from canary.model.dataset import FEATURE_COLUMNS
from canary.replay.probe import contribution_matrix
from tests.analyst_fakes import FakeClient

CERT = 3
PER_RATIO = ["trend_value", "trend_lo", "trend_hi", "trend_change_1q", "trend_change_4q",
             "trend_contribution", "trend_direction"]


def _trend(feature, value, lo, hi, window="pit", c1=2.0, c4=3.0, contribution=0.2):
    return RatioTrend(feature=feature, value=value, lo=lo, hi=hi, window=window, n_prior=12,
                      excess_pp=5.0, score=2.0, change_1q_pp=c1, change_4q_pp=c4,
                      contribution=contribution, direction=trends_mod.direction_label(contribution))


def _force(monkeypatch, as_of, outside, checked=None, too_little=0):
    res = TrendResult(as_of=as_of, checked=len(outside) if checked is None else checked,
                      too_little=too_little, outside=outside)
    monkeypatch.setattr(trends_mod, "compute_trends", lambda history, a, contributions: replace(res, as_of=a))
    return res


def _sheet(ctx, tmp_path, cert=CERT):
    return build_fact_sheet(ctx, cert, replay_dir=tmp_path / "none")


def _kind(sheet, kind, feature=None):
    return [f for f in sheet.facts if f.kind == kind and (feature is None or f.feature == feature)]


def test_trend_facts_paired_by_feature(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    shown = sheet.extras["trends"].shown
    assert shown
    for r in shown:
        for kind in PER_RATIO:
            got = _kind(sheet, kind, r.feature)
            if kind == "trend_change_1q" and r.change_1q_pp is None:
                assert got == []
            elif kind == "trend_change_4q" and r.change_4q_pp is None:
                assert got == []
            else:
                assert len(got) == 1, (kind, r.feature)
    assert len(_kind(sheet, "trend_value")) == len(shown)


def test_contribution_matches_drivers(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    s = analyst_ctx.scored
    row = s[(s["cert"] == CERT) & (s["report_date"] == pd.Timestamp(sheet.as_of))]
    contrib = contribution_matrix(analyst_ctx.model, row)[0]
    for r in sheet.extras["trends"].shown:
        (f,) = _kind(sheet, "trend_contribution", r.feature)
        assert f.value == pytest.approx(float(contrib[FEATURE_COLUMNS.index(r.feature)]))
        assert f.display == f"{f.value:+.3f}"


def test_change_forms_have_no_percent(analyst_ctx, tmp_path, monkeypatch):
    as_of = date(2019, 12, 31)
    _force(monkeypatch, as_of, [_trend("equity_to_assets", 12.0, 8.0, 10.0, c1=1.2, c4=2.4),
                                _trend("noncurrent_loans_to_loans", 0.05, 0.01, 0.02, c1=41.8, c4=41.8)])
    sheet = _sheet(analyst_ctx, tmp_path)
    changes = _kind(sheet, "trend_change_1q") + _kind(sheet, "trend_change_4q")
    assert changes and all("%" not in x for f in changes for x in f.forms)
    (pct,) = _kind(sheet, "trend_change_1q", "equity_to_assets")
    (frac,) = _kind(sheet, "trend_change_1q", "noncurrent_loans_to_loans")
    assert pct.display == "+1.2 pp" and frac.display == "+41.8 pp"
    assert frac.quarter == sheet.as_of


def test_negative_forms(analyst_ctx, tmp_path, monkeypatch):
    _force(monkeypatch, date(2019, 12, 31),
           [_trend("htm_unrealized_loss_to_equity", -0.1172, -0.05, 0.0, c1=-41.8, c4=-41.8,
                   contribution=-0.2)])
    sheet = _sheet(analyst_ctx, tmp_path)
    (v,) = _kind(sheet, "trend_value", "htm_unrealized_loss_to_equity")
    assert "-11.7%" in v.forms and v.display == "-11.7%"
    (c,) = _kind(sheet, "trend_change_1q", "htm_unrealized_loss_to_equity")
    assert c.display == "-41.8 pp" and "-41.8" in c.forms and "41.8" in c.forms
    # the checker accepts a Unicode minus against those forms
    secs = sections_for(sheet)
    memo = {"sections": [{"key": s.key, "paragraphs": [{"sentences": []}]} for s in secs if s.ai_written]}
    for sec in memo["sections"]:
        if sec["key"] == "trends":
            sec["paragraphs"] = [{"sentences": [
                {"text": "It was −11.7% and moved −41.8 pp.", "cites": [v.id, c.id]}]}]
    errs = [e for e in check_memo(memo, sheet, secs) if "section 'trends'" in e]
    assert errs == []


def test_no_nan_in_trend_facts(analyst_ctx, tmp_path, monkeypatch):
    bad = _trend("equity_to_assets", 12.0, 8.0, 10.0, c1=float("nan"), c4=3.0, contribution=float("nan"))
    _force(monkeypatch, date(2019, 12, 31), [bad])
    sheet = _sheet(analyst_ctx, tmp_path)
    trend_facts = [f for f in sheet.facts if f.kind and f.kind.startswith("trend_")]
    assert trend_facts
    for f in trend_facts:
        assert "nan" not in f.display.lower() and all("nan" not in x.lower() for x in f.forms)
        assert not (isinstance(f.value, float) and np.isnan(f.value))
    (c,) = _kind(sheet, "trend_contribution", "equity_to_assets")
    assert c.value == 0.0
    (d,) = _kind(sheet, "trend_direction", "equity_to_assets")
    assert d.value == "little effect on the score"
    assert _kind(sheet, "trend_change_1q") == []
    assert "nan" not in "\n".join(render_trends(sheet)).lower()


def test_no_year_earlier_score(analyst_ctx, tmp_path):
    first = analyst_ctx.scored[analyst_ctx.scored["cert"] == CERT]["report_date"].min()
    sheet = build_fact_sheet(analyst_ctx, CERT, as_of=first.date(), replay_dir=tmp_path / "none")
    assert _kind(sheet, "trend_prior_percentile") == []
    assert _kind(sheet, "trend_rank_phrase") == []
    assert TREND_KEY in [s.key for s in sections_for(sheet)]
    lines = render_trends(sheet)
    assert lines[0] == ("There is no score from a year earlier to compare with (scores start 2016-03-31, "
                        "or the bank did not report then).")


def test_year_earlier_line_absent_when_rank_phrase_present(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    assert not any("no score from a year earlier" in ln for ln in render_trends(sheet))


def test_shown_count_fact(analyst_ctx, tmp_path, monkeypatch):
    outs = [_trend(f, 20.0 + i, 8.0, 10.0) for i, f in enumerate(
        ["equity_to_assets", "leverage_ratio", "tier1_risk_based_ratio", "total_risk_based_ratio",
         "return_on_assets", "return_on_equity", "net_interest_margin"])]
    _force(monkeypatch, date(2019, 12, 31), outs, checked=20)
    sheet = _sheet(analyst_ctx, tmp_path)
    (f,) = _kind(sheet, "trend_count_shown")
    assert f.value == 6 and f.display == "6" and "6" in f.forms and f.feature is None
    (o,) = _kind(sheet, "trend_count_outside")
    assert o.value == 7


def test_no_negative_zero(analyst_ctx, tmp_path, monkeypatch):
    tiny = _trend("allowance_to_loans", -0.0001, 0.0, 0.0, c1=-0.0001, c4=-0.0, contribution=-0.0001)
    _force(monkeypatch, date(2019, 12, 31), [tiny])
    sheet = _sheet(analyst_ctx, tmp_path)
    text = "\n".join(render_trends(sheet))
    bad = ("-0.0%", "-0.00 pp", "-0.0 pp", "-0.000", "-0.00%")
    for f in sheet.facts:
        if f.kind and f.kind.startswith("trend_"):
            for x in [f.display, *f.forms]:
                assert not re.fullmatch(r"-0(\.0+)?%?", x), (f.label, x)
                assert not any(b in x for b in bad), (f.label, x)
    assert not any(b in text for b in bad), text
    (v,) = _kind(sheet, "trend_value")
    assert v.display == "-0.01%"  # reads differently from the 0.00% bound


def test_year_earlier_facts_present(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    (p,) = _kind(sheet, "trend_prior_percentile")
    (ph,) = _kind(sheet, "trend_rank_phrase")
    assert p.quarter == pd.Timestamp(sheet.as_of).date().replace(year=sheet.as_of.year - 1)
    assert ph.value in ("the model rated it riskier than a year earlier",
                        "the model rated it safer than a year earlier",
                        "about the same as a year earlier")
    assert "a year" in ph.forms


def test_none_outside_is_code_only(analyst_ctx, tmp_path, monkeypatch):
    _force(monkeypatch, date(2019, 12, 31), [], checked=5)
    sheet = _sheet(analyst_ctx, tmp_path)
    assert TREND_KEY in sheet.code_only
    assert next(s for s in sections_for(sheet) if s.key == TREND_KEY).ai_written is False
    lines = render_trends(sheet)
    assert f"None of this bank's ratios were outside their own prior range at {sheet.as_of}." in lines
    assert lines[-1] == TREND_SENTENCE


def test_too_little_history_line(analyst_ctx, tmp_path, monkeypatch):
    _force(monkeypatch, date(2019, 12, 31), [], checked=0, too_little=4)
    sheet = _sheet(analyst_ctx, tmp_path)
    lines = render_trends(sheet)
    assert (f"This bank has too little history before {sheet.as_of} to compare its ratios "
            "with its own prior range.") in lines
    assert lines[-1] == TREND_SENTENCE


def test_table_lines_and_truncation_note(analyst_ctx, tmp_path, monkeypatch):
    outs = [_trend(f, 20.0 + i, 8.0, 10.0, c1=None) for i, f in enumerate(
        ["equity_to_assets", "leverage_ratio", "tier1_risk_based_ratio", "total_risk_based_ratio",
         "return_on_assets", "return_on_equity", "net_interest_margin"])]
    outs[4].window = "ytd"
    _force(monkeypatch, date(2019, 12, 31), outs, checked=20)
    sheet = _sheet(analyst_ctx, tmp_path)
    lines = render_trends(sheet)
    assert lines[0] == ("| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | "
                        "Model contribution | Direction |")
    text = "\n".join(lines)
    assert "prior 12 quarters" in text and "same quarter, prior 3 years" in text and "n/a" in text
    assert "7 of 20 ratios were outside their prior range; the 6 furthest are shown." in text
    assert lines[-1] == TREND_SENTENCE
    assert sum(1 for ln in lines if ln.startswith("| ") and "---" not in ln) == 7  # header + 6


def test_table_rendered_and_section_position(analyst_ctx, tmp_path):
    from tests.test_analyst_writer import _memo

    sheet = _sheet(analyst_ctx, tmp_path)
    client = FakeClient([_memo(sheet)])
    res = write_memo(analyst_ctx, CERT, client=client, out_dir=tmp_path / "banks",
                     replay_dir=tmp_path / "none")
    assert res.ok, res.errors
    text = res.path.read_text()
    i_hist, i_tr = text.index("## Score history"), text.index("## How its ratios moved")
    assert i_hist < i_tr
    assert i_tr < min(text.index(h) for h in ("## Outcome", "## How early", "## Why", "## What happened next")
                      if h in text)
    assert "| Ratio | As-of value | Prior range |" in text
    assert text.count(TREND_SENTENCE) == 1


def test_registered_once():
    import canary.analyst.writer  # noqa: F401

    found = [sp for sp in sections.SPECIALISTS if sp.key == TREND_KEY]
    assert len(found) == 1 and isinstance(found[0], TrendSpecialist)
    saved = list(sections.SPECIALISTS)
    try:
        sections.register(TrendSpecialist())
        assert len([sp for sp in sections.SPECIALISTS if sp.key == TREND_KEY]) == 1
    finally:
        sections.SPECIALISTS[:] = saved


def test_section_definition():
    assert TREND_SECTION.key == "trends" and TREND_SECTION.title == "How its ratios moved"
    assert TREND_SECTION.window == "as_of" and TREND_SECTION.ai_written
    assert TREND_SECTION.render is render_trends
    assert "percentage points" in TREND_SECTION.instructions
    ins = TREND_SECTION.instructions
    assert "one ratio per sentence" in ins and "fixed sentence" not in ins
    assert "Don't write a disclaimer" in ins and "predict, forecast or warning" in ins
    assert "if a rank-phrase fact is given" in ins.lower()


def test_near_bound_values_get_more_decimals(analyst_ctx, tmp_path, monkeypatch):
    # frac ratio: 0.597% vs bound 0.601% read the same ("0.6%") at one decimal
    near = _trend("allowance_to_loans", 0.00597, 0.00601, 0.016, c1=-0.04, c4=2.0, contribution=0.0)
    far = _trend("noncurrent_loans_to_loans", 0.05, 0.01, 0.02)
    _force(monkeypatch, date(2019, 12, 31), [near, far])
    sheet = _sheet(analyst_ctx, tmp_path)
    table = "\n".join(render_trends(sheet))
    (v,) = _kind(sheet, "trend_value", "allowance_to_loans")
    (lo,) = _kind(sheet, "trend_lo", "allowance_to_loans")
    # 0.60% vs 0.60% tie at 2 decimals, so 3 are used; the table matches the fact
    assert v.forms[0] == v.display and lo.forms[0] == lo.display
    assert v.display == "0.597%" and lo.display == "0.601%", (v.display, lo.display)
    assert "0.6%" in v.forms
    assert f"| {v.display} | {lo.display} to 1.6% |" in table
    (c,) = _kind(sheet, "trend_change_1q", "allowance_to_loans")
    assert c.display == "-0.04 pp" and "-0.04" in c.forms and all("%" not in x for x in c.forms)
    assert "-0.04 pp" in table
    # ordinary values keep one decimal
    (ov,) = _kind(sheet, "trend_value", "noncurrent_loans_to_loans")
    assert ov.display == "5.0%" and "| 5.0% | 1.0% to 2.0% |" in table


def test_two_decimals_when_they_differ(analyst_ctx, tmp_path, monkeypatch):
    near = _trend("allowance_to_loans", 0.0058, 0.0063, 0.016)
    _force(monkeypatch, date(2019, 12, 31), [near])
    sheet = _sheet(analyst_ctx, tmp_path)
    (v,) = _kind(sheet, "trend_value")
    (lo,) = _kind(sheet, "trend_lo")
    assert v.display == "0.58%" and lo.display == "0.63%"
    assert "| 0.58% | 0.63% to 1.6% |" in "\n".join(render_trends(sheet))


def test_instructions_require_value_with_contribution():
    """Showcase diagnostic 2026-11-19: a contribution sentence without the ratio's value or range was the
    first-attempt failure; the instructions must say both go in the same sentence."""
    from canary.analyst.trends import TREND_SECTION

    assert "in that same sentence also give that ratio's as-of value or its prior range" in TREND_SECTION.instructions
