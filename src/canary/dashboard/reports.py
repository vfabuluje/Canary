"""reports/<cert>.json for each showcase bank (spec 5.5, 6): slim trace, report cards, the fact sheet
(for Ask Canary) and the note. Facts are rebuilt by code from the same data and model as the run;
the export fails if the trace no longer checks against the rebuilt sheet. No Claude calls."""

import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from canary.analyst.checker import _norm, check_memo
from canary.analyst.concentration import CONCENTRATION_KEY, render_concentration
from canary.analyst.facts import Fact, FactSheet, build_fact_sheet
from canary.analyst.pipeline import AGENTS, agent_sections, agent_sheet
from canary.dashboard.cards import headline, last_memo, memo_section, pick_sentences, rule_sentences, slim_trace
from canary.dashboard.copy import FLAGSHIP_CARDS
from canary.dashboard.tables import note_key, showcase_certs

# Report cards in page order: key -> (agent, memo section key); the rule card is code-rendered.
CARD_ORDER: tuple[tuple[str, str | None, str | None], ...] = (
    ("trend", "trend", "trends"), ("peer", "peer", "peers"), ("rule", None, None), ("summary", "analyst", "summary"),
)


def _iso(d: date | None) -> str | None:
    return d.isoformat() if d is not None else None


def _json_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, np.generic):
        return obj.item()
    raise TypeError(f"not JSON serializable: {type(obj).__name__}")


def fact_dict(f: Fact) -> dict:
    d = asdict(f)
    d["quarter"] = _iso(f.quarter)
    return d


def check_trace(sheet: FactSheet, trace: dict) -> None:
    """Raise ValueError unless each agent's last memo still passes the checker against the rebuilt sheet
    (same fact ids, same forms), and the agents that ran are the ones the sheet asks for."""
    ids = {f.id for f in sheet.facts}
    for agent in AGENTS:
        memo = last_memo(trace, agent)
        sections = agent_sections(sheet, agent)
        if memo is None:
            if sections:
                raise ValueError(f"cert {sheet.cert}: no {agent} call in the trace, but the sheet asks for one")
            continue
        if not sections:
            raise ValueError(f"cert {sheet.cert}: the trace has a {agent} call, but the sheet asks for none")
        cited = {c for s in memo.get("sections", []) for p in s.get("paragraphs", [])
                 for sent in p.get("sentences", []) for c in sent.get("cites") or []}
        missing = sorted(cited - ids)
        if missing:
            raise ValueError(f"cert {sheet.cert}: {agent} cites fact ids missing from the rebuilt sheet: "
                             f"{', '.join(missing)}")
        errors = check_memo(memo, agent_sheet(sheet, agent), sections)
        if errors:
            raise ValueError(f"cert {sheet.cert}: {agent} memo no longer checks against the rebuilt sheet: "
                             f"{errors[:3]}")


def _unsigned(s: str) -> str:
    return _norm(s).lstrip("+-")


def _flagship_sentences(cert: int, key: str, sheet: FactSheet) -> list[dict]:
    """FLAGSHIP_CARDS text with each number's label and quarter; a number naming a fact must be one of
    that fact's forms (sign aside: "shrank 8.4%"), and a rule-card number must be in the rendered rule."""
    by_label = {f.label: f for f in sheet.facts}
    conc = sheet.extras.get(CONCENTRATION_KEY)
    rendered = "\n".join(render_concentration(conc)) if conc is not None else ""
    out = []
    for s in FLAGSHIP_CARDS[cert]["cards"][key]:
        nums = []
        for n in s["numbers"]:
            if "fact" in n:
                f = by_label.get(n["fact"])
                if f is None or _unsigned(n["text"]) not in {_unsigned(x) for x in f.forms}:
                    raise ValueError(f"cert {cert} {key} card: {n['text']!r} is not a form of fact {n['fact']!r}")
                nums.append({"text": n["text"], "label": f.label, "quarter": _iso(f.quarter),
                             "explain": n["explain"]})
            else:
                if key == "rule" and n["text"] not in rendered:
                    raise ValueError(f"cert {cert} rule card: {n['text']!r} is not in the rendered rule")
                quarter = n.get("quarter", sheet.as_of.isoformat())
                nums.append({"text": n["text"], "label": n["label"], "quarter": quarter, "explain": n["explain"]})
        out.append({"text": s["text"], "numbers": nums})
    return out


def build_cards(sheet: FactSheet, trace: dict, agents: dict) -> list[dict]:
    facts = {f.id: f for f in sheet.facts}
    flagship = sheet.cert in FLAGSHIP_CARDS
    conc = sheet.extras.get(CONCENTRATION_KEY)
    cards = []
    for key, agent, section_key in CARD_ORDER:
        if agent is not None and not agents[agent]["ran"]:
            continue
        if key == "rule" and conc is None:
            continue
        if flagship:
            sentences = _flagship_sentences(sheet.cert, key, sheet)
        elif key == "rule":
            sentences = rule_sentences(conc)
        else:
            section = memo_section(last_memo(trace, agent), section_key)
            sentences = pick_sentences(section, facts) if section is not None else []
        if sentences:
            cards.append({"key": key, "who": key, "badge": "RULE" if key == "rule" else "AI",
                          "sentences": sentences})
    return cards


def _note_body(note_md: str) -> str:
    """The note without its YAML front matter."""
    if note_md.startswith("---"):
        parts = note_md.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    return note_md


def build_report(ctx, cert: int, as_of: date, trace: dict, note_md: str) -> dict:
    sheet = build_fact_sheet(ctx, cert, as_of)
    check_trace(sheet, trace)
    s = ctx.scored
    row = s[(s["cert"] == cert) & (s["report_date"] == pd.Timestamp(as_of))].iloc[0]
    agents = slim_trace(trace)["agents"]
    title = FLAGSHIP_CARDS[cert]["headline"] if cert in FLAGSHIP_CARDS else headline(sheet.outcome.kind, sheet.name)
    return {
        "cert": cert,
        "name": sheet.name,
        "as_of": as_of.isoformat(),
        "outcome": sheet.outcome.kind,
        "failure_date": _iso(sheet.outcome.failure_date),
        "rank": int(row["rank"]),
        "n_banks": int(row["n_banks"]),
        "percentile": float(row["percentile"]),
        "flagged": bool(row["flagged"]),
        "headline": title,
        "cards": build_cards(sheet, trace, agents),
        "agents": agents,
        "facts": [fact_dict(f) for f in sheet.facts],
        "note_md": _note_body(note_md),
    }


def write_reports(ctx, notes_dir: Path, trace_dir: Path, out: Path) -> list[int]:
    """Write reports/<cert>.json for every note with a passing trace (the same set as banks.has_report);
    old report files are removed first. Returns the certs written, sorted."""
    certs = showcase_certs(notes_dir, trace_dir)
    rdir = Path(out) / "reports"
    rdir.mkdir(parents=True, exist_ok=True)
    for old in rdir.glob("*.json"):
        old.unlink()
    written = []
    for note in sorted(Path(notes_dir).glob("*.md")):
        text = note.read_text(encoding="utf-8")
        key = note_key(text)
        if key is None or int(key[0]) not in certs:
            continue
        trace = json.loads((Path(trace_dir) / f"{key[0]}_{key[1]}.json").read_text(encoding="utf-8"))
        report = build_report(ctx, int(key[0]), date.fromisoformat(key[1]), trace, text)
        (rdir / f"{int(key[0])}.json").write_text(json.dumps(report, default=_json_default), encoding="utf-8")
        written.append(int(key[0]))
    return sorted(written)
