"""Memo writer (spec 5.5, 10): fact sheet -> Claude (structured JSON citing fact ids) -> checker
-> one retry with the checker's errors -> note saved only if the check passes.
"""

import json
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

from canary.analyst.checker import check_memo
from canary.analyst.facts import POSTHOC_LABEL, FactSheet, build_fact_sheet
from canary.analyst.render import note_path, render_note
from canary.analyst.sections import Section, all_sections

DEFAULT_MODEL = "claude-opus-5-5"
EFFORT = "medium"
MAX_TOKENS = 16000
FALLBACK_BETA = "server-side-fallback-2026-07-01"
PRICES = {"claude-opus-5-5": (4.0, 20.0), "claude-sonnet-5-5": (2.0, 10.0)}  # $ per 1M tokens in/out

SYSTEM_PROMPT = f"""You are Canary's risk analyst. Canary is a research tool that ranks every FDIC-insured US bank \
by a machine-learning score of its risk of failing within the next 4 quarters. You write short memo sections \
about one bank from a fact sheet, in plain English for a non-banker (a recruiter or interviewer). Explain any \
banking term in a few words the first time you use it. Be calm and factual; no hype, no advice.

Rules (code checks every one; a memo that breaks them is rejected):
1. Use only the facts in the fact sheet. Do not add outside knowledge, news, or claims the data cannot \
support (for example who the depositors are, fraud, or management quality).
2. Every sentence that contains a number or a date must list, in its "cites", the ids of the facts it \
uses (for example ["F5", "F6"]). Sentences without numbers or dates may have empty cites. Do not put \
fact ids or brackets in the text itself.
3. Copy every number exactly as the fact sheet's "display" column shows it: same digits, same rounding, \
same commas, keep % signs, keep +/- signs. Never write "percent" in words, never convert units, never \
compute new numbers (no differences, ratios, sums or "twice as high"). For comparisons, use words \
("well above the national median").
4. Write dates as the fact sheet shows them (2023-03-31), or as "Q1 2023", or with the full month name \
("March 31, 2023"). Never abbreviate a month (write "September", not "Sep"). Only use a date or year \
that belongs to a fact you cite.
5. Small counts that are not facts (for example the number of drivers you list) must be spelled out as \
words ("five"), never digits. Spelled time spans ("four quarters", "a year") count as numbers: use one \
only when a cited fact has it (the lead time, or a label that says it).
6. Sections marked as-of (summary, warning_signs, score) describe the bank only as of the as-of \
quarter. In them never cite a fact marked hindsight and never mention, hint at, or foreshadow anything \
after the as-of date, including whether the bank later failed. Do not use the words "failed", \
"collapsed", "was closed" or "was seized" in them.
7. The score is not a probability. Describe the bank by its national rank and percentile (lead with \
the rank), never as a chance or likelihood of failure.
8. A fact whose label contains "{POSTHOC_LABEL}" must be described with that exact label wording in the \
same sentence, so the reader knows it is not the model's result.
9. The summary is 2-4 sentences. Other sections are one to three short paragraphs.
10. Return only the JSON memo with one entry per requested section key."""


class RefusalError(RuntimeError):
    """Claude (and every fallback model) declined to write the memo."""


class TruncatedError(RuntimeError):
    """The response hit max_tokens before the JSON memo was complete."""


class EmptyResponseError(ValueError):
    """The response had no text block to parse as the JSON memo."""


@dataclass
class MemoResult:
    cert: int
    as_of: date
    path: Path | None
    ok: bool
    attempts: int
    errors: list[str] = field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    model: str = DEFAULT_MODEL
    cost_usd: float = 0.0
    first_errors: list[str] = field(default_factory=list)  # first attempt's checker errors; [] if it passed


def cost_usd(model: str, input_tokens: int, output_tokens: int) -> float:
    pin, pout = PRICES.get(model, PRICES[DEFAULT_MODEL])
    return (input_tokens * pin + output_tokens * pout) / 1_000_000


def ai_sections(sections: list[Section]) -> list[Section]:
    return [s for s in sections if s.ai_written]


def memo_schema(sections: list[Section]) -> dict:
    sentence = {
        "type": "object",
        "properties": {"text": {"type": "string"}, "cites": {"type": "array", "items": {"type": "string"}}},
        "required": ["text", "cites"],
        "additionalProperties": False,
    }
    paragraph = {
        "type": "object",
        "properties": {"sentences": {"type": "array", "items": sentence}},
        "required": ["sentences"],
        "additionalProperties": False,
    }
    section = {
        "type": "object",
        "properties": {
            "key": {"type": "string", "enum": [s.key for s in ai_sections(sections)]},
            "paragraphs": {"type": "array", "items": paragraph},
        },
        "required": ["key", "paragraphs"],
        "additionalProperties": False,
    }
    return {
        "type": "object",
        "properties": {"sections": {"type": "array", "items": section}},
        "required": ["sections"],
        "additionalProperties": False,
    }


def _cell(s: str) -> str:
    return str(s).replace("|", "/").replace("\n", " ")


def _user_message(sheet: FactSheet, sections: list[Section]) -> str:
    o = sheet.outcome
    lines = [
        f"Bank: {sheet.name} (cert {sheet.cert}). As-of quarter: {sheet.as_of.isoformat()}.",
        f"Outcome case for the hindsight sections: {o.kind}"
        + (" (failed after the test window)" if o.after_test_window else "") + ".",
        "",
        "Fact sheet. \"hindsight\" facts describe data after the as-of quarter and may be cited only in "
        "hindsight sections.",
        "",
        "| id | label | quarter | display | window |",
        "|---|---|---|---|---|",
    ]
    for f in sheet.facts:
        q = f.quarter.isoformat() if f.quarter else "-"
        lines.append(f"| {f.id} | {_cell(f.label)} | {q} | {_cell(f.display)} | "
                     f"{'hindsight' if f.hindsight else 'as-of'} |")
    lines += ["", "Write these sections (key, window, title: instructions):", ""]
    for s in ai_sections(sections):
        lines.append(f"- {s.key} ({s.window}), \"{s.title}\": {s.instructions}")
    lines += [
        "",
        "Code adds the score history table, the sources list, the outcome banner, the fixed sentence that "
        "the score is not a probability, and the \"What the model can't see\" paragraph after your score "
        "section. Do not write those yourself.",
    ]
    return "\n".join(lines)


def _retry_message(errors: list[str]) -> str:
    return (
        "The citation checker rejected that memo with these errors:\n"
        + "\n".join(f"- {e}" for e in errors)
        + "\n\nReturn a corrected full memo (every section, same JSON shape) that fixes all of them. "
        "Copy numbers exactly from the fact sheet's display column, cite the fact ids that support each "
        "number or date, and remove any number you cannot support."
    )


def build_request(sheet: FactSheet, sections: list[Section], model: str, errors: list[str] | None = None,
                  previous: dict | None = None) -> dict:
    """Keyword arguments for messages.create (no betas/fallbacks; batch requests can't set them)."""
    messages = [{"role": "user", "content": _user_message(sheet, sections)}]
    if errors:
        if previous is not None:
            messages.append({"role": "assistant", "content": json.dumps(previous)})
        messages.append({"role": "user", "content": _retry_message(errors)})
    # No `thinking` key: Opus 5.5 always thinks adaptively when it is omitted.
    return {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "system": SYSTEM_PROMPT,
        "messages": messages,
        "output_config": {"effort": EFFORT, "format": {"type": "json_schema", "schema": memo_schema(sections)}},
    }


def parse_response(message) -> dict:
    if message.stop_reason == "refusal":
        details = getattr(message, "stop_details", None)
        why = f" ({getattr(details, 'category', None)}: {getattr(details, 'explanation', None)})" if details else ""
        raise RefusalError(f"Claude refused to write the memo{why}")
    if message.stop_reason == "max_tokens":
        raise TruncatedError(f"response hit max_tokens ({MAX_TOKENS}) before the memo was complete")
    text = next((b.text for b in message.content if b.type == "text"), None)
    if text is None:
        kinds = ", ".join(b.type for b in message.content) or "none"
        raise EmptyResponseError(f"response has no text block to parse (stop_reason {message.stop_reason}; "
                                 f"blocks: {kinds})")
    return json.loads(text)


def write_memo(ctx, cert: int, as_of: date | None = None, *, client, model: str = DEFAULT_MODEL,
               out_dir: Path = Path("banks"), first_memo: dict | None = None,
               replay_dir: Path = Path("data/replay")) -> MemoResult:
    """Write one checked note. Raises ValueError for a bad as-of, RefusalError / TruncatedError from Claude.

    Any exception raised after calls were made carries `exc.usage` = {input_tokens, output_tokens,
    cost_usd, model} for those calls, so callers can still count the spend.
    """
    sheet = build_fact_sheet(ctx, cert, as_of, replay_dir=replay_dir)
    sections = all_sections(sheet.outcome.kind)
    to_check = ai_sections(sections)
    usage = {"in": 0, "out": 0, "cost": 0.0}
    served = model

    def call(errors=None, previous=None) -> dict:
        nonlocal served
        msg = client.beta.messages.create(
            **build_request(sheet, sections, model, errors, previous), betas=[FALLBACK_BETA], fallbacks="default"
        )
        served = msg.model or model
        i, o = msg.usage.input_tokens, msg.usage.output_tokens
        usage["in"] += i
        usage["out"] += o
        usage["cost"] += cost_usd(served if served in PRICES else model, i, o)
        return parse_response(msg)

    try:
        memo = first_memo if first_memo is not None else call()
        attempts = 1
        errors = check_memo(memo, sheet, to_check)
        first_errors = list(errors)
        if errors:
            memo = call(errors, memo)
            attempts = 2
            errors = check_memo(memo, sheet, to_check)
    except Exception as exc:
        try:
            exc.usage = {"input_tokens": usage["in"], "output_tokens": usage["out"],
                         "cost_usd": usage["cost"], "model": served}
        except AttributeError:  # an exception type that refuses attributes; nothing to attach
            pass
        raise

    path = None
    if not errors:
        meta = {"model_run": ctx.model_run, "written_at": datetime.now().isoformat(timespec="seconds"),
                "writer_model": served}
        path = note_path(out_dir, sheet.name, cert)
        out_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(render_note(sheet, memo, sections, meta))
    return MemoResult(cert, sheet.as_of, path, not errors, attempts, errors,
                      usage["in"], usage["out"], served, usage["cost"], first_errors)
