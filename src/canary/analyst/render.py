"""Note renderer (spec 5.2, 5.3): FactSheet + checked memo -> Obsidian Markdown.

Everything not written by Claude (banner, tables, fixed sentence, sources) comes from the
FactSheet and Outcome, never from the memo.
"""

import json
import re
from datetime import date
from pathlib import Path

import pandas as pd

from canary.analyst.facts import FactSheet
from canary.analyst.sections import Section

SCORE_SENTENCE = (
    "The score ranks banks against each other; it is not a probability of failure, "
    "because the model was trained with extra weight on banks that failed."
)
AFTER_WINDOW = "*After the test window: not part of the reported 2016-2024 results.*"
_UNSAFE = re.compile(r'[/\\:*?"<>|#^\[\]]')
_CITE = re.compile(r"\s*\[F\d+\]")


def note_path(out_dir: Path, name: str, cert: int) -> Path:
    safe = _UNSAFE.sub("-", name.title())
    return out_dir / f"{safe} ({cert}).md"


def _d(ts) -> str:
    return pd.Timestamp(ts).date().isoformat()


def _yaml(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, date):
        return v.isoformat()
    if isinstance(v, (int, float)):
        return repr(v)
    return json.dumps(str(v), ensure_ascii=False)  # JSON strings are valid YAML


def _percentile(sheet: FactSheet):
    for f in sheet.facts:
        if f.label.startswith("Percentile"):
            return float(f.value)
    return None


def _front_matter(sheet: FactSheet, meta: dict) -> str:
    row = sheet.history[sheet.history["report_date"] == pd.Timestamp(sheet.as_of)]
    r = row.iloc[-1] if len(row) else None
    o = sheet.outcome
    fields = [
        ("cert", sheet.cert), ("name", sheet.name), ("as_of", sheet.as_of),
        ("rank", int(r["rank"]) if r is not None else None),
        ("n_banks", int(r["n_banks"]) if r is not None else None),
        ("percentile", _percentile(sheet)),
        ("flagged", bool(r["flagged"]) if r is not None else None),
        ("outcome", o.kind), ("after_test_window", o.after_test_window),
        ("failure_date", o.failure_date), ("model_run", meta["model_run"]),
        ("written_at", meta["written_at"]), ("writer_model", meta["writer_model"]),
        ("checked", True),
    ]
    return "---\n" + "".join(f"{k}: {_yaml(v)}\n" for k, v in fields) + "---\n"


def _banner(sheet: FactSheet) -> list[str]:
    o = sheet.outcome
    lines = []
    if o.kind == "caught":
        n = o.lead_quarters
        lines.append(f"*Hindsight: failed {o.failure_date.isoformat()}. "
                     f"Canary flagged it {n} quarter{'' if n == 1 else 's'} ahead.*")
    elif o.kind == "missed":
        lines.append(f"*Hindsight: failed {o.failure_date.isoformat()}. Canary did not flag it.*")
    elif o.kind == "false_alarm":
        lines.append(f"*Hindsight: flagged, but had not failed as of {o.last_report.isoformat()}.*")
    elif o.kind == "open_watchlist":
        lines.append("*Outcome not yet known.*")
    if o.after_test_window:
        lines.append(AFTER_WINDOW)
    return lines


def _table(df: pd.DataFrame, first_flag: date | None) -> list[str]:
    out = ["| Quarter | Rank | Of | Watchlist |", "|---|---|---|---|"]
    for _, r in df.sort_values("report_date").iterrows():
        d = _d(r["report_date"])
        mark = "▲ watchlist" if bool(r["flagged"]) else ""
        if first_flag is not None and d == first_flag.isoformat():
            mark = (mark + " (first flag)").strip()
        out.append(f"| {d} | {int(r['rank']):,} | {int(r['n_banks']):,} | {mark} |")
    return out


def _paragraphs(memo_sec: dict) -> list[str]:
    paras = []
    for p in memo_sec["paragraphs"]:
        text = " ".join(_CITE.sub("", s["text"]).strip() for s in p["sentences"])
        paras.append(text)
    return paras


def _cited(memo: dict) -> set[str]:
    return {c for s in memo["sections"] for p in s["paragraphs"] for sent in p["sentences"] for c in sent["cites"]}


def render_note(sheet: FactSheet, memo: dict, sections: list[Section], meta: dict) -> str:
    by_key = {s["key"]: s for s in memo["sections"]}
    out = [_front_matter(sheet, meta), f"# {sheet.name} (cert {sheet.cert})", ""]
    banner = _banner(sheet)
    if banner:
        out += banner + [""]
    for sec in sections:
        out += [f"## {sec.title}", ""]
        if sec.key == "score_history":
            out += _table(sheet.history, sheet.outcome.first_flag) + [""]
            continue
        if sec.key == "sources":
            ids = _cited(memo)
            facts = sorted((f for f in sheet.facts if f.id in ids), key=lambda f: int(f.id[1:]))
            for f in facts:
                q = f.quarter.isoformat() if f.quarter else "n/a"
                out.append(f"- {f.id} · {f.label} · {q} · {f.display} · {f.source}")
            out.append("")
            continue
        if sec.key in by_key:
            for p in _paragraphs(by_key[sec.key]):
                out += [p, ""]
        if sec.key == "score":
            out += [SCORE_SENTENCE, "", "**What the model can't see.** " + sheet.cant_see, ""]
        if sec.key == "what_next" and len(sheet.after_history):
            out += _table(sheet.after_history, sheet.outcome.first_flag) + [""]
    return "\n".join(out).rstrip() + "\n"
