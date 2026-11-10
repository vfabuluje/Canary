import re
from datetime import date

import pytest

from canary.athena_ddl import AthenaError, DDL_DIR, load_sql, render, run, statements
from canary.config import ConfigError, Settings
from canary.quarters import quarter_ends
from canary.schema import FAILURE_FIELDS, FINANCIAL_FIELDS

TYPE_MAP = {
    "string": "string",
    "int64": "bigint",
    "Int64": "bigint",
    "float64": "double",
    "date_ymd": "date",
    "date_mdy": "date",
}


def parse_columns(sql: str) -> list[tuple[str, str]]:
    """Column (name, type) pairs from the first parenthesised block of a CREATE."""
    body = sql[sql.index("(") + 1 : sql.index("\n)")]
    pairs = []
    for line in body.splitlines():
        line = line.strip().rstrip(",")
        if line:
            name, dtype = line.split()
            pairs.append((name, dtype))
    return pairs


def expected(fields: dict, skip: set[str] = frozenset()) -> list[tuple[str, str]]:
    cols = [(n.lower(), TYPE_MAP[f.dtype]) for n, f in fields.items() if n not in skip]
    return cols + [("ingested_at", "timestamp")]


def test_render_fills_bucket():
    assert render("s3://{{bucket}}/raw/", "my-bucket") == "s3://my-bucket/raw/"


@pytest.mark.parametrize("bucket", ["", "   "])
def test_render_requires_bucket(bucket):
    with pytest.raises(ConfigError):
        render("s3://{{bucket}}/raw/", bucket)


def test_financials_ddl_columns_match_schema():
    sql = load_sql("fdic_financials.sql", "b")
    assert parse_columns(sql) == expected(FINANCIAL_FIELDS, skip={"REPDTE"})
    # repdte is the partition column only; it must not also be a regular column
    assert len(re.findall(r"\brepdte\b", sql.split("PARTITIONED BY")[0], re.I)) == 0
    assert "PARTITIONED BY (repdte string)" in sql


def test_failures_ddl_columns_match_schema():
    sql = load_sql("fdic_failures.sql", "b")
    assert parse_columns(sql) == expected(FAILURE_FIELDS)


def test_statements_are_idempotent():
    stmts = statements(Settings(bucket="b"), date(2026, 6, 30))
    creates = [s for s in stmts if s.lstrip().upper().startswith("CREATE")]
    assert len(creates) == 2
    assert all("IF NOT EXISTS" in s.upper() for s in creates)
    assert not any("DROP" in s.upper() for s in stmts)
    assert all("{{bucket}}" not in s for s in stmts)


def test_enum_values_cover_all_quarters():
    stmts = statements(Settings(bucket="b"), date(2026, 6, 30))
    alter = [s for s in stmts if s.lstrip().upper().startswith("ALTER TABLE")]
    assert len(alter) == 1
    assert "canary_raw.fdic_financials SET TBLPROPERTIES" in alter[0]
    match = re.search(r"'projection\.repdte\.values'\s*=\s*'([^']*)'", alter[0])
    assert match
    want = [d.strftime("%Y%m%d") for d in quarter_ends(date(2001, 3, 31), date(2026, 6, 30))]
    assert match.group(1).split(",") == want


class FakeAthena:
    def __init__(self, state: str, reason: str = ""):
        self.state, self.reason, self.started = state, reason, []

    def start_query_execution(self, QueryString, WorkGroup):
        self.started.append((QueryString, WorkGroup))
        return {"QueryExecutionId": "q1"}

    def get_query_execution(self, QueryExecutionId):
        status = {"State": self.state}
        if self.reason:
            status["StateChangeReason"] = self.reason
        return {"QueryExecution": {"Status": status}}


def test_run_raises_on_failed_query():
    client = FakeAthena("FAILED", "SYNTAX_ERROR: line 1")
    with pytest.raises(AthenaError, match="SYNTAX_ERROR"):
        run(["SELECT bad"], client, "canary")


def test_run_succeeds_and_uses_workgroup():
    client = FakeAthena("SUCCEEDED")
    run(["SELECT 1", "SELECT 2"], client, "canary")
    assert client.started == [("SELECT 1", "canary"), ("SELECT 2", "canary")]
