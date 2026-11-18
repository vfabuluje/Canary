---
cert: 420
name: "Bank Of Vici"
as_of: 2026-06-30
rank: 19
n_banks: 4313
percentile: 99.58265708323673
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:54"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of Vici (cert 420)

*Outcome not yet known.*

## Summary

Bank Of Vici, a small Oklahoma bank with certificate number 420, ranked 19 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.6th percentile. That put it on the watchlist, which covers the riskiest 2% of banks. The main concerns were large paper losses on its bond holdings, a high share of loans that borrowers had stopped paying, and a loss-making quarter.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin by one measure: equity was 7.1% of assets, against a national median of 10.6%. Its leverage ratio (core capital as a share of average assets) was 10.2%, a little below the median of 11.0%. Unrealized losses on bonds available for sale (bonds the bank could sell at any time) equaled 56.7% of equity, far above the median of 5.6%.

Credit quality was weak: loans 90 or more days late or no longer earning interest were 12.3% of loans, versus a median of 0.5%. The Texas ratio, which compares troubled assets with the bank's capital plus reserves, stood at 69.0% against a median of 2.9%. The bank set aside loan-loss reserves of 3.2% of loans, well above the median of 1.2%, and it lost money, with a return on assets of -0.9% versus a median of 1.2%. Operating costs ran at 118.5% of revenue, compared with a median of 62.1%.

On funding, the bank was shrinking: assets fell -11.7% and deposits fell -13.5% over the past four quarters, while the medians grew 4.5% and 4.2%. Volatile funding, money that can leave quickly, was 15.7% of assets against a median of 9.0%, though uninsured deposits were a lower-than-typical 15.7% of deposits versus a median of 24.8%.

## Understanding the score

As of 2026-06-30, Bank Of Vici ranked 19 of 4,313 banks, in the 99.6th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, one of 87 banks that quarter in the riskiest 2%.

The five factors pushing the score up most were bond losses at 56.7% of equity, seriously late or non-paying loans at 12.3% of loans, and the Texas ratio at 69.0%. Smaller upward pushes came from asset growth over the past four quarters of -11.7% and loans equal to 50.3% of deposits.

The five factors pulling the score down most were the Tier 1 risk-based capital ratio (core capital measured against riskier assets), nonaccrual assets and foreclosed property at 0.9% of assets, and the efficiency ratio at 118.5%. The leverage ratio at 10.2% and return on equity at -13.2% also pulled the score down.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 21 | 4,589 | ▲ watchlist |
| 2024-12-31 | 18 | 4,560 | ▲ watchlist |
| 2025-03-31 | 11 | 4,536 | ▲ watchlist |
| 2025-06-30 | 9 | 4,494 | ▲ watchlist |
| 2025-09-30 | 25 | 4,452 | ▲ watchlist |
| 2025-12-31 | 34 | 4,411 | ▲ watchlist |
| 2026-03-31 | 197 | 4,353 |  |
| 2026-06-30 | 19 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this fact sheet contains no data from after the as-of quarter, so there is no later result to explain. The bank's status is that of a bank that remains on the watchlist with no recorded outcome yet. Its watchlist place rests on the warning signs described above, not on any later event.

## What happened next

Looking back, the fact sheet holds no later ranks, flags or filings for this bank. Whether it keeps reporting, leaves the watchlist, or stops reporting cannot be judged from this data yet.

## Sources

- F1 · Bank name · n/a · Bank Of Vici · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 420 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 19 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 118.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 56.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: asset growth over the past four quarters · 2026-06-30 · -11.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F68 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -13.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 56.7%; contribution to the score · 2026-06-30 · +0.920 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 12.3%; contribution to the score · 2026-06-30 · +0.917 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 69.0%; contribution to the score · 2026-06-30 · +0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F74 · Driver up #4: asset growth over the past four quarters, value -11.7%; contribution to the score · 2026-06-30 · +0.125 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F75 · Driver up #5: loans as a share of deposits, value 50.3%; contribution to the score · 2026-06-30 · +0.122 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.744 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2026-06-30 · -0.385 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F78 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 118.5%; contribution to the score · 2026-06-30 · -0.282 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: return on equity (profit as a share of equity), value -13.2%; contribution to the score · 2026-06-30 · -0.237 · data/analyst/scores.parquet: feature return_on_equity contribution
