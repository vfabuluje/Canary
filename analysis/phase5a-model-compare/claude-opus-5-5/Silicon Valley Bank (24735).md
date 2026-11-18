---
cert: 24735
name: "Silicon Valley Bank"
as_of: 2022-12-31
rank: 3494
n_banks: 4773
percentile: 26.81751518960821
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-03-10
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T21:16:58"
writer_model: "claude-opus-5-5"
checked: true
---

# Silicon Valley Bank (cert 24735)

*Hindsight: failed 2023-03-10. Canary did not flag it.*

## Summary

As of 2022-12-31, Silicon Valley Bank, a California bank, ranked 3,494 out of 4,773 banks on Canary's risk score, placing it at the 26.8% percentile, where higher means riskier. It was not flagged on Canary's watchlist that quarter. Its loan book looked clean, but uninsured deposits (money above the government insurance limit) made up 86.4% of deposits against a national median of 25.5%. Paper losses on bonds it planned to hold until they repay equaled 98.1% of its equity (the owners' cushion), against a national median of 0.0%.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than typical on simple measures: equity was 7.4% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 8.0% against 10.3%. On the risk-weighted measure it looked stronger, with a Tier 1 risk-based capital ratio of 15.3% against a median of 14.2%. Credit quality was in line with peers: loans 90+ days past due or not accruing interest were 0.2% of loans, the same as the national median of 0.2%.

Funding stood out: uninsured deposits were 86.4% of deposits against a median of 25.5%, and deposits had shrunk by -8.4% over the past four quarters while the median bank grew 2.6%. The bank leaned more on borrowed money, with Federal Home Loan Bank borrowings at 7.2% of assets against a median of 0.3%, and volatile funding at 14.8% against 5.7%.

Securities, mostly bonds, made up 56.1% of assets against a median of 22.3%. Unrealized losses on bonds held to maturity equaled 98.1% of equity against a median of 0.0%, while losses on bonds available for sale were 16.3% of equity, close to the median of 18.6%. Its net interest margin (the spread earned on lending and investing) was 2.2% against a median of 3.4%.

## Understanding the score

For the quarter ending 2022-12-31, the bank ranked 3,494 of 4,773 banks, at the 26.8% percentile. The watchlist covers the top 2% of banks, which was 96 banks that quarter, and this bank was not flagged.

Five features pushed the score up: losses on bonds available for sale at 16.3% of equity (+0.804), the efficiency ratio (operating costs as a share of revenue) at 46.4% (+0.159), commercial real estate loans at 2.4% of loans (+0.118), equity at 7.4% of assets (+0.047), and construction loans at 0.6% of loans (+0.023).

Five features pulled it down more strongly: interest expense at 0.5% of assets (-1.065), the Tier 1 risk-based capital ratio at 15.3% (-1.054), the Texas ratio (troubled assets against capital plus reserves) at 0.9% (-0.987), securities at 56.1% of assets (-0.864), and return on equity at 13.4% (-0.506).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-03-31 | 1,263 | 5,044 |  |
| 2021-06-30 | 1,018 | 5,015 |  |
| 2021-09-30 | 1,142 | 4,979 |  |
| 2021-12-31 | 2,160 | 4,904 |  |
| 2022-03-31 | 3,638 | 4,861 |  |
| 2022-06-30 | 4,489 | 4,838 |  |
| 2022-09-30 | 3,640 | 4,813 |  |
| 2022-12-31 | 3,494 | 4,773 |  |

## Why the model missed it

In hindsight, the bank failed on March 10, 2023, while the model ranked it 3,494 of 4,773 in its last report. The model learned from 539 failed banks, and 96% of those were credit-loss failures, so it mainly looks for bad loans, which this bank did not show. Only 53 training failures combined credit losses with run risk, against 462 that were credit-loss only.

On the Run-risk rank (post-hoc check, designed after the 2023 failures), the bank placed 54, far nearer the top. In a What-if (post-hoc check, designed after the 2023 failures) setting losses on bonds held to maturity anywhere from 0.0% to 150.0% of equity, the best rank stayed at 3,494 of 4,773, so the model gave that loss no weight. In a What-if (post-hoc check, designed after the 2023 failures) varying uninsured deposits from 0.0% to 100.0%, the best rank reached was 3,019 of 4,773, at 0.0%. In a What-if (post-hoc check, designed after the 2023 failures) varying losses on bonds available for sale from 0.0% to 100.0% of equity, the best rank reached was 1,948 of 4,773, at 30.0%.

## What happened next

In hindsight, the bank's failure date is March 10, 2023. The last quarter it reported was 2022-12-31, so there are no later ranks or watchlist flags. Our data records only that the bank stopped reporting, which can mean a merger or a closure.

## Sources

- F1 · Bank name · n/a · Silicon Valley Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2022-12-31 · 3,494 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 26.8% · data/analyst/scores.parquet: percentile
- F9 · On the watchlist · 2022-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F10 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F11 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F12 · Bank: equity as a share of assets · 2022-12-31 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F13 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F14 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F15 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F16 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F17 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F20 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F21 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F42 · Bank: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F43 · National median: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F50 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 86.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F51 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F56 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F57 · National median: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F58 · Bank: volatile funding as a share of assets · 2022-12-31 · 14.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F59 · National median: volatile funding as a share of assets · 2022-12-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F62 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 98.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F63 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F64 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 16.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F65 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F66 · Bank: securities as a share of assets · 2022-12-31 · 56.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F67 · National median: securities as a share of assets · 2022-12-31 · 22.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F72 · Bank: deposit growth over the past four quarters · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F73 · National median: deposit growth over the past four quarters · 2022-12-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F74 · Driver up #1: losses on bonds available for sale, as a share of equity, value 16.3%; contribution to the score · 2022-12-31 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F75 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 46.4%; contribution to the score · 2022-12-31 · +0.159 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F76 · Driver up #3: commercial real estate loans as a share of loans, value 2.4%; contribution to the score · 2022-12-31 · +0.118 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #4: equity as a share of assets, value 7.4%; contribution to the score · 2022-12-31 · +0.047 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver up #5: construction loans as a share of loans, value 0.6%; contribution to the score · 2022-12-31 · +0.023 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #1: annualized interest expense as a share of assets, value 0.5%; contribution to the score · 2022-12-31 · -1.065 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #2: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2022-12-31 · -1.054 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.9%; contribution to the score · 2022-12-31 · -0.987 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #4: securities as a share of assets, value 56.1%; contribution to the score · 2022-12-31 · -0.864 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F83 · Driver down #5: return on equity (profit as a share of equity), value 13.4%; contribution to the score · 2022-12-31 · -0.506 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Failure date · 2023-03-10 · 2023-03-10 · data/raw/failures: FAILDATE
- F85 · Last quarter the bank reported · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F86 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2022-12-31 · 54 · data/replay/replay_banks.csv: run_risk_rank
- F87 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 1,948 of 4,773, at 30.0% · 2022-12-31 · 1,948 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 3,494 of 4,773, at 0.0% · 2022-12-31 · 3,494 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 3,019 of 4,773, at 0.0% · 2022-12-31 · 3,019 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F90 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
