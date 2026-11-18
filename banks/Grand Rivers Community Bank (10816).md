---
cert: 10816
name: "Grand Rivers Community Bank"
as_of: 2026-06-30
rank: 12
n_banks: 4313
percentile: 99.74495710642243
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Grand Rivers Community Bank (cert 10816)

*Outcome not yet known.*

## Summary

Grand Rivers Community Bank, a small Illinois bank, held a national rank of 12 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.7th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. The main concerns are a very large share of seriously late or non-paying loans (19.0% of loans), heavy losses (return on equity of -38.7%), and capital ratios below the national median.

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, was thinner than at a typical bank: equity was 8.6% of assets against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 8.4% versus a median of 11.0%, and the Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 10.7% versus 14.6%. The total risk-based capital ratio was 12.0%, below the median of 15.8%.

Credit quality, meaning how well borrowers are repaying, stands out most: loans 90 or more days past due or no longer earning interest were 19.0% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 12.6% of assets versus a median of 0.3%, and loans that were late but not yet seriously overdue were 6.4% of assets versus 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 113.1% against a median of 2.9%, although loan-loss reserves set aside for bad loans were well above normal at 5.0% of loans versus 1.2%. The bank was losing money, with return on assets of -3.4% versus a median of 1.2%, and operating costs were 169.4% of revenue versus a median of 62.1%.

Funding and liquidity looked steadier: core deposits, the stable everyday accounts, were 89.2% of assets versus a median of 75.5%, cash was 13.8% of assets versus 6.2%, and volatile funding was 0.0% versus 9.0%. Uninsured deposits, those above the FDIC insurance limit, were 21.6% of deposits, a bit below the median of 24.8%, and unrealized losses on bonds available for sale were just 0.1% of equity versus a median of 5.6%. The bank is very small and shrinking, with total assets of $15.1 million versus a median of $384.7 million and asset growth over the past four quarters of -14.0% versus 4.5%.

## Understanding the score

As of 2026-06-30, the bank held a national rank of 12 out of 4,313 banks, in the 99.7th percentile on a scale of 0 to 100 where higher means riskier, with a raw model score of 0.5394. It was flagged for the watchlist, one of 87 banks that quarter, which is the top 2% by score.

The five features pushing the score up most were: seriously late or non-paying loans at 19.0% of loans (+1.079), return on equity at -38.7% (+0.701), the Texas ratio at 113.1% (+0.672), loans that were late but not yet seriously overdue at 6.4% of assets (+0.550), and small size, with total assets of $15.1 million (+0.459).

The five features pulling the score down most were: the Tier 1 risk-based capital ratio at 10.7% (-1.502), interest expense at 1.0% of assets (-0.902), the total risk-based capital ratio at 12.0% (-0.318), commercial real estate loans at 42.0% of loans (-0.240), and construction loans at 0.0% of loans (-0.198).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 7 | 4,589 | ▲ watchlist |
| 2024-12-31 | 207 | 4,560 |  |
| 2025-03-31 | 17 | 4,536 | ▲ watchlist |
| 2025-06-30 | 14 | 4,494 | ▲ watchlist |
| 2025-09-30 | 13 | 4,452 | ▲ watchlist |
| 2025-12-31 | 12 | 4,411 | ▲ watchlist |
| 2026-03-31 | 17 | 4,353 | ▲ watchlist |
| 2026-06-30 | 12 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank falls in the open-watchlist case: it remains open and on Canary's watchlist, so there is no failure to explain. The fact sheet contains no data from after the as-of quarter, so this hindsight view cannot say whether the warning signs above have since improved or worsened.

## What happened next

Hindsight view: no later ranks, flags or reporting status beyond the as-of quarter are available in this fact sheet. The bank is classed as still open and on the watchlist; any further quarters will appear in the score history table as they are reported.

## Sources

- F1 · Bank name · n/a · Grand Rivers Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.5394 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 12 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 113.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 169.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 21.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $15.1 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -14.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 19.0%; contribution to the score · 2026-06-30 · +1.079 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -38.7%; contribution to the score · 2026-06-30 · +0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 113.1%; contribution to the score · 2026-06-30 · +0.672 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 6.4%; contribution to the score · 2026-06-30 · +0.550 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: total assets, value $15.1 million; contribution to the score · 2026-06-30 · +0.459 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.7%; contribution to the score · 2026-06-30 · -1.502 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2026-06-30 · -0.902 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 12.0%; contribution to the score · 2026-06-30 · -0.318 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 42.0%; contribution to the score · 2026-06-30 · -0.240 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.198 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
