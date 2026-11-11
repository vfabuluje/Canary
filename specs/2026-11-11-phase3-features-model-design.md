# Phase 3 Spec: CAMELS-style Features → XGBoost → Honest Test on 2016–2024

**Date:** 2026-11-11
**Status:** Approved by Victor 2026-11-11
**Phase:** 3 (see `CLAUDE.md`)

## 1. Intent: why this exists

Phase 2 produced one trusted table, `canary_marts.fct_bank_quarters`: 710,691 bank-quarters (2001-03-31 to 2026-06-30), 45 FDIC fields per row, and the label `quarters_until_failure`. Phase 3 answers the project's core question for the first time: **from public quarterly data alone, can a model trained only on 2001–2015 pick out the banks that failed in 2016–2024, and in particular SVB, Signature Bank and First Republic, before they failed?**

Three things make this worth doing carefully:
1. **It's the headline result.** The README, the LinkedIn post and the interview hook ("Could a model have seen SVB coming?") all rest on Phase 3's numbers, so they must hold up when someone pokes at them.
2. **It has to be honest.** The training years are dominated by the 2008–2012 credit crisis: 540 failures in 2001–2015, about 85% of them in 2008–2012, mostly from bad real-estate loans. SVB failed differently: its loans were fine, and it was undone by bond losses plus a run on uninsured deposits. A model trained honestly may not catch it. Per the project plan, **if SVB isn't caught, we report that and explain why.** A result that only looks good because the test was peeked at is worse than an honest miss.
3. **It's data engineering work.** Victor's target roles are data engineering and analytics at banks. The features are built as a tested dbt model in the warehouse, not inside a notebook, so the pipeline from raw data to model input is version-controlled, documented and checked.

## 2. Goals
- G1. A dbt model `canary_marts.fct_bank_features`: one row per bank-quarter with CAMELS-style ratios (§6), with dbt data tests and a data dictionary entry.
- G2. A one-command export of `fct_bank_features` from Athena to a local Parquet file for modeling.
- G3. A Python training pipeline (`canary.model`) that builds the label, applies the time split (§5), trains XGBoost on 2001–2014 report dates, and scores 2016–2024 once.
- G4. A metrics report with the project's metrics (§7): AUC, recall, lead time, false-alarm rate, plus a simple baseline for comparison.
- G5. A first-look case-study table for SVB, Signature and First Republic: each bank's score, its rank and whether it was flagged, for every quarter from 2021 to its failure, and the top signals behind each score. The deep replay and error analysis stay in Phase 4.
- G6. Unit tests for the label, split, flagging and metric functions (no AWS, no network). Decisions logged; README results section updated honestly.

## 3. Non-goals (later phases or post-launch)
- Deep SVB/Signature/First Republic replay, error analysis of misses and false alarms (Phase 4).
- The AI analyst agent, the data-quality agent, Obsidian bank notes (Phase 5 or post-launch).
- Dashboard (Phase 6). FRED macro data (post-launch roadmap).
- Probability calibration, model ensembles, deep learning, SageMaker or any cloud training.
- New FDIC fields. If a feature truly needs one, stop and raise it; adding fields means re-pulling (decision 0005).

## 4. Anti-goals (a failure even if it "works")
- **Leakage.** Any training row whose label depends on a failure after 2015-12-31; any feature computed from information dated after the row's report date; `failure_date`, `quarters_until_failure` or `institution_name` used as model inputs; selecting `*` from the mart as features.
- **Tuning on the test years.** Hyperparameters, feature choices, the 2% flag rate and 0-handling rules are all fixed using 2001–2014 only. The 2016–2024 scores are produced once and reported as they come out. If anything is changed after looking at test results, the README says so.
- **Overclaiming.** Lead time counted from the report date is presented with the one-month reporting-lag caveat (README limitations). "Caught SVB" is only claimed if SVB was in the flagged 2% at a quarter before it failed.
- **Unexplainable features.** Every feature has a one-line plain-English meaning Victor can say out loud.
- **AWS surprises.** No deletes without Victor's yes; `dbt build` of the new model needs his yes (it creates and later replaces a table); stays inside the $5/month budget.

## 5. The label and the time split (decided)

**Label.** For a bank-quarter row, `fails_within_4q = 1` if `quarters_until_failure` is 1, 2, 3 or 4; otherwise 0. Banks that never failed (null) and failures more than 4 quarters away are 0. (`quarters_until_failure` counts quarter-ends between the report date and the closure; 1 means that report was the bank's last before closing. A test already forbids values ≤ 0.)

**Split by report date.**

| Set | Report dates | Why |
|---|---|---|
| Train | 2001-03-31 to 2014-12-31 | Every label is fully determined by failures up to 2015-12-31, so training never depends on a failure after 2015. |
| Gap (unused) | 2015-03-31 to 2015-12-31 | These rows' labels would depend on 2016 failures, which belong to the test period. Dropping them keeps the boundary clean. |
| Test | 2016-03-31 to 2024-12-31 | The project's test window. Labels for the 2024 rows depend on failures through 2025-12-31, which are in the data (latest quarter 2026-06-30), so every test label is known. |
| Not scored | 2025-03-31 onward | Labels are censored: "not yet known", not "safe". |

Hyperparameters and early stopping use a time-based split *inside* the training years (e.g. fit on 2001–2011 report dates, validate on 2012–2014 with AUC or PR-AUC; builder may refine, but it must be time-ordered and stay within 2001–2014). The final model is then refit on all 2001–2014 rows with the chosen settings. *(Builder-check call.)*

**Training window wording.** The model learns from every failure from 2001 through 2015; rows *reported* in 2015 are dropped because their outcome depends on 2016. `CLAUDE.md` was reworded on 2026-11-11 to say exactly this (Victor's approval), and the decision note repeats it.

## 6. Features (decided at the group level; exact formulas are the builder's, logged)

Built in dbt from `fct_bank_quarters` columns, one row per `cert` + `report_date`, keys plus features only. All dollar fields are in thousands, so ratios are unit-free. Every division guards against a zero or null denominator and returns null. XGBoost handles nulls natively.

| CAMELS group | Features (plain English) |
|---|---|
| **C**apital | equity ÷ assets; leverage ratio; tier 1 risk-based ratio; total risk-based ratio |
| **A**sset quality | noncurrent loans ÷ loans; (nonaccrual assets + other real estate owned) ÷ assets; 30–89-day past-due ÷ assets; loan-loss allowance ÷ loans; net charge-offs ÷ loans (annualized); provision ÷ assets (annualized); construction loans ÷ loans; commercial real estate loans ÷ loans |
| **E**arnings | return on assets; return on equity; net interest margin; efficiency ratio; interest expense ÷ assets (annualized) |
| **L**iquidity | loans ÷ deposits; uninsured deposits ÷ deposits; brokered deposits ÷ deposits; core deposits ÷ assets; FHLB advances ÷ assets; volatile liabilities ÷ assets; cash ÷ assets |
| **S**ensitivity | held-to-maturity unrealized loss ÷ equity, i.e. (HTM cost − HTM fair value) ÷ equity; available-for-sale unrealized loss ÷ equity; securities ÷ assets |
| Size & growth | log of total assets; asset growth over 4 quarters; deposit growth over 4 quarters |

Notes the builder must handle:
- **Year-to-date fields.** `net_charge_offs`, `provision_for_credit_losses`, `total_interest_expense` and `net_income` are year-to-date dollars. They are annualized by × 4 ÷ (quarter number). FDIC's own ratios (`return_on_assets`, `return_on_equity`, `net_interest_margin`, `efficiency_ratio`) are already annualized and used as-is.
- **Growth features** look back to the same bank's row dated exactly 12 months earlier (matched on date, not on row position, so a gap in a bank's reporting gives null instead of a wrong comparison). They must never look forward. *(Builder-check call.)*
- **SVB check value.** At 2022-12-31, SVB's HTM unrealized loss ÷ equity ≈ 15.2 ÷ 15.5 ≈ 0.98 (README table). A dbt singular test pins it within a tolerance.

**0 vs "not reported" (decided rule, per-field details logged in a decision).** XGBoost treats null as "missing" and learns from it. A 0 that really means "not reported" would teach it something false. Profiling of the raw data (2002–2022, sampled year-ends) shows:
- `idt1rwajr` (tier 1 risk-based ratio) is 0 for about 1% of banks until 2019, then about 36% in 2022. That's the 2020 community bank leverage ratio option, under which small banks stop reporting risk-based ratios. **0 → null** for both risk-based ratios.
- Held-to-maturity cost (`scha`) and fair value (`schf`) are 0 for about 60% of banks, which mostly have no HTM bonds. That's a real 0, and the loss feature is 0. But where cost > 0 and fair value = 0 (more common in 2002–2006), **fair value → null**, and so does the loss feature.
- Uninsured deposits (`depunins`) are non-zero for about 99% of banks in every sampled year. Treat 0 as null. The README's "mainly available for $1B+ banks" limitation should be re-checked against this and corrected if it's wrong.
- Other fields: the builder profiles each and applies 0 → null only where the data shows "not reported" behavior, logging each rule.

## 7. Flagging and metrics (decided)

**Flag rule: a watchlist.** Each quarter, flag the riskiest **2%** of all banks reporting that quarter (no size or other filter; banks with missing features are still scored, since XGBoost handles nulls) by model score (about 90–120 banks in the test years), the way a supervisor's watchlist works. A ranking stays meaningful when failures are rare: the training years' crisis base rate would make raw probabilities run high in calm test years. The 2% is fixed now and not tuned on the test years.

**Metrics, on the test set (report dates 2016–2024):**
- **AUC.** How well scores separate rows with `fails_within_4q = 1` from 0 (bank-quarter level).
- **Recall (bank level).** Only reports dated 2016-03-31 to 2024-12-31 can count. A failed bank is in the denominator if it has at least one such report 1–4 quarters before its failure; recall is the share flagged in at least one of those reports. Banks whose only qualifying reports fall in the 2015 gap (e.g. a failure in early 2016) are excluded, and the denominator count is always shown next to the recall figure, because with a few dozen banks one bank moves recall noticeably. Also reported: recall when counting only flags at least 2 quarters before failure. *(Builder-check call.)*
- **Lead time.** For each caught bank, the largest `quarters_until_failure` among its flagged reports. Reported as median and range, with the reporting-lag caveat.
- **False-alarm rate.** Share of flagged bank-quarters where the bank does not fail within 4 quarters (= 1 − precision). Plus a bank-level count: distinct banks ever flagged that never failed in the window.
- **Baseline.** A single-rule ranking (builder's choice, logged, e.g. rank by (noncurrent loans + other real estate owned − allowance) ÷ (equity + allowance), a "Texas ratio"-style score) under the same 2% rule. This shows whether XGBoost adds anything over a classic analyst rule.
- **Case studies** (SVB 24735, Signature 57053, First Republic 59017): per quarter from 2021-03-31 to each bank's last report, the score, the national rank and percentile, flagged yes/no, and the top 5 signals behind the score (XGBoost's built-in per-row contributions, no extra library).

## 8. Data flow and where things live (decided)

```
fct_bank_quarters (Athena)
   | dbt build --select fct_bank_features     (needs Victor's yes)
   v
canary_marts.fct_bank_features (Athena, Parquet under dbt/)
   | python -m canary.export_features         (Athena query → local Parquet)
   v
data/features/fct_bank_features.parquet       (git-ignored)
   | python -m canary.model train / evaluate
   v
data/model/  model file, test-set scores, metrics.json, case_studies.csv   (git-ignored)
   |
   v
README results section, decision notes (committed, human-written from metrics.json)
```

- The export joins `fct_bank_features` to `fct_bank_quarters` on (`cert`, `report_date`) to carry the label inputs (`quarters_until_failure`, `failure_date`) and `institution_name` alongside the features, in clearly separate columns. The features table itself stays keys plus features only. Training selects an explicit feature list (§10 test). *(Builder-check call.)*
- The export uses the `canary` profile and workgroup. Its output staging lands under `athena-results/` (auto-deleted after 7 days), so no new delete permissions are needed. The builder picks the mechanism (plain query result download or `UNLOAD` to Parquet) and logs it. It must stay within the 1 GB scan limit, which a ~700K-row table easily does.
- Scores are not written back to AWS in Phase 3. Phases 5–6 decide how scores reach the agent and the dashboard.
- New dependencies: `xgboost` and `scikit-learn` (for AUC and simple utilities) in a `model` optional group. The builder may drop scikit-learn if it isn't needed.
- A fixed random seed, and the exact training configuration saved alongside `metrics.json`, so results reproduce.

## 9. Approaches considered (decided: A)

- **A. Features in dbt, model in Python locally (chosen).** Features become a tested, documented warehouse table, reusable by the Phase 5 agent and the Phase 6 dashboard. It also shows the data-engineering skill set the project targets. Cost: one export step, and dbt builds need Victor's approval.
- **B. Everything in pandas on local Parquet.** Fastest to build, but the features would live only in Python, untested in the warehouse, and would need rebuilding later for the dashboard and agent.
- **C. Train in AWS (SageMaker).** Rejected: costs money, is overkill for ~700K rows, and adds a service to explain without adding to the result.

## 9a. Build order (builder-check call)
Two stages. First, all code, the dbt model SQL and tests, and the Python pipeline with unit tests, using no AWS. Then the gated live stage: `dbt build --select fct_bank_features` only after Victor's yes, then export, train, evaluate.

## 10. Testing
- **dbt** (`fct_bank_features`):
  - `unique_combination_of_columns` on (`cert`, `report_date`); `not_null` on keys.
  - Row count equals `fct_bank_quarters`.
  - Ratio sanity ranges as warnings, e.g. shares between 0 and 1 where that must hold.
  - The SVB HTM-loss check value (§6).
  - A test that no growth feature is non-null for a bank's first 4 quarters of history.
- **pytest** (no AWS):
  - The label function (1–4 → 1; null, 0, 5+ → 0).
  - The split assigns every report date to exactly one of train, gap, test or not-scored, with the boundaries exactly as in §5.
  - The training set contains no row whose label depends on a failure after 2015-12-31.
  - The feature list excludes the label, name and date columns.
  - The flag rule flags `ceil` or `floor` (builder's choice, logged) of 2% per quarter.
  - The recall, lead-time and false-alarm functions, on a small hand-made example with known answers.
- One end-to-end smoke test: train on a tiny synthetic dataset, so the pipeline runs without real data.

## 11. Documentation
- `data-dictionary/fct_bank_features.md` (every feature: formula, meaning, units, null rule), enforced by the existing dictionary test.
- Decisions (next free numbers):
  - feature set and 0-handling rules
  - label and time split, including the 2015 gap
  - watchlist flag rule (2%) and metric definitions
  - export mechanism
- `runbooks/model-training.md`: export, train, evaluate, and what to do if each fails.
- README: a results section with the metrics, the baseline comparison and the case-study table, and an honest paragraph on what was or wasn't caught and why. The roadmap is updated, and TOOLS.md's XGBoost section moves from "planned" to what it does.
- `daily-log.md` at session end.

## 12. Left to the builder (log each choice)
Exact feature formulas within §6; per-field 0-handling beyond the three cases in §6; the internal validation split and the small hyperparameter grid; class-imbalance handling (e.g. `scale_pos_weight`); export mechanism; baseline rule; how flag ties and rounding are handled; module and file names beyond those named here.
