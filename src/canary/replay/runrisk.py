"""Post-hoc run-risk check and corrected Texas-ratio baseline (spec sections 6 and 7).

Both scores were designed after seeing the 2023 failures, so every number built from
them is labeled post-hoc. None of this touches the Phase 3 model or its outputs.
"""

from datetime import date

import numpy as np
import pandas as pd

from canary.model.metrics import flag_watchlist
from canary.model.train import CASE_STUDY_CERTS, _summary

NOTE = (
    "Post-hoc: the run-risk score and the corrected Texas-ratio baseline were designed after "
    "seeing the 2023 failures, so these numbers are not a fair out-of-sample test."
)
TEST_HORIZON_END = date(2025, 12, 31)
TRAIN_ERA_HORIZON_END = date(2015, 12, 31)


def bond_loss_to_equity(df: pd.DataFrame) -> pd.Series:
    """HTM plus AFS unrealized loss over equity. One null counts as zero; both null stays null."""
    htm = df["htm_unrealized_loss_to_equity"]
    afs = df["afs_unrealized_loss_to_equity"]
    return (htm.fillna(0.0) + afs.fillna(0.0)).mask(htm.isna() & afs.isna())


def run_risk_score(df: pd.DataFrame) -> pd.Series:
    """clip(uninsured_to_deposits, 0, 1) * bond_loss_to_equity. Null uninsured gives null."""
    return df["uninsured_to_deposits"].clip(0, 1) * bond_loss_to_equity(df)


def corrected_texas_score(df: pd.DataFrame) -> pd.Series:
    """texas_ratio with negative values (negative equity, insolvent) set to +inf; null stays null."""
    t = df["texas_ratio"]
    return t.mask(t < 0, np.inf)


def score_posthoc(df: pd.DataFrame) -> pd.DataFrame:
    """Rows in the train, gap and test splits (2001-2024) with post-hoc scores and flags."""
    rows = df[df["split"].isin(["train", "gap", "test"])].copy()
    rows["bond_loss_to_equity"] = bond_loss_to_equity(rows)
    rows["run_risk_score"] = run_risk_score(rows)
    rows["corrected_baseline_score"] = corrected_texas_score(rows)
    rows["run_risk_flagged"] = flag_watchlist(rows, "run_risk_score")
    rows["corrected_baseline_flagged"] = flag_watchlist(rows, "corrected_baseline_score")
    return rows.reset_index(drop=True)


def window_summary(rows: pd.DataFrame, score_col: str, flag_col: str, horizon_end: date) -> dict:
    """Phase 3 summary plus the number of rows with no score (they sit below every real score in AUC)."""
    scores = rows[score_col]
    finite = scores[np.isfinite(scores)]
    if (scores == np.inf).any():
        # roc_auc_score rejects inf. For AUC only, put +inf rows just above the largest finite
        # score; they still rank first. Flags were already computed and the input is not changed.
        top = (finite.max() if len(finite) else 0.0) + 1.0
        rows = rows.assign(**{score_col: scores.replace(np.inf, top)})
    out = _summary(rows, score_col, flag_col, horizon_end)
    out["n_null_scores"] = int(scores.isna().sum())
    return out


def watchlist_overlap(rows: pd.DataFrame, flag_a: str, flag_b: str) -> dict:
    a = rows[flag_a].astype(bool)
    b = rows[flag_b].astype(bool)
    return {
        "rows_both": int((a & b).sum()),
        "rows_a_only": int((a & ~b).sum()),
        "rows_b_only": int((~a & b).sum()),
        "banks_both": int(rows.loc[a & b, "cert"].nunique()),
    }


def posthoc_metrics(scored: pd.DataFrame, model_flags: pd.DataFrame) -> dict:
    """All post-hoc numbers. model_flags has cert, report_date, flagged for test-window rows."""
    test = scored[scored["split"] == "test"]
    train_era = scored[scored["split"] == "train"]
    flags = model_flags[["cert", "report_date", "flagged"]].rename(columns={"flagged": "model_flagged"})
    merged = test.merge(flags, on=["cert", "report_date"], how="left")
    merged["model_flagged"] = merged["model_flagged"].fillna(False).astype(bool)

    case_flags = {}
    for cert in CASE_STUDY_CERTS:
        hit = scored[(scored["cert"] == cert) & scored["run_risk_flagged"]]
        case_flags[cert] = sorted(str(pd.Timestamp(d).date()) for d in hit["report_date"])

    return {
        "post_hoc": True,
        "note": NOTE,
        "run_risk": {
            "test_2016_2024": window_summary(test, "run_risk_score", "run_risk_flagged", TEST_HORIZON_END),
            "train_era_2001_2014": window_summary(
                train_era, "run_risk_score", "run_risk_flagged", TRAIN_ERA_HORIZON_END
            ),
        },
        "corrected_baseline": {
            "test_2016_2024": window_summary(
                test, "corrected_baseline_score", "corrected_baseline_flagged", TEST_HORIZON_END
            ),
        },
        "overlap_with_model_test": watchlist_overlap(merged, "run_risk_flagged", "model_flagged"),
        "case_study_flags": case_flags,
    }
