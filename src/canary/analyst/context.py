"""Scored context for the risk analyst: features, model scores, failures and a bank table.

Scores for every bank-quarter from 2016-03-31 on are cached so repeated runs do not
re-predict. The cache key is the model file hash plus the features file size and mtime.
"""

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd
import xgboost

from canary.model.dataset import TEST_START, load_dataset, select_features
from canary.model.metrics import flag_watchlist
from canary.replay.probe import national_rank


@dataclass
class Context:
    """Everything the analyst reads.

    Date convention: every DataFrame date column (features.report_date/failure_date,
    scored.report_date/failure_date, failures.failure_date, banks.first_report/last_report/
    failure_date) is datetime64 (pd.Timestamp, NaT when missing). Scalars such as
    latest_quarter, and API parameters such as as-of dates, are datetime.date.
    """

    features: pd.DataFrame
    scored: pd.DataFrame
    failures: pd.DataFrame
    banks: pd.DataFrame
    model: xgboost.XGBClassifier
    model_run: str
    latest_quarter: date


def score_rows(features: pd.DataFrame, model: xgboost.XGBClassifier) -> pd.DataFrame:
    """Rows from TEST_START on with score, rank, n_banks, percentile and watchlist flag.

    Each report date is ranked over every bank scored that quarter (the Phase 3 rule), and
    percentile = 100 * (1 - (rank - 1) / n_banks), as in case_studies.csv.
    """
    rows = features[pd.to_datetime(features["report_date"]) >= pd.Timestamp(TEST_START)].reset_index(drop=True)
    rows["report_date"] = pd.to_datetime(rows["report_date"])
    rows["failure_date"] = pd.to_datetime(rows["failure_date"])
    rows["score"] = model.predict_proba(select_features(rows))[:, 1]
    rows["rank"] = national_rank(rows, "score")
    rows["n_banks"] = rows.groupby("report_date")["cert"].transform("size")
    rows["percentile"] = 100.0 * (1 - (rows["rank"] - 1) / rows["n_banks"])
    rows["flagged"] = flag_watchlist(rows, "score")
    return rows


def _model_run(model_path: Path) -> str:
    return hashlib.sha256(model_path.read_bytes()).hexdigest()[:12]


def _cached_scores(features_path: Path, features: pd.DataFrame, model, run: str, cache_dir: Path) -> pd.DataFrame:
    stat = features_path.stat()
    key = {"model_run": run, "features_size": stat.st_size, "features_mtime": stat.st_mtime}
    meta_path, data_path = cache_dir / "scores.json", cache_dir / "scores.parquet"
    if meta_path.exists() and data_path.exists() and json.loads(meta_path.read_text()) == key:
        return pd.read_parquet(data_path)
    scored = score_rows(features, model)
    cache_dir.mkdir(parents=True, exist_ok=True)
    scored.to_parquet(data_path)
    meta_path.write_text(json.dumps(key))
    return scored


def _load_failures(path: Path) -> pd.DataFrame:
    raw = pd.read_parquet(path).dropna(subset=["CERT"])
    out = pd.DataFrame(
        {
            "cert": raw["CERT"].astype("int64"),
            "name": raw["NAME"],
            "city": raw["CITY"],
            "state": raw["PSTALP"],
            "failure_date": pd.to_datetime(raw["FAILDATE"]),
        }
    )
    return out.reset_index(drop=True)


def _last_states(financials_dir: Path) -> pd.Series:
    """STALP at each bank's last report, indexed by cert."""
    fin = pd.read_parquet(financials_dir, columns=["CERT", "STALP", "REPDTE"])
    fin = fin.sort_values("REPDTE", kind="mergesort").drop_duplicates("CERT", keep="last")
    return fin.set_index(fin["CERT"].astype("int64"))["STALP"]


def _build_banks(features: pd.DataFrame, failures: pd.DataFrame, financials_dir: Path) -> pd.DataFrame:
    ordered = features.sort_values("report_date", kind="mergesort")
    g = ordered.groupby("cert")
    banks = pd.DataFrame(
        {
            "name": g["institution_name"].last(),
            "first_report": g["report_date"].min(),
            "last_report": g["report_date"].max(),
            "failure_date": g["failure_date"].last(),
        }
    )
    fail = failures.drop_duplicates("cert").set_index("cert")
    banks["name"] = fail["name"].reindex(banks.index).fillna(banks["name"])
    banks["city"] = fail["city"].reindex(banks.index)
    banks["state"] = _last_states(financials_dir).reindex(banks.index)
    banks = banks.reset_index()
    return banks[["cert", "name", "state", "first_report", "last_report", "failure_date", "city"]]


def load_context(
    features: Path,
    model_dir: Path,
    failures: Path,
    financials_dir: Path = Path("data/raw/financials"),
    cache_dir: Path = Path("data/analyst"),
) -> Context:
    frame = load_dataset(features)
    frame["report_date"] = pd.to_datetime(frame["report_date"])
    frame["failure_date"] = pd.to_datetime(frame["failure_date"])
    model_path = model_dir / "model.json"
    model = xgboost.XGBClassifier()
    model.load_model(model_path)
    run = _model_run(model_path)
    scored = _cached_scores(features, frame, model, run, cache_dir)
    fails = _load_failures(failures)
    return Context(
        features=frame,
        scored=scored,
        failures=fails,
        banks=_build_banks(frame, fails, financials_dir),
        model=model,
        model_run=run,
        latest_quarter=frame["report_date"].max().date(),
    )
