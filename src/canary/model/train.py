"""Train the XGBoost model on 2001-2014, score 2016-2024 once, and build the case studies.

See decisions/0010-label-and-time-split.md and 0011-watchlist-flag-and-metrics.md.
Only `train()` fits anything, and it only ever sees rows with split == "train".
Only `evaluate()` and `case_studies()` score test rows, and nothing is tuned on them.
"""

import itertools
import math
from datetime import date

import numpy as np
import pandas as pd
import xgboost

from canary.model.dataset import FEATURE_COLUMNS, INNER_FIT_END, TRAIN_END, select_features
from canary.model.metrics import (
    auc,
    bank_recall,
    false_alarm_banks,
    false_alarm_rate,
    flag_watchlist,
    lead_times,
)

SEED = 42
CASE_STUDY_CERTS = {24735: "Silicon Valley Bank", 57053: "Signature Bank", 59017: "First Republic Bank"}
CASE_STUDY_START = date(2021, 3, 31)

# 2 x 2 x 2 = 8 combinations, the most the spec allows.
GRID: list[dict] = [
    {"max_depth": d, "learning_rate": lr, "min_child_weight": mcw}
    for d, lr, mcw in itertools.product((3, 5), (0.05, 0.1), (1, 10))
]
MAX_TREES = 500
EARLY_STOPPING_ROUNDS = 30
N_JOBS = 4  # fixed so results do not depend on the machine's core count
N_SIGNALS = 5


def _classifier(params: dict, n_estimators: int, scale_pos_weight: float, **extra) -> xgboost.XGBClassifier:
    return xgboost.XGBClassifier(
        n_estimators=n_estimators,
        scale_pos_weight=scale_pos_weight,
        tree_method="hist",
        eval_metric="aucpr",
        random_state=SEED,
        n_jobs=N_JOBS,
        **params,
        **extra,
    )


def _spw(label: pd.Series) -> float:
    pos = int((label == 1).sum())
    if pos == 0:
        raise ValueError("no positive rows in the fit set; cannot train")
    return float((len(label) - pos) / pos)


def train(df: pd.DataFrame) -> tuple[xgboost.XGBClassifier, dict]:
    """Pick hyperparameters on an inner validation block, then refit on all train rows."""
    tr = df[df["split"] == "train"].reset_index(drop=True)
    dates = pd.to_datetime(tr["report_date"])
    fit = tr[dates <= pd.Timestamp(INNER_FIT_END)]
    valid = tr[(dates > pd.Timestamp(INNER_FIT_END)) & (dates <= pd.Timestamp(TRAIN_END))]
    if valid["label"].sum() == 0:
        raise ValueError("no positive rows in the validation block; cannot early-stop")

    X_fit, y_fit = select_features(fit), fit["label"]
    X_valid, y_valid = select_features(valid), valid["label"]
    spw_fit = _spw(y_fit)

    results = []
    for params in GRID:
        m = _classifier(params, MAX_TREES, spw_fit, early_stopping_rounds=EARLY_STOPPING_ROUNDS)
        m.fit(X_fit, y_fit, eval_set=[(X_valid, y_valid)], verbose=False)
        results.append(
            {"params": params, "val_pr_auc": float(m.best_score), "best_iteration": int(m.best_iteration)}
        )
    best = max(results, key=lambda r: r["val_pr_auc"])  # first one wins ties
    n_trees = best["best_iteration"] + 1

    model = _classifier(best["params"], n_trees, _spw(tr["label"]))
    model.fit(select_features(tr), tr["label"], verbose=False)

    config = {
        "seed": SEED,
        "best_params": best["params"],
        "n_trees": n_trees,
        "grid_results": results,
        "scale_pos_weight_fit": spw_fit,
        "scale_pos_weight_refit": _spw(tr["label"]),
        "n_train_rows": int(len(tr)),
        "n_train_positives": int(tr["label"].sum()),
        "n_fit_rows": int(len(fit)),
        "n_fit_positives": int(fit["label"].sum()),
        "n_valid_rows": int(len(valid)),
        "n_valid_positives": int(valid["label"].sum()),
        "fit_max_date": str(pd.to_datetime(fit["report_date"]).max().date()),
        "valid_max_date": str(pd.to_datetime(valid["report_date"]).max().date()),
        "features": list(FEATURE_COLUMNS),
    }
    return model, config


def _score_test(df: pd.DataFrame, model: xgboost.XGBClassifier) -> pd.DataFrame:
    """Test-split rows with model score, baseline score and watchlist flags (unique index)."""
    test = df[df["split"] == "test"].reset_index(drop=True)
    test["score"] = model.predict_proba(select_features(test))[:, 1]
    test["baseline_score"] = test["texas_ratio"]  # NaN ranks lowest in flag_watchlist
    test["flagged"] = flag_watchlist(test, "score")
    test["baseline_flagged"] = flag_watchlist(test, "baseline_score")
    return test


def _summary(test: pd.DataFrame, score_col: str, flag_col: str) -> dict:
    lt = lead_times(test, flag_col)
    r1 = bank_recall(test, flag_col, 1)
    r2 = bank_recall(test, flag_col, 2)
    scores = test[score_col]
    if scores.isna().any():  # roc_auc_score rejects NaN; put missing scores below every real one
        scores = scores.fillna(scores.min() - 1.0)
    return {
        "auc": auc(test.assign(**{score_col: scores}), score_col),
        "recall": r1.recall,
        "banks_caught": r1.caught,
        "eligible_banks": r1.eligible,
        "caught_certs": r1.caught_certs,
        "recall_2q": r2.recall,
        "banks_caught_2q": r2.caught,
        "eligible_banks_2q": r2.eligible,
        "lead_time_median": float(lt.median()) if len(lt) else float("nan"),
        "lead_time_min": int(lt.min()) if len(lt) else float("nan"),
        "lead_time_max": int(lt.max()) if len(lt) else float("nan"),
        "false_alarm_rate": false_alarm_rate(test, flag_col),
        "false_alarm_banks": false_alarm_banks(test, flag_col),
        "rows_flagged": int(test[flag_col].sum()),
    }


def _jsonable(obj):
    """Plain Python types only; NaN and inf become null."""
    if isinstance(obj, dict):
        return {str(k): _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonable(v) for v in obj]
    if isinstance(obj, np.generic):
        obj = obj.item()
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    return obj


def evaluate(df: pd.DataFrame, model: xgboost.XGBClassifier) -> dict:
    """Score the test split once and compare the model with the texas_ratio baseline."""
    test = _score_test(df, model)
    metrics = _summary(test, "score", "flagged")
    metrics["baseline"] = _summary(test, "baseline_score", "baseline_flagged")
    metrics["n_test_rows"] = int(len(test))
    metrics["n_test_positives"] = int(test["label"].sum())
    return _jsonable(metrics)


def format_signals(contrib_row: np.ndarray) -> str:
    """Up to N_SIGNALS features pushing the score up (contribution > 0), largest first.

    Fewer than N_SIGNALS (even none, giving "") when few features raise the score.
    """
    top = [j for j in np.argsort(-contrib_row, kind="stable")[:N_SIGNALS] if contrib_row[j] > 0]
    return ", ".join(f"{FEATURE_COLUMNS[j]}={contrib_row[j]:+.3f}" for j in top)


def case_studies(df: pd.DataFrame, model: xgboost.XGBClassifier) -> pd.DataFrame:
    """Per-quarter score, national rank and top signals for SVB, Signature and First Republic.

    rank 1 = highest score in that quarter among all test-split banks (ties: cert ascending);
    percentile = 100 * (n_banks - rank + 1) / n_banks, so rank 1 is 100.
    """
    test = _score_test(df, model)
    ordered = test.sort_values(["report_date", "score", "cert"], ascending=[True, False, True], kind="mergesort")
    test["rank"] = ordered.groupby("report_date").cumcount().add(1).reindex(test.index)
    test["n_banks"] = test.groupby("report_date")["cert"].transform("size")
    test["percentile"] = 100.0 * (test["n_banks"] - test["rank"] + 1) / test["n_banks"]

    contrib = model.get_booster().predict(
        xgboost.DMatrix(select_features(test), feature_names=list(FEATURE_COLUMNS)), pred_contribs=True
    )[:, :-1]  # last column is the bias
    keep = test["cert"].isin(CASE_STUDY_CERTS) & (
        pd.to_datetime(test["report_date"]) >= pd.Timestamp(CASE_STUDY_START)
    )
    out = test[keep].copy()
    out["top_signals"] = [format_signals(contrib[i]) for i in out.index]
    cols = [
        "cert", "institution_name", "report_date", "quarters_until_failure", "score",
        "rank", "n_banks", "percentile", "flagged", "top_signals",
    ]
    return out[cols].sort_values(["cert", "report_date"]).reset_index(drop=True)
