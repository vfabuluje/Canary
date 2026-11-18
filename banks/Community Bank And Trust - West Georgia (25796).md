---
cert: 25796
name: "Community Bank And Trust - West Georgia"
as_of: 2026-03-31
rank: 2
n_banks: 4353
percentile: 99.97702733746841
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-05-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:05"
writer_model: "claude-opus-5-5"
checked: true
---

# Community Bank And Trust - West Georgia (cert 25796)

*Hindsight: failed 2026-05-01. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2026-03-31, Community Bank And Trust - West Georgia, a Georgia bank, ranked 2 out of 4,353 banks nationally on Canary's risk score, placing it at the 100.0th percentile, where higher means riskier. It was on Canary's watchlist, which covers roughly the riskiest 2% of banks. Its capital cushion, meaning the owners' money that absorbs losses, was very thin, with equity at 1.3% of assets against a national median of 10.4%. Its loan problems were severe: 17.3% of its loans were seriously overdue or no longer earning interest, compared with a national median of 0.5%.

## Warning signs in the data

Capital was far below normal levels. The leverage ratio, which measures core capital against average assets, was 0.2% versus a national median of 10.9%, and the Tier 1 risk-based capital ratio, a similar measure weighted by how risky the assets are, was 0.2% versus 14.5%. The total risk-based capital ratio was 1.5%, well under the national median of 15.7%.

Credit quality, meaning how well borrowers are repaying, was very weak. Nonaccrual assets, which no longer earn interest, plus foreclosed property made up 9.2% of assets against a median of 0.3%, and loans 30-89 days late were 5.5% of assets against 0.3%. Annualized write-offs of bad loans were 6.3% of loans versus a median of 0.0%, and the Texas ratio, which compares troubled assets with capital plus reserves, stood at 280.0% versus 2.9%. The bank was losing money, with a return on assets of -6.9% compared with a median of 1.2%.

Funding looked steadier than the rest of the picture: cash was 16.2% of assets versus a median of 6.9%, core deposits, the stable everyday kind, were 91.3% of assets versus 75.8%, and uninsured deposits were only 3.6% of deposits versus 24.4%. Deposits grew 42.6% over the past four quarters, far faster than the median of 4.0%. The measure of losses on bonds available for sale, as a share of equity, was an unusual -177.9%, against a national median of 5.8%.

## Understanding the score

On 2026-03-31 the bank ranked 2 of 4,353 banks, at the 100.0th percentile on a scale of 0 to 100 where higher is riskier. It was flagged on the watchlist, one of 88 banks on it that quarter.

Five features pushed the score up the most: the Tier 1 risk-based capital ratio at 0.2%, return on equity (profit as a share of equity) at -191.5%, the Texas ratio at 280.0%, seriously overdue or non-earning loans at 17.3% of loans, and the total risk-based capital ratio at 1.5%.

Five features pulled the score down the most: losses on bonds available for sale at -177.9% of equity, asset growth over the past four quarters at 23.9%, construction loans at 8.1% of loans, total assets of $292.6 million, and the efficiency ratio (operating costs as a share of revenue) at 92.4%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 6 | 4,610 | ▲ watchlist |
| 2024-09-30 | 4 | 4,589 | ▲ watchlist |
| 2024-12-31 | 5 | 4,560 | ▲ watchlist |
| 2025-03-31 | 3 | 4,536 | ▲ watchlist |
| 2025-06-30 | 1 | 4,494 | ▲ watchlist (first flag) |
| 2025-09-30 | 15 | 4,452 | ▲ watchlist |
| 2025-12-31 | 16 | 4,411 | ▲ watchlist |
| 2026-03-31 | 2 | 4,353 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged this bank in the quarter ending 2025-06-30. That was 4 quarters before the bank failed on 2026-05-01, so the model caught it well ahead of time.

At that first flag, the biggest drivers were already the Texas ratio at 158.3%, the Tier 1 risk-based capital ratio at 5.6%, and seriously overdue or non-earning loans at 14.7% of loans. Those same pressures on capital and loan quality grew worse by the later as-of quarter.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

Looking back with hindsight, the bank failed on 2026-05-01. Its last reported quarter was 2026-03-31, so the as-of quarter in this memo was its final filing. Our data alone cannot tell a merger from a closure when a bank stops reporting, but here the recorded failure date shows how it ended.

## Sources

- F1 · Bank name · n/a · Community Bank And Trust - West Georgia · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 1.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 1.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 17.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 9.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 280.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 3.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 91.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 16.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · -177.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-03-31 · 42.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-03-31 · 4.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.2%; contribution to the score · 2026-03-31 · +1.741 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -191.5%; contribution to the score · 2026-03-31 · +1.318 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 280.0%; contribution to the score · 2026-03-31 · +1.050 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 17.3%; contribution to the score · 2026-03-31 · +0.770 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.5%; contribution to the score · 2026-03-31 · +0.510 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -177.9%; contribution to the score · 2026-03-31 · -0.273 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: asset growth over the past four quarters, value 23.9%; contribution to the score · 2026-03-31 · -0.219 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F82 · Driver down #3: construction loans as a share of loans, value 8.1%; contribution to the score · 2026-03-31 · -0.179 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $292.6 million; contribution to the score · 2026-03-31 · -0.160 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 92.4%; contribution to the score · 2026-03-31 · -0.129 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F85 · Failure date · 2026-05-01 · 2026-05-01 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-06-30 · 2025-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-06-30: the Texas ratio (troubled assets against capital plus reserves), value 158.3%; contribution to the score · 2025-06-30 · +1.113 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2025-06-30: the Tier 1 risk-based capital ratio, value 5.6%; contribution to the score · 2025-06-30 · +1.022 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F90 · Driver up #3 at 2025-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 14.7%; contribution to the score · 2025-06-30 · +0.948 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
