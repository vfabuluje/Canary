---
cert: 11317
name: "Iuka State Bank"
as_of: 2026-06-30
rank: 14
n_banks: 4313
percentile: 99.69858567122652
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:55:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Iuka State Bank (cert 11317)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Iuka State Bank, a small Illinois bank, ranked 14 out of 4,313 FDIC-insured banks on Canary's risk score, which places it in the 99.7th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the top 2% of banks by score. The main reasons are a large pile of troubled loans compared with its capital, a high share of loans that have stopped paying, losses on its bond holdings and heavy reliance on brokered deposits, meaning money placed through middlemen rather than gathered from local customers.

## Warning signs in the data

Capital, the cushion that absorbs losses, is somewhat thin: equity was 9.6% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.3% against a median of 11.0%. Credit quality is the biggest concern: loans 90 or more days past due or no longer accruing interest were 8.0% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 6.9% of assets versus a median of 0.3%, and the Texas ratio, which weighs troubled assets against capital plus reserves, was 57.1% versus a median of 2.9%.

On funding, brokered deposits made up 20.2% of deposits, while the national median was 0.0%. Federal Home Loan Bank borrowings, a type of wholesale loan to banks, were 4.6% of assets against a median of 0.2%, and core deposits, the stable everyday customer money, were 63.6% of assets, below the median of 75.5%. Unrealized losses on bonds available for sale equaled 11.0% of equity, well above the median of 5.6%.

## Understanding the score

Iuka State Bank ranked 14 of 4,313 banks on 2026-06-30, the 99.7th percentile on a scale of 0 to 100 where higher means riskier. It is flagged on the watchlist, the top 2% of banks by score, which held 87 banks that quarter.

The five features pushing the score up most were the Texas ratio at 57.1% (+0.900), loans 90+ days past due or not accruing at 8.0% (+0.844), losses on bonds available for sale at 11.0% of equity (+0.589), brokered deposits at 20.2% of deposits (+0.349), and the provision for loan losses, money set aside for expected bad loans, at 1.2% of assets (+0.145).

The five features pulling the score down most were the Tier 1 risk-based capital ratio, a measure of core capital against riskier assets (-0.733), return on equity at 0.8% (-0.369), construction loans at 1.7% of loans (-0.310), the leverage ratio at 10.3% (-0.272), and volatile funding at 11.8% of assets (-0.178).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 338 | 4,589 |  |
| 2024-12-31 | 212 | 4,560 |  |
| 2025-03-31 | 37 | 4,536 | ▲ watchlist |
| 2025-06-30 | 34 | 4,494 | ▲ watchlist |
| 2025-09-30 | 382 | 4,452 |  |
| 2025-12-31 | 19 | 4,411 | ▲ watchlist |
| 2026-03-31 | 16 | 4,353 | ▲ watchlist |
| 2026-06-30 | 14 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, mostly the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios compared, 14 sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 14 of 4,313, at the 99.7th percentile, against the 99.3% percentile a year earlier, so the model rated it about the same as a year earlier.

Brokered deposits reached 20.2% of deposits, above a prior range of 0.0% to 15.3%, up +4.9 pp in one quarter and +17.3 pp over four quarters. At 20.2% of deposits, brokered deposits had a contribution of +0.349 log-odds units, which pushed the score up. The provision for loan losses was 1.2% of assets, above its prior range of 0.4% to 0.8%, a change of +0.8 pp over four quarters, and its contribution of +0.145 log-odds units pushed the score up.

Return on equity fell to 0.8%, below its prior range of 7.9% to 12.1%, a change of -11.3 pp over four quarters, yet its contribution of -0.369 log-odds units pushed the score down, the opposite of what the drop might suggest. Return on assets fell to 0.1%, below its prior range of 0.7% to 1.1%, a change of -1.1 pp, yet its contribution of -0.163 log-odds units pushed the score down. The efficiency ratio rose to 74.4%, above its prior range of 59.0% to 65.6%, up +8.8 pp, yet its contribution of -0.052 log-odds units pushed the score down. Net loan write-offs rose to 1.8% of loans, above a prior range of 0.0% to 0.4%, up +1.4 pp, but with a contribution of -0.001 log-odds units they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 0.8% | 7.9% to 12.1% | same quarter, prior 3 years | n/a | -11.3 pp | -0.369 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.8% | 0.0% to 0.4% | same quarter, prior 3 years | n/a | +1.4 pp | -0.001 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 74.4% | 59.0% to 65.6% | same quarter, prior 3 years | n/a | +8.8 pp | -0.052 | pushed the score down |
| return on assets (profit as a share of assets) | 0.1% | 0.7% to 1.1% | same quarter, prior 3 years | n/a | -1.1 pp | -0.163 | pushed the score down |
| annualized provision for loan losses as a share of assets | 1.2% | 0.4% to 0.8% | same quarter, prior 3 years | n/a | +0.8 pp | +0.145 | pushed the score up |
| brokered deposits as a share of deposits | 20.2% | 0.0% to 15.3% | prior 12 quarters | +4.9 pp | +17.3 pp | +0.349 | pushed the score up |

14 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank remains an open watchlist case: the fact sheet contains no data from after the as-of quarter, so there is no later result to report. Its place on the watchlist rests on the as-of figures described above, chiefly heavy troubled loans relative to capital, bond losses and a rising reliance on brokered deposits.

## What happened next

In hindsight, no later ranks, flags or reporting status are available in our data for this bank yet. Whether it stays on the watchlist, moves off it, or stops reporting will only be known once newer quarterly filings arrive.

## Sources

- F1 · Bank name · n/a · Iuka State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 14 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.1% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 63.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 8.0%; contribution to the score · 2026-06-30 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: losses on bonds available for sale, as a share of equity, value 11.0%; contribution to the score · 2026-06-30 · +0.589 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F74 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.349 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F75 · Driver up #5: annualized provision for loan losses as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.145 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 0.8%; contribution to the score · 2026-06-30 · -0.369 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 1.7%; contribution to the score · 2026-06-30 · -0.310 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: volatile funding as a share of assets, value 11.8%; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F81 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_equity
- F82 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.9% · data/features/fct_bank_features.parquet: return_on_equity
- F83 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 12.1% · data/features/fct_bank_features.parquet: return_on_equity
- F84 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -11.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F85 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.369 · data/analyst/scores.parquet: feature return_on_equity contribution
- F86 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F87 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F88 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F90 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +1.4 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 74.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 59.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · +8.8 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.052 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F100 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2026-06-30 · -1.1 pp · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature return_on_assets contribution
- F104 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F106 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F108 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +0.8 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.145 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F110 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F111 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F112 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F113 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 15.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F114 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +4.9 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +17.3 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.349 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F117 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F118 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F119 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F120 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F121 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F122 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F123 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F124 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
