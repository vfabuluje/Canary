---
cert: 28611
name: "Pulaski Savings Bank"
as_of: 2024-09-30
rank: 1814
n_banks: 4589
percentile: 60.49248202222706
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2025-01-17
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:39"
writer_model: "claude-opus-5-5"
checked: true
---

# Pulaski Savings Bank (cert 28611)

*Hindsight: failed 2025-01-17. Canary did not flag it.*

## Summary

As of 2024-09-30, Pulaski Savings Bank ranked 1,814 out of 4,589 banks nationally, placing it at the 60.5th percentile on a scale where higher means riskier. It was not on the watchlist, which covers the riskiest 2% of banks. The model rated it riskier than a year earlier, when it sat at the 32.4th percentile. Its capital and loan quality looked strong against national medians, but it was losing money and its operating costs were higher than its revenue.

## Warning signs in the data

Capital, the owners' cushion against losses, looked solid: equity was 10.2% of assets against a national median of 10.0%, and the Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 20.0% against a median of 14.3%. The leverage ratio, core capital as a share of average assets, was slightly below the median at 10.3% versus 10.7%. Loan quality was clean: loans 90+ days past due or not accruing interest were 0.0% of loans against a median of 0.4%, and the Texas ratio (troubled assets against capital plus reserves) was 0.0% against 2.2%. One early sign was loans 30-89 days past due at 0.9% of assets, well above the median of 0.2%.

The clearest weakness was earnings: return on assets (profit as a share of assets) was -0.6% against a median of 0.9%, and the efficiency ratio (operating costs as a share of revenue) was 117.4% against 67.8%, meaning costs exceeded revenue. The peer section notes these readings are unusual nationally but typical among similar small mortgage-focused banks, so the two comparisons point different ways. Commercial real estate loans were only 5.9% of loans against a median of 23.1%, and the concentration section found the bank did not cross either supervisory line.

Funding looked stable: uninsured deposits (money above the government insurance limit) were 5.0% of deposits against a median of 23.6%, and core deposits, the steady everyday base, were 83.8% of assets against 75.0%. The bank did lend out more of its deposits than most, with loans at 97.3% of deposits against 79.2%, and Federal Home Loan Bank borrowings were 3.0% of assets against 0.8%. Unrealized losses on bonds available for sale were small at 0.4% of equity against a median of 8.5%.

## Understanding the score

As of 2024-09-30, the bank ranked 1,814 out of 4,589 banks, at the 60.5th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged for the watchlist, which held 92 banks that quarter, the top 2% by score.

The five features pushing the score up most were securities at 0.6% of assets (+0.493), total assets of $49.5 million (+0.184), commercial real estate loans at 5.9% of loans (+0.151), equity at 10.2% of assets (+0.097), and losses on bonds available for sale at 0.4% of equity (+0.070). The five features pushing it down most were the Tier 1 risk-based capital ratio at 20.0% (-1.106), interest expense at 1.3% of assets (-0.833), the Texas ratio at 0.0% (-0.806), the total risk-based capital ratio at 21.3% (-0.682), and seriously overdue or non-accruing loans at 0.0% of loans (-0.402). The downward pushes were larger than the upward ones, which kept the bank in the middle of the national ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-12-31 | 2,651 | 4,773 |  |
| 2023-03-31 | 3,017 | 4,740 |  |
| 2023-06-30 | 3,038 | 4,714 |  |
| 2023-09-30 | 3,169 | 4,686 |  |
| 2023-12-31 | 2,323 | 4,658 |  |
| 2024-03-31 | 2,738 | 4,640 |  |
| 2024-06-30 | 1,980 | 4,610 |  |
| 2024-09-30 | 1,814 | 4,589 |  |

## How its ratios moved

As of 2024-09-30, the bank ranked 1,814 out of 4,589 banks nationally, which puts it at the 60.5th percentile on a scale where higher means riskier. On 2023-09-30 it sat at the 32.4th percentile, and the model rated it riskier than a year earlier. Most ratios are compared with the bank's own values over the prior 12 quarters, and 7 of the 30 ratios checked this way were outside that prior range, with 6 shown here. Each ratio's contribution is given in model log-odds units, an internal scoring scale where a positive number pushes the score up and a negative one pushes it down.

Interest expense as a share of assets, meaning what the bank pays on deposits and borrowings, was 1.3%, above its prior range of 0.4% to 0.7%, yet its contribution of -0.833 pushed the score down. The efficiency ratio, operating costs as a share of revenue, was 117.4%, above its prior range of 54.2% to 97.5% after a rise of +19.9 pp over four quarters, but its contribution of -0.060 also pushed the score down. Return on equity, profit as a share of the owners' stake, was -5.7%, below its prior range of 0.7% to 32.4%, and its contribution of -0.303 pushed the score down.

Return on assets, profit as a share of assets, was -0.6%, below its prior range of 0.1% to 2.6%, yet its contribution of -0.007 had little effect on the score. Net interest margin, the spread earned on lending and investing, was 3.44%, just above its prior range of 3.0% to 3.42%, and its contribution of -0.046 had little effect on the score. Cash as a share of assets was 8.2%, slightly below its prior range of 8.3% to 13.2% after a change of -2.1 pp over four quarters, and its contribution of +0.032 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 1.3% | 0.4% to 0.7% | same quarter, prior 3 years | n/a | +0.6 pp | -0.833 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 117.4% | 54.2% to 97.5% | same quarter, prior 3 years | n/a | +19.9 pp | -0.060 | pushed the score down |
| return on assets (profit as a share of assets) | -0.6% | 0.1% to 2.6% | same quarter, prior 3 years | n/a | -0.7 pp | -0.007 | little effect on the score |
| return on equity (profit as a share of equity) | -5.7% | 0.7% to 32.4% | same quarter, prior 3 years | n/a | -6.4 pp | -0.303 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.44% | 3.0% to 3.42% | same quarter, prior 3 years | n/a | +0.4 pp | -0.046 | little effect on the score |
| cash as a share of assets | 8.2% | 8.3% to 13.2% | prior 12 quarters | -1.3 pp | -2.1 pp | +0.032 | little effect on the score |

7 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2024-09-30: Mortgage Lending Specialization.

Peers: 78 banks in the same specialty group and size tier (under $100 million).

Uninsured deposits (money held above the government deposit insurance limit) made up 5.0% of the bank's deposits, at the 2.2nd percentile nationally, which is unusually low; among its peers it sat at the 28.3rd percentile against a peer median of 8.4%, which is typical for its peer group. The efficiency ratio (operating costs as a share of revenue, where higher means costlier operations) was 117.4%, at the 97.4th percentile nationally, which is unusually high; among its peers it sat at the 85.3rd percentile against a peer median of 93.6%, which is typical for its peer group. Return on assets (profit as a share of assets) was -0.6%, at the 2.7th percentile nationally, which is unusually low; among its peers it sat at the 14.7th percentile against a peer median of 0.2%, which is typical for its peer group. Return on equity (profit as a share of the owners' capital) was -5.7%, at the 2.8th percentile nationally, which is unusually low; among its peers it sat at the 9.6th percentile against a peer median of 1.0%, which is typical for its peer group. Securities (bonds and similar investments) made up 0.6% of assets, at the 3.9th percentile nationally, which is unusually low; among its peers it sat at the 19.9th percentile against a peer median of 13.6%, which is typical for its peer group.

Overall, 5 of the bank's ratios fall in the national top or bottom 10%, but 0 of those are also unusual among its peers, so its pattern looks much like that of similar small mortgage-focused banks.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 5.0% | 2.2nd (unusually low) | 8.4% | 28.3rd | typical for its peer group |
| the efficiency ratio (operating costs as a share of revenue) | 117.4% | 97.4th (unusually high) | 93.6% | 85.3rd | typical for its peer group |
| return on assets (profit as a share of assets) | -0.6% | 2.7th (unusually low) | 0.2% | 14.7th | typical for its peer group |
| return on equity (profit as a share of equity) | -5.7% | 2.8th (unusually low) | 1.0% | 9.6th | typical for its peer group |
| securities as a share of assets | 0.6% | 3.9th (unusually low) | 13.6% | 19.9th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 1.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 79.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 30.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, the bank failed on 2025-01-17, and its last report, for 2024-09-30, had it ranked 1,814 out of 4,589 and not on the watchlist, so the model missed it. The model gave heavy weight to the bank's strong capital and clean loan book, with the Tier 1 risk-based capital ratio at 20.0% and the Texas ratio at 0.0% pulling the score down most.

Most failures the model learned from, 96%, were credit-loss failures, and this bank showed almost no loan problems, so it did not match that pattern. Its visible weakness was losses and high costs, yet return on equity of -5.7% and an efficiency ratio of 117.4% both pushed the score down rather than up.

## What happened next

In hindsight, 2024-09-30 was the last quarter the bank reported, and it failed on 2025-01-17. Because it stopped reporting, there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Pulaski Savings Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2024-09-30 · 1,814 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-09-30 · 4,589 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-09-30 · 60.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-09-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-09-30 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-09-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-09-30 · 20.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-09-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2024-09-30 · 5.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2024-09-30 · 23.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 117.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2024-09-30 · 97.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2024-09-30 · 79.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-09-30 · 5.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2024-09-30 · 83.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2024-09-30 · 75.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 3.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 0.8% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-09-30 · 8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: securities as a share of assets, value 0.6%; contribution to the score · 2024-09-30 · +0.493 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: total assets, value $49.5 million; contribution to the score · 2024-09-30 · +0.184 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 5.9%; contribution to the score · 2024-09-30 · +0.151 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: equity as a share of assets, value 10.2%; contribution to the score · 2024-09-30 · +0.097 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 0.4%; contribution to the score · 2024-09-30 · +0.070 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 20.0%; contribution to the score · 2024-09-30 · -1.106 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2024-09-30 · -0.833 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2024-09-30 · -0.806 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 21.3%; contribution to the score · 2024-09-30 · -0.682 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2024-09-30 · -0.402 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F85 · Failure date · 2025-01-17 · 2025-01-17 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2024-09-30 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F92 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F93 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F95 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2024-09-30 · -0.833 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F96 · Trend: annualized interest expense as a share of assets, what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2024-09-30 · 117.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 54.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 97.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2024-09-30 · +19.9 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2024-09-30 · -0.060 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2024-09-30 · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F104 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2024-09-30 · -0.007 · data/analyst/scores.parquet: feature return_on_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), what the model did with it · 2024-09-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F109 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2024-09-30 · -5.7% · data/features/fct_bank_features.parquet: return_on_equity
- F110 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: return_on_equity
- F111 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 32.4% · data/features/fct_bank_features.parquet: return_on_equity
- F113 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2024-09-30 · -0.303 · data/analyst/scores.parquet: feature return_on_equity contribution
- F114 · Trend: return on equity (profit as a share of equity), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F115 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2024-09-30 · 3.44% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F117 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.42% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2024-09-30 · -0.046 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F120 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2024-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F121 · Trend: cash as a share of assets, value at the as-of quarter · 2024-09-30 · 8.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F122 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F123 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F125 · Trend: cash as a share of assets, change over four quarters, in percentage points · 2024-09-30 · -2.1 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F126 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2024-09-30 · +0.032 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F127 · Trend: cash as a share of assets, what the model did with it · 2024-09-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F128 · Trend: ratios outside their own prior range · 2024-09-30 · 7 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios shown in the table (the furthest outside their prior range) · 2024-09-30 · 6 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2024-09-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2023-09-30 · 32.4% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2024-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2024-09-30 · 5.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F139 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2024-09-30 · 2.2nd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F140 · Peers: uninsured deposits as a share of deposits, national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F141 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2024-09-30 · 28.3rd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F142 · Peers: uninsured deposits as a share of deposits, peer median · 2024-09-30 · 8.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F143 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2024-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F144 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2024-09-30 · 117.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F145 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2024-09-30 · 97.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F146 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F147 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2024-09-30 · 85.3rd · data/features/fct_bank_features.parquet: efficiency_ratio
- F148 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2024-09-30 · 93.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F149 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2024-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: efficiency_ratio
- F150 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2024-09-30 · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F151 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2024-09-30 · 2.7th · data/features/fct_bank_features.parquet: return_on_assets
- F152 · Peers: return on assets (profit as a share of assets), national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F153 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2024-09-30 · 14.7th · data/features/fct_bank_features.parquet: return_on_assets
- F154 · Peers: return on assets (profit as a share of assets), peer median · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F155 · Peers: return on assets (profit as a share of assets), reading against its peers · 2024-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: return_on_assets
- F156 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2024-09-30 · -5.7% · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2024-09-30 · 2.8th · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2024-09-30 · 9.6th · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), peer median · 2024-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), reading against its peers · 2024-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: securities as a share of assets, bank value at the as-of quarter · 2024-09-30 · 0.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F163 · Peers: securities as a share of assets, national percentile (100 = highest value among all banks) · 2024-09-30 · 3.9th · data/features/fct_bank_features.parquet: securities_to_assets
- F164 · Peers: securities as a share of assets, national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: securities_to_assets
- F165 · Peers: securities as a share of assets, percentile among its peers (100 = highest value) · 2024-09-30 · 19.9th · data/features/fct_bank_features.parquet: securities_to_assets
- F166 · Peers: securities as a share of assets, peer median · 2024-09-30 · 13.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F167 · Peers: securities as a share of assets, reading against its peers · 2024-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: securities_to_assets
- F169 · Peers: ratios in the national top or bottom 10% · 2024-09-30 · 5 · data/features/fct_bank_features.parquet
- F170 · Peers: those ratios also unusual among peers · 2024-09-30 · 0 · data/features/fct_bank_features.parquet
- F172 · Peers: cut-off for unusual (top or bottom share of banks) · 2024-09-30 · 10% · data/features/fct_bank_features.parquet
