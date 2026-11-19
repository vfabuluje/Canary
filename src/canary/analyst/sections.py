"""Section registry for the memo (spec 5.2, 5.3, 7). Specialists (5b-5d) register extra sections."""

from collections.abc import Callable
from dataclasses import dataclass, replace
from typing import Any, Literal, Protocol


@dataclass
class Section:
    key: str
    title: str
    window: Literal["as_of", "hindsight"]
    instructions: str
    ai_written: bool
    # Code-rendered lines appended after the section's AI paragraphs; takes the FactSheet.
    render: Callable[[Any], list[str]] | None = None
    # Code-rendered lines placed right after the heading, before the AI paragraphs.
    render_before: Callable[[Any], list[str]] | None = None


ANALYST_SECTIONS: list[Section] = [
    Section("summary", "Summary", "as_of",
            "2-4 sentences using only as-of facts. Lead with the rank, not the raw score. No outcome.", True),
    Section("warning_signs", "Warning signs in the data", "as_of",
            "The bank's notable figures at as-of (capital, credit quality, liquidity/funding, bond losses), "
            "each compared with the national median for that quarter. Only as-of facts.", True),
    Section("score", "Understanding the score", "as_of",
            "Rank, percentile and the watchlist line; then the top five drivers up and down in plain "
            "names, with each feature's value. Do not write the sentence that the score is not a "
            "probability or the can't-see paragraph: code adds both after this section. Only as-of facts.",
            True),
    Section("score_history", "Score history", "as_of",
            "Code-rendered table of rank and flag for the 8 quarters to as-of.", False),
    Section("outcome", "Outcome", "hindsight",
            "Explain the outcome with hindsight facts only; label it as hindsight.", True),
    Section("what_next", "What happened next", "hindsight",
            "Hindsight, labeled: failure date and later ranks, or rank and flags after as-of and whether "
            "the bank still reports (stopped reporting: merged or closed, not distinguished in our data).", True),
    Section("sources", "Sources", "as_of", "Code-rendered list of every cited fact.", False),
]

OUTCOME_TITLES = {
    "caught": "How early Canary caught it",
    "missed": "Why the model missed it",
    "false_alarm": "Why it was flagged, and what happened",
    "open_watchlist": "Why it's on the watchlist",
}


class Specialist(Protocol):
    key: str
    sections: list[Section]

    def build_facts(self, ctx, sheet) -> list: ...


SPECIALISTS: list[Specialist] = []


def register(specialist: Specialist) -> None:
    if any(sp.key == specialist.key for sp in SPECIALISTS):
        return
    SPECIALISTS.append(specialist)


def all_sections(kind: str) -> list[Section]:
    """Sections for an outcome kind; specialist sections follow score_history."""
    out: list[Section] = []
    for sec in ANALYST_SECTIONS:
        if sec.key == "outcome":
            if kind not in OUTCOME_TITLES:
                continue
            sec = replace(sec, title=OUTCOME_TITLES[kind])
        out.append(sec)
        if sec.key == "score_history":
            for sp in SPECIALISTS:
                out.extend(sp.sections)
    return out


def sections_for(sheet: Any) -> list[Section]:
    """Sections for this sheet's outcome; keys in sheet.code_only are not asked of the AI."""
    return [replace(s, ai_written=False) if s.key in sheet.code_only else s
            for s in all_sections(sheet.outcome.kind)]
