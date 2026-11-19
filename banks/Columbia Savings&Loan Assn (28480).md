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
written_at: "2026-11-19T14:08:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Columbia Savings&Loan Assn (cert 28480)

*Outcome not yet known.*

## Summary

Columbia Savings&Loan Assn, a small savings institution in WI, ranked 5 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.9th percentile, where higher means riskier. That placed it on the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter. The main pressures are thin capital, a very large share of loans behind on payments, and heavy losses, with a Texas ratio (troubled assets measured against capital plus reserves) of 231.1% and a return on equity of -53.3%.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thin: equity was 5.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 5.5% against 11.0%. The risk-based capital ratios, which weight assets by how risky they are, were also well below typical levels, with Tier 1 at 7.6% against a median of 14.6% and total capital at 8.9% against 15.8%.

Credit quality stood out most: loans 90 or more days past due or no longer accruing interest were 19.5% of loans, far above the national median of 0.5%. Loans at an earlier stage of missed payments were 4.6% of assets against a median of 0.2%, and nonaccrual assets plus foreclosed property were 4.4% of assets against 0.3%. The Texas ratio was 231.1%, compared with a national median of 2.9%. The bank was losing money, with a return on assets of -3.3% against a median of 1.2% and an efficiency ratio (operating costs as a share of revenue) of 176.0% against 62.1%.

Funding looked steadier: uninsured deposits (balances above the government insurance limit) were only 1.7% of deposits against a median of 24.8%, brokered deposits were 0.0% against 0.0%, and core deposits were 83.2% of assets against 75.5%. The bank was shrinking, with assets down -13.2% and deposits down -10.3% over the past four quarters, while the national medians grew 4.5% and 4.2%. Unrealized bond losses were not a concern: losses on bonds available for sale were 0.0% of equity against a median of 5.6%, partly because securities made up just 0.2% of assets against a median of 17.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 5 out of 4,313 banks, in the 99.9th percentile on a scale where higher means riskier. That put it on the watchlist, the top 2% of banks by score, which held 87 banks that quarter.

The five factors that pushed the score up most were the Texas ratio at 231.1%, return on equity at -53.3%, loans 90 or more days past due or not accruing at 19.5% of loans, securities at 0.2% of assets, and uninsured deposits at 1.7% of deposits. Their contributions to the score were +1.217, +0.679, +0.407, +0.254 and +0.251 respectively.

The five factors that pulled the score down most were interest expense at 0.6% of assets, nonaccrual assets and foreclosed property at 4.4% of assets, loans at 83.4% of deposits, the leverage ratio at 5.5%, and deposit growth of -10.3%. Their contributions were -1.050, -0.341, -0.093, -0.087 and -0.080 respectively.

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

Canary compared 28 of the bank's ratios with their own history over the prior 12 quarters, and 14 of them sat outside their earlier range. The model rated the bank riskier than a year earlier, when it stood at the 97.0th percentile, compared with the 99.9th percentile now.

Return on equity fell to -53.3%, below its prior range of -12.5% to 0.5%, and contributed +0.679 model log-odds units, which pushed the score up. Return on assets fell to -3.3%, below its prior range of -1.1% to 0.0%, and contributed +0.181, which pushed the score up. The efficiency ratio rose to 176.0%, well above its prior range of 100.8% to 124.2%, yet it contributed -0.045 and had little effect on the score.

The leverage ratio dropped to 5.5%, below its prior range of 6.3% to 9.0%, but its contribution of -0.087 pushed the score down rather than up. Equity as a share of assets fell to 5.5%, below its prior range of 6.0% to 9.0%, yet its contribution of +0.039 had little effect on the score. Cash rose to 8.3% of assets, above its prior range of 1.9% to 6.8%, while its contribution of -0.017 had little effect on the score.

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

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 76 banks in the same specialty group and size tier (under $100 million).

The Texas ratio of 231.1% was unusually high nationally, at the 99.9th percentile. Against a peer median of 1.7%, it sat at the 99.3rd percentile among peers, unusually high among its peers too. Loans 90 or more days past due or not accruing were 19.5% of loans, unusually high nationally at the 99.9th percentile. With a peer median of 0.5%, that figure was at the 99.3rd peer percentile, unusually high among its peers too. Loans at an earlier stage of missed payments were 4.6% of assets, unusually high nationally at the 99.8th percentile, and at the 95.4th peer percentile against a peer median of 0.5%, unusually high among its peers too.

The total risk-based capital ratio of 8.9% was unusually low nationally at the 0.1st percentile, and at the 1.3rd peer percentile against a peer median of 24.1%, unusually low among its peers too. The Tier 1 risk-based capital ratio of 7.6% was unusually low nationally at the 0.1st percentile, and at the 1.3rd peer percentile against a peer median of 23.2%, unusually low among its peers too. The leverage ratio of 5.5% was unusually low nationally at the 0.5th percentile, and at the 2.0th peer percentile against a peer median of 12.7%, unusually low among its peers too. Return on equity of -53.3% was unusually low nationally at the 0.3rd percentile, and at the 0.7th peer percentile against a peer median of 2.6%, unusually low among its peers too. Uninsured deposits at 1.7% of deposits were unusually low nationally at the 0.5th percentile, and at the 7.2nd peer percentile against a peer median of 9.9%, unusually low among its peers too.

Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and 14 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 231.1% | 99.9th (unusually high) | 1.7% | 99.3rd | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 19.5% | 99.9th (unusually high) | 0.5% | 99.3rd | unusually high among its peers too |
| the total risk-based capital ratio | 8.9% | 0.1st (unusually low) | 24.1% | 1.3rd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 7.6% | 0.1st (unusually low) | 23.2% | 1.3rd | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 4.6% | 99.8th (unusually high) | 0.5% | 95.4th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -53.3% | 0.3rd (unusually low) | 2.6% | 0.7th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 1.7% | 0.5th (unusually low) | 9.9% | 7.2nd | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 5.5% | 0.5th (unusually low) | 12.7% | 2.0th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 2.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | n/a | 50% or more | n/a |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight view: this bank falls in the open-watchlist case, meaning it was flagged by the model and our records do not show a failure. The fact sheet contains no hindsight data points for this bank, so this memo cannot describe what followed the as-of quarter in any more detail.

## What happened next

Hindsight view: no later ranks, flags or reporting status are included in the fact sheet for this bank. Without that data, we cannot say how its rank moved afterward or whether it continued to file reports, and readers should check the score history table for any later quarters.

## Sources

- F1 · Bank name · n/a · Columbia Savings&Loan Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 5 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
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
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 176.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 83.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -13.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
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
- F129 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.0% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 231.1% · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 19.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F141 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F142 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F143 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F144 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F145 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F146 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F147 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F148 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F149 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F153 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F154 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F155 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F156 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 23.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F159 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F160 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F161 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.4th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F162 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F163 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F164 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -53.3% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.7th · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: return_on_equity
- F169 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F171 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F172 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F173 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 7.2nd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F174 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F175 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F176 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F177 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F178 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F179 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F181 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F183 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
