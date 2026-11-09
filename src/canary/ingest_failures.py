"""Pull the FDIC failed bank list into one Parquet file."""

import logging
from pathlib import Path

import pandas as pd

from canary.fdic_client import FDICClient
from canary.schema import FAILURE_FIELDS, to_typed_frame
from canary.storage import failures_path, write_parquet_atomic

log = logging.getLogger("canary")


def run_failures(root: Path, client: FDICClient) -> int:
    """Download every failure (about 4,100 rows) and overwrite the file."""
    ingested_at = pd.Timestamp.now(tz="UTC")
    records = client.get_all("failures", {"fields": ",".join(FAILURE_FIELDS)})
    df = to_typed_frame(records, FAILURE_FIELDS, ingested_at)
    write_parquet_atomic(df, failures_path(root))
    log.info("failures pulled %s rows", f"{len(df):,}")
    return len(df)
