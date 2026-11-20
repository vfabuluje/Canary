"""The chart builders, and the 2023 and Watchlist pages run through AppTest on fixture data."""

import html
import json
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from canary.dashboard import charts
from canary.dashboard.copy import CASE_CAPTIONS
from tests.dashboard_fixtures import REAL_DATA, write_fixture_data

REPO = Path(__file__).resolve().parents[1]
APP = str(REPO / "dashboard" / "app.py")
CASES = json.loads((REAL_DATA / "case_studies.json").read_text())
THRESHOLD = json.loads((REAL_DATA / "threshold.json").read_text())


@pytest.fixture
def fixture_data(tmp_path, monkeypatch):
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(write_fixture_data(tmp_path)))


def _run(page: str, theme: str = "basketball") -> AppTest:
    at = AppTest.from_file(APP, default_timeout=30)
    at.session_state["theme"] = theme
    at.run()
    at.switch_page(f"views/{page}.py").run()
    assert not at.exception, at.exception
    return at


def _texts(at: AppTest) -> str:
    return "\n".join(m.value for m in at.markdown)


def _y_encodings(spec) -> list[dict]:
    """Every y encoding anywhere in a Vega-Lite spec."""
    found = []
    if isinstance(spec, dict):
        if isinstance(spec.get("encoding"), dict) and "y" in spec["encoding"]:
            found.append(spec["encoding"]["y"])
        for value in spec.values():
            found += _y_encodings(value)
    elif isinstance(spec, list):
        for value in spec:
            found += _y_encodings(value)
    return found


def _all_charts():
    rows = CASES["24735"]
    return [charts.score_chart(rows, 7), charts.weak_chart(rows, 7, "Bond losses"),
            charts.threshold_chart(THRESHOLD, 2)]


def test_charts_single_axis():
    for chart in _all_charts():
        spec = chart.to_dict()
        assert '"independent"' not in json.dumps(spec)
        ys = _y_encodings(spec)
        assert ys and len({y.get("field") for y in ys}) == 1  # one y field, one scale, drawn once


def test_score_chart_rule_at_98():
    spec = charts.score_chart(CASES["24735"], 7).to_dict()
    text = json.dumps(spec)
    assert "WATCHLIST" in text and '"mark": {"type": "rule"' in text
    rule = next(layer for layer in spec["layer"] if layer["mark"]["type"] == "rule")
    data = spec["datasets"][rule["data"]["name"]]
    assert [row["pct"] for row in data] == [98.0]
    assert any(layer["mark"].get("shape") == "square" for layer in spec["layer"])
    y = next(layer["encoding"]["y"] for layer in spec["layer"] if layer["mark"]["type"] == "line")
    assert y["scale"]["domain"] == [0, 100]


def test_cases_page_default_last_quarter(fixture_data):
    at = _run("cases")
    texts = _texts(at)
    assert "#3,494" in texts and "of 4,773" in texts
    assert "SILICON VALLEY BANK" in texts and "FAILED · NOT FLAGGED" in texts
    assert html.escape(CASE_CAPTIONS[24735]["last"]) in texts
    assert at.select_slider[0].value == "Q4 2022"
    assert len(at.get("vega_lite_chart")) == 2


def test_cases_first_republic_nine_quarters(fixture_data):
    at = _run("cases")
    at.segmented_control[0].set_value(59017).run()
    assert not at.exception
    assert len(at.select_slider[0].options) == 9 == len(CASES["59017"])
    assert "#809" in _texts(at)
    at.select_slider[0].set_value(at.select_slider[0].options[0]).run()
    assert "#995" in _texts(at) and html.escape(CASE_CAPTIONS[59017]["before"]) in _texts(at)


def test_cases_signature_flagged_when_at_or_above_watchlist(fixture_data):
    at = _run("cases")
    at.segmented_control[0].set_value(57053).run()
    texts = _texts(at)
    assert "#246" in texts and "94.9" in texts and "No" in texts  # 94.9 is under the 98 line


def test_watchlist_page_published_default(fixture_data):
    at = _run("watchlist")
    texts = _texts(at)
    assert "21" in texts and "of 29" in texts and "98.3%" in texts and "3,783" in texts
    assert "None of the three 2023 collapses" in texts


def test_watchlist_ten_percent_names_signature(fixture_data):
    at = _run("watchlist")
    at.segmented_control[0].set_value(0.1).run()
    texts = _texts(at)
    assert "25" in texts and "of 29" in texts and "Signature Bank would have been caught" in texts
    assert "SVB and First Republic still would not" in texts
