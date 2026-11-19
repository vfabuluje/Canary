from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.model import train as train_mod
from canary.model.dataset import FEATURE_COLUMNS, assign_split, fails_within_4q
from canary.model.train import CASE_STUDY_CERTS

STRONG = "noncurrent_loans_to_loans"


class FakeResponse:
    def __init__(self, status_code, payload=None, text=""):
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def json(self):
        if self._payload is None:
            raise ValueError("no JSON body")
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.headers = {}

    def get(self, url, params=None, timeout=None):
        self.calls.append((url, dict(params) if params else params))
        item = self.responses.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item


def page(rows, total):
    return FakeResponse(
        200, {"meta": {"total": total}, "data": [{"data": r} for r in rows]}
    )


def _quarters(first_year=2001, last_year=2026):
    return [
        date(y, m, d)
        for y in range(first_year, last_year + 1)
        for m, d in ((3, 31), (6, 30), (9, 30), (12, 31))
    ]


@pytest.fixture
def small_grid(monkeypatch):
    """Keep model tests fast: two combos, few trees. Not autouse; opt in per module."""
    monkeypatch.setattr(
        train_mod,
        "GRID",
        [
            {"max_depth": 2, "learning_rate": 0.3, "min_child_weight": 1},
            {"max_depth": 3, "learning_rate": 0.3, "min_child_weight": 1},
        ],
    )
    monkeypatch.setattr(train_mod, "MAX_TREES", 30)
    monkeypatch.setattr(train_mod, "EARLY_STOPPING_ROUNDS", 5)


@pytest.fixture(scope="module")
def raw() -> pd.DataFrame:
    """40 banks x 2001-2026. Failures (cert: failure quarter): train 2008Q3, 2013Q2;
    test 2019Q4, and the three 2023 case-study banks. Failed banks stop reporting."""
    rng = np.random.default_rng(0)
    quarters = _quarters()
    fail_q = {
        1: date(2008, 9, 30),
        2: date(2013, 6, 30),
        3: date(2019, 12, 31),
        24735: date(2023, 3, 31),
        57053: date(2023, 3, 31),
        59017: date(2023, 6, 30),
    }
    certs = list(fail_q) + list(range(100, 134))
    rows = []
    for cert in certs:
        fq = fail_q.get(cert)
        for i, q in enumerate(quarters):
            if fq is not None and q >= fq:
                break
            qtf = None
            if fq is not None:
                qtf = quarters.index(fq) - i
            row = {c: rng.normal() for c in FEATURE_COLUMNS}
            row[STRONG] = rng.normal() + (6.0 if qtf is not None and qtf <= 4 else 0.0)
            if rng.random() < 0.1:
                row["texas_ratio"] = np.nan
            row.update(
                cert=cert,
                institution_name=CASE_STUDY_CERTS.get(cert, f"Bank {cert}"),
                report_date=q,
                quarters_until_failure=qtf,
                failure_date=fq,
            )
            rows.append(row)
    return pd.DataFrame(rows)


@pytest.fixture
def df(raw) -> pd.DataFrame:
    out = raw.copy()
    out["label"] = fails_within_4q(out["quarters_until_failure"])
    out["split"] = assign_split(out["report_date"])
    return out


@pytest.fixture
def features_path(raw, tmp_path):
    path = tmp_path / "features.parquet"
    raw.to_parquet(path)
    return path


@pytest.fixture(scope="module")
def trained_model(raw):
    """Small-grid fitted model on `raw` (same training as tests/test_replay_probe.py::model)."""
    from canary.model.dataset import assign_split as _split, fails_within_4q as _label

    frame = raw.copy()
    rng = np.random.default_rng(1)
    n = len(frame)
    frame["htm_unrealized_loss_to_equity"] = rng.uniform(0, 1, n)
    frame["afs_unrealized_loss_to_equity"] = rng.uniform(0, 0.5, n)
    frame["uninsured_to_deposits"] = rng.uniform(0, 1, n)
    frame["label"] = _label(frame["quarters_until_failure"])
    frame["split"] = _split(frame["report_date"])
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(train_mod, "GRID", [{"max_depth": 2, "learning_rate": 0.3, "min_child_weight": 1}])
        mp.setattr(train_mod, "MAX_TREES", 30)
        mp.setattr(train_mod, "EARLY_STOPPING_ROUNDS", 5)
        fitted, _ = train_mod.train(frame)
    return fitted


@pytest.fixture
def failures_path(raw, tmp_path):
    certs = [3, 24735, 57053, 59017]
    rows = []
    for cert in certs:
        sub = raw[raw["cert"] == cert].iloc[0]
        rows.append(
            {
                "CERT": cert,
                "NAME": f"FAILED BANK {cert}",
                "CITY": f"City{cert}",
                "PSTALP": "CA",
                "FAILDATE": sub["failure_date"].isoformat(),
            }
        )
    path = tmp_path / "failures.parquet"
    pd.DataFrame(rows).to_parquet(path)
    return path


@pytest.fixture
def financials_dir(raw, tmp_path):
    out = tmp_path / "financials"
    last_two = sorted(raw["report_date"].unique())[-2:]
    for q in last_two:
        part = out / f"repdte={q.strftime('%Y%m%d')}"
        part.mkdir(parents=True)
        certs = raw.loc[raw["report_date"] == q, "cert"]
        pd.DataFrame({"CERT": certs.to_numpy(), "STALP": "PA", "REPDTE": q.isoformat()}).to_parquet(
            part / "part.parquet"
        )
    return out


def _specgrp(cert: int) -> int:
    if cert in (24735, 120, 121, 122, 123, 124, 125, 126, 127):
        return 9
    if cert == 57053 or 100 <= cert <= 119:
        return 4
    if cert == 59017:
        return 6
    if 128 <= cert <= 133:
        return 3
    return 8  # certs 1-3


@pytest.fixture
def specialty_dir(raw, tmp_path):
    out = tmp_path / "specialty"
    for q in sorted(raw["report_date"].unique()):
        part = out / f"repdte={q.strftime('%Y%m%d')}"
        part.mkdir(parents=True)
        certs = raw.loc[raw["report_date"] == q, "cert"].to_numpy()
        pd.DataFrame(
            {
                "CERT": certs,
                "REPDTE": q.isoformat(),
                "SPECGRP": pd.array([_specgrp(int(c)) for c in certs], dtype="Int64"),
                "CITY": ["SANTA CLARA" if c == 24735 else f"City {c}" for c in certs],
            }
        ).to_parquet(part / "part.parquet")
    return out


@pytest.fixture
def concentration_dir(raw, tmp_path):
    """Cert 100 crosses the construction line, 101 has no rows, everyone else crosses neither."""
    out = tmp_path / "concentration"
    for q in sorted(raw["report_date"].unique()):
        part = out / f"repdte={q.strftime('%Y%m%d')}"
        part.mkdir(parents=True)
        certs = [int(c) for c in raw.loc[raw["report_date"] == q, "cert"] if c != 101]
        big = np.array([c == 100 for c in certs])
        pd.DataFrame(
            {
                "CERT": certs,
                "REPDTE": q.isoformat(),
                "LNRECONS": np.where(big, 150.0, 10.0),
                "LNREMULT": 10.0,
                "LNRENROT": 10.0,
                "LNCOMRE": 10.0,
                "RBC": 100.0,
                "RBCT1J": np.where(big, 100.0, 90.0),
                "LNATRES": np.where(big, 0.0, 10.0),
            }
        ).to_parquet(part / "part.parquet")
    return out


@pytest.fixture
def analyst_ctx(raw, trained_model, failures_path, financials_dir, specialty_dir, concentration_dir, tmp_path):
    from canary.analyst.context import load_context

    features = tmp_path / "features.parquet"
    raw.to_parquet(features)
    model_dir = tmp_path / "model"
    model_dir.mkdir()
    trained_model.save_model(model_dir / "model.json")
    return load_context(features, model_dir, failures_path, financials_dir, tmp_path / "cache", specialty_dir,
                        concentration_dir)
