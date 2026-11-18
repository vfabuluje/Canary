"""Fact sheet: every number a memo may cite, with the exact renderings the checker accepts.

Forms are generous but true: only real renderings of the value. Facts with `hindsight=True`
may be used only in the outcome sections (spec 4).
"""

import json
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import pandas as pd

from canary.analyst import sections as sections_mod
from canary.analyst.context import Context
from canary.analyst.labels import PLAIN_NAMES, display_forms
from canary.analyst.outcome import Outcome, classify, default_as_of, validate_as_of
from canary.model.dataset import FEATURE_COLUMNS
from canary.model.metrics import WATCHLIST_SHARE
from canary.replay.analysis import credit_loss_profile
from canary.replay.probe import contribution_matrix

PERCENTILE_SCALE_LABEL = "Percentile scale (0 to 100; higher means riskier)"
POSTHOC_LABEL = "post-hoc check, designed after the 2023 failures"
_WORDS = {1: "one", 2: "two", 3: "three", 4: "four"}
# Spelled time spans ("four quarters", "a year") are numbers too: the checker matches them against
# fact forms as "<word> <unit>" (an -> a), so labels that contain one carry it as a form.
SPELLED_WORDS = "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|an|a"
SPELLED_SPAN = re.compile(rf"\b(?P<sw>{SPELLED_WORDS})\s+(?P<su>quarters?|years?)\b", re.IGNORECASE)


def spelled_norm(word: str, unit: str) -> str:
    word = word.lower()
    return f"{'a' if word == 'an' else word} {unit.lower()}"
_FEATURES_SRC = "data/features/fct_bank_features.parquet"
_SCORES_SRC = "data/analyst/scores.parquet"


@dataclass
class Fact:
    id: str
    label: str
    quarter: date | None
    value: float | str
    display: str
    forms: list[str]
    hindsight: bool
    source: str
    feature: str | None = None
    kind: str | None = None


@dataclass
class FactSheet:
    cert: int
    name: str
    as_of: date
    outcome: Outcome
    facts: list[Fact]
    history: pd.DataFrame
    after_history: pd.DataFrame
    cant_see: str
    section_keys: list[str]
    code_only: set[str] = field(default_factory=set)
    extras: dict = field(default_factory=dict)

    def by_id(self, id: str) -> Fact:
        for f in self.facts:
            if f.id == id:
                return f
        raise KeyError(id)


def date_forms(d: date) -> list[str]:
    return [d.isoformat(), f"Q{(d.month - 1) // 3 + 1} {d.year}", f"{d:%B} {d.day}, {d.year}", str(d.year)]


def _dedupe(forms: list[str]) -> list[str]:
    return list(dict.fromkeys(forms))


class _Builder:
    def __init__(self) -> None:
        self.facts: list[Fact] = []

    def add(self, label, value, display, forms, source, quarter=None, hindsight=False) -> None:
        forms = list(forms) + (date_forms(quarter) if quarter else [])
        forms += [spelled_norm(m["sw"], m["su"]) for m in SPELLED_SPAN.finditer(label)]
        self.facts.append(
            Fact(f"F{len(self.facts) + 1}", label, quarter, value, display, _dedupe(forms), hindsight, source)
        )


def _ordinal(n: int) -> str:
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def _count_forms(n: int) -> list[str]:
    return [f"{n:,}", str(n)]


def _history(rows: pd.DataFrame) -> pd.DataFrame:
    cols = ["report_date", "rank", "n_banks", "flagged"]
    return rows.sort_values("report_date")[cols].reset_index(drop=True)


def _drivers(b: _Builder, ctx: Context, row: pd.DataFrame, quarter: date, prefix: str, hindsight: bool) -> None:
    contrib = contribution_matrix(ctx.model, row)[0]
    order = sorted(range(len(FEATURE_COLUMNS)), key=lambda j: contrib[j])
    ups = [j for j in reversed(order) if contrib[j] > 0][:5]
    downs = [j for j in order if contrib[j] < 0][:5]
    when = "" if not hindsight else f" at {quarter}"
    for direction, picks in (("up", ups), ("down", downs)):
        for i, j in enumerate(picks, 1):
            name = FEATURE_COLUMNS[j]
            val = row.iloc[0][name]
            vforms = display_forms(name, float(val)) if pd.notna(val) else []
            shown = f", value {vforms[0]}" if vforms else ""
            c = float(contrib[j])
            b.add(
                f"{prefix} {direction} #{i}{when}: {PLAIN_NAMES[name]}{shown}; contribution to the score",
                c,
                f"{c:+.3f}",
                [f"{c:+.3f}", f"{abs(c):.3f}", f"{abs(c):.2f}"] + vforms,
                f"{_SCORES_SRC}: feature {name} contribution",
                quarter,
                hindsight,
            )


def _quarter_name(d: date) -> str:
    return f"Q{(d.month - 1) // 3 + 1} {d.year}"


def _what_if(b: _Builder, replay_dir: Path, cert: int) -> None:
    """Phase 4 what-if (one feature changed at a time on one bank-quarter), for a missed bank.

    Post-hoc analysis, so hindsight and labeled. One fact per feature: the best (lowest) rank the
    bank reached anywhere on the grid, and the grid value that reached it.
    """
    path = replay_dir / "what_if.csv"
    if not path.exists():
        return
    wi = pd.read_csv(path)
    wi = wi[wi["cert"] == cert]
    for (rd, feature), g in wi.groupby(["report_date", "feature"], sort=True):
        if feature not in PLAIN_NAMES:
            continue
        q = pd.Timestamp(rd).date()
        best = g.sort_values(["rank", "value"]).iloc[0]
        rk, n = int(best["rank"]), int(best["n_banks"])
        lo, hi, at = (display_forms(feature, float(g["value"].min())), display_forms(feature, float(g["value"].max())),
                      display_forms(feature, float(best["value"])))
        b.add(f"What-if ({POSTHOC_LABEL}): {PLAIN_NAMES[feature]} set to each value from {lo[0]} to {hi[0]}, "
              f"other data unchanged; best rank reached {rk:,} of {n:,}, at {at[0]}",
              rk, f"{rk:,}", _count_forms(rk) + [f"#{rk}", f"#{rk:,}"] + _count_forms(n) + lo + hi + at,
              f"{path}: rank (feature {feature})", q, True)


def _cant_see(lacks_profile: bool, share: float | None) -> str:
    parts = []
    if lacks_profile:
        lead = "This bank does not show a credit-loss profile in the data."
        if share is not None:
            lead += f" The model was trained on failures that were {share:.0f}% credit-loss failures,"
        else:
            lead += " The model was trained mostly on credit-loss failures,"
        parts.append(lead + " and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons.")
    parts.append(
        "FDIC data has no loan fair values, no depositor identity, and no non-financial causes "
        "such as fraud or management, so the model cannot see them."
    )
    return " ".join(parts)


def build_fact_sheet(
    ctx: Context, cert: int, as_of: date | None = None, replay_dir: Path = Path("data/replay")
) -> FactSheet:
    if as_of is None:
        as_of = default_as_of(ctx, cert)
    validate_as_of(ctx, cert, as_of)
    outcome = classify(ctx, cert, as_of)
    ts = pd.Timestamp(as_of)
    bank = ctx.banks[ctx.banks["cert"] == cert].iloc[0]
    name = str(bank["name"]).title()
    rows = ctx.scored[ctx.scored["cert"] == cert]
    at = rows[rows["report_date"] == ts]
    row = at.iloc[0]
    b = _Builder()

    b.add("Bank name", name, name, [name], f"{_FEATURES_SRC}: institution_name")
    b.add("Certificate number", cert, str(cert), [str(cert)], f"{_FEATURES_SRC}: cert")
    b.add("As-of quarter", as_of.isoformat(), as_of.isoformat(), [], f"{_FEATURES_SRC}: report_date", as_of)
    if pd.notna(bank["state"]):
        b.add("State", str(bank["state"]), str(bank["state"]), [str(bank["state"])], "data/raw/financials: STALP")

    score = float(row["score"])
    b.add("Model score", score, f"{score:.4f}", [f"{score:.4f}", f"{score:.3f}"], f"{_SCORES_SRC}: score", as_of)
    rank, n = int(row["rank"]), int(row["n_banks"])
    b.add("National rank (1 = highest score)", rank, f"{rank:,}",
          _count_forms(rank) + [f"#{rank:,}", f"#{rank}"], f"{_SCORES_SRC}: rank", as_of)
    b.add("Banks ranked that quarter", n, f"{n:,}", _count_forms(n), f"{_SCORES_SRC}: n_banks", as_of)
    pct = float(row["percentile"])
    pct_forms = [f"{pct:.1f}%", f"{pct:.0f}%", f"{pct:.1f}", f"{pct:.0f}", _ordinal(round(pct)), f"{pct:.1f}th"]
    b.add("Percentile (100 = highest risk)", pct, f"{pct:.1f}%", pct_forms, f"{_SCORES_SRC}: percentile", as_of)
    b.add(PERCENTILE_SCALE_LABEL, 100, "0 to 100", ["100", "0 to 100", "0-100", "0"],
          "canary.analyst.facts: percentile scale (fixed)")
    flagged = bool(row["flagged"])
    b.add("On the watchlist", "yes" if flagged else "no", "flagged" if flagged else "not flagged",
          ["flagged", "on the watchlist"] if flagged else ["not flagged"], f"{_SCORES_SRC}: flagged", as_of)
    share = WATCHLIST_SHARE * 100
    b.add("Watchlist share of banks", share, f"{share:.0f}%", [f"{share:.0f}%", f"{share:.1f}%", f"{share:.0f}"],
          "canary.model.metrics.WATCHLIST_SHARE")
    k = int(ctx.scored.loc[ctx.scored["report_date"] == ts, "flagged"].astype(bool).sum())
    b.add("Banks on the watchlist that quarter", k, str(k), _count_forms(k), f"{_SCORES_SRC}: flagged", as_of)

    feats = ctx.features
    at_feats = feats[feats["report_date"] == ts]
    frow = at_feats[at_feats["cert"] == cert].iloc[0]
    for name_ in FEATURE_COLUMNS:
        v = frow[name_]
        if pd.isna(v):
            continue
        v = float(v)
        label = PLAIN_NAMES[name_]
        forms = display_forms(name_, v)
        b.add(f"Bank: {label}", v, forms[0], forms, f"{_FEATURES_SRC}: {name_}", as_of)
        med = at_feats[name_].median(skipna=True)
        if pd.notna(med):
            mf = display_forms(name_, float(med))
            b.add(f"National median: {label}", float(med), mf[0], mf, f"{_FEATURES_SRC}: {name_} (median of all banks)", as_of)

    _drivers(b, ctx, at, as_of, "Driver", False)

    # Hindsight facts
    if outcome.failure_date:
        fd = outcome.failure_date
        b.add("Failure date", fd.isoformat(), fd.isoformat(), [], "data/raw/failures: FAILDATE", fd, True)
    if outcome.first_flag:
        ff = outcome.first_flag
        b.add("First flag quarter (Phase 3 lead-time rule)", ff.isoformat(), ff.isoformat(), [],
              f"{_SCORES_SRC}: flagged", ff, True)
        if outcome.lead_quarters is not None:
            q = outcome.lead_quarters
            word = _WORDS.get(q, str(q))
            words = [word, f"{word} quarter{'' if q == 1 else 's'}"] + (["a quarter"] if q == 1 else [])
            b.add("Lead time in quarters before failure", q, str(q), [str(q), *words],
                  f"{_SCORES_SRC}: quarters_until_failure", None, True)
        if ff != as_of:
            fr = rows[rows["report_date"] == pd.Timestamp(ff)]
            if len(fr):
                _drivers(b, ctx, fr, ff, "Driver", True)
    if outcome.late_flag:
        lf = outcome.late_flag
        b.add(f"Flagged at {_quarter_name(lf)}, after the 2016-2024 test period (not counted in the reported results)",
              lf.isoformat(), lf.isoformat(), ["2016", "2024"], f"{_SCORES_SRC}: flagged", lf, True)
    if not outcome.still_reporting:
        lr = outcome.last_report
        b.add("Last quarter the bank reported", lr.isoformat(), lr.isoformat(), [], f"{_FEATURES_SRC}: report_date", lr, True)
    after = rows[rows["report_date"] > ts].sort_values("report_date")
    for _, r in after.iterrows():
        d = r["report_date"].date()
        rk = int(r["rank"])
        on = bool(r["flagged"])
        status = "flagged (on the watchlist)" if on else "not flagged"
        b.add(f"Rank in a later quarter ({d}), {status}", rk, f"{rk:,} ({'flagged' if on else 'not flagged'})",
              _count_forms(rk) + [f"#{rk}", f"#{rk:,}"], f"{_SCORES_SRC}: rank, flagged", d, True)

    # Phase 4 facts
    banks_csv = replay_dir / "replay_banks.csv"
    if banks_csv.exists():
        rb = pd.read_csv(banks_csv)
        rb = rb[(rb["cert"] == cert) & (pd.to_datetime(rb["report_date"]) == ts)]
        if len(rb):
            rr = int(rb.iloc[0]["run_risk_rank"])
            b.add(f"Run-risk rank ({POSTHOC_LABEL})", rr, f"{rr:,}", _count_forms(rr) + [f"#{rr}"],
                  f"{banks_csv}: run_risk_rank", as_of, True)

    if outcome.kind == "missed":
        _what_if(b, replay_dir, cert)

    lacks_profile = not bool(credit_loss_profile(at_feats[at_feats["cert"] == cert]).iloc[0])
    credit_share = None
    metrics = replay_dir / "posthoc_metrics.json"
    if lacks_profile and metrics.exists():
        mix = json.loads(metrics.read_text())["failure_mix"]["training"]
        total = sum(mix.values())
        credit_share = 100.0 * (mix["credit only"] + mix["both"]) / total
        src = f"{metrics}: failure_mix.training"
        b.add("Training failures that were credit-loss failures (share)", credit_share, f"{credit_share:.0f}%",
              [f"{credit_share:.0f}%", f"{credit_share:.1f}%"], src)
        b.add("Failed banks in the training period", total, str(total), _count_forms(total), src)
        for key, text in (("credit only", "credit-loss only"), ("both", "credit-loss and run-risk")):
            b.add(f"Training failures with profile: {text}", mix[key], str(mix[key]), _count_forms(mix[key]), src)

    all_secs = sections_mod.all_sections(outcome.kind)
    sheet = FactSheet(
        cert=cert,
        name=name,
        as_of=as_of,
        outcome=outcome,
        facts=b.facts,
        history=_history(rows[rows["report_date"] <= ts].sort_values("report_date").tail(8)),
        after_history=_history(after),
        cant_see=_cant_see(lacks_profile, credit_share),
        section_keys=[s.key for s in all_secs],
    )
    for sp in sections_mod.SPECIALISTS:
        for f in sp.build_facts(ctx, sheet):
            f.id = f"F{len(sheet.facts) + 1}"
            sheet.facts.append(f)
    return sheet
