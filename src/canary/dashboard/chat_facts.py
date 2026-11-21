"""Ask Canary's read-only lookup tools and the per-visit fact ledger.

Every number a tool hands the model is also issued as a fact (id F1, F2, ... across the whole visit) with the
spellings the answer checker accepts, so a later step can verify each number in the model's answer against the
facts the tools actually returned. Tools never raise: bad input comes back as {"error": ...}.
"""

import re
from dataclasses import asdict
from datetime import date

import pandas as pd

from canary.analyst.facts import Fact, count_forms, date_forms, decimal_ordinal_forms, ordinal
from canary.dashboard import copy, data
from canary.dashboard.search import _status, search

MAX_ROWS = 25
MAX_QUARTERS = 12
MAX_MATCHES = 8
WATCHLIST_SHARE_PCT = 2  # the flag rule: top 2% of banks each quarter (canary.model.metrics.WATCHLIST_SHARE)
_SRC = "dashboard/data"
_QUARTER = re.compile(r"^\s*Q([1-4])\s+(\d{4})\s*$", re.IGNORECASE)
_SLIM_KEYS = ("id", "label", "quarter", "display", "hindsight")


def _iso(d) -> str | None:
    return None if d is None else d.isoformat()


class FactLedger:
    """Every fact issued this visit, numbered across tools."""

    def __init__(self) -> None:
        self.facts: dict[str, Fact] = {}
        self.bank_of: dict[str, tuple[int, str]] = {}
        self.report_ids: dict[str, str] = {}  # ledger id -> the report's original fact id

    def _next_id(self) -> str:
        return f"F{len(self.facts) + 1}"

    def add(self, label, value, display, forms, source, quarter=None, hindsight=False, cert=None, bank=None) -> Fact:
        forms = list(forms) + (date_forms(quarter) if quarter else [])
        fact = Fact(self._next_id(), label, quarter, value, display, list(dict.fromkeys(forms)), hindsight, source)
        self.facts[fact.id] = fact
        if cert is not None:
            self.bank_of[fact.id] = (int(cert), bank or "")
        return fact

    def import_report(self, report: dict) -> list[Fact]:
        """Re-id a written report's facts into this ledger, remembering each original id."""
        out = []
        cert, name = int(report["cert"]), report.get("name", "")
        for f in report["facts"]:
            q = f.get("quarter")
            fact = Fact(self._next_id(), f["label"], date.fromisoformat(q) if q else None, f["value"], f["display"],
                        list(f["forms"]), bool(f["hindsight"]), f["source"], f.get("feature"), f.get("kind"))
            self.facts[fact.id] = fact
            self.bank_of[fact.id] = (cert, name)
            self.report_ids[fact.id] = f["id"]
            out.append(fact)
        return out

    def facts_for(self, ids) -> list[Fact]:
        return [self.facts[i] for i in ids if i in self.facts]

    def slim(self, facts) -> list[dict]:
        return [{"id": f.id, "label": f.label, "quarter": _iso(f.quarter), "display": f.display,
                 "hindsight": f.hindsight} for f in facts]

    def to_state(self) -> dict:
        facts = []
        for f in self.facts.values():
            d = asdict(f)
            d["quarter"] = _iso(f.quarter)
            facts.append(d)
        return {"facts": facts, "bank_of": {k: list(v) for k, v in self.bank_of.items()},
                "report_ids": dict(self.report_ids)}

    @classmethod
    def from_state(cls, state: dict) -> "FactLedger":
        led = cls()
        for d in state.get("facts", []):
            d = dict(d)
            d["quarter"] = date.fromisoformat(d["quarter"]) if d["quarter"] else None
            led.facts[d["id"]] = Fact(**d)
        led.bank_of = {k: (int(v[0]), v[1]) for k, v in state.get("bank_of", {}).items()}
        led.report_ids = dict(state.get("report_ids", {}))
        return led


# ---- helpers -------------------------------------------------------------------------------------------------

def _num_forms(n: int) -> list[str]:
    return count_forms(n) + [f"#{n:,}", f"#{n}"]


def _pct_forms(p: float) -> list[str]:
    return [f"{p:.1f}%", f"{p:.0f}%", f"{p:.1f}", f"{p:.0f}", ordinal(round(p)), *decimal_ordinal_forms(p)]


def _full_date_forms(d: date) -> list[str]:
    return [d.isoformat(), f"{d:%B} {d.day}, {d.year}", str(d.year)]


def _day(ts) -> date:
    return pd.Timestamp(ts).date()


def _parse_quarter(text: str) -> pd.Timestamp | None:
    m = _QUARTER.match(text or "")
    if m:
        q, y = int(m.group(1)), int(m.group(2))
        return pd.Timestamp(y, q * 3, 30 if q in (2, 3) else 31)
    try:
        return pd.Timestamp(text).normalize() if text and re.match(r"^\d{4}-\d{2}-\d{2}$", text.strip()) else None
    except ValueError:
        return None


def _cert(value) -> int | None:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        return None
    try:
        f = float(value)
    except ValueError:
        return None
    return int(f) if f == int(f) else None


def _bank_row(cert) -> pd.Series | None:
    c = _cert(cert)
    if c is None:
        return None
    b = data.banks()
    hit = b[b["cert"] == c]
    return hit.iloc[0] if len(hit) else None


def _identity(led: FactLedger, row: pd.Series) -> list[Fact]:
    cert, name = int(row["cert"]), row["name"]
    kw = dict(cert=cert, bank=name)
    latest = data.banks()["last_report"].max()
    status = _status(row, latest)
    out = [
        led.add("Bank name", name, name, [name], f"{_SRC}/banks.parquet: name", **kw),
        led.add("Certificate number", cert, str(cert), [str(cert)], f"{_SRC}/banks.parquet: cert", **kw),
        led.add("City", row["city"], str(row["city"]), [str(row["city"])], f"{_SRC}/banks.parquet: city", **kw),
        led.add("State", row["state"], str(row["state"]), [str(row["state"])], f"{_SRC}/banks.parquet: state", **kw),
        led.add("Status", status, status, [status], f"{_SRC}/banks.parquet: failure_date, last_report", **kw),
        led.add("Last quarter reported", _day(row["last_report"]).isoformat(), _day(row["last_report"]).isoformat(),
                [], f"{_SRC}/banks.parquet: last_report", _day(row["last_report"]), **kw),
    ]
    if pd.notna(row["failure_date"]):
        d = _day(row["failure_date"])
        out.append(led.add("Failure date", d.isoformat(), f"{d:%B} {d.day}, {d.year}", _full_date_forms(d),
                           f"{_SRC}/banks.parquet: failure_date", **kw))
    return out


def _score_facts(led: FactLedger, kw: dict, q: date, rank: int, n: int, pct: float, flagged: bool,
                 prefix: str = "") -> list[Fact]:
    src = f"{_SRC}/scores_history.parquet"
    return [
        led.add(f"{prefix}National rank (1 = highest score)", rank, f"{rank:,}", _num_forms(rank), f"{src}: rank", q, **kw),
        led.add(f"{prefix}Banks ranked that quarter", n, f"{n:,}", count_forms(n), f"{src}: n_banks", q, **kw),
        led.add(f"{prefix}Percentile (100 = highest risk)", pct, f"{pct:.1f}%", _pct_forms(pct), f"{src}: percentile", q, **kw),
        led.add(f"{prefix}On the watchlist", "yes" if flagged else "no", "flagged" if flagged else "not flagged",
                [], f"{src}: flagged", q, **kw),
    ]


# ---- tools ---------------------------------------------------------------------------------------------------

def find_bank(ledger: FactLedger, query: str, state: str | None = None) -> dict:
    if not isinstance(query, str) or not query.strip():
        return {"error": "query must be a non-empty bank name."}
    banks = data.banks()
    if state:
        banks = banks[banks["state"] == str(state).upper()].reset_index(drop=True)
    res = search(query, banks, MAX_MATCHES)
    latest = data.banks()["last_report"].max()
    ordered = []
    if res.direct is not None:
        hit = banks[banks["cert"] == res.direct]
        if len(hit):
            ordered.append(hit.iloc[0])
    for s in res.suggestions:
        if s["cert"] != res.direct:
            ordered.append(banks[banks["cert"] == s["cert"]].iloc[0])
    matches, facts = [], []
    for row in ordered[:MAX_MATCHES]:
        cert, name = int(row["cert"]), row["name"]
        kw = dict(cert=cert, bank=name)
        status = _status(row, latest)
        facts += [
            ledger.add("Bank name", name, name, [name], f"{_SRC}/banks.parquet: name", **kw),
            ledger.add("Certificate number", cert, str(cert), [str(cert)], f"{_SRC}/banks.parquet: cert", **kw),
            ledger.add("City", row["city"], str(row["city"]), [str(row["city"])], f"{_SRC}/banks.parquet: city", **kw),
            ledger.add("Status", status, status, [status], f"{_SRC}/banks.parquet: failure_date, last_report", **kw),
        ]
        matches.append({"cert": cert, "name": name, "city": row["city"], "state": row["state"], "status": status,
                        "has_report": bool(row["has_report"])})
    out = {"matches": matches, "facts": ledger.slim(facts)}
    if not matches:
        out["note"] = "No bank matched that name."
    elif res.direct is not None:
        out["opens_directly"] = res.direct
    return out


def bank_profile(ledger: FactLedger, cert: int, start: str | None = None, end: str | None = None) -> dict:
    row = _bank_row(cert)
    if row is None:
        return {"error": f"No bank with certificate number {cert!r}."}
    c, name = int(row["cert"]), row["name"]
    kw = dict(cert=c, bank=name)
    facts = _identity(ledger, row)
    out: dict = {"cert": c, "name": name}
    if not bool(row["scored"]):
        out["note"] = copy.BANK_UNSCORED.format(year=_day(row["last_report"]).year)
        out["facts"] = ledger.slim(facts)
        return out

    lo = hi = None
    if start:
        lo = _parse_quarter(start)
    if end:
        hi = _parse_quarter(end)
    if (start and lo is None) or (end and hi is None):
        return {"error": "start and end must look like 2022-12-31 or Q4 2022."}

    facts += _score_facts(ledger, kw, _day(row["latest_report_date"]), int(row["latest_rank"]), int(row["latest_n"]),
                          float(row["latest_percentile"]), bool(row["latest_flagged"]), "Latest ")
    hist = data.scores_history()
    hist = hist[hist["cert"] == c].sort_values("report_date")
    if lo is not None:
        hist = hist[hist["report_date"] >= lo]
    if hi is not None:
        hist = hist[hist["report_date"] <= hi]
    hist = hist.tail(MAX_QUARTERS)
    rows = []
    for r in hist.itertuples():
        q = _day(r.report_date)
        facts += _score_facts(ledger, kw, q, int(r.rank), int(r.n_banks), float(r.percentile), bool(r.flagged))
        rows.append({"quarter": q.isoformat(), "rank": int(r.rank), "n_banks": int(r.n_banks),
                     "percentile": round(float(r.percentile), 1), "flagged": bool(r.flagged)})
    out["history"] = rows

    conc = data.concentration()
    conc = conc[conc["cert"] == c].sort_values("as_of")
    if len(conc):
        r = conc.iloc[-1]
        q = _day(r["as_of"])
        src = f"{_SRC}/concentration.parquet"
        facts.append(ledger.add("Concentration test used", str(r["measure"]), str(r["measure"]), [str(r["measure"])],
                                f"{src}: measure", q, **kw))
        for label, col in (("Construction loans, % of capital", "construction_pct"),
                           ("Commercial real estate loans, % of capital", "cre_pct"),
                           ("Loan growth over three years, %", "growth_pct")):
            v = r[col]
            if pd.notna(v):
                v = float(v)
                facts.append(ledger.add(label, v, f"{v:.1f}%", [f"{v:.1f}%", f"{v:.0f}%", f"{v:.1f}", f"{v:.0f}"],
                                        f"{src}: {col}", q, **kw))
        if isinstance(r["reason"], str):
            out["concentration_note"] = r["reason"]
    out["facts"] = ledger.slim(facts)
    return out


def bank_report(ledger: FactLedger, cert: int) -> dict:
    c = _cert(cert)
    rep = data.report(c) if c is not None else None
    if rep is None:
        return {"error": "No written report for this bank; use bank_profile."}
    facts = ledger.import_report(rep)
    return {"headline": rep["headline"], "as_of": rep["as_of"], "facts": ledger.slim(facts)}


def failures(ledger: FactLedger, year: int | None = None, state: str | None = None) -> dict:
    b = data.banks()
    b = b[b["failure_date"].notna()]
    if year is None and not state:
        year = int(b["failure_date"].dt.year.max())
    if year is not None:
        y = _cert(year)
        if y is None:
            return {"error": "year must be a four-digit year."}
        b = b[b["failure_date"].dt.year == y]
        year = y
    if state:
        b = b[b["state"] == str(state).upper()]
    b = b.sort_values("failure_date")
    total = len(b)
    shown = b.tail(MAX_ROWS)
    facts = [ledger.add("Number of failed banks in this list", total, f"{total:,}", count_forms(total),
                        f"{_SRC}/banks.parquet: failure_date")]
    if year is not None:
        facts.append(ledger.add("Year shown", year, str(year), [str(year)], f"{_SRC}/banks.parquet: failure_date"))
    rows = []
    for r in shown.itertuples():
        d = _day(r.failure_date)
        kw = dict(cert=r.cert, bank=r.name)
        fs = [ledger.add("Bank name", r.name, r.name, [r.name], f"{_SRC}/banks.parquet: name", **kw),
              ledger.add("Failure date", d.isoformat(), f"{d:%B} {d.day}, {d.year}", _full_date_forms(d),
                         f"{_SRC}/banks.parquet: failure_date", **kw)]
        facts += fs
        rows.append({"cert": int(r.cert), "name": r.name, "city": r.city, "state": r.state,
                     "failure_date": d.isoformat(), "fact_ids": [f.id for f in fs]})
    out = {"total": total, "rows": rows, "facts": ledger.slim(facts)}
    if total > len(rows):
        out["note"] = f"Showing the latest {len(rows)} of {total}."
    return out


def watchlist(ledger: FactLedger, quarter: str | None = None, state: str | None = None) -> dict:
    hist = data.scores_history()
    quarters = sorted(hist["report_date"].unique())
    if quarter is None:
        q = quarters[-1]
    else:
        q = _parse_quarter(quarter)
    if q is None or pd.Timestamp(q) not in set(pd.to_datetime(quarters)):
        return {"error": f"No scores for that quarter. Quarters run from {_day(quarters[0])} to {_day(quarters[-1])}; "
                         "use YYYY-MM-DD or a form like Q4 2022."}
    q = pd.Timestamp(q)
    rows = hist[(hist["report_date"] == q) & hist["flagged"]]
    names = data.banks().set_index("cert")[["name", "state", "city"]]
    rows = rows.join(names, on="cert")
    if state:
        rows = rows[rows["state"] == str(state).upper()]
    rows = rows.sort_values("rank")
    total, qd = len(rows), _day(q)
    facts = [ledger.add("Banks on the watchlist in this list", total, f"{total:,}", count_forms(total),
                        f"{_SRC}/scores_history.parquet: flagged", qd)]
    out_rows = []
    for r in rows.head(MAX_ROWS).itertuples():
        kw = dict(cert=r.cert, bank=r.name)
        fs = [ledger.add("Bank name", r.name, r.name, [r.name], f"{_SRC}/banks.parquet: name", **kw),
              ledger.add("National rank (1 = highest score)", int(r.rank), f"{int(r.rank):,}", _num_forms(int(r.rank)),
                         f"{_SRC}/scores_history.parquet: rank", qd, **kw)]
        facts += fs
        out_rows.append({"cert": int(r.cert), "name": r.name, "state": r.state, "rank": int(r.rank),
                         "n_banks": int(r.n_banks), "fact_ids": [f.id for f in fs]})
    out = {"quarter": qd.isoformat(), "total": total, "rows": out_rows, "facts": ledger.slim(facts)}
    if total > len(out_rows):
        out["note"] = f"Showing the {len(out_rows)} highest-ranked of {total}."
    return out


def canary_facts(ledger: FactLedger) -> dict:
    m = data.metrics()
    src = f"{_SRC}/metrics.json"

    def pct(label, v, key):
        v = float(v) * 100
        return ledger.add(label, v, f"{v:.1f}%", [f"{v:.1f}%", f"{v:.0f}%", f"{v:.1f}", f"{v:.0f}", f"{v / 100:.2f}"],
                          f"{src}: {key}")

    def dec(label, v, key):
        return ledger.add(label, float(v), f"{v:.2f}", [f"{v:.2f}", f"{v:.3f}", f"{v:.1f}"], f"{src}: {key}")

    lead = float(m["lead_time_median"])
    words = {1: "one", 2: "two", 3: "three", 4: "four"}
    lead_forms = [f"{lead:g}", f"{lead:.1f}"] + ([words[int(lead)], f"{words[int(lead)]} quarters"]
                                                 if lead == int(lead) and int(lead) in words else [])
    facts = [
        dec("Ranking score (AUC), 2016-2024 test", m["auc"], "auc"),
        pct("Recall: share of failures flagged at least one quarter early", m["recall"], "recall"),
        ledger.add("Failures caught early", m["banks_caught"], str(m["banks_caught"]), count_forms(m["banks_caught"]),
                   f"{src}: banks_caught"),
        ledger.add("Failures eligible to be caught (2016-2024)", m["eligible_banks"], str(m["eligible_banks"]),
                   count_forms(m["eligible_banks"]), f"{src}: eligible_banks"),
        ledger.add("Median lead time, in quarters", lead, f"{lead:g}", lead_forms, f"{src}: lead_time_median"),
        pct("False-alarm rate: share of flagged banks that did not fail", m["false_alarm_rate"], "false_alarm_rate"),
        dec("Texas-ratio baseline ranking score (AUC)", m["baseline"]["auc"], "baseline.auc"),
        ledger.add("Flag rule: share of banks flagged each quarter", WATCHLIST_SHARE_PCT, f"{WATCHLIST_SHARE_PCT}%",
                   [f"{WATCHLIST_SHARE_PCT}%", str(WATCHLIST_SHARE_PCT), "two percent"],
                   "canary.model.metrics: WATCHLIST_SHARE (fixed)"),
    ]
    banks = data.banks().set_index("cert")
    case_lines = []
    for cert, rows in data.cases().items():
        last = rows[-1]
        name = banks.loc[int(cert), "name"] if int(cert) in banks.index else f"cert {cert}"
        kw = dict(cert=int(cert), bank=name)
        q = date.fromisoformat(last["q"])
        src_c = f"{_SRC}/case_studies.json"
        facts += [
            ledger.add("Bank name", name, name, [name], f"{_SRC}/banks.parquet: name", **kw),
            ledger.add("Last score: national rank (1 = highest score)", int(last["rank"]), f"{int(last['rank']):,}",
                       _num_forms(int(last["rank"])), f"{src_c}: rank", q, **kw),
            ledger.add("Last score: banks ranked that quarter", int(last["n"]), f"{int(last['n']):,}",
                       count_forms(int(last["n"])), f"{src_c}: n", q, **kw),
            ledger.add("Last score: percentile (100 = highest risk)", float(last["pct"]), f"{last['pct']:.1f}%",
                       _pct_forms(float(last["pct"])), f"{src_c}: pct", q, **kw),
        ]
        case_lines.append(f"{name}: last scored {q.isoformat()}, rank {int(last['rank']):,} of {int(last['n']):,}.")
    return {
        "facts": ledger.slim(facts),
        "case_studies": case_lines,
        "how_it_works": copy.HOME_WHAT + " " + " ".join(f"{t}. {line}" for t, line, _ in copy.HOW_STEPS),
        "why_2023_missed": copy.HONEST_MISS,
    }


# ---- tool definitions and dispatch --------------------------------------------------------------------------

def _spec(name, description, properties) -> dict:
    # strict mode: every property is required and nullable when optional, and no extra keys are allowed.
    return {"name": name, "description": description, "strict": True,
            "input_schema": {"type": "object", "properties": properties, "required": list(properties),
                             "additionalProperties": False}}


_STR_OPT = {"type": ["string", "null"]}
_INT_OPT = {"type": ["integer", "null"]}

TOOL_SPECS: list[dict] = [
    _spec("find_bank", "Find banks by name. Returns up to 8 matches with certificate number, city, state and status.",
          {"query": {"type": "string", "description": "Bank name or part of it."},
           "state": {**_STR_OPT, "description": "Optional two-letter state code, or null."}}),
    _spec("bank_profile", "A bank's identity, status, latest Canary rank and percentile, up to 12 quarters of rank "
          "history and its latest loan-concentration result. Works for banks without a written report.",
          {"cert": {"type": "integer", "description": "FDIC certificate number."},
           "start": {**_STR_OPT, "description": "Optional first quarter (2022-12-31 or Q4 2022), or null."},
           "end": {**_STR_OPT, "description": "Optional last quarter, or null."}}),
    _spec("bank_report", "The checked facts from Canary's written report on a bank (only some banks have one).",
          {"cert": {"type": "integer", "description": "FDIC certificate number."}}),
    _spec("failures", "FDIC bank failures, sorted by date, at most 25 rows plus the total. With no filter, the latest "
          "year in the data.",
          {"year": {**_INT_OPT, "description": "Failure year, or null."},
           "state": {**_STR_OPT, "description": "Two-letter state code, or null."}}),
    _spec("watchlist", "Banks Canary flagged in a quarter (its riskiest 2%), by rank, at most 25 plus the total.",
          {"quarter": {**_STR_OPT, "description": "2022-12-31 or Q4 2022; null for the latest quarter."},
           "state": {**_STR_OPT, "description": "Two-letter state code, or null."}}),
    _spec("canary_facts", "Canary's headline results, the flag rule, the SVB, Signature and First Republic case "
          "studies, and how the score works and why 2023 was missed.", {}),
]

_TOOLS = {"find_bank": find_bank, "bank_profile": bank_profile, "bank_report": bank_report, "failures": failures,
          "watchlist": watchlist, "canary_facts": canary_facts}


def run_tool(ledger: FactLedger, name: str, args: dict) -> dict:
    fn = _TOOLS.get(name)
    if fn is None:
        return {"error": f"Unknown tool {name!r}."}
    if not isinstance(args, dict):
        return {"error": "Tool arguments must be an object."}
    try:
        return fn(ledger, **args)
    except TypeError:
        return {"error": f"Bad arguments for {name}."}
    except Exception as exc:  # tools never raise into the chat loop
        return {"error": f"{name} failed: {type(exc).__name__}."}
