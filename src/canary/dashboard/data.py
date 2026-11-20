"""Cached loaders for the exported dashboard files. The app reads only this folder, never the pipeline's data."""

import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_ENV = "CANARY_DASHBOARD_DATA"


def data_dir() -> Path:
    """The exported folder: env CANARY_DASHBOARD_DATA if set (tests), else <repo>/dashboard/data."""
    override = os.environ.get(DATA_ENV)
    return Path(override) if override else Path(__file__).resolve().parents[3] / "dashboard" / "data"


# The cached readers take the file's path and modification time, so a different folder or a re-export
# is read afresh instead of served from a stale cache entry.
@st.cache_data(show_spinner=False)
def _read_parquet(path: str, mtime: float) -> pd.DataFrame:
    return pd.read_parquet(path)


@st.cache_data(show_spinner=False)
def _read_json(path: str, mtime: float):
    return json.loads(Path(path).read_text())


def _parquet(name: str) -> pd.DataFrame:
    path = data_dir() / name
    return _read_parquet(str(path), path.stat().st_mtime)


def _json(path: Path):
    return _read_json(str(path), path.stat().st_mtime)


def banks() -> pd.DataFrame:
    return _parquet("banks.parquet")


def scores_history() -> pd.DataFrame:
    return _parquet("scores_history.parquet")


def concentration() -> pd.DataFrame:
    return _parquet("concentration.parquet")


def metrics() -> dict:
    return _json(data_dir() / "metrics.json")


def threshold() -> list[dict]:
    return _json(data_dir() / "threshold.json")


def cases() -> dict:
    """The three 2023 case studies, keyed by cert as a string (as exported)."""
    return _json(data_dir() / "case_studies.json")


def report(cert: int) -> dict | None:
    """A showcase bank's report page content, or None if the bank has no written report."""
    path = data_dir() / "reports" / f"{int(cert)}.json"
    return _json(path) if path.is_file() else None


def report_certs() -> list[int]:
    return sorted(int(p.stem) for p in (data_dir() / "reports").glob("*.json"))
