---
cert: 34995
name: "First Central Bank Mccook"
as_of: 2025-12-31
rank: 82
n_banks: 4411
percentile: 98.16368170482885
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:58:32"
writer_model: "claude-opus-5-5"
checked: true
---

# First Central Bank Mccook (cert 34995)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2025-12-31, First Central Bank Mccook ranked 82 out of 4,411 FDIC-insured banks on Canary's risk score, with a percentile of 98.2%, where higher means riskier. That put it on the watchlist, which holds the top 2% of banks by score. The main concern was loan quality: 6.4% of its loans were 90+ days past due or no longer accruing interest, against a national median of 0.4%. It also leaned on brokered deposits (money placed through middlemen), at 18.9% of deposits, while its capital ratios sat close to national norms.

## Warning signs in the data

Credit quality stood out most: loans 90+ days past due or not accruing interest were 6.4% of loans, far above the national median of 0.4%. Nonaccrual assets and foreclosed property (loans no longer paying, plus repossessed real estate) were 4.5% of assets, against a median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 37.6%, well above the median of 2.7%, and net loan write-offs ran at 1.3% of loans against a median of 0.0%. Its loan-loss reserves, money set aside for expected losses, were 1.8% of loans, above the median of 1.2%.

Capital, the cushion that absorbs losses, was close to typical levels: equity was 10.6% of assets versus a median of 10.4%, and the leverage ratio was 10.7% versus 10.8%. Its Tier 1 risk-based capital ratio was 13.7% and its total risk-based capital ratio 14.9%, both somewhat below the medians of 14.4% and 15.6%. Profitability was weaker than usual, with return on assets of 0.6% against a median of 1.1%.

On funding, brokered deposits were 18.9% of deposits, while the median bank had 0.0%, and core deposits, the stable everyday kind, were 59.6% of assets against a median of 75.4%. Borrowings from the Federal Home Loan Bank were 3.3% of assets versus a median of 0.2%, and interest expense was 2.4% of assets versus 1.7%. Uninsured deposits were lower than typical, at 12.4% against a median of 24.5%. On bonds, unrealized losses on bonds held to maturity were 2.9% of equity versus a median of 0.0%, while bonds available for sale showed -0.4% against a median of 5.2%.

## Understanding the score

The bank ranked 82 out of 4,411 banks as of 2025-12-31, with a percentile of 98.2% on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 89 banks that quarter.

The five factors pushing the score up were: loans 90+ days past due or not accruing interest at 6.4% (+0.867), brokered deposits at 18.9% of deposits (+0.677), interest expense at 2.4% of assets (+0.340), loans 30-89 days past due at 0.0% of assets (+0.163), and commercial real estate loans at 11.4% of loans (+0.097).

The five factors pulling the score down were: the Tier 1 risk-based capital ratio at 13.7% (-1.178), the total risk-based capital ratio at 14.9% (-0.402), return on equity at 5.5% (-0.384), return on assets at 0.6% (-0.368), and deposit growth over the past four quarters at -0.8% (-0.298).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 1,257 | 4,640 |  |
| 2024-06-30 | 654 | 4,610 |  |
| 2024-09-30 | 895 | 4,589 |  |
| 2024-12-31 | 25 | 4,560 | ▲ watchlist |
| 2025-03-31 | 49 | 4,536 | ▲ watchlist |
| 2025-06-30 | 43 | 4,494 | ▲ watchlist |
| 2025-09-30 | 261 | 4,452 |  |
| 2025-12-31 | 82 | 4,411 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked, 13 were outside their own prior range, and 6 are shown in the table. The model rated the bank safer than a year earlier: its percentile was 99.5% at 2024-12-31 and 98.2% at 2025-12-31.

Return on equity was 5.5%, above its prior range of -5.2% to 3.0% after rising +10.8 pp over four quarters, yet it pushed the score down with a contribution of -0.384. Return on assets was 0.6%, above its prior range of -0.6% to 0.3% after a +1.1 pp change over four quarters, and it pushed the score down with a contribution of -0.368. The Tier 1 risk-based capital ratio was 13.7%, above its range of 11.1% to 13.4% after gaining +2.6 pp over four quarters, and it pushed the score down with a contribution of -1.178. The total risk-based capital ratio was 14.9%, above its range of 12.3% to 14.6% after gaining +2.6 pp over four quarters, and it pushed the score down with a contribution of -0.402.

Brokered deposits were 18.9% of deposits, below their prior range of 21.8% to 32.8% after falling -7.5 pp over four quarters, but they still pushed the score up with a contribution of +0.677. Losses on bonds available for sale were -0.4% of equity, below their range of -0.1% to 1.0% after a -0.9 pp change over four quarters, and they pushed the score down with a contribution of -0.085.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 5.5% | -5.2% to 3.0% | same quarter, prior 3 years | n/a | +10.8 pp | -0.384 | pushed the score down |
| brokered deposits as a share of deposits | 18.9% | 21.8% to 32.8% | prior 12 quarters | -2.9 pp | -7.5 pp | +0.677 | pushed the score up |
| losses on bonds available for sale, as a share of equity | -0.4% | -0.1% to 1.0% | prior 12 quarters | -0.3 pp | -0.9 pp | -0.085 | pushed the score down |
| return on assets (profit as a share of assets) | 0.6% | -0.6% to 0.3% | same quarter, prior 3 years | n/a | +1.1 pp | -0.368 | pushed the score down |
| the Tier 1 risk-based capital ratio | 13.7% | 11.1% to 13.4% | prior 12 quarters | +1.2 pp | +2.6 pp | -1.178 | pushed the score down |
| the total risk-based capital ratio | 14.9% | 12.3% to 14.6% | prior 12 quarters | +1.2 pp | +2.6 pp | -0.402 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it was flagged, and what happened

In hindsight, this flag looks like a false alarm in the data we have. By 2026-03-31 the bank had moved to rank 271 and was no longer flagged, and by 2026-06-30 it ranked 534, still not flagged. The flag was driven mainly by high levels of seriously late loans and reliance on brokered deposits, but the bank's improving capital and profits appear to have carried more weight as later quarters came in.

## What happened next

Looking back with hindsight, the bank kept reporting after the as-of quarter and dropped off the watchlist. It ranked 271 at 2026-03-31 and 534 at 2026-06-30, not flagged in either quarter. Its rank moved steadily away from the riskiest group of banks over those quarters.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 271 | 4,353 |  |
| 2026-06-30 | 534 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · First Central Bank Mccook · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2025-12-31 · 82 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 6.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2025-12-31 · 1.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2025-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 37.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2025-12-31 · 24.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 59.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 2.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 6.4%; contribution to the score · 2025-12-31 · +0.867 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 18.9%; contribution to the score · 2025-12-31 · +0.677 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2025-12-31 · +0.340 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2025-12-31 · +0.163 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 11.4%; contribution to the score · 2025-12-31 · +0.097 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.7%; contribution to the score · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 14.9%; contribution to the score · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 5.5%; contribution to the score · 2025-12-31 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.6%; contribution to the score · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -0.8%; contribution to the score · 2025-12-31 · -0.298 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 271 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 534 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · 5.5% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -5.2% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2025-12-31 · +10.8 pp · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F92 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F94 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 21.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F95 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 32.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F97 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2025-12-31 · -7.5 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F98 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2025-12-31 · +0.677 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F99 · Trend: brokered deposits as a share of deposits, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F100 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F102 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, change over four quarters, in percentage points · 2025-12-31 · -0.9 pp · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F105 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2025-12-31 · -0.085 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2025-12-31 · +1.1 pp · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F114 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 11.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F115 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F117 · Trend: the Tier 1 risk-based capital ratio, change over four quarters, in percentage points · 2025-12-31 · +2.6 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F118 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F119 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F120 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2025-12-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F122 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F124 · Trend: the total risk-based capital ratio, change over four quarters, in percentage points · 2025-12-31 · +2.6 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F125 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: the total risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F127 · Trend: ratios outside their own prior range · 2025-12-31 · 13 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 99.5% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
