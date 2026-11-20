"""The report replay (spec 5.5) and the How it works page (5.5a)."""

import copy
import json
import re
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from canary.dashboard.replay import replay_html, scenes
from tests.dashboard_fixtures import REAL_DATA, write_fixture_data

APP = str(Path(__file__).resolve().parents[1] / "dashboard" / "app.py")
SVB, COMENITY = 24735, 57570


def _report(cert: int) -> dict:
    return json.loads((REAL_DATA / "reports" / f"{cert}.json").read_text())


def _payload(page: str) -> dict:
    m = re.search(r"window\.CANARY = (\{.*?\});\n", page, re.S)
    assert m, "no CANARY payload"
    return json.loads(m.group(1))


@pytest.fixture
def svb() -> dict:
    return _report(SVB)


# ------------------------------------------------------------------------------------------- the engine
def test_replay_html_scales_and_stacks(svb):
    page = replay_html(svb, "standard")
    assert re.search(r"addEventListener\(\s*['\"]resize['\"]", page), "no resize handler"
    assert "scale(" in page and "640" in page  # the 640 x 300 stage is scaled to the container width
    stack = re.search(r"@media \(max-width:700px\)\s*\{[^}]*\.stagewrap\s*\{[^}]*grid-template-columns:1fr", page)
    assert stack, "the side panel does not stack under the scene below 700px"


def test_tips_open_on_tap(svb):
    page = replay_html(svb, "detective")
    assert re.search(r"addEventListener\(\s*['\"]mouseover['\"]", page)
    assert re.search(r"addEventListener\(\s*['\"]click['\"]", page)
    assert "data-tip" in page or "dataset.tip" in page


def test_six_scenes_in_order(svb):
    got = scenes(svb)
    assert [s["key"] for s in got] == ["numbers", "rule", "specialists", "check", "lead", "done"]
    for s in got:
        assert {"key", "now", "who", "active", "note"} <= set(s)
        assert set(s["who"]) == {"detective", "basketball"}
    assert got[0]["active"] == []
    assert got[2]["active"] == ["trend", "peer"]
    assert got[4]["active"] == ["lead", "check"]  # the lead writes, then the fact checker checks, same scene


def test_peer_benched_when_no_peer():
    comenity = _report(COMENITY)
    assert comenity["agents"]["peer"]["ran"] is False
    got = scenes(comenity)
    assert got[2]["active"] == ["trend"]
    assert "not enough similar banks to compare" in got[2]["note"]
    assert "peer" not in got[5]["active"]
    assert all(s["note"] is None or "sent back" not in s["note"] for s in got)
    assert _payload(replay_html(comenity, "basketball"))["bench"] is True


def test_retry_notes_only_when_retried(svb):
    first_try = scenes(svb)
    assert all(s["note"] is None for s in first_try)
    assert "Nothing had to be redone" in first_try[5]["who"]["detective"]

    lead_retry = copy.deepcopy(svb)
    lead_retry["agents"]["analyst"] = {"ran": True, "attempts": 2, "first_try": False}
    got = scenes(lead_retry)
    assert got[3]["note"] is None
    assert "sent back once, fixed" in got[4]["note"]
    assert "Nothing had to be redone" not in got[5]["who"]["detective"]

    peer_retry = copy.deepcopy(svb)
    peer_retry["agents"]["peer"] = {"ran": True, "attempts": 2, "first_try": False}
    got = scenes(peer_retry)
    assert "Peer" in got[3]["note"] and "sent back once, fixed" in got[3]["note"] and "Trend" not in got[3]["note"]
    assert got[4]["note"] is None


def test_retry_notes_match_real_traces():
    """Republic Bank (27332): the summary needed attempt 2; First Nb Of America (17438): trend did."""
    got = scenes(_report(27332))
    assert got[3]["note"] is None and "sent back once, fixed" in got[4]["note"]
    got = scenes(_report(17438))
    assert "Trend" in got[3]["note"] and got[4]["note"] is None


def test_html_has_no_svb_literal_for_other_bank():
    other = _report(COMENITY)
    other.update(cert=91, name="Fixture Bank Of Ohio")
    page = replay_html(other, "detective")
    assert "Fixture Bank Of Ohio" in page
    assert "Silicon Valley" not in page and "SVB" not in page
    payload = _payload(page)
    assert payload["report"]["rank"]["numbers"][0]["text"] == f"{other['rank']:,}th"


def test_standard_theme_uses_detectives(svb):
    standard, detective, basketball = (_payload(replay_html(svb, t)) for t in ("standard", "detective", "basketball"))
    assert standard["cast"] == detective["cast"] == "detective"
    assert basketball["cast"] == "basketball"
    assert standard["team"]["trend"]["name"] == "Trend Detective"
    assert basketball["team"]["lead"]["name"] == "Captain #23"
    page = replay_html(svb, "standard")
    assert '<body class="t-standard">' in page and "#d5d7db" in page
    assert '<body class="t-basketball">' in replay_html(svb, "basketball")


def test_figures_come_from_the_report(svb):
    p = _payload(replay_html(svb, "standard"))
    assert p["name"] == "Silicon Valley Bank"
    assert p["papers"][0] == "RANK 3,494"
    assert p["stamp"]["kind"] == "ok" and any("13.7%" in line for line in p["stamp"]["lines"])
    assert "8.4%" in p["checks"]["specialists"] and "98.1%" in p["checks"]["summary"]
    assert "Silicon Valley Bank failed on March 10, 2023." in p["report"]["after"]
    assert [c["member"] for c in p["report"]["cards"]] == ["trend", "peer", "rule", "lead"]


def test_rule_stamp_follows_the_rule_card():
    crossed = _report(25796)  # crossed both lines
    assert _payload(replay_html(crossed, "standard"))["stamp"]["kind"] == "warn"
    cant = _report(17719)  # capital zero or negative: the rule can't be applied
    stamp = _payload(replay_html(cant, "standard"))["stamp"]
    assert stamp["kind"] == "cant" and all("%" not in line for line in stamp["lines"])


def test_payload_cannot_close_the_script_tag(svb):
    svb = copy.deepcopy(svb)
    svb["name"] = "</script><script>alert(1)</script>"
    page = replay_html(svb, "standard")
    assert "</script><script>alert(1)" not in page


# ------------------------------------------------------------------------------------------ the pages
@pytest.fixture
def fixture_data(tmp_path, monkeypatch):
    path = write_fixture_data(tmp_path)
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(path))
    return path


def _page(page: str, theme: str | None = None, **params) -> AppTest:
    at = AppTest.from_file(APP, default_timeout=30)
    if theme:
        at.session_state["theme"] = theme
    at.run()
    at.switch_page(f"views/{page}.py")
    for key, value in params.items():
        at.query_params[key] = value
    at.run()
    assert not at.exception, at.exception
    return at


def _replays(at: AppTest) -> list[dict]:
    return [_payload(e.proto.srcdoc) for e in at.get("iframe")]


def test_how_defaults_to_svb_and_shows_the_strip(fixture_data):
    at = _page("how")
    assert at.selectbox(key="how-bank").value == SVB
    (replay,) = _replays(at)
    assert replay["name"] == "Silicon Valley Bank"
    text = "\n".join(m.value for m in at.markdown)
    steps = re.findall(r'<span class="mark (ai|code)">', text)
    assert steps == ["code", "code", "ai", "code"]


def test_how_picker_changes_the_replay(fixture_data):
    at = _page("how")
    at.selectbox(key="how-bank").select(57053).run()
    assert not at.exception
    assert _replays(at)[0]["name"] == "Signature Bank"


def test_how_replay_follows_the_theme(fixture_data):
    assert _replays(_page("how", theme="basketball"))[0]["cast"] == "basketball"


def test_bank_page_shows_the_replay(fixture_data):
    at = _page("find", cert=str(SVB))
    (replay,) = _replays(at)
    assert replay["name"] == "Silicon Valley Bank"
    assert any(e.label == "Read the full report" for e in at.expander)
