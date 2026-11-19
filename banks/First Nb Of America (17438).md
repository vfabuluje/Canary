---
cert: 17438
name: "First Nb Of America"
as_of: 2026-06-30
rank: 76
n_banks: 4313
percentile: 98.26107118015302
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:57:20"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of America (cert 17438)

*Outcome not yet known.*

## Summary

First Nb Of America, a Michigan bank with $6.8 billion in assets, held national rank 76 out of 4,313 banks on Canary's risk score as of June 30, 2026, with a percentile of 98.3%, where higher means riskier. That rank puts it on Canary's watchlist, the riskiest 2% of banks. Its funding leans heavily on brokered deposits (money placed through middlemen rather than gathered from local customers) at 43.4% of deposits, against a national median of 0.0%. Its profits are strong, with return on assets of 2.8% against a national median of 1.2%, and that pulled its score down.

## Warning signs in the data

On capital (the bank's own cushion against losses), equity was 8.1% of assets, below the national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.1%, against a median of 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were slightly above the median: Tier 1 at 15.3% against 14.6%, and total at 16.5% against 15.8%.

On credit quality, loans 90+ days past due or not accruing interest were 1.9% of loans, well above the national median of 0.5%. Nonaccrual assets and foreclosed property were 1.9% of assets against a median of 0.3%, and loans 30-89 days past due were 0.8% of assets against 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 20.6%, well above the median of 2.9%.

Funding stands out most: loans were 160.1% of deposits against a median of 80.2%, and core deposits (stable everyday deposits) were only 26.0% of assets against 75.5%. Brokered deposits were 43.4% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 34.2% of assets against 0.2%. Interest expense was 3.5% of assets, well above the median of 1.6%, while losses on bonds available for sale were small at 0.1% of equity, against a median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median.

## Understanding the score

As of June 30, 2026, the bank held national rank 76 of 4,313 banks, with a percentile of 98.3% on a scale from 0 to 100 where higher means riskier. It was flagged for the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter.

Five features pushed the score up the most. Brokered deposits at 43.4% of deposits added +1.179, and interest expense at 3.5% of assets added +0.570. Securities at only 1.2% of assets added +0.358, commercial real estate loans at 1.1% of loans added +0.303, and the efficiency ratio (operating costs as a share of revenue) at 26.6% added +0.191.

Five features pulled the score down the most. The Tier 1 risk-based capital ratio at 15.3% contributed -0.967, return on equity at 34.7% contributed -0.796, and return on assets at 2.8% contributed -0.549. The total risk-based capital ratio at 16.5% contributed -0.475, and the Texas ratio at 20.6% contributed -0.311.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 39 | 4,589 | ▲ watchlist |
| 2024-12-31 | 57 | 4,560 | ▲ watchlist |
| 2025-03-31 | 141 | 4,536 |  |
| 2025-06-30 | 139 | 4,494 |  |
| 2025-09-30 | 121 | 4,452 |  |
| 2025-12-31 | 116 | 4,411 |  |
| 2026-03-31 | 76 | 4,353 | ▲ watchlist |
| 2026-06-30 | 76 | 4,313 | ▲ watchlist |

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of 30 ratios checked, 10 sat outside their own prior range as of June 30, 2026. The bank's percentile was 98.3%, up from 96.9% on June 30, 2025, so the model rated it riskier than a year earlier.

Construction loans were 3.9% of loans, above their prior range of 1.4% to 3.6%, yet their contribution of -0.307 model log-odds units pushed the score down. Loans 30-89 days past due were 0.8% of assets, above their prior range of 0.5% to 0.7%, yet their contribution of -0.180 pushed the score down. Nonaccrual assets and foreclosed property were 1.9% of assets, above their prior range of 1.1% to 1.8%, yet their contribution of -0.116 pushed the score down. Loans 90+ days past due or not accruing interest were 1.90% of loans, just above their prior range of 1.1% to 1.88%, yet their contribution of -0.217 pushed the score down.

Commercial real estate loans were 1.1% of loans, below their prior range of 1.2% to 1.4%, and their contribution of +0.303 pushed the score up. The efficiency ratio was 26.6%, above its prior range of 24.4% to 26.4%, and its contribution of +0.191 pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| construction loans as a share of loans | 3.9% | 1.4% to 3.6% | prior 12 quarters | +0.3 pp | +0.9 pp | -0.307 | pushed the score down |
| loans 30-89 days past due, as a share of assets | 0.8% | 0.5% to 0.7% | prior 12 quarters | +0.1 pp | +0.3 pp | -0.180 | pushed the score down |
| commercial real estate loans as a share of loans | 1.1% | 1.2% to 1.4% | prior 12 quarters | -0.1 pp | -0.3 pp | +0.303 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 26.6% | 24.4% to 26.4% | same quarter, prior 3 years | n/a | +2.0 pp | +0.191 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 1.9% | 1.1% to 1.8% | prior 12 quarters | +0.03 pp | +0.2 pp | -0.116 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 1.90% | 1.1% to 1.88% | prior 12 quarters | +0.02 pp | +0.1 pp | -0.217 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this fact sheet holds no data from after the as-of quarter, so it cannot yet show how the bank's watchlist status played out. The bank remains an open watchlist case, meaning there is no later result in our data to explain.

## What happened next

In hindsight, our data contains no later ranks, flags or reporting status for this bank after the as-of quarter. Its later path will be visible only once newer quarterly reports are added.

## Sources

- F1 · Bank name · n/a · First Nb Of America · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 76 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 16.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 20.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 160.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 43.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 34.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $6.8 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: brokered deposits as a share of deposits, value 43.4%; contribution to the score · 2026-06-30 · +1.179 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.5%; contribution to the score · 2026-06-30 · +0.570 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.358 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.303 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 26.6%; contribution to the score · 2026-06-30 · +0.191 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 34.7%; contribution to the score · 2026-06-30 · -0.796 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 2.8%; contribution to the score · 2026-06-30 · -0.549 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 16.5%; contribution to the score · 2026-06-30 · -0.475 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 20.6%; contribution to the score · 2026-06-30 · -0.311 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F90 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F91 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F94 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.307 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F95 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F96 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F97 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F98 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F101 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F102 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F103 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F104 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F105 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F108 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.303 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F109 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 26.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 24.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F112 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 26.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.191 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F116 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F117 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F118 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F121 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.116 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.90% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F124 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F125 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 1.88% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F128 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.217 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F129 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.9% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
