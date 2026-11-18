---
cert: 21111
name: "City National Bank Of New Jersey"
as_of: 2019-09-30
rank: 21
n_banks: 5325
percentile: 99.6244131455399
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-11-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:30"
writer_model: "claude-opus-5-5"
checked: true
---

# City National Bank Of New Jersey (cert 21111)

*Hindsight: failed 2019-11-01. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, City National Bank Of New Jersey ranked 21 out of 5,325 banks in Canary's national risk ranking, placing it in the 99.6th percentile, where higher means riskier. That put the New Jersey bank on the watchlist, the riskiest 2% of banks, which held 107 banks that quarter. Its capital cushion was far thinner than at a typical bank: equity was 2.9% of assets against a national median of 11.6%. It was also losing money, with a return on equity of -45.9% against a national median of 9.6%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was very low as of 2019-09-30. Equity was 2.9% of assets, well below the national median of 11.6%, and the leverage ratio (core capital as a share of average assets) was 2.6% against a median of 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 4.9% versus a median of 15.6%, and the total risk-based capital ratio was 6.2% versus 16.7%. The bank was also unprofitable: return on assets was -1.4% against a median of 1.1%, and the efficiency ratio (operating costs as a share of revenue) was 148.2% against 66.8%, meaning costs exceeded revenue.

Credit quality, meaning how well borrowers were repaying, was weaker than typical. Loans 90 or more days past due or not accruing interest were 2.6% of loans, well above the median of 0.6%, and loans 30-89 days past due were 1.3% of assets versus 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 25.5% against a median of 3.7%. Commercial real estate loans made up 62.1% of loans, far above the median of 22.6%.

On funding, the bank had been shrinking quickly: assets fell -33.2% over the past four quarters and deposits fell -36.3%, while the medians grew 4.7% and 4.4%. Uninsured deposits, those above the government insurance limit, were 32.1% of deposits against a median of 19.0%, though cash was a sizable 17.3% of assets versus 6.9%. Unrealized losses on bonds available for sale, meaning the drop in market value of bonds it could sell, were 4.0% of equity, compared with a median of -0.8%.

## Understanding the score

As of 2019-09-30 the bank ranked 21 of 5,325 banks, in the 99.6th percentile on a scale of 0 to 100 where higher means riskier. Its raw model score was 0.1284, and it was flagged on the watchlist, which covers the top 2% of banks and held 107 banks that quarter.

The five features that pushed the score up most were return on equity at -45.9%, the Tier 1 risk-based capital ratio at 4.9%, asset growth over the past four quarters at -33.2%, the total risk-based capital ratio at 6.2%, and loans as a share of deposits at 54.0%. Their contributions were +1.116, +0.973, +0.418, +0.284 and +0.150 respectively.

The five features that pulled the score down most were interest expense at 0.3% of assets, the Texas ratio at 25.5%, nonaccrual assets and foreclosed property at 1.5% of assets, construction loans at 4.8% of loans, and commercial real estate loans at 62.1% of loans. Their contributions were -1.158, -0.941, -0.699, -0.461 and -0.448 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 11 | 5,738 | ▲ watchlist |
| 2018-03-31 | 98 | 5,674 | ▲ watchlist |
| 2018-06-30 | 4 | 5,610 | ▲ watchlist |
| 2018-09-30 | 4 | 5,544 | ▲ watchlist |
| 2018-12-31 | 6 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 17 | 5,428 | ▲ watchlist |
| 2019-06-30 | 16 | 5,369 | ▲ watchlist |
| 2019-09-30 | 21 | 5,325 | ▲ watchlist |

## How early Canary caught it

In hindsight, the bank failed on 2019-11-01, and Canary had first flagged it at 2018-12-31, a lead time of 4 quarters before the failure. At that first flag, the biggest factors raising the score were the Tier 1 risk-based capital ratio at 5.3% and return on equity at -88.2%. Other top factors then were losses on bonds available for sale at 34.1% of equity, the Texas ratio at 56.8%, and the total risk-based capital ratio at 6.6%.

This fits the pattern in the training data, where 96% of the 539 failed banks were credit-loss failures, meaning losses on loans eroded capital.

## What happened next

In hindsight, the last quarter the bank reported data was 2019-09-30, the same quarter as this memo. The bank failed on 2019-11-01, so no later ranks exist. It no longer reports to regulators; our data shows when a bank stops reporting but does not by itself distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · City National Bank Of New Jersey · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NJ · data/raw/financials: STALP
- F5 · Model score · 2019-09-30 · 0.1284 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2019-09-30 · 21 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 4.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2019-09-30 · 62.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2019-09-30 · 22.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -45.9% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 32.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-09-30 · 17.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 4.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2019-09-30 · -33.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2019-09-30 · 4.7% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -45.9%; contribution to the score · 2019-09-30 · +1.116 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 4.9%; contribution to the score · 2019-09-30 · +0.973 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: asset growth over the past four quarters, value -33.2%; contribution to the score · 2019-09-30 · +0.418 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 6.2%; contribution to the score · 2019-09-30 · +0.284 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 54.0%; contribution to the score · 2019-09-30 · +0.150 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2019-09-30 · -1.158 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2019-09-30 · -0.941 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 1.5%; contribution to the score · 2019-09-30 · -0.699 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 4.8%; contribution to the score · 2019-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 62.1%; contribution to the score · 2019-09-30 · -0.448 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2019-11-01 · 2019-11-01 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Tier 1 risk-based capital ratio, value 5.3%; contribution to the score · 2018-12-31 · +1.364 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -88.2%; contribution to the score · 2018-12-31 · +0.941 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: losses on bonds available for sale, as a share of equity, value 34.1%; contribution to the score · 2018-12-31 · +0.661 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F91 · Driver up #4 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 56.8%; contribution to the score · 2018-12-31 · +0.656 · data/analyst/scores.parquet: feature texas_ratio contribution
- F92 · Driver up #5 at 2018-12-31: the total risk-based capital ratio, value 6.6%; contribution to the score · 2018-12-31 · +0.498 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F100 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
