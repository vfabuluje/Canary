---
cert: 59017
name: "First Republic Bank"
as_of: 2023-03-31
rank: 809
n_banks: 4740
percentile: 82.9535864978903
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-05-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:05:13"
writer_model: "claude-opus-5-5"
checked: true
---

# First Republic Bank (cert 59017)

*Hindsight: failed 2023-05-01. Canary did not flag it.*

## Summary

As of 2023-03-31, First Republic Bank, a California bank with $232.9 billion in assets, ranked 809 out of 4,740 banks on Canary's risk score, which places it at the 83.0th percentile. It was not flagged on the watchlist that quarter. Its loan book looked clean, but its funding stood out: loans equaled 165.1% of deposits, and volatile funding made up 53.0% of assets, both far above the national medians. Its capital cushions were also somewhat thinner than those of the typical bank.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below the national median on every measure as of 2023-03-31. Equity was 7.7% of assets against a median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 8.2% against 10.4%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 11.7% against a median of 14.2%. Credit quality, by contrast, was strong: loans 90+ days past due or not accruing interest were 0.1% of loans against a median of 0.2%.

Funding is where the bank looked most unusual. Uninsured deposits, balances above the government insurance limit, were 48.7% of deposits against a median of 24.2%. Core deposits, the stable everyday kind, were only 25.2% of assets against a median of 80.0%, while borrowings from the Federal Home Loan Bank, a lender to banks, were 12.1% of assets against 0.5%. Deposits changed by -35.5% over the past four quarters, compared with a median of 0.0%, even as assets grew 24.5%.

The bank also carried large paper losses on bonds it planned to hold until they mature, equal to 22.7% of equity against a national median of 0.0%. Its earnings were thin too, with a net interest margin (the spread earned on lending and investing) of 1.7% against a median of 3.5%.

## Understanding the score

First Republic Bank ranked 809 out of 4,740 banks as of 2023-03-31, at the 83.0th percentile on a scale from 0 to 100 where higher means riskier. The watchlist covers the top 2% of banks, which was 95 banks that quarter, and this bank was not flagged.

The five features that pushed the score up most were volatile funding at 53.0% of assets, commercial real estate loans at 7.0% of loans, core deposits at 25.2% of assets, loans at 165.1% of deposits, and equity at 7.7% of assets. The five that pulled it down most were the Tier 1 risk-based capital ratio at 11.7%, the Texas ratio (troubled assets against capital plus reserves) at 0.7%, loans 90+ days past due or not accruing at 0.1% of loans, nonaccrual assets and foreclosed property at 0.1% of assets, and return on equity at 6.1%. The downward pulls, driven by clean credit and adequate risk-based capital, were larger than the upward pushes from funding.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-06-30 | 1,327 | 5,015 |  |
| 2021-09-30 | 566 | 4,979 |  |
| 2021-12-31 | 948 | 4,904 |  |
| 2022-03-31 | 3,502 | 4,861 |  |
| 2022-06-30 | 3,262 | 4,838 |  |
| 2022-09-30 | 3,095 | 4,813 |  |
| 2022-12-31 | 3,355 | 4,773 |  |
| 2023-03-31 | 809 | 4,740 |  |

## Why the model missed it

In hindsight, this is a miss: the bank failed on 2023-05-01 while sitting outside the watchlist. The model learned from 539 failed banks, and 96% of them were credit-loss failures, where bad loans ate through capital. Only 53 of those had both credit losses and run risk, compared with 462 that were credit-loss only. First Republic's loans were clean, so the features that usually signal trouble pulled its score down.

On the Run-risk rank (post-hoc check, designed after the 2023 failures), the bank placed 895, so even that later check did not put it near the top. In the What-if (post-hoc check, designed after the 2023 failures) that set losses on bonds held to maturity to each value from 0.0% to 150.0%, the best rank reached was 809 of 4,740, at 0.0%, meaning these losses did not raise the score. In the What-if (post-hoc check, designed after the 2023 failures) for uninsured deposits from 0.0% to 100.0%, the best rank reached was 543 of 4,740, at 0.0%, and in the one for losses on bonds available for sale from 0.0% to 100.0%, it was 298 of 4,740, at 30.0%. None of these changes alone would have moved the bank onto the watchlist.

## What happened next

In hindsight, First Republic Bank failed on 2023-05-01. Its last reported quarter was 2023-03-31, so no later ranks exist; in our data, a bank that stops reporting was either merged or closed, and the two are not distinguished.

## Sources

- F1 · Bank name · n/a · First Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-03-31 · 809 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-03-31 · 4,740 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-03-31 · 83.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-03-31 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-03-31 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 8.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-03-31 · 11.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F49 · Bank: loans as a share of deposits · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F51 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 12.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 22.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2023-03-31 · $232.9 billion · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2023-03-31 · 24.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F73 · Bank: deposit growth over the past four quarters · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: volatile funding as a share of assets, value 53.0%; contribution to the score · 2023-03-31 · +0.357 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 7.0%; contribution to the score · 2023-03-31 · +0.306 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: core deposits as a share of assets, value 25.2%; contribution to the score · 2023-03-31 · +0.090 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: loans as a share of deposits, value 165.1%; contribution to the score · 2023-03-31 · +0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F79 · Driver up #5: equity as a share of assets, value 7.7%; contribution to the score · 2023-03-31 · +0.053 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.7%; contribution to the score · 2023-03-31 · -0.986 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 0.7%; contribution to the score · 2023-03-31 · -0.902 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2023-03-31 · -0.546 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2023-03-31 · -0.286 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 6.1%; contribution to the score · 2023-03-31 · -0.259 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2023-05-01 · 2023-05-01 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2023-03-31 · 895 · data/replay/replay_banks.csv: run_risk_rank
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 298 of 4,740, at 30.0% · 2023-03-31 · 298 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 809 of 4,740, at 0.0% · 2023-03-31 · 809 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F90 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 543 of 4,740, at 0.0% · 2023-03-31 · 543 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
