"""Tests for training, evaluation, baseline and case studies on a small synthetic dataset."""

import hashlib
import json

import numpy as np
import pandas as pd
import pytest

from canary.model.__main__ import main
from canary.model.dataset import FEATURE_COLUMNS
from canary.model.train import CASE_STUDY_CERTS, case_studies, evaluate, format_signals, train

STRONG = "noncurrent_loans_to_loans"  # same as tests/conftest.py


@pytest.fixture(autouse=True)
def _small(small_grid):
    pass


def test_train_uses_only_train_rows(df):
    model, config = train(df)
    train_rows = df[df["split"] == "train"]
    assert config["n_train_rows"] == len(train_rows)
    assert config["n_train_positives"] == int(train_rows["label"].sum())
    assert config["n_fit_rows"] + config["n_valid_rows"] == len(train_rows)
    assert max(config["fit_max_date"], config["valid_max_date"]) <= "2014-12-31"
    assert len(config["grid_results"]) == 2
    assert config["n_trees"] >= 1


def test_train_ignores_test_rows(df):
    """Scrambling every non-train row must not change the model."""
    other = df.copy()
    mask = other["split"] != "train"
    other.loc[mask, "label"] = 1 - other.loc[mask, "label"]
    other.loc[mask, STRONG] = 99.0
    a, _ = train(df)
    b, _ = train(other)
    X = df[list(FEATURE_COLUMNS)]
    assert np.array_equal(a.predict_proba(X), b.predict_proba(X))


def test_train_is_deterministic(df):
    a, _ = train(df)
    b, _ = train(df)
    X = df[list(FEATURE_COLUMNS)]
    assert np.array_equal(a.predict_proba(X), b.predict_proba(X))


def test_evaluate_metrics_keys(df):
    model, _ = train(df)
    m = evaluate(df, model)
    for key in (
        "auc",
        "recall",
        "recall_2q",
        "eligible_banks",
        "lead_time_median",
        "false_alarm_rate",
        "false_alarm_banks",
        "baseline",
    ):
        assert key in m
    assert m["auc"] > 0.8
    assert m["eligible_banks"] == 4  # cert 3 and the three 2023 banks
    assert "auc" in m["baseline"] and "recall" in m["baseline"]
    json.dumps(m)  # serializable
    json.dumps(m, allow_nan=False)  # NaN already turned into null


def test_baseline_ranks_nan_lowest(df):
    model, _ = train(df)
    m = evaluate(df, model)
    # texas_ratio is pure noise in the fixture, so baseline AUC is near chance, below the model.
    assert m["baseline"]["auc"] < m["auc"]


def test_case_studies_columns_and_top_signals(df):
    model, _ = train(df)
    cs = case_studies(df, model)
    assert list(cs.columns) == [
        "cert",
        "institution_name",
        "report_date",
        "quarters_until_failure",
        "score",
        "rank",
        "n_banks",
        "percentile",
        "flagged",
        "top_signals",
    ]
    assert set(cs["cert"]) == set(CASE_STUDY_CERTS)
    assert (pd.to_datetime(cs["report_date"]) >= pd.Timestamp("2021-03-31")).all()
    assert cs["rank"].between(1, cs["n_banks"]).all()
    assert cs["percentile"].between(0, 100).all()
    for signals in cs["top_signals"]:
        parts = [p for p in signals.split(", ") if p]
        assert len(parts) <= 5
        for p in parts:
            name, value = p.split("=")
            assert name in FEATURE_COLUMNS
            assert value.startswith("+")


def test_case_study_rank_is_national(df):
    model, _ = train(df)
    cs = case_studies(df, model)
    test = df[df["split"] == "test"]
    row = cs.iloc[0]
    quarter_rows = test[test["report_date"] == row["report_date"]]
    assert row["n_banks"] == len(quarter_rows)
    assert row["n_banks"] > 3


def test_evaluate_refuses_to_overwrite(features_path, tmp_path):
    out = tmp_path / "out"
    assert main(["train", "--features", str(features_path), "--out", str(out)]) == 0
    assert main(["evaluate", "--features", str(features_path), "--out", str(out)]) == 0
    first = (out / "metrics.json").read_text()
    assert main(["evaluate", "--features", str(features_path), "--out", str(out)]) == 1
    assert (out / "metrics.json").read_text() == first
    assert main(["evaluate", "--features", str(features_path), "--out", str(out), "--force"]) == 0
    assert json.loads((out / "metrics.json").read_text())["rerun"] is True


def test_cli_end_to_end_smoke(features_path, tmp_path):
    out = tmp_path / "out"
    assert main(["train", "--features", str(features_path), "--out", str(out)]) == 0
    assert (out / "model.json").exists() and (out / "run_config.json").exists()
    assert main(["evaluate", "--features", str(features_path), "--out", str(out)]) == 0
    for name in ("model.json", "run_config.json", "scores_test.parquet", "metrics.json", "case_studies.csv"):
        assert (out / name).exists()
    scores = pd.read_parquet(out / "scores_test.parquet")
    assert (pd.to_datetime(scores["report_date"]) >= pd.Timestamp("2016-03-31")).all()
    assert "rerun" not in json.loads((out / "metrics.json").read_text())


def test_evaluate_without_model_fails(features_path, tmp_path):
    assert main(["evaluate", "--features", str(features_path), "--out", str(tmp_path / "none")]) == 1


def test_format_signals_positive_only():
    contrib = np.zeros(len(FEATURE_COLUMNS))
    contrib[0], contrib[1], contrib[2], contrib[3] = 0.5, -0.4, 0.2, 0.0
    out = format_signals(contrib)
    assert out == f"{FEATURE_COLUMNS[0]}=+0.500, {FEATURE_COLUMNS[2]}=+0.200"
    assert format_signals(-np.ones(len(FEATURE_COLUMNS))) == ""


def test_case_study_signals_never_non_positive(df):
    model, _ = train(df)
    for signals in case_studies(df, model)["top_signals"]:
        parts = [p for p in signals.split(", ") if p]
        assert len(parts) <= 5
        assert all(float(p.split("=")[1]) > 0 for p in parts)


def test_metrics_record_run_config_and_model_hash(features_path, tmp_path):
    out = tmp_path / "out"
    assert main(["train", "--features", str(features_path), "--out", str(out)]) == 0
    assert main(["evaluate", "--features", str(features_path), "--out", str(out)]) == 0
    metrics = json.loads((out / "metrics.json").read_text())
    assert metrics["run_config"] == json.loads((out / "run_config.json").read_text())
    assert metrics["model_sha256"] == hashlib.sha256((out / "model.json").read_bytes()).hexdigest()
