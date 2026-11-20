"""Find a bank and the three kinds of bank page, through AppTest on fixture data."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from tests.dashboard_fixtures import write_fixture_data

APP = str(Path(__file__).resolve().parents[1] / "dashboard" / "app.py")
UNSCORED, AFTER_TEST, NO_REPORT = 9, 14, 46


@pytest.fixture(autouse=True)
def fixture_data(tmp_path, monkeypatch):
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(write_fixture_data(tmp_path)))


def _find(**params) -> AppTest:
    at = AppTest.from_file(APP, default_timeout=30)
    at.run()
    at.switch_page("views/find.py")
    for key, value in params.items():
        at.query_params[key] = value
    at.run()
    assert not at.exception, at.exception
    return at


def _text(at: AppTest) -> str:
    return "\n".join(m.value for m in at.markdown)


def test_unscored_page_text():
    text = _text(_find(cert=str(UNSCORED)))
    assert "Canary only scores banks from 2016 on; this bank stopped reporting in 2007, before that." in text
    assert "No written report" not in text


def test_scored_page_no_report_label():
    at = _find(cert=str(NO_REPORT))
    text = _text(at)
    assert "No written report for this bank" in text
    assert "Ranked **#" in text and "after the test period" not in text
    assert "Commercial real estate check" in text


def test_after_test_period_label():
    assert "after the test period" in _text(_find(cert=str(AFTER_TEST)))


def test_svb_query_opens_report_page():
    at = _find(q="SVB")
    assert at.query_params["cert"] == ["24735"] or at.query_params["cert"] == "24735"
    assert "SILICON VALLEY BANK" in _text(at)
    assert any(e.label == "Read the full report" for e in at.expander)


def test_suggestions_are_buttons_and_pick_opens_bank():
    at = _find(q="bank")
    picks = [b for b in at.button if str(b.key).startswith("pick-")]
    assert picks
    picks[0].click().run()
    assert not at.exception and "cert" in at.query_params


@pytest.mark.parametrize("cert", ["abc", "999999999"])
def test_bad_cert_param(cert):
    at = _find(cert=cert)
    assert any("No bank found" in w.value for w in at.warning)


def test_empty_search_shows_hint():
    assert "Try “SVB”" in _text(_find())
