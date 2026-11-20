import pytest

from analyst_fakes import FakeClient, split_memo
from canary.analyst import sections
from canary.analyst.facts import Fact, build_fact_sheet
from canary.analyst.render import render_note
from canary.analyst.writer import write_memo
from test_analyst_writer import _memo

CERT = 3


def _spec(code_only=True, render=None):
    class Spec:
        key = "x"
        sections = [sections.Section("x", "X", "as_of", "say x", True, render)]

        def build_facts(self, ctx, sheet):
            if code_only:
                sheet.code_only.add("x")
            return []

    return Spec()


@pytest.fixture
def registry():
    saved = list(sections.SPECIALISTS)
    yield
    sections.SPECIALISTS[:] = saved


def test_sections_for_code_only(registry, analyst_ctx, tmp_path):
    sections.register(_spec())
    sheet = build_fact_sheet(analyst_ctx, CERT, replay_dir=tmp_path / "none")
    by = {s.key: s for s in sections.sections_for(sheet)}
    assert by["x"].ai_written is False
    assert by["summary"].ai_written is True and by["score_history"].ai_written is False


def test_code_only_section_not_requested(registry, analyst_ctx, tmp_path):
    sections.register(_spec())
    sheet = build_fact_sheet(analyst_ctx, CERT, replay_dir=tmp_path / "none")
    client = FakeClient(split_memo(sheet, _memo(sheet)))
    res = write_memo(analyst_ctx, CERT, client=client, out_dir=tmp_path / "banks", replay_dir=tmp_path / "none")
    for kw in client.calls:
        schema = kw["output_config"]["format"]["schema"]
        assert "x" not in schema["properties"]["sections"]["items"]["properties"]["key"]["enum"]
    assert res.ok, res.errors


def test_render_hook_output_in_note(registry, analyst_ctx, tmp_path):
    sections.register(_spec(code_only=False, render=lambda sheet: ["RENDERED LINE"]))
    sheet = build_fact_sheet(analyst_ctx, CERT, replay_dir=tmp_path / "none")
    memo = _memo(sheet)
    memo["sections"].append({"key": "x", "paragraphs": [{"sentences": [{"text": "AI x text.", "cites": []}]}]})
    text = render_note(sheet, memo, sections.sections_for(sheet), {"model_run": "r", "written_at": "t", "writer_model": "m"})
    body = text.split("## X")[1].split("\n## ")[0]
    assert body.index("AI x text.") < body.index("RENDERED LINE")


def test_register_is_idempotent_by_key(registry):
    n = len(sections.SPECIALISTS)
    sections.register(_spec())
    sections.register(_spec())
    assert len(sections.SPECIALISTS) == n + 1
