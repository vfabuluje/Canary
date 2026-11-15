import numpy as np
import pandas as pd
import pytest

from canary.model.train import CASE_STUDY_CERTS, _jsonable, _summary
from canary.replay.runrisk import (
    corrected_texas_score,
    posthoc_metrics,
    run_risk_score,
    score_posthoc,
    watchlist_overlap,
    window_summary,
)


def _with_signal(df, seed=1):
    out = df.copy()
    rng = np.random.default_rng(seed)
    n = len(out)
    out["htm_unrealized_loss_to_equity"] = rng.uniform(0, 1, n)
    out["afs_unrealized_loss_to_equity"] = rng.uniform(0, 0.5, n)
    out["uninsured_to_deposits"] = rng.uniform(0, 1, n)
    return out


def test_run_risk_score_cases():
    df = pd.DataFrame({
        "htm_unrealized_loss_to_equity": [0.5, np.nan, 0.5, np.nan, -0.2, 0.4],
        "afs_unrealized_loss_to_equity": [0.1, 0.3, np.nan, np.nan, 0.0, 0.0],
        "uninsured_to_deposits":         [0.5, 0.5, 0.5, 0.5, 0.9, 1.7],
    })
    before = df.copy()
    s = run_risk_score(df)
    assert s.tolist()[:3] == pytest.approx([0.3, 0.15, 0.25])
    assert np.isnan(s[3])
    assert s[4] == pytest.approx(-0.18)
    assert s[5] == pytest.approx(0.4)
    assert df.equals(before)


def test_run_risk_null_uninsured_is_null():
    df = pd.DataFrame({
        "htm_unrealized_loss_to_equity": [0.5],
        "afs_unrealized_loss_to_equity": [0.1],
        "uninsured_to_deposits": [np.nan],
    })
    assert np.isnan(run_risk_score(df)[0])


def test_corrected_texas_insolvent_ranks_worst():
    df = pd.DataFrame({"texas_ratio": [0.2, -3.0, 5.0, np.nan]})
    s = corrected_texas_score(df)
    assert s[1] == np.inf and s[0] < s[2] and np.isnan(s[3])


def test_score_posthoc_window_and_flags(df):
    before = df.copy()
    scored = _scored(df)
    d = pd.to_datetime(scored["report_date"])
    assert d.min() == pd.Timestamp("2001-03-31") and d.max() == pd.Timestamp("2024-12-31")
    assert scored["split"].isin(["train", "gap", "test"]).all()
    per_q = scored.groupby("report_date")["run_risk_flagged"].sum()
    assert (per_q >= 1).all()
    assert (scored.groupby("report_date")["corrected_baseline_flagged"].sum() >= 1).all()
    assert scored.index.equals(pd.RangeIndex(len(scored)))
    assert df.equals(before)


def _scored(df):
    return score_posthoc(_with_signal(df))


def test_window_summary_reports_null_scores(df):
    scored = _scored(df)
    scored.loc[scored.index[::7], "run_risk_score"] = np.nan
    test = scored[scored["split"] == "test"]
    out = window_summary(test, "run_risk_score", "run_risk_flagged", pd.Timestamp("2025-12-31").date())
    assert np.isfinite(out["auc"])
    assert out["n_null_scores"] == int(test["run_risk_score"].isna().sum()) > 0


def test_window_summary_inf_score_ok(df):
    scored = _scored(df)
    test = scored[scored["split"] == "test"].copy()
    test.loc[test.index[:5], "corrected_baseline_score"] = np.inf
    out = window_summary(test, "corrected_baseline_score", "corrected_baseline_flagged",
                         pd.Timestamp("2025-12-31").date())
    assert np.isfinite(out["auc"])
    assert test["corrected_baseline_score"].iloc[:5].eq(np.inf).all()  # input untouched


def test_watchlist_overlap_counts():
    rows = pd.DataFrame({
        "cert": [1, 1, 2, 3],
        "a": [True, True, True, False],
        "b": [True, False, False, True],
    })
    out = watchlist_overlap(rows, "a", "b")
    assert out == {"rows_both": 1, "rows_a_only": 2, "rows_b_only": 1, "banks_both": 1}


def test_posthoc_metrics_labeled(df):
    scored = _scored(df)
    test = scored[scored["split"] == "test"]
    model_flags = test[["cert", "report_date"]].copy()
    model_flags["flagged"] = (model_flags["cert"] % 2 == 0)
    before = scored.copy()
    m = posthoc_metrics(scored, model_flags)
    assert m["post_hoc"] is True and "2023" in m["note"]
    assert set(m["case_study_flags"]) == {24735, 57053, 59017}
    assert set(m["run_risk"]) == {"test_2016_2024", "train_era_2001_2014"}
    assert set(m["corrected_baseline"]) == {"test_2016_2024"}
    assert set(m["overlap_with_model_test"]) == {"rows_both", "rows_a_only", "rows_b_only", "banks_both"}
    _jsonable(m)
    assert scored.equals(before)


def test_summary_default_horizon_unchanged(df):
    test = df[df["split"] == "test"].copy()
    test["score"] = test["noncurrent_loans_to_loans"]
    from canary.model.metrics import flag_watchlist
    test["flagged"] = flag_watchlist(test, "score")
    from datetime import date
    assert _summary(test, "score", "flagged") == _summary(test, "score", "flagged", horizon_end=date(2025, 12, 31))
