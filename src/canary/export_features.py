"""Export the feature table from Athena to a local Parquet file.

python -m canary.export_features [--out data/features/fct_bank_features.parquet]

Athena UNLOAD writes Parquet parts under athena-results/exports/<run_id>/ (a
prefix that auto-expires after 7 days and that canary-dev may delete). We
download the parts, join them and write one local file. See decision 0012.
"""
import argparse
import io
import logging
import os
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path

import boto3
import pandas as pd
from botocore.exceptions import ClientError

from canary.athena_ddl import AthenaError, run
from canary.config import ConfigError, Settings, load_settings
from canary.upload import log_profile

log = logging.getLogger(__name__)

DEFAULT_OUT = "data/features/fct_bank_features.parquet"


def export_sql(bucket: str, run_id: str) -> str:
    return (
        "UNLOAD (SELECT f.*, q.quarters_until_failure, q.failure_date, q.institution_name "
        "FROM canary_marts.fct_bank_features f "
        "JOIN canary_marts.fct_bank_quarters q "
        "ON f.cert = q.cert AND f.report_date = q.report_date) "
        f"TO 's3://{bucket}/athena-results/exports/{run_id}/' "
        "WITH (format = 'PARQUET', compression = 'SNAPPY')"
    )


def export(settings: Settings, athena_client, s3_client, out_path: Path, run_id: str) -> int:
    """Run the UNLOAD, download the parts, write out_path atomically. Returns row count."""
    run([export_sql(settings.bucket, run_id)], athena_client, settings.workgroup)
    prefix = f"athena-results/exports/{run_id}/"
    keys = []
    for page in s3_client.get_paginator("list_objects_v2").paginate(
        Bucket=settings.bucket, Prefix=prefix
    ):
        keys += [o["Key"] for o in page.get("Contents", []) if not o["Key"].endswith("/")]
    if not keys:
        raise RuntimeError(f"no files under s3://{settings.bucket}/{prefix}")
    frames = []
    for key in sorted(keys):
        body = s3_client.get_object(Bucket=settings.bucket, Key=key)["Body"].read()
        frames.append(pd.read_parquet(io.BytesIO(body)))
    df = pd.concat(frames, ignore_index=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_name(out_path.name + ".tmp")
    try:
        df.to_parquet(tmp, index=False)
        os.replace(tmp, out_path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise
    return len(df)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.export_features")
    parser.add_argument("--out", default=DEFAULT_OUT, help="local Parquet file to write")
    return parser


def main(
    argv: list[str] | None = None,
    athena_client=None,
    s3_client=None,
    env: Mapping[str, str] | None = None,
) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        settings = load_settings(env)
        log_profile(settings.profile)
        if athena_client is None or s3_client is None:
            session = boto3.Session(profile_name=settings.profile, region_name=settings.region)
            athena_client = athena_client or session.client("athena")
            s3_client = s3_client or session.client("s3")
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        rows = export(settings, athena_client, s3_client, Path(args.out), run_id)
        log.info("wrote %d rows to %s", rows, args.out)
    except (ConfigError, AthenaError, ClientError, RuntimeError) as exc:
        log.error("export_features failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
