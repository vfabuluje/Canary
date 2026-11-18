"""How a bank's ratios moved against their own prior range (descriptive, no model).

The range rule is fixed by convention (spec 2026-11-18-phase5b-trend-design, section 5)
and has not been tested as a warning signal.
"""
from dataclasses import dataclass
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst.labels import PLAIN_NAMES, UNIT
from canary.model.dataset import FEATURE_COLUMNS

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
