"""Report-card text built by code from a showcase trace (spec 5.5): slim trace, sentence picking,
hover text for highlighted numbers, the outcome headline and the rule card. No Claude calls."""

import json
import re

# _tokens/_norm are the checker's own tokenizer: extract_tokens() returns only the normalized form,
# and a card needs the number exactly as written in the sentence so the page can highlight it.
from canary.analyst.checker import _norm, _tokens
from canary.analyst.concentration import (
    DEFINITIONS, NA, ROW_CONSTRUCTION, ROW_CRE, ROW_GROWTH, TABLE_HEADER, YES, ConcentrationResult,
    render_concentration,
)
from canary.analyst.facts import Fact, date_forms
from canary.analyst.pipeline import AGENTS, IDENTITY_LABELS
from canary.dashboard.copy import GLOSSARY, HEADLINES

# (agent, memo section key) for the AI-written cards.
CARD_SECTIONS: tuple[tuple[str, str], ...] = (("trend", "trends"), ("peer", "peers"), ("analyst", "summary"))
_RULE_ROWS = {ROW_CONSTRUCTION: "construction_concentration", ROW_CRE: "cre_concentration",
              ROW_GROWTH: "cre_growth"}
# Facts that only restate who the bank is, its rank, or its FDIC peer group (spec 5.5: skip sentences that
# "only repeat the rank or the FDIC specialty group"). IDENTITY_LABELS plus the other context the
# writers open with: state, size, score, watchlist size, last year's percentile, the peer group itself.
CONTEXT_LABELS: frozenset[str] = frozenset(IDENTITY_LABELS) | {
    "State", "Model score", "Watchlist share of banks", "Banks on the watchlist that quarter", "Bank: total assets",
}
CONTEXT_KINDS: frozenset[str] = frozenset({
    "trend_prior_percentile", "trend_rank_phrase", "peer_specialty", "peer_tier", "peer_basis", "peer_count",
})
_FEATURE_SOURCE = re.compile(r"fct_bank_features\.parquet: (\w+)|scores\.parquet: feature (\w+) contribution")


def slim_trace(trace: dict) -> dict:
    """Per agent: whether it ran, how many attempts it took, and whether the first attempt passed."""
    agents = {}
    for agent in AGENTS:
        attempts = [int(c["attempt"]) for c in trace.get("calls", []) if c["agent"] == agent]
        n = max(attempts, default=0)
        agents[agent] = {"ran": bool(attempts), "attempts": n, "first_try": n == 1}
    return {"agents": agents}


def last_memo(trace: dict, agent: str) -> dict | None:
    """The agent's memo from its last attempt (the one that passed, in an ok trace); None if it didn't run."""
    calls = [c for c in trace.get("calls", []) if c["agent"] == agent]
    if not calls:
        return None
    return json.loads(max(calls, key=lambda c: int(c["attempt"]))["response_text"])


def memo_section(memo: dict | None, key: str) -> dict | None:
    if memo is None:
        return None
    return next((s for s in memo.get("sections", []) if s.get("key") == key), None)


def explain(fact: Fact) -> str:
    """Glossary text for the ratio a fact is about, else the fact's label."""
    feature = fact.feature
    if feature is None and (m := _FEATURE_SOURCE.search(fact.source)):
        feature = m.group(1) or m.group(2)
    return GLOSSARY.get(feature, fact.label) if feature else fact.label


def _number(text: str, label: str, quarter: str | None, explain_text: str) -> dict:
    return {"text": text, "label": label, "quarter": quarter, "explain": explain_text}


def numbers_in(text: str, cited: list[Fact]) -> list[dict]:
    """Numbers in the sentence, as written, each matched to the first cited fact whose (non-date) forms
    contain it. Dates and spelled spans ("a year") are not highlighted."""
    plain = [(f, {_norm(x) for x in f.forms if f.quarter is None or x not in date_forms(f.quarter)})
             for f in cited]
    out = []
    for tok in _tokens(text):
        if tok.kind != "num" or not any(ch.isdigit() for ch in tok.raw):
            continue
        fact = next((f for f, forms in plain if tok.norm in forms), None)
        if fact is not None:
            out.append(_number(tok.raw, fact.label, fact.quarter.isoformat() if fact.quarter else None,
                               explain(fact)))
    return out


def is_context(fact: Fact) -> bool:
    return fact.label in CONTEXT_LABELS or fact.kind in CONTEXT_KINDS


def pick_sentences(memo_section: dict, facts: dict[str, Fact], n: int = 2) -> list[dict]:
    """The first n sentences that are findings, with their numbers: a sentence is skipped when every fact
    it cites only restates the bank's identity, rank or peer group. A sentence with no cites has no
    numbers (the checker requires a cite for any number) and is kept: it states a finding in words."""
    out = []
    for para in memo_section.get("paragraphs", []):
        for sent in para.get("sentences", []):
            cited = [facts[c] for c in sent.get("cites") or []]
            if cited and all(is_context(f) for f in cited):
                continue
            out.append({"text": sent["text"], "numbers": numbers_in(sent["text"], cited)})
            if len(out) == n:
                return out
    return out


def headline(outcome_kind: str, name: str) -> str:
    return HEADLINES[outcome_kind].format(name=name)


def rule_sentences(result: ConcentrationResult) -> list[dict]:
    """The rule card from the code-rendered concentration lines: the verdict, then the construction and
    total commercial real estate rows that have a value, and the growth row when the 300% line was
    reached (the only case where growth decides the result). A test that can't be applied shows its
    reason and no figures."""
    lines = render_concentration(result)
    row_idx = [i for i, line in enumerate(lines) if line.startswith("| ") and line != TABLE_HEADER]
    rows = [[c.strip() for c in lines[i].strip().strip("|").split("|")] for i in row_idx]
    verdict = [line for line in lines[row_idx[-1] + 1:lines.index(DEFINITIONS)] if line.strip()]
    quarter = result.as_of.isoformat()
    cre_reached = any(test == ROW_CRE and meets == YES for test, _, _, meets in rows)
    out = [{"text": line, "numbers": []} for line in verdict]
    for test, bank, line, _ in rows:
        if bank == NA or (test == ROW_GROWTH and not cre_reached):
            continue
        out.append({"text": f"{test}: {bank} (the line is {line}).",
                    "numbers": [_number(bank, test, quarter, GLOSSARY[_RULE_ROWS[test]])]})
    return out
