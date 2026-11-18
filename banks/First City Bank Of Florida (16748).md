---
cert: 16748
name: "First City Bank Of Florida"
as_of: 2020-09-30
rank: 2
n_banks: 5098
percentile: 99.98038446449588
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-16
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# First City Bank Of Florida (cert 16748)

*Hindsight: failed 2020-10-16. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, First City Bank Of Florida, a bank in FL, ranked 2 out of 5,098 banks in Canary's national risk ranking, which places it in the 100.0th percentile. It was on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was very thin, with equity, the owners' stake, at 1.5% of assets against a national median of 10.9%. Its troubled assets were also very large relative to its capital, and it was losing money.

## Warning signs in the data

Capital, the buffer that absorbs losses, was far below typical levels: equity was 1.5% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 1.4% against a median of 10.2%. The Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 2.5% against a median of 14.7%, and the total risk-based capital ratio was 3.7% against 15.9%. The bank was also unprofitable, with return on assets of -1.5% against a median of 1.0%, and its efficiency ratio (operating costs as a share of revenue) was 148.2% against 65.6%.

Credit quality was weak: nonaccrual assets (loans no longer paying interest) and foreclosed property made up 12.7% of assets, far above the national median of 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 489.0% against a median of 3.4%. Loans 30-89 days past due were 3.0% of assets against a median of 0.2%, and construction loans were 15.6% of loans against a median of 4.3%.

Funding looked steadier: core deposits, the stable everyday kind, were 98.1% of assets against a median of 78.8%, brokered deposits were 0.0%, and cash was 32.0% of assets against a median of 9.6%. On bonds, unrealized losses on bonds available for sale equaled -11.2% of equity, deeper than the national median of -2.5%.

## Understanding the score

As of 2020-09-30, the bank ranked 2 of 5,098 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 102 banks that quarter in the riskiest 2%.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 2.5%, the Texas ratio at 489.0%, return on equity (profit as a share of the owners' stake) at -68.6%, the leverage ratio at 1.4%, and the total risk-based capital ratio at 3.7%. The five factors pulling the score down most were loans 90+ days past due or not accruing interest at 1.6% of loans, interest expense at 0.3% of assets, losses on bonds available for sale at -11.2% of equity, uninsured deposits at 12.3% of deposits, and net interest margin (the spread earned on lending and investing) at 3.7%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 4 | 5,473 | ▲ watchlist |
| 2019-03-31 | 3 | 5,428 | ▲ watchlist |
| 2019-06-30 | 4 | 5,369 | ▲ watchlist |
| 2019-09-30 | 5 | 5,325 | ▲ watchlist |
| 2019-12-31 | 3 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 2 | 5,182 | ▲ watchlist |
| 2020-06-30 | 2 | 5,131 | ▲ watchlist |
| 2020-09-30 | 2 | 5,098 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged this bank in the quarter ending 2019-12-31, and the bank failed on 2020-10-16. That gave a lead time of 4 quarters before the failure. At that first flag, the top drivers were already capital and troubled assets: the Tier 1 risk-based capital ratio was 3.4% and the Texas ratio was 473.5%. Loans 90+ days past due or not accruing interest were then 6.6% of loans, and the leverage ratio was 2.4%.

## What happened next

In hindsight, the bank's last reported quarter was 2020-09-30, the same quarter as this memo's as-of date. The bank failed on 2020-10-16, a few weeks after that report, so no later ranks exist.

## Sources

- F1 · Bank name · n/a · First City Bank Of Florida · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · FL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-09-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 1.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-09-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2020-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2020-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2020-09-30 · 15.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2020-09-30 · 4.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 489.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-09-30 · -1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F55 · Bank: core deposits as a share of assets · 2020-09-30 · 98.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-09-30 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-09-30 · 32.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-09-30 · 9.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.5%; contribution to the score · 2020-09-30 · +2.082 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 489.0%; contribution to the score · 2020-09-30 · +1.510 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -68.6%; contribution to the score · 2020-09-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2020-09-30 · +0.590 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 3.7%; contribution to the score · 2020-09-30 · +0.436 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 1.6%; contribution to the score · 2020-09-30 · -0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2020-09-30 · -0.622 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -11.2%; contribution to the score · 2020-09-30 · -0.375 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 12.3%; contribution to the score · 2020-09-30 · -0.131 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2020-09-30 · -0.108 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2020-10-16 · 2020-10-16 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: the Tier 1 risk-based capital ratio, value 3.4%; contribution to the score · 2019-12-31 · +1.988 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 473.5%; contribution to the score · 2019-12-31 · +1.290 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2019-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 6.6%; contribution to the score · 2019-12-31 · +0.452 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-12-31: the leverage ratio (core capital as a share of average assets), value 2.4%; contribution to the score · 2019-12-31 · +0.380 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
