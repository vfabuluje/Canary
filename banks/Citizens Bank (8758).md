---
cert: 8758
name: "Citizens Bank"
as_of: 2023-09-30
rank: 1
n_banks: 4686
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2023-11-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:47:26"
writer_model: "claude-opus-5-5"
checked: true
---

# Citizens Bank (cert 8758)

*Hindsight: failed 2023-11-03. Canary flagged it 2 quarters ahead.*

## Summary

Citizens Bank, an Iowa bank, ranked 1 out of 4,686 banks nationally on Canary's risk score as of 2023-09-30, which puts it in the 100.0th percentile, the riskiest end of the scale. It was flagged on Canary's watchlist, which covers roughly the top 2% of banks by score. Its capital cushion had disappeared: equity (what the owners' stake is worth) stood at -4.5% of assets, against a national median of 9.1%. It was also losing money heavily, with a return on assets of -10.0% compared with a national median of 1.0%.

## Warning signs in the data

Capital, the money a bank has to absorb losses, was essentially gone as of 2023-09-30. Equity as a share of assets was -4.5%, against a national median of 9.1%. The leverage ratio (core capital as a share of average assets) was 0.0%, versus a median of 10.6%, and the Tier 1 risk-based capital ratio (core capital measured against riskier assets) was also 0.0%, versus 14.2%. The total risk-based capital ratio was 1.3%, far below the median of 15.4%.

Loan quality was poor: loans 90 or more days overdue or no longer paying interest were 9.6% of loans, against a median of 0.3%. Nonaccrual assets (loans no longer earning interest) plus foreclosed property were 5.9% of assets, versus 0.1%, and loans 30-89 days overdue were 1.5% of assets, versus 0.2%. Write-offs of bad loans, net of recoveries, ran at an annualized 15.1% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 9.8% of assets, also against 0.0%.

On funding, uninsured deposits (balances above the government insurance limit) were 34.5% of deposits, above the median of 23.6%, and volatile funding was 20.9% of assets, well above the median of 8.3%. Deposits shrank by -9.2% over the past four quarters, a steeper decline than the median of -0.6%, while cash was 2.6% of assets against a median of 5.4%. Losses on bonds available for sale read -105.6% of equity against a median of 19.9%, a figure distorted by the bank's negative equity rather than a sign of bond gains.

## Understanding the score

As of 2023-09-30, Citizens Bank ranked 1 of 4,686 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 94 banks that quarter, a list that holds about 2% of banks.

The five features that pushed the score up most were mostly about capital and profit. The Tier 1 risk-based capital ratio, at 0.0%, added +2.465, and return on equity (profit as a share of the owners' stake), at -596.8%, added +2.131. The total risk-based capital ratio at 1.3% added +0.728, the leverage ratio at 0.0% added +0.618, and equity as a share of assets at -4.5% added +0.390.

Five features pulled the score down. The Texas ratio (troubled assets against capital plus reserves), at -261.2%, subtracted -0.910, a negative reading that comes from the bank's negative capital. Securities at 38.2% of assets subtracted -0.312, losses on bonds available for sale at -105.6% of equity subtracted -0.293, interest expense at 1.1% of assets subtracted -0.236, and deposit growth of -9.2% subtracted -0.132.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-12-31 | 297 | 4,904 |  |
| 2022-03-31 | 20 | 4,861 | ▲ watchlist |
| 2022-06-30 | 586 | 4,838 |  |
| 2022-09-30 | 261 | 4,813 |  |
| 2022-12-31 | 515 | 4,773 |  |
| 2023-03-31 | 303 | 4,740 |  |
| 2023-06-30 | 33 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 1 | 4,686 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios compared, 17 were outside their own prior range, and the table shows the 6 furthest out. The bank ranked 1 of 4,686, and the model rated it riskier than a year earlier, when it sat in the 94.6th percentile.

Return on equity was -596.8%, against a prior range of 11.9% to 23.8%, a change of -620.6 pp, and it pushed the score up by +2.131 model log-odds units. Return on assets was -10.0%, against a prior range of 1.0% to 1.4%, and it pushed the score up by +0.116. The leverage ratio was 0.0%, against a prior range of 7.5% to 8.8%, after a drop of -8.3 pp in one quarter, and it pushed the score up by +0.618. The provision for loan losses was 9.8% of assets, against a prior range of 0.0% to 0.5%, and it pushed the score up by +0.200.

The efficiency ratio (operating costs as a share of revenue) jumped to 88.3%, well outside its prior range of 61.9% to 62.6%, yet it pushed the score down by -0.120. Net loan write-offs reached 15.1% of loans, far above the prior range of 0.3% to 2.2%, yet they had little effect on the score, at -0.026.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -596.8% | 11.9% to 23.8% | same quarter, prior 3 years | n/a | -620.6 pp | +2.131 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 88.3% | 61.9% to 62.6% | same quarter, prior 3 years | n/a | +25.7 pp | -0.120 | pushed the score down |
| return on assets (profit as a share of assets) | -10.0% | 1.0% to 1.4% | same quarter, prior 3 years | n/a | -11.2 pp | +0.116 | pushed the score up |
| annualized provision for loan losses as a share of assets | 9.8% | 0.0% to 0.5% | same quarter, prior 3 years | n/a | +9.7 pp | +0.200 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 15.1% | 0.3% to 2.2% | same quarter, prior 3 years | n/a | +12.9 pp | -0.026 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 0.0% | 7.5% to 8.8% | prior 12 quarters | -8.3 pp | -8.2 pp | +0.618 | pushed the score up |

17 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged Citizens Bank in the quarter ending 2023-06-30, and the bank failed on 2023-11-03, a lead time of 2 quarters. At that first flag, the top drivers pushing the score up were losses on bonds available for sale at 119.8% of equity, adding +1.104, and the Texas ratio at 143.5%, adding +1.045. Overdue and non-paying loans at 9.7% of loans added +0.295, while capital still looked adequate then, with a Tier 1 risk-based capital ratio of 10.4% pulling the score down by -0.829.

## What happened next

In hindsight, the last quarter Citizens Bank reported was 2023-09-30, the same quarter as this memo's data. The bank failed on November 3, 2023, so there are no later ranks or flags to report.

## Sources

- F1 · Bank name · n/a · Citizens Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-09-30 · 4,686 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-09-30 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-09-30 · -4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-09-30 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-09-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-09-30 · 1.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-09-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 9.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2023-09-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2023-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-09-30 · -10.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-09-30 · 34.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-09-30 · 20.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-09-30 · 8.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-09-30 · 2.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-09-30 · 5.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-09-30 · -105.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-09-30 · 19.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-09-30 · -9.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-09-30 · -0.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2023-09-30 · +2.465 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -596.8%; contribution to the score · 2023-09-30 · +2.131 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 1.3%; contribution to the score · 2023-09-30 · +0.728 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 0.0%; contribution to the score · 2023-09-30 · +0.618 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: equity as a share of assets, value -4.5%; contribution to the score · 2023-09-30 · +0.390 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value -261.2%; contribution to the score · 2023-09-30 · -0.910 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: securities as a share of assets, value 38.2%; contribution to the score · 2023-09-30 · -0.312 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -105.6%; contribution to the score · 2023-09-30 · -0.293 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2023-09-30 · -0.236 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -9.2%; contribution to the score · 2023-09-30 · -0.132 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Failure date · 2023-11-03 · 2023-11-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 119.8%; contribution to the score · 2023-06-30 · +1.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: the Texas ratio (troubled assets against capital plus reserves), value 143.5%; contribution to the score · 2023-06-30 · +1.045 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2023-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 9.7%; contribution to the score · 2023-06-30 · +0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F94 · Driver down #2 at 2023-06-30: the Tier 1 risk-based capital ratio, value 10.4%; contribution to the score · 2023-06-30 · -0.829 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-09-30 · -596.8% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 23.8% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2023-09-30 · -620.6 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-09-30 · +2.131 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2023-09-30 · 88.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 61.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 62.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2023-09-30 · -0.120 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2023-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2023-09-30 · -10.0% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F113 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F115 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2023-09-30 · +0.116 · data/analyst/scores.parquet: feature return_on_assets contribution
- F116 · Trend: return on assets (profit as a share of assets), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F117 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F118 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F119 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F121 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2023-09-30 · +0.200 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F122 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2023-09-30 · -0.026 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2023-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F130 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), change over one quarter, in percentage points · 2023-09-30 · -8.3 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2023-09-30 · +0.618 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F135 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: ratios outside their own prior range · 2023-09-30 · 17 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-09-30 · 6 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2023-09-30 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2022-09-30 · 94.6% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2023-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
