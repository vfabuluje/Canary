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
