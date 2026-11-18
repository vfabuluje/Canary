---
cert: 27332
name: "Republic Bank"
as_of: 2023-12-31
rank: 135
n_banks: 4658
percentile: 97.12322885358523
flagged: false
outcome: "caught"
after_test_window: false
failure_date: 2024-04-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Republic Bank (cert 27332)

*Hindsight: failed 2024-04-26. Canary flagged it 4 quarters ahead.*

## Summary

Republic Bank, based in PA (certificate 27332), ranked 135 out of 4,658 banks nationally on Canary's risk score as of 2023-12-31, with a percentile of 97.1% on a scale where higher means riskier. Its capital cushion was thin, with equity (the owners' stake) at 1.8% of assets against a national median of 9.5%. It was also losing money, with a return on equity (profit as a share of the owners' stake) of -36.6% against a national median of 10.8%. Despite its high rank, it was not on Canary's watchlist that quarter.

## Warning signs in the data

Capital, the money that absorbs losses, was far below typical levels: equity was 1.8% of assets against a national median of 9.5%, and the leverage ratio (core capital as a share of average assets) was 4.4% against 10.6%. The total risk-based capital ratio, which weighs capital against how risky the assets are, was 9.6% against a median of 15.3%. Earnings were weak, with return on assets of -0.7% against a median of 1.0%, a net interest margin (the spread earned on lending and investing) of 1.2% against 3.4%, and operating costs at 145.3% of revenue against a median of 66.5%.

The biggest strain was in its bond portfolio, which made up 40.5% of assets against a median of 20.1%. Losses on bonds held to maturity equaled 250.7% of equity against a national median of 0.0%, and losses on bonds available for sale equaled 155.9% of equity against 12.9%. Funding also looked less stable: uninsured deposits (balances above the government insurance limit) were 51.5% of deposits against a median of 23.9%, and deposit growth over the past four quarters was -12.8% against a median of 0.9%. Borrowings from the Federal Home Loan Bank, a lender to banks, were 11.9% of assets against a median of 1.0%.

Problem loans were above the median but still small: loans 90+ days past due or not accruing interest were 0.7% of loans against 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 16.4% against 1.8%. Commercial real estate loans were 42.7% of loans, well above the median of 23.2%.

## Understanding the score

As of 2023-12-31, Republic Bank ranked 135 out of 4,658 banks, with a percentile of 97.1% on a 0 to 100 scale where higher means riskier. Canary's watchlist covers the top 2% of banks, which was 94 banks that quarter, and Republic Bank was not flagged.

The five features pushing the score up most were return on equity at -36.6%, losses on bonds available for sale at 155.9% of equity, equity at 1.8% of assets, the total risk-based capital ratio at 9.6%, and loans at 69.0% of deposits. The five features pulling the score down most were nonaccrual assets and foreclosed property at 0.4% of assets, loans 90+ days past due or not accruing interest at 0.7% of loans, the Texas ratio at 16.4%, loans 30-89 days past due at 0.2% of assets, and construction loans at 4.8% of loans. In short, weak profits, bond losses and thin capital raised the score, while relatively low levels of problem loans held it back.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-03-31 | 178 | 4,861 |  |
| 2022-06-30 | 159 | 4,838 |  |
| 2022-09-30 | 27 | 4,813 | ▲ watchlist |
| 2022-12-31 | 32 | 4,773 | ▲ watchlist |
| 2023-03-31 | 5 | 4,740 | ▲ watchlist |
| 2023-06-30 | 29 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 65 | 4,686 | ▲ watchlist |
| 2023-12-31 | 135 | 4,658 |  |

## How early Canary caught it

In hindsight, Canary first flagged Republic Bank in the quarter ending 2023-06-30, and the bank failed on 2024-04-26, a lead time of 4 quarters. At that first flag, the top drivers pushing the score up were losses on bonds available for sale at 134.7% of equity, return on equity at -30.3%, and equity at 2.1% of assets. These were the same weaknesses in bond losses, profits and capital that still topped the list at the last reported quarter.

## What happened next

In hindsight, Republic Bank failed on 2024-04-26. The last quarter the bank reported data was 2023-12-31, so there are no later ranks or flags for it.

## Sources

- F1 · Bank name · n/a · Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 27332 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-12-31 · 135 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-12-31 · 4,658 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-12-31 · 97.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-12-31 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 4.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-12-31 · 9.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2023-12-31 · 42.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2023-12-31 · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 16.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-12-31 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-12-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2023-12-31 · 10.8% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2023-12-31 · 145.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2023-12-31 · 66.5% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-12-31 · 51.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-12-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 11.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 1.0% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 250.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-12-31 · 155.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-12-31 · 12.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-12-31 · 40.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-12-31 · 20.1% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-12-31 · -12.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-12-31 · 0.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -36.6%; contribution to the score · 2023-12-31 · +1.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 155.9%; contribution to the score · 2023-12-31 · +0.912 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: equity as a share of assets, value 1.8%; contribution to the score · 2023-12-31 · +0.367 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 9.6%; contribution to the score · 2023-12-31 · +0.089 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 69.0%; contribution to the score · 2023-12-31 · +0.087 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: nonaccrual assets and foreclosed property, as a share of assets, value 0.4%; contribution to the score · 2023-12-31 · -1.161 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2023-12-31 · -1.006 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 16.4%; contribution to the score · 2023-12-31 · -0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2023-12-31 · -0.359 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: construction loans as a share of loans, value 4.8%; contribution to the score · 2023-12-31 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2024-04-26 · 2024-04-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 134.7%; contribution to the score · 2023-06-30 · +1.306 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: return on equity (profit as a share of equity), value -30.3%; contribution to the score · 2023-06-30 · +1.044 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2023-06-30: equity as a share of assets, value 2.1%; contribution to the score · 2023-06-30 · +0.233 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F98 · Last quarter the bank reported · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
