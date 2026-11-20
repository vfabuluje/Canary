from analyst_fakes import FakeClient, split_memo
from canary.analyst import concentration as conc
from canary.analyst import sections
from canary.analyst.facts import build_fact_sheet
from canary.analyst.writer import build_request, write_memo
from test_analyst_writer import _memo

TITLE = "Real-estate concentration (2006 regulator thresholds)"


def _sheet(ctx, tmp_path, cert=3):
    return build_fact_sheet(ctx, cert, replay_dir=tmp_path / "none")


def test_section_last_after_peers(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    keys = [s.key for s in sections.sections_for(sheet)]
    i = keys.index("concentration")
    assert keys[i - 2:i] == ["trends", "peers"]
    assert keys[i + 1] in ("outcome", "what_next")


def test_always_code_only_no_facts(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    assert conc.CONCENTRATION_KEY in sheet.code_only
    assert not any("data/raw/concentration" in f.source or f.label.startswith("Concentration") for f in sheet.facts)
    assert conc.ConcentrationSpecialist().build_facts(analyst_ctx, sheet) == []
    assert isinstance(sheet.extras["concentration"], conc.ConcentrationResult)
    by = {s.key: s for s in sections.sections_for(sheet)}
    assert by["concentration"].ai_written is False
    req = build_request(sheet, sections.sections_for(sheet), "claude-opus-5-5")
    assert "concentration" not in str(req["output_config"]) and "concentration" not in req["messages"][0]["content"].lower()


def test_section_definition():
    s = conc.CONCENTRATION_SECTION
    assert s.key == "concentration" and s.title == TITLE and s.window == "as_of" and not s.ai_written
    assert s.render is not None


def test_note_renders_section(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    res = write_memo(analyst_ctx, 3, client=FakeClient(split_memo(sheet, _memo(sheet))), out_dir=tmp_path / "banks",
                     replay_dir=tmp_path / "none")
    assert res.ok, res.errors
    text = res.path.read_text()
    assert f"## {TITLE}" in text
    assert text.count(conc.LEAD) == 1 and text.count(conc.TABLE_HEADER) == 1 and text.count(conc.CLOSING) == 1
    assert text.index("## Score history") < text.index(f"## {TITLE}")


def test_crossing_bank(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path, 100)
    r = sheet.extras["concentration"]
    assert r.construction_pct is not None and r.construction_pct >= 100
    assert conc.L1_CROSSED in "\n".join(conc.render_concentration(r))


def test_no_rows_bank(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path, 101)
    r = sheet.extras["concentration"]
    assert r.reason == conc.REASON_NO_DATA
    assert conc.REASON_NO_DATA in "\n".join(conc.render_concentration(r))


def test_registered_once():
    import canary.analyst.writer  # noqa: F401

    keys = [sp.key for sp in sections.SPECIALISTS]
    assert keys.index("trends") < keys.index("peers") < keys.index("concentration")
    assert keys.count("concentration") == 1
    saved = list(sections.SPECIALISTS)
    try:
        sections.register(conc.ConcentrationSpecialist())
        assert [sp.key for sp in sections.SPECIALISTS].count("concentration") == 1
    finally:
        sections.SPECIALISTS[:] = saved
