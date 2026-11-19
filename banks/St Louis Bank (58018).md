---
cert: 58018
name: "St Louis Bank"
as_of: 2026-06-30
rank: 20
n_banks: 4313
percentile: 99.55947136563876
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:57"
writer_model: "claude-opus-5-5"
checked: true
---

# St Louis Bank (cert 58018)

*Outcome not yet known.*

## Summary

St Louis Bank, a Missouri bank, ranked 20 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. That rank puts it on Canary's watchlist, the riskiest 2% of banks. Its funding stands out most: brokered deposits (money placed through middlemen rather than gathered from local customers) made up 42.2% of deposits, against a national median of 0.0%. Its capital cushions were also thinner than typical, and its share of troubled loans was well above the national median.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was below typical levels: equity was 8.6% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.8% versus 11.0%. Risk-based measures, which weigh assets by how risky they are, were also lower, with a Tier 1 risk-based capital ratio of 10.0% against a median of 14.6% and a total risk-based capital ratio of 11.3% against 15.8%.

Credit quality was weaker than most banks: loans 90 or more days past due or no longer accruing interest were 2.9% of loans versus a median of 0.5%, and nonaccrual assets plus foreclosed property were 2.5% of assets versus 0.3%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, was 25.5%, far above the median of 2.9%. Lending leaned toward property, with commercial real estate loans at 40.1% of loans versus 23.6% nationally, and construction loans at 10.9% versus 5.3%.

On funding, brokered deposits were 42.2% of deposits against a median of 0.0%, while core deposits, the steadier everyday deposit base, were only 48.6% of assets versus 75.5%. The bank lent out more of its deposits than typical, with loans at 90.2% of deposits versus 80.2%, paid more for its funding, with interest expense at 2.4% of assets versus 1.6%, and held less cash, at 3.2% of assets versus 6.2%. Unrealized losses on bonds available for sale equaled 6.6% of equity, somewhat above the median of 5.6%.

## Understanding the score

As of 2026-06-30, St Louis Bank ranked 20 out of 4,313 banks, which is the 99.6th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were brokered deposits at 42.2% of deposits, contributing +1.489, and losses on bonds available for sale at 6.6% of equity, contributing +0.804. Next came core deposits at 48.6% of assets, contributing +0.440, the efficiency ratio (operating costs as a share of revenue) at 56.8%, contributing +0.393, and interest expense at 2.4% of assets, contributing +0.256.

The five factors that pulled the score down most were return on equity (profit as a share of equity) at 10.7%, contributing -0.656, and the Tier 1 risk-based capital ratio at 10.0%, contributing -0.600. They were followed by loans 30-89 days past due at 0.5% of assets, contributing -0.424, the Texas ratio at 25.5%, contributing -0.294, and construction loans at 10.9% of loans, contributing -0.294.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 421 | 4,589 |  |
| 2024-12-31 | 287 | 4,560 |  |
| 2025-03-31 | 225 | 4,536 |  |
| 2025-06-30 | 156 | 4,494 |  |
| 2025-09-30 | 113 | 4,452 |  |
| 2025-12-31 | 247 | 4,411 |  |
| 2026-03-31 | 21 | 4,353 | ▲ watchlist |
| 2026-06-30 | 20 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compared 30 of the bank's ratios with their own range over the prior 12 quarters, and 10 of them sat outside that range as of 2026-06-30. The model rated the bank riskier than a year earlier: it was in the 96.6th percentile on 2025-06-30 and in the 99.6th percentile, at rank 20, on 2026-06-30.

Nonaccrual assets and foreclosed property reached 2.5% of assets, above their prior range of 0.8% to 1.8%, yet this ratio contributed -0.010 model log-odds units and had little effect on the score. The Texas ratio rose to 25.5%, above its prior range of 8.7% to 19.2% after a +6.2 pp jump in one quarter, but its contribution of -0.294 pushed the score down. Loans 90 or more days past due or not accruing interest climbed to 2.9% of loans, above their prior range of 0.3% to 2.1%, yet their contribution of -0.180 pushed the score down. Commercial real estate loans rose to 40.1% of loans, above their prior range of 35.7% to 39.0%, but their contribution of -0.152 pushed the score down.

Core deposits fell to 48.6% of assets, below their prior range of 50.5% to 60.7%, and their contribution of +0.440 pushed the score up. The efficiency ratio improved to 56.8%, below its prior range of 59.8% to 78.0%, and its contribution of +0.393 pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 2.5% | 0.8% to 1.8% | prior 12 quarters | +0.8 pp | +1.0 pp | -0.010 | little effect on the score |
| the Texas ratio (troubled assets against capital plus reserves) | 25.5% | 8.7% to 19.2% | prior 12 quarters | +6.2 pp | +10.4 pp | -0.294 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 2.9% | 0.3% to 2.1% | prior 12 quarters | +0.8 pp | +1.3 pp | -0.180 | pushed the score down |
| commercial real estate loans as a share of loans | 40.1% | 35.7% to 39.0% | prior 12 quarters | +1.4 pp | +1.8 pp | -0.152 | pushed the score down |
| core deposits as a share of assets | 48.6% | 50.5% to 60.7% | prior 12 quarters | -1.9 pp | -3.4 pp | +0.440 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 56.8% | 59.8% to 78.0% | same quarter, prior 3 years | n/a | -3.0 pp | +0.393 | pushed the score up |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank's case is an open watchlist entry: it was flagged as of the as-of quarter, and the fact sheet holds no later data that settles how things turned out. Its place on the watchlist rests on the as-of picture described above, chiefly its heavy reliance on brokered deposits, thin core deposit base and bond losses, rather than on any known later event.

## What happened next

In hindsight, the fact sheet provides no information after the as-of quarter, so it does not show later ranks, later watchlist flags, or whether the bank has kept filing its regular reports. The case therefore remains open, and nothing here indicates either a failure or a recovery.

## Sources

- F1 · Bank name · n/a · St Louis Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MO · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 20 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 40.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 90.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 42.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 42.2%; contribution to the score · 2026-06-30 · +1.489 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.6%; contribution to the score · 2026-06-30 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 48.6%; contribution to the score · 2026-06-30 · +0.440 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 56.8%; contribution to the score · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.256 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 10.7%; contribution to the score · 2026-06-30 · -0.656 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.0%; contribution to the score · 2026-06-30 · -0.600 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.5%; contribution to the score · 2026-06-30 · -0.424 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature texas_ratio contribution
- F84 · Driver down #5: construction loans as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F89 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F90 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F91 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F94 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F95 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F96 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F97 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 8.7% · data/features/fct_bank_features.parquet: texas_ratio
- F98 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 19.2% · data/features/fct_bank_features.parquet: texas_ratio
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +6.2 pp · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature texas_ratio contribution
- F102 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F103 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F104 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F108 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F109 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F110 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 40.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F111 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 35.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F112 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 39.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F115 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.152 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F116 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 50.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 60.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.440 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 56.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 59.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 78.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.6% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
