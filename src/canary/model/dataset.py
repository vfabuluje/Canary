"""Dataset rules for the Phase 3 model: label, time split and feature list.

See decisions/0010-label-and-time-split.md for the reasoning.
"""

from datetime import date
from pathlib import Path

import pandas as pd

# Same 31 names, same order, as fct_bank_features in warehouse/models/marts/_marts.yml.
FEATURE_COLUMNS: tuple[str, ...] = (
    "equity_to_assets",
    "leverage_ratio",
    "tier1_risk_based_ratio",
    "total_risk_based_ratio",
    "noncurrent_loans_to_loans",
    "nonaccrual_ore_to_assets",
    "past_due_30_89_to_assets",
    "allowance_to_loans",
    "net_charge_offs_to_loans_ann",
    "provision_to_assets_ann",
    "construction_loans_to_loans",
    "cre_loans_to_loans",
    "texas_ratio",
    "return_on_assets",
    "return_on_equity",
    "net_interest_margin",
    "efficiency_ratio",
    "interest_expense_to_assets_ann",
    "loans_to_deposits",
    "uninsured_to_deposits",
    "brokered_to_deposits",
    "core_deposits_to_assets",
    "fhlb_to_assets",
    "volatile_liabilities_to_assets",
    "cash_to_assets",
    "htm_unrealized_loss_to_equity",
    "afs_unrealized_loss_to_equity",
    "securities_to_assets",
    "log_total_assets",
    "asset_growth_4q",
    "deposit_growth_4q",
)

TRAIN_END = date(2014, 12, 31)
TEST_START = date(2016, 3, 31)
TEST_END = date(2024, 12, 31)
INNER_FIT_END = date(2011, 12, 31)
TRAINING_FAILURE_CUTOFF = date(2015, 12, 31)


def fails_within_4q(quarters_until_failure: pd.Series) -> pd.Series:
    """1 if the bank fails 1-4 quarters after the report date, else 0 (incl. null)."""
    q = pd.to_numeric(quarters_until_failure, errors="coerce")
    return q.between(1, 4).fillna(False).astype(int)


def assign_split(report_date: pd.Series) -> pd.Series:
    """Label each report date: train, gap (2015), test, or not_scored (after 2024)."""
    d = pd.to_datetime(report_date)
    out = pd.Series("not_scored", index=d.index, dtype=object)
    out[d <= pd.Timestamp(TRAIN_END)] = "train"
    out[(d > pd.Timestamp(TRAIN_END)) & (d < pd.Timestamp(TEST_START))] = "gap"
    out[(d >= pd.Timestamp(TEST_START)) & (d <= pd.Timestamp(TEST_END))] = "test"
    return out


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing:
        raise KeyError(f"missing feature columns: {missing}")
    return df[list(FEATURE_COLUMNS)]


def load_dataset(path: Path) -> pd.DataFrame:
    """Read the Parquet export and add `label` and `split` columns."""
    df = pd.read_parquet(path)
    df["label"] = fails_within_4q(df["quarters_until_failure"])
    df["split"] = assign_split(df["report_date"])
    return df
