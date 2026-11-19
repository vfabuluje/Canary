---
cert: 1756
name: "Central Bank"
as_of: 2026-06-30
rank: 10
n_banks: 4313
percentile: 99.79132854161836
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:54:42"
writer_model: "claude-opus-5-5"
checked: true
---

# Central Bank (cert 1756)

*Outcome not yet known.*

## Summary

Central Bank, based in AR, ranked 10 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.8th percentile, where higher means riskier. That puts it on Canary's watchlist, the top 2% of banks by score. The main concerns in the data are heavy reliance on brokered deposits (funds placed through middlemen rather than gathered from local customers) and a high level of troubled loans compared with its capital.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than at a typical bank: equity was 9.2% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.4% against 11.0%. Its Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was 10.3% versus a median of 14.6%, and its total risk-based capital ratio was 11.6% versus 15.8%.

Credit quality stood out most: loans 90+ days past due or not accruing interest were 4.8% of loans, far above the 0.5% national median. Nonaccrual assets and foreclosed property were 4.5% of assets versus a median of 0.3%, and loans 30-89 days past due were 1.9% of assets versus 0.2%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 43.2%, far above the 2.9% median.

On funding, brokered deposits made up 39.9% of deposits while the median bank had 0.0%, and core deposits (stable, everyday customer deposits) were only 40.0% of assets against a median of 75.5%. Federal Home Loan Bank borrowings were 12.3% of assets versus 0.2%, loans equaled 108.9% of deposits versus 80.2%, and cash was 3.4% of assets versus 6.2%. Interest expense was 3.3% of assets, well above the 1.6% median, while unrealized losses on bonds available for sale were modest at 2.6% of equity, below the 5.6% median.

## Understanding the score

As of 2026-06-30, Central Bank ranked 10 out of 4,313 banks, which is the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors that pushed its score up most were brokered deposits at 39.9% of deposits (+0.785), the Texas ratio at 43.2% (+0.743), and interest expense at 3.3% of assets (+0.581). Also pushing it up were loans 90+ days past due or not accruing at 4.8% of loans (+0.324) and the efficiency ratio, operating costs as a share of revenue, at 34.5% (+0.324).

The five factors that pulled its score down most were the Tier 1 risk-based capital ratio at 10.3% (-0.658), return on equity at 11.8% (-0.624), and construction loans at 7.9% of loans (-0.414). Loan-loss reserves, money set aside for expected bad loans, at 1.4% of loans (-0.292) and return on assets at 1.1% (-0.281) also pulled the score down.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 158 | 4,589 |  |
| 2024-12-31 | 292 | 4,560 |  |
| 2025-03-31 | 163 | 4,536 |  |
| 2025-06-30 | 209 | 4,494 |  |
| 2025-09-30 | 87 | 4,452 | ▲ watchlist |
| 2025-12-31 | 55 | 4,411 | ▲ watchlist |
| 2026-03-31 | 18 | 4,353 | ▲ watchlist |
| 2026-06-30 | 10 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked, 15 sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 10 out of 4,313 at the 99.8th percentile, up from the 95.4th percentile on 2025-06-30, so the model rated it riskier than a year earlier.

Loans 30-89 days past due rose +0.9 pp over one quarter and +1.7 pp over four quarters. At 1.9% of assets, above a prior range of 0.1% to 1.2%, this ratio pushed the score up, contributing +0.141 model log-odds units. The annualized provision for loan losses, money expensed for expected bad loans, was 0.7% of assets against a prior range of 0.3% to 0.4%, up +0.4 pp, and it pushed the score up with a contribution of +0.077.

Return on equity fell to 11.8%, below its prior range of 18.2% to 21.3% and down -6.4 pp over four quarters, yet it still pushed the score down with a contribution of -0.624. Return on assets dropped to 1.1%, below its prior range of 1.6% to 1.8% and down -0.7 pp, but it too pushed the score down, contributing -0.281. Net interest margin slipped to 3.2%, below its prior range of 3.7% to 3.9% and down -0.5 pp, while it pushed the score down with a contribution of -0.075. Net loan write-offs rose to 0.7% of loans, above a prior range of 0.0% to 0.0% and up +0.6 pp, yet this had little effect on the score, at +0.012.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 11.8% | 18.2% to 21.3% | same quarter, prior 3 years | n/a | -6.4 pp | -0.624 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.6 pp | +0.012 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 1.9% | 0.1% to 1.2% | prior 12 quarters | +0.9 pp | +1.7 pp | +0.141 | pushed the score up |
| return on assets (profit as a share of assets) | 1.1% | 1.6% to 1.8% | same quarter, prior 3 years | n/a | -0.7 pp | -0.281 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.2% | 3.7% to 3.9% | same quarter, prior 3 years | n/a | -0.5 pp | -0.075 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.7% | 0.3% to 0.4% | same quarter, prior 3 years | n/a | +0.4 pp | +0.077 | pushed the score up |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this fact sheet contains no data from after the as-of quarter, so the bank remains an open watchlist case. It was flagged on the watchlist based on its own figures, and nothing here records what became of it afterward.

## What happened next

Looking ahead in hindsight, the fact sheet provides no later ranks, watchlist flags or reporting status for this bank. Because of that, we cannot say from this data whether it stayed on the watchlist, moved off it, or stopped reporting.

## Sources

- F1 · Bank name · n/a · Central Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 43.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 108.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 39.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 40.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 39.9%; contribution to the score · 2026-06-30 · +0.785 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 43.2%; contribution to the score · 2026-06-30 · +0.743 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.581 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 4.8%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 34.5%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.3%; contribution to the score · 2026-06-30 · -0.658 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 11.8%; contribution to the score · 2026-06-30 · -0.624 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 7.9%; contribution to the score · 2026-06-30 · -0.414 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.4%; contribution to the score · 2026-06-30 · -0.292 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 18.2% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 21.3% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -6.4 pp · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.624 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F98 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +0.6 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F104 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +0.9 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F105 · Trend: loans 30-89 days past due, as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +1.7 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.141 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2026-06-30 · -0.7 pp · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F114 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F115 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F117 · Trend: net interest margin (the spread earned on lending and investing), change over four quarters, in percentage points · 2026-06-30 · -0.5 pp · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.075 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F119 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F120 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F121 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F122 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F123 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +0.4 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F124 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.077 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F125 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 95.4% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
