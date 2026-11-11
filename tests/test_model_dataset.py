from datetime import date
from pathlib import Path

import pandas as pd
import pytest
import yaml

from canary.model.dataset import (
    FEATURE_COLUMNS,
    TRAINING_FAILURE_CUTOFF,
    assign_split,
    fails_within_4q,
    load_dataset,
    select_features,
)

MARTS = Path(__file__).parents[1] / "warehouse" / "models" / "marts" / "_marts.yml"


def test_label_values():
    got = fails_within_4q(pd.Series([1, 2, 3, 4]))
    assert got.tolist() == [1, 1, 1, 1]
    got = fails_within_4q(pd.Series([None, 5, 8], dtype="Int64"))
    assert got.tolist() == [0, 0, 0]
    assert got.dtype.kind == "i"


def test_split_boundaries():
    dates = pd.Series(
        pd.to_datetime(
            ["2014-12-31", "2015-03-31", "2015-12-31", "2016-03-31",
             "2024-12-31", "2025-03-31", "2001-03-31"]
        ).date
    )
    assert assign_split(dates).tolist() == [
        "train", "gap", "gap", "test", "test", "not_scored", "train"
    ]


def test_training_labels_only_use_failures_through_2015(tmp_path):
    df = pd.DataFrame(
        {
            "cert": [1, 2, 3, 4],
            "report_date": [date(2014, 12, 31), date(2014, 9, 30), date(2010, 6, 30), date(2022, 12, 31)],
            "quarters_until_failure": pd.array([1, 4, None, 1], dtype="Int64"),
            "failure_date": [date(2015, 3, 31), date(2015, 9, 30), None, date(2023, 3, 10)],
            "institution_name": list("abcd"),
        }
    )
    for c in FEATURE_COLUMNS:
        df[c] = 0.0
    path = tmp_path / "x.parquet"
    df.to_parquet(path)
    out = load_dataset(path)
    train_pos = out[(out["split"] == "train") & (out["label"] == 1)]
    assert len(train_pos) == 2
    assert (pd.to_datetime(train_pos["failure_date"]).dt.date <= TRAINING_FAILURE_CUTOFF).all()
    assert out["label"].tolist() == [1, 1, 0, 1]
    assert out["split"].tolist() == ["train", "train", "train", "test"]


def test_feature_columns_exclude_label_and_ids():
    banned = {"cert", "report_date", "failure_date", "quarters_until_failure",
              "institution_name", "label", "split"}
    assert not banned & set(FEATURE_COLUMNS)
    assert len(FEATURE_COLUMNS) == 31


def test_feature_columns_match_dbt_yml():
    models = yaml.safe_load(MARTS.read_text())["models"]
    model = next(m for m in models if m["name"] == "fct_bank_features")
    names = [c["name"] for c in model["columns"]]
    assert list(FEATURE_COLUMNS) == names[2:]
    assert names[:2] == ["cert", "report_date"]


def test_select_features_missing_column_raises():
    df = pd.DataFrame({c: [1.0] for c in FEATURE_COLUMNS if c != "texas_ratio"})
    with pytest.raises(KeyError, match="texas_ratio"):
        select_features(df)
