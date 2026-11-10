"""Upload raw FDIC Parquet files to S3: python -m canary.upload [--root data/raw].

Only ever adds or overwrites objects; it never deletes anything in S3.
"""
import argparse
import hashlib
import logging
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

from canary.config import ConfigError, load_settings

log = logging.getLogger(__name__)

KEY_PREFIX = "raw/fdic"


@dataclass
class UploadReport:
    uploaded: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)


def plan_keys(root: Path) -> list[tuple[Path, str]]:
    """Map each local *.parquet file under root to its S3 key, sorted by key."""
    pairs = [
        (path, f"{KEY_PREFIX}/{path.relative_to(root).as_posix()}")
        for path in root.rglob("*.parquet")
        if path.is_file()
    ]
    return sorted(pairs, key=lambda pair: pair[1])


def _md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_current(s3_client, bucket: str, key: str, size: int, md5: str) -> bool:
    """True if S3 already holds this exact file (same size and md5 metadata)."""
    try:
        head = s3_client.head_object(Bucket=bucket, Key=key)
    except ClientError as exc:
        if exc.response["Error"]["Code"] in ("404", "NoSuchKey", "NotFound"):
            return False
        raise
    return head["ContentLength"] == size and head.get("Metadata", {}).get("md5") == md5


def sync(root: Path, bucket: str, s3_client) -> UploadReport:
    """Upload new or changed files. The md5 is stored as object metadata because
    multipart ETags are not plain MD5s."""
    report = UploadReport()
    for path, key in plan_keys(root):
        md5 = _md5(path)
        if _is_current(s3_client, bucket, key, path.stat().st_size, md5):
            log.info("skipped %s", key)
            report.skipped.append(key)
            continue
        s3_client.upload_file(
            str(path), bucket, key, ExtraArgs={"Metadata": {"md5": md5}}
        )
        log.info("uploaded %s", key)
        report.uploaded.append(key)
    log.info(
        "done: %d uploaded, %d skipped", len(report.uploaded), len(report.skipped)
    )
    return report


EXPECTED_TOP_DIRS = {"financials", "failures"}


def check_root(root: Path) -> str | None:
    """Return an error message if root is not the raw data folder, else None."""
    root = root.resolve()
    if not root.is_dir():
        return f"upload root {root} is not a directory"
    top = {p.name for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")}
    if not top or not top <= EXPECTED_TOP_DIRS:
        return (
            f"upload root {root} must contain only the folders financials/ and/or "
            f"failures/ (found: {sorted(top) or 'none'}); pass the data/raw folder"
        )
    if not plan_keys(root):
        return f"no .parquet files found under {root}; nothing to upload"
    return None


def log_profile(profile: str) -> None:
    """Say which AWS profile is in use; warn if it is not the project's."""
    log.info("AWS profile: %s", profile)
    if profile != "canary":
        log.warning(
            "AWS profile is %r, not 'canary'. A stray AWS_PROFILE in your shell "
            "overrides .env; unset it unless this is intended.",
            profile,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.upload")
    parser.add_argument("--root", default="data/raw", help="raw data directory")
    return parser


def main(
    argv: list[str] | None = None,
    s3_client=None,
    env: Mapping[str, str] | None = None,
) -> int:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    args = build_parser().parse_args(argv)
    try:
        settings = load_settings(env)
        log_profile(settings.profile)
        problem = check_root(Path(args.root))
        if problem:
            log.error("upload failed: %s", problem)
            return 1
        if s3_client is None:
            session = boto3.Session(
                profile_name=settings.profile, region_name=settings.region
            )
            s3_client = session.client("s3")
        sync(Path(args.root).resolve(), settings.bucket, s3_client)
    except ConfigError as exc:
        log.error("upload failed: %s", exc)
        return 1
    except ClientError as exc:
        log.error("upload failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
