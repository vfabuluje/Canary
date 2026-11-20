"""The report replay ("loading screen") and report screen (spec 5.5): the v6 engine as a data-driven page.

`replay_html` inlines web/replay.css, web/sprites.js and web/replay.js with a JSON payload built here
from one report dict (dashboard/data/reports/<cert>.json). Every figure on screen comes from that dict;
the fixed captions and role lines below contain none. The page runs in an iframe that sizes itself to
its content, scales the 640 x 300 scene to the container width and stacks the side panel below 700 px.
"""

import html
import json
from datetime import date
from pathlib import Path
from typing import Literal

import streamlit as st

from canary.analyst.concentration import BOTH_CROSSED, L1_CROSSED, L2_CROSSED
from canary.dashboard.charts import quarter_label

WEB = Path(__file__).parent / "web"
SCENE_MS = 5500
MEMBERS = ("rule", "trend", "peer", "check", "lead")
CASTS = ("detective", "basketball")
# Standard uses the detective cast on the grey page (spec 4).
CAST_FOR_THEME = {"standard": "detective", "detective": "detective", "basketball": "basketball"}

TEAM = {
    "detective": {"rule": "The Rule Stamp", "trend": "Trend Detective", "peer": "Peer Detective",
                  "check": "The Fact Checker", "lead": "Lead Detective"},
    "basketball": {"rule": "The Referee", "trend": "Trend Player #5", "peer": "Peer Player #13",
                   "check": "Replay Review", "lead": "Captain #23"},
}
BADGE = {"rule": "RULE", "trend": "AI", "peer": "AI", "check": "RULE", "lead": "AI"}
ROLE = {
    "rule": "Checks one fixed rule: did the bank lend too much on commercial buildings? Just math.",
    "trend": "Looks at how this bank's own numbers changed over the last few years.",
    "peer": "Compares the bank with similar banks to see what's normal for a bank like it.",
    "check": "Makes sure every number the AI helpers wrote really comes from the bank's data.",
    "lead": "Reads everything and writes the summary. If findings disagree, must say so.",
}
BENCH = "not enough similar banks to compare"
DONE = "Done ✓"

CARD_MEMBER = {"trend": "trend", "peer": "peer", "rule": "rule", "summary": "lead"}
CARD_TITLE = {"trend": "How its numbers changed", "peer": "Compared with similar banks",
              "rule": "The building-loan rule", "summary": "The summary"}

TEXT = {
    "building": "Building Canary's report on",
    "panel": "WHO'S ON NOW",
    "legend_ai": "an AI helper that writes in plain English",
    "legend_rule": "plain computer code following a fixed rule",
    "see": "SEE THE REPORT ▶",
    "skip": "Skip to the report",
    "watch": "▶ Watch how it was made",
    "short": "THE SHORT VERSION",
    "after_label": "What happened next:",
    "found_by": "Found by",
    "checked_ai": "✓ Every number fact-checked",
    "checked_rule": "✓ Plain math, no AI",
    "real": "✓ real",
    "checked_summary": "✓ every sentence checked",
    "bench_sign": "ON THE BENCH",
    "bench_card": "sat this one out: " + BENCH + ".",
    "swish": "SWISH!",
    "foot": ("Every number above was checked against the bank's government data before it was saved. "
             "**Hover or tap** a highlighted number for what it means."),
    "close": "Close",
}

STAMP_WORD = {"ok": "NO WARNING", "warn": "LINE CROSSED", "cant": "CAN'T CHECK", "none": "NO RULE DATA"}
CROSSED = (BOTH_CROSSED, L1_CROSSED, L2_CROSSED)
CANT = "can't be checked"

OUTCOME_AFTER = {"caught": "Canary flagged it before it failed.", "missed": "Canary did not flag it in time."}


# ----------------------------------------------------------------------------------------------- scenes
def _ran(report: dict, agent: str) -> bool:
    return bool(report["agents"].get(agent, {}).get("ran"))


def _retry(report: dict, agent: str, label: str) -> str | None:
    """"sent back once, fixed" when the trace shows that agent needed a second attempt."""
    a = report["agents"].get(agent, {})
    n = int(a.get("attempts", 0))
    if not a.get("ran") or n < 2:
        return None
    return f"{label}: sent back {'once' if n == 2 else f'{n - 1} times'}, fixed"


def _peer_count(report: dict) -> str | None:
    return next((f["display"] for f in report.get("facts", []) if f.get("kind") == "peer_count"), None)


def _both(line) -> dict[str, str]:
    """A caption for each cast, from a function of that cast's team names."""
    return {cast: line(TEAM[cast]) for cast in CASTS}


def scenes(report: dict) -> list[dict]:
    """The six replay scenes in pipeline order, with who is working and any retry or bench note."""
    benched = not _ran(report, "peer")
    specialist_notes = [n for n in (_retry(report, "trend", "Trend's section"), _retry(report, "peer", "Peer's section")) if n]
    lead_note = _retry(report, "analyst", "The summary")
    retried = bool(specialist_notes or lead_note)
    peers = _peer_count(report)

    if benched:
        specialists = {
            "now": "One AI helper investigates. Peer sits this one out.",
            "who": _both(lambda t: f"{t['trend']} studies how the bank changed"),
            "active": ["trend"],
            "note": f"Peer is on the bench: {BENCH}.",
            "doing": {"trend": "Now: studying how this bank's numbers changed", "peer": f"On the bench: {BENCH}"},
        }
    else:
        specialists = {
            "now": "Two AI helpers investigate at the same time.",
            "who": _both(lambda t: f"{t['trend']} studies how the bank changed · {t['peer']} compares it with similar banks"),
            "active": ["trend", "peer"],
            "note": None,
            "doing": {"trend": "Now: studying how this bank's numbers changed",
                      "peer": f"Now: comparing it with a group of {peers} similar banks" if peers
                      else "Now: comparing it with similar banks"},
        }
    done_doing = {m: DONE for m in MEMBERS}
    if benched:
        done_doing["peer"] = f"Sat out: {BENCH}"
    return [
        {"key": "numbers", "now": "Gathering the bank's numbers from public government data…",
         "who": _both(lambda t: "No AI yet: just collecting the facts."), "active": [], "note": None, "doing": {}},
        {"key": "rule", "now": "Checking one simple rule: did the bank lend too much on commercial buildings?",
         "who": _both(lambda t: f"{t['rule']} · plain math, not AI"), "active": ["rule"], "note": None,
         "doing": {"rule": "Now: checking the building-loan rule"}},
        {"key": "specialists", **specialists},
        {"key": "check", "now": "Making sure every number the AI wrote is real…",
         "who": _both(lambda t: f"{t['check']} · plain code, not AI"), "active": ["check"],
         "note": " · ".join(specialist_notes) or None, "doing": {"check": "Now: checking every number"}},
        {"key": "lead", "now": "Writing the summary from everything found, then checking it…",
         "who": _both(lambda t: f"{t['lead']} writes the summary (AI) · then {t['check']} checks it (plain code)"),
         "active": ["lead", "check"], "note": lead_note,
         "doing": {"lead": "Now: writing the summary", "check": "Next: checking the summary"}},
        {"key": "done", "now": "Report ready!",
         "who": _both(lambda t: "Every number checked. " + ("Anything that failed a check was sent back and fixed."
                                                            if retried else "Nothing had to be redone.")),
         "active": [m for m in MEMBERS if not (benched and m == "peer")], "note": None, "doing": done_doing},
    ]


# ------------------------------------------------------------------------------------------ the payload
def _card(report: dict, key: str) -> dict | None:
    return next((c for c in report["cards"] if c["key"] == key), None)


def _numbers(card: dict | None) -> list[str]:
    seen: list[str] = []
    for s in card["sentences"] if card else []:
        for n in s["numbers"]:
            if n["text"] not in seen:
                seen.append(n["text"])
    return seen


def _specialist_numbers(report: dict, n: int = 4) -> list[str]:
    """Up to n numbers for the check scene, alternating Trend's and Peer's."""
    trend, peer = _numbers(_card(report, "trend")), _numbers(_card(report, "peer"))
    mixed = [x for pair in zip(trend, peer) for x in pair] + trend[len(peer):] + peer[len(trend):]
    return list(dict.fromkeys(mixed))[:n]


def _stamp(report: dict) -> dict:
    """The rule scene's stamp, read from the bank's own rule card (its real concentration result)."""
    card = _card(report, "rule")
    if card is None:
        return {"kind": "none", "word": STAMP_WORD["none"], "lines": []}
    texts = [s["text"] for s in card["sentences"]]
    with_numbers = [s["text"] for s in card["sentences"] if s["numbers"]]
    cant = [t for t in texts if CANT in t]
    if any(t in CROSSED for t in texts):
        kind = "warn"
    elif cant and not with_numbers:
        kind = "cant"
    else:
        kind = "ok"
    lines = (cant + with_numbers)[:2]
    return {"kind": kind, "word": STAMP_WORD[kind], "lines": lines}


def _quarter(day: str | None) -> str | None:
    return quarter_label(day) if day else None


def _as_of_phrase(day: str) -> str:
    d = date.fromisoformat(day)
    return f"the end of {d.year}" if d.month == 12 else quarter_label(day)


def _ordinal(n: int) -> str:
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n:,}{suffix}"


def _long_date(day: str) -> str:
    d = date.fromisoformat(day)
    return f"{d:%B} {d.day}, {d.year}"


def _sentence(s: dict) -> dict:
    return {"text": s["text"], "numbers": [{"text": n["text"], "explain": n["explain"], "label": n["label"],
                                            "when": _quarter(n.get("quarter"))} for n in s["numbers"]]}


def _report_screen(report: dict) -> dict:
    name, quarter = report["name"], quarter_label(report["as_of"])
    rank, n = _ordinal(int(report["rank"])), f"{int(report['n_banks']):,}"
    riskier = round(float(report["percentile"]))
    rank_line = {
        "text": f"Canary ranked it {rank} riskiest of {n} banks that quarter."
                + (" That put it on the watchlist." if report["flagged"] else ""),
        "numbers": [
            {"text": rank, "label": "National rank (1 = riskiest)", "when": quarter,
             "explain": f"Canary's model ranks every US bank by risk each quarter; #1 is the riskiest. "
                        f"{name} was {rank}: riskier than about {riskier}% of banks."},
            {"text": n, "label": "Banks ranked that quarter", "when": quarter,
             "explain": f"{n} banks were ranked that quarter."},
        ],
    }
    after = None
    if report.get("failure_date"):
        after = " ".join(x for x in (f"{name} failed on {_long_date(report['failure_date'])}.",
                                     OUTCOME_AFTER.get(report["outcome"])) if x)
    cards = [{"key": c["key"], "member": CARD_MEMBER[c["key"]], "title": CARD_TITLE[c["key"]], "badge": c["badge"],
              "wide": c["key"] == "summary", "sentences": [_sentence(s) for s in c["sentences"]]}
             for c in report["cards"]]
    return {"as_of": f"Canary's report, using the bank's numbers from {_as_of_phrase(report['as_of'])}.",
            "headline": report["headline"], "rank": rank_line, "after": after, "cards": cards}


def payload(report: dict, theme: str) -> dict:
    cast = CAST_FOR_THEME.get(theme, "detective")
    summary_numbers = _numbers(_card(report, "summary"))
    papers = [f"RANK {int(report['rank']):,}", "DEPOSITS", "BONDS", "LOANS", "CAPITAL"]
    papers += summary_numbers[:1] + ["…"]
    return {
        "theme": theme,
        "cast": cast,
        "name": report["name"],
        "scene_ms": SCENE_MS,
        "team": {m: {"name": TEAM[cast][m], "badge": BADGE[m], "role": ROLE[m]} for m in MEMBERS},
        "scenes": scenes(report),
        "bench": not _ran(report, "peer"),
        "papers": papers,
        "stamp": _stamp(report),
        "checks": {"specialists": _specialist_numbers(report),
                   "summary": summary_numbers[:3]},
        "report": _report_screen(report),
        "text": TEXT,
    }


# ----------------------------------------------------------------------------------------------- page
PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Canary report replay</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body class="t-{theme}">
<div class="wrap">
  <section id="loading">
    <div class="pix building">{building}</div><div class="bankname">{name}</div>
    <div class="stagewrap"><div>
      <div class="scene {cast}" id="scene"><div class="stage" id="stage"></div></div>
      <div class="caps"><div class="now" id="now"></div><div class="who" id="who"></div><div class="noteline" id="noteline"></div>
        <div class="bar" id="bar"></div>
        <button class="btn big" id="see" style="visibility:hidden">{see}</button><br>
        <button class="skip" id="skip">{skip}</button></div>
    </div>
    <aside class="team"><h2 class="pix">{panel}</h2><div id="members"></div>
      <div class="legend"><span class="tag ai">AI</span> {legend_ai}<br><span class="tag rule">RULE</span> {legend_rule}</div></aside>
    </div>
  </section>
  <section id="report">
    <div class="rhead"><div><h1 class="pix">{name}</h1><p id="asof"></p></div><button class="btn" id="watch">{watch}</button></div>
    <div class="verdict"><div class="label">{short}</div><div class="big" id="headline"></div>
      <div class="small" id="rankline"></div><div class="after" id="after"></div></div>
    <div class="grid" id="grid"></div>
    <div class="foot" id="foot"></div>
  </section>
</div>
<div id="tip" role="tooltip"></div>
<script>window.CANARY = {data};
</script>
<script>{sprites}</script>
<script>{engine}</script>
</body></html>
"""


def _json_for_script(obj) -> str:
    """JSON safe inside <script>: '<' is escaped so no string can close the tag."""
    return json.dumps(obj, ensure_ascii=False).replace("<", "\\u003c")


def replay_html(report: dict, theme: str) -> str:
    """The self-contained replay + report page for one showcase bank in `theme`."""
    data = payload(report, theme)
    esc = html.escape
    return PAGE.format(
        css=(WEB / "replay.css").read_text(encoding="utf-8"),
        sprites=(WEB / "sprites.js").read_text(encoding="utf-8"),
        engine=(WEB / "replay.js").read_text(encoding="utf-8"),
        data=_json_for_script(data), theme=esc(data["theme"]), cast=esc(data["cast"]), name=esc(report["name"]),
        **{k: esc(v) for k, v in TEXT.items() if k in {"building", "panel", "legend_ai", "legend_rule", "see",
                                                        "skip", "watch", "short"}},
    )


def render_replay(report: dict, theme: str, height: int | Literal["content"] = "content") -> None:
    """Draw the replay in an iframe. By default the frame grows and shrinks with its content (the stacked
    phone layout and the report screen are taller than the desktop replay)."""
    st.iframe(replay_html(report, theme), height=height, alt=f"How Canary built its report on {report['name']}")
