# Canary: detailed results (Phase 3)

**Research tool, not financial advice.**

This page holds the full detail behind the [README](README.md)'s results: every quarter of the three 2023 case studies, with the signals that pushed each score up, and the full analysis of why the model did not flag them. The README has the summary and the headline metrics.

## Case studies: SVB, Signature, First Republic
**None of the three was flagged in any quarter.** Percentile is the bank's score rank among all banks that quarter (99 = riskier than 99% of banks; the flag needs about the top 2%, so roughly 98 or higher). The top signal is the feature that pushed the bank's score up most.

**Silicon Valley Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 8 | 75.0 | 1263 / 5044 | no | deposit_growth_4q=+0.327, cre_loans_to_loans=+0.229, efficiency_ratio=+0.133 |
| 2021-06-30 | 7 | 79.7 | 1018 / 5015 | no | deposit_growth_4q=+0.364, cre_loans_to_loans=+0.196, efficiency_ratio=+0.100 |
| 2021-09-30 | 6 | 77.1 | 1142 / 4979 | no | deposit_growth_4q=+0.350, cre_loans_to_loans=+0.230, leverage_ratio=+0.081 |
| 2021-12-31 | 5 | 56.0 | 2160 / 4904 | no | deposit_growth_4q=+0.333, cre_loans_to_loans=+0.163, efficiency_ratio=+0.107 |
| 2022-03-31 | 4 | 25.2 | 3638 / 4861 | no | deposit_growth_4q=+0.281, cre_loans_to_loans=+0.180, afs_unrealized_loss_to_equity=+0.169 |
| 2022-06-30 | 3 | 7.2 | 4489 / 4838 | no | efficiency_ratio=+0.190, cre_loans_to_loans=+0.163, afs_unrealized_loss_to_equity=+0.156 |
| 2022-09-30 | 2 | 24.4 | 3640 / 4813 | no | afs_unrealized_loss_to_equity=+0.798, efficiency_ratio=+0.167, cre_loans_to_loans=+0.123 |
| 2022-12-31 | 1 | 26.8 | 3494 / 4773 | no | afs_unrealized_loss_to_equity=+0.804, efficiency_ratio=+0.159, cre_loans_to_loans=+0.118 |

**Signature Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 8 | 79.8 | 1022 / 5044 | no | deposit_growth_4q=+0.325, efficiency_ratio=+0.291, loans_to_deposits=+0.149 |
| 2021-06-30 | 7 | 83.4 | 831 / 5015 | no | deposit_growth_4q=+0.308, efficiency_ratio=+0.256, loans_to_deposits=+0.155 |
| 2021-09-30 | 6 | 81.7 | 913 / 4979 | no | deposit_growth_4q=+0.299, efficiency_ratio=+0.214, loans_to_deposits=+0.155 |
| 2021-12-31 | 5 | 79.9 | 986 / 4904 | no | deposit_growth_4q=+0.294, efficiency_ratio=+0.215, loans_to_deposits=+0.158 |
| 2022-03-31 | 4 | 49.5 | 2456 / 4861 | no | efficiency_ratio=+0.333, afs_unrealized_loss_to_equity=+0.290, deposit_growth_4q=+0.190 |
| 2022-06-30 | 3 | 55.3 | 2162 / 4838 | no | afs_unrealized_loss_to_equity=+0.848, efficiency_ratio=+0.333, loans_to_deposits=+0.146 |
| 2022-09-30 | 2 | 91.3 | 420 / 4813 | no | afs_unrealized_loss_to_equity=+1.999, efficiency_ratio=+0.268, core_deposits_to_assets=+0.042 |
| 2022-12-31 | 1 | 94.9 | 246 / 4773 | no | afs_unrealized_loss_to_equity=+2.063, efficiency_ratio=+0.186, asset_growth_4q=+0.101 |

**First Republic Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 9 | 80.3 | 995 / 5044 | no | cre_loans_to_loans=+0.274, deposit_growth_4q=+0.227, past_due_30_89_to_assets=+0.074 |
| 2021-06-30 | 8 | 73.6 | 1327 / 5015 | no | cre_loans_to_loans=+0.302, deposit_growth_4q=+0.220, leverage_ratio=+0.061 |
| 2021-09-30 | 7 | 88.7 | 566 / 4979 | no | cre_loans_to_loans=+0.328, deposit_growth_4q=+0.250, past_due_30_89_to_assets=+0.083 |
| 2021-12-31 | 6 | 80.7 | 948 / 4904 | no | cre_loans_to_loans=+0.350, deposit_growth_4q=+0.236, afs_unrealized_loss_to_equity=+0.056 |
| 2022-03-31 | 5 | 28.0 | 3502 / 4861 | no | cre_loans_to_loans=+0.242, deposit_growth_4q=+0.050, afs_unrealized_loss_to_equity=+0.049 |
| 2022-06-30 | 4 | 32.6 | 3262 / 4838 | no | cre_loans_to_loans=+0.317, afs_unrealized_loss_to_equity=+0.055, deposit_growth_4q=+0.049 |
| 2022-09-30 | 3 | 35.7 | 3095 / 4813 | no | cre_loans_to_loans=+0.308, past_due_30_89_to_assets=+0.074, afs_unrealized_loss_to_equity=+0.051 |
| 2022-12-31 | 2 | 29.7 | 3355 / 4773 | no | cre_loans_to_loans=+0.308, afs_unrealized_loss_to_equity=+0.051, equity_to_assets=+0.043 |
| 2023-03-31 | 1 | 83.0 | 809 / 4740 | no | volatile_liabilities_to_assets=+0.357, cre_loans_to_loans=+0.306, core_deposits_to_assets=+0.090 |

Every case-study quarter is shown (25 rows, from 2021-03-31). Rank 1 is the riskiest bank; the flag needs rank within the top 2% (rank 96 or better for 4,773 banks, about the 98th percentile). Signals are the features that pushed the score up most (the CSV, `case_studies.csv`, lists up to 5); values are in the model's score units (log-odds contributions), not percentages. None of the three was flagged by the model or by the Texas-ratio baseline in any test quarter 2016-2024.

## What was caught, what wasn't, and why
The model caught 21 of 29 eligible failed banks at least once with 1-4 quarters of notice, but none of the three famous 2023 failures. Signature came closest (94.9th percentile at 2022-12-31: rank 246; the cutoff was rank 96, about the 98th percentile). First Republic reached the 83rd percentile in its last report. SVB was in the 80th percentile in mid-2021 and then **fell** to the 27th percentile by 2022-12-31: right before it failed, the model rated it safer than most banks. The model did react to bond losses: unrealized losses on available-for-sale bonds were the top push for SVB and Signature in the second half of 2022. It was not enough to reach the top 2%. SVB's much bigger held-to-maturity (HTM) loss (about 98% of its equity at 2022-12-31) did not push its score up. I checked the model's per-feature contributions for SVB's four 2022 reports (read-only, no re-evaluation). Every one of them pushed SVB toward safe: low interest expense (about -1.1 in the model's log-odds units), strong Tier 1 risk-based capital (about -1.0), a low Texas ratio (about -1.0) and a large securities book (about -0.9) did most of the work, with return on equity (about -0.5) next. The HTM loss itself contributed about -0.16, slightly lowering the score, and the uninsured-deposit share contributed about -0.03 to -0.06, also slightly lowering it. In plain English: to a model trained on 2001-2014, a bank with cheap funding, strong capital and a big bond book looked safe, and its huge HTM loss was not read as a danger sign.

Why the HTM loss was not read as a danger sign is supported by the training data: among the 2,134 positive training rows, the 99th percentile of the HTM-loss-to-equity ratio is about 0.17 (17% of equity), and only 11 positive training rows exceed 0.3, compared with SVB's roughly 0.5 to 1.0 in 2022. (Across all 470,361 training rows only 145 exceed 0.3.) The model essentially never saw "large HTM loss followed by failure", so it had nothing to learn that signal from. One hypothesis, not proven, for the wider pattern: the training years (2001-2014) are dominated by credit-loss failures of 2008-2012, banks that failed because their loans went bad, and perhaps few training-era banks failed from bond losses or a run by uninsured depositors, so the model may have learned that clean loans plus profits mean safe. Another possibility is that the signals were present but too weak relative to thousands of other banks. This is a limit of learning from past failures, and it is the honest result: **a model trained only on pre-2015 data did not catch SVB.** SVB's reports for 2022-09-30 and 2022-12-31 got identical scores (0.0023) even though their HTM ratios differed (about 1.05 vs 0.98), so the model is insensitive to the HTM ratio in that range. Phase 4 (replay and error analysis) tests these hypotheses and asks what signal would have caught them. Any model change made after seeing the 2023 results means 2016-2024 is no longer a clean out-of-sample test, so Phase 4 reports such changes separately.

