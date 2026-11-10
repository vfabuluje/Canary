from datetime import date

import pandas as pd
import pytest

from canary.fdic_client import FDICAPIError, FDICClient, IncompleteResponseError
from canary.ingest_financials import (
    latest_report_date,
    pull_quarter,
    quarters_to_pull,
    run_financials,
)
from canary.quarters import quarter_ends
from canary.schema import FINANCIAL_FIELDS
from canary.storage import financials_path
from conftest import FakeSession, page


def make_client(responses):
    session = FakeSession(responses)
    return FDICClient(session=session, pause=0, sleep=lambda s: None), session


def row(cert, repdte):
    r = {f: None for f in FINANCIAL_FIELDS}
    r["REPDTE"] = repdte
    r["CERT"] = cert
    return r


def touch(root, d, name="part.parquet"):
    p = financials_path(root, d).with_name(name)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b"x")


def test_latest_report_date():
    client, session = make_client([page([{"REPDTE": "20260630", "ID": "1"}], 1)])
    assert latest_report_date(client) == date(2026, 6, 30)
    assert session.calls[0][1]["sort_order"] == "DESC"
    assert session.calls[0][1]["limit"] == 1


def test_quarters_to_pull_resume_and_refresh(tmp_path):
    qs = quarter_ends(date(2022, 3, 31), date(2023, 6, 30))
    for i in (0, 1, 3, 4, 5):
        touch(tmp_path, qs[i])
    assert quarters_to_pull(qs, tmp_path) == [qs[2], qs[4], qs[5]]


def test_quarters_to_pull_force(tmp_path):
    qs = quarter_ends(date(2022, 3, 31), date(2023, 6, 30))
    for q in qs:
        touch(tmp_path, q)
    assert quarters_to_pull(qs, tmp_path, force=True) == qs


def test_leftover_tmp_file_counts_as_missing(tmp_path):
    qs = quarter_ends(date(2022, 3, 31), date(2023, 6, 30))
    touch(tmp_path, qs[0], "part.parquet.tmp")
    for q in qs[1:]:
        touch(tmp_path, q)
    assert qs[0] in quarters_to_pull(qs, tmp_path)


def test_pull_quarter_requests_fields_and_filter():
    client, session = make_client([page([row(1, "20221231")], 1)])
    df = pull_quarter(client, date(2022, 12, 31), pd.Timestamp.now(tz="UTC"))
    params = session.calls[0][1]
    assert params["filters"] == "REPDTE:20221231"
    assert params["fields"].split(",") == list(FINANCIAL_FIELDS)
    assert len(params["fields"].split(",")) == 45
    assert len(df) == 1


def test_duplicate_cert_in_quarter_raises():
    client, _ = make_client(
        [page([row(24735, "20221231"), row(24735, "20221231")], 2)]
    )
    with pytest.raises(IncompleteResponseError):
        pull_quarter(client, date(2022, 12, 31), pd.Timestamp.now(tz="UTC"))


def test_run_financials_writes_and_skips(tmp_path):
    touch(tmp_path, date(2022, 9, 30))
    client, _ = make_client(
        [
            page([{"REPDTE": "20230331"}], 1),
            page([row(1, "20221231")], 1),
            page([row(1, "20230331")], 1),
        ]
    )
    results = run_financials(
        tmp_path, client, start=date(2022, 9, 30), refresh_latest=2
    )
    # latest 2 (Dec, Mar) refreshed; Sep exists and is skipped
    assert [r.status for r in results] == ["skipped", "pulled", "pulled"]
    assert [r.rows for r in results][1:] == [1, 1]
    for d in (date(2022, 9, 30), date(2022, 12, 31), date(2023, 3, 31)):
        assert financials_path(tmp_path, d).exists()


def test_run_stops_on_error_keeps_written(tmp_path):
    client, _ = make_client(
        [
            page([{"REPDTE": "20221231"}], 1),
            page([row(1, "20220930")], 1),
            page([row(1, "20221231"), row(1, "20221231")], 2),
        ]
    )
    with pytest.raises(IncompleteResponseError):
        run_financials(tmp_path, client, start=date(2022, 9, 30))
    assert financials_path(tmp_path, date(2022, 9, 30)).exists()
    assert not financials_path(tmp_path, date(2022, 12, 31)).exists()


def test_pull_quarter_empty_raises_and_run_writes_nothing(tmp_path):
    client, _ = make_client([page([], 0), page([], 0)])
    with pytest.raises(IncompleteResponseError, match="0 rows"):
        pull_quarter(client, date(2022, 12, 31), pd.Timestamp.now(tz="UTC"))
    client, _ = make_client([page([{"REPDTE": "20221231"}], 1), page([], 0)])
    with pytest.raises(IncompleteResponseError):
        run_financials(tmp_path, client, start=date(2022, 12, 31), refresh_latest=1)
    assert not financials_path(tmp_path, date(2022, 12, 31)).exists()


def test_latest_report_date_empty_data_raises():
    client, _ = make_client([page([], 0)])
    with pytest.raises(FDICAPIError, match="no rows"):
        latest_report_date(client)


def test_latest_report_date_non_quarter_end_raises():
    client, _ = make_client([page([{"REPDTE": "20260715"}], 1)])
    with pytest.raises(FDICAPIError, match="quarter"):
        latest_report_date(client)
