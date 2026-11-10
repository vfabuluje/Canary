import logging
from datetime import date

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from canary.schema import FAILURE_FIELDS, FINANCIAL_FIELDS, Field, SchemaError, to_typed_frame
from canary.storage import write_parquet_atomic

TS = pd.Timestamp("2026-11-09T12:00:00", tz="UTC")


def test_columns_ordered_extras_dropped():
    fields = {"CERT": Field("int64", "c"), "ASSET": Field("float64", "a")}
    df = to_typed_frame([{"ASSET": 1, "ID": "x", "CERT": 5}], fields, TS)
    assert list(df.columns) == ["CERT", "ASSET", "ingested_at"]
    assert str(df["ingested_at"].dtype) == "datetime64[ms, UTC]"


def test_types_applied():
    fields = {
        "CERT": Field("int64", ""),
        "ASSET": Field("float64", ""),
        "NAME": Field("string", ""),
        "REPDTE": Field("date_ymd", ""),
    }
    df = to_typed_frame(
        [{"CERT": 1, "ASSET": 5, "NAME": "A", "REPDTE": "20221231"}], fields, TS
    )
    assert df["CERT"].dtype == "int64"
    assert df["ASSET"].dtype == "float64"
    assert df["NAME"].dtype == "string"
    assert df["REPDTE"].dtype == object
    assert all(isinstance(v, date) for v in df["REPDTE"])
    assert df["REPDTE"].iloc[0] == date(2022, 12, 31)


def test_values_unchanged():
    fields = {"ASSET": Field("float64", ""), "EQ": Field("float64", "")}
    df = to_typed_frame([{"ASSET": 209026000, "EQ": 0}], fields, TS)
    assert df["ASSET"][0] == 209026000.0
    assert df["EQ"][0] == 0.0 and not pd.isna(df["EQ"][0])


def test_empty_string_becomes_null():
    fields = {"COST": Field("float64", ""), "RESDATE": Field("date_mdy", "")}
    df = to_typed_frame([{"COST": "", "RESDATE": ""}, {"COST": 1, "RESDATE": "3/10/2023"}], fields, TS)
    assert pd.isna(df["COST"][0])
    assert pd.isna(df["RESDATE"][0])
    assert df["COST"][1] == 1.0


def test_non_numeric_string_raises():
    with pytest.raises(SchemaError, match="ASSET"):
        to_typed_frame([{"ASSET": "N/A"}], {"ASSET": Field("float64", "")}, TS)


def test_bad_date_raises():
    with pytest.raises(SchemaError, match="FAILDATE"):
        to_typed_frame([{"FAILDATE": "13/45/2023"}], {"FAILDATE": Field("date_mdy", "")}, TS)


def test_mdy_date_parsed():
    df = to_typed_frame([{"FAILDATE": "3/10/2023"}], {"FAILDATE": Field("date_mdy", "")}, TS)
    assert df["FAILDATE"].iloc[0] == date(2023, 3, 10)


def test_parquet_roundtrip_types(tmp_path):
    fields = {"REPDTE": Field("date_ymd", ""), "FAILDATE": Field("date_mdy", "")}
    df = to_typed_frame([{"REPDTE": "20221231", "FAILDATE": "3/10/2023"}, {"REPDTE": "20221231", "FAILDATE": None}], fields, TS)
    path = tmp_path / "part.parquet"
    write_parquet_atomic(df, path)
    schema = pq.read_schema(path)
    assert schema.field("REPDTE").type == pa.date32()
    assert schema.field("FAILDATE").type == pa.date32()
    assert schema.field("ingested_at").type == pa.timestamp("ms", tz="UTC")


def test_nullable_int_allows_missing():
    df = to_typed_frame(
        [{"CERT": None, "FAILYR": "1934"}, {"CERT": 5, "FAILYR": "2023"}], FAILURE_SUBSET, TS
    )
    assert pd.isna(df["CERT"][0])
    assert df["CERT"].dtype == "Int64"
    assert df["FAILYR"][1] == 2023


FAILURE_SUBSET = {"CERT": FAILURE_FIELDS["CERT"], "FAILYR": FAILURE_FIELDS["FAILYR"]}


def test_null_in_int64_raises():
    with pytest.raises(SchemaError, match="CERT"):
        to_typed_frame([{"CERT": None}], {"CERT": Field("int64", "")}, TS)


def test_all_null_column_logs_warning(caplog):
    fields = {"ASSET": Field("float64", ""), "LNCI": Field("float64", "")}
    with caplog.at_level(logging.WARNING, logger="canary"):
        to_typed_frame([{"ASSET": 1}, {"ASSET": 2}], fields, TS)
    assert any(r.levelno == logging.WARNING and "LNCI" in r.getMessage() for r in caplog.records)


def test_field_lists_match_spec():
    assert len(FINANCIAL_FIELDS) == 45
    assert len(FAILURE_FIELDS) == 21
    for f in ("DEPUNINS", "SCHA", "SCHF"):
        assert f in FINANCIAL_FIELDS
    assert list(FINANCIAL_FIELDS)[:3] == ["CERT", "REPDTE", "NAME"]
    assert FINANCIAL_FIELDS["CERT"].dtype == "int64"
    assert FAILURE_FIELDS["CERT"].dtype == "Int64"
