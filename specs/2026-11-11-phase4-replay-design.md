# Phase 4 Spec: SVB / Signature / First Republic Replay and Error Analysis

**Date:** 2026-11-11
**Status:** Approved by Victor 2026-11-11
**Phase:** 4 (see `CLAUDE.md`)

## 1. Intent: why this exists

Phase 3 answered the headline question honestly: an XGBoost model trained on 2001-2014 report dates did **not** flag SVB, Signature or First Republic in any quarter. It also found the first reason: in SVB's 2022 reports, strong capital, low interest expense and a large securities book pushed the score toward "safe", and the model barely reacted to an HTM bond loss of about 98% of equity, because almost no training-era failure had a bond loss that large.

Phase 4 turns that miss into the project's most useful finding. It asks three questions:
1. **Why exactly** was each of the three banks missed? (Error analysis, using only the existing model.)
2. **Is the "wrong kind of failure in training" hypothesis true?** Were 2001-2014 failures mostly bad-loan failures, with almost no bond-loss or uninsured-run profile?
3. **What public signal would have caught them, and at what cost in false alarms?** A simple, explainable run-risk check, evaluated the same way as the model.

The point for a reader (a bank data team, an interviewer) is: the project can say *why* a model failed, show a signal that would have worked, and keep that post-hoc fix clearly separate from the clean test.

## 2. Goals
- G1. **Replay tables** for SVB (cert 24735), Signature (57053) and First Republic (59017): every quarter from 2021-03-31 to each bank's last report, side by side: model score, rank and flag; run-risk score, rank and flag; corrected-baseline rank and flag; the key raw ratios (HTM and AFS loss ÷ equity, uninsured ÷ deposits, tier 1 ratio, interest expense ÷ assets, securities ÷ assets).
- G2. **A run-risk check** (post-hoc): score each bank-quarter, rank within quarter, flag the top 2% (decision 0011's watchlist rule). Report recall, recall at 2+ quarters, lead time, false-alarm rate, false-alarm banks and AUC on 2016-2024 with the existing metric functions, plus whether and when it flags each of the three banks.
- G3. **A corrected Texas-ratio baseline** (post-hoc): a negative denominator (equity + allowance ≤ 0, i.e. an insolvent bank) ranks as worst, not safest. Same metrics.
- G4. **Training-era failure mix**: classify every failed bank with a training row 1-4 quarters before failure by its profile at that row (credit-loss, run-risk, both, neither), and compare with the three 2023 banks.
- G5. **Model sensitivity ("what-if")**: for SVB's 2022-12-31 row, vary one feature at a time across a grid (HTM loss ÷ equity, AFS loss ÷ equity, uninsured ÷ deposits) holding the rest fixed, and record the model's score and national rank. This shows directly whether the model can react to these signals at all.
- G6. **Test-set misses and false alarms**: the 8 eligible failed banks the model missed (of 29), with their top signals at their best-ranked row; and a profile of false alarms (flagged rows of banks that did not fail) vs true alarms, by median feature value.
- G7. **A written report**, `analysis/phase4-replay.md` (committed, Obsidian note), with the numbers from G1-G6 and plain-English conclusions; README results and limitations updated; decisions logged.
- G8. Unit tests for every new function (no AWS, no network).

## 3. Non-goals
- **Retraining or changing the Phase 3 model.** `data/model/model.json`, `metrics.json` and `scores_test.parquet` are read, never rewritten.
- New features in dbt or new FDIC fields. Everything is computed from the existing `fct_bank_features` export.
- Combining the model and the run-risk check into one list (option 3, rejected: it mixes the clean test with the post-hoc check).
- Loan-level unrealized losses (First Republic's main problem). The FDIC data has no fair value for loans (§8).
- AI analyst agent, bank notes, dashboard (Phases 5-6).
- Any AWS use. Phase 4 runs entirely locally on files that already exist.

## 4. Anti-goals (a failure even if it "works")
- **Passing post-hoc results off as out-of-sample.** Every run-risk and corrected-baseline number is labeled "post-hoc (designed after seeing the 2023 failures)" in `posthoc_metrics.json`, the report and the README. The README headline stays the Phase 3 clean result.
- **Tuning the run-risk check to the three banks.** The formula and the 2% share are fixed in this spec before results are computed. No alternative formulas, weights or shares are tried and then picked by how well they catch SVB. If a variant is shown at all, it is shown next to the fixed one, never instead of it.
- **Overclaiming.** "Would have caught SVB" is only said with its rank, the quarter, the lead time (report date, one-month lag caveat) and the number of other banks on the same list that quarter. First Republic is called a miss for the run-risk check if it is a miss.
- **Overwriting Phase 3 outputs.** The new CLI writes only to its own output folder.
- **Unexplainable analysis.** Every rule (run-risk formula, credit-loss profile thresholds) has one plain-English sentence Victor can say out loud.

## 5. Approaches considered (decided: 1)

1. **Separate 2% run-risk watchlist ranked by a continuous score (chosen).** It reuses decision 0011's watchlist rule, so there is no threshold to tune with SVB in view, and it is evaluated with the same metric functions as the model.
2. **Fixed thresholds** (e.g. bond losses ≥ 50% of equity and uninsured ≥ 50% of deposits). Simplest to explain, but the cut-offs would be chosen after seeing SVB, which is hard to defend. A quick look shows that rule flags 62 banks at 2022-12-31.
3. **Combined list (model OR run-risk).** One headline recall number, but it blurs the clean model with the post-hoc check. Rejected.

Pre-spec look (scratch, not saved): with approach 1, SVB ranks 3rd-70th of ~4,800 banks every quarter 2021-12-31 to 2022-12-31 (top 2% ≈ 96 banks); Signature ranks 23rd at 2021-12-31 then 184th-348th; First Republic ~87th percentile. These numbers were seen before this spec was written, which is exactly why approach 1 is labeled post-hoc.

## 6. The run-risk check (decided)

**Plain English:** "How much of the bank's equity its bond losses have already eaten, weighted by how much of its deposits could run." A bank with large losses but sticky insured deposits, or flighty deposits but no losses, scores low; only the combination scores high.

**Formula**, per bank-quarter, from existing `fct_bank_features` columns:

```
bond_loss_to_equity = htm_unrealized_loss_to_equity + afs_unrealized_loss_to_equity
run_risk_score      = clip(uninsured_to_deposits, 0, 1) * bond_loss_to_equity
```

- Null handling: if both loss features are null, `bond_loss_to_equity` is null; if one is null, use the other. If `uninsured_to_deposits` is null, the score is null. Null scores rank lowest (existing `flag_watchlist` behavior).
- Negative losses (unrealized gains) are kept, so such banks rank low.
- `uninsured_to_deposits` is clipped to [0, 1] because 144 rows have reporting errors outside that range (data dictionary).
- **Flag:** `flag_watchlist(df, "run_risk_score")`, top 2% per quarter, same ceil and tie rule.
- **Scored on** every quarter 2001-03-31 to 2024-12-31 (all labeled report dates, including the 2015 gap year since nothing is trained). Metrics are reported for the 2016-2024 test window (comparable with Phase 3) and separately for 2001-2014 (how the check would have done in the credit-crisis years). No training, so there is no leakage concern from using 2001-2014.
- Also reported: overlap with the model's watchlist on 2016-2024 (rows and banks flagged by both).

## 7. The corrected baseline (decided)

Phase 3's baseline ranks by `texas_ratio`, whose denominator is equity + allowance. When that denominator is ≤ 0 the bank is insolvent, but the ratio goes negative and ranks as safest. Corrected rule: every row with a negative `texas_ratio` is treated as **+infinity** (worst). This is safe because the numerator (noncurrent loans + other real estate owned, `warehouse/models/marts/fct_bank_features.sql`) is a sum of non-negative amounts, so a negative ratio can only come from a negative denominator. A null ratio (zero denominator) stays null and ranks lowest, as before. Ties among the +infinity rows resolve by `cert`, as in decision 0011. Same metrics as §6 on 2016-2024. Labeled post-hoc.

## 8. Error analysis (decided at the level of what; exact cut-offs are the builder's, logged)

**8.1 Training-era failure mix (G4).** For each failed bank with at least one training row (report date 2001-2014) 1-4 quarters before failure, take its row closest to failure and classify:
- **Credit-loss profile:** `noncurrent_loans_to_loans` ≥ 0.05 **or** `texas_ratio` ≥ 1.0 (or the corrected texas rule says insolvent). One sentence: "its loans had gone bad."
- **Run-risk profile:** the row is in the top 2% of `run_risk_score` that quarter.
- Cross-tab: credit only / run-risk only / both / neither, with counts by failure year. Then the same classification for the three 2023 banks at their last pre-failure row.
- The thresholds are round, standard analyst rules of thumb, fixed here, not tuned. *(The ≥ 5% noncurrent and Texas ≥ 100% cut-offs are Claude's call, offered for Victor's correction.)*
- Also: distribution (median, 90th, 99th percentile) of `bond_loss_to_equity` and `uninsured_to_deposits` among training positive rows vs all training rows vs the three banks.

**8.2 What-if (G5).** SVB 2022-12-31 row. For each of HTM loss ÷ equity (0 to 1.5 in steps of 0.1), AFS loss ÷ equity (0 to 1.0), uninsured ÷ deposits (0 to 1.0): replace that one value, score with the saved model, and compute the rank the score would get among all banks' real scores that quarter. Output one table. Same for Signature 2022-12-31 and First Republic 2023-03-31 (their last reports).

**8.3 Why each bank was missed (G1 + contributions).** For each of the three banks' last two reports: the top 5 positive and top 5 negative per-feature contributions (XGBoost built-in `pred_contribs`, as in Phase 3). Phase 3 listed positive signals only; Phase 4 adds the negatives because the miss is about what pushed the score *down*.

**8.4 Test-set misses and false alarms (G6).**
- The 8 missed eligible banks: cert, name, failure date, best (highest) model percentile in their 1-4 quarter window, top 3 signals at that row, and the profile from §8.1.
- False vs true alarms on 2016-2024 model-flagged rows: median of each feature for flagged-and-failed-within-4q vs flagged-and-did-not, and the 10 banks flagged most often that never failed by 2025-12-31.

**8.5 First Republic and the data limit.** The report states plainly that First Republic's main loss was on low-rate mortgages held as loans, and FDIC call-report financials give fair values for securities only, so no feature in this dataset can see it. *(Builder or Victor to confirm the specific public figure cited, e.g. from First Republic's 10-K fair-value note, before quoting a number; otherwise describe it without a number.)*

## 9. Data flow and where things live (decided)

```
data/features/fct_bank_features.parquet   (Phase 3 export, read-only)
data/model/model.json, scores_test.parquet  (Phase 3, read-only)
   | python -m canary.replay --features ... --model-dir data/model --out data/replay
   v
data/replay/   (git-ignored)
   posthoc_metrics.json      run-risk + corrected baseline metrics, both windows, labeled post_hoc: true
   replay_banks.csv          G1, one row per bank-quarter for the three banks
   contributions.csv         §8.3
   what_if.csv               §8.2
   training_mix.csv          §8.1 per bank; summary in posthoc_metrics.json
   test_misses.csv           §8.4
   false_alarm_profile.csv   §8.4
   |
   v
analysis/phase4-replay.md, README, decisions (committed, written from those files)
```

- New package `src/canary/replay/` with `runrisk.py` (score, corrected baseline), `analysis.py` (mix, what-if, contributions, misses), `__main__.py` (CLI). It reuses `canary.model.dataset` and `canary.model.metrics`; it does not modify them except to add pure helpers if needed.
- The CLI refuses to run if `--out` equals the Phase 3 model folder.
- No new dependencies.
- Note: the local data paths are `data.nosync/...` on Victor's machine (iCloud exclusion); CLI arguments, not hard-coded paths.

## 10. Testing
- pytest, no AWS:
  - `run_risk_score`: hand-made rows covering both-null, one-null, uninsured null, uninsured > 1 (clipped), negative loss.
  - Corrected baseline: an insolvent row ranks above every solvent row; ordinary rows keep their order.
  - Failure-mix classifier: one row per category with known answers; picks the row closest to failure; only training-window rows used.
  - What-if: changes exactly one feature, leaves the input frame unchanged, rank computed against the quarter's real scores (tiny synthetic model, as in Phase 3's smoke test).
  - Contributions: positive and negative lists are sorted and of length ≤ 5.
  - CLI: refuses to write into the model folder; end-to-end smoke run on synthetic data writes every output file.
- No dbt changes, so no new dbt tests. (CLAUDE.md's dbt rule applies to dbt models; none are added.)

## 11. Documentation
- `analysis/phase4-replay.md`: the story in plain English, with tables from §8 and the post-hoc label on every post-hoc number. Linked from README.
- Decisions: **0013** run-risk check (formula, why continuous + 2%, why post-hoc, rejected options); **0014** corrected Texas baseline; **0015** failure-mix profile rules.
- `data-dictionary/`: the run-risk score and the output files' columns get an entry (`data-dictionary/replay_outputs.md`), even though they are files, not warehouse tables, so every column the README cites is defined.
- `runbooks/model-training.md`: add a "Phase 4 replay" section (command, inputs, outputs, failure modes).
- `reference/GLOSSARY.md`: add "post-hoc", "run-risk score", "what-if analysis" if missing.
- README: keep the clean Phase 3 result as the headline; add a clearly labeled post-hoc section with the run-risk and corrected-baseline results and the First Republic data limit; update the roadmap.
- `daily-log.md` at session end.

## 12. Left to the builder (log each choice)
Module internals and function names beyond §9; grid step sizes in §8.2 if the ones given are impractical; how AUC treats null run-risk scores (exclude or rank lowest, stated next to the number); whether `replay_outputs.md` needs an exemption in the data-dictionary test (which checks dbt columns); the exact columns of each output file (documented in the dictionary); the report's layout.
