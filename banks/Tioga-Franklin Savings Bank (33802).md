---
cert: 33802
name: "Tioga-Franklin Savings Bank"
as_of: 2026-06-30
rank: 1
n_banks: 4313
percentile: 100.0
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Tioga-Franklin Savings Bank (cert 33802)

*Outcome not yet known.*

## Summary

Tioga-Franklin Savings Bank, a small Pennsylvania savings bank, ranked 1 out of 4,313 banks on Canary's risk score for 2026-06-30, which put it at the 100.0th percentile, the riskiest end of the scale. It was flagged on the watchlist that quarter. Its capital cushion was very thin, with equity at 2.0% of assets against a national median of 10.6%, and it was losing money, with return on assets of -3.4%. The bank held $68.4 million in total assets, well below the national median of $384.7 million.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels as of 2026-06-30. Equity was 2.0% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 2.1% versus 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against riskier assets, was 2.9% against a median of 14.6%, and the total risk-based capital ratio was 4.1% against 15.8%.

Credit quality, meaning how well borrowers are repaying, was also weak. Loans 90 or more days past due or no longer earning interest made up 9.2% of loans, compared with a national median of 0.5%, and nonaccrual assets plus foreclosed property were 6.8% of assets versus 0.3%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 257.0% against a median of 2.9%. Earnings were negative: return on equity was -121.2% versus a median of 11.6%, and the efficiency ratio (operating costs as a share of revenue) was 188.7% versus 62.1%.

Funding looked less alarming: uninsured deposits, those above the government insurance limit, were 6.4% of deposits, well below the median of 24.8%, though volatile funding was 13.1% of assets versus 9.0% and interest expense was 3.4% of assets versus 1.6%. Unrealized losses on bonds available for sale were modest at 1.6% of equity, below the national median of 5.6%.

## Understanding the score

For 2026-06-30 the bank ranked 1 of 4,313 banks, placing it at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the top 2% of banks, which was 87 banks that quarter, and this bank was flagged.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 2.9% (contribution +1.705), return on equity at -121.2% (+1.638), the Texas ratio at 257.0% (+1.153), loans 90+ days past due or not accruing interest at 9.2% of loans (+0.544), and the total risk-based capital ratio at 4.1% (+0.488).

The five factors pulling the score down most were construction loans at 2.4% of loans (contribution -0.265), loans 30-89 days past due at 0.4% of assets (-0.239), loan-loss reserves at 1.3% of loans (-0.098), commercial real estate loans at 31.8% of loans (-0.070), and deposit growth over the past four quarters at 9.5% (-0.069). These offsetting factors were small next to the capital, earnings and bad-loan figures driving the score up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3 | 4,589 | ▲ watchlist |
| 2024-12-31 | 4 | 4,560 | ▲ watchlist |
| 2025-03-31 | 4 | 4,536 | ▲ watchlist |
| 2025-06-30 | 2 | 4,494 | ▲ watchlist |
| 2025-09-30 | 5 | 4,452 | ▲ watchlist |
| 2025-12-31 | 4 | 4,411 | ▲ watchlist |
| 2026-03-31 | 4 | 4,353 | ▲ watchlist |
| 2026-06-30 | 1 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

Hindsight view: this bank is in the open-watchlist group, meaning it was flagged by the model and no later outcome is recorded in our data. The fact sheet contains no information from after the as-of quarter, so there is not yet any hindsight evidence on whether the warning signs eased or worsened. Its place on the watchlist rests on the as-of figures described above, chiefly very thin capital, heavy losses and a high share of bad loans.

## What happened next

Hindsight view: our data does not yet include any quarter after the as-of date for this bank. There are no later ranks, watchlist flags or reporting records to show here, so what happened next cannot be described from the data. The score history table will show later quarters once they are reported.

## Sources

- F1 · Bank name · n/a · Tioga-Franklin Savings Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 6.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 257.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -121.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 188.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $68.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2026-06-30 · +1.705 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -121.2%; contribution to the score · 2026-06-30 · +1.638 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 257.0%; contribution to the score · 2026-06-30 · +1.153 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 9.2%; contribution to the score · 2026-06-30 · +0.544 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.1%; contribution to the score · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: construction loans as a share of loans, value 2.4%; contribution to the score · 2026-06-30 · -0.265 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.4%; contribution to the score · 2026-06-30 · -0.239 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: loan-loss reserves as a share of loans, value 1.3%; contribution to the score · 2026-06-30 · -0.098 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 31.8%; contribution to the score · 2026-06-30 · -0.070 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value 9.5%; contribution to the score · 2026-06-30 · -0.069 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
