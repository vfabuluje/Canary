---
cert: 58018
name: "St Louis Bank"
as_of: 2026-06-30
rank: 20
n_banks: 4313
percentile: 99.55947136563876
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:54"
writer_model: "claude-opus-5-5"
checked: true
---

# St Louis Bank (cert 58018)

*Outcome not yet known.*

## Summary

St Louis Bank, a Missouri bank, ranked 20 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, which puts it in the 99.6th percentile, where higher means riskier. That placed it on Canary's watchlist, which covers the top 2% of banks by score. Its funding stands out most: brokered deposits, which is money placed through middlemen rather than gathered from local customers, made up 42.2% of its deposits against a national median of 0.0%. Its capital cushions were thinner and its problem loans higher than at the typical bank.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below typical levels: equity was 8.6% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.8% versus 11.0%. Risk-based measures, which weight assets by how risky they are, were also lower, with a Tier 1 ratio of 10.0% against a median of 14.6% and a total capital ratio of 11.3% against 15.8%.

Credit quality was weaker than at most banks: loans 90 or more days late or no longer paying interest were 2.9% of loans versus a median of 0.5%, and nonaccrual assets plus foreclosed property were 2.5% of assets versus 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 25.5% against a median of 2.9%, and commercial real estate loans were 40.1% of loans versus 23.6%.

On funding, brokered deposits were 42.2% of deposits against a median of 0.0%, while core deposits, the stable everyday accounts, were only 48.6% of assets versus 75.5%. Loans equaled 90.2% of deposits versus a median of 80.2%, and cash was 3.2% of assets versus 6.2%. Unrealized losses on bonds available for sale, meaning drops in market value not yet booked, were 6.6% of equity, somewhat above the median of 5.6%.

## Understanding the score

As of 2026-06-30, St Louis Bank ranked 20 out of 4,313 banks, placing it in the 99.6th percentile on a scale of 0 to 100 where higher means riskier; its raw model score was 0.3539. It was flagged on the watchlist, one of 87 banks that quarter, which is the top 2% by score.

The five features that pushed the score up most were brokered deposits at 42.2% of deposits, losses on available-for-sale bonds at 6.6% of equity, core deposits at 48.6% of assets, the efficiency ratio (operating costs as a share of revenue) at 56.8%, and interest expense at 2.4% of assets. The brokered deposit figure had by far the largest upward contribution, at +1.489.

The five features that pulled the score down most were return on equity (profit as a share of equity) at 10.7%, the Tier 1 risk-based capital ratio at 10.0%, loans 30-89 days past due at 0.5% of assets, the Texas ratio at 25.5%, and construction loans at 10.9% of loans. The largest downward contribution came from return on equity, at -0.656.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 421 | 4,589 |  |
| 2024-12-31 | 287 | 4,560 |  |
| 2025-03-31 | 225 | 4,536 |  |
| 2025-06-30 | 156 | 4,494 |  |
| 2025-09-30 | 113 | 4,452 |  |
| 2025-12-31 | 247 | 4,411 |  |
| 2026-03-31 | 21 | 4,353 | ▲ watchlist |
| 2026-06-30 | 20 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank's case is an open bank that remains on the watchlist rather than one that has stopped operating. Our fact sheet contains no data from after the as-of quarter, so we cannot yet say whether the risk signals the model picked up will ease or worsen. Its place on the list rests on the funding, capital and credit patterns described in the earlier sections.

## What happened next

Looking back in hindsight, our data shows no later quarters for this bank beyond the as-of quarter, so there are no later ranks or flags to report here. The bank is treated as still open and still on the watchlist; future quarterly filings will show whether its rank moves.

## Sources

- F1 · Bank name · n/a · St Louis Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MO · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.3539 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 20 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 40.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 90.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 42.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 42.2%; contribution to the score · 2026-06-30 · +1.489 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.6%; contribution to the score · 2026-06-30 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 48.6%; contribution to the score · 2026-06-30 · +0.440 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 56.8%; contribution to the score · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.256 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 10.7%; contribution to the score · 2026-06-30 · -0.656 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.0%; contribution to the score · 2026-06-30 · -0.600 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.5%; contribution to the score · 2026-06-30 · -0.424 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature texas_ratio contribution
- F84 · Driver down #5: construction loans as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
