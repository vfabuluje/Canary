"""How a bank's ratios moved against their own prior range (descriptive, no model).

The range rule is fixed by convention (spec 2026-11-18-phase5b-trend-design, section 5)
and has not been tested as a warning signal.
"""
import math
from dataclasses import dataclass, replace
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst import sections as sections_mod
from canary.analyst.facts import SPELLED_SPAN, Fact, _count_forms, _ordinal, date_forms, spelled_norm
from canary.analyst.labels import PLAIN_NAMES, UNIT, display_forms
from canary.analyst.sections import Section
from canary.model.dataset import FEATURE_COLUMNS
from canary.replay.probe import contribution_matrix

TREND_RATIOS: tuple[str, ...] = tuple(f for f in FEATURE_COLUMNS if f != "log_total_assets")
YTD_RATIOS: frozenset[str] = frozenset({
    "return_on_assets", "return_on_equity", "net_interest_margin", "efficiency_ratio",
    "net_charge_offs_to_loans_ann", "provision_to_assets_ann", "interest_expense_to_assets_ann",
})
MAX_SHOWN = 6
WIDTH_FLOOR_PP = 1.0
DIRECTION_CUTOFF = 0.05
RANK_SAME_PP = 1.0

_PIT_QUARTERS = 12
_PIT_MIN = 8
_YTD_YEARS = 3
_YTD_MIN = 2


@dataclass
class RatioTrend:
    feature: str
    value: float
    lo: float
    hi: float
    window: Literal["pit", "ytd"]
    n_prior: int
    excess_pp: float
    score: float
    change_1q_pp: float | None
    change_4q_pp: float | None
    contribution: float
    direction: str


@dataclass
class TrendResult:
    as_of: date
    checked: int
    too_little: int
    outside: list[RatioTrend]

    @property
    def shown(self) -> list[RatioTrend]:
        return self.outside[:MAX_SHOWN]


def to_pp(feature: str, delta: float) -> float:
    """Convert a difference in a ratio's own unit to percentage points."""
    return delta if UNIT[feature] == "pct" else delta * 100.0


def direction_label(contribution: float) -> str:
    if contribution >= DIRECTION_CUTOFF:
        return "pushed the score up"
    if contribution <= -DIRECTION_CUTOFF:
        return "pushed the score down"
    return "little effect on the score"


def rank_phrase(pct_now: float, pct_prior: float) -> str:
    diff = pct_now - pct_prior
    if diff > RANK_SAME_PP:
        return "the model rated it riskier than a year earlier"
    if diff < -RANK_SAME_PP:
        return "the model rated it safer than a year earlier"
    return "about the same as a year earlier"


def _window_dates(feature: str, as_of: date) -> list[pd.Timestamp]:
    t = pd.Timestamp(as_of)
    if feature in YTD_RATIOS:
        return [(t - pd.DateOffset(years=y)) + pd.offsets.QuarterEnd(0) for y in range(1, _YTD_YEARS + 1)]
    return [t - pd.offsets.QuarterEnd(k) for k in range(1, _PIT_QUARTERS + 1)]


def _series(history: pd.DataFrame, feature: str) -> pd.Series:
    s = pd.Series(history[feature].to_numpy(dtype=float),
                  index=pd.to_datetime(history["report_date"]).to_numpy())
    return s[~s.index.duplicated(keep="last")]


def prior_values(history: pd.DataFrame, feature: str, as_of: date) -> pd.Series:
    """Prior-window values for one ratio, NaN and missing quarters dropped."""
    s = _series(history, feature)
    return s.reindex(_window_dates(feature, as_of)).dropna()


def _at(s: pd.Series, when: pd.Timestamp) -> float | None:
    v = s.get(when)
    return None if v is None or pd.isna(v) else float(v)


def compute_trends(history: pd.DataFrame, as_of: date, contributions: dict[str, float]) -> TrendResult:
    t = pd.Timestamp(as_of)
    checked = too_little = 0
    outside: list[RatioTrend] = []
    for feature in TREND_RATIOS:
        if feature not in history.columns:
            continue
        s = _series(history, feature)
        now = _at(s, t)
        if now is None:
            continue
        ytd = feature in YTD_RATIOS
        prior = prior_values(history, feature, as_of)
        if len(prior) < (_YTD_MIN if ytd else _PIT_MIN):
            too_little += 1
            continue
        checked += 1
        lo, hi = float(prior.min()), float(prior.max())
        if lo <= now <= hi:
            continue
        excess = to_pp(feature, lo - now if now < lo else now - hi)
        width = max(to_pp(feature, hi - lo), WIDTH_FLOOR_PP)

        def change(quarters: int) -> float | None:
            before = _at(s, t - pd.offsets.QuarterEnd(quarters))
            return None if before is None else to_pp(feature, now - before)

        contribution = float(contributions.get(feature, 0.0))
        outside.append(RatioTrend(
            feature=feature, value=now, lo=lo, hi=hi, window="ytd" if ytd else "pit",
            n_prior=len(prior), excess_pp=excess, score=excess / width,
            change_1q_pp=None if ytd else change(1), change_4q_pp=change(4),
            contribution=contribution, direction=direction_label(contribution),
        ))
    outside.sort(key=lambda r: (-r.score, PLAIN_NAMES[r.feature]))
    return TrendResult(as_of=as_of, checked=checked, too_little=too_little, outside=outside)


TREND_KEY = "trends"
TREND_SENTENCE = (
    "This section only describes how the bank's own ratios moved against its own history. "
    "The range rule was set by convention and has not been tested as a warning signal, "
    "so a ratio outside its range is not a prediction of failure."
)
NONE_OUTSIDE = "None of this bank's ratios were outside their own prior range at {as_of}."
TOO_LITTLE = "This bank has too little history before {as_of} to compare its ratios with its own prior range."
_FEATURES_SRC = "data/features/fct_bank_features.parquet"
_SCORES_SRC = "data/analyst/scores.parquet"
_WINDOW_TEXT = {"pit": "prior 12 quarters", "ytd": "same quarter, prior 3 years"}

TREND_SECTION = Section(
    TREND_KEY, "How its ratios moved", "as_of",
    "Use only the trend facts (labels starting \"Trend\") and the as-of rank facts. For each ratio you "
    "discuss, give its as-of value, its prior range (low and high) and the model's contribution for that "
    "same ratio, with that ratio's direction label. State the rank phrase (how the model rated the bank "
    "against a year earlier). Where a ratio is outside its range but its direction is \"pushed the score "
    "down\" or \"little effect on the score\", say that contrast plainly. Never say a trend predicted, "
    "warned of or would have caught anything, and do not mention the outcome. Contributions are in "
    "\"model log-odds units\" (positive pushes the score up). Write changes with \"percentage points\" "
    "or \"pp\", never \"%\".",
    True,
)


def _ok(x: float | None) -> bool:
    return x is not None and not math.isnan(x)


def _sanitize(result: TrendResult) -> TrendResult:
    """No NaN reaches a fact or the table: a NaN contribution counts as 0.0 (little effect), a NaN
    change becomes missing, and a ratio with a NaN value, bound or score is dropped."""
    clean = []
    for r in result.outside:
        if not all(_ok(x) for x in (r.value, r.lo, r.hi, r.score, r.excess_pp)):
            continue
        c = r.contribution if _ok(r.contribution) else 0.0
        clean.append(replace(
            r, contribution=c, direction=direction_label(c),
            change_1q_pp=r.change_1q_pp if _ok(r.change_1q_pp) else None,
            change_4q_pp=r.change_4q_pp if _ok(r.change_4q_pp) else None,
        ))
    return replace(result, outside=clean)


def _change_forms(d: float) -> list[str]:
    # No "%" form: a change written as a level ("41.8%") must fail the checker.
    return [f"{d:+.1f}", f"{abs(d):.1f}", f"{d:+.0f}", f"{abs(d):.0f}"]


def _fact(label, value, display, forms, source, quarter, feature=None, kind=None) -> Fact:
    forms = list(forms) + (date_forms(quarter) if quarter else [])
    forms += [spelled_norm(m["sw"], m["su"]) for m in SPELLED_SPAN.finditer(f"{label} {display}")]
    return Fact("", label, quarter, value, display, list(dict.fromkeys(forms)), False, source, feature, kind)


class TrendSpecialist:
    key = TREND_KEY
    sections = [TREND_SECTION]

    def build_facts(self, ctx, sheet) -> list[Fact]:
        as_of, ts = sheet.as_of, pd.Timestamp(sheet.as_of)
        history = ctx.features[ctx.features["cert"] == sheet.cert]
        rows = ctx.scored[ctx.scored["cert"] == sheet.cert]
        at = rows[rows["report_date"] == ts]
        contrib = contribution_matrix(ctx.model, at)[0]
        contributions = {n: (float(c) if _ok(float(c)) else 0.0) for n, c in zip(FEATURE_COLUMNS, contrib)}
        result = _sanitize(compute_trends(history, as_of, contributions))
        sheet.extras[TREND_KEY] = result
        if not result.shown:
            sheet.code_only.add(TREND_KEY)

        out: list[Fact] = []
        for r in result.shown:
            name = PLAIN_NAMES[r.feature]
            src = f"{_FEATURES_SRC}: {r.feature}"
            v, lo, hi = (display_forms(r.feature, x) for x in (r.value, r.lo, r.hi))
            out.append(_fact(f"Trend: {name}, value at the as-of quarter", r.value, v[0], v, src, as_of,
                             r.feature, "trend_value"))
            out.append(_fact(f"Trend: {name}, lowest value in the comparison window", r.lo, lo[0], lo, src,
                             None, r.feature, "trend_lo"))
            out.append(_fact(f"Trend: {name}, highest value in the comparison window", r.hi, hi[0], hi, src,
                             None, r.feature, "trend_hi"))
            for kind, span, d in (("trend_change_1q", "one quarter", r.change_1q_pp),
                                  ("trend_change_4q", "four quarters", r.change_4q_pp)):
                if d is not None:
                    out.append(_fact(f"Trend: {name}, change over {span}, in percentage points", d,
                                     f"{d:+.1f} pp", _change_forms(d), src, as_of, r.feature, kind))
            c = r.contribution
            out.append(_fact(f"Trend: {name}, contribution to the score (model log-odds units)", c,
                             f"{c:+.3f}", [f"{c:+.3f}", f"{abs(c):.3f}", f"{abs(c):.2f}", f"{c:+.2f}"],
                             f"{_SCORES_SRC}: feature {r.feature} contribution", as_of, r.feature,
                             "trend_contribution"))
            out.append(_fact(f"Trend: {name}, what the model did with it", r.direction, r.direction, [],
                             f"{_SCORES_SRC}: feature {r.feature} contribution", as_of, r.feature,
                             "trend_direction"))

        n_out = len(result.outside)
        out.append(_fact("Trend: ratios outside their own prior range", n_out, str(n_out), _count_forms(n_out),
                         _FEATURES_SRC, as_of, None, "trend_count_outside"))
        out.append(_fact("Trend: ratios compared with their own prior range", result.checked,
                         str(result.checked), _count_forms(result.checked), _FEATURES_SRC, as_of, None,
                         "trend_count_checked"))
        out.append(_fact("Comparison window for most ratios: the prior 12 quarters (at least 8 with a value)",
                         12, "12 quarters", ["12", "8"], "canary.analyst.trends: range rule (fixed)", None,
                         None, "trend_window_pit"))
        out.append(_fact("Comparison window for year-to-date ratios: the same quarter in the prior 3 years "
                         "(at least 2 with a value)", 3, "3 years", ["3", "2"],
                         "canary.analyst.trends: range rule (fixed)", None, None, "trend_window_ytd"))

        prior = (ts - pd.DateOffset(years=1)) + pd.offsets.QuarterEnd(0)
        prior_row = rows[rows["report_date"] == prior]
        if len(prior_row) and len(at):
            p_now, p_prior = float(at.iloc[0]["percentile"]), float(prior_row.iloc[0]["percentile"])
            if _ok(p_now) and _ok(p_prior):
                forms = [f"{p_prior:.1f}%", f"{p_prior:.0f}%", f"{p_prior:.1f}", f"{p_prior:.0f}",
                         _ordinal(round(p_prior)), f"{p_prior:.1f}th"]
                out.append(_fact("Percentile a year earlier (100 = highest risk)", p_prior, f"{p_prior:.1f}%",
                                 forms, f"{_SCORES_SRC}: percentile", prior.date(), None,
                                 "trend_prior_percentile"))
                phrase = rank_phrase(p_now, p_prior)
                out.append(_fact("Trend: how the model's rating compares with a year earlier", phrase, phrase,
                                 [], f"{_SCORES_SRC}: percentile", as_of, None, "trend_rank_phrase"))
        return out


def _range(r: RatioTrend) -> str:
    return f"{display_forms(r.feature, r.lo)[0]} to {display_forms(r.feature, r.hi)[0]}"


def _pp(d: float | None) -> str:
    return "n/a" if d is None else f"{d:+.1f} pp"


def render_trends(sheet) -> list[str]:
    result: TrendResult | None = sheet.extras.get(TREND_KEY)
    if result is None:
        return []
    shown = result.shown
    if not shown:
        line = (TOO_LITTLE if result.checked == 0 else NONE_OUTSIDE).format(as_of=result.as_of)
        return [line, "", TREND_SENTENCE]
    lines = ["| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |",
             "|---|---|---|---|---|---|---|---|"]
    for r in shown:
        lines.append(f"| {PLAIN_NAMES[r.feature]} | {display_forms(r.feature, r.value)[0]} | {_range(r)} | "
                     f"{_WINDOW_TEXT[r.window]} | {_pp(r.change_1q_pp)} | {_pp(r.change_4q_pp)} | "
                     f"{r.contribution:+.3f} | {r.direction} |")
    lines.append("")
    if len(result.outside) > len(shown):
        lines += [f"{len(result.outside)} of {result.checked} ratios were outside their prior range; "
                  f"the {len(shown)} furthest are shown.", ""]
    lines.append(TREND_SENTENCE)
    return lines


TREND_SECTION.render = render_trends
sections_mod.register(TrendSpecialist())
