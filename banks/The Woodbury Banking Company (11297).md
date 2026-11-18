---
cert: 11297
name: "The Woodbury Banking Company"
as_of: 2016-06-30
rank: 2
n_banks: 6129
percentile: 99.98368412465328
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-08-19
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# The Woodbury Banking Company (cert 11297)

*Hindsight: failed 2016-08-19. Canary flagged it 2 quarters ahead.*

## Summary

As of 2016-06-30, The Woodbury Banking Company in GA ranked 2 out of 6,129 banks nationally on Canary's risk score, placing it in the 100.0th percentile, where higher means riskier. It was flagged on the watchlist, which covers roughly the riskiest 2% of banks. Its equity, the owners' cushion that absorbs losses, was just 1.0% of assets, against a national median of 11.0%. Its troubled loans were far above typical levels, and it was losing money.

## Warning signs in the data

Capital, the money a bank can lose before depositors are at risk, was extremely thin: the leverage ratio (core capital as a share of average assets) was 0.8%, against a national median of 10.5%. The Tier 1 risk-based capital ratio, which weighs capital against riskier assets, was 1.6% versus a median of 15.1%, and the total risk-based capital ratio was 2.9% versus 16.3%.

Credit quality was poor: loans 90 or more days past due or no longer accruing interest made up 8.3% of loans, against a national median of 0.7%. Nonaccrual assets and foreclosed property were 12.8% of assets versus a median of 0.6%, and loans 30-89 days past due were 2.5% of assets versus 0.3%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 519.7%, far above the median of 5.3%. Return on assets, a measure of profit, was -4.5% against a median of 0.9%, and return on equity was -195.4% against 7.9%.

Funding looked stable: core deposits, the steady everyday deposits, were 98.6% of assets versus a median of 78.4%, brokered deposits were 0.0%, and cash was 13.1% of assets versus 6.4%. Unrealized losses on bonds available for sale equaled -21.3% of equity, well beyond the median of -1.6%, partly because equity itself was so small. The bank was also shrinking, with assets down -9.9% over the past four quarters, while the median bank grew 3.8%.

## Understanding the score

On 2016-06-30 the bank ranked 2 of 6,129 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 123 banks on it that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 1.6%, the Texas ratio at 519.7%, return on equity at -195.4%, the total risk-based capital ratio at 2.9%, and the leverage ratio at 0.8%. The five factors pulling the score down most were interest expense at 0.4% of assets, losses on bonds available for sale at -21.3% of equity, construction loans at 3.4% of loans, net interest margin (the spread earned on lending and investing) at 3.9%, and brokered deposits at 0.0% of deposits. The upward pushes were much larger than the downward ones, which is why the bank sat near the very top of the ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 22 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 2 | 6,129 | ▲ watchlist |

## How early Canary caught it

In hindsight, the bank failed on 2016-08-19. Canary first flagged it in the quarter ending 2016-03-31 under its lead-time rule, a lead time of 2 quarters before the failure. At that first flag, the main factors raising the score were the Texas ratio at 291.6%, the Tier 1 risk-based capital ratio at 4.9%, and loans 90 or more days past due or not accruing interest at 10.4% of loans.

## What happened next

In hindsight, the quarter ending 2016-06-30 was the last one the bank reported, so there are no later ranks or flags. The bank failed on 2016-08-19, shortly after that final report.

## Sources

- F1 · Bank name · n/a · The Woodbury Banking Company · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-06-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-06-30 · 6,129 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-06-30 · 123 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-06-30 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-06-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 0.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-06-30 · 1.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-06-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-06-30 · 2.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-06-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 8.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 12.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-06-30 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-06-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-06-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-06-30 · -195.4% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-06-30 · 7.9% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: brokered deposits as a share of deposits · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F53 · Bank: core deposits as a share of assets · 2016-06-30 · 98.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F54 · National median: core deposits as a share of assets · 2016-06-30 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2016-06-30 · 13.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-06-30 · 6.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-06-30 · -21.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2016-06-30 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2016-06-30 · -9.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2016-06-30 · 3.8% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.6%; contribution to the score · 2016-06-30 · +2.122 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 519.7%; contribution to the score · 2016-06-30 · +1.338 · data/analyst/scores.parquet: feature texas_ratio contribution
- F75 · Driver up #3: return on equity (profit as a share of equity), value -195.4%; contribution to the score · 2016-06-30 · +1.335 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #4: the total risk-based capital ratio, value 2.9%; contribution to the score · 2016-06-30 · +0.551 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F77 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 0.8%; contribution to the score · 2016-06-30 · +0.491 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver down #1: annualized interest expense as a share of assets, value 0.4%; contribution to the score · 2016-06-30 · -0.558 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver down #2: losses on bonds available for sale, as a share of equity, value -21.3%; contribution to the score · 2016-06-30 · -0.317 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #3: construction loans as a share of loans, value 3.4%; contribution to the score · 2016-06-30 · -0.194 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #4: net interest margin (the spread earned on lending and investing), value 3.9%; contribution to the score · 2016-06-30 · -0.107 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F82 · Driver down #5: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2016-06-30 · -0.093 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Failure date · 2016-08-19 · 2016-08-19 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Driver up #1 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 291.6%; contribution to the score · 2016-03-31 · +1.063 · data/analyst/scores.parquet: feature texas_ratio contribution
- F87 · Driver up #2 at 2016-03-31: the Tier 1 risk-based capital ratio, value 4.9%; contribution to the score · 2016-03-31 · +0.623 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F88 · Driver up #3 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 10.4%; contribution to the score · 2016-03-31 · +0.450 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F96 · Last quarter the bank reported · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
