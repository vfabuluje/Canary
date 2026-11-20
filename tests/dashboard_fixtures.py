"""A tiny but real `dashboard/data` folder for app tests, sliced from the committed export.

Every value comes from the real export, so tests that check figures against it keep holding:
the three case studies as exported, the seven watchlist sizes, the headline metrics, and these banks:
SVB, Signature and First Republic (written reports), Union Trust (stopped reporting in 2007, never
scored), Auburnbank (latest score after the test period) and Merchants Bank of Alabama (scored,
no written report).
"""

import json
import shutil
from pathlib import Path

import pandas as pd

REAL_DATA = Path(__file__).resolve().parents[1] / "dashboard" / "data"
FIXTURE_CERTS = [24735, 57053, 59017, 9, 35, 46]
REPORT_CERTS = [24735, 57053, 59017]


def write_fixture_data(root: Path) -> Path:
    """Write the fixture folder under `root` and return its path (point CANARY_DASHBOARD_DATA at it)."""
    out = Path(root) / "dashboard-data"
    (out / "reports").mkdir(parents=True, exist_ok=True)
    for name in ("banks", "scores_history", "concentration"):
        frame = pd.read_parquet(REAL_DATA / f"{name}.parquet")
        frame[frame["cert"].isin(FIXTURE_CERTS)].reset_index(drop=True).to_parquet(out / f"{name}.parquet")
    for name in ("metrics.json", "threshold.json", "case_studies.json"):
        shutil.copyfile(REAL_DATA / name, out / name)
    for cert in REPORT_CERTS:
        shutil.copyfile(REAL_DATA / "reports" / f"{cert}.json", out / "reports" / f"{cert}.json")
    return out


def set_metric(data: Path, key: str, value) -> None:
    """Change one headline figure in the fixture's metrics.json."""
    path = data / "metrics.json"
    metrics = json.loads(path.read_text())
    metrics[key] = value
    path.write_text(json.dumps(metrics))
