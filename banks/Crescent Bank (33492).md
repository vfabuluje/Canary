---
cert: 33492
name: "Crescent Bank"
as_of: 2024-12-31
rank: 59
n_banks: 4560
percentile: 98.7280701754386
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:58:09"
writer_model: "claude-opus-5-5"
checked: true
---

# Crescent Bank (cert 33492)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2024-12-31, Crescent Bank, a Louisiana bank, ranked 59 out of 4,560 FDIC-insured banks on Canary's risk score, placing it in the 98.7th percentile, where higher means riskier. That put it on the watchlist, the 2% of banks with the highest scores. Its loan problems stood far above national medians, with loans 30-89 days past due at 17.6% of assets and net loan write-offs at 11.4% of loans. Its risk-based capital ratios sat below the national medians, while it depended much less on uninsured deposits than the typical bank.

## Warning signs in the data

Capital, the cushion that absorbs losses, was mixed: equity was 9.1% of assets against a national median of 9.7%, and the Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 12.4% against a median of 14.3%. The leverage ratio (core capital as a share of average assets) was 10.8%, slightly above the median of 10.6%.

Credit quality was the weakest area: loans 90+ days past due or not accruing interest were 3.3% of loans against a median of 0.4%, and loans 30-89 days past due were 17.6% of assets against a median of 0.2%. Net write-offs (loans written off as uncollectable, minus recoveries) ran at an annualized 11.4% of loans against a median of 0.0%, and loan-loss reserves, money set aside for expected losses, were 11.2% of loans against a median of 1.2%. Profit was slightly negative, with return on assets at -0.2% against a median of 0.9%.

On funding, interest expense was 4.2% of assets against a median of 1.8%, and volatile funding, money that can leave quickly, was 18.3% of assets against a median of 8.8%. Deposit growth over the past four quarters was -19.5%, against a median of 3.9%, though uninsured deposits (balances above the federal insurance limit) were only 4.6% of deposits against a median of 24.1%. Losses on bonds available for sale (paper losses on bonds the bank could sell) were 10.0% of equity, close to the median of 11.2%.

## Understanding the score

Crescent Bank ranked 59 of 4,560 banks, the 98.7th percentile on a 0 to 100 scale where higher means riskier. It was flagged for the watchlist, which covers the top 2% of banks, or 92 banks that quarter.

Contributions below are in model units, where positive pushes the score up. The five factors that pushed the score up most were interest expense at 4.2% of assets (+0.688), losses on bonds available for sale at 10.0% of equity (+0.673), the provision for loan losses, an expense for expected bad loans, at 8.4% of assets (+0.562), the efficiency ratio, operating costs as a share of revenue, at 45.3% (+0.290), and commercial real estate loans at 1.9% of loans (+0.147). The five that pulled the score down most were the Tier 1 risk-based capital ratio at 12.4% (-1.220), deposit growth over the past four quarters at -19.5% (-0.403), the Texas ratio, troubled assets against capital plus reserves, at 15.7% (-0.402), return on equity at -2.8% (-0.363), and the leverage ratio at 10.8% (-0.261).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 6 | 4,740 | ▲ watchlist |
| 2023-06-30 | 11 | 4,714 | ▲ watchlist |
| 2023-09-30 | 21 | 4,686 | ▲ watchlist |
| 2023-12-31 | 55 | 4,658 | ▲ watchlist |
| 2024-03-31 | 64 | 4,640 | ▲ watchlist |
| 2024-06-30 | 59 | 4,610 | ▲ watchlist |
| 2024-09-30 | 44 | 4,589 | ▲ watchlist |
| 2024-12-31 | 59 | 4,560 | ▲ watchlist |

## How its ratios moved

The model rated the bank about the same as a year earlier: it sat in the 98.8th percentile at 2023-12-31 and the 98.7th percentile at 2024-12-31. Each ratio is compared with its own prior range, the prior 12 quarters for most ratios, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios compared, 8 were outside their prior range.

Annualized interest expense was 4.2% of assets, above its prior range of 1.2% to 3.1% and up +1.1 pp over four quarters, and it pushed the score up, contributing +0.688 model log-odds units. Loans 30-89 days past due were 17.6% of assets, above their prior range of 9.4% to 15.9% and up +1.7 pp in one quarter, and they pushed the score up, contributing +0.147 model log-odds units.

Net loan write-offs were 11.4% of loans, above their prior range of 3.5% to 8.8% and up +2.6 pp over four quarters, yet they had little effect on the score, at -0.023 model log-odds units. Loans 90+ days past due or not accruing were 3.3% of loans, just above their prior range of 2.0% to 3.2%, but had little effect on the score, at +0.017 model log-odds units. Brokered deposits were 3.6% of deposits, above their prior range of 0.9% to 3.3%, yet they pushed the score down, at -0.155 model log-odds units. Deposit growth was -19.5%, below its prior range of -14.7% to 51.3% and down -21.7 pp over four quarters, yet it pushed the score down, at -0.403 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 4.2% | 1.2% to 3.1% | same quarter, prior 3 years | n/a | +1.1 pp | +0.688 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 11.4% | 3.5% to 8.8% | same quarter, prior 3 years | n/a | +2.6 pp | -0.023 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 17.6% | 9.4% to 15.9% | prior 12 quarters | +1.7 pp | +2.8 pp | +0.147 | pushed the score up |
| brokered deposits as a share of deposits | 3.6% | 0.9% to 3.3% | prior 12 quarters | +0.3 pp | +0.7 pp | -0.155 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 3.3% | 2.0% to 3.2% | prior 12 quarters | +0.4 pp | +0.1 pp | +0.017 | little effect on the score |
| deposit growth over the past four quarters | -19.5% | -14.7% to 51.3% | prior 12 quarters | -4.8 pp | -21.7 pp | -0.403 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it was flagged, and what happened

In hindsight, this flag was a false alarm: the bank kept reporting and was not flagged again in any later quarter in our data. By 2025-03-31 it ranked 240, outside the watchlist, and it was still reporting at 2026-06-30, when it ranked 4,037. The flag rested mainly on high funding costs, bond losses and heavy loan-loss provisions, while strong risk-based capital pulled the score down; those pressures did not end in failure during the period our data covers.

## What happened next

With hindsight, the bank ranked 240 at 2025-03-31, 244 at 2025-06-30 and 299 at 2025-09-30, none of them flagged. It moved closer to the top of the list at 145 on 2025-12-31, still not flagged, then dropped to 3,355 at 2026-03-31 and 4,037 at 2026-06-30. The bank was still reporting as of 2026-06-30, the latest quarter in our data.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2025-03-31 | 240 | 4,536 |  |
| 2025-06-30 | 244 | 4,494 |  |
| 2025-09-30 | 299 | 4,452 |  |
| 2025-12-31 | 145 | 4,411 |  |
| 2026-03-31 | 3,355 | 4,353 |  |
| 2026-06-30 | 4,037 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Crescent Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-12-31 · 2024-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2024-12-31 · 59 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-12-31 · 4,560 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-12-31 · 98.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-12-31 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-12-31 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-12-31 · 9.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-12-31 · 12.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-12-31 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2024-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-12-31 · -0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2024-12-31 · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-12-31 · 4.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-12-31 · 24.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2024-12-31 · 18.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2024-12-31 · 8.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-12-31 · 10.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2024-12-31 · 3.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: annualized interest expense as a share of assets, value 4.2%; contribution to the score · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 10.0%; contribution to the score · 2024-12-31 · +0.673 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized provision for loan losses as a share of assets, value 8.4%; contribution to the score · 2024-12-31 · +0.562 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 45.3%; contribution to the score · 2024-12-31 · +0.290 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 1.9%; contribution to the score · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 12.4%; contribution to the score · 2024-12-31 · -1.220 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -19.5%; contribution to the score · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 15.7%; contribution to the score · 2024-12-31 · -0.402 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value -2.8%; contribution to the score · 2024-12-31 · -0.363 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 10.8%; contribution to the score · 2024-12-31 · -0.261 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F85 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 240 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 244 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 299 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 145 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 3,355 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 4,037 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F98 · Trend: annualized interest expense as a share of assets, change over four quarters, in percentage points · 2024-12-31 · +1.1 pp · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2024-12-31 · +2.6 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F105 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · -0.023 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F108 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F109 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 15.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F110 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2024-12-31 · +1.7 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F112 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F113 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F114 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2024-12-31 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F119 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2024-12-31 · -0.155 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F120 · Trend: brokered deposits as a share of deposits, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F121 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F122 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F126 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · +0.017 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F127 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F128 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F129 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -14.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 51.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F132 · Trend: deposit growth over the past four quarters, change over four quarters, in percentage points · 2024-12-31 · -21.7 pp · data/features/fct_bank_features.parquet: deposit_growth_4q
- F133 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F134 · Trend: deposit growth over the past four quarters, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: ratios outside their own prior range · 2024-12-31 · 8 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2024-12-31 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2023-12-31 · 98.8% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2024-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
