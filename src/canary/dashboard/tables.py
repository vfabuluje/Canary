"""Table exports for the dashboard: banks, score history, concentration, headline metrics, watchlist sizes."""

import json
import re
from pathlib import Path

import pandas as pd

from canary.analyst.concentration import compute_concentration, render_concentration
from canary.analyst.context import Context
from canary.model.metrics import bank_recall, false_alarm_rate, flag_watchlist

WATCHLIST_SHARES: tuple[float, ...] = (0.005, 0.01, 0.02, 0.03, 0.05, 0.075, 0.10)
CASE_STUDY_CERTS = (24735, 57053, 59017)
TEST_END = pd.Timestamp("2024-12-31")
METRIC_KEYS = ("auc", "recall", "banks_caught", "eligible_banks", "lead_time_median", "false_alarm_rate",
               "rows_flagged", "baseline")

_FRONT_FIELD = re.compile(r"^(cert|as_of):\s*(\S+)\s*$", re.MULTILINE)


def showcase_certs(notes_dir: Path, trace_dir: Path) -> set[int]:
    """Certs with a note in notes_dir and a passing trace `<cert>_<as_of>.json` in trace_dir."""
    certs: set[int] = set()
    for note in Path(notes_dir).glob("*.md"):
        head = note.read_text(encoding="utf-8").split("---", 2)
        if len(head) < 3:
            continue
        fields = dict(_FRONT_FIELD.findall(head[1]))
        if "cert" not in fields or "as_of" not in fields:
            continue
        trace = Path(trace_dir) / f"{fields['cert']}_{fields['as_of']}.json"
        if not trace.exists():
            continue
        try:
            ok = json.loads(trace.read_text(encoding="utf-8")).get("ok") is True
        except (json.JSONDecodeError, OSError):
            continue
        if ok:
            certs.add(int(fields["cert"]))
    return certs


def _latest_scores(scored: pd.DataFrame) -> pd.DataFrame:
    last = scored.sort_values("report_date", kind="mergesort").drop_duplicates("cert", keep="last")
    return last.set_index("cert")


def export_banks(ctx: Context, showcase_certs: set[int]) -> pd.DataFrame:
    b = ctx.banks.copy()
    latest = _latest_scores(ctx.scored).reindex(b["cert"])
    out = pd.DataFrame({
        "cert": b["cert"].astype("int64").to_numpy(),
        "name": b["name"].astype(str).str.title().to_numpy(),
        "state": b["state"].to_numpy(),
        "city": b["city"].to_numpy(),
        "first_report": b["first_report"].to_numpy(),
        "last_report": b["last_report"].to_numpy(),
        "failure_date": b["failure_date"].to_numpy(),
    })
    out["scored"] = latest["score"].notna().to_numpy()
    out["latest_report_date"] = latest["report_date"].to_numpy()
    out["latest_rank"] = latest["rank"].astype("Int64").to_numpy()
    out["latest_n"] = latest["n_banks"].astype("Int64").to_numpy()
    out["latest_percentile"] = latest["percentile"].to_numpy()
    out["latest_flagged"] = latest["flagged"].astype("boolean").to_numpy()
    out["after_test_period"] = (out["latest_report_date"] > TEST_END).fillna(False).astype(bool)
    out["has_report"] = out["cert"].isin(showcase_certs)
    return out.reset_index(drop=True)


def export_scores_history(ctx: Context) -> pd.DataFrame:
    s = ctx.scored
    out = s.loc[s["report_date"] >= pd.Timestamp("2016-03-31"), ["cert", "report_date", "rank", "n_banks",
                                                                   "percentile", "flagged"]]
    return out.reset_index(drop=True)


def export_concentration(ctx: Context) -> pd.DataFrame:
    """One row per scored bank at its latest scored quarter; `reason` is kept when the test cannot be applied."""
    latest = _latest_scores(ctx.scored)
    by_cert = {c: g for c, g in ctx.concentration.groupby("cert")}
    empty = ctx.concentration.iloc[0:0]
    rows = []
    for cert, rec in latest.iterrows():
        as_of = rec["report_date"].date()
        r = compute_concentration(by_cert.get(cert, empty), as_of)
        rows.append({
            "cert": int(cert), "as_of": pd.Timestamp(r.as_of), "measure": r.measure,
            "construction_pct": r.construction_pct, "cre_pct": r.cre_pct, "growth_pct": r.growth_pct,
            "reason": r.reason, "lines": "\n".join(render_concentration(r)),
        })
    out = pd.DataFrame(rows, columns=["cert", "as_of", "measure", "construction_pct", "cre_pct", "growth_pct",
                                      "reason", "lines"])
    for col in ("construction_pct", "cre_pct", "growth_pct"):
        out[col] = out[col].astype("float64")
    return out


def threshold_table(scores_test: pd.DataFrame) -> list[dict]:
    """Test-period results at each watchlist size, recomputed from the saved test scores."""
    df = scores_test.reset_index(drop=True)
    table = []
    for share in WATCHLIST_SHARES:
        df["_flag"] = flag_watchlist(df, "score", share)
        recall = bank_recall(df, "_flag")
        table.append({
            "share": share,
            "caught": recall.caught,
            "eligible": recall.eligible,
            "false_alarm": false_alarm_rate(df, "_flag"),
            "rows": int(df["_flag"].sum()),
            "caught_case_studies": sorted(c for c in recall.caught_certs if c in CASE_STUDY_CERTS),
        })
    return table


def write_tables(ctx: Context, model_dir: Path, out: Path, showcase_certs: set[int]) -> None:
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    export_banks(ctx, showcase_certs).to_parquet(out / "banks.parquet", index=False)
    export_scores_history(ctx).to_parquet(out / "scores_history.parquet", index=False)
    export_concentration(ctx).to_parquet(out / "concentration.parquet", index=False)
    metrics = json.loads((Path(model_dir) / "metrics.json").read_text())
    (out / "metrics.json").write_text(json.dumps({k: metrics[k] for k in METRIC_KEYS}, indent=2) + "\n")
    table = threshold_table(pd.read_parquet(Path(model_dir) / "scores_test.parquet"))
    (out / "threshold.json").write_text(json.dumps(table, indent=2) + "\n")
