---
cert: 4134
name: "First Nb Of Lindsay"
as_of: 2024-09-30
rank: 9
n_banks: 4589
percentile: 99.82567008062759
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2024-10-18
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of Lindsay (cert 4134)

*Hindsight: failed 2024-10-18. Canary flagged it 1 quarter ahead.*

## Summary

First Nb Of Lindsay, an Oklahoma bank (certificate 4134), ranked 9 out of 4,589 FDIC-insured banks on Canary's risk score for the quarter ending 2024-09-30. That places it in the 99.8th percentile, where higher means riskier, and it was on Canary's watchlist that quarter. The main pressures in the data were very high troubled loans compared with the bank's capital, many overdue loans, and operating losses, while its cash and deposit base looked comparatively solid.

## Warning signs in the data

Credit quality, meaning how well borrowers are repaying, stands out most: loans 90+ days past due or not accruing interest were 10.6% of loans, against a national median of 0.4%. Loans 30-89 days past due were 10.4% of assets, far above the 0.2% median. The Texas ratio, which compares troubled assets with the capital and reserves available to absorb them, was 133.7% against a median of 2.2%. Annualized loan write-offs (loans the bank gave up on, net of recoveries) were 20.6% of loans versus a 0.0% median, and loan-loss reserves, the cushion set aside for bad loans, showed an unusual negative reading of -11.2% against a 1.2% median.

On capital, the bank's own cushion against losses, equity was 11.1% of assets, a little above the 10.0% median, while the leverage ratio (core capital as a share of average assets) was 10.0%, a little below the 10.7% median. Profitability was weak: return on assets was -0.7% against a median of 0.9%, and the efficiency ratio, operating costs as a share of revenue, was 126.6% versus 67.8%, meaning costs exceeded revenue.

Liquidity and funding looked stronger than typical: cash was 21.4% of assets versus a 6.2% median, and core deposits, the stable everyday deposits, were 83.6% of assets versus 75.0%. Brokered deposits, money placed through middlemen, were 0.0%, matching the median, and uninsured deposits showed an unusual reading of -1.6% against a 23.6% median. Losses on bonds available for sale were small at 0.1% of equity, well below the 8.5% median, and losses on bonds held to maturity were 0.0%.

## Understanding the score

For the quarter ending 2024-09-30, the bank ranked 9 of 4,589 banks, putting it in the 99.8th percentile on a 0 to 100 scale where higher means riskier. Canary's watchlist covers the riskiest 2% of banks, 92 banks that quarter, and this bank was flagged.

The five factors pushing the score up most were the Texas ratio at 133.7% (contribution +1.563), loans 90+ days past due or not accruing at 10.6% (+1.261), and loans 30-89 days past due at 10.4% (+0.296). Smaller upward pushes came from losses on bonds available for sale at 0.1% (+0.104) and deposit growth over the past four quarters at 17.8% (+0.097).

The five factors pulling the score down most were the Tier 1 risk-based capital ratio, a capital measure whose value is not shown here (contribution -0.670), return on equity at -6.9% (-0.526), and construction loans at 3.9% of loans (-0.461). Nonaccrual assets and foreclosed property at 0.9% of assets (-0.254) and loan-loss reserves at -11.2% of loans (-0.251) also lowered the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-12-31 | 2,776 | 4,773 |  |
| 2023-03-31 | 1,256 | 4,740 |  |
| 2023-06-30 | 1,082 | 4,714 |  |
| 2023-09-30 | 2,298 | 4,686 |  |
| 2023-12-31 | 2,335 | 4,658 |  |
| 2024-03-31 | 799 | 4,640 |  |
| 2024-06-30 | 573 | 4,610 |  |
| 2024-09-30 | 9 | 4,589 | ▲ watchlist (first flag) |

## How early Canary caught it

In hindsight, Canary first flagged this bank in the quarter ending 2024-09-30, and the bank failed on October 18, 2024. That gave a lead time of 1 quarter between the first flag and the failure, so the warning came shortly before the event.

## What happened next

Looking back, the bank failed on 2024-10-18, only weeks after the as-of quarter. Its last reported quarter was 2024-09-30, so there are no later ranks or flags for it in Canary's data.

## Sources

- F1 · Bank name · n/a · First Nb Of Lindsay · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 4134 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2024-09-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-09-30 · 4,589 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-09-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-09-30 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-09-30 · 11.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 10.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2024-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2024-09-30 · -1.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2024-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2024-09-30 · 83.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2024-09-30 · 75.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2024-09-30 · 21.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2024-09-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2024-09-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2024-09-30 · 8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 133.7%; contribution to the score · 2024-09-30 · +1.563 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 10.6%; contribution to the score · 2024-09-30 · +1.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: loans 30-89 days past due, as a share of assets, value 10.4%; contribution to the score · 2024-09-30 · +0.296 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F74 · Driver up #4: losses on bonds available for sale, as a share of equity, value 0.1%; contribution to the score · 2024-09-30 · +0.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 17.8%; contribution to the score · 2024-09-30 · +0.097 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2024-09-30 · -0.670 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value -6.9%; contribution to the score · 2024-09-30 · -0.526 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 3.9%; contribution to the score · 2024-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2024-09-30 · -0.254 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value -11.2%; contribution to the score · 2024-09-30 · -0.251 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Failure date · 2024-10-18 · 2024-10-18 · data/raw/failures: FAILDATE
- F82 · First flag quarter (Phase 3 lead-time rule) · 2024-09-30 · 2024-09-30 · data/analyst/scores.parquet: flagged
- F83 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F84 · Last quarter the bank reported · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
