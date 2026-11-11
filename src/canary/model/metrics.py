"""Watchlist flags and evaluation metrics for the Phase 3 model.

See decisions/0011-watchlist-flag-and-metrics.md for the reasoning.
"""

import math
from dataclasses import dataclass
from datetime import date

import pandas as pd
from sklearn.metrics import roc_auc_score

WATCHLIST_SHARE = 0.02


@dataclass
class RecallResult:
    caught: int
    eligible: int
    recall: float
    caught_certs: list[int]


def flag_watchlist(df: pd.DataFrame, score_col: str, share: float = WATCHLIST_SHARE) -> pd.Series:
    """Flag the top `share` of banks in each report date (rounded up, at least 1).

    k = ceil(round(n * share, 9)); the round() stops float noise (e.g. 3.0000000000000004)
    from bumping k up by one. Ties are broken by cert ascending. NaN scores rank lowest,
    so a bank with no score is never flagged ahead of a bank with a real score.
    Returns a bool Series aligned to df.index.
    """
    flags = pd.Series(False, index=df.index, dtype=bool)
    for _, group in df.groupby("report_date", sort=False):
        k = math.ceil(round(len(group) * share, 9))
        ordered = group.assign(_s=group[score_col].fillna(float("-inf")))
        ordered = ordered.sort_values(["_s", "cert"], ascending=[False, True], kind="mergesort")
        flags.loc[ordered.index[:k]] = True
    return flags


def _eligible_rows(df: pd.DataFrame, min_quarters: int) -> pd.Series:
    q = pd.to_numeric(df["quarters_until_failure"], errors="coerce")
    return q.between(min_quarters, 4).fillna(False)


def bank_recall(df: pd.DataFrame, flag_col: str, min_quarters: int = 1) -> RecallResult:
    """Share of failing banks flagged at least once while still `min_quarters`-4 quarters out.

    A bank is eligible if it has at least one row in df with quarters_until_failure in
    [min_quarters, 4]. The caller passes test-period rows only.
    """
    eligible_rows = df[_eligible_rows(df, min_quarters)]
    eligible = eligible_rows["cert"].nunique()
    caught_certs = sorted(int(c) for c in eligible_rows.loc[eligible_rows[flag_col].astype(bool), "cert"].unique())
    recall = len(caught_certs) / eligible if eligible else float("nan")
    return RecallResult(len(caught_certs), eligible, recall, caught_certs)


def lead_times(df: pd.DataFrame, flag_col: str) -> pd.Series:
    """Per failing bank, the largest quarters_until_failure (1-4) among its flagged rows."""
    rows = df[df[flag_col].astype(bool) & _eligible_rows(df, 1)]
    out = pd.to_numeric(rows["quarters_until_failure"]).groupby(rows["cert"]).max()
    out.index.name = "cert"
    return out.astype(int)


def false_alarm_rate(df: pd.DataFrame, flag_col: str) -> float:
    """Flagged rows whose label is 0, divided by all flagged rows (1 - precision)."""
    flagged = df[df[flag_col].astype(bool)]
    if flagged.empty:
        return float("nan")
    return float((flagged["label"] == 0).sum() / len(flagged))


def false_alarm_banks(df: pd.DataFrame, flag_col: str, horizon_end: date = date(2025, 12, 31)) -> int:
    """Distinct flagged banks that did not fail by horizon_end (never failed, or failed later)."""
    flagged = df[df[flag_col].astype(bool)]
    fd = pd.to_datetime(flagged["failure_date"])
    survived = fd.isna() | (fd > pd.Timestamp(horizon_end))
    return int(flagged.loc[survived, "cert"].nunique())


def auc(df: pd.DataFrame, score_col: str) -> float:
    return float(roc_auc_score(df["label"], df[score_col]))
