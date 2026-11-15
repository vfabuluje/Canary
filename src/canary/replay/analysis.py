"""Model-free error analysis (spec section 8.1 and 8.4).

- failure_mix: what kind of failure the model learned from (2001-2014) vs the three 2023 banks.
- distribution_table: how big bond losses and uninsured deposits were in training vs those banks.
- false_alarm_profile / top_false_alarm_banks: what the model's false alarms look like.

Every function works on a copy; the input frame is never changed.
"""

from datetime import date

import pandas as pd

from canary.model.dataset import FEATURE_COLUMNS
from canary.model.train import CASE_STUDY_CERTS

# Round analyst rules of thumb, fixed in the spec before results were seen (decision 0015).
CREDIT_NONCURRENT = 0.05  # 5% or more of loans are 90+ days past due or not accruing
CREDIT_TEXAS = 1.0  # bad assets at least as large as equity plus loan-loss reserves

PROFILES = ("credit only", "run-risk only", "both", "neither")
HORIZON_END = date(2025, 12, 31)


def credit_loss_profile(rows: pd.DataFrame) -> pd.Series:
    """True when the bank's loans had gone bad: noncurrent >= 5%, Texas >= 100%, or insolvent.

    A negative Texas ratio only happens when equity + allowance is negative (insolvent), see
    decision 0014. Nulls count as False.
    """
    noncurrent = rows["noncurrent_loans_to_loans"]
    texas = rows["texas_ratio"]
    return ((noncurrent >= CREDIT_NONCURRENT) | (texas >= CREDIT_TEXAS) | (texas < 0)).fillna(False).astype(bool)


def _profile(credit: pd.Series, run: pd.Series) -> pd.Series:
    out = pd.Series("neither", index=credit.index, dtype=object)
    out[credit & ~run] = "credit only"
    out[~credit & run] = "run-risk only"
    out[credit & run] = "both"
    return out


def _closest_to_failure(rows: pd.DataFrame) -> pd.DataFrame:
    q = pd.to_numeric(rows["quarters_until_failure"], errors="coerce")
    rows = rows[q.between(1, 4)].assign(_q=q)
    rows = rows.sort_values(["cert", "_q", "report_date"], kind="mergesort")
    return rows.drop_duplicates("cert", keep="first").drop(columns="_q")


def failure_mix(scored: pd.DataFrame) -> pd.DataFrame:
    """One row per failed bank: its profile at the row closest to failure (1-4 quarters out).

    era "training": banks with such a row whose report date is in the training split (2001-2014).
    era "2023": the three case-study banks at their last pre-failure row.
    """
    training = _closest_to_failure(scored[scored["split"] == "train"]).assign(era="training")
    cases = _closest_to_failure(scored[scored["cert"].isin(CASE_STUDY_CERTS)]).assign(era="2023")
    mix = pd.concat([training, cases], ignore_index=True)

    mix["credit_loss"] = credit_loss_profile(mix)
    mix["run_risk"] = mix["run_risk_flagged"].fillna(False).astype(bool)
    mix["profile"] = _profile(mix["credit_loss"], mix["run_risk"])
    mix["failure_year"] = pd.to_datetime(mix["failure_date"]).dt.year
    cols = [
        "era", "cert", "institution_name", "failure_date", "failure_year", "report_date",
        "quarters_until_failure", "credit_loss", "run_risk", "profile",
        "noncurrent_loans_to_loans", "texas_ratio", "bond_loss_to_equity",
        "uninsured_to_deposits", "run_risk_score",
    ]
    return mix[cols].reset_index(drop=True)


def _counts(profiles: pd.Series) -> dict:
    return {p: int((profiles == p).sum()) for p in PROFILES}


def mix_summary(mix: pd.DataFrame) -> dict:
    """Profile counts per era, and per failure year for the training era."""
    training = mix[mix["era"] == "training"]
    return {
        "training": _counts(training["profile"]),
        "2023": _counts(mix.loc[mix["era"] == "2023", "profile"]),
        "training_by_year": {
            int(year): _counts(group["profile"]) for year, group in training.groupby("failure_year")
        },
    }


def _stats(values: pd.Series, group: str, variable: str) -> dict:
    v = values.dropna()
    return {
        "variable": variable,
        "group": group,
        "n": int(len(v)),
        "median": float(v.median()) if len(v) else float("nan"),
        "p90": float(v.quantile(0.9)) if len(v) else float("nan"),
        "p99": float(v.quantile(0.99)) if len(v) else float("nan"),
        "share_above_0_3": float((v > 0.3).mean()) if len(v) else float("nan"),
    }


def distribution_table(scored: pd.DataFrame) -> pd.DataFrame:
    """bond_loss_to_equity and uninsured_to_deposits: training failures vs all training rows vs the 2023 banks.

    For each 2023 bank the "distribution" is its single last pre-failure row (n = 1).
    """
    train = scored[scored["split"] == "train"]
    last = _closest_to_failure(scored[scored["cert"].isin(CASE_STUDY_CERTS)]).set_index("cert")
    out = []
    for variable in ("bond_loss_to_equity", "uninsured_to_deposits"):
        out.append(_stats(train.loc[train["label"] == 1, variable], "train_positive_rows", variable))
        out.append(_stats(train[variable], "train_all_rows", variable))
        for cert, name in CASE_STUDY_CERTS.items():
            if cert in last.index:
                out.append(_stats(pd.Series([last.loc[cert, variable]]), name, variable))
    return pd.DataFrame(out)


def false_alarm_profile(test_scored: pd.DataFrame) -> pd.DataFrame:
    """Median of each feature for true alarms (flagged, failed within 4q) vs false alarms (flagged, did not)."""
    flagged = test_scored[test_scored["flagged"].astype(bool)]
    true_alarm = flagged[flagged["label"] == 1]
    false_alarm = flagged[flagged["label"] == 0]
    rows = []
    for feature in FEATURE_COLUMNS:
        t = float(true_alarm[feature].median())
        f = float(false_alarm[feature].median())
        rows.append({"feature": feature, "median_true_alarm": t, "median_false_alarm": f, "difference": f - t})
    out = pd.DataFrame(rows)
    out.attrs["n_true_alarm_rows"] = int(len(true_alarm))
    out.attrs["n_false_alarm_rows"] = int(len(false_alarm))
    return out


def top_false_alarm_banks(test_scored: pd.DataFrame, n: int = 10, horizon_end: date = HORIZON_END) -> pd.DataFrame:
    """Banks flagged most often that had not failed by horizon_end (ties: cert ascending)."""
    flagged = test_scored[test_scored["flagged"].astype(bool)]
    fd = pd.to_datetime(flagged["failure_date"])
    survived = flagged[fd.isna() | (fd > pd.Timestamp(horizon_end))]
    survived = survived.sort_values(["cert", "report_date"], kind="mergesort")
    out = survived.groupby("cert").agg(
        institution_name=("institution_name", "last"), quarters_flagged=("report_date", "size")
    )
    out = out.reset_index().sort_values(["quarters_flagged", "cert"], ascending=[False, True], kind="mergesort")
    return out.head(n)[["cert", "institution_name", "quarters_flagged"]].reset_index(drop=True)
