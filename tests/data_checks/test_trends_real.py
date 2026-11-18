"""Data checks on SVB's real feature rows (skipped when no local data)."""
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from canary.analyst.trends import compute_trends

FEATURES = Path(__file__).resolve().parents[2] / "data" / "features" / "fct_bank_features.parquet"
SVB_CERT = 24735
HTM = "htm_unrealized_loss_to_equity"

pytestmark = [
    pytest.mark.data,
    pytest.mark.skipif(not FEATURES.exists(), reason="no local data"),
]


@pytest.fixture(scope="module")
def svb():
    df = pd.read_parquet(FEATURES)
    df = df[df["cert"] == SVB_CERT].copy()
    df["report_date"] = pd.to_datetime(df["report_date"])
    return df


def test_svb_2022q1_htm_outside(svb):
    r = compute_trends(svb, date(2022, 3, 31), {})
    t = next(x for x in r.outside if x.feature == HTM)
    assert t.value == pytest.approx(0.4836, abs=1e-3)
    assert t.lo == pytest.approx(-0.1172, abs=1e-3)
    assert t.hi == pytest.approx(0.0659, abs=1e-3)
    assert t.change_1q_pp == pytest.approx(41.8, abs=0.1)
    assert t.change_4q_pp == pytest.approx(48.6, abs=0.1)


def test_svb_2022q4_htm_inside(svb):
    """Pins the known consequence in spec section 1: by 2022-12-31 the loss
    (about 0.9808) sits inside the widened range (about -0.1172..1.0526).
    Do not change the range rule to make this pass differently."""
    r = compute_trends(svb, date(2022, 12, 31), {})
    assert HTM not in [x.feature for x in r.outside]
