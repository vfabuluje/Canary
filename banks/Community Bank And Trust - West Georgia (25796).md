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
written_at: "2026-11-18T19:52:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Community Bank And Trust - West Georgia (cert 25796)

*Hindsight: failed 2026-05-01. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

Community Bank And Trust - West Georgia, a bank based in GA, ranked 2 out of 4,353 banks nationally on Canary's risk score as of 2026-03-31, placing it in the 100.0th percentile, the riskiest end of the scale. It was flagged on Canary's watchlist, which covers about 2% of banks. Its equity, the owners' cushion against losses, was only 1.3% of assets against a national median of 10.4%, while troubled loans and losses were far above typical levels.

## Warning signs in the data

Capital, the bank's buffer for absorbing losses, was extremely thin as of 2026-03-31. Equity was 1.3% of assets versus a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 0.2% versus a median of 10.9%. The Tier 1 risk-based capital ratio, which measures core capital against riskier assets, was 0.2% against a median of 14.5%, and the total risk-based capital ratio was 1.5% against 15.7%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 17.3% of loans, far above the national median of 0.5%, and loans 30-89 days past due were 5.5% of assets against a median of 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 280.0% versus a median of 2.9%. Annualized loan write-offs were 6.3% of loans against a median of 0.0%, and the bank lost money, with return on assets of -6.9% versus a median of 1.2%.

Funding looked steadier: uninsured deposits, those above the government insurance limit, were 3.6% of deposits, well below the median of 24.4%, and cash was 16.2% of assets versus a median of 6.9%. On bonds available for sale, the bank's figure for losses as a share of equity was -177.9%, very different from the national median of 5.8%.

## Understanding the score

As of 2026-03-31 the bank ranked 2 of 4,353 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds about 2% of banks, or 88 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 0.2%, return on equity (profit as a share of the owners' stake) at -191.5%, the Texas ratio at 280.0%, loans 90+ days past due or not accruing interest at 17.3%, and the total risk-based capital ratio at 1.5%. The five factors that pulled the score down most were the bond-loss measure for available-for-sale bonds at -177.9%, asset growth over the past four quarters at 23.9%, construction loans at 8.1% of loans, total assets of $292.6 million, and the efficiency ratio (operating costs as a share of revenue) at 92.4%.

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

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. As of 2026-03-31, 15 of the 30 ratios checked sat outside their own prior range, and the 6 furthest outside are discussed here. The bank ranked 2 of 4,353, and the model rated it about the same as a year earlier, when its percentile was also 100.0%.

Return on equity was -191.5%, below its prior range of 0.4% to 19.1% and down -191.9 pp over four quarters; it contributed +1.318 model log-odds units and pushed the score up. Return on assets was -6.9%, below its prior range of 0.0% to 0.7% and down -6.9 pp over four quarters; it contributed +0.166 and pushed the score up. The annualized provision for loan losses, money set aside for expected bad loans, was 8.7% of assets, above its prior range of 0.3% to 1.7% and up +7.0 pp; it contributed +0.144 and pushed the score up.

Net interest margin was 2.4%, below its prior range of 4.7% to 6.3% and down -2.3 pp over four quarters; it contributed +0.094 and pushed the score up. The leverage ratio was 0.2%, below its prior range of 5.1% to 9.8%, down -6.5 pp over one quarter and -7.2 pp over four quarters; it contributed +0.180 and pushed the score up. Loan write-offs were 6.3% of loans, above their prior range of 0.0% to 2.6% and up +3.7 pp, yet they contributed only -0.005 and had little effect on the score despite being outside their range.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -191.5% | 0.4% to 19.1% | same quarter, prior 3 years | n/a | -191.9 pp | +1.318 | pushed the score up |
| return on assets (profit as a share of assets) | -6.9% | 0.0% to 0.7% | same quarter, prior 3 years | n/a | -6.9 pp | +0.166 | pushed the score up |
| annualized provision for loan losses as a share of assets | 8.7% | 0.3% to 1.7% | same quarter, prior 3 years | n/a | +7.0 pp | +0.144 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.4% | 4.7% to 6.3% | same quarter, prior 3 years | n/a | -2.3 pp | +0.094 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 6.3% | 0.0% to 2.6% | same quarter, prior 3 years | n/a | +3.7 pp | -0.005 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 0.2% | 5.1% to 9.8% | prior 12 quarters | -6.5 pp | -7.2 pp | +0.180 | pushed the score up |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged this bank in the quarter ending 2025-06-30, 4 quarters before it failed on 2026-05-01. At that first flag, the top factors pushing the score up were the Texas ratio at 158.3%, the Tier 1 risk-based capital ratio at 5.6%, and loans 90+ days past due or not accruing interest at 14.7%. Also pushing up were the bond-loss measure for available-for-sale bonds at 36.8% of equity and the total risk-based capital ratio at 6.9%.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the bank failed on 2026-05-01. The last quarter it reported financial data was 2026-03-31, the same quarter this memo describes, so there are no later ranks or flags.

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
- F61 · Bank: cash as a share of assets · 2026-03-31 · 16.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · -177.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
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
- F91 · Driver up #4 at 2025-06-30: losses on bonds available for sale, as a share of equity, value 36.8%; contribution to the score · 2025-06-30 · +0.877 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F92 · Driver up #5 at 2025-06-30: the total risk-based capital ratio, value 6.9%; contribution to the score · 2025-06-30 · +0.510 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-03-31 · -191.5% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 19.1% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-03-31 · -191.9 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-03-31 · +1.318 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-03-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2026-03-31 · -6.9 pp · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.166 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-03-31 · 8.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F114 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-03-31 · +7.0 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.144 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-03-31 · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), change over four quarters, in percentage points · 2026-03-31 · -2.3 pp · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-03-31 · +0.094 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F126 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-03-31 · +3.7 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-03-31 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F130 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 5.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), change over one quarter, in percentage points · 2026-03-31 · -6.5 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F133 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2026-03-31 · -7.2 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.180 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F135 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: ratios outside their own prior range · 2026-03-31 · 15 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-03-31 · 6 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2026-03-31 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
