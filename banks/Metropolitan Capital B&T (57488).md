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
written_at: "2026-11-18T19:53:13"
writer_model: "claude-opus-5-5"
checked: true
---

# Metropolitan Capital B&T (cert 57488)

*Hindsight: failed 2026-01-30. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2025-12-31, Metropolitan Capital B&T ranked 2 out of 4,411 banks nationally on Canary's risk score, placing it in the 100.0th percentile on a 0 to 100 scale where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks and held 89 banks that quarter. Its cushion of owners' money was gone, with equity at -0.8% of assets against a national median of 10.4%, and it was losing money, with a return on assets of -6.9% against a median of 1.1%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below normal: the leverage ratio (core capital as a share of average assets) was 1.8% against a national median of 10.8%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 3.0% against a median of 14.4%, and the total risk-based capital ratio was 4.3% against 15.6%.

Loan quality was weak: loans 90 or more days late or no longer paying interest were 2.8% of loans, well above the median of 0.4%. Annualized write-offs of bad loans, net of recoveries, reached 12.4% of loans against a median of 0.0%, and new provisions set aside for loan losses ran at 6.1% of assets against 0.1%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 152.5%, far above the median of 2.7%.

On funding, brokered deposits (money placed through intermediaries, which can leave quickly) were 22.0% of deposits against a median of 0.0%, and borrowings from the Federal Home Loan Bank were 14.0% of assets against 0.2%. Deposit growth over the past four quarters was -7.3% while the median bank's was 4.1%, though the bank did hold more cash than usual, at 16.7% of assets against 6.5%. Losses on bonds available for sale, as a share of equity, read -684.7%, an unusual figure far from the national median of 5.2%.

## Understanding the score

Metropolitan Capital B&T ranked 2 of 4,411 banks as of 2025-12-31, the 100.0th percentile, with a raw model score of 0.9774. It was flagged on the watchlist, the riskiest 2% of banks, which numbered 89 that quarter.

Five features pushed the score up the most, led by the Tier 1 risk-based capital ratio at 3.0%, contributing +1.701. Next came return on equity (profit as a share of owners' money) at -672.4%, contributing +1.537, and the Texas ratio at 152.5%, contributing +1.021. The total risk-based capital ratio at 4.3% added +0.524, and the leverage ratio at 1.8% added +0.364.

Five features pulled the score down, led by nonaccrual assets and foreclosed property at 2.2% of assets, contributing -0.489. Net interest margin, the spread earned on lending and investing, at 4.9% contributed -0.426, and losses on bonds available for sale at -684.7% of equity contributed -0.368. Loans 90 or more days late or not accruing interest at 2.8% contributed -0.262, and construction loans at 4.7% of loans contributed -0.227.

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

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked, 15 sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 2 of 4,411 as of 2025-12-31 and was in the 100.0th percentile a year earlier at 2024-12-31, so the model rated it about the same as a year earlier.

Return on equity fell to -672.4%, a change of -581.5 pp over four quarters. At -672.4%, far below its prior range of -91.0% to 14.6%, return on equity had a contribution of +1.537 model log-odds units, which pushed the score up. The efficiency ratio (operating costs as a share of revenue) rose to 123.3%, above its range of 76.3% to 91.0%, yet its contribution of -0.044 had little effect on the score. Annualized net loan write-offs reached 12.4%, above their range of 0.0% to 4.5%, but their contribution of -0.024 had little effect on the score.

Losses on bonds available for sale, as a share of equity, read -684.7%, below their range of 73.1% to 505.3%, yet their contribution of -0.368 pushed the score down. Construction loans rose to 4.7% of loans, above their range of 0.0% to 3.2%, yet their contribution of -0.227 pushed the score down. Net interest margin slipped to 4.9%, below its range of 5.7% to 7.4%, and its contribution of -0.426 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -672.4% | -91.0% to 14.6% | same quarter, prior 3 years | n/a | -581.5 pp | +1.537 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 123.3% | 76.3% to 91.0% | same quarter, prior 3 years | n/a | +32.3 pp | -0.044 | little effect on the score |
| losses on bonds available for sale, as a share of equity | -684.7% | 73.1% to 505.3% | prior 12 quarters | -982.2 pp | -1189.9 pp | -0.368 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 12.4% | 0.0% to 4.5% | same quarter, prior 3 years | n/a | +7.8 pp | -0.024 | little effect on the score |
| construction loans as a share of loans | 4.7% | 0.0% to 3.2% | prior 12 quarters | +1.5 pp | +4.7 pp | -0.227 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 4.9% | 5.7% to 7.4% | same quarter, prior 3 years | n/a | -1.7 pp | -0.426 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, this is a case Canary caught: the bank failed on 2026-01-30, after the model's test window. Under the lead-time rule, the bank was first flagged in the quarter ending 2025-03-31, a lead time of 4 quarters before the failure.

At that first flag, the top driver pushing the score up was return on equity at -72.9%, contributing +1.052. The Texas ratio at 138.8% added +0.874, and the Tier 1 risk-based capital ratio at 6.3% added +0.666.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the last quarter the bank reported was 2025-12-31, so there are no later ranks or flags. The bank failed on 2026-01-30.

## Sources

- F1 · Bank name · n/a · Metropolitan Capital B&T · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
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
- F31 · Bank: annualized provision for loan losses as a share of assets · 2025-12-31 · 6.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 152.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2025-12-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
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
- F98 · Last quarter the bank reported · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · -672.4% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -91.0% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2025-12-31 · -581.5 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · +1.537 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-12-31 · 123.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 76.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 91.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-12-31 · -0.044 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2025-12-31 · -684.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F112 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · 73.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F113 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 505.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F116 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F118 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F119 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F120 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F122 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · -0.024 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F124 · Trend: construction loans as a share of loans, value at the as-of quarter · 2025-12-31 · 4.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F125 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F126 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F129 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · -0.227 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F130 · Trend: construction loans as a share of loans, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F131 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2025-12-31 · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F132 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 5.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F133 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F135 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2025-12-31 · -0.426 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F136 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F137 · Trend: ratios outside their own prior range · 2025-12-31 · 15 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
