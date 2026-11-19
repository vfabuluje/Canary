"""Three-agent memo pipeline, request side (phase 5e): per-agent fact subsets, section lists and
`messages.create` kwargs. The trend agent writes `trends`, the peer agent writes `peers`, and the
risk analyst writes every other AI section after seeing the specialists' checked text.
"""

import json
from dataclasses import dataclass, field, replace

from canary.analyst.checker import check_memo
from canary.analyst.concentration import CONCENTRATION_KEY, render_concentration
from canary.analyst.facts import PERCENTILE_SCALE_LABEL, FactSheet
from canary.analyst.sections import Section, sections_for
from canary.analyst.writer import (
    EFFORT, FALLBACK_BETA, MAX_TOKENS, PRICES, SYSTEM_PROMPT, _cell, _retry_message, _user_message, ai_sections,
    cost_usd, memo_schema, parse_response, system_prompt,
)

AGENTS = ("trend", "peer", "analyst")
AGENT_SECTIONS: dict[str, str] = {"trend": "trends", "peer": "peers"}
_KIND_PREFIX = {"trend": "trend_", "peer": "peer_"}
_ROLE = {"trend": "trend agent", "peer": "peer agent"}
IDENTITY_LABELS: tuple[str, ...] = (
    "Bank name", "Certificate number", "As-of quarter", "National rank (1 = highest score)",
    "Banks ranked that quarter", "Percentile (100 = highest risk)", PERCENTILE_SCALE_LABEL, "On the watchlist",
)
ANALYST_INSTRUCTION = (
    "The trend, peer and concentration sections are written by other agents or code and appear in the "
    "note as they are. Don't repeat them at length; you may refer to their findings and cite the same "
    "fact ids for any number you use. If two sections genuinely point different ways, say so plainly in "
    "warning signs or the summary; never blend them into one statement."
)


def _check_agent(agent: str) -> None:
    if agent not in AGENTS:
        raise ValueError(f"unknown agent {agent!r}; expected one of {AGENTS}")


def agent_sheet(sheet: FactSheet, agent: str) -> FactSheet:
    """A copy of the sheet showing only what this agent may see (same fact ids); analyst: everything."""
    _check_agent(agent)
    if agent == "analyst":
        return replace(sheet, facts=list(sheet.facts), code_only=set(sheet.code_only), extras=dict(sheet.extras))
    prefix = _KIND_PREFIX[agent]
    facts = [f for f in sheet.facts if (f.kind or "").startswith(prefix) or f.label in IDENTITY_LABELS]
    return replace(sheet, facts=facts, code_only=set(sheet.code_only), extras=dict(sheet.extras))


def agent_sections(sheet: FactSheet, agent: str) -> list[Section]:
    """The AI-written sections this agent is asked for ([] for a specialist whose section is code-only)."""
    _check_agent(agent)
    ai = ai_sections(sections_for(sheet))
    if agent == "analyst":
        specialist = set(AGENT_SECTIONS.values())
        return [s for s in ai if s.key not in specialist]
    return [s for s in ai if s.key == AGENT_SECTIONS[agent]]


def _specialist_message(sheet: FactSheet, sections: list[Section]) -> str:
    lines = [
        f"Bank: {sheet.name} (cert {sheet.cert}). As-of quarter: {sheet.as_of.isoformat()}.",
        "",
        "Fact sheet (the only facts you may use or cite).",
        "",
        "| id | label | quarter | display | window |",
        "|---|---|---|---|---|",
    ]
    for f in sheet.facts:
        q = f.quarter.isoformat() if f.quarter else "-"
        lines.append(f"| {f.id} | {_cell(f.label)} | {q} | {_cell(f.display)} | "
                     f"{'hindsight' if f.hindsight else 'as-of'} |")
    lines += ["", "Write this section (key, window, title: instructions):", ""]
    for s in sections:
        lines.append(f"- {s.key} ({s.window}), \"{s.title}\": {s.instructions}")
        if s.render is not None or s.render_before is not None:
            lines.append(f"Code adds the table and fixed sentences around your {s.key} section; do not write them.")
    return "\n".join(lines)


_BLOCK_TITLES = {"trend": "Trend agent's section (checked, do not rewrite)",
                 "peer": "Peer agent's section (checked, do not rewrite)"}


def _specialist_block(agent: str, key: str, memo: dict) -> list[str]:
    entry = next((s for s in memo.get("sections", []) if s["key"] == key), None)
    paragraphs = [p for p in (entry or {}).get("paragraphs", []) if p.get("sentences")]
    if not paragraphs:
        raise ValueError(f"{agent} memo has no text for section {key!r}")
    lines = [f"### {_BLOCK_TITLES[agent]}",
             "(Each sentence is followed by the fact ids it cites. Cites are metadata, not text to copy.)"]
    for para in paragraphs:
        for s in para["sentences"]:
            lines.append(s["text"])
            if s.get("cites"):
                lines.append("  cites: " + ", ".join(s["cites"]))
        lines.append("")
    return lines


def _analyst_message(sheet: FactSheet, sections: list[Section], specialist_memos: dict[str, dict]) -> str:
    lines = [_user_message(sheet, sections), "", "Sections written by other agents or code:", ""]
    code_only = []
    for agent, key in AGENT_SECTIONS.items():
        if key in sheet.code_only:
            code_only.append(key)
            continue
        memo = specialist_memos.get(agent)
        if memo is None:
            raise ValueError(f"missing {agent} memo for the analyst request")
        lines += _specialist_block(agent, key, memo)
    conc = sheet.extras.get(CONCENTRATION_KEY)
    if conc is not None:
        lines += ["### Real-estate concentration (code-written)", *render_concentration(conc), ""]
    if code_only:
        lines.append("These specialist sections are code-only for this bank (no agent text): "
                     + ", ".join(code_only) + ".")
        lines.append("")
    lines.append(ANALYST_INSTRUCTION)
    return "\n".join(lines)


def build_agent_request(sheet: FactSheet, agent: str, model: str,
                        specialist_memos: dict[str, dict] | None = None, errors: list[str] | None = None,
                        previous: dict | None = None) -> dict:
    """Keyword arguments for messages.create, same shape as writer.build_request."""
    _check_agent(agent)
    sections = agent_sections(sheet, agent)
    if agent != "analyst" and not sections:
        raise ValueError(f"{agent} section is code-only; no request should be built")
    if agent == "analyst":
        user = _analyst_message(sheet, sections, specialist_memos or {})
        system = SYSTEM_PROMPT
    else:
        user = _specialist_message(agent_sheet(sheet, agent), sections)
        system = system_prompt(_ROLE[agent])
    messages = [{"role": "user", "content": user}]
    if errors:
        if previous is not None:
            messages.append({"role": "assistant", "content": json.dumps(previous)})
        messages.append({"role": "user", "content": _retry_message(errors)})
    return {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "system": system,
        "messages": messages,
        "output_config": {"effort": EFFORT, "format": {"type": "json_schema", "schema": memo_schema(sections)}},
    }


@dataclass
class AgentResult:
    agent: str
    ok: bool
    attempts: int = 0
    errors: list[str] = field(default_factory=list)
    first_errors: list[str] = field(default_factory=list)
    memo: dict | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    served_model: str | None = None
    skipped: bool = False


def run_agent(sheet: FactSheet, agent: str, *, client, model: str, specialist_memos: dict[str, dict] | None = None,
              first_memo: dict | None = None, trace: list, before_call=None) -> AgentResult:
    """One agent: a call (or the given batch `first_memo`), check, one retry with the errors, check.

    Checks run against this agent's sheet and sections. Appends one entry per attempt to `trace`.
    An exception from a call carries `exc.usage` for this agent's calls so far.
    `before_call(agent, attempt)`, if given, runs immediately before each direct (non-batch) API call;
    raising from it stops that call (none is made) and propagates.
    """
    _check_agent(agent)
    sections = agent_sections(sheet, agent)
    if agent != "analyst" and not sections:
        return AgentResult(agent, ok=True, skipped=True)
    check_sheet = agent_sheet(sheet, agent)
    res = AgentResult(agent, ok=False, served_model=model)

    def request(errors=None, previous=None) -> dict:
        return build_agent_request(sheet, agent, model, specialist_memos, errors, previous)

    def call(errors=None, previous=None) -> dict:
        if before_call is not None:
            before_call(agent, res.attempts + 1)
        kw = request(errors, previous)
        entry = {"agent": agent, "attempt": res.attempts + 1, "request": kw, "response_text": "",
                 "checker_errors": [], "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0,
                 "served_model": None, "source": "direct"}
        trace.append(entry)
        try:
            msg = client.beta.messages.create(**kw, betas=[FALLBACK_BETA], fallbacks="default")
            served = msg.model or model
            i, o = msg.usage.input_tokens, msg.usage.output_tokens
            c = cost_usd(served if served in PRICES else model, i, o)
            res.served_model = served
            res.input_tokens += i
            res.output_tokens += o
            res.cost_usd += c
            entry.update(input_tokens=i, output_tokens=o, cost_usd=c, served_model=served,
                         response_text=next((b.text for b in msg.content if b.type == "text"), ""))
            return parse_response(msg)
        finally:
            res.attempts += 1

    def given(memo: dict) -> dict:
        trace.append({"agent": agent, "attempt": 1, "request": request(), "response_text": json.dumps(memo),
                      "checker_errors": [], "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0,
                      "served_model": None, "source": "batch"})
        res.attempts += 1
        return memo

    try:
        memo = given(first_memo) if first_memo is not None else call()
        errors = check_memo(memo, check_sheet, sections)
        trace[-1]["checker_errors"] = list(errors)
        res.first_errors = list(errors)
        if errors:
            memo = call(errors, memo)
            errors = check_memo(memo, check_sheet, sections)
            trace[-1]["checker_errors"] = list(errors)
    except Exception as exc:
        try:
            exc.usage = {"input_tokens": res.input_tokens, "output_tokens": res.output_tokens,
                         "cost_usd": res.cost_usd, "model": res.served_model}
        except AttributeError:
            pass
        raise
    res.errors = list(errors)
    res.ok = not errors
    res.memo = memo
    return res
