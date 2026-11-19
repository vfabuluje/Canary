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
written_at: "2026-11-18T19:56:58"
writer_model: "claude-opus-5-5"
checked: true
---

# Prime Alliance Bank (cert 57920)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

Prime Alliance Bank, a UT bank with $1.1 billion in total assets, ranked 88 out of 4,411 banks nationally as of 2025-12-31, which puts it in the 98.0th percentile of Canary's risk ranking. That placed it on Canary's watchlist, which covers roughly the top 2% of banks by score. The ranking was pushed up mainly by its reliance on brokered deposits (money gathered through middlemen), its unusually low operating costs relative to revenue, and its high interest costs, while strong profits and its capital level pulled the score down.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than at a typical bank: equity was 9.5% of assets against a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 9.9% against 10.8%. Its Tier 1 risk-based capital ratio was 11.4% and its total risk-based capital ratio 12.7%, both well below the medians of 14.4% and 15.6%.

Credit quality was weaker than the norm: loans 90+ days past due or not accruing interest were 2.0% of loans, against a median of 0.4%, and nonaccrual assets plus foreclosed property were 1.6% of assets, against 0.3%. Net loan write-offs ran at 0.7% of loans versus a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 1.1% of assets versus 0.1%. The bank did hold large loan-loss reserves of 3.4% of loans, well above the 1.2% median, and its Texas ratio (troubled assets against capital plus reserves) was 12.8% against a median of 2.7%.

On funding, brokered deposits made up 16.0% of deposits while the median bank had 0.0%, and interest expense was 3.3% of assets against a median of 1.7%. Cash was only 0.6% of assets against a median of 6.5%, core deposits (stable, everyday deposits) were 65.5% of assets against 75.4%, and deposits grew 26.6% over the past four quarters against a median of 4.1%. Unrealized losses on bonds available for sale were 5.3% of equity, close to the national median of 5.2%, while uninsured deposits were a lower-than-typical 12.6% of deposits against 24.5%.

## Understanding the score

As of 2025-12-31, Prime Alliance Bank ranked 88 out of 4,411 banks, placing it in the 98.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 89 banks that quarter, a list that covers about the top 2% of banks.

The five factors that pushed the score up most were brokered deposits at 16.0% of deposits (+0.449) and the efficiency ratio, operating costs as a share of revenue, at 21.0% (+0.449). Next came interest expense at 3.3% of assets (+0.420), deposit growth over the past four quarters of 26.6% (+0.218), and losses on bonds available for sale at 5.3% of equity (+0.202).

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 11.4% (-0.811), return on equity at 27.1% (-0.654), and return on assets at 2.4% (-0.569). The Texas ratio at 12.8% (-0.511) and total assets of $1.1 billion (-0.290) also lowered the score.

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

## How its ratios moved

Each ratio was compared with its own history over the prior 12 quarters, or for year-to-date ratios with the same quarter in the prior 3 years. Of 30 ratios checked, 9 sat outside their own prior range, and the 6 furthest outside are shown in the table. The model rated the bank about the same as a year earlier: it was in the 97.9th percentile at 2024-12-31 and the 98.0th percentile at 2025-12-31.

Brokered deposits were 16.0% of deposits, below their prior range of 17.6% to 24.1% after a -4.3 pp move over one quarter, yet they pushed the score up with a contribution of +0.449. The efficiency ratio was 21.0%, below its prior range of 22.7% to 30.0%, and it pushed the score up with a contribution of +0.449. Commercial real estate loans were 4.3% of loans, below their prior range of 6.0% to 8.6% after a -3.9 pp change over four quarters, and they pushed the score up with a contribution of +0.175.

Return on equity was 27.1%, above its prior range of 15.2% to 21.7%, but this pushed the score down with a contribution of -0.654. Return on assets was 2.4%, above its prior range of 1.5% to 2.2%, but this also pushed the score down with a contribution of -0.569. Net loan write-offs were 0.7% of loans, below their prior range of 0.8% to 1.4%, yet this had little effect on the score, with a contribution of +0.014.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 27.1% | 15.2% to 21.7% | same quarter, prior 3 years | n/a | +5.4 pp | -0.654 | pushed the score down |
| commercial real estate loans as a share of loans | 4.3% | 6.0% to 8.6% | prior 12 quarters | -2.0 pp | -3.9 pp | +0.175 | pushed the score up |
| brokered deposits as a share of deposits | 16.0% | 17.6% to 24.1% | prior 12 quarters | -4.3 pp | -2.3 pp | +0.449 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 21.0% | 22.7% to 30.0% | same quarter, prior 3 years | n/a | -1.7 pp | +0.449 | pushed the score up |
| return on assets (profit as a share of assets) | 2.4% | 1.5% to 2.2% | same quarter, prior 3 years | n/a | +0.3 pp | -0.569 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 0.8% to 1.4% | same quarter, prior 3 years | n/a | -0.7 pp | +0.014 | little effect on the score |

9 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it was flagged, and what happened

In hindsight, this flag looks like a false alarm. The bank was flagged because of its heavy use of brokered deposits, high interest costs and fast deposit growth, even though it was very profitable. In the following quarters its rank eased to 177 at 2026-03-31 and 249 at 2026-06-30, and it was not flagged in either quarter.

## What happened next

Looking back with hindsight, Prime Alliance Bank ranked 177 and was not flagged as of March 31, 2026. By June 30, 2026 its rank had moved to 249, again not flagged. The bank was still filing reports in the latest quarter shown, 2026-06-30.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 177 | 4,353 |  |
| 2026-06-30 | 249 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Prime Alliance Bank · data/features/fct_bank_features.parquet: institution_name
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
- F51 · Bank: uninsured deposits as a share of deposits · 2025-12-31 · 12.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2025-12-31 · 24.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 16.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 65.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2025-12-31 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2025-12-31 · $1.1 billion · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2025-12-31 · 26.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2025-12-31 · 4.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
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
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · 27.1% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · -0.654 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2025-12-31 · 4.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F98 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 8.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F101 · Trend: commercial real estate loans as a share of loans, change over four quarters, in percentage points · 2025-12-31 · -3.9 pp · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F102 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · +0.175 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F103 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F104 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2025-12-31 · 16.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F105 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 17.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F106 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F107 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2025-12-31 · -4.3 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F109 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F110 · Trend: brokered deposits as a share of deposits, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-12-31 · 21.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F112 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 22.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 30.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F116 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F117 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F118 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F121 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-12-31 · -0.569 · data/analyst/scores.parquet: feature return_on_assets contribution
- F122 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2025-12-31 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · +0.014 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: ratios outside their own prior range · 2025-12-31 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 97.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
