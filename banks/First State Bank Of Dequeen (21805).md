---
cert: 21805
name: "First State Bank Of Dequeen"
as_of: 2026-06-30
rank: 17
n_banks: 4313
percentile: 99.62902851843265
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:37"
writer_model: "claude-opus-5-5"
checked: true
---

# First State Bank Of Dequeen (cert 21805)

*Outcome not yet known.*

## Summary

First State Bank Of Dequeen, an Arkansas bank, ranked 17 out of 4,313 banks nationally on Canary's risk score as of June 30, 2026, placing it in the 99.6th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the top 2% of banks, or 87 banks that quarter. The biggest factors raising its score were large paper losses on its bond holdings and a heavy reliance on brokered deposits, which is money placed with the bank through middlemen. Its profitability and fairly low troubled loans pushed the score the other way.

## Warning signs in the data

Capital, the bank's cushion against losses, is thin: equity was 6.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.5% against 11.0%. Credit quality is weaker than typical: loans 90 or more days past due or not accruing interest were 1.2% of loans versus a median of 0.5%, and nonaccrual assets plus foreclosed property were 0.7% of assets versus 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 9.7% compared with a median of 2.9%.

On funding, brokered deposits made up 24.1% of deposits, while the national median was 0.0%. Federal Home Loan Bank borrowings were 4.0% of assets versus a median of 0.2%, and core deposits, the steadier everyday deposits, were 65.2% of assets versus 75.5%. Interest expense ran at 2.7% of assets against a median of 1.6%, and cash was 2.5% of assets against 6.2%. One offsetting point: uninsured deposits were only 4.0% of deposits, well below the median of 24.8%.

The largest single concern is bond losses: unrealized losses on bonds available for sale (bonds the bank could sell before they mature) equaled 27.4% of equity, far above the national median of 5.6%. Securities were also a large part of the balance sheet, at 37.8% of assets versus a median of 17.6%.

## Understanding the score

As of June 30, 2026, the bank ranked 17 of 4,313 banks, in the 99.6th percentile, on a scale of 0 to 100 where higher means riskier. It is flagged on the watchlist, which holds the top 2% of banks by score, 87 banks that quarter.

Five factors pushed the score up most. Losses on bonds available for sale, at 27.4% of equity, added +1.634, and brokered deposits, at 24.1% of deposits, added +1.019. The efficiency ratio (operating costs as a share of revenue), at 53.5%, added +0.558, and interest expense, at 2.7% of assets, added +0.329. Deposit growth over the past four quarters, at 14.6%, added +0.100.

Five factors pulled the score down most. The Texas ratio, at 9.7%, contributed -0.868, and the Tier 1 risk-based capital ratio (core capital measured against riskiness of assets) contributed -0.562. Return on equity (profit as a share of equity), at 22.1%, contributed -0.454. Loans 90 or more days past due or not accruing interest, at 1.2% of loans, contributed -0.295, and nonaccrual assets plus foreclosed property, at 0.7% of assets, contributed -0.277.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 64 | 4,589 | ▲ watchlist |
| 2024-12-31 | 83 | 4,560 | ▲ watchlist |
| 2025-03-31 | 80 | 4,536 | ▲ watchlist |
| 2025-06-30 | 19 | 4,494 | ▲ watchlist |
| 2025-09-30 | 24 | 4,452 | ▲ watchlist |
| 2025-12-31 | 52 | 4,411 | ▲ watchlist |
| 2026-03-31 | 20 | 4,353 | ▲ watchlist |
| 2026-06-30 | 17 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of the 28 ratios compared, 4 sat outside their own prior range, and all 4 are discussed here. The model rated the bank about the same as a year earlier: it was in the 99.6th percentile on June 30, 2025, and ranked 17 of 4,313 as of June 30, 2026.

The efficiency ratio was 53.5%, below its prior range of 56.1% to 63.5% after a change of -2.6 pp over four quarters, yet it still pushed the score up, contributing +0.558 model log-odds units. Securities were 37.8% of assets, above their prior range of 16.7% to 34.9% after rising +3.3 pp in one quarter, but this ratio pushed the score down, contributing -0.218 model log-odds units.

Commercial real estate loans were 12.6% of loans, just above their prior range of 10.5% to 12.5% after rising +0.4 pp over four quarters, and this ratio pushed the score up, contributing +0.051 model log-odds units. Recently overdue loans, those not yet in the most serious late category, were 0.29% of assets, below their prior range of 0.32% to 1.3%, and this ratio pushed the score down, contributing -0.244 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 53.5% | 56.1% to 63.5% | same quarter, prior 3 years | n/a | -2.6 pp | +0.558 | pushed the score up |
| securities as a share of assets | 37.8% | 16.7% to 34.9% | prior 12 quarters | +3.3 pp | +3.2 pp | -0.218 | pushed the score down |
| commercial real estate loans as a share of loans | 12.6% | 10.5% to 12.5% | prior 12 quarters | +0.1 pp | +0.4 pp | +0.051 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 0.29% | 0.32% to 1.3% | prior 12 quarters | -0.1 pp | -0.02 pp | -0.244 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank remains an open watchlist case: the fact sheet contains no data from after the as-of quarter. Because no later outcome is recorded, the reasons it is on the watchlist are the as-of figures described above, and nothing more can be said about how events turned out.

## What happened next

In hindsight, Canary's fact sheet includes no later ranks, watchlist flags or reporting status for this bank. We therefore cannot say how its rank moved after the as-of quarter or whether it is still filing reports.

## Sources

- F1 · Bank name · n/a · First State Bank Of Dequeen · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 17 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 65.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 27.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 37.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 27.4%; contribution to the score · 2026-06-30 · +1.634 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 24.1%; contribution to the score · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 53.5%; contribution to the score · 2026-06-30 · +0.558 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.329 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 14.6%; contribution to the score · 2026-06-30 · +0.100 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 9.7%; contribution to the score · 2026-06-30 · -0.868 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.562 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 22.1%; contribution to the score · 2026-06-30 · -0.454 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.2%; contribution to the score · 2026-06-30 · -0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.277 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F85 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 53.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F86 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 56.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F87 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 63.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · -2.6 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.558 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F91 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 37.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F92 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F93 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 34.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F94 · Trend: securities as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +3.3 pp · data/features/fct_bank_features.parquet: securities_to_assets
- F96 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.218 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F97 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F98 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 10.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F100 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 12.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F102 · Trend: commercial real estate loans as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +0.4 pp · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F103 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.051 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F104 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F105 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.29% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.32% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F107 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F110 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.244 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F111 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F112 · Trend: ratios outside their own prior range · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F113 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F114 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F115 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F116 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F117 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F118 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
