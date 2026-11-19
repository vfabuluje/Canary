---
cert: 28480
name: "Columbia Savings&Loan Assn"
as_of: 2026-06-30
rank: 5
n_banks: 4313
percentile: 99.90725712960817
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:53:34"
writer_model: "claude-opus-5-5"
checked: true
---

# Columbia Savings&Loan Assn (cert 28480)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Columbia Savings&Loan Assn, a small savings institution in WI, ranked 5 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. That rank put it on Canary's watchlist, the riskiest 2% of banks. Its capital cushion was thin, with equity at 5.5% of assets against a national median of 10.6%, and 19.5% of its loans were 90+ days past due or not accruing interest, against a median of 0.5%. It was also losing money, with a return on assets of -3.3% against a median of 1.2%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was well below typical levels: equity was 5.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 5.5% against 11.0%. Its risk-based capital ratios, which weigh assets by riskiness, were also low, with a Tier 1 ratio of 7.6% against a median of 14.6% and a total ratio of 8.9% against 15.8%.

Credit quality stood far outside the norm: 19.5% of loans were 90+ days past due or not accruing interest, against a national median of 0.5%, and loans 30-89 days past due equaled 4.6% of assets, against 0.2%. Nonaccrual assets and foreclosed property were 4.4% of assets against a median of 0.3%, and the Texas ratio, which compares troubled assets with capital plus reserves, was 231.1% against 2.9%. Earnings were deeply negative, with return on equity at -53.3% against a median of 11.6%, and the efficiency ratio (operating costs as a share of revenue) was 176.0% against 62.1%.

Funding looked steadier: uninsured deposits, those above the government insurance limit, were only 1.7% of deposits against a median of 24.8%, and core deposits, a stable funding source, were 83.2% of assets against 75.5%. Still, the bank was shrinking, with deposits down -10.3% over the past four quarters against a median of 4.2%, and total assets were $20.6 million against a median of $384.7 million. Bond losses were not a concern, as losses on bonds available for sale were 0.0% of equity against a median of 5.6%, and securities made up just 0.2% of assets against 17.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 5 out of 4,313 banks, placing it in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which covers the riskiest 2% of banks, or 87 banks that quarter.

The five factors that pushed the score up the most were the Texas ratio at 231.1% (contribution +1.217), return on equity at -53.3% (+0.679), loans 90+ days past due or not accruing at 19.5% of loans (+0.407), securities at 0.2% of assets (+0.254), and uninsured deposits at 1.7% of deposits (+0.251). The five factors that pulled the score down the most were interest expense at 0.6% of assets (contribution -1.050), nonaccrual assets and foreclosed property at 4.4% of assets (-0.341), loans at 83.4% of deposits (-0.093), the leverage ratio at 5.5% (-0.087), and deposit growth of -10.3% over the past four quarters (-0.080).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 187 | 4,589 |  |
| 2024-12-31 | 56 | 4,560 | ▲ watchlist |
| 2025-03-31 | 124 | 4,536 |  |
| 2025-06-30 | 134 | 4,494 |  |
| 2025-09-30 | 116 | 4,452 |  |
| 2025-12-31 | 9 | 4,411 | ▲ watchlist |
| 2026-03-31 | 11 | 4,353 | ▲ watchlist |
| 2026-06-30 | 5 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, using the prior 12 quarters for most ratios and the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios compared, 14 were outside their own prior range. The bank ranked 5 out of 4,313 and sat in the 99.9th percentile, up from the 97.0th percentile on 2025-06-30, so the model rated it riskier than a year earlier.

Return on equity was -53.3%, far below its prior range of -12.5% to 0.5% after a change of -40.8 pp over four quarters, and its contribution of +0.679 model log-odds units pushed the score up. Return on assets was -3.3%, below its prior range of -1.1% to 0.0%, and its contribution of +0.181 pushed the score up. The efficiency ratio was 176.0%, well above its prior range of 100.8% to 124.2%, yet its contribution of -0.045 had little effect on the score.

The leverage ratio was 5.5%, below its prior range of 6.3% to 9.0%, yet its contribution of -0.087 pushed the score down. Equity as a share of assets was 5.5%, below its prior range of 6.0% to 9.0%, but its contribution of +0.039 had little effect on the score. Cash as a share of assets was 8.3%, above its prior range of 1.9% to 6.8%, and its contribution of -0.017 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -53.3% | -12.5% to 0.5% | same quarter, prior 3 years | n/a | -40.8 pp | +0.679 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 176.0% | 100.8% to 124.2% | same quarter, prior 3 years | n/a | +51.8 pp | -0.045 | little effect on the score |
| return on assets (profit as a share of assets) | -3.3% | -1.1% to 0.0% | same quarter, prior 3 years | n/a | -2.2 pp | +0.181 | pushed the score up |
| cash as a share of assets | 8.3% | 1.9% to 6.8% | prior 12 quarters | +1.5 pp | +3.5 pp | -0.017 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 5.5% | 6.3% to 9.0% | prior 12 quarters | -0.8 pp | -3.1 pp | -0.087 | pushed the score down |
| equity as a share of assets | 5.5% | 6.0% to 9.0% | prior 12 quarters | -0.6 pp | -3.1 pp | +0.039 | little effect on the score |

14 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this is an open watchlist case: the model flagged the bank, and our data does not yet record a final outcome for it. The fact sheet contains no data from after the as-of quarter, so there is nothing later to confirm or contradict the flag. The flag rests on the figures described above, chiefly very weak loan quality, heavy losses and a thin capital cushion.

## What happened next

In hindsight, no later quarters are available in this fact sheet, so there are no later ranks, watchlist flags or reporting status to show yet. Whether the bank keeps reporting, leaves the watchlist or stops reporting will only be visible once newer data arrives.

## Sources

- F1 · Bank name · n/a · Columbia Savings&Loan Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 5 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 19.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 231.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -53.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 176.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 83.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $20.6 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -10.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 231.1%; contribution to the score · 2026-06-30 · +1.217 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -53.3%; contribution to the score · 2026-06-30 · +0.679 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 19.5%; contribution to the score · 2026-06-30 · +0.407 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: securities as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · +0.254 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F79 · Driver up #5: uninsured deposits as a share of deposits, value 1.7%; contribution to the score · 2026-06-30 · +0.251 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2026-06-30 · -1.050 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 4.4%; contribution to the score · 2026-06-30 · -0.341 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F82 · Driver down #3: loans as a share of deposits, value 83.4%; contribution to the score · 2026-06-30 · -0.093 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F83 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 5.5%; contribution to the score · 2026-06-30 · -0.087 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -10.3%; contribution to the score · 2026-06-30 · -0.080 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -53.3% · data/features/fct_bank_features.parquet: return_on_equity
- F86 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -12.5% · data/features/fct_bank_features.parquet: return_on_equity
- F87 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -40.8 pp · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.679 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 176.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 100.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 124.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.045 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F97 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -3.3% · data/features/fct_bank_features.parquet: return_on_assets
- F98 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F99 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.181 · data/analyst/scores.parquet: feature return_on_assets contribution
- F102 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F103 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F104 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F105 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 6.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F108 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.017 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F109 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F110 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F111 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F112 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F115 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.087 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F116 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F117 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F118 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F119 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F122 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.039 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F123 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F124 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.0% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
