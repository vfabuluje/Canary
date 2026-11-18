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
written_at: "2026-11-17T21:19:02"
writer_model: "claude-opus-5-5"
checked: true
---

# First Republic Bank (cert 59017)

*Hindsight: failed 2023-05-01. Canary did not flag it.*

## Summary

As of Q1 2023, First Republic Bank, based in CA, ranked 809 out of 4,740 FDIC-insured banks on Canary's risk score, placing it at the 83.0% percentile, where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks by score. Its loan book looked clean, but its funding stood out: volatile funding, meaning money that can leave quickly, was 53.0% of assets against a national median of 6.5%, and uninsured deposits, balances above the government insurance limit, were 48.7% of deposits.

## Warning signs in the data

Capital, the bank's cushion against losses, was below typical levels: equity was 7.7% of assets against a national median of 9.2%, and the leverage ratio, core capital as a share of average assets, was 8.2% against 10.4%. Its Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 11.7% versus a median of 14.2%, and its total risk-based capital ratio was 12.7% versus 15.4%. Credit quality looked strong: seriously late loans or loans not paying interest were 0.1% of loans against a median of 0.2%, though loan-loss reserves, money set aside for bad loans, were a thin 0.5% of loans against 1.2%.

Funding was the clearest outlier: loans were 165.1% of deposits against a national median of 73.4%, and core deposits, the stable everyday kind, were only 25.2% of assets against 80.0%. Uninsured deposits were 48.7% of deposits versus a median of 24.2%, and borrowings from the Federal Home Loan Bank, a lender to banks, were 12.1% of assets versus 0.5%. Deposits shrank by -35.5% over the past four quarters while the median bank's were flat at 0.0%, even as assets grew 24.5% against a median of 1.5%.

Unrealized losses on bonds held to maturity, bonds the bank plans to keep until they repay, equaled 22.7% of equity against a national median of 0.0%, while losses on bonds available for sale were 2.0% of equity against 15.5%. Profitability was weak: the net interest margin, the spread earned on lending and investing, was 1.7% against a median of 3.5%, and return on assets was 0.5% against 1.0%.

## Understanding the score

In Q1 2023 the bank ranked 809 of 4,740 banks, at the 83.0% percentile. It was not flagged on the watchlist, which held 95 banks that quarter, the top 2% by score.

The five factors that pushed the score up most were volatile funding at 53.0% of assets, commercial real estate loans at 7.0% of loans, core deposits at 25.2% of assets, loans at 165.1% of deposits, and equity at 7.7% of assets. Their contributions to the score were +0.357, +0.306, +0.090, +0.072 and +0.053 respectively.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 11.7%, the Texas ratio, troubled assets against capital plus reserves, at 0.7%, seriously late or non-paying loans at 0.1% of loans, nonaccrual assets and foreclosed property at 0.1% of assets, and return on equity at 6.1%. Their contributions were -0.986, -0.902, -0.546, -0.286 and -0.259 respectively, so these reassuring signals outweighed the funding concerns.

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

In hindsight, this is a miss: the bank failed on 2023-05-01 while ranked 809 and off the watchlist. The model learned from 539 bank failures, and 96% of them were credit-loss failures, driven by bad loans. Of those, 462 had a credit-loss-only profile and just 53 combined credit losses with run risk, the danger of depositors pulling money fast. This bank had very clean loans, so the model's strongest signals pointed toward safety.

A separate run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 895, so even that measure did not single it out. In a what-if (post-hoc check, designed after the 2023 failures) that set uninsured deposits as a share of deposits to each value from 0.0% to 100.0% with other data unchanged, the best rank reached was 543 of 4,740, at 0.0%. In a what-if (post-hoc check, designed after the 2023 failures) that set losses on bonds held to maturity, as a share of equity to each value from 0.0% to 150.0%, the best rank reached stayed at 809 of 4,740, at 0.0%, showing the model gave those large losses little weight. In a what-if (post-hoc check, designed after the 2023 failures) for losses on bonds available for sale, as a share of equity from 0.0% to 100.0%, the best rank reached was 298 of 4,740, at 30.0%.

## What happened next

In hindsight, First Republic Bank failed on May 1, 2023. The last quarter it reported was 2023-03-31, so there are no later ranks or watchlist flags in our data. Our data records only that the bank stopped reporting; it does not distinguish a merger from a closure on its own.

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
- F18 · Bank: the total risk-based capital ratio · 2023-03-31 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F19 · National median: the total risk-based capital ratio · 2023-03-31 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F20 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F21 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F26 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F27 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F38 · Bank: return on assets (profit as a share of assets) · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F39 · National median: return on assets (profit as a share of assets) · 2023-03-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
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
- F64 · Bank: losses on bonds available for sale, as a share of equity · 2023-03-31 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F65 · National median: losses on bonds available for sale, as a share of equity · 2023-03-31 · 15.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F70 · Bank: asset growth over the past four quarters · 2023-03-31 · 24.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F71 · National median: asset growth over the past four quarters · 2023-03-31 · 1.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
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
