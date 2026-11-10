"""Pull FDIC quarterly financials into one Parquet file per quarter."""

import logging
import time
from datetime import date, datetime
from pathlib import Path
from typing import NamedTuple

import pandas as pd

from canary.fdic_client import FDICAPIError, FDICClient, IncompleteResponseError
from canary.quarters import quarter_ends
from canary.schema import FINANCIAL_FIELDS, to_typed_frame
from canary.storage import financials_path, write_parquet_atomic

START = date(2001, 3, 31)
log = logging.getLogger("canary")


class QuarterResult(NamedTuple):
    repdte: date
    status: str  # "pulled" or "skipped"
    rows: int
    seconds: float


def latest_report_date(client: FDICClient) -> date:
    payload = client.get_page(
        "financials",
        {"fields": "REPDTE", "sort_by": "REPDTE", "sort_order": "DESC", "limit": 1},
    )
    if not payload["data"]:
        raise FDICAPIError("API returned no rows when asked for the latest REPDTE")
    raw = payload["data"][0]["data"]["REPDTE"]
    try:
        latest = datetime.strptime(raw, "%Y%m%d").date()
        quarter_ends(latest, latest)  # raises ValueError unless it is a quarter-end
    except ValueError as exc:
        raise FDICAPIError(f"Latest REPDTE {raw!r} is not a quarter-end date") from exc
    return latest


def quarters_to_pull(
    quarters: list[date], root: Path, refresh_latest: int = 2, force: bool = False
) -> list[date]:
    """Missing quarters plus the latest `refresh_latest`; all of them if `force`.

    Only a finished part.parquet counts as present, so a leftover
    part.parquet.tmp from a crash is treated as missing.
    """
    if force:
        return list(quarters)
    wanted = {q for q in quarters if not financials_path(root, q).exists()}
    if refresh_latest > 0:
        wanted.update(quarters[-refresh_latest:])
    return sorted(wanted)


def pull_quarter(
    client: FDICClient, repdte: date, ingested_at: pd.Timestamp
) -> pd.DataFrame:
    records = client.get_all(
        "financials",
        {"filters": f"REPDTE:{repdte:%Y%m%d}", "fields": ",".join(FINANCIAL_FIELDS)},
    )
    if not records:
        raise IncompleteResponseError(f"API returned 0 rows for quarter {repdte}")
    df = to_typed_frame(records, FINANCIAL_FIELDS, ingested_at)
    if df["CERT"].duplicated().any():
        raise IncompleteResponseError(f"duplicate CERT in quarter {repdte}")
    return df


def run_financials(
    root: Path,
    client: FDICClient,
    start: date = START,
    refresh_latest: int = 2,
    force: bool = False,
) -> list[QuarterResult]:
    quarters = quarter_ends(start, latest_report_date(client))
    to_pull = set(quarters_to_pull(quarters, root, refresh_latest, force))
    ingested_at = pd.Timestamp.now(tz="UTC")
    results = []
    for q in quarters:
        began = time.monotonic()
        if q in to_pull:
            df = pull_quarter(client, q, ingested_at)
            write_parquet_atomic(df, financials_path(root, q))
            result = QuarterResult(q, "pulled", len(df), time.monotonic() - began)
            log.info("%s pulled %s rows in %.1fs", q, f"{result.rows:,}", result.seconds)
        else:
            result = QuarterResult(q, "skipped", 0, 0.0)
            log.info("%s skipped", q)
        results.append(result)
    return results
