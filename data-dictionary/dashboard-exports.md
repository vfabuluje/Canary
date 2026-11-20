# dashboard-exports (Phase 6 files)

The files `python -m canary.dashboard export --out dashboard/data` writes. They are what the Streamlit app reads: the app never touches `data/`, the warehouse or the model. Unlike the Phase 3 to 5 outputs these **are committed** (the whole folder is well under the 50 MB limit the export enforces). Decision: [[decisions/0023-dashboard]]. Runbook: [[runbooks/dashboard]]. Spec: [[specs/2026-11-19-phase6-dashboard-design]].

| | |
|---|---|
| Inputs (read only) | `fct_bank_features` export, Phase 3 model folder (`metrics.json`, `scores_test.parquet`, `case_studies.csv`), failures file, analyst notes (`banks/`), analyst traces |
| Built by | `src/canary/dashboard/` (`__main__.py`, `tables.py`, `cases.py`, `reports.py`) |
| Deterministic | Yes. No Claude calls |
| Ranks | Rank 1 is the riskiest bank that quarter. Percentile = `100 * (n_banks - rank + 1) / n_banks`, so rank 1 is 100 |

## `banks.parquet`

One row per bank (11,243 rows).

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number |
| `name` | Bank name, title-cased |
| `state`, `city` | Headquarters |
| `first_report`, `last_report` | First and last quarter the bank filed |
| `failure_date` | Date it failed, empty if it never did |
| `scored` | True if the model gave it a score at its latest quarter |
| `latest_report_date` | Latest quarter the bank was scored |
| `latest_rank`, `latest_n`, `latest_percentile` | Rank, banks ranked that quarter, and percentile at that quarter |
| `latest_flagged` | True if it was on the 2% watchlist at that quarter |
| `after_test_period` | True if the latest scored quarter is after the 2016-2024 test window (so no tested result exists for it) |
| `has_report` | True if the bank has a written, checked report (`reports/<cert>.json`) |

## `scores_history.parquet`

One row per bank per quarter from 2016-03-31.

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number |
| `report_date` | Quarter end |
| `rank` | Risk rank that quarter (1 = riskiest) |
| `n_banks` | Banks ranked that quarter |
| `percentile` | Percentile of the bank that quarter |
| `flagged` | On the 2% watchlist that quarter |

## `concentration.parquet`

One row per scored bank, at its latest scored quarter: the code-written real-estate concentration check ([[decisions/0021-cre-concentration-2006-thresholds]]).

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number |
| `as_of` | Quarter the check was run for |
| `measure` | Which version of the measure the data allowed |
| `construction_pct` | Construction loans as a percent of capital |
| `cre_pct` | Commercial real estate loans as a percent of capital |
| `growth_pct` | Three-year growth in commercial real estate loans, percent |
| `reason` | Why the test could not be applied, empty when it could |
| `lines` | The finished sentences shown to the reader, one per line |

## `metrics.json`

One JSON object, a copy of the headline Phase 3 test results (see [[data-dictionary/replay_outputs]] and the README for what each means).

| Key | Meaning |
|---|---|
| `auc` | Model AUC on the 2016-2024 test |
| `recall` | Share of eligible failed banks caught |
| `banks_caught` | Failed banks on the watchlist at least once |
| `eligible_banks` | Failed banks with a report 1 to 4 quarters before failing |
| `lead_time_median` | Median quarters of warning |
| `false_alarm_rate` | Share of flagged bank-quarters that did not fail within a year |
| `rows_flagged` | Bank-quarters flagged |
| `baseline` | The same measures for the Texas-ratio baseline (`auc`, `recall`, `banks_caught`, `eligible_banks`, `caught_certs`, `recall_2q`, `banks_caught_2q`, `eligible_banks_2q`, `lead_time_median`, `lead_time_min`, `lead_time_max`, `false_alarm_rate`, `false_alarm_banks`, `rows_flagged`) |

## `threshold.json`

A JSON list with one object per watchlist size (0.5%, 1%, 2% and so on, seven sizes), recomputed from the saved test scores.

| Key | Meaning |
|---|---|
| `share` | Watchlist size as a fraction of banks (0.02 = 2%) |
| `caught` | Eligible failed banks caught at that size |
| `eligible` | Eligible failed banks |
| `false_alarm` | False-alarm rate at that size |
| `rows` | Bank-quarters flagged at that size |
| `caught_case_studies` | Which of SVB, Signature, First Republic (cert numbers) were caught at that size |

## `case_studies.json`

One JSON object keyed by cert (`24735` SVB, `57053` Signature, `59017` First Republic). Each value is a list of that bank's quarters, oldest first.

| Key | Meaning |
|---|---|
| `q` | Quarter end |
| `pct` | Percentile that quarter |
| `rank` | Rank that quarter |
| `n` | Banks ranked that quarter |
| `weak` | The bank's weak-spot ratio in percent (bond loss to equity for SVB and Signature's AFS loss, uninsured share for First Republic) |
| `signals` | The top three model signals as `[plain-English name, contribution]` pairs |
| `phase` | `before` (2021), `rising` (2022) or `last` (the last report before failing) |

## `reports/<cert>.json`

One file per bank with a written, checked report (the same set as `banks.has_report`). The export rebuilds the fact sheet from the data and fails if a stored agent trace no longer passes the citation checker.

| Key | Meaning |
|---|---|
| `cert` | FDIC certificate number |
| `name` | Bank name |
| `as_of` | Quarter the report is about |
| `outcome` | `failed`, `missed`, `alive` and similar outcome kind |
| `failure_date` | Failure date, empty if none |
| `rank`, `n_banks`, `percentile` | Position at `as_of` |
| `flagged` | On the 2% watchlist at `as_of` |
| `headline` | One-line title for the report page |
| `cards` | The report cards in page order: `key`, `who`, `badge` (`AI` or `RULE`), `sentences` (each with `text` and its `numbers`) |
| `agents` | Slim trace per agent (`trend`, `peer`, `analyst`): `ran`, `attempts`, `first_try` |
| `facts` | The fact sheet Ask Canary and the cards cite: `id`, `label`, `quarter`, `value`, `display`, `forms`, `hindsight`, `source`, `feature`, `kind` |
| `note_md` | The checked memo text, without its front matter |
