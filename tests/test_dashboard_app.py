"""App shell, themes, Home and Why Canary, run through Streamlit's AppTest on fixture data."""

import re
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from canary.dashboard import data
from canary.dashboard.copy import HONEST_MISS, WHY_SECTIONS
from tests.dashboard_fixtures import REPORT_CERTS, set_metric, write_fixture_data

REPO = Path(__file__).resolve().parents[1]
APP = str(REPO / "dashboard" / "app.py")
PAGES = ["home", "find", "cases", "watchlist", "how", "why"]


@pytest.fixture
def fixture_data(tmp_path, monkeypatch):
    path = write_fixture_data(tmp_path)
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(path))
    return path


def _run(page: str = "home", theme: str | None = None) -> AppTest:
    at = AppTest.from_file(APP, default_timeout=30)
    if theme:
        at.session_state["theme"] = theme
    at.run()
    if page != "home":
        at.switch_page(f"pages/{page}.py").run()
    assert not at.exception, at.exception
    return at


def _texts(at: AppTest) -> list[str]:
    return [m.value for m in at.markdown]


def _css(at: AppTest) -> str:
    return "\n".join(t for t in _texts(at) if t.lstrip().startswith("<style>"))


def _stat_values(at: AppTest) -> list[str]:
    stats = next(t for t in _texts(at) if "FAILURES CAUGHT EARLY" in t)
    return re.findall(r'<div class="big">(.*?)</div>', stats)


def test_home_hero(fixture_data):
    at = _run()
    texts = _texts(at)
    hero = next(i for i, t in enumerate(texts) if "CANARY" in t and "Bank Failure Early-Warning System" in t)
    stats = next(i for i, t in enumerate(texts) if "FAILURES CAUGHT EARLY" in t)
    miss = next(i for i, t in enumerate(texts) if "Canary did not flag any of them in time." in t)
    assert hero < stats < miss
    assert len(_stat_values(at)) == 4


def test_home_numbers_from_metrics(fixture_data):
    set_metric(fixture_data, "banks_caught", 7)
    assert _stat_values(_run())[0] == "7 <small>of 29</small>"


def test_home_numbers_match_real_metrics(fixture_data):
    at = _run()
    assert _stat_values(at) == ["21 <small>of 29</small>", "4 <small>quarters</small>", "0.90", "98.3%"]
    stats = next(t for t in _texts(at) if "FAILURES CAUGHT EARLY" in t)
    assert "scores 0.77" in stats  # the Texas-ratio baseline's AUC
    assert any(f"{len(REPORT_CERTS)} banks have a full written report" in t for t in _texts(at))


def test_why_has_no_student_line(fixture_data):
    text = "\n".join(_texts(_run("why"))).lower()
    assert "why \"canary\"?" in text
    assert "student" not in text


def test_why_honest_answer_from_metrics(fixture_data):
    assert any("21 of the 29 banks" in t for t in _texts(_run("why")))
    set_metric(fixture_data, "banks_caught", 7)
    assert any("7 of the 29 banks" in t for t in _texts(_run("why")))


def test_fixed_copy_has_no_metric_figures():
    """The honest-answer figures are filled from metrics.json at display time, never typed into copy."""
    copy = HONEST_MISS + " ".join(body for _, body in WHY_SECTIONS)
    assert "{banks_caught} of the {eligible_banks}" in copy
    assert not re.search(r"\b(21|29)\b", copy)


@pytest.mark.parametrize("theme, present, absent", [
    ("basketball", "#b97a45", "#b4875a"),
    ("detective", "#b4875a", "#b97a45"),
])
def test_theme_css_switches(fixture_data, theme, present, absent):
    css = _css(_run(theme=theme))
    assert present in css and absent not in css


def test_standard_theme_is_default(fixture_data):
    at = _run()
    assert at.session_state["theme"] == "standard"
    css = _css(at)
    assert "#d5d7db" in css and "#b97a45" not in css and "#b4875a" not in css


def test_theme_picker_switches_theme(fixture_data):
    at = _run()
    at.button(key="theme-pick-basketball").click().run()
    assert at.session_state["theme"] == "basketball"
    # AppTest reruns a multipage app with a pages/ folder straight into the page script, so the shell's
    # CSS is not in this rerun's tree (the browser keeps it); check the CSS the new theme produces instead.
    assert "#b97a45" in _css(_run(theme=at.session_state["theme"]))


@pytest.mark.parametrize("page", PAGES)
def test_every_page_renders_with_footer(fixture_data, page):
    at = _run(page)
    assert any("Research tool, not financial advice." in t for t in _texts(at))


def test_home_search_opens_find_with_query(fixture_data):
    at = _run()
    at.text_input(key="home-q").input("svb")
    submit = next(b for b in at.button if b.label == "SEARCH")
    submit.click().run()
    assert not at.exception
    assert at.query_params["q"] == "svb"
    assert any("FIND A BANK" in t for t in _texts(at))


def test_data_loaders_read_fixture(fixture_data):
    assert data.data_dir() == fixture_data
    assert data.report_certs() == sorted(REPORT_CERTS)
    assert data.report(24735)["cert"] == 24735
    assert data.report(46) is None
    assert data.metrics()["banks_caught"] == 21
    assert len(data.threshold()) == 7
    assert set(data.cases()) == {"24735", "57053", "59017"}
    assert set(data.banks()["cert"]) == {24735, 57053, 59017, 9, 14, 46}
    assert not data.scores_history().empty and not data.concentration().empty


def test_data_dir_default(monkeypatch):
    monkeypatch.delenv("CANARY_DASHBOARD_DATA", raising=False)
    assert data.data_dir() == REPO / "dashboard" / "data"


EXPORT_ONLY = {"__main__.py", "tables.py", "cases.py", "reports.py"}


def _app_sources() -> list[Path]:
    files = list((REPO / "dashboard").rglob("*.py")) + list((REPO / "src" / "canary" / "dashboard").rglob("*.py"))
    return [f for f in files if f.name not in EXPORT_ONLY]


def test_app_never_reads_data_dir():
    offenders = [str(f) for f in _app_sources() if re.search(r"[\"']data/", f.read_text())]
    assert offenders == []


def test_only_ask_imports_anthropic():
    pattern = re.compile(r"^\s*(import anthropic|from anthropic\b)", re.M)
    files = list((REPO / "dashboard").rglob("*.py")) + list((REPO / "src" / "canary" / "dashboard").rglob("*.py"))
    importers = [f.relative_to(REPO).as_posix() for f in files if pattern.search(f.read_text())]
    assert set(importers) <= {"src/canary/dashboard/ask.py"}
