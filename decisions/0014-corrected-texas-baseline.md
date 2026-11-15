# 0014 — Corrected Texas-ratio baseline (post-hoc)

**Date:** 2026-11-11 (decided), 2026-11-14 (built and run)
**Status:** Accepted

## Decision
The Phase 3 baseline ranks banks by `texas_ratio` = (noncurrent loans + other real estate owned) / (equity + loan-loss allowance). When the denominator is below zero, the bank is insolvent, but the ratio comes out negative and the baseline ranked it as the **safest** bank. The corrected baseline treats every negative Texas ratio as **+infinity (worst)**. A null ratio (zero denominator) stays null and ranks last, as before. Ties among the +infinity rows resolve by cert.

**In one sentence:** a bank whose losses have already wiped out its capital goes to the top of the list, not the bottom.

This is safe because the numerator is a sum of non-negative amounts (`warehouse/models/marts/fct_bank_features.sql`), so a negative ratio can only come from a negative denominator.

Code: `corrected_texas_score` in `src/canary/replay/runrisk.py`. For AUC only, +infinity is replaced by a value just above the largest finite score (scikit-learn rejects infinity); the flags are computed before that.

## Why post-hoc
The bug was found while reading the Phase 3 test results (cert 9956, Bank of Mason, was missed by the baseline only because of the sign). Fixing a baseline after seeing which bank it missed is not a clean test, so the corrected numbers are reported separately and the Phase 3 table keeps the original baseline.

## What it found (2026-11-14 run, 2016-2024)
AUC 0.803 (was 0.774); recall 20 of 29 (was 19; the extra bank is cert 9956); recall at 2+ quarters 17 of 27 (unchanged); false-alarm banks 527 (was 544). The model's recall lead over the baseline shrinks to one bank (21 vs 20); the model's clearer advantage stays AUC (0.902). Details: [[analysis/phase4-replay]].

## Alternatives
1. **Leave the baseline as is.** Rejected: an analyst would never rank an insolvent bank as safest; keeping the bug overstates the model's edge.
2. **Drop insolvent rows.** Rejected: they are real, failing banks and belong at the top of any list.
3. **Rewrite Phase 3's `metrics.json`.** Rejected: the Phase 3 run is a single, recorded evaluation and is never rewritten.

Related: [[decisions/0011-watchlist-flag-and-metrics]], [[decisions/0013-run-risk-check]].
