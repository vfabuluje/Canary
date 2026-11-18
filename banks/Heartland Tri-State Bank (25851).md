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
written_at: "2026-11-17T22:05:53"
writer_model: "claude-opus-5-5"
checked: true
---

# Heartland Tri-State Bank (cert 25851)

*Hindsight: failed 2023-07-28. Canary did not flag it.*

## Summary

As of Q1 2023, Heartland Tri-State Bank ranked 329 out of 4,740 banks nationally on Canary's risk score, a percentile of 93.1%, where higher means riskier. It was not flagged for Canary's watchlist, which covers the top 2% of banks by score. The biggest pushes upward came from large paper losses on its bond holdings, equal to 80.2% of its equity, and a thin equity cushion of 5.9% of assets. These were partly offset by a strong Tier 1 risk-based capital ratio of 17.7% and solid profitability.

## Warning signs in the data

Capital, the cushion that absorbs losses, was mixed: equity was 5.9% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 9.1% against 10.4%. By contrast, the Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 17.7%, well above the median of 14.2%.

Credit quality showed strain: loans 90 or more days late or no longer earning interest were 2.1% of loans, far above the median of 0.2%, and loans 30-89 days past due were 1.7% of assets against 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 11.5% versus a median of 1.7%, though loan-loss reserves (money set aside for bad loans) were a relatively high 2.1% of loans against 1.2%.

The most striking figure was bond losses: unrealized losses on bonds available for sale equaled 80.2% of equity, against a median of 15.5%, and securities made up 39.9% of assets versus 22.0%. Funding looked steadier: core deposits, the stable everyday deposits, were 87.9% of assets against 80.0%, uninsured deposits (balances above the insurance limit) were 26.7% versus 24.2%, and brokered deposits were 0.0%.

## Understanding the score

Heartland Tri-State Bank ranked 329 of 4,740 banks in Q1 2023, a percentile of 93.1% on a scale of 0 to 100. It was not flagged for the watchlist, which holds the top 2% of banks and had 95 banks that quarter.

The five features that raised the score most were losses on bonds available for sale at 80.2% of equity (+1.298), equity at 5.9% of assets (+0.147), construction loans at 0.0% of loans (+0.146), commercial real estate loans at 4.9% of loans (+0.018), and loans at 37.1% of deposits (+0.018).

The five features that lowered the score most were the Tier 1 risk-based capital ratio at 17.7% (-1.078), return on equity, or profit as a share of equity, at 14.5% (-0.606), the Texas ratio at 11.5% (-0.514), interest expense at 1.1% of assets (-0.495), and the total risk-based capital ratio at 18.9% (-0.356).

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

## Why the model missed it

In hindsight, the bank failed on 2023-07-28, and its last reported quarter was 2023-03-31. At that last report the model ranked it 329 of 4,740, high but outside the watchlist, so this counts as a miss.

The model was trained mostly on credit-loss failures, which made up 96% of the 539 failed banks in the training period. The fact sheet does not show what caused this failure, so the data cannot say why the model's warning was not stronger.

## What happened next

In hindsight, the bank failed on 2023-07-28. Its last reported quarter was 2023-03-31, so there are no later ranks or watchlist flags in our data after that point.

## Sources

- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
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
