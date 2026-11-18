---
cert: 34951
name: "Harvest Community Bank"
as_of: 2016-12-31
rank: 3
n_banks: 5983
percentile: 99.9665719538693
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Harvest Community Bank (cert 34951)

*Hindsight: failed 2017-01-13. Canary flagged it 4 quarters ahead.*

## Summary

Harvest Community Bank, a New Jersey bank, ranked 3 out of 5,983 banks nationally on Canary's risk score as of 2016-12-31, placing it in the 100.0th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital, the owners' money that absorbs losses, was very thin: equity was 1.4% of assets, against a national median of 10.7%. Problem loans were also high, with 18.2% of loans 90+ days past due or not accruing interest, compared with a median of 0.6%.

## Warning signs in the data

Capital was far below normal levels: the leverage ratio (core capital as a share of average assets) was 1.4% versus a national median of 10.4%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by riskiness, was 1.9% versus a median of 15.0%, and the total risk-based capital ratio was 3.2% versus 16.2%.

Credit quality, meaning how reliably borrowers repay, was poor: nonaccrual assets (loans no longer earning interest) and foreclosed property made up 16.3% of assets, against a median of 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 382.7%, far above the median of 4.9%. The bank was losing money, with a return on assets of -1.3% and a return on equity of -64.3%, against medians of 0.9% and 8.0%, and an efficiency ratio (operating costs as a share of revenue) of 143.4% versus 69.7%.

Funding looked steadier: core deposits, a stable funding source, were 96.6% of assets versus a median of 78.8%, and uninsured deposits were just 2.3% of deposits versus 17.3%. Still, deposits shrank by -9.5% over the past four quarters while the median bank grew 3.6%, and losses on bonds available for sale equaled 6.7% of equity, well above the median of 0.7%.

## Understanding the score

As of 2016-12-31, Harvest Community Bank ranked 3 of 5,983 banks, in the 100.0th percentile on a scale of 0 to 100. It was flagged on the watchlist, one of 120 banks that quarter, which makes up the top 2% of banks by score.

The factors pushing the score up most were a Tier 1 risk-based capital ratio of 1.9%, a Texas ratio of 382.7%, a return on equity of -64.3%, problem loans at 18.2% of loans, and a leverage ratio of 1.4%. The factors pulling it down most were interest expense at 0.7% of assets, construction loans at 9.7% of loans, volatile funding (money that can leave quickly) at 1.8% of assets, cash at 5.6% of assets, and an efficiency ratio of 143.4%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 4 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 3 | 6,129 | ▲ watchlist |
| 2016-09-30 | 1 | 6,051 | ▲ watchlist |
| 2016-12-31 | 3 | 5,983 | ▲ watchlist |

## How early Canary caught it

In hindsight, Harvest Community Bank failed on 2017-01-13. Canary first flagged it in the quarter ending 2016-03-31, giving a lead time of 4 quarters before the failure.

At that first flag, the main factors raising the score were a Tier 1 risk-based capital ratio of 2.9%, a Texas ratio of 322.2%, a return on equity of -51.7%, problem loans at 17.9% of loans, and a total risk-based capital ratio of 4.2%. Those same weaknesses were still present, and in most cases worse, by the as-of quarter.

## What happened next

Looking back with hindsight, the last quarter the bank reported data was 2016-12-31. The bank failed shortly afterward, on 2017-01-13, so no later ranks or flags exist for it.

## Sources

- F1 · Bank name · n/a · Harvest Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NJ · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 3.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 18.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 16.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -64.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 143.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 2.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-12-31 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 6.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.9%; contribution to the score · 2016-12-31 · +2.139 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 382.7%; contribution to the score · 2016-12-31 · +1.450 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -64.3%; contribution to the score · 2016-12-31 · +1.282 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 18.2%; contribution to the score · 2016-12-31 · +0.755 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2016-12-31 · +0.636 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.7%; contribution to the score · 2016-12-31 · -0.720 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 9.7%; contribution to the score · 2016-12-31 · -0.124 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 1.8%; contribution to the score · 2016-12-31 · -0.112 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: cash as a share of assets, value 5.6%; contribution to the score · 2016-12-31 · -0.098 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 143.4%; contribution to the score · 2016-12-31 · -0.078 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F85 · Failure date · 2017-01-13 · 2017-01-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2016-03-31 · +2.088 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 322.2%; contribution to the score · 2016-03-31 · +1.217 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -51.7%; contribution to the score · 2016-03-31 · +0.923 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 17.9%; contribution to the score · 2016-03-31 · +0.661 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +0.492 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
