---
cert: 18265
name: "Ericson State Bank"
as_of: 2019-12-31
rank: 4
n_banks: 5244
percentile: 99.94279176201373
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-02-14
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Ericson State Bank (cert 18265)

*Hindsight: failed 2020-02-14. Canary flagged it 4 quarters ahead.*

## Summary

Ericson State Bank, a Nebraska bank, ranked 4 out of 5,244 banks nationally on Canary's risk score as of 2019-12-31, placing it in the 99.9th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was very thin, with equity at 3.7% of assets against a national median of 11.4%, and a large share of its loans had gone bad.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was far below typical levels: the leverage ratio (core capital as a share of average assets) was 3.4% versus a national median of 10.9%. Its Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 4.3% against a median of 15.5%, and its total risk-based capital ratio was 5.6% against 16.6%.

Credit quality was poor: loans 90+ days past due or no longer accruing interest made up 6.9% of loans, compared with a national median of 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 90.1% versus a median of 3.6%. The bank wrote off loans at an annualized 7.1% of loans against a median of 0.0%, set aside provisions for future loan losses equal to 6.9% of assets against 0.1%, and posted a return on assets of -3.4% versus a median of 1.1%.

On funding and liquidity, cash was just 0.5% of assets compared with a median of 7.2%, and brokered deposits, money placed through middlemen, were 4.2% of deposits against a median of 0.0%. Losses on bonds held to maturity equaled -7.5% of equity, while the national median was 0.0%.

## Understanding the score

As of 2019-12-31, Ericson State Bank ranked 4 of 5,244 banks, in the 99.9th percentile on a 0 to 100 scale where higher means riskier. It was one of 105 banks on the watchlist that quarter, a list made up of the top 2% of banks by score.

The factors pushing the score up most were the Tier 1 risk-based capital ratio at 4.3%, return on equity (profit as a share of equity) at -48.4%, and the Texas ratio at 90.1%. Also raising it were loans 90+ days past due or not accruing interest at 6.9% of loans and the annualized provision for loan losses at 6.9% of assets.

Pulling the score down were losses on bonds held to maturity at -7.5% of equity, construction loans at 0.0% of loans, and a net interest margin (the spread earned on lending and investing) of 4.0%. Core deposits, the stable everyday deposits, at 83.8% of assets and volatile funding at 8.3% of assets also lowered the score slightly.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-03-31 | 275 | 5,674 |  |
| 2018-06-30 | 252 | 5,610 |  |
| 2018-09-30 | 253 | 5,544 |  |
| 2018-12-31 | 11 | 5,473 | ▲ watchlist |
| 2019-03-31 | 9 | 5,428 | ▲ watchlist (first flag) |
| 2019-06-30 | 10 | 5,369 | ▲ watchlist |
| 2019-09-30 | 11 | 5,325 | ▲ watchlist |
| 2019-12-31 | 4 | 5,244 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Ericson State Bank in the quarter ending 2019-03-31, 4 quarters before it failed on 2020-02-14. At that first flag, the main drivers raising the score were a Texas ratio of 77.2% and loans 90+ days past due or not accruing interest at 8.8% of loans. Notably, the bank still looked profitable then, with return on equity of 26.6% and return on assets of 2.1%, which held the score down, yet the model flagged it on its troubled loans.

## What happened next

Looking back with hindsight, the bank failed on 2020-02-14. Its last report in our data was for the quarter ending 2019-12-31, after which it stopped reporting; our data does not distinguish a merger from a closure, but the failure date confirms the outcome here.

## Sources

- F1 · Bank name · n/a · Ericson State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NE · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-12-31 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-12-31 · 5,244 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-12-31 · 105 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-12-31 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-12-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 3.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-12-31 · 15.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-12-31 · 5.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-12-31 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2019-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 90.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 3.6% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-12-31 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-12-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-12-31 · 7.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-12-31 · -7.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 4.3%; contribution to the score · 2019-12-31 · +1.915 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -48.4%; contribution to the score · 2019-12-31 · +0.809 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 90.1%; contribution to the score · 2019-12-31 · +0.500 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 6.9%; contribution to the score · 2019-12-31 · +0.476 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: annualized provision for loan losses as a share of assets, value 6.9%; contribution to the score · 2019-12-31 · +0.196 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F80 · Driver down #1: losses on bonds held to maturity, as a share of equity, value -7.5%; contribution to the score · 2019-12-31 · -0.784 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F81 · Driver down #2: construction loans as a share of loans, value 0.0%; contribution to the score · 2019-12-31 · -0.309 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: net interest margin (the spread earned on lending and investing), value 4.0%; contribution to the score · 2019-12-31 · -0.149 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F83 · Driver down #4: core deposits as a share of assets, value 83.8%; contribution to the score · 2019-12-31 · -0.131 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 8.3%; contribution to the score · 2019-12-31 · -0.092 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-02-14 · 2020-02-14 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-03-31 · 2019-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-03-31: the Texas ratio (troubled assets against capital plus reserves), value 77.2%; contribution to the score · 2019-03-31 · +1.067 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2019-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2019-03-31 · +0.760 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F93 · Driver down #1 at 2019-03-31: return on equity (profit as a share of equity), value 26.6%; contribution to the score · 2019-03-31 · -0.616 · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Driver down #3 at 2019-03-31: return on assets (profit as a share of assets), value 2.1%; contribution to the score · 2019-03-31 · -0.295 · data/analyst/scores.parquet: feature return_on_assets contribution
- F98 · Last quarter the bank reported · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
