"""Citation checker (spec 4, 5.5): refuses a memo containing a number not supported by its cited facts.

Memo shape: {"sections": [{"key", "paragraphs": [{"sentences": [{"text", "cites": [fact ids]}]}]}]}.
Tokens are compared only against the normalized forms of the facts cited in the same sentence. A bare
year (or FY2022) passes only if it equals the year of a cited fact's date. Month names, lowercase or
abbreviated (Dec, Sept.), must match a cited date; a lone capitalised "May" is ignored. Spelled time
spans ("four quarters", "a year") must match a cited fact's forms; other spelled counts ("five
drivers") are not checked, nor is the exact post-hoc label text (it names 2023 as wording, not as a
figure). A sentence citing a post-hoc fact must contain the post-hoc label. Phrase guards (ruling R12):
probability-of-failure wording anywhere; "failed", "collapsed", "was closed", "was seized" in as-of
sections.
"""

import re
from dataclasses import dataclass

from canary.analyst.facts import POSTHOC_LABEL, SPELLED_WORDS, FactSheet, date_forms, spelled_norm
from canary.analyst.labels import PLAIN_NAMES
from canary.analyst.sections import Section

_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
_MONTH_NO = {m[:3].lower(): i for i, m in enumerate(_MONTHS.split("|"), 1)}
# Capitalised full names, lowercase full names (not "may", a verb), and three-letter abbreviations
# (plus "Sept"); full names come first so the alternation never stops at a prefix.
_MONTH_RE = "|".join(
    _MONTHS.split("|")
    + [m.lower() for m in _MONTHS.split("|") if m != "May"]
    + ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sept", "Sep", "Oct", "Nov", "Dec"]
)
_TOKEN = re.compile(
    rf"""
    (?P<spelled>\b(?i:(?P<sw>{SPELLED_WORDS}))\s+(?i:(?P<su>quarters?|years?))\b)
  | (?P<fy>\bFY\s?(?P<fy_y>\d{{4}})(?!\d))
  | (?P<iso>(?<![\w.])\d{{4}}-\d{{2}}-\d{{2}}(?!\w))
  | (?P<yq>(?<![\w.])(?P<yq_y>\d{{4}})\s*[Qq](?P<yq_q>[1-4])\b)
  | (?P<qtr>\b[Qq](?P<q>[1-4])\b(?:(?:\s+of\s+|\s*[-,]?\s*)(?P<qy>\d{{4}})(?!\d))?)
  | (?P<mon>\b(?P<m>{_MONTH_RE})\b\.?(?:\s+(?P<d>\d{{1,2}})(?!\d))?(?:,?\s+(?P<y>\d{{4}})(?!\d))?)
  | (?P<num>(?<![\w.])(?:US)?[-+]?\$?\#?\d[\d,]*(?:\.\d+)?
       (?:%|(?:st|nd|rd|th)\b|\s(?:billion|million|trillion|thousand|bps|bp)\b|[A-Za-z]+\b)?)
    """,
    re.VERBOSE,
)


def _term_pattern() -> re.Pattern:
    """Fixed term names from PLAIN_NAMES whose digits are wording, not figures (ruling R17):
    "Tier 1" (also Tier 2), "30-89 days" (en dash too), "90+ days" and its spoken forms
    "90 or more days" / "90 days or more". Exact phrases only, case-insensitive."""
    phrases: set[str] = set()
    for name in PLAIN_NAMES.values():
        for m in re.finditer(r"\b[Tt]ier\s+\d\b|\b\d+(?:[-\u2013]\d+|\+)\s+days\b", name):
            phrases.add(m.group(0))
            # Spoken synonyms of an "N+ days" term, derived from the same PLAIN_NAMES phrase.
            plus = re.fullmatch(r"(\d+)\+\s+days", m.group(0))
            if plus:
                phrases.add(f"{plus.group(1)} or more days")
                phrases.add(f"{plus.group(1)} days or more")
    alts = []
    for ph in sorted(phrases):
        if ph.lower().startswith("tier"):
            alts.append(r"\bTier\s+[12](?!\s?\.?\d)")  # Tier 1 is the listed term; Tier 2 is its sibling
        else:
            alts.append(r"(?<![\w.])" + re.sub(r"\\[-\u2013]", "[-\u2013]", re.escape(ph)).replace(r"\ ", r"\s+"))
    return re.compile("|".join(dict.fromkeys(alts)), re.IGNORECASE)


_TERMS = _term_pattern()
_EDGE = " .,;:!?()[]\"'"
_PROBABILITY = re.compile(
    r"\b(?:chance|probability|likelihood)\s+of\s+(?:failing|failure|fail)\b|\d+(?:\.\d+)?%\s+chance\b",
    re.IGNORECASE)
# The one allowed disclaimer (ruling R15): "not a/the probability|likelihood of failure|failing".
# Never "chance", never "N% chance", never after "no" or "never".
_DISCLAIMER = re.compile(r"\bnot\s+(?:a|the)\s+(?:probability|likelihood)\s+of\s+(?:failure|failing)\b",
                         re.IGNORECASE)
_AS_OF_WORDS = re.compile(r"\b(?:failed|collapsed)\b|\bwas\s+(?:closed|seized)\b", re.IGNORECASE)


@dataclass
class _Tok:
    raw: str
    norm: str
    kind: str  # "date" (iso/quarter/month), "num"
    q: int | None = None
    month: int | None = None
    day: int | None = None
    year: int | None = None


def _norm(s: str) -> str:
    s = re.sub(r"\s+", " ", s.replace(",", "").lower())
    return s.strip(_EDGE)


def _tokens(text: str) -> list[_Tok]:
    text = _TERMS.sub(" ", text)
    text = text.replace("\u2212", "-").replace("\u2013", "-").replace("\u00d7", "x")
    out = []
    for m in _TOKEN.finditer(text):
        raw = m.group(0)
        if m.group("spelled"):
            out.append(_Tok(raw, spelled_norm(m.group("sw"), m.group("su")), "num"))
        elif m.group("fy"):
            out.append(_Tok(raw, _norm(raw), "date", year=int(m.group("fy_y"))))
        elif m.group("iso"):
            y, mo, d = (int(x) for x in raw.split("-"))
            out.append(_Tok(raw, _norm(raw), "date", month=mo, day=d, year=y))
        elif m.group("yq"):
            q, y = int(m.group("yq_q")), int(m.group("yq_y"))
            out.append(_Tok(raw, f"q{q} {y}", "date", q=q, year=y))
        elif m.group("qtr"):
            q = int(m.group("q"))
            y = int(m.group("qy")) if m.group("qy") else None
            out.append(_Tok(raw, f"q{q}" + (f" {y}" if y else ""), "date", q=q, year=y))
        elif m.group("mon"):
            if m.group("m") == "May" and not (m.group("d") or m.group("y")):
                continue
            d = int(m.group("d")) if m.group("d") else None
            y = int(m.group("y")) if m.group("y") else None
            out.append(_Tok(raw, _norm(raw), "date", month=_MONTH_NO[m.group("m")[:3].lower()], day=d, year=y))
        else:
            norm = _norm(raw)
            if norm.endswith("-"):
                continue
            out.append(_Tok(raw.strip(_EDGE), norm, "num"))
    return out


def extract_tokens(text: str) -> list[str]:
    return [t.norm for t in _tokens(text)]


def _clip(s: str, n: int = 100) -> str:
    return s if len(s) <= n else s[: n - 3] + "..."


def check_memo(memo: dict, sheet: FactSheet, sections: list[Section]) -> list[str]:
    errors: list[str] = []
    expected = {s.key: s for s in sections}
    seen: set[str] = set()
    facts = {f.id: f for f in sheet.facts}
    for sec in memo.get("sections", []):
        key = sec.get("key")
        if key in seen:
            errors.append(f"section '{key}': duplicate section")
        seen.add(key)
        spec = expected.get(key)
        if spec is None:
            errors.append(f"section '{key}': unexpected section key")
            continue
        for para in sec.get("paragraphs", []):
            for sent in para.get("sentences", []):
                errors.extend(_check_sentence(key, spec, sent, facts))
    for key in expected:
        if key not in seen:
            errors.append(f"section '{key}': missing section")
    return errors


def _check_sentence(key, spec, sent, facts) -> list[str]:
    text = sent.get("text", "")
    cites = sent.get("cites") or []
    where = f"section '{key}', sentence \"{_clip(text)}\""
    # The required post-hoc label contains "2023"; it is fixed wording, not a figure to check.
    tokens = _tokens(text.replace(POSTHOC_LABEL, " "))
    errors = []
    cited = []
    for cid in cites:
        f = facts.get(cid)
        if f is None:
            errors.append(f"{where}: unknown fact id {cid}")
            continue
        if f.hindsight and spec.window == "as_of":
            errors.append(f"{where}: cites hindsight fact {cid} ({f.label}) in an as-of section")
        cited.append(f)
    allowed = {d.end() for d in _DISCLAIMER.finditer(text)}
    for m in _PROBABILITY.finditer(text):
        if m.end() not in allowed:
            errors.append(f"{where}: describes the score as a probability of failure ('{m.group(0)}')")
    if spec.window == "as_of":
        for m in _AS_OF_WORDS.finditer(text):
            errors.append(f"{where}: '{m.group(0)}' in an as-of section (says or hints at what happened later)")
    if any(POSTHOC_LABEL in f.label for f in cited) and POSTHOC_LABEL not in text:
        errors.append(f"{where}: cites a post-hoc fact but does not include the label \"{POSTHOC_LABEL}\"")
    if tokens and not cites:
        errors.append(f"{where}: contains a number ({tokens[0].norm}) but has no cites")
        return errors
    all_forms = {_norm(x) for f in cited for x in f.forms}
    # Forms that are not date renderings: a count/rank/amount form, never a calendar year.
    plain = {_norm(x) for f in cited for x in f.forms
             if f.quarter is None or x not in date_forms(f.quarter)}
    dates = [f.quarter for f in cited if f.quarter is not None]
    years = {str(d.year) for d in dates}
    for tok in tokens:
        if tok.kind == "date":
            ok = tok.norm in all_forms or any(
                (tok.q is None or (d.month - 1) // 3 + 1 == tok.q)
                and (tok.month is None or d.month == tok.month)
                and (tok.day is None or d.day == tok.day)
                and (tok.year is None or d.year == tok.year)
                for d in dates
            )
        elif re.fullmatch(r"\d{4}", tok.raw):
            ok = tok.norm in years or tok.norm in plain
        else:
            ok = tok.norm in plain
        if not ok:
            errors.append(f"{where}: '{tok.raw}' is not supported by cited facts {', '.join(cites)}")
    return errors
