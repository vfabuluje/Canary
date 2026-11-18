---
cert: 35495
name: "Proficio Bank"
as_of: 2016-12-31
rank: 6
n_banks: 5983
percentile: 99.91642988467324
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-03-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Proficio Bank (cert 35495)

*Hindsight: failed 2017-03-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Proficio Bank, a UT bank with certificate number 35495, ranked 6 out of 5,983 banks nationally on Canary's risk score, placing it in the 99.9th percentile. The bank was flagged on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was very thin, with equity at 3.4% of assets against a national median of 10.7%, and it was losing money, with a return on assets of -4.5%.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was far below typical levels: equity was 3.4% of assets versus a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was 3.1% versus 10.4%. Its Tier 1 risk-based capital ratio, which weighs capital against the riskiness of assets, was 3.6% versus a median of 15.0%, and its total risk-based capital ratio was 4.7% versus 16.2%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 2.2% of loans versus a median of 0.6%, and nonaccrual assets plus foreclosed property were 5.0% of assets versus 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 114.1% against a national median of 4.9%. Earnings were deeply negative, with a return on equity of -133.2% versus a median of 8.0%, and an efficiency ratio (operating costs as a share of revenue) of 179.2% versus 69.7%.

On funding, volatile funding (money that can leave quickly) was 15.4% of assets versus a median of 5.2%, and interest expense was 1.3% of assets versus 0.4%, while uninsured deposits were only 0.8% of deposits versus 17.3% and cash was 11.1% of assets versus 6.6%. The figure for losses on bonds available for sale was -4.9% of equity, compared with a national median of 0.7%. The bank was also shrinking, with asset growth over the past four quarters of -37.7% versus a median of 3.5%.

## Understanding the score

As of 2016-12-31, Proficio Bank ranked 6 out of 5,983 banks, putting it in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score and contained 120 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 3.6%, return on equity at -133.2%, the Texas ratio at 114.1%, the total risk-based capital ratio at 4.7%, and asset growth over the past four quarters at -37.7%. The five factors that pulled the score down most were loans 90+ days past due or not accruing at 2.2% of loans, interest expense at 1.3% of assets, losses on bonds available for sale at -4.9% of equity, loans 30-89 days past due at 0.4% of assets, and commercial real estate loans at 60.6% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 9 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 7 | 6,129 | ▲ watchlist |
| 2016-09-30 | 14 | 6,051 | ▲ watchlist |
| 2016-12-31 | 6 | 5,983 | ▲ watchlist |

## How early Canary caught it

In hindsight, Proficio Bank failed on 2017-03-03. Canary first flagged it in the quarter ending 2016-03-31, a lead time of 4 quarters before the failure. At that first flag, the top drivers were a Tier 1 risk-based capital ratio of 4.2%, a return on equity of -197.5%, and a Texas ratio of 175.8%.

## What happened next

Looking back, the bank failed on March 3, 2017. The last quarter it reported data was 2016-12-31, so there are no later ranks or flags; in our data, stopping reporting can mean a merger or a closure, and the two are not distinguished.

## Sources

- F1 · Bank name · n/a · Proficio Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 35495 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 3.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 4.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 2.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 5.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 114.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2016-12-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 0.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 15.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 11.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · -4.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -37.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.6%; contribution to the score · 2016-12-31 · +2.373 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -133.2%; contribution to the score · 2016-12-31 · +1.406 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 114.1%; contribution to the score · 2016-12-31 · +0.569 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 4.7%; contribution to the score · 2016-12-31 · +0.495 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: asset growth over the past four quarters, value -37.7%; contribution to the score · 2016-12-31 · +0.370 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 2.2%; contribution to the score · 2016-12-31 · -0.414 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2016-12-31 · -0.333 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -4.9%; contribution to the score · 2016-12-31 · -0.327 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.4%; contribution to the score · 2016-12-31 · -0.293 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 60.6%; contribution to the score · 2016-12-31 · -0.275 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-03-03 · 2017-03-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +2.485 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: return on equity (profit as a share of equity), value -197.5%; contribution to the score · 2016-03-31 · +1.496 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 175.8%; contribution to the score · 2016-03-31 · +1.038 · data/analyst/scores.parquet: feature texas_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
