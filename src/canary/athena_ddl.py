"""Create the raw Athena tables: python -m canary.athena_ddl [--latest YYYYMMDD].

Runs the hand-written SQL in warehouse/ddl/. Every statement is safe to repeat
(CREATE ... IF NOT EXISTS, ALTER ... SET TBLPROPERTIES). It never drops anything.
"""
import argparse
import logging
import time
from collections.abc import Mapping
from datetime import date, datetime
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

from canary.config import REPO_ROOT, ConfigError, Settings, load_settings
from canary.quarters import quarter_ends
from canary.upload import log_profile

log = logging.getLogger(__name__)

DDL_DIR = REPO_ROOT / "warehouse" / "ddl"
FIRST_QUARTER = date(2001, 3, 31)
POLL_SECONDS = 1.0


class AthenaError(Exception):
    """An Athena query failed or was cancelled."""


def render(sql: str, bucket: str) -> str:
    """Fill the {{bucket}} placeholder."""
    if not bucket.strip():
        raise ConfigError("bucket is blank; set CANARY_BUCKET")
    return sql.replace("{{bucket}}", bucket.strip())


def load_sql(name: str, bucket: str) -> str:
    """Read a DDL file, drop its -- comment lines (Athena DDL is sent as plain SQL), fill the bucket."""
    lines = (DDL_DIR / name).read_text().splitlines()
    return render("\n".join(l for l in lines if not l.lstrip().startswith("--")).strip(), bucket)


def statements(settings: Settings, latest: date) -> list[str]:
    """All SQL to run, in order. Partition values are listed explicitly (enum
    projection) because date-range projection found only one quarter."""
    if latest < FIRST_QUARTER:
        raise ValueError(f"latest quarter {latest} is before {FIRST_QUARTER}; nothing to project")
    values = ",".join(d.strftime("%Y%m%d") for d in quarter_ends(FIRST_QUARTER, latest))
    return [
        load_sql("fdic_financials.sql", settings.bucket),
        load_sql("fdic_failures.sql", settings.bucket),
        "ALTER TABLE canary_raw.fdic_financials SET TBLPROPERTIES "
        f"('projection.repdte.values'='{values}')",
    ]


def run(statements: list[str], athena_client, workgroup: str) -> None:
    """Run each statement and wait for it; raise AthenaError if one fails."""
    for sql in statements:
        qid = athena_client.start_query_execution(QueryString=sql, WorkGroup=workgroup)[
            "QueryExecutionId"
        ]
        while True:
            status = athena_client.get_query_execution(QueryExecutionId=qid)[
                "QueryExecution"
            ]["Status"]
            if status["State"] in ("SUCCEEDED", "FAILED", "CANCELLED"):
                break
            time.sleep(POLL_SECONDS)
        if status["State"] != "SUCCEEDED":
            reason = status.get("StateChangeReason", "no reason given")
            raise AthenaError(f"{status['State']}: {reason}\n{sql[:200]}")
        log.info("ok: %s", sql.strip().splitlines()[0][:80])


def latest_local_quarter(root: Path) -> date | None:
    folders = [p.name.removeprefix("repdte=") for p in root.glob("repdte=*") if p.is_dir()]
    return max((datetime.strptime(f, "%Y%m%d").date() for f in folders), default=None)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.athena_ddl")
    parser.add_argument("--root", default="data/raw/financials", help="local financials folder")
    parser.add_argument("--latest", help="newest quarter YYYYMMDD (default: newest folder under --root)")
    return parser


def main(
    argv: list[str] | None = None,
    athena_client=None,
    env: Mapping[str, str] | None = None,
) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        settings = load_settings(env)
        log_profile(settings.profile)
        latest = (
            datetime.strptime(args.latest, "%Y%m%d").date()
            if args.latest
            else latest_local_quarter(Path(args.root))
        )
        if latest is None:
            raise ConfigError(f"no repdte=* folders under {args.root}; pass --latest YYYYMMDD")
        if athena_client is None:
            session = boto3.Session(profile_name=settings.profile, region_name=settings.region)
            athena_client = session.client("athena")
        run(statements(settings, latest), athena_client, settings.workgroup)
    except (ConfigError, AthenaError, ClientError, ValueError) as exc:
        log.error("athena_ddl failed: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
