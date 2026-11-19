---
cert: 25851
name: "Heartland Tri-State Bank"
as_of: 2023-03-31
rank: 329
n_banks: 4740
percentile: 93.08016877637131
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-07-28
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:46:09"
writer_model: "claude-opus-5-5"
checked: true
---

# Heartland Tri-State Bank (cert 25851)

*Hindsight: failed 2023-07-28. Canary did not flag it.*

## Summary

Heartland Tri-State Bank, a Kansas bank with $139.4 million in total assets, ranked 329 out of 4,740 banks on Canary's risk score as of March 31, 2023. That put it at a percentile of 93.1% on a 0 to 100 scale where higher means riskier, but it was not flagged on the watchlist, which covers the riskiest 2% of banks. Its biggest weak spot was paper losses on bonds it could sell before maturity, equal to 80.2% of its equity (the owners' cushion), far above the national median of 15.5%. Strong risk-based capital and solid profits pulled its score down.

## Warning signs in the data

Capital was mixed: equity, the owners' cushion against losses, was 5.9% of assets, well below the national median of 9.2%. The leverage ratio (core capital as a share of average assets) was 9.1%, also below the median of 10.4%. Yet the Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 17.7%, above the median of 14.2%.

On credit quality, loans 90 or more days past due or no longer earning interest were 2.1% of loans, far above the median of 0.2%. Loans 30-89 days past due were 1.7% of assets, against a median of 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 11.5%, well above the median of 1.7%, though reserves set aside for loan losses were 2.1% of loans versus a median of 1.2%.

The largest outlier was bonds: paper losses on available-for-sale bonds equaled 80.2% of equity, against a median of 15.5%, and securities made up 39.9% of assets versus a median of 22.0%. Funding looked steady, with core deposits (stable, everyday deposits) at 87.9% of assets versus a median of 80.0%, brokered deposits at 0.0%, and uninsured deposits at 26.7% of deposits, a little above the median of 24.2%.

## Understanding the score

As of March 31, 2023, the bank ranked 329 out of 4,740 banks, with a percentile of 93.1% on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which held the top 2% of banks, or 95 banks that quarter.

The five factors that pushed the score up most were: paper losses on available-for-sale bonds at 80.2% of equity, contributing +1.298; equity at 5.9% of assets, contributing +0.147; construction loans at 0.0% of loans, contributing +0.146; commercial real estate loans at 4.9% of loans, contributing +0.018; and loans at 37.1% of deposits, contributing +0.018.

The five factors that pulled the score down most were: the Tier 1 risk-based capital ratio at 17.7%, contributing -1.078; return on equity (profit as a share of equity) at 14.5%, contributing -0.606; the Texas ratio at 11.5%, contributing -0.514; interest expense at 1.1% of assets, contributing -0.495; and the total risk-based capital ratio at 18.9%, contributing -0.356.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-06-30 | 2,387 | 5,015 |  |
| 2021-09-30 | 1,822 | 4,979 |  |
| 2021-12-31 | 2,742 | 4,904 |  |
| 2022-03-31 | 619 | 4,861 |  |
| 2022-06-30 | 1,146 | 4,838 |  |
| 2022-09-30 | 571 | 4,813 |  |
| 2022-12-31 | 1,349 | 4,773 |  |
| 2023-03-31 | 329 | 4,740 |  |

## How its ratios moved

The bank ranked 329 out of 4,740 in Q1 2023 with a percentile of 93.1%, compared with 87.3% in Q1 2022, so the model rated it riskier than a year earlier. Of 30 ratios compared with the bank's own prior 12 quarters, 10 sat outside their earlier range, and the table shows the 6 furthest out.

Return on equity was 14.5%, above its prior range of 8.2% to 13.7%, yet it pushed the score down, contributing -0.606. Interest expense was 1.1% of assets, above its prior range of 0.3% to 0.8%, yet it pushed the score down, contributing -0.495. Securities were 39.9% of assets, just above their prior range of 29.9% to 39.2%, yet they pushed the score down, contributing -0.160.

Core deposits were 87.9% of assets, above their prior range of 78.2% to 87.3%, and pushed the score down with a contribution of -0.079. Cash was 6.6% of assets, above its prior range of 2.9% to 5.6%, yet had little effect on the score, contributing -0.037. Loans were 37.1% of deposits, below their prior range of 39.2% to 66.1%, and also had little effect on the score, contributing +0.018.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| cash as a share of assets | 6.6% | 2.9% to 5.6% | prior 12 quarters | +1.0 pp | +1.3 pp | -0.037 | little effect on the score |
| annualized interest expense as a share of assets | 1.1% | 0.3% to 0.8% | same quarter, prior 3 years | n/a | +0.8 pp | -0.495 | pushed the score down |
| return on equity (profit as a share of equity) | 14.5% | 8.2% to 13.7% | same quarter, prior 3 years | n/a | +6.4 pp | -0.606 | pushed the score down |
| loans as a share of deposits | 37.1% | 39.2% to 66.1% | prior 12 quarters | -4.4 pp | -5.3 pp | +0.018 | little effect on the score |
| core deposits as a share of assets | 87.9% | 78.2% to 87.3% | prior 12 quarters | +0.6 pp | +2.1 pp | -0.079 | pushed the score down |
| securities as a share of assets | 39.9% | 29.9% to 39.2% | prior 12 quarters | +2.1 pp | +4.4 pp | -0.160 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on July 28, 2023, and its last report was for the quarter ending March 31, 2023. The model ranked it 329 out of 4,740 with a percentile of 93.1%, high but not on the watchlist, so this counts as a miss.

The model learned mostly from past credit-loss failures: 96% of the 539 failed banks in its training period were credit-loss failures. This bank did not fit that pattern well, with construction loans at 0.0% and commercial real estate loans at 4.9% of loans, both far below national medians. Its strong risk-based capital and profits pulled the score down, offsetting much of the push from bond losses equal to 80.2% of equity.

## What happened next

In hindsight, the bank failed on July 28, 2023. Its last reported quarter was March 31, 2023, so it has no later scores or ranks.

## Sources

- F1 · Bank name · n/a · Heartland Tri-State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-03-31 · 329 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-03-31 · 4,740 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-03-31 · 93.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-03-31 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-03-31 · 5.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 9.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-03-31 · 17.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F35 · Bank: commercial real estate loans as a share of loans · 2023-03-31 · 4.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 11.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 26.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F55 · Bank: core deposits as a share of assets · 2023-03-31 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-03-31 · 80.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-03-31 · 15.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-03-31 · 39.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-03-31 · 22.0% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2023-03-31 · $139.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 80.2%; contribution to the score · 2023-03-31 · +1.298 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: equity as a share of assets, value 5.9%; contribution to the score · 2023-03-31 · +0.147 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F77 · Driver up #3: construction loans as a share of loans, value 0.0%; contribution to the score · 2023-03-31 · +0.146 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 4.9%; contribution to the score · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: loans as a share of deposits, value 37.1%; contribution to the score · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 17.7%; contribution to the score · 2023-03-31 · -1.078 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 14.5%; contribution to the score · 2023-03-31 · -0.606 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 11.5%; contribution to the score · 2023-03-31 · -0.514 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2023-03-31 · -0.495 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 18.9%; contribution to the score · 2023-03-31 · -0.356 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F85 · Failure date · 2023-07-28 · 2023-07-28 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: cash as a share of assets, value at the as-of quarter · 2023-03-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F92 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F93 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 5.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F96 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.037 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F97 · Trend: cash as a share of assets, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F98 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2023-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F100 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F102 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.495 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F103 · Trend: annualized interest expense as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F104 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-03-31 · 14.5% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.7% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-03-31 · -0.606 · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: loans as a share of deposits, value at the as-of quarter · 2023-03-31 · 37.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F111 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F112 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 66.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F115 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F116 · Trend: loans as a share of deposits, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2023-03-31 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 78.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 87.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.079 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: securities as a share of assets, value at the as-of quarter · 2023-03-31 · 39.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F125 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 29.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F126 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F129 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.160 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F130 · Trend: securities as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F131 · Trend: ratios outside their own prior range · 2023-03-31 · 10 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-03-31 · 6 · data/features/fct_bank_features.parquet
- F133 · Trend: ratios compared with their own prior range · 2023-03-31 · 30 · data/features/fct_bank_features.parquet
- F134 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F136 · Percentile a year earlier (100 = highest risk) · 2022-03-31 · 87.3% · data/analyst/scores.parquet: percentile
- F137 · Trend: how the model's rating compares with a year earlier · 2023-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
