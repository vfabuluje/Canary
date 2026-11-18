---
cert: 14361
name: "The First State Bank"
as_of: 2020-03-31
rank: 1
n_banks: 5182
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-04-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# The First State Bank (cert 14361)

*Hindsight: failed 2020-04-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-03-31, The First State Bank in WV ranked 1 out of 5,182 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile, the riskiest end of the scale. It was flagged on Canary's watchlist, which holds the top 2% of banks by score. Its capital cushion was nearly gone, with equity at 0.6% of assets against a national median of 11.4%, and 26.7% of its loans were 90+ days past due or not earning interest. The bank was also losing money, with a return on assets of -4.1%.

## Warning signs in the data

Capital, the owners' money that absorbs losses before depositors are hurt, was extremely thin. Equity was 0.6% of assets, far below the national median of 11.4%. The leverage ratio, core capital as a share of average assets, was 0.3% against a median of 10.9%. Risk-based capital ratios, which weigh assets by how risky they are, were also far below normal: the Tier 1 ratio was 0.4% versus a median of 14.6%, and the total ratio was 1.7% versus 15.7%.

Loan quality was very poor: 26.7% of loans were 90+ days past due or not accruing interest, compared with a national median of 0.6%. Nonaccrual assets and foreclosed property made up 26.0% of assets, against a median of 0.4%, and loans 30-89 days late were 2.4% of assets versus 0.4%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 1704.3%, against a median of 3.8%. Earnings were deeply negative, with return on assets of -4.1% versus a median of 0.9%, and the efficiency ratio, operating costs as a share of revenue, was 249.2% versus 68.7%.

On funding, the bank relied little on uninsured deposits, at 3.4% of deposits versus a median of 19.4%, and held more cash than usual, at 15.9% of assets versus 7.8%. Brokered deposits, money placed through middlemen that can leave quickly, were 4.2% of deposits, above the median of 0.0%. Unrealized losses on bonds available for sale equaled -40.1% of equity, far larger than the median of -0.8%, a sign of how small the equity base had become.

## Understanding the score

As of 2020-03-31, the bank ranked 1 of 5,182 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 104 banks that quarter, which covers the top 2% of banks by score.

The five features pushing the score up most were the Tier 1 risk-based capital ratio at 0.4%, return on equity at -406.7%, the Texas ratio at 1704.3%, loans 90+ days past due or not accruing at 26.7%, and the total risk-based capital ratio at 1.7%. Their contributions to the score were +2.093, +1.374, +1.289, +0.836 and +0.573 respectively.

The five features pulling the score down most were losses on bonds available for sale at -40.1% of equity, interest expense at 1.5% of assets, construction loans at 9.8% of loans, total assets of $151.8 million, and brokered deposits at 4.2% of deposits. Their contributions were -0.267, -0.170, -0.117, -0.089 and -0.085 respectively, small next to the drivers pushing the score up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-06-30 | 6 | 5,610 | ▲ watchlist |
| 2018-09-30 | 6 | 5,544 | ▲ watchlist |
| 2018-12-31 | 1 | 5,473 | ▲ watchlist |
| 2019-03-31 | 1 | 5,428 | ▲ watchlist |
| 2019-06-30 | 2 | 5,369 | ▲ watchlist (first flag) |
| 2019-09-30 | 4 | 5,325 | ▲ watchlist |
| 2019-12-31 | 1 | 5,244 | ▲ watchlist |
| 2020-03-31 | 1 | 5,182 | ▲ watchlist |

## How early Canary caught it

In hindsight, the bank failed on 2020-04-03. Canary first flagged it in the quarter ending 2019-06-30, a lead time of 4 quarters before the failure.

At that first flag, the main drivers were already visible: a Tier 1 risk-based capital ratio of 3.3%, return on equity of -87.3%, a Texas ratio of 704.2%, loans 90+ days past due or not accruing at 19.1%, and a total risk-based capital ratio of 4.5%. These same measures worsened by the quarter ending 2020-03-31, when the bank ranked first nationally.

## What happened next

In hindsight, the bank's last report to regulators covered the quarter ending 2020-03-31. It failed on 2020-04-03, just days after that quarter ended, so there are no later ranks or flags. The bank no longer reports; our data does not by itself distinguish a merger from a closure, but the failure date confirms how this case ended.

## Sources

- F3 · As-of quarter · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WV · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-03-31 · 5,182 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-03-31 · 104 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-03-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 0.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-03-31 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2020-03-31 · 2.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 3.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-03-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-03-31 · 68.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-03-31 · 3.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-03-31 · 19.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-03-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-03-31 · 15.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-03-31 · 7.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-03-31 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.4%; contribution to the score · 2020-03-31 · +2.093 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -406.7%; contribution to the score · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 1704.3%; contribution to the score · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 26.7%; contribution to the score · 2020-03-31 · +0.836 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.7%; contribution to the score · 2020-03-31 · +0.573 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -40.1%; contribution to the score · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2020-03-31 · -0.170 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: construction loans as a share of loans, value 9.8%; contribution to the score · 2020-03-31 · -0.117 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $151.8 million; contribution to the score · 2020-03-31 · -0.089 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: brokered deposits as a share of deposits, value 4.2%; contribution to the score · 2020-03-31 · -0.085 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F85 · Failure date · 2020-04-03 · 2020-04-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-06-30 · 2019-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2019-06-30 · +1.924 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-06-30: return on equity (profit as a share of equity), value -87.3%; contribution to the score · 2019-06-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2019-06-30: the Texas ratio (troubled assets against capital plus reserves), value 704.2%; contribution to the score · 2019-06-30 · +1.210 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2019-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 19.1%; contribution to the score · 2019-06-30 · +0.793 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-06-30: the total risk-based capital ratio, value 4.5%; contribution to the score · 2019-06-30 · +0.504 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
