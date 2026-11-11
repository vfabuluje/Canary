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


def _quarters_until(report: date, failure: date) -> int:
    # Same arithmetic as fct_bank_quarters.sql.
    return (failure.year * 4 + (failure.month - 1) // 3 + 1) - (
        report.year * 4 + (report.month - 1) // 3 + 1
    )


def test_training_labels_only_use_failures_through_2015(tmp_path):
    rows = [
        (1, date(2014, 12, 31), date(2015, 11, 6)),   # train, fails in 2015: ok
        (2, date(2015, 9, 30), date(2016, 2, 19)),    # would leak if 2015 were train
        (3, date(2015, 3, 31), date(2015, 12, 1)),    # gap
        (4, date(2010, 6, 30), None),
        (5, date(2022, 12, 31), date(2023, 3, 10)),   # test
    ]
    df = pd.DataFrame(
        {
            "cert": [r[0] for r in rows],
            "report_date": [r[1] for r in rows],
            "quarters_until_failure": pd.array(
                [None if r[2] is None else _quarters_until(r[1], r[2]) for r in rows],
                dtype="Int64",
            ),
            "failure_date": [r[2] for r in rows],
            "institution_name": list("abcde"),
        }
    )
    # Link check: the synthetic quarters match the failure dates.
    assert df["quarters_until_failure"].tolist()[:3] == [4, 2, 3]
    for c in FEATURE_COLUMNS:
        df[c] = 0.0
    path = tmp_path / "x.parquet"
    df.to_parquet(path)
    out = load_dataset(path)

    by_cert = out.set_index("cert")
    assert by_cert.loc[2, "label"] == 1
    assert by_cert.loc[2, "split"] == "gap"
    assert by_cert.loc[3, "split"] == "gap"
    train_pos = out[(out["split"] == "train") & (out["label"] == 1)]
    assert train_pos["cert"].tolist() == [1]
    assert (pd.to_datetime(train_pos["failure_date"]).dt.date <= TRAINING_FAILURE_CUTOFF).all()
    assert out["label"].tolist() == [1, 1, 1, 0, 1]
    assert out["split"].tolist() == ["train", "gap", "gap", "train", "test"]


def test_split_accepts_datetime64():
    d = pd.Series(pd.to_datetime(["2014-12-31", "2015-06-30", "2016-03-31"]))
    assert assign_split(d).tolist() == ["train", "gap", "test"]


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
