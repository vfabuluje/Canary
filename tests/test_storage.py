from datetime import date

import pandas as pd
import pytest

from canary.storage import failures_path, financials_path, write_parquet_atomic


def _frame():
    return pd.DataFrame(
        {
            "NAME": pd.array(["A", None], dtype="string"),
            "CERT": pd.array([1, 2], dtype="int64"),
            "N": pd.array([5, None], dtype="Int64"),
            "ASSET": pd.array([1.5, None], dtype="float64"),
            "REPDTE": pd.to_datetime(["2022-12-31", "2023-03-31"]).astype("datetime64[ns]"),
            "ingested_at": pd.Series(
                pd.to_datetime(["2024-01-01", "2024-01-01"], utc=True)
            ).astype("datetime64[ns, UTC]"),
        }
    )


def test_financials_path(tmp_path):
    assert financials_path(tmp_path, date(2022, 12, 31)) == (
        tmp_path / "financials/repdte=20221231/part.parquet"
    )


def test_failures_path(tmp_path):
    assert failures_path(tmp_path) == tmp_path / "failures/failures.parquet"


def test_round_trip(tmp_path):
    df = _frame()
    path = financials_path(tmp_path, date(2022, 12, 31))
    write_parquet_atomic(df, path)
    out = pd.read_parquet(path)
    pd.testing.assert_frame_equal(out, df)
    assert not path.with_name("part.parquet.tmp").exists()


def _failing_to_parquet(self, path, *a, **k):
    with open(path, "wb") as f:
        f.write(b"junk")
    raise OSError("disk full")


def test_failed_write_leaves_nothing(tmp_path, monkeypatch):
    path = financials_path(tmp_path, date(2022, 12, 31))
    monkeypatch.setattr(pd.DataFrame, "to_parquet", _failing_to_parquet)
    with pytest.raises(OSError):
        write_parquet_atomic(_frame(), path)
    assert not path.exists()
    assert not path.with_name("part.parquet.tmp").exists()


def test_failed_overwrite_keeps_old_file(tmp_path, monkeypatch):
    path = financials_path(tmp_path, date(2022, 12, 31))
    path.parent.mkdir(parents=True)
    path.write_bytes(b"old")
    monkeypatch.setattr(pd.DataFrame, "to_parquet", _failing_to_parquet)
    with pytest.raises(OSError):
        write_parquet_atomic(_frame(), path)
    assert path.read_bytes() == b"old"
    assert not path.with_name("part.parquet.tmp").exists()
