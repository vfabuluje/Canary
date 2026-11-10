from datetime import date

import pandas as pd
import pytest

from canary.fdic_client import FDICClient, IncompleteResponseError
from canary.ingest_failures import run_failures
from canary.schema import FAILURE_FIELDS
from canary.storage import failures_path
from conftest import FakeSession, page


def make_client(rows):
    session = FakeSession([page(rows, len(rows))])
    return FDICClient(session=session, pause=0, sleep=lambda s: None), session


def test_run_failures_writes_typed_file(tmp_path):
    rows = [
        {"CERT": 24735, "NAME": "SILICON VALLEY BANK", "FAILDATE": "3/10/2023",
         "FAILYR": "2023", "COST": 18744254.463, "ID": "x"},
        {"CERT": None, "NAME": "OLD BANK", "FAILDATE": "1/5/1934",
         "FAILYR": "1934", "COST": ""},
    ]
    client, _ = make_client(rows)
    assert run_failures(tmp_path, client) == 2
    df = pd.read_parquet(failures_path(tmp_path))
    assert list(df["FAILDATE"]) == [date(2023, 3, 10), date(1934, 1, 5)]
    assert str(df["CERT"].dtype) == "Int64"
    assert df["CERT"].isna().sum() == 1
    assert "ID" not in df.columns


def test_run_failures_requests_21_fields(tmp_path):
    client, session = make_client([{"CERT": 1, "FAILDATE": "3/10/2023", "FAILYR": "2023"}])
    run_failures(tmp_path, client)
    params = session.calls[0][1]
    assert params["fields"].split(",") == list(FAILURE_FIELDS)
    assert len(FAILURE_FIELDS) == 21


def test_empty_failures_response_keeps_existing_file(tmp_path):
    client, _ = make_client([{"CERT": 1, "FAILDATE": "3/10/2023", "FAILYR": "2023"}])
    run_failures(tmp_path, client)
    before = failures_path(tmp_path).read_bytes()
    empty_client, _ = make_client([])
    with pytest.raises(IncompleteResponseError, match="0 rows"):
        run_failures(tmp_path, empty_client)
    assert failures_path(tmp_path).read_bytes() == before
