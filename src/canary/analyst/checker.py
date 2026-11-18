"""Citation checker (spec 4, 5.5): refuses a memo containing a number not supported by its cited facts.

Memo shape: {"sections": [{"key", "paragraphs": [{"sentences": [{"text", "cites": [fact ids]}]}]}]}.
Tokens are compared only against the normalized forms of the facts cited in the same sentence. A bare
year passes only if it equals the year of a cited fact's date. Spelled number words are not checked.
"""

import re

from canary.analyst.facts import FactSheet
from canary.analyst.sections import Section

_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
_TOKEN = re.compile(
    rf"""
    (?P<iso>(?<![\w.])\d{{4}}-\d{{2}}-\d{{2}}(?![\w]))
  | (?P<quarter>(?<![\w.])Q[1-4]\s+\d{{4}}(?!\d))
  | (?P<mdy>\b(?:{_MONTHS})\s+\d{{1,2}},\s+\d{{4}}(?!\d))
  | (?P<num>(?<![\w.])[-+]?\$?\#?\d[\d,]*(?:\.\d+)?(?:%|x\b|\s(?:billion|million)\b|(?:st|nd|rd|th)\b)?)
    """,
    re.VERBOSE | re.IGNORECASE,
)
_YEAR = re.compile(r"(19|20)\d\d")
_EDGE = " .,;:!?()[]\"'"


def _norm(s: str) -> str:
    s = re.sub(r"\s+", " ", s.replace(",", "").lower())
    return s.strip(_EDGE)


def extract_tokens(text: str) -> list[str]:
    out = []
    for m in _TOKEN.finditer(text):
        tok = _norm(m.group(0))
        if tok.endswith("-"):
            continue
        out.append(tok)
    return out


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
    tokens = extract_tokens(text)
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
    if tokens and not cites:
        errors.append(f"{where}: contains a number ({tokens[0]}) but has no cites")
        return errors
    forms = {_norm(x) for f in cited for x in f.forms}
    years = {str(f.quarter.year) for f in cited if f.quarter is not None}
    for tok in tokens:
        ok = tok in years if _YEAR.fullmatch(tok) else tok in forms
        if not ok:
            errors.append(f"{where}: '{tok}' is not supported by cited facts {', '.join(cites)}")
    return errors
