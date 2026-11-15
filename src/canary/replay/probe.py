"""Probes of the saved Phase 3 model (spec sections 8.2-8.4 and G1).

The model is only used to predict; nothing here fits or changes it.
"""

from datetime import date

import numpy as np
import pandas as pd
import xgboost

from canary.model.dataset import FEATURE_COLUMNS, select_features
from canary.model.train import CASE_STUDY_CERTS, CASE_STUDY_START
from canary.replay.analysis import credit_loss_profile


def _grid(stop: float) -> np.ndarray:
    return np.round(np.arange(0.0, stop + 0.05, 0.1), 2)


WHAT_IF_GRID = {
    "htm_unrealized_loss_to_equity": _grid(1.5),
    "afs_unrealized_loss_to_equity": _grid(1.0),
    "uninsured_to_deposits": _grid(1.0),
}
# Each bank's last report before it failed.
WHAT_IF_ROWS = [(24735, date(2022, 12, 31)), (57053, date(2022, 12, 31)), (59017, date(2023, 3, 31))]


def _contribs(model: xgboost.XGBClassifier, rows: pd.DataFrame) -> np.ndarray:
    matrix = xgboost.DMatrix(select_features(rows), feature_names=list(FEATURE_COLUMNS))
    return model.get_booster().predict(matrix, pred_contribs=True)[:, :-1]  # last column is the bias


def _format(contrib_row: np.ndarray, n: int, sign: int) -> str:
    """Up to n features whose contribution has the given sign, strongest first (name=+0.123)."""
    order = np.argsort(-sign * contrib_row, kind="stable")
    picked = [j for j in order[:n] if sign * contrib_row[j] > 0]
    return ", ".join(f"{FEATURE_COLUMNS[j]}={contrib_row[j]:+.3f}" for j in picked)


def contributions(model: xgboost.XGBClassifier, rows: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Per row, the features pushing the score up (top_positive) and down (top_negative)."""
    c = _contribs(model, rows)
    return pd.DataFrame({
        "cert": rows["cert"].to_numpy(),
        "report_date": rows["report_date"].to_numpy(),
        "top_positive": [_format(r, n, +1) for r in c],
        "top_negative": [_format(r, n, -1) for r in c],
    })


def national_rank(rows: pd.DataFrame, score_col: str) -> pd.Series:
    """Rank within each report date: 1 = highest score, ties by cert ascending, NaN last.

    Same ordering as flag_watchlist, so rank <= k exactly when the row is flagged.
    """
    ordered = rows.assign(_s=rows[score_col].fillna(float("-inf")))
    ordered = ordered.sort_values(["report_date", "_s", "cert"], ascending=[True, False, True], kind="mergesort")
    return ordered.groupby("report_date").cumcount().add(1).reindex(rows.index)


def _percentile(rank: pd.Series, n: pd.Series) -> pd.Series:
    return 100.0 * (n - rank + 1) / n


def what_if(
    model: xgboost.XGBClassifier,
    test_scored: pd.DataFrame,
    cert: int,
    report_date: date,
    grid: dict = WHAT_IF_GRID,
) -> pd.DataFrame:
    """Change one feature at a time on one bank-quarter; score it and rank it against that quarter.

    rank = 1 + number of other banks that quarter with a higher real score (the bank's own
    original row is left out, so it is not counted twice). n_banks counts every bank that quarter.
    """
    quarter = test_scored[test_scored["report_date"] == report_date]
    own = quarter[quarter["cert"] == cert]
    if len(own) != 1:
        raise ValueError(f"expected one row for cert {cert} at {report_date}, found {len(own)}")
    others = quarter.loc[quarter["cert"] != cert, "score"].to_numpy()
    base = select_features(own)
    out = []
    for feature, values in grid.items():
        probes = pd.concat([base] * len(values), ignore_index=True)
        probes[feature] = values
        scores = model.predict_proba(probes)[:, 1]
        for value, score in zip(values, scores):
            rank = 1 + int((others > score).sum())
            n = len(quarter)
            out.append({
                "cert": cert, "report_date": report_date, "feature": feature, "value": float(value),
                "score": float(score), "rank": rank, "n_banks": n,
                "percentile": 100.0 * (n - rank + 1) / n,
                "actual_value": float(base.iloc[0][feature]),
            })
    return pd.DataFrame(out)


def test_misses(model: xgboost.XGBClassifier, test_scored: pd.DataFrame) -> pd.DataFrame:
    """Failed banks eligible in the test window (a row 1-4 quarters out) that were never flagged on one.

    For each, its highest-scoring eligible row, that row's national percentile and top 3 signals.
    """
    ranked = test_scored.assign(
        _rank=national_rank(test_scored, "score"),
        _n=test_scored.groupby("report_date")["cert"].transform("size"),
    )
    q = pd.to_numeric(ranked["quarters_until_failure"], errors="coerce")
    eligible = ranked[q.between(1, 4)]
    caught = set(eligible.loc[eligible["flagged"].astype(bool), "cert"])
    missed = eligible[~eligible["cert"].isin(caught)]
    best = missed.sort_values(["cert", "score", "report_date"], ascending=[True, False, False], kind="mergesort")
    best = best.drop_duplicates("cert", keep="first").copy()

    best["best_percentile"] = _percentile(best["_rank"], best["_n"])
    c = _contribs(model, best) if len(best) else np.empty((0, len(FEATURE_COLUMNS)))
    best["top_signals"] = [_format(r, 3, +1) for r in c]
    best["credit_loss"] = credit_loss_profile(best)
    cols = [
        "cert", "institution_name", "failure_date", "report_date", "quarters_until_failure",
        "best_percentile", "top_signals", "credit_loss",
    ]
    return best[cols].reset_index(drop=True)


test_misses.__test__ = False  # not a pytest test, despite the name


def replay_banks(test_scored: pd.DataFrame, scored: pd.DataFrame) -> pd.DataFrame:
    """SVB, Signature and First Republic from 2021-03-31: model, run-risk and corrected-baseline side by side.

    Model ranks are national among test-window banks; run-risk and corrected-baseline ranks among
    all banks in `scored` that quarter (the same banks for test-window quarters).
    """
    model = test_scored.assign(
        model_rank=national_rank(test_scored, "score"),
        _n=test_scored.groupby("report_date")["cert"].transform("size"),
    )
    model["model_percentile"] = _percentile(model["model_rank"], model["_n"])
    model = model.rename(columns={"score": "model_score", "flagged": "model_flagged"})

    post = scored.assign(
        run_risk_rank=national_rank(scored, "run_risk_score"),
        corrected_baseline_rank=national_rank(scored, "corrected_baseline_score"),
    )
    post_cols = [
        "cert", "report_date", "run_risk_score", "run_risk_rank", "run_risk_flagged",
        "corrected_baseline_rank", "corrected_baseline_flagged",
    ]
    keep = model["cert"].isin(CASE_STUDY_CERTS) & (
        pd.to_datetime(model["report_date"]) >= pd.Timestamp(CASE_STUDY_START)
    )
    out = model[keep].merge(post[post_cols], on=["cert", "report_date"], how="left", validate="one_to_one")
    cols = [
        "cert", "institution_name", "report_date", "quarters_until_failure", "model_score",
        "model_rank", "model_percentile", "model_flagged", "run_risk_score", "run_risk_rank",
        "run_risk_flagged", "corrected_baseline_rank", "corrected_baseline_flagged",
        "htm_unrealized_loss_to_equity", "afs_unrealized_loss_to_equity", "uninsured_to_deposits",
        "tier1_risk_based_ratio", "interest_expense_to_assets_ann", "securities_to_assets",
    ]
    return out[cols].sort_values(["cert", "report_date"]).reset_index(drop=True)
