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
written_at: "2026-11-18T19:46:34"
writer_model: "claude-opus-5-5"
checked: true
---

# Pulaski Savings Bank (cert 28611)

*Hindsight: failed 2025-01-17. Canary did not flag it.*

## Summary

As of 2024-09-30, Pulaski Savings Bank, a small Illinois savings bank, ranked 1,814 out of 4,589 banks on Canary's risk score, placing it at the 60.5th percentile, where higher means riskier. It was not flagged on the watchlist, which covered the riskiest 2% of banks, or 92 banks that quarter. Its capital cushion was strong, with a Tier 1 risk-based capital ratio (core capital against risk-weighted assets) of 20.0% against a national median of 14.3%. It was losing money, though, with a return on assets of -0.6% against a national median of 0.9%.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, looked solid: equity was 10.2% of assets against a national median of 10.0%, and the total risk-based capital ratio was 21.3% against a median of 15.5%. The leverage ratio (core capital as a share of average assets) was slightly below the median, at 10.3% against 10.7%. Profitability was the weakest area: the efficiency ratio (operating costs as a share of revenue) was 117.4% against a median of 67.8%, meaning costs exceeded revenue, and return on equity was -5.7% against 9.8%.

Credit quality was mostly clean, with 0.0% of loans seriously overdue or not accruing interest against a median of 0.4%. However, loans 30-89 days past due, an early sign of borrower strain, were 0.9% of assets, well above the median of 0.2%. Loan-loss reserves, money set aside for bad loans, were 1.0% of loans against a median of 1.2%.

On funding, loans were 97.3% of deposits against a median of 79.2%, so the bank lent out most of what it took in, and borrowings from the Federal Home Loan Bank were 3.0% of assets against a median of 0.8%. Uninsured deposits, which can leave quickly in a scare, were low at 5.0% against a median of 23.6%, and cash was 8.2% of assets against 6.2%. Unrealized losses on bonds available for sale were small, at 0.4% of equity against a median of 8.5%.

## Understanding the score

Pulaski Savings Bank ranked 1,814 of 4,589 banks as of 2024-09-30, at the 60.5th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which held the top 2% of banks, or 92 banks that quarter.

Five features pushed the score up the most: securities at just 0.6% of assets (+0.493), the bank's small size of $49.5 million in total assets (+0.184), commercial real estate loans at 5.9% of loans (+0.151), equity at 10.2% of assets (+0.097), and losses on bonds available for sale at 0.4% of equity (+0.070). Five features pushed the score down the most: the Tier 1 risk-based capital ratio of 20.0% (-1.106), interest expense at 1.3% of assets (-0.833), a Texas ratio (troubled assets against capital plus reserves) of 0.0% (-0.806), the total risk-based capital ratio of 21.3% (-0.682), and seriously overdue or non-accruing loans at 0.0% of loans (-0.402). In short, strong capital and a lack of troubled loans held the score down, outweighing the factors that raised it.

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

Canary compared 30 of the bank's ratios with their own history, mostly over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios; 7 sat outside their prior range, and the table shows the 6 furthest outside. The model rated it riskier than a year earlier, moving from the 32.4th percentile at 2023-09-30 to the 60.5th percentile, rank 1,814, at 2024-09-30.

Interest expense was 1.3% of assets, above its prior range of 0.4% to 0.7% and up +0.6 pp over four quarters, yet its contribution of -0.833 model log-odds units pushed the score down. The efficiency ratio was 117.4%, above its prior range of 54.2% to 97.5% and up +19.9 pp over four quarters, yet its contribution of -0.060 pushed the score down.

Return on assets was -0.6%, below its prior range of 0.1% to 2.6%, with a contribution of -0.007 that had little effect on the score. Return on equity was -5.7%, below its prior range of 0.7% to 32.4%, yet its contribution of -0.303 pushed the score down. Net interest margin was 3.44%, just above its prior range of 3.0% to 3.42%, with a contribution of -0.046 that had little effect on the score. Cash was 8.2% of assets, just below its prior range of 8.3% to 13.2% after a change of -2.1 pp over four quarters, with a contribution of +0.032 that had little effect on the score.

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

## Why the model missed it

In hindsight, this is a miss: the bank failed on 2025-01-17, and its last report was for 2024-09-30, when it ranked 1,814 of 4,589 and was not on the watchlist. The model learned from 539 past failures, and 96% of them were credit-loss failures, where bad loans eat through capital. This bank showed almost none of that pattern, with a Texas ratio of 0.0% and capital ratios well above the median, so those features pulled its score down.

The weaknesses it did show, such as an efficiency ratio of 117.4% and a return on assets of -0.6%, were given little weight or even lowered the score. The fact sheet does not say why the bank failed, so the cause cannot be confirmed from this data.

## What happened next

In hindsight, Pulaski Savings Bank failed on 2025-01-17. Its last quarterly report in our data was for 2024-09-30, so there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Pulaski Savings Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
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
- F19 · Bank: the total risk-based capital ratio · 2024-09-30 · 21.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2024-09-30 · 15.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2024-09-30 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2024-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F39 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2024-09-30 · -5.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2024-09-30 · 9.8% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 117.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2024-09-30 · 97.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2024-09-30 · 79.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-09-30 · 5.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 3.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 0.8% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2024-09-30 · 8.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2024-09-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
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
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2024-09-30 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F92 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F93 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F94 · Trend: annualized interest expense as a share of assets, change over four quarters, in percentage points · 2024-09-30 · +0.6 pp · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
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
- F132 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2023-09-30 · 32.4% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2024-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
