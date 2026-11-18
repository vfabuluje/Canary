---
cert: 28480
name: "Columbia Savings&Loan Assn"
as_of: 2026-06-30
rank: 5
n_banks: 4313
percentile: 99.90725712960817
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:45"
writer_model: "claude-opus-5-5"
checked: true
---

# Columbia Savings&Loan Assn (cert 28480)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Columbia Savings&Loan Assn, a small Wisconsin savings institution, ranked 5 out of 4,313 banks nationally on Canary's risk score, placing it in the 99.9th percentile. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was thin, many of its loans were seriously behind on payments, and it was losing money, all well out of line with typical banks.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was low: equity was 5.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 5.5% against a median of 11.0%. Risk-weighted measures told the same story, with a Tier 1 risk-based capital ratio of 7.6% versus a median of 14.6% and a total risk-based capital ratio of 8.9% versus 15.8%.

Credit quality was the starkest problem: loans seriously past due or no longer earning interest were 19.5% of loans, far above the national median of 0.5%. Loans in the earlier stages of lateness were 4.6% of assets versus a median of 0.2%, and nonaccrual assets plus foreclosed property were 4.4% of assets versus 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 231.1% against a median of 2.9%, and the bank's return on assets (profit as a share of assets) was -3.3% versus a median of 1.2%.

Funding looked steadier: uninsured deposits, those above the government insurance limit, were only 1.7% of deposits against a median of 24.8%, and core deposits, a stable funding source, were 83.2% of assets versus 75.5%. Deposit growth over the past four quarters was -10.3% while the median bank grew 4.2%. Losses on bonds available for sale were 0.0% of equity, well below the median of 5.6%, partly because securities made up just 0.2% of assets versus a median of 17.6%.

## Understanding the score

On 2026-06-30 the bank ranked 5 of 4,313 banks, which is the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 87 banks that quarter, a list that holds the top 2% of scores.

The five factors pushing the score up most were the Texas ratio at 231.1%, return on equity (profit as a share of the owners' stake) at -53.3%, seriously late or nonaccruing loans at 19.5% of loans, securities at 0.2% of assets, and uninsured deposits at 1.7% of deposits.

The five factors pulling the score down most were interest expense at 0.6% of assets, nonaccrual assets and foreclosed property at 4.4% of assets, loans at 83.4% of deposits, the leverage ratio at 5.5%, and deposit growth over the past four quarters at -10.3%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 187 | 4,589 |  |
| 2024-12-31 | 56 | 4,560 | ▲ watchlist |
| 2025-03-31 | 124 | 4,536 |  |
| 2025-06-30 | 134 | 4,494 |  |
| 2025-09-30 | 116 | 4,452 |  |
| 2025-12-31 | 9 | 4,411 | ▲ watchlist |
| 2026-03-31 | 11 | 4,353 | ▲ watchlist |
| 2026-06-30 | 5 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank's case is that it remains open and on the watchlist. The fact sheet contains no data from after the as-of quarter, so there is no later event to explain; the watchlist placement rests on the weak capital, heavy problem loans and losses described above.

## What happened next

Looking back in hindsight, our data holds no later ranks, flags or reports for this bank beyond the as-of quarter. It is therefore treated as still open and still on the watchlist, with no later results available yet to confirm or contradict the score.

## Sources

- F1 · Bank name · n/a · Columbia Savings&Loan Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 5 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 19.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 231.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 83.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -10.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 231.1%; contribution to the score · 2026-06-30 · +1.217 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -53.3%; contribution to the score · 2026-06-30 · +0.679 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 19.5%; contribution to the score · 2026-06-30 · +0.407 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: securities as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · +0.254 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F79 · Driver up #5: uninsured deposits as a share of deposits, value 1.7%; contribution to the score · 2026-06-30 · +0.251 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2026-06-30 · -1.050 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 4.4%; contribution to the score · 2026-06-30 · -0.341 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F82 · Driver down #3: loans as a share of deposits, value 83.4%; contribution to the score · 2026-06-30 · -0.093 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F83 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 5.5%; contribution to the score · 2026-06-30 · -0.087 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -10.3%; contribution to the score · 2026-06-30 · -0.080 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
