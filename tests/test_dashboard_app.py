"""App shell, themes, Home and Why Canary, run through Streamlit's AppTest on fixture data."""

import re
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from canary.dashboard import data
from canary.dashboard.copy import HOME_CARDS, HOME_STATS, HOME_WHAT, HONEST_MISS, WHY_SECTIONS
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
        at.switch_page(f"views/{page}.py").run()
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
    assert any("21 of the 29 banks" in t and "typically 4 quarters ahead" in t for t in _texts(_run("why")))
    set_metric(fixture_data, "banks_caught", 7)
    set_metric(fixture_data, "lead_time_median", 2.0)
    assert any("7 of the 29 banks" in t and "typically 2 quarters ahead" in t for t in _texts(_run("why")))


def test_home_lead_time_and_baseline_from_metrics(fixture_data):
    set_metric(fixture_data, "lead_time_median", 3.0)
    set_metric(fixture_data, "baseline", {"auc": 0.6})
    at = _run()
    assert _stat_values(at)[1] == "3 <small>quarters</small>"
    assert "scores 0.60" in next(t for t in _texts(at) if "FAILURES CAUGHT EARLY" in t)


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in list(value.keys()) + list(value.values()):
            yield from _strings(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from _strings(item)


def _all_fixed_copy() -> str:
    """Every string in every public constant of canary.dashboard.copy, so new copy is covered automatically."""
    from canary.dashboard import copy
    return "\n".join(t for name, v in vars(copy).items() if not name.startswith("_") and name not in CHECKED_ELSEWHERE for t in _strings(v))


# Figures in fixed copy that are history or definitions, not results the data could contradict.
FIXED_FIGURES = {"2008", "2015", "2016", "2020", "2021", "2022", "2023", "2024", "1.00", "250,000", "42", "10",
                 "1", "12", "30", "89", "4"}  # + failure dates (March 12, May 1), "#1 = riskiest", "30-89 days", "4 quarters" definitions
# FLAGSHIP_CARDS quote a bank's own figures, checked against the exported reports in test_dashboard_reports.
CHECKED_ELSEWHERE = {"FLAGSHIP_CARDS"}


def test_fixed_copy_has_no_metric_figures():
    """Results (banks caught, lead time, AUC, report count) are filled in at display time, never typed into copy."""
    copy = _all_fixed_copy()
    assert "{banks_caught} of the {eligible_banks}" in copy and "{lead_time_median:g} quarters" in copy
    assert "{baseline[auc]:.2f}" in copy and "{report_count}" in copy
    figures = set(re.findall(r"\d[\d,.]*\d|\d", re.sub(r"\{[^}]*\}", "", copy)))
    assert figures <= FIXED_FIGURES, figures - FIXED_FIGURES
    assert not re.search(r"year (ahead|before|early)|up to a year", copy, re.I)


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
    css = _css(at)
    assert "#b97a45" in css and "#b4875a" not in css


@pytest.mark.parametrize("page", PAGES)
def test_shell_stays_after_page_switch(fixture_data, page):
    """The app shell (theme CSS, 🎨 picker) runs before every page, also on reruns and page switches."""
    at = _run(page, theme="detective")
    assert "#b4875a" in _css(at)
    assert at.button(key="theme-pick-basketball")
    at.button(key="theme-pick-basketball").click().run()
    assert not at.exception
    assert "#b97a45" in _css(at)
    assert any("Research tool, not financial advice." in t for t in _texts(at))


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


def test_data_dir_from_a_site_packages_copy(tmp_path, monkeypatch):
    """A plain `pip install .` (Streamlit Community Cloud) copies the package away from the repo: the folder
    beside the source doesn't exist, so the one under the working directory (the repo root) is used."""
    copied = tmp_path / "venv" / "lib" / "python3.12" / "site-packages" / "canary" / "dashboard" / "data.py"
    copied.parent.mkdir(parents=True)
    copied.write_text("")
    repo = tmp_path / "repo"
    (repo / "dashboard" / "data").mkdir(parents=True)
    assert data.default_dir(copied, repo) == repo / "dashboard" / "data"
    monkeypatch.delenv("CANARY_DASHBOARD_DATA", raising=False)
    monkeypatch.setattr(data, "__file__", str(copied))
    monkeypatch.chdir(repo)
    assert data.data_dir() == repo / "dashboard" / "data"


def test_app_pins_the_data_folder_beside_itself(monkeypatch, tmp_path):
    """Run from anywhere with no env var set, app.py points the loaders at dashboard/data beside itself."""
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", "placeholder")  # recorded, so teardown restores the original
    monkeypatch.delenv("CANARY_DASHBOARD_DATA")
    monkeypatch.chdir(tmp_path)  # no dashboard/data under the working directory
    _run()
    assert data.data_dir() == REPO / "dashboard" / "data"


EXPORT_ONLY = {f"src/canary/dashboard/{name}" for name in ("__main__.py", "tables.py", "cases.py", "reports.py")}


def _app_sources() -> list[Path]:
    files = list((REPO / "dashboard").rglob("*.py")) + list((REPO / "src" / "canary" / "dashboard").rglob("*.py"))
    return [f for f in files if f.relative_to(REPO).as_posix() not in EXPORT_ONLY]


def test_app_sources_skip_only_export_modules():
    sources = {f.relative_to(REPO).as_posix() for f in _app_sources()}
    assert "dashboard/views/cases.py" in sources and "dashboard/app.py" in sources
    assert not sources & EXPORT_ONLY


def test_app_never_reads_data_dir():
    offenders = [str(f) for f in _app_sources() if re.search(r"[\"']data/", f.read_text())]
    assert offenders == []


def test_only_ask_imports_anthropic():
    pattern = re.compile(r"^\s*(import anthropic|from anthropic\b)", re.M)
    files = list((REPO / "dashboard").rglob("*.py")) + list((REPO / "src" / "canary" / "dashboard").rglob("*.py"))
    importers = [f.relative_to(REPO).as_posix() for f in files if pattern.search(f.read_text())]
    assert set(importers) <= {"src/canary/dashboard/ask.py"}


def test_selected_chip_css_matches_streamlit_markup(fixture_data):
    """The 2023 and Watchlist chips are navy when chosen. Streamlit 1.67 draws them as
    button[data-variant='segmented_control'] and marks the chosen one [data-selected] (checked in a browser);
    if an upgrade changes that markup, the bundle check below fails before the chip silently goes pale."""
    import streamlit
    bundle = "".join(p.read_text(errors="ignore") for p in
                     (Path(streamlit.__file__).parent / "static" / "static" / "js").glob("*.js"))
    assert "button[data-variant='segmented_control']" in bundle and "[data-selected]" in bundle
    css = _css(_run("cases"))
    chosen = 'button[data-variant="segmented_control"][data-selected]:not([data-disabled])'
    rule = re.search(re.escape(chosen) + r"\s*\{([^}]*)\}", css)
    assert rule and "background:var(--navy)" in rule.group(1) and "color:#fff" in rule.group(1)
    assert "stBaseButton-segmented_control" not in css
