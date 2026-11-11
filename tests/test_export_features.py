import io

import boto3
import pandas as pd
import pytest
from moto import mock_aws

from canary.export_features import export_sql, main

BUCKET = "test-bucket"
ENV = {"CANARY_BUCKET": BUCKET}


def parquet_bytes(df: pd.DataFrame) -> bytes:
    buf = io.BytesIO()
    df.to_parquet(buf, index=False)
    return buf.getvalue()


class FakeAthena:
    """Drops two Parquet parts under the UNLOAD prefix, then reports `state`."""

    def __init__(self, s3, state="SUCCEEDED", write=True):
        self.s3, self.state, self.write, self.calls = s3, state, write, 0

    def start_query_execution(self, QueryString, WorkGroup):
        self.calls += 1
        if self.state == "SUCCEEDED" and self.write:
            prefix = QueryString.split("TO 's3://" + BUCKET + "/")[1].split("'")[0]
            for i, n in enumerate((2, 3)):
                df = pd.DataFrame(
                    {
                        "cert": range(n),
                        "report_date": ["2020-03-31"] * n,
                        "roa": [0.1] * n,
                        "quarters_until_failure": [None] * n,
                        "failure_date": [None] * n,
                        "institution_name": ["x"] * n,
                    }
                )
                self.s3.put_object(Bucket=BUCKET, Key=f"{prefix}part-{i}", Body=parquet_bytes(df))
        return {"QueryExecutionId": "q1"}

    def get_query_execution(self, QueryExecutionId):
        status = {"State": self.state}
        if self.state == "FAILED":
            status["StateChangeReason"] = "boom"
        return {"QueryExecution": {"Status": status}}


@pytest.fixture
def s3():
    with mock_aws():
        client = boto3.client("s3", region_name="us-east-1")
        client.create_bucket(Bucket=BUCKET)
        yield client


def test_export_sql_targets_athena_results_prefix():
    sql = export_sql("b", "20260101T000000Z")
    assert "s3://b/athena-results/exports/20260101T000000Z/" in sql
    assert "PARQUET" in sql
    assert "f.cert = q.cert AND f.report_date = q.report_date" in sql


def test_export_writes_concatenated_parquet(s3, tmp_path):
    out = tmp_path / "sub" / "f.parquet"
    assert main(["--out", str(out)], FakeAthena(s3), s3, ENV) == 0
    df = pd.read_parquet(out)
    assert len(df) == 5
    assert {"roa", "quarters_until_failure", "failure_date", "institution_name"} <= set(df.columns)
    assert not out.with_name("f.parquet.tmp").exists()


def test_export_failed_query_leaves_no_file(s3, tmp_path):
    out = tmp_path / "f.parquet"
    assert main(["--out", str(out)], FakeAthena(s3, "FAILED"), s3, ENV) == 1
    assert not out.exists()


def test_export_failure_keeps_existing_file(s3, tmp_path):
    out = tmp_path / "f.parquet"
    out.write_text("good")
    assert main(["--out", str(out)], FakeAthena(s3, "FAILED"), s3, ENV) == 1
    assert out.read_text() == "good"


def test_export_no_files_fails(s3, tmp_path):
    out = tmp_path / "f.parquet"
    assert main(["--out", str(out)], FakeAthena(s3, write=False), s3, ENV) == 1
    assert not out.exists()


def test_missing_bucket_env_fails(s3, tmp_path):
    athena = FakeAthena(s3)
    assert main(["--out", str(tmp_path / "f.parquet")], athena, s3, {}) == 1
    assert athena.calls == 0
