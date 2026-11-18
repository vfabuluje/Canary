---
cert: 5520
name: "Santa Anna National Bank"
as_of: 2025-03-31
rank: 84
n_banks: 4536
percentile: 98.17019400352733
flagged: true
outcome: "missed"
after_test_window: false
failure_date: 2025-06-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:05:28"
writer_model: "claude-opus-5-5"
checked: true
---

# Santa Anna National Bank (cert 5520)

*Hindsight: failed 2025-06-27. Canary did not flag it.*

## Summary

As of 2025-03-31, Santa Anna National Bank, a small bank in TX, ranked 84 out of 4,536 FDIC-insured banks on Canary's risk score, a percentile of 98.2% on a scale where higher means riskier. That put the bank on Canary's watchlist, which covers the riskiest 2% of banks. The biggest push upward came from large paper losses on bonds it could sell, equal to 40.8% of its equity against a national median of 9.3%. Strong profits and few troubled loans pulled the score down.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin: equity was 6.5% of assets, against a national median of 9.9%. The leverage ratio (core capital as a share of average assets) was 8.6%, below the national median of 10.7%. The most striking figure was unrealized losses on bonds available for sale (bonds the bank could sell, valued at current prices), equal to 40.8% of equity, far above the national median of 9.3%. Securities made up 29.5% of assets, well above the national median of 18.3%.

Credit quality looked broadly normal: loans 90+ days past due or not accruing interest were 0.5% of loans, close to the national median of 0.4%. The Texas ratio, which compares troubled assets with capital plus reserves, was 3.7%, a little above the national median of 2.5%. Loans 30-89 days past due were 0.0% of assets, below the national median of 0.3%.

On funding, uninsured deposits (balances above the government insurance limit) were 29.5% of deposits, above the national median of 23.9%. Volatile funding, money that can leave quickly, was 14.6% of assets against a national median of 8.6%, while cash was only 3.7% of assets against a median of 6.9%. The bank was also growing fast, with deposits up 33.2% over the past four quarters versus a national median of 4.6%.

## Understanding the score

On 2025-03-31 the bank ranked 84 of 4,536 banks, a percentile of 98.2% on a scale of 0 to 100 where higher means riskier. It was one of 91 banks on the watchlist that quarter, the group covering the top 2% of scores.

The five factors pushing the score up were: losses on bonds available for sale at 40.8% of equity (contribution +1.665), the efficiency ratio, meaning operating costs as a share of revenue, at 52.9% (+0.354), deposit growth over the past four quarters at 33.2% (+0.274), commercial real estate loans at 6.0% of loans (+0.174), and loans at 56.9% of deposits (+0.119).

The five factors pulling the score down were: the Texas ratio at 3.7% (contribution -1.296), the Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets (-0.914), return on equity at 27.6% (-0.439), loans 90+ days past due or not accruing at 0.5% of loans (-0.304), and return on assets at 1.7% (-0.281).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-06-30 | 525 | 4,714 |  |
| 2023-09-30 | 429 | 4,686 |  |
| 2023-12-31 | 346 | 4,658 |  |
| 2024-03-31 | 282 | 4,640 |  |
| 2024-06-30 | 388 | 4,610 |  |
| 2024-09-30 | 191 | 4,589 |  |
| 2024-12-31 | 297 | 4,560 |  |
| 2025-03-31 | 84 | 4,536 | ▲ watchlist |

## Why the model missed it

In hindsight, the bank failed on June 27, 2025. The model did place the bank on its watchlist at Q1 2025, but that flag came after the 2016-2024 test period and is not counted in the reported results. Because the flag falls outside the period used to measure the model's performance, this case is recorded as a miss in the reported results even though the bank was flagged in real time.

## What happened next

In hindsight, the last quarter the bank reported was 2025-03-31, so there are no later ranks or flags. The bank failed on June 27, 2025.

## Sources

- F1 · Bank name · n/a · Santa Anna National Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-03-31 · 84 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-03-31 · 4,536 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-03-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-03-31 · 91 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-03-31 · 6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-03-31 · 9.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2025-03-31 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2025-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2025-03-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2025-03-31 · 14.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2025-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2025-03-31 · 40.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2025-03-31 · 9.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2025-03-31 · 18.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2025-03-31 · 33.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2025-03-31 · 4.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 40.8%; contribution to the score · 2025-03-31 · +1.665 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 52.9%; contribution to the score · 2025-03-31 · +0.354 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F73 · Driver up #3: deposit growth over the past four quarters, value 33.2%; contribution to the score · 2025-03-31 · +0.274 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F74 · Driver up #4: commercial real estate loans as a share of loans, value 6.0%; contribution to the score · 2025-03-31 · +0.174 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F75 · Driver up #5: loans as a share of deposits, value 56.9%; contribution to the score · 2025-03-31 · +0.119 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.7%; contribution to the score · 2025-03-31 · -1.296 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2025-03-31 · -0.914 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 27.6%; contribution to the score · 2025-03-31 · -0.439 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2025-03-31 · -0.304 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: return on assets (profit as a share of assets), value 1.7%; contribution to the score · 2025-03-31 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F81 · Failure date · 2025-06-27 · 2025-06-27 · data/raw/failures: FAILDATE
- F82 · Flagged at Q1 2025, after the 2016-2024 test period (not counted in the reported results) · 2025-03-31 · 2025-03-31 · data/analyst/scores.parquet: flagged
- F83 · Last quarter the bank reported · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
