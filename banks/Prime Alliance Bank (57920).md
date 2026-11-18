---
cert: 57920
name: "Prime Alliance Bank"
as_of: 2025-12-31
rank: 88
n_banks: 4411
percentile: 98.02765812740874
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:55"
writer_model: "claude-opus-5-5"
checked: true
---

# Prime Alliance Bank (cert 57920)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

Prime Alliance Bank, a UT bank with certificate number 57920, ranked 88 out of 4,411 FDIC-insured banks on Canary's risk score as of 2025-12-31. That places it in the 98.0th percentile, where 100 is the riskiest end of a 0 to 100 scale, and it was flagged on Canary's watchlist. The bank was highly profitable but held thinner capital than the typical bank, carried more troubled loans, and leaned on brokered deposits, which are deposits gathered through middlemen rather than from the bank's own customers.

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, was below the national median on every measure: equity was 9.5% of assets against a median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 9.9% against 10.8%. The Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 11.4% against a median of 14.4%, and the total risk-based capital ratio was 12.7% against 15.6%.

Credit quality was weaker than typical: loans 90+ days past due or not accruing interest were 2.0% of loans against a median of 0.4%, and nonaccrual assets plus foreclosed property were 1.6% of assets against 0.3%. Net loan write-offs, meaning loans written off as lost minus recoveries, ran at 0.7% of loans against a median of 0.0%, and the provision for loan losses was 1.1% of assets against 0.1%. The bank did hold larger loan-loss reserves, at 3.4% of loans against a median of 1.2%, and its Texas ratio (troubled assets against capital plus reserves) was 12.8% against a median of 2.7%.

On funding, brokered deposits were 16.0% of deposits against a national median of 0.0%, core deposits (stable, everyday deposits) were 65.5% of assets against 75.4%, and cash was only 0.6% of assets against 6.5%. Interest expense was 3.3% of assets against a median of 1.7%, and assets grew 27.3% over the past four quarters against a median of 4.6%. Paper losses on bonds available for sale were 5.3% of equity, roughly in line with the national median of 5.2%.

## Understanding the score

As of 2025-12-31, Prime Alliance Bank ranked 88 out of 4,411 banks, which is the 98.0th percentile on a 0 to 100 scale where higher means riskier. Canary's watchlist covers the top 2% of banks, which was 89 banks that quarter, and this bank was flagged.

The five features that pushed the score up most were brokered deposits at 16.0% of deposits, a low efficiency ratio (operating costs as a share of revenue) of 21.0%, interest expense at 3.3% of assets, deposit growth of 26.6% over the past four quarters, and bond losses on available-for-sale securities at 5.3% of equity. Their contributions to the score were +0.449, +0.449, +0.420, +0.218 and +0.202 respectively.

The five features that pulled the score down most were the Tier 1 risk-based capital ratio at 11.4%, return on equity at 27.1%, return on assets at 2.4%, the Texas ratio at 12.8%, and total assets of $1.1 billion. Their contributions were -0.811, -0.654, -0.569, -0.511 and -0.290 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 31 | 4,640 | ▲ watchlist |
| 2024-06-30 | 204 | 4,610 |  |
| 2024-09-30 | 211 | 4,589 |  |
| 2024-12-31 | 96 | 4,560 |  |
| 2025-03-31 | 52 | 4,536 | ▲ watchlist |
| 2025-06-30 | 41 | 4,494 | ▲ watchlist |
| 2025-09-30 | 30 | 4,452 | ▲ watchlist |
| 2025-12-31 | 88 | 4,411 | ▲ watchlist |

## Why it was flagged, and what happened

In hindsight, this flag looks like a false alarm. The bank kept reporting after the as-of quarter and fell to rank 177 in Q1 2026, no longer on the watchlist. By 2026-06-30 it ranked 249 and was again not flagged, so its relative risk standing eased rather than worsened.

## What happened next

Looking back with hindsight, the bank continued to report data in later quarters. It ranked 177 as of March 31, 2026 and 249 as of June 30, 2026, and was not flagged in either quarter.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 177 | 4,353 |  |
| 2026-06-30 | 249 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Prime Alliance Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 57920 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-12-31 · 88 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 98.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 9.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 11.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2025-12-31 · 3.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2025-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 12.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 16.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 65.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2025-12-31 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2025-12-31 · 27.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2025-12-31 · 4.6% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 16.0%; contribution to the score · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 21.0%; contribution to the score · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2025-12-31 · +0.420 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: deposit growth over the past four quarters, value 26.6%; contribution to the score · 2025-12-31 · +0.218 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 5.3%; contribution to the score · 2025-12-31 · +0.202 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.4%; contribution to the score · 2025-12-31 · -0.811 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 27.1%; contribution to the score · 2025-12-31 · -0.654 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 2.4%; contribution to the score · 2025-12-31 · -0.569 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the Texas ratio (troubled assets against capital plus reserves), value 12.8%; contribution to the score · 2025-12-31 · -0.511 · data/analyst/scores.parquet: feature texas_ratio contribution
- F84 · Driver down #5: total assets, value $1.1 billion; contribution to the score · 2025-12-31 · -0.290 · data/analyst/scores.parquet: feature log_total_assets contribution
- F85 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 177 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 249 (not flagged) · data/analyst/scores.parquet: rank, flagged
