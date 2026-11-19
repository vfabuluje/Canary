from datetime import date

import pandas as pd
import pytest

from canary import ingest
from canary.fdic_client import FDICClient, IncompleteResponseError
from canary.ingest_specialty import pull_specialty_quarter, run_specialty
from canary.schema import SPECIALTY_FIELDS
from canary.storage import specialty_path
from conftest import FakeSession, page


def make_client(responses):
    session = FakeSession(responses)
    return FDICClient(session=session, pause=0, sleep=lambda s: None), session


def row(cert, repdte, specgrp="9", city="SANTA CLARA"):
    return {"CERT": cert, "REPDTE": repdte, "SPECGRP": specgrp, "CITY": city}


def touch(root, d):
    p = specialty_path(root, d)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b"x")


def test_pull_quarter_requests_specialty_fields():
    client, session = make_client([page([row(1, "20221231")], 1)])
    df = pull_specialty_quarter(client, date(2022, 12, 31), pd.Timestamp.now(tz="UTC"))
    params = session.calls[0][1]
    assert params["fields"] == "CERT,REPDTE,SPECGRP,CITY"
    assert params["filters"] == "REPDTE:20221231"
    assert list(SPECIALTY_FIELDS) == ["CERT", "REPDTE", "SPECGRP", "CITY"]
    assert len(df) == 1


def test_run_writes_partitioned_parquet(tmp_path):
    client, _ = make_client(
        [page([{"REPDTE": "20221231"}], 1), page([row(24735, "20221231"), row(2, "20221231", "")], 2)]
    )
    run_specialty(tmp_path, client, start=date(2022, 12, 31))
    path = tmp_path / "specialty" / "repdte=20221231" / "part.parquet"
    assert path == specialty_path(tmp_path, date(2022, 12, 31))
    df = pd.read_parquet(path)
    assert list(df.columns) == [*SPECIALTY_FIELDS, "ingested_at"]
    assert str(df["SPECGRP"].dtype) == "Int64"
    assert df["SPECGRP"].tolist()[0] == 9 and pd.isna(df["SPECGRP"].iloc[1])
    assert df["CITY"].iloc[0] == "SANTA CLARA"


def test_skips_present_quarters_and_refreshes_latest_two(tmp_path):
    touch(tmp_path, date(2022, 9, 30))
    client, _ = make_client(
        [
            page([{"REPDTE": "20230331"}], 1),
            page([row(1, "20221231")], 1),
            page([row(1, "20230331")], 1),
        ]
    )
    results = run_specialty(tmp_path, client, start=date(2022, 9, 30), refresh_latest=2)
    assert [r.status for r in results] == ["skipped", "pulled", "pulled"]
    assert not (tmp_path / "financials").exists()


def test_force_repulls_all(tmp_path):
    for d in (date(2022, 9, 30), date(2022, 12, 31), date(2023, 3, 31)):
        touch(tmp_path, d)
    client, _ = make_client(
        [page([{"REPDTE": "20230331"}], 1)]
        + [page([row(1, q)], 1) for q in ("20220930", "20221231", "20230331")]
    )
    results = run_specialty(
        tmp_path, client, start=date(2022, 9, 30), refresh_latest=0, force=True
    )
    assert [r.status for r in results] == ["pulled"] * 3


def test_zero_rows_raises(tmp_path):
    client, _ = make_client([page([{"REPDTE": "20221231"}], 1), page([], 0)])
    with pytest.raises(IncompleteResponseError, match="0 rows"):
        run_specialty(tmp_path, client, start=date(2022, 12, 31), refresh_latest=1)
    assert not specialty_path(tmp_path, date(2022, 12, 31)).exists()


def test_duplicate_cert_raises():
    client, _ = make_client([page([row(1, "20221231"), row(1, "20221231")], 2)])
    with pytest.raises(IncompleteResponseError):
        pull_specialty_quarter(client, date(2022, 12, 31), pd.Timestamp.now(tz="UTC"))


def test_cli_specialty_subcommand(tmp_path):
    client, _ = make_client([page([{"REPDTE": "20260331"}], 1)])
    # latest_report_date succeeds, then the next call has no response -> stop early via monkey-free check
    args = ingest.build_parser().parse_args(["specialty", "--force", "--root", str(tmp_path)])
    assert args.command == "specialty" and args.force and args.root == str(tmp_path)


def test_cli_specialty_runs(tmp_path, monkeypatch):
    calls = {}

    def fake(root, client, force=False):
        calls["args"] = (root, force)

    monkeypatch.setattr(ingest, "run_specialty", fake)
    assert ingest.main(["specialty", "--force", "--root", str(tmp_path)], client=object()) == 0
    assert calls["args"] == (tmp_path, True)
