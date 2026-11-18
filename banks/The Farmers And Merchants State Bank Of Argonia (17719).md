---
cert: 17719
name: "The Farmers And Merchants State Bank Of Argonia"
as_of: 2017-09-30
rank: 1
n_banks: 5806
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-10-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# The Farmers And Merchants State Bank Of Argonia (cert 17719)

*Hindsight: failed 2017-10-13. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-09-30, The Farmers And Merchants State Bank Of Argonia, a bank based in KS, ranked 1 out of 5,806 banks in Canary's national risk ranking, placing it in the 100.0th percentile. That put it on Canary's watchlist, which covers the 2% of banks with the highest scores. Its capital, the owners' cushion that absorbs losses, was negative at -1.1% of assets, against a national median of 11.0%. Problem loans and loan losses were also far above typical levels.

## Warning signs in the data

Capital was below zero on every measure: equity was -1.1% of assets versus a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was -1.3% versus 10.6%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by riskiness, was -2.3% versus a median of 15.1%, and the total risk-based capital ratio was -1.0% versus 16.3%.

Loan quality was poor: loans 90+ days past due or not accruing interest were 11.5% of loans, against a median of 0.6%, and loans 30-89 days past due were 3.0% of assets versus 0.3%. Annualized loan write-offs, net of recoveries, were 10.5% of loans versus a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 8.1% of assets versus 0.1%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 292.3%, far above the median of 4.5%, and return on assets was -10.5% versus 0.9%.

On funding, brokered deposits (money placed through middlemen) were 10.3% of deposits versus a median of 0.0%, and Federal Home Loan Bank borrowings were 13.8% of assets versus 0.9%. Deposits shrank by -9.9% over the past four quarters while the median bank grew them 3.8%, though cash was a high 20.8% of assets versus 6.1%. Losses on bonds available for sale were -5.0% of equity, compared with a median of 0.0%.

## Understanding the score

As of 2017-09-30, the bank ranked 1 of 5,806 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier, with a model score of 0.9971. It was flagged on the watchlist, one of 117 banks that quarter, which makes up the top 2% of scores.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at -2.3% (+2.007), return on equity at -282.8% (+1.348), the Texas ratio at 292.3% (+1.262), the leverage ratio at -1.3% (+0.692), and the total risk-based capital ratio at -1.0% (+0.562). The five factors pulling the score down most were interest expense at 0.9% of assets (-0.635), losses on bonds available for sale at -5.0% of equity (-0.248), construction loans at 0.5% of loans (-0.168), deposit growth at -9.9% (-0.125), and net interest margin at 4.2% (-0.122).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 375 | 6,193 |  |
| 2016-06-30 | 426 | 6,129 |  |
| 2016-09-30 | 108 | 6,051 | ▲ watchlist |
| 2016-12-31 | 22 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 12 | 5,925 | ▲ watchlist |
| 2017-06-30 | 3 | 5,856 | ▲ watchlist |
| 2017-09-30 | 1 | 5,806 | ▲ watchlist |

## How early Canary caught it

In hindsight, the bank failed on 2017-10-13. Canary first flagged it in the quarter ending 2016-12-31, a lead time of 4 quarters before the failure.

At that first flag, the main drivers were loans 90+ days past due or not accruing interest at 12.1% of loans (+0.956), the Texas ratio at 115.6% (+0.747), and loans 30-89 days past due at 4.0% of assets (+0.575). Its Tier 1 risk-based capital ratio was still positive then at 9.1%, which pulled the score down (-0.226), so the early flag came from loan problems before capital turned negative.

## What happened next

In hindsight, the last quarter the bank reported was 2017-09-30, and its failure date was 2017-10-13. Because it stopped reporting after that, there are no later ranks or flags to show.

## Sources

- F1 · Bank name · n/a · The Farmers And Merchants State Bank Of Argonia · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F5 · Model score · 2017-09-30 · 0.9971 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2017-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-09-30 · 5,806 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-09-30 · 117 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-09-30 · -1.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · -1.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-09-30 · -2.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-09-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-09-30 · -1.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-09-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 11.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2017-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 292.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-09-30 · 10.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 13.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-09-30 · -5.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2017-09-30 · -9.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2017-09-30 · 3.8% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -2.3%; contribution to the score · 2017-09-30 · +2.007 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -282.8%; contribution to the score · 2017-09-30 · +1.348 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 292.3%; contribution to the score · 2017-09-30 · +1.262 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.3%; contribution to the score · 2017-09-30 · +0.692 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value -1.0%; contribution to the score · 2017-09-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.9%; contribution to the score · 2017-09-30 · -0.635 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -5.0%; contribution to the score · 2017-09-30 · -0.248 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.5%; contribution to the score · 2017-09-30 · -0.168 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: deposit growth over the past four quarters, value -9.9%; contribution to the score · 2017-09-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 4.2%; contribution to the score · 2017-09-30 · -0.122 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2017-10-13 · 2017-10-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 12.1%; contribution to the score · 2016-12-31 · +0.956 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F89 · Driver up #2 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 115.6%; contribution to the score · 2016-12-31 · +0.747 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-12-31: loans 30-89 days past due, as a share of assets, value 4.0%; contribution to the score · 2016-12-31 · +0.575 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F95 · Driver down #3 at 2016-12-31: the Tier 1 risk-based capital ratio, value 9.1%; contribution to the score · 2016-12-31 · -0.226 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
