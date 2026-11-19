"""Pull the FDIC CRE concentration and capital fields per bank-quarter.

Same path as the financials pull, into a separate raw table so the 45-field
files (and the specialty table) are never touched.
"""

import logging
import time
from datetime import date
from pathlib import Path

import pandas as pd

from canary.fdic_client import FDICClient, IncompleteResponseError
from canary.ingest_financials import (
    START,
    QuarterResult,
    latest_report_date,
    quarters_to_pull,
)
from canary.quarters import quarter_ends
from canary.schema import CONCENTRATION_FIELDS, to_typed_frame
from canary.storage import concentration_path, write_parquet_atomic

log = logging.getLogger("canary")


def pull_concentration_quarter(
    client: FDICClient, repdte: date, ingested_at: pd.Timestamp
) -> pd.DataFrame:
    records = client.get_all(
        "financials",
        {"filters": f"REPDTE:{repdte:%Y%m%d}", "fields": ",".join(CONCENTRATION_FIELDS)},
    )
    if not records:
        raise IncompleteResponseError(f"API returned 0 rows for quarter {repdte}")
    df = to_typed_frame(records, CONCENTRATION_FIELDS, ingested_at)
    if df["CERT"].duplicated().any():
        raise IncompleteResponseError(f"duplicate CERT in quarter {repdte}")
    return df


def run_concentration(
    root: Path,
    client: FDICClient,
    start: date = START,
    refresh_latest: int = 2,
    force: bool = False,
) -> list[QuarterResult]:
    quarters = quarter_ends(start, latest_report_date(client))
    to_pull = set(
        quarters_to_pull(quarters, root, refresh_latest, force, path_fn=concentration_path)
    )
    ingested_at = pd.Timestamp.now(tz="UTC")
    results = []
    for q in quarters:
        began = time.monotonic()
        if q in to_pull:
            df = pull_concentration_quarter(client, q, ingested_at)
            write_parquet_atomic(df, concentration_path(root, q))
            result = QuarterResult(q, "pulled", len(df), time.monotonic() - began)
            log.info("%s concentration pulled %s rows in %.1fs", q, f"{result.rows:,}", result.seconds)
        else:
            result = QuarterResult(q, "skipped", 0, 0.0)
            log.info("%s concentration skipped", q)
        results.append(result)
    return results
