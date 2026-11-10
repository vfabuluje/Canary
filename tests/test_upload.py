import hashlib
from pathlib import Path

import boto3
import pytest
from moto import mock_aws

from canary.upload import main, plan_keys, sync

BUCKET = "canary-test-bucket"


def md5_of(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


@pytest.fixture
def raw_root(tmp_path: Path) -> Path:
    root = tmp_path / "raw"
    for repdte in ("20221231", "20230331"):
        part = root / "financials" / f"repdte={repdte}" / "part.parquet"
        part.parent.mkdir(parents=True)
        part.write_bytes(b"quarter " + repdte.encode())
    failures = root / "failures" / "failures.parquet"
    failures.parent.mkdir(parents=True)
    failures.write_bytes(b"failures")
    return root


@pytest.fixture
def s3():
    with mock_aws():
        client = boto3.client("s3", region_name="us-east-1")
        client.create_bucket(Bucket=BUCKET)
        yield client


def test_plan_keys_maps_paths(raw_root):
    keys = [key for _, key in plan_keys(raw_root)]
    assert keys == [
        "raw/fdic/failures/failures.parquet",
        "raw/fdic/financials/repdte=20221231/part.parquet",
        "raw/fdic/financials/repdte=20230331/part.parquet",
    ]


def test_skips_non_parquet_and_tmp(raw_root):
    (raw_root / ".DS_Store").write_bytes(b"x")
    (raw_root / "financials" / "repdte=20221231" / "part.parquet.tmp").write_bytes(b"x")
    keys = [key for _, key in plan_keys(raw_root)]
    assert len(keys) == 3
    assert not any(k.endswith((".DS_Store", ".tmp")) for k in keys)


def test_first_run_uploads_all(raw_root, s3):
    report = sync(raw_root, BUCKET, s3)
    assert len(report.uploaded) == 3 and report.skipped == []
    for path, key in plan_keys(raw_root):
        head = s3.head_object(Bucket=BUCKET, Key=key)
        assert head["Metadata"]["md5"] == md5_of(path)


def test_second_run_uploads_nothing(raw_root, s3):
    sync(raw_root, BUCKET, s3)
    report = sync(raw_root, BUCKET, s3)
    assert report.uploaded == [] and len(report.skipped) == 3


def test_changed_file_reuploaded(raw_root, s3):
    sync(raw_root, BUCKET, s3)
    changed = raw_root / "financials" / "repdte=20230331" / "part.parquet"
    changed.write_bytes(b"different content")
    report = sync(raw_root, BUCKET, s3)
    assert report.uploaded == ["raw/fdic/financials/repdte=20230331/part.parquet"]
    assert len(report.skipped) == 2


def test_new_quarter_uploads_one_file(raw_root, s3):
    sync(raw_root, BUCKET, s3)
    part = raw_root / "financials" / "repdte=20230630" / "part.parquet"
    part.parent.mkdir(parents=True)
    part.write_bytes(b"new quarter")
    report = sync(raw_root, BUCKET, s3)
    assert report.uploaded == ["raw/fdic/financials/repdte=20230630/part.parquet"]
    assert len(report.skipped) == 3


def test_compares_md5_metadata_not_etag(raw_root, s3):
    path = raw_root / "failures" / "failures.parquet"
    key = "raw/fdic/failures/failures.parquet"
    size = path.stat().st_size
    # Same size, different md5 metadata -> must upload.
    s3.put_object(Bucket=BUCKET, Key=key, Body=b"x" * size, Metadata={"md5": "0" * 32})
    assert key in sync(raw_root, BUCKET, s3).uploaded
    # Matching md5 metadata but an ETag that is not the file's MD5 -> must skip.
    s3.put_object(Bucket=BUCKET, Key=key, Body=b"y" * size, Metadata={"md5": md5_of(path)})
    assert key in sync(raw_root, BUCKET, s3).skipped


def test_never_deletes(raw_root, s3):
    s3.put_object(Bucket=BUCKET, Key="raw/fdic/financials/repdte=19990331/part.parquet", Body=b"old")
    sync(raw_root, BUCKET, s3)
    keys = {o["Key"] for o in s3.list_objects_v2(Bucket=BUCKET)["Contents"]}
    assert "raw/fdic/financials/repdte=19990331/part.parquet" in keys


def test_missing_bucket_env_fails(raw_root):
    assert main(["--root", str(raw_root)], env={}) == 1


def test_empty_root_fails(tmp_path, caplog):
    root = tmp_path / "empty"
    (root / "financials").mkdir(parents=True)
    assert main(["--root", str(root)], env={"CANARY_BUCKET": BUCKET}, s3_client=object()) == 1
    assert str(root.resolve()) in caplog.text


def test_wrong_root_fails(raw_root, caplog):
    # data/raw/financials would put keys outside the table LOCATION
    root = raw_root / "financials"
    assert main(["--root", str(root)], env={"CANARY_BUCKET": BUCKET}, s3_client=object()) == 1
    assert "financials/" in caplog.text


def test_missing_root_fails(tmp_path):
    missing = tmp_path / "nope"
    assert main(["--root", str(missing)], env={"CANARY_BUCKET": BUCKET}, s3_client=object()) == 1


def test_warns_when_profile_is_not_canary(raw_root, s3, caplog):
    env = {"CANARY_BUCKET": BUCKET, "AWS_PROFILE": "other"}
    assert main(["--root", str(raw_root)], env=env, s3_client=s3) == 0
    assert any(r.levelname == "WARNING" and "other" in r.getMessage() for r in caplog.records)


def test_no_warning_for_canary_profile(raw_root, s3, caplog):
    assert main(["--root", str(raw_root)], env={"CANARY_BUCKET": BUCKET}, s3_client=s3) == 0
    assert not any(r.levelname == "WARNING" for r in caplog.records)
