---
cert: 57570
name: "Comenity Capital Bank"
as_of: 2026-06-30
rank: 80
n_banks: 4313
percentile: 98.1683283097612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:58:57"
writer_model: "claude-opus-5-5"
checked: true
---

# Comenity Capital Bank (cert 57570)

*Outcome not yet known.*

## Summary

Comenity Capital Bank, a Utah bank, ranked 80 out of 4,313 banks on Canary's risk score as of 2026-06-30, with a percentile of 98.2%, where higher means riskier. That puts it on the watchlist, which covers the riskiest 2% of banks. Its loan problems stand out: 3.2% of loans were 90+ days late or no longer paying interest, against a national median of 0.5%, and it wrote off 7.5% of its loans, against a median of 0.0%. Its capital cushion is strong, with equity at 13.0% of assets against a median of 10.6%, which holds the score down.

## Warning signs in the data

Credit quality is the clearest concern as of 2026-06-30. Loans 90+ days past due or not accruing interest were 3.2% of loans, well above the national median of 0.5%. Loans 30-89 days past due, an early sign of trouble, were 2.8% of assets against a median of 0.2%. Annualized write-offs (loans given up as lost, net of recoveries) were 7.5% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 6.5% of assets against a median of 0.1%. The bank holds large loss reserves to match, at 11.4% of loans against a median of 1.2%.

Capital, the cushion that absorbs losses, is mostly above the median: equity was 13.0% of assets against 10.6%, the leverage ratio was 12.8% against 11.0%, and the total risk-based capital ratio was 17.7% against 15.8%. The Tier 1 risk-based capital ratio was 14.2%, slightly below the median of 14.6%. Earnings are healthy, with return on assets of 1.7% against a median of 1.2% and a net interest margin of 19.3% against 3.9%.

On funding, the bank pays more for its money: annualized interest expense was 3.3% of assets against a median of 1.6%. Brokered deposits (funds placed through middlemen, often less loyal) were 9.8% of deposits against a median of 0.0%, and core deposits (stable everyday deposits) were 64.1% of assets, below the median of 75.5%. Uninsured deposits were only 8.8% of deposits against a median of 24.8%, and cash was 17.8% of assets against 6.2%, both reassuring for liquidity. Unrealized losses on bonds available for sale were small, at 0.6% of equity against a median of 5.6%.

## Understanding the score

As of 2026-06-30 the bank ranked 80 out of 4,313 banks, with a percentile of 98.2% on a scale of 0 to 100 where higher means riskier. It was one of 87 banks flagged on the watchlist, which covers the riskiest 2% of banks; its raw model score was 0.1040.

Five factors pushed the score up most. The largest was the provision for loan losses at 6.5% of assets, contributing +0.625. Next came interest expense at 3.3% of assets, contributing +0.488, and a small securities holding at 0.8% of assets, contributing +0.406. Loans 30-89 days past due at 2.8% of assets added +0.206, and brokered deposits at 9.8% of deposits added +0.194.

Five factors pulled the score down most. The Tier 1 risk-based capital ratio at 14.2% contributed -0.967, and return on equity (profit as a share of equity) at 12.7% contributed -0.544. The leverage ratio at 12.8% contributed -0.456, the total risk-based capital ratio at 17.7% contributed -0.447, and the Texas ratio (troubled assets against capital plus reserves) at 12.0% contributed -0.377.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 45 | 4,589 | ▲ watchlist |
| 2024-12-31 | 54 | 4,560 | ▲ watchlist |
| 2025-03-31 | 90 | 4,536 | ▲ watchlist |
| 2025-06-30 | 79 | 4,494 | ▲ watchlist |
| 2025-09-30 | 70 | 4,452 | ▲ watchlist |
| 2025-12-31 | 111 | 4,411 |  |
| 2026-03-31 | 63 | 4,353 | ▲ watchlist |
| 2026-06-30 | 80 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared, 14 were outside their own prior range, and the table shows the 6 furthest outside. The model rated the bank about the same as a year earlier: its percentile was 98.3% on 2025-06-30 and 98.2%, rank 80 of 4,313, on 2026-06-30.

Interest expense was 3.25% of assets, below its prior range of 3.34% to 3.9%, and it contributed +0.488, which pushed the score up. Loans 30-89 days past due were 2.8% of assets, just below their prior range of 2.9% to 3.6%, and they contributed +0.206, which pushed the score up. Loans 90+ days past due or not accruing were 3.2% of loans, below their prior range of 3.4% to 4.5%, and they contributed -0.090, which pushed the score down. Write-offs were 7.5% of loans, below their prior range of 8.4% to 9.5%, and contributed -0.010, which had little effect on the score.

Core deposits were 64.1% of assets, above their prior range of 48.8% to 62.3%, and they contributed -0.154, which pushed the score down. Uninsured deposits were 8.8% of deposits, above their prior range of 4.4% to 8.3% after rising +2.9 pp over four quarters, yet they contributed -0.109, which pushed the score down rather than up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 7.5% | 8.4% to 9.5% | same quarter, prior 3 years | n/a | -1.2 pp | -0.010 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 3.2% | 3.4% to 4.5% | prior 12 quarters | -0.4 pp | -0.5 pp | -0.090 | pushed the score down |
| core deposits as a share of assets | 64.1% | 48.8% to 62.3% | prior 12 quarters | +1.8 pp | +3.4 pp | -0.154 | pushed the score down |
| uninsured deposits as a share of deposits | 8.8% | 4.4% to 8.3% | prior 12 quarters | +0.5 pp | +2.9 pp | -0.109 | pushed the score down |
| annualized interest expense as a share of assets | 3.25% | 3.34% to 3.9% | same quarter, prior 3 years | n/a | -0.4 pp | +0.488 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 2.8% | 2.9% to 3.6% | prior 12 quarters | -0.1 pp | -0.2 pp | +0.206 | pushed the score up |

14 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this fact sheet contains no data from after the as-of quarter, so there is no later evidence to explain the bank's watchlist status. Its place on the watchlist rests on its as-of figures, and the bank is treated as an open watchlist case: flagged, with no later outcome recorded in our data.

## What happened next

In hindsight, our data holds no later quarters for this bank yet, so later ranks, later watchlist flags, and whether it keeps reporting cannot be stated. Canary would show those once newer filings are added, without distinguishing a merger from a closure if the bank stops reporting.

## Sources

- F1 · Bank name · n/a · Comenity Capital Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.1040 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 80 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 12.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 19.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 64.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 17.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: annualized provision for loan losses as a share of assets, value 6.5%; contribution to the score · 2026-06-30 · +0.625 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · +0.406 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.206 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 9.8%; contribution to the score · 2026-06-30 · +0.194 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.2%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 12.7%; contribution to the score · 2026-06-30 · -0.544 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 12.8%; contribution to the score · 2026-06-30 · -0.456 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 17.7%; contribution to the score · 2026-06-30 · -0.447 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 12.0%; contribution to the score · 2026-06-30 · -0.377 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F90 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 9.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F94 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F95 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F96 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F97 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F100 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.090 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F101 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F102 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 64.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F103 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 48.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F104 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 62.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F107 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.154 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F108 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F109 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F110 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F113 · Trend: uninsured deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +2.9 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F114 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.109 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F115 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F116 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 3.25% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F117 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 3.34% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F118 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F120 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F121 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F122 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F123 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F124 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F127 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.206 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F128 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
