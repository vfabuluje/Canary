"""Find a bank and the three kinds of bank page, through AppTest on fixture data."""

from pathlib import Path

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from tests.dashboard_fixtures import write_fixture_data

APP = str(Path(__file__).resolve().parents[1] / "dashboard" / "app.py")
UNSCORED, AFTER_TEST, NO_REPORT = 9, 35, 46


@pytest.fixture(autouse=True)
def fixture_data(tmp_path, monkeypatch):
    path = write_fixture_data(tmp_path)
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(path))
    return path


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


@pytest.mark.parametrize("cert", ["abc", "999999999", "²", "٣", "1" * 5000, "-46", " 46"])
def test_bad_cert_param(cert):
    """Non-ASCII digits ("²" passes str.isdigit), a 5,000-digit number and signs get the message, not a traceback."""
    at = _find(cert=cert)
    assert any("No bank found" in w.value for w in at.warning)


def test_visitors_never_see_tracebacks():
    import tomllib
    config = tomllib.loads((Path(__file__).resolve().parents[1] / ".streamlit" / "config.toml").read_text())
    assert config["client"]["showErrorDetails"] == "none"


def _rename(fixture_data, cert: int, **values) -> None:
    path = fixture_data / "banks.parquet"
    frame = pd.read_parquet(path)
    for col, value in values.items():
        frame[col] = frame[col].astype(object)
        frame.loc[frame["cert"] == cert, col] = value
    frame.to_parquet(path)


def _pick(at: AppTest, cert: int):
    return next(b for b in at.button if b.key == f"pick-{cert}")


def test_suggestion_label_escapes_markdown(fixture_data):
    _rename(fixture_data, NO_REPORT, name="E*Trade [Bank] _One_")
    _rename(fixture_data, AFTER_TEST, name="E*Trade Savings")
    label = _pick(_find(q="e trade"), NO_REPORT).label
    assert label.startswith(r"**E\*Trade \[Bank\] \_One\_**")


def test_suggestion_without_a_state_shows_no_nan(fixture_data):
    _rename(fixture_data, NO_REPORT, name="Banco De La Nacion Argentina", state=None)
    _rename(fixture_data, AFTER_TEST, name="Banco De La Nacion Uruguay")
    label = _pick(_find(q="banco de la nacion"), NO_REPORT).label
    assert "nan" not in label.lower() and "None" not in label
    assert label.endswith("]") and ":small[" in label and ":small[ ·" not in label


def test_empty_search_shows_hint():
    assert "Try “SVB”" in _text(_find())


def test_search_again_leaves_the_bank_after_a_direct_match():
    at = _find(q="SVB")
    assert "SILICON VALLEY BANK" in _text(at)
    at.button(key="find-back").click().run()
    assert not at.exception, at.exception
    assert "SILICON VALLEY BANK" not in _text(at)
    assert "cert" not in at.query_params and not at.query_params.get("q")


def test_concentration_reason_is_shown(fixture_data):
    path = fixture_data / "concentration.parquet"
    frame = pd.read_parquet(path)
    frame.loc[frame["cert"] == NO_REPORT, "reason"] = "the bank's capital was zero or negative this quarter"
    frame.loc[frame["cert"] == NO_REPORT, "lines"] = "The construction line can't be checked: capital was zero or negative.\n\n| Test | Bank |\n|---|---|\n| x | n/a |"
    frame.to_parquet(path)
    text = _text(_find(cert=str(NO_REPORT)))
    assert "can't be applied" in text and "can't be checked" in text and "0.0%" not in text


def test_full_report_dollars_are_not_maths(fixture_data):
    """Two dollar amounts in one paragraph ("$100 million to $1 billion") must not render as LaTeX."""
    import json
    path = fixture_data / "reports" / "24735.json"
    report = json.loads(path.read_text())
    report["note_md"] += "\n\nIts size band ($100 million to $1 billion) is shown for context."
    path.write_text(json.dumps(report))
    at = _find(cert="24735")
    [note] = [m.value for m in at.expander[0].markdown if "size band" in m.value]
    assert r"(\$100 million to \$1 billion)" in note
    assert "$" not in note.replace(r"\$", "")


def test_empty_page_suggests_banks_with_reports():
    at = _find()
    text = _text(at)
    assert "Or start with one of these" in text and "The 2023 collapses" in text
    starters = [b for b in at.button if str(b.key).startswith("pick-")]
    assert [str(b.key) for b in starters] == ["pick-24735", "pick-57053", "pick-59017"]
    at.button(key="pick-24735").click().run()
    assert not at.exception and at.query_params["cert"] in ("24735", ["24735"])
    assert "SILICON VALLEY BANK" in _text(at)


def test_typed_search_hides_the_starters():
    assert "Or start with one of these" not in _text(_find(q="bank"))
