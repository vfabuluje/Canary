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
written_at: "2026-11-17T21:20:08"
writer_model: "claude-sonnet-5-5"
checked: true
---

# First Republic Bank (cert 59017)

*Hindsight: failed 2023-05-01. Canary did not flag it.*

## Summary

First Republic Bank, a California bank with $232.9 billion in assets, ranked 809 out of 4,740 banks on Canary's risk score as of 2023-03-31. That puts it at a percentile of 83.0%, with higher percentiles meaning higher risk. The bank was not flagged on the watchlist that quarter. Its funding relied far more on volatile sources than the typical bank's.

## Warning signs in the data

Capital was thinner than the national median: equity was 7.7% of assets against a median of 9.2%, and the Tier 1 risk-based capital ratio (core capital against risk-weighted assets) was 11.7% against 14.2%. The leverage ratio (core capital as a share of average assets) was 8.2% against a median of 10.4%.

Credit quality looked clean. Loans 90+ days past due or not accruing interest were 0.1% of loans, against a median of 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 0.7% against 1.7%. Loan-loss reserves were 0.5% of loans, below the median of 1.2%.

Funding and liquidity are where the data stands out. Loans were 165.1% of deposits against a median of 73.4%, and uninsured deposits (above the insurance limit) were 48.7% of deposits against 24.2%. Core deposits were 25.2% of assets against a median of 80.0%, and volatile funding was 53.0% of assets against 6.5%. Federal Home Loan Bank borrowings were 12.1% of assets against a median of 0.5%. Deposit growth over the past four quarters was -35.5%, against a median of 0.0%.

Losses on bonds held to maturity were 22.7% of equity, against a median of 0.0%. Profitability was weaker than typical, with a net interest margin (the spread earned on lending and investing) of 1.7% against a median of 3.5%.

## Understanding the score

The bank ranked 809 of 4,740 banks, at a percentile of 83.0%, with higher percentiles meaning higher risk. It was not flagged on the watchlist, which covers 2% of banks, or 95 banks that quarter.

Five features pushed the score up. The largest was volatile funding at 53.0% of assets (+0.357), followed by commercial real estate loans at 7.0% of loans (+0.306). Next came core deposits at 25.2% of assets (+0.090), loans as a share of deposits at 165.1% (+0.072), and equity as a share of assets at 7.7% (+0.053).

Five features pulled the score down, and by more. The Tier 1 risk-based capital ratio at 11.7% pulled it down most (-0.986), then the Texas ratio at 0.7% (-0.902). Loans 90+ days past due or not accruing interest at 0.1% of loans (-0.546), nonaccrual assets and foreclosed property at 0.1% of assets (-0.286), and return on equity at 6.1% (-0.259) followed.

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

Hindsight: the model missed this bank. Its 2023-03-31 rank of 809 did not place it on the watchlist. The model learned from 539 failed banks in the training period, and 96% of them were credit-loss failures. Of those, 462 had a credit-loss-only profile and 53 had both credit-loss and run-risk profiles. First Republic's loans were clean, so the model saw little of what it had learned to look for, while its funding strain was a run-risk pattern the training data showed less of.

A post-hoc check, designed after the 2023 failures, gave a run-risk rank of 895, which is not the model's result. In a what-if (post-hoc check, designed after the 2023 failures), setting losses on bonds available for sale to 30.0% of equity improved the best rank to 298 of 4,740. In another what-if (post-hoc check, designed after the 2023 failures), setting uninsured deposits to 0.0% of deposits gave a best rank of 543. In a third what-if (post-hoc check, designed after the 2023 failures), changing losses on bonds held to maturity did not improve the rank beyond 809.

## What happened next

Hindsight: the failure date recorded for First Republic Bank is 2023-05-01. The last quarter the bank reported was 2023-03-31, the same quarter as the score. So there is no later score for this bank in our data.

## Sources

- F1 · Bank name · n/a · First Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-03-31 · 809 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-03-31 · 4,740 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-03-31 · 83.0% · data/analyst/scores.parquet: percentile
- F9 · On the watchlist · 2023-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F10 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F11 · Banks on the watchlist that quarter · 2023-03-31 · 95 · data/analyst/scores.parquet: flagged
- F12 · Bank: equity as a share of assets · 2023-03-31 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F13 · National median: equity as a share of assets · 2023-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F14 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 8.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F15 · National median: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F16 · Bank: the Tier 1 risk-based capital ratio · 2023-03-31 · 11.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F17 · National median: the Tier 1 risk-based capital ratio · 2023-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F20 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F21 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F26 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F27 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F36 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 0.7% · data/features/fct_bank_features.parquet: texas_ratio
- F37 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F42 · Bank: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F43 · National median: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F48 · Bank: loans as a share of deposits · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F49 · National median: loans as a share of deposits · 2023-03-31 · 73.4% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F50 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F51 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F54 · Bank: core deposits as a share of assets · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F55 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F56 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 12.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F57 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F58 · Bank: volatile funding as a share of assets · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F59 · National median: volatile funding as a share of assets · 2023-03-31 · 6.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F62 · Bank: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 22.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F63 · National median: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F68 · Bank: total assets · 2023-03-31 · $232.9 billion · data/features/fct_bank_features.parquet: log_total_assets
- F72 · Bank: deposit growth over the past four quarters · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F73 · National median: deposit growth over the past four quarters · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F74 · Driver up #1: volatile funding as a share of assets, value 53.0%; contribution to the score · 2023-03-31 · +0.357 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F75 · Driver up #2: commercial real estate loans as a share of loans, value 7.0%; contribution to the score · 2023-03-31 · +0.306 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver up #3: core deposits as a share of assets, value 25.2%; contribution to the score · 2023-03-31 · +0.090 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #4: loans as a share of deposits, value 165.1%; contribution to the score · 2023-03-31 · +0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F78 · Driver up #5: equity as a share of assets, value 7.7%; contribution to the score · 2023-03-31 · +0.053 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.7%; contribution to the score · 2023-03-31 · -0.986 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F80 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 0.7%; contribution to the score · 2023-03-31 · -0.902 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2023-03-31 · -0.546 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2023-03-31 · -0.286 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #5: return on equity (profit as a share of equity), value 6.1%; contribution to the score · 2023-03-31 · -0.259 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Failure date · 2023-05-01 · 2023-05-01 · data/raw/failures: FAILDATE
- F85 · Last quarter the bank reported · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F86 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2023-03-31 · 895 · data/replay/replay_banks.csv: run_risk_rank
- F87 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 298 of 4,740, at 30.0% · 2023-03-31 · 298 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 809 of 4,740, at 0.0% · 2023-03-31 · 809 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 543 of 4,740, at 0.0% · 2023-03-31 · 543 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F90 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
