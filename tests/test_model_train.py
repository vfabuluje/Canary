"""Tests for training, evaluation, baseline and case studies on a small synthetic dataset."""

import json
from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.model import train as train_mod
from canary.model.__main__ import main
from canary.model.dataset import FEATURE_COLUMNS, assign_split, fails_within_4q
from canary.model.train import CASE_STUDY_CERTS, case_studies, evaluate, train

STRONG = "noncurrent_loans_to_loans"


def _quarters(first_year=2001, last_year=2026):
    return [
        date(y, m, d)
        for y in range(first_year, last_year + 1)
        for m, d in ((3, 31), (6, 30), (9, 30), (12, 31))
    ]


@pytest.fixture(autouse=True)
def small_grid(monkeypatch):
    """Keep tests fast: two combos, few trees."""
    monkeypatch.setattr(
        train_mod,
        "GRID",
        [
            {"max_depth": 2, "learning_rate": 0.3, "min_child_weight": 1},
            {"max_depth": 3, "learning_rate": 0.3, "min_child_weight": 1},
        ],
    )
    monkeypatch.setattr(train_mod, "MAX_TREES", 30)
    monkeypatch.setattr(train_mod, "EARLY_STOPPING_ROUNDS", 5)


@pytest.fixture(scope="module")
def raw() -> pd.DataFrame:
    """40 banks x 2001-2026. Failures (cert: failure quarter): train 2008Q3, 2013Q2;
    test 2019Q4, and the three 2023 case-study banks. Failed banks stop reporting."""
    rng = np.random.default_rng(0)
    quarters = _quarters()
    fail_q = {
        1: date(2008, 9, 30),
        2: date(2013, 6, 30),
        3: date(2019, 12, 31),
        24735: date(2023, 3, 31),
        57053: date(2023, 3, 31),
        59017: date(2023, 6, 30),
    }
    certs = list(fail_q) + list(range(100, 134))
    rows = []
    for cert in certs:
        fq = fail_q.get(cert)
        for i, q in enumerate(quarters):
            if fq is not None and q >= fq:
                break
            qtf = None
            if fq is not None:
                qtf = quarters.index(fq) - i
            row = {c: rng.normal() for c in FEATURE_COLUMNS}
            row[STRONG] = rng.normal() + (6.0 if qtf is not None and qtf <= 4 else 0.0)
            if rng.random() < 0.1:
                row["texas_ratio"] = np.nan
            row.update(
                cert=cert,
                institution_name=CASE_STUDY_CERTS.get(cert, f"Bank {cert}"),
                report_date=q,
                quarters_until_failure=qtf,
                failure_date=fq,
            )
            rows.append(row)
    return pd.DataFrame(rows)


@pytest.fixture
def df(raw) -> pd.DataFrame:
    out = raw.copy()
    out["label"] = fails_within_4q(out["quarters_until_failure"])
    out["split"] = assign_split(out["report_date"])
    return out


@pytest.fixture
def features_path(raw, tmp_path):
    path = tmp_path / "features.parquet"
    raw.to_parquet(path)
    return path


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
        parts = signals.split(", ")
        assert len(parts) == 5
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
