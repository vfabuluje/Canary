import json
import re
from datetime import date

import pytest
import yaml

from analyst_fakes import FakeClient, fake_message
from canary.analyst import __main__ as cli
from canary.analyst.facts import POSTHOC_LABEL, build_fact_sheet
from canary.analyst.sections import all_sections
from canary.analyst.writer import (
    FALLBACK_BETA,
    RefusalError,
    TruncatedError,
    build_request,
    cost_usd,
    memo_schema,
    parse_response,
    write_memo,
)

CERT = 3


@pytest.fixture
def sheet(analyst_ctx, tmp_path):
    return build_fact_sheet(analyst_ctx, CERT, replay_dir=tmp_path / "none")


def _memo(sheet, rank_text=None, extra=None):
    rank = next(f for f in sheet.facts if f.label.startswith("National rank"))
    secs = []
    for s in all_sections(sheet.outcome.kind):
        if not s.ai_written:
            continue
        sents = [{"text": "The bank looked weak in plain terms.", "cites": []}]
        if s.key == "summary":
            sents.append({"text": f"It ranked {rank_text or rank.display} nationally.", "cites": [rank.id]})
        if extra and s.key in extra:
            sents.append(extra[s.key])
        secs.append({"key": s.key, "paragraphs": [{"sentences": sents}]})
    return {"sections": secs}


def _write(ctx, tmp_path, responses, **kw):
    client = FakeClient(responses)
    res = write_memo(ctx, CERT, client=client, out_dir=tmp_path / "banks",
                     replay_dir=tmp_path / "none", **kw)
    return res, client


def test_good_memo_written(analyst_ctx, sheet, tmp_path):
    res, client = _write(analyst_ctx, tmp_path, [_memo(sheet)])
    assert res.ok and res.attempts == 1 and res.errors == [] and len(client.calls) == 1
    assert res.path.exists() and res.path.parent == tmp_path / "banks"
    text = res.path.read_text()
    fm = yaml.safe_load(text.split("---\n")[1])
    assert fm["writer_model"] == "claude-opus-5-5" and fm["model_run"] == analyst_ctx.model_run
    assert "The bank looked weak in plain terms." in text
    assert res.input_tokens == 1000 and res.output_tokens == 500
    assert res.cost_usd == pytest.approx(cost_usd("claude-opus-5-5", 1000, 500))


def test_writer_model_is_the_serving_model(analyst_ctx, sheet, tmp_path):
    msg = fake_message(json.dumps(_memo(sheet)), model="claude-sonnet-5-5")
    res, _ = _write(analyst_ctx, tmp_path, [msg])
    assert res.model == "claude-sonnet-5-5"
    assert "writer_model: \"claude-sonnet-5-5\"" in res.path.read_text()


def test_bad_then_good_retries_once(analyst_ctx, sheet, tmp_path):
    bad = _memo(sheet, rank_text="999,999")
    res, client = _write(analyst_ctx, tmp_path, [bad, _memo(sheet)])
    assert res.ok and res.attempts == 2 and res.path.exists()
    assert res.input_tokens == 2000 and res.output_tokens == 1000
    second = client.calls[1]["messages"]
    assert "999,999" in second[-1]["content"] and "not supported by cited facts" in second[-1]["content"]
    assert json.loads(second[-2]["content"]) == bad  # previous memo echoed as the assistant turn
    assert second[-2]["role"] == "assistant"
    assert len(res.first_errors) >= 1 and any("999,999" in e for e in res.first_errors)
    assert res.errors == []


def test_first_errors_empty_when_first_attempt_passes(analyst_ctx, sheet, tmp_path):
    res, _ = _write(analyst_ctx, tmp_path, [_memo(sheet)])
    assert res.first_errors == []


def test_bad_twice_not_written(analyst_ctx, sheet, tmp_path):
    bad = _memo(sheet, rank_text="999,999")
    res, client = _write(analyst_ctx, tmp_path, [bad, bad])
    assert not res.ok and res.path is None and res.attempts == 2 and len(client.calls) == 2
    assert any("999,999" in e for e in res.errors)
    assert not (tmp_path / "banks").exists() or not any((tmp_path / "banks").iterdir())


def test_first_memo_skips_first_call(analyst_ctx, sheet, tmp_path):
    res, client = _write(analyst_ctx, tmp_path, [], first_memo=_memo(sheet))
    assert res.ok and res.attempts == 1 and client.calls == []
    bad = _memo(sheet, rank_text="999,999")
    res, client = _write(analyst_ctx, tmp_path, [_memo(sheet)], first_memo=bad)
    assert res.ok and res.attempts == 2 and len(client.calls) == 1


def test_refusal_raises_clean_error(analyst_ctx, tmp_path):
    with pytest.raises(RefusalError):
        _write(analyst_ctx, tmp_path, [fake_message("", stop_reason="refusal")])
    with pytest.raises(TruncatedError):
        _write(analyst_ctx, tmp_path, [fake_message("{\"sec", stop_reason="max_tokens")])


def test_parse_response_skips_thinking_blocks():
    from types import SimpleNamespace

    msg = fake_message('{"sections": []}')
    msg.content.insert(0, SimpleNamespace(type="thinking", thinking="..."))
    assert parse_response(msg) == {"sections": []}


def test_bad_as_of_raises(analyst_ctx, tmp_path):
    with pytest.raises(ValueError):
        _write(analyst_ctx, tmp_path, [], as_of=date(2010, 3, 31))


def test_request_shape(analyst_ctx, sheet):
    secs = all_sections("caught")
    kw = build_request(sheet, secs, "claude-opus-5-5")
    assert kw["output_config"]["effort"] == "medium" and "fallbacks" not in kw
    assert kw["model"] == "claude-opus-5-5" and kw["max_tokens"] == 16000 and "thinking" not in kw
    assert kw["output_config"]["format"]["type"] == "json_schema"
    assert kw["output_config"]["format"]["schema"] == memo_schema(secs)
    user = kw["messages"][0]["content"]
    assert len(kw["messages"]) == 1 and kw["messages"][0]["role"] == "user"
    for f in sheet.facts:
        assert f"| {f.id} |" in user
    assert "hindsight" in user
    assert "Score history" not in user  # code-rendered sections are not sent
    system = kw["system"]
    for phrase in ("cite", "post-hoc check, designed after the 2023 failures", "probability",
                   "2-4 sentences", "September", "non-banker"):
        assert phrase in system


def test_schema_section_enum():
    secs = all_sections("quiet")
    schema = memo_schema(secs)
    sec_item = schema["properties"]["sections"]["items"]
    assert sec_item["properties"]["key"]["enum"] == ["summary", "warning_signs", "score", "what_next"]
    assert schema["additionalProperties"] is False and sec_item["additionalProperties"] is False


def test_create_called_with_fallbacks(analyst_ctx, sheet, tmp_path):
    _, client = _write(analyst_ctx, tmp_path, [_memo(sheet)])
    kw = client.calls[0]
    assert kw["betas"] == [FALLBACK_BETA] == ["server-side-fallback-2026-07-01"]
    assert kw["fallbacks"] == "default"


def test_cost():
    assert cost_usd("claude-opus-5-5", 1_000_000, 1_000_000) == pytest.approx(24.0)
    assert cost_usd("claude-sonnet-5-5", 1_000_000, 1_000_000) == pytest.approx(12.0)


def _cli(monkeypatch, analyst_ctx, tmp_path, responses, *extra):
    client = FakeClient(responses)
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "make_client", lambda: client)
    monkeypatch.setattr(cli, "REPLAY_DIR", tmp_path / "none")
    return cli.main(["memo", "--cert", str(CERT), "--out", str(tmp_path / "banks"), *extra])


def test_cli_memo_ok(monkeypatch, analyst_ctx, sheet, tmp_path, capsys):
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [_memo(sheet)]) == 0
    assert "Failed Bank 3 (3).md" in capsys.readouterr().out


def test_cli_memo_fails_check(monkeypatch, analyst_ctx, sheet, tmp_path, capsys):
    bad = _memo(sheet, rank_text="999,999")
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [bad, bad]) == 1
    assert "999,999" in capsys.readouterr().err


def test_cli_bad_as_of_exits_2(monkeypatch, analyst_ctx, tmp_path, capsys):
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [], "--as-of", "2010-03-31") == 2
    assert "as-of" in capsys.readouterr().err


def test_cli_refusal_exits_1(monkeypatch, analyst_ctx, tmp_path, capsys):
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [fake_message("", stop_reason="refusal")]) == 1
    assert "refused" in capsys.readouterr().err


def test_posthoc_label_passes_first_try(analyst_ctx, tmp_path):
    # SVB-like: last report 2022-12-31, run-risk fact dated then, label mentions "2023".
    replay = tmp_path / "replay"
    replay.mkdir()
    import pandas as pd

    pd.DataFrame({"cert": [24735], "report_date": ["2022-12-31"], "run_risk_rank": [3],
                  "run_risk_flagged": [True]}).to_csv(replay / "replay_banks.csv", index=False)
    sheet = build_fact_sheet(analyst_ctx, 24735, replay_dir=replay)
    assert sheet.as_of == date(2022, 12, 31)
    rr = next(f for f in sheet.facts if POSTHOC_LABEL in f.label)
    assert rr.quarter == date(2022, 12, 31)
    sent = {"text": f"On the run-risk rank, a {POSTHOC_LABEL}, it was #3 nationally.", "cites": [rr.id]}
    memo = _memo(sheet, extra={"outcome": sent})
    client = FakeClient([memo])
    res = write_memo(analyst_ctx, 24735, client=client, out_dir=tmp_path / "banks", replay_dir=replay)
    assert res.ok and res.attempts == 1, res.errors


def test_section_instructions_match_renderer(sheet):
    from canary.analyst.sections import OUTCOME_TITLES

    for kind in list(OUTCOME_TITLES) + ["quiet"]:
        for s in all_sections(kind):
            if not s.ai_written:
                continue
            low = s.instructions.lower()
            assert "provided paragraph" not in low and "fixed sentence" not in low, s.key
            assert "code-rendered" not in low, s.key
            assert not re.search(r"top \d", low), s.key  # bare digits invite unchecked counts
    score = next(s for s in all_sections("quiet") if s.key == "score").instructions.lower()
    assert "do not write" in score and "probability" in score and "can't-see" in score
    assert "top five drivers" in score
    # The request agrees with the instructions: code adds these parts, Claude must not write them.
    user = build_request(sheet, all_sections(sheet.outcome.kind), "claude-opus-5-5")["messages"][0]["content"]
    assert "Do not write those yourself" in user
    assert "fixed sentence" not in user.split("Write these sections")[1].split("Code adds")[0].lower()


def test_cli_malformed_json_exits_1(monkeypatch, analyst_ctx, tmp_path, capsys):
    assert _cli(monkeypatch, analyst_ctx, tmp_path, ["not json {"]) == 1
    assert "malformed" in capsys.readouterr().err


# ---- final-review fixes ----------------------------------------------------------------

def test_parse_response_without_text_block_is_clear():
    from types import SimpleNamespace

    from canary.analyst.writer import EmptyResponseError

    msg = fake_message("")
    msg.content = [SimpleNamespace(type="thinking", thinking="...")]
    with pytest.raises(EmptyResponseError, match="no text block"):
        parse_response(msg)
    assert issubclass(EmptyResponseError, ValueError)


def test_cli_memo_no_text_block_exits_1(monkeypatch, analyst_ctx, tmp_path, capsys):
    msg = fake_message("")
    msg.content = []
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [msg]) == 1
    assert "no text block" in capsys.readouterr().err


def test_cli_memo_api_error_exits_1(monkeypatch, analyst_ctx, tmp_path, capsys):
    from analyst_fakes import api_status_error

    err = api_status_error("RateLimitError", 429, "rate limited")
    assert _cli(monkeypatch, analyst_ctx, tmp_path, [err]) == 1
    out = capsys.readouterr().err
    assert "Claude API call failed (RateLimitError)" in out and len(out.strip().splitlines()) == 1


def test_exception_carries_usage_of_earlier_calls(analyst_ctx, sheet, tmp_path):
    bad = _memo(sheet, rank_text="999,999")
    with pytest.raises(RefusalError) as info:
        _write(analyst_ctx, tmp_path, [bad, fake_message("", stop_reason="refusal")])
    u = info.value.usage
    assert u["input_tokens"] == 2000 and u["output_tokens"] == 1000  # both calls returned usage
    assert u["cost_usd"] == pytest.approx(2 * cost_usd("claude-opus-5-5", 1000, 500))
    assert u["model"] == "claude-opus-5-5"
    with pytest.raises(RuntimeError) as info:
        _write(analyst_ctx, tmp_path, [bad, RuntimeError("down")])
    assert info.value.usage["input_tokens"] == 1000


def test_request_comment_on_adaptive_thinking():
    import inspect

    from canary.analyst import writer

    assert "always thinks adaptively" in inspect.getsource(writer.build_request)


def test_make_client_without_credentials_exits_1(monkeypatch, analyst_ctx, tmp_path, capsys):
    """R15: no key anywhere -> one clear line and exit 1, before any API call."""
    import anthropic

    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
    monkeypatch.setattr(cli, "_read_dotenv", lambda path: {})
    for var in ("ANTHROPIC_CONFIG_DIR", "ANTHROPIC_PROFILE"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))  # no `ant auth login` profile on disk
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "xdg"))
    with pytest.raises(cli.NoCredentialsError, match="No Anthropic API key found"):
        cli.make_client()
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    assert cli.main(["memo", "--cert", str(CERT), "--out", str(tmp_path / "banks")]) == 1
    err = capsys.readouterr().err.strip().splitlines()
    assert err == ["error: No Anthropic API key found: set ANTHROPIC_API_KEY in .env or run `ant auth login`"]
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test-not-used")
    assert isinstance(cli.make_client(), anthropic.Anthropic)  # constructed only, never called
    monkeypatch.delenv("ANTHROPIC_API_KEY")
    monkeypatch.setenv("ANTHROPIC_CONFIG_DIR", str(tmp_path / "cfg"))  # a profile that does not exist
    monkeypatch.setenv("ANTHROPIC_PROFILE", "missing")
    with pytest.raises(cli.NoCredentialsError, match="No Anthropic API key found"):
        cli.make_client()
