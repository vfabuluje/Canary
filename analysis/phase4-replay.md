# Phase 4: SVB, Signature and First Republic replay and error analysis

**Date:** 2026-11-14 · **Spec:** [[specs/2026-11-11-phase4-replay-design]] · **Source files:** `data/replay/*` from `python -m canary.replay` (columns: [[replay_outputs]]) · **Research tool, not financial advice.**

> **Read this first: clean vs post-hoc.** The Phase 3 model was trained on 2001-2014 and tested once on 2016-2024; nothing here changes it, and its numbers below are as clean as that test. The **run-risk check** and the **corrected Texas baseline** were designed *after* seeing the 2023 failures. Every number from them is marked **(post-hoc)** and is not a fair out-of-sample result.

## The answer in brief
1. **Why the model missed them.** It learned from failures that were almost all bad-loan failures. 96% of the 539 training-era failures had a credit-loss profile; the three 2023 banks had none. In SVB's last report the model's score did not move at all when its held-to-maturity bond loss was varied from 0 to 150% of equity.
2. **The "wrong kind of failure in training" hypothesis holds.** Only 1 of 539 training-era failures looked like SVB (big bond losses, flighty deposits, clean loans). In the test years, 19 of the 21 failed banks the model caught had a credit-loss profile; none of the 8 it missed did.
3. **A simple run-risk check would have flagged SVB 4 quarters ahead (post-hoc)**, at rank 9 of 4,861 banks on the 2022-03-31 report. But it caught only 3 of 29 test-era failures, has an AUC of 0.515 (a coin flip as a general risk score), missed Signature in its last year and never flagged First Republic. It is a narrow detector for one kind of failure, not a replacement for the model.

## 1. Replay: the three banks quarter by quarter
Source: `replay_banks.csv`. Rank 1 = riskiest. The 2% watchlist takes rank <= 96 to 99 depending on the quarter (`k` = 99 at 2021-12-31, 98 at 2022-03-31, 97 at 2022-06-30 and 2022-09-30, 96 at 2022-12-31, 95 at 2023-03-31). Losses and uninsured share are fractions (0.98 = 98%).

**Silicon Valley Bank (cert 24735, failed 2023-03-10)**

| Report | Qtrs to failure | Model rank (pct) | Run-risk rank (post-hoc) | HTM loss / equity | AFS loss / equity | Uninsured / deposits |
|---|---|---|---|---|---|---|
| 2021-03-31 | 8 | 1263 (75.0) | 73 flagged | -0.00 | 0.02 | 0.86 |
| 2021-06-30 | 7 | 1018 (79.7) | 4471 | -0.01 | -0.01 | 0.86 |
| 2021-09-30 | 6 | 1142 (77.1) | 19 flagged | 0.03 | -0.01 | 0.87 |
| 2021-12-31 | 5 | 2160 (56.0) | 3 flagged | 0.07 | 0.01 | 0.87 |
| 2022-03-31 | 4 | 3638 (25.2) | **9 flagged** | 0.48 | 0.09 | 0.86 |
| 2022-06-30 | 3 | 4489 (7.2) | 63 flagged | 0.73 | 0.12 | 0.87 |
| 2022-09-30 | 2 | 3640 (24.4) | 70 flagged | 1.05 | 0.18 | 0.87 |
| 2022-12-31 | 1 | 3494 (26.8) | 54 flagged | 0.98 | 0.16 | 0.86 |

**Signature Bank (cert 57053, failed 2023-03-12)**

| Report | Qtrs to failure | Model rank (pct) | Run-risk rank (post-hoc) | HTM loss / equity | AFS loss / equity | Uninsured / deposits |
|---|---|---|---|---|---|---|
| 2021-03-31 | 8 | 1022 (79.8) | 95 flagged | -0.00 | 0.01 | 0.89 |
| 2021-06-30 | 7 | 831 (83.4) | 58 flagged | -0.00 | 0.01 | 0.91 |
| 2021-09-30 | 6 | 913 (81.7) | 29 flagged | 0.00 | 0.02 | 0.92 |
| 2021-12-31 | 5 | 986 (79.9) | 23 flagged | 0.01 | 0.03 | 0.92 |
| 2022-03-31 | 4 | 2456 (49.5) | 184 | 0.04 | 0.13 | 0.92 |
| 2022-06-30 | 3 | 2162 (55.3) | 348 | 0.06 | 0.21 | 0.91 |
| 2022-09-30 | 2 | 420 (91.3) | 300 | 0.10 | 0.33 | 0.91 |
| 2022-12-31 | 1 | 246 (94.9) | 247 | 0.10 | 0.31 | 0.90 |

**First Republic Bank (cert 59017, failed 2023-05-01)**

| Report | Qtrs to failure | Model rank (pct) | Run-risk rank (post-hoc) | HTM loss / equity | AFS loss / equity | Uninsured / deposits |
|---|---|---|---|---|---|---|
| 2021-03-31 | 9 | 995 (80.3) | 4940 | -0.07 | 0.00 | 0.72 |
| 2021-06-30 | 8 | 1327 (73.6) | 4925 | -0.10 | 0.00 | 0.73 |
| 2021-09-30 | 7 | 566 (88.7) | 4867 | -0.07 | 0.00 | 0.74 |
| 2021-12-31 | 6 | 948 (80.7) | 4811 | -0.07 | 0.00 | 0.75 |
| 2022-03-31 | 5 | 3502 (28.0) | 625 | 0.10 | 0.01 | 0.74 |
| 2022-06-30 | 4 | 3262 (32.6) | 599 | 0.22 | 0.02 | 0.72 |
| 2022-09-30 | 3 | 3095 (35.7) | 608 | 0.33 | 0.03 | 0.69 |
| 2022-12-31 | 2 | 3355 (29.7) | 606 | 0.27 | 0.03 | 0.68 |
| 2023-03-31 | 1 | 809 (83.0) | 895 | 0.23 | 0.02 | 0.49 |

The corrected Texas baseline (post-hoc) never flagged any of the three; their best rank was 1,806 (Signature, 2022-12-31). Their Texas ratios were tiny (0.009, 0.028 and 0.007 at their last reports, `training_mix.csv`): their loans were fine.

## 2. Why each bank was missed
Source: `contributions.csv` (log-odds units; positive pushes toward "will fail").

- **SVB, 2022-12-31.** Up: AFS loss / equity +0.804, efficiency ratio +0.159, CRE loans +0.118. Down: interest expense / assets -1.065, Tier 1 ratio -1.054, Texas ratio -0.987, securities / assets -0.864, return on equity -0.506. The HTM loss (0.98 of equity) is in neither top five. Cheap deposits, strong capital, clean loans and a big bond book all read as "safe" to a model trained on bad-loan failures.
- **Signature, 2022-12-31.** Up: AFS loss / equity +2.063 (the largest single push of any of the three banks), efficiency ratio +0.186, asset growth +0.101. Down: interest expense -0.854, Texas ratio -0.793, Tier 1 ratio -0.672, ROE -0.392, noncurrent loans -0.342. The AFS signal got it to rank 246, about 2.5 times too far down the list to be flagged.
- **First Republic, 2023-03-31.** Up: volatile liabilities / assets +0.357, CRE loans +0.306. This is the one report where funding stress shows: its uninsured share fell from 0.68 to 0.49 in the quarter (`replay_banks.csv`), consistent with uninsured depositors leaving in March 2023. Down: Tier 1 ratio -0.986, Texas ratio -0.902, noncurrent loans -0.546. Bond losses barely register: First Republic's main exposure was low-rate mortgages it held as **loans**, and the FDIC call-report financials give fair values for securities only, so no feature in this dataset can see that loss. (No dollar figure is quoted here because none was verified from a cited source.)

## 3. What-if: can the model react to these signals at all?
Source: `what_if.csv`. One feature changed at a time, everything else as reported, re-scored with the saved model, and ranked against the other banks' real scores that quarter.

| Bank, report | Feature (actual) | Score range over the grid | Best rank / banks |
|---|---|---|---|
| SVB 2022-12-31 | HTM loss / equity (0.98), 0 to 1.5 | **0.0023 to 0.0023 (flat)** | 3494 / 4773 |
| SVB 2022-12-31 | AFS loss / equity (0.16), 0 to 1.0 | 0.0009 to 0.0075 | 1948 / 4773 |
| SVB 2022-12-31 | Uninsured / deposits (0.86), 0 to 1.0 | 0.0022 to 0.0033 | 3019 / 4773 |
| Signature 2022-12-31 | HTM loss / equity (0.10) | 0.0296 to 0.0410 | 134 / 4773 |
| Signature 2022-12-31 | AFS loss / equity (0.31) | 0.0017 to 0.0296 | 246 / 4773 |
| Signature 2022-12-31 | Uninsured / deposits (0.90) | 0.0296 to 0.0372 | 154 / 4773 |
| First Republic 2023-03-31 | HTM loss / equity (0.23) | **0.0176 to 0.0176 (flat)** | 809 / 4740 |
| First Republic 2023-03-31 | AFS loss / equity (0.02) | 0.0133 to 0.0341 | 298 / 4740 |
| First Republic 2023-03-31 | Uninsured / deposits (0.49) | 0.0176 to 0.0231 | 543 / 4740 |

**Finding.** For SVB and First Republic the model is completely flat in HTM loss: any value from 0 to 150% of equity gives the same score. This also explains the Phase 3 puzzle of SVB's identical 2022-09-30 and 2022-12-31 scores. AFS loss moves the score (it did occur in training failures), but no single change gets any of the three banks onto the list (rank 95 or 96 needed). The model cannot be "nudged" into catching SVB; it simply never learned what an HTM loss means.

## 4. The training years: what kind of failures the model learned from
Source: `training_mix.csv`, `failure_mix` in `posthoc_metrics.json`. Rules: [[decisions/0015-failure-mix-profiles]] (credit loss = noncurrent loans >= 5% or Texas ratio >= 100% or insolvent; run-risk = on the run-risk 2% list that quarter).

| Profile | Training-era failures (2001-2014 reports) | 2023 banks |
|---|---|---|
| Credit only | 462 | 0 |
| Both | 53 | 0 |
| Run-risk only | 1 (Independent Bankers Bank, failed 2009-12-18) | 1 (SVB) |
| Neither | 23 | 2 (Signature, First Republic) |
| **Total** | **539** | **3** |

515 of 539 (96%) training-era failures had bad loans; 389 of the 539 failed in 2009-2011 alone. Only one looked like SVB.

**Bond losses and uninsured deposits in training** (`distributions.csv`):

| | Bond loss / equity: median, p90, p99 | Share > 0.3 | Uninsured / deposits: median, p90 |
|---|---|---|---|
| Training failures (2,134 rows 1-4 qtrs before failure) | -0.00, 0.14, 1.40 | 5.3% | 0.08, 0.29 |
| All training rows (470,361) | -0.01, 0.03, 0.16 | 0.3% | 0.16, 0.37 |
| SVB, last report | 1.14 | | 0.86 |
| Signature, last report | 0.40 | | 0.90 |
| First Republic, last report | 0.25 | | 0.49 |

Two things stand out:
- **Training failures had *fewer* uninsured deposits than other banks** (median 8% vs 16%). The model had every reason to read a high uninsured share as normal, or even safe.
- **The few large bond-loss ratios among training failures came from vanishing equity, not big bond books.** The 105 training-failure rows with bond loss above 30% of equity had a median equity / assets of 1.6%, against 3.5% for all training-failure rows and 10.1% for all training rows (one-off check on the feature export). A 30% ratio on a nearly insolvent bank is a different signal from SVB's, whose equity was intact while its bonds lost value.

## 5. The run-risk check (post-hoc)
Source: `posthoc_metrics.json`. Rule: [[decisions/0013-run-risk-check]] (`clip(uninsured, 0, 1) x (HTM + AFS loss) / equity`, top 2% per quarter).

| Metric (2016-2024) | Phase 3 model (clean) | Run-risk (post-hoc) | Corrected Texas baseline (post-hoc) |
|---|---|---|---|
| AUC | 0.902 | 0.515 | 0.803 |
| Recall, 1-4 qtrs | 21 of 29 | 3 of 29 | 20 of 29 |
| Recall, 2+ qtrs | 18 of 27 | 3 of 27 | 17 of 27 |
| Lead time, median | 4 | 4 | 4 |
| False-alarm rate | 98.3% | 99.7% | 98.3% |
| Never-failed banks flagged | 746 | 846 | 527 |
| Rows with no score | 0 | 2,676 | 612 |

- **Caught by run-risk:** SVB (first flagged 2022-03-31, 4 quarters ahead, rank 9 of 4,861), Republic First Bank (cert 27332, failed 2024-04-26, 4 quarters ahead) and City National Bank of New Jersey (cert 21111, failed 2019-11-01, 4 quarters ahead). Republic First was also caught by the model; City National by the model and the corrected baseline. **SVB is the only bank the run-risk check adds.**
- **Signature: a miss.** It was on the run-risk list for 2021-03-31 to 2021-12-31 (5 to 8 quarters before failing, outside the label window) and then fell to ranks 184-348 in 2022, as rising rates gave hundreds of other banks bond losses too. On 2022-09-30, 458 banks had a run-risk score above 0.3 and 1,360 had bond losses at least half their equity.
- **First Republic: a miss.** Never on the list; best rank 599 (2022-06-30).
- **It is not a general risk score.** AUC 0.515 on 2016-2024 and 0.569 on 2001-2014 (95 of 539 caught): bond losses and uninsured deposits are not what sank most banks.
- **It flags SVB in calm years too.** SVB was on the run-risk list in 2005-2007 and 2017-2018 (`case_study_flags`), when it did not fail: a high uninsured share alone keeps a bank near the list whenever it has any bond loss.
- **Overlap with the model** (2016-2024): 216 rows (82 banks) were on both lists; 3,567 rows on each list were on that list only. The two lists mostly flag different banks.

## 6. The corrected Texas baseline (post-hoc)
Rule: [[decisions/0014-corrected-texas-baseline]] (an insolvent bank, negative Texas ratio, ranks worst instead of safest). Recall rises from 19 to 20 of 29 (the extra bank is cert 9956, Bank of Mason, failed 2016-04-29) and AUC from 0.774 to 0.803. **The model's recall edge over a fair baseline is one bank (21 vs 20).** Its real advantage is the ranking (AUC 0.902 vs 0.803) and fewer missing scores.

## 7. The model's other test-era misses and false alarms
Source: `test_misses.csv`. The model missed 8 of 29 eligible failed banks:

| Bank (cert) | Failed | Best report (qtrs before) | Best percentile | Top signals | Credit-loss profile |
|---|---|---|---|---|---|
| Washington Federal Bank for Savings (30570) | 2017-12-15 | 2017-09-30 (1) | 35.7 | securities / assets, CRE loans | no |
| Enloe State Bank (10716) | 2019-05-31 | 2018-12-31 (2) | 92.2 | construction loans, CRE loans | no |
| Silicon Valley Bank (24735) | 2023-03-10 | 2022-12-31 (1) | 26.8 | AFS loss, efficiency | no |
| Signature Bank (57053) | 2023-03-12 | 2022-12-31 (1) | 94.9 | AFS loss, efficiency | no |
| First Republic Bank (59017) | 2023-05-01 | 2023-03-31 (1) | 83.0 | volatile liabilities, CRE loans | no |
| Heartland Tri-State Bank (25851) | 2023-07-28 | 2023-03-31 (2) | 93.1 | AFS loss, equity / assets | no |
| Pulaski Savings Bank (28611) | 2025-01-17 | 2024-06-30 (3) | 57.1 | securities / assets, size | no |
| Santa Anna National Bank (5520) | 2025-06-27 | 2024-09-30 (3) | 95.9 | AFS loss, efficiency | no |

**None of the 8 misses had a credit-loss profile on its best report; 19 of the 21 banks the model caught did** (same rule applied to each caught bank's report closest to failure; one-off check, not an output file). The model is a good detector of bad-loan failures and blind to failures that look healthy on the loan book, whatever their cause. Why each of these banks failed (for example fraud vs funding) is not checked here.

**False alarms** (`false_alarm_profile.csv`, 65 true-alarm rows vs 3,718 false-alarm rows): at the median, true alarms were deeply troubled (equity 2.4% of assets, Texas ratio 1.67, return on assets -2.8%, noncurrent loans 10.4%), while false alarms looked much closer to ordinary banks (equity 8.3%, Texas ratio 0.18, ROA +0.43%, noncurrent loans 2.2%). The ten banks flagged most often without failing were each flagged in 28 to 36 of the 36 test quarters (`top_false_alarm_banks.csv`); a persistent flag on a bank that stays open for nine years is a sign that bank is structurally unusual, not that it is failing.

## 8. What this means
- **The headline stays the clean result:** a model trained on 2001-2014 caught 21 of 29 test-era failures and missed SVB, Signature and First Republic.
- **The miss is explained, not just reported.** The training years contain almost no bank that failed with clean loans, and the model is literally flat in the one feature (HTM loss) that told SVB's story.
- **A one-line run-risk rule would have put SVB on a 2% watchlist a year before it failed (post-hoc)**, but it would also have flagged 846 banks that never failed, missed Signature and First Republic, and it adds no general skill. It is a useful second lens, not a fix.
- **First Republic is a data limit, not only a model limit:** its loan losses are invisible in FDIC financials.

## Limitations of this analysis
- Run-risk and corrected-baseline results are post-hoc (designed after seeing 2023).
- Lead times are from the report date; reports become public about a month later ([[decisions/0011-watchlist-flag-and-metrics]]).
- FDIC data shows current, amended values, not what was filed at the time.
- Small samples: 29 eligible test-era failures, 3 case-study banks.
- The failure-mix cut-offs are rules of thumb ([[decisions/0015-failure-mix-profiles]]).
