"""Where raw Parquet files live and how they are written safely."""

import os
from datetime import date
from pathlib import Path

import pandas as pd


def financials_path(root: Path, repdte: date) -> Path:
    return root / "financials" / f"repdte={repdte:%Y%m%d}" / "part.parquet"


def failures_path(root: Path) -> Path:
    return root / "failures" / "failures.parquet"


def write_parquet_atomic(df: pd.DataFrame, path: Path) -> None:
    """Write to path + ".tmp", then rename. A crash never leaves a partial `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    try:
        df.to_parquet(tmp, index=False)
        os.replace(tmp, path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise
