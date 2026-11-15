# 0015 — Failure-mix profiles

**Date:** 2026-11-11 (decided), 2026-11-14 (built and run)
**Status:** Accepted (cut-offs open for the owner's correction)

## Decision
To test "the model learned from the wrong kind of failure", every failed bank with a 2001-2014 report 1 to 4 quarters before failure is classified at its report **closest to failure**:

- **Credit-loss profile** ("its loans had gone bad"): `noncurrent_loans_to_loans >= 0.05`, or `texas_ratio >= 1.0`, or `texas_ratio < 0` (insolvent, [[decisions/0014-corrected-texas-baseline]]).
- **Run-risk profile** ("big bond losses and flighty deposits"): the report is on the run-risk 2% watchlist that quarter ([[decisions/0013-run-risk-check]]).
- Each bank is then `credit only`, `run-risk only`, `both` or `neither`. The three 2023 banks are classified the same way at their last report.

Code: `src/canary/replay/analysis.py`. Output: `training_mix.csv`, `failure_mix` in `posthoc_metrics.json` ([[replay_outputs]]).

## Why these cut-offs
They are round, common analyst rules of thumb, fixed in the spec before results were seen, not tuned: 5% noncurrent loans is a level examiners treat as serious trouble, and a Texas ratio of 100% means bad assets as large as the cushion to absorb them. Nulls count as "no".

## Why the row closest to failure
It is the bank's state when it was clearly failing, and it gives one row per bank. A report dated 2015 (the dropped gap year) never counts as training, so a bank whose only 1-4 quarter reports are in 2015 is left out.

## What it found (2026-11-14 run)
Of 539 training-era failures: 462 credit only, 53 both, 1 run-risk only (Independent Bankers Bank, 2009), 23 neither. So 515 (96%) had the credit-loss profile. The 2023 banks: SVB run-risk only; Signature and First Republic neither. Details: [[analysis/phase4-replay]].

## Alternatives
1. **Use the worst row in the 1-4 quarter window.** Rejected: "worst" needs a score to define it, which brings in the model.
2. **Cluster failures with machine learning.** Rejected: not explainable in one sentence.

## Open question
Are 5% and 100% the right rules of thumb? They are Claude's call in the spec; the owner may correct them. Changing them would change the counts, so any change is logged here.
