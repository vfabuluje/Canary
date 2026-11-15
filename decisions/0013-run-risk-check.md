# 0013 — The run-risk check (post-hoc)

**Date:** 2026-11-11 (decided), 2026-11-14 (built and run)
**Status:** Accepted

## Decision
Phase 4 adds one simple, explainable check next to the Phase 3 model, never mixed into it:

```
bond_loss_to_equity = htm_unrealized_loss_to_equity + afs_unrealized_loss_to_equity
run_risk_score      = clip(uninsured_to_deposits, 0, 1) * bond_loss_to_equity
```

**In one sentence:** how much of the bank's equity its bond losses have already eaten, weighted by how much of its deposits could run. Large losses with sticky insured deposits score low, flighty deposits with no losses score low, and only the combination scores high.

- **Nulls.** One loss feature null counts as 0; both null gives null. Null uninsured gives a null score. Null scores rank last.
- **Gains are kept.** A negative loss (bonds worth more than cost) gives a negative score, so the bank ranks low.
- **Uninsured is clipped to 0-1** because 144 rows have reporting errors outside that range ([[fct_bank_features]]).
- **The flag** is the same 2% watchlist as the model ([[decisions/0011-watchlist-flag-and-metrics]]): top 2% per quarter, rounded up, ties by cert.
- **Scored on every quarter 2001-2024.** Nothing is trained, so the 2001-2014 numbers carry no leakage; they show how the check would have done in the credit-crisis years.
- **Code:** `src/canary/replay/runrisk.py`. Output: `posthoc_metrics.json` ([[replay_outputs]]).

## Why it is labeled post-hoc
The formula was chosen after seeing that SVB, Signature and First Republic were missed, and a scratch look before the spec showed SVB ranking 3rd to 70th on it in 2022. A check designed with the answer in view is not an out-of-sample test. So every run-risk number carries "post-hoc" in the JSON, the report and the README, and the README headline stays the clean Phase 3 result. The formula and the 2% share were fixed in the spec before the results were computed, and no variant was tried.

## Why a continuous score and the 2% list
It reuses decision 0011's rule, so there is no cut-off to pick with SVB in view, and it is measured with the same metric code as the model.

## What it found (2026-11-14 run)
On 2016-2024 it caught 3 of 29 failed banks (SVB, Republic First Bank, City National Bank of New Jersey), all 4 quarters ahead, with AUC 0.515 (a coin flip) and 846 never-failed banks flagged. On 2001-2014 it caught 95 of 539 (AUC 0.569). It is a narrow detector of one failure type, not a general risk score. Details: [[analysis/phase4-replay]].

## Alternatives
1. **Fixed thresholds** (bond losses >= 50% of equity and uninsured >= 50%). Simplest to say, but the cut-offs would be picked after seeing SVB. Rejected.
2. **Combine model and run-risk into one list.** One headline recall, but it blurs the clean test with the post-hoc check. Rejected.
3. **Retrain the model with new features.** Out of scope for Phase 4 (spec non-goal); it would also make 2016-2024 no longer a clean test.

Related: [[decisions/0014-corrected-texas-baseline]], [[decisions/0015-failure-mix-profiles]].
