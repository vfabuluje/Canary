---
cert: 57488
name: "Metropolitan Capital B&T"
as_of: 2025-12-31
rank: 2
n_banks: 4411
percentile: 99.97732940376332
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-01-30
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:22"
writer_model: "claude-opus-5-5"
checked: true
---

# Metropolitan Capital B&T (cert 57488)

*Hindsight: failed 2026-01-30. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2025-12-31, Metropolitan Capital B&T, an Illinois bank, ranked 2 out of 4,411 banks nationally on Canary's risk score, which places it in the 100.0th percentile. That put it on Canary's watchlist for the quarter. Its equity, meaning the owners' cushion against losses, was -0.8% of assets, against a national median of 10.4%. Heavy loan losses and deep operating losses also stand out in the data.

## Warning signs in the data

Capital, the bank's buffer to absorb losses, was far below typical levels: equity was -0.8% of assets versus a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 1.8% versus 10.8%. Its Tier 1 risk-based capital ratio, which measures core capital against riskier assets, was 3.0% against a median of 14.4%, and its total risk-based capital ratio was 4.3% against 15.6%.

Credit quality was weak: loans 90 or more days past due or no longer earning interest made up 2.8% of loans, well above the national median of 0.4%, and annualized loan write-offs, net of recoveries, were 12.4% of loans versus a median of 0.0%. The Texas ratio, which compares troubled assets with capital plus reserves, was 152.5% against a median of 2.7%. Profitability was deeply negative, with return on assets of -6.9% versus a median of 1.1% and an efficiency ratio (operating costs as a share of revenue) of 123.3% versus 63.8%.

On funding, brokered deposits (money placed through intermediaries, often seen as less stable) were 22.0% of deposits versus a median of 0.0%, and Federal Home Loan Bank borrowings were 14.0% of assets versus 0.2%. Deposits shrank by -7.3% over the past four quarters while the national median grew by 4.1%, though the bank held cash equal to 16.7% of assets, above the median of 6.5%. Losses on bonds available for sale, measured against equity, showed an unusual reading of -684.7%, compared with a national median of 5.2%.

## Understanding the score

At 2025-12-31 the bank ranked 2 of 4,411 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier, with a model score of 0.9774. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 89 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 3.0% (contribution +1.701), return on equity at -672.4% (+1.537), the Texas ratio at 152.5% (+1.021), the total risk-based capital ratio at 4.3% (+0.524), and the leverage ratio at 1.8% (+0.364).

The five factors pulling the score down most were nonaccrual assets and foreclosed property at 2.2% of assets (contribution -0.489), net interest margin, the spread earned on lending and investing, at 4.9% (-0.426), losses on bonds available for sale at -684.7% of equity (-0.368), loans 90+ days past due or not accruing at 2.8% of loans (-0.262), and construction loans at 4.7% of loans (-0.227).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 95 | 4,640 |  |
| 2024-06-30 | 38 | 4,610 | ▲ watchlist |
| 2024-09-30 | 40 | 4,589 | ▲ watchlist |
| 2024-12-31 | 2 | 4,560 | ▲ watchlist |
| 2025-03-31 | 5 | 4,536 | ▲ watchlist (first flag) |
| 2025-06-30 | 4 | 4,494 | ▲ watchlist |
| 2025-09-30 | 2 | 4,452 | ▲ watchlist |
| 2025-12-31 | 2 | 4,411 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged this bank in Q1 2025, and the bank failed on January 30, 2026, giving a lead time of 4 quarters before failure. At that first flag, the top factors raising the score were return on equity at -72.9% (+1.052), the Texas ratio at 138.8% (+0.874), and the Tier 1 risk-based capital ratio at 6.3% (+0.666). Losses on bonds available for sale at 388.4% of equity (+0.566) and loans 90+ days past due or not accruing at 8.8% of loans (+0.454) rounded out the top five.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the bank failed on 2026-01-30, about a month after the as-of quarter. The last quarter it reported data was 2025-12-31, so no later ranks or flags are available in our data.

## Sources

- F1 · Bank name · n/a · Metropolitan Capital B&T · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2025-12-31 · 0.9774 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2025-12-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · -0.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 3.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 4.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 2.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 152.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2025-12-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2025-12-31 · 123.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2025-12-31 · 63.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 22.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 14.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2025-12-31 · 16.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2025-12-31 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · -684.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2025-12-31 · -7.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2025-12-31 · 4.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.0%; contribution to the score · 2025-12-31 · +1.701 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -672.4%; contribution to the score · 2025-12-31 · +1.537 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 152.5%; contribution to the score · 2025-12-31 · +1.021 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 4.3%; contribution to the score · 2025-12-31 · +0.524 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 1.8%; contribution to the score · 2025-12-31 · +0.364 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: nonaccrual assets and foreclosed property, as a share of assets, value 2.2%; contribution to the score · 2025-12-31 · -0.489 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F81 · Driver down #2: net interest margin (the spread earned on lending and investing), value 4.9%; contribution to the score · 2025-12-31 · -0.426 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -684.7%; contribution to the score · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 2.8%; contribution to the score · 2025-12-31 · -0.262 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: construction loans as a share of loans, value 4.7%; contribution to the score · 2025-12-31 · -0.227 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2026-01-30 · 2026-01-30 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-03-31 · 2025-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-03-31: return on equity (profit as a share of equity), value -72.9%; contribution to the score · 2025-03-31 · +1.052 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-03-31: the Texas ratio (troubled assets against capital plus reserves), value 138.8%; contribution to the score · 2025-03-31 · +0.874 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2025-03-31: the Tier 1 risk-based capital ratio, value 6.3%; contribution to the score · 2025-03-31 · +0.666 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2025-03-31: losses on bonds available for sale, as a share of equity, value 388.4%; contribution to the score · 2025-03-31 · +0.566 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F92 · Driver up #5 at 2025-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2025-03-31 · +0.454 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
