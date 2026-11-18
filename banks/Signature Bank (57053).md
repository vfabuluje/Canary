---
cert: 57053
name: "Signature Bank"
as_of: 2022-12-31
rank: 246
n_banks: 4773
percentile: 94.86695998323906
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-03-12
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:05:12"
writer_model: "claude-opus-5-5"
checked: true
---

# Signature Bank (cert 57053)

*Hindsight: failed 2023-03-12. Canary did not flag it.*

## Summary

As of 2022-12-31, Signature Bank, based in NY, ranked 246 of 4,773 banks nationally on Canary's risk score, placing it in the 94.9th percentile. It was not flagged for the watchlist, which covers the top 2% of banks. Its most unusual figures were a very high share of uninsured deposits (money above the government insurance limit), at 89.7% against a national median of 25.5%, and large paper losses on its bonds.

## Warning signs in the data

Capital, the bank's cushion against losses, was thinner than at a typical bank: equity was 7.3% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 8.8% against 10.3%. Its Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 11.2% against a median of 14.2%, and its total risk-based capital ratio was 12.3% against 15.3%. Loan quality looked fairly normal: loans 90+ days past due or not accruing interest were 0.3% of loans against a median of 0.2%, though loan-loss reserves (money set aside for bad loans) were lower, at 0.7% against 1.2%.

Funding stood out most: uninsured deposits were 89.7% of deposits, far above the national median of 25.5%, and deposits shrank by -16.5% over the past four quarters while the median bank grew 2.6%. The bank also leaned more on borrowed money, with Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) at 10.2% of assets against a median of 0.3%, and volatile funding at 14.7% against 5.7%.

Unrealized losses on bonds available for sale (bonds the bank may sell, now worth less than it paid) equaled 30.6% of equity, well above the median of 18.6%. Losses on bonds held to maturity (bonds the bank plans to keep) equaled 9.5% of equity, while the median bank showed 0.0%.

## Understanding the score

Signature Bank ranked 246 of 4,773 banks on 2022-12-31, the 94.9th percentile on a scale of 0 to 100 where higher means riskier. The watchlist holds the top 2% of banks, 96 banks that quarter, and this bank was not flagged.

The five features pushing the score up most were losses on bonds available for sale at 30.6% of equity, by far the largest at +2.063; the efficiency ratio (operating costs as a share of revenue) at 32.0%; asset growth of -6.8%; equity at 7.3% of assets; and net interest margin (the spread earned on lending and investing) at 2.2%.

The five features pulling the score down most were interest expense at 0.9% of assets; the Texas ratio (troubled assets against capital plus reserves) at 2.8%; the Tier 1 risk-based capital ratio at 11.2%; return on equity (profit as a share of equity) at 16.8%; and loans 90+ days past due or not accruing at 0.3% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-03-31 | 1,022 | 5,044 |  |
| 2021-06-30 | 831 | 5,015 |  |
| 2021-09-30 | 913 | 4,979 |  |
| 2021-12-31 | 986 | 4,904 |  |
| 2022-03-31 | 2,456 | 4,861 |  |
| 2022-06-30 | 2,162 | 4,838 |  |
| 2022-09-30 | 420 | 4,813 |  |
| 2022-12-31 | 246 | 4,773 |  |

## Why the model missed it

In hindsight, Signature Bank failed on 2023-03-12, while the model had ranked it 246, outside the 96 banks on the watchlist that quarter. The model learned mostly from credit-loss failures: 96% of the 539 failed banks in its training period failed from bad loans, and only 53 combined credit losses with run risk (depositors pulling money quickly). This bank's loan problems were small, so the features that usually signal trouble pulled its score down.

The run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 247, so even this measure did not put it near the top. In a what-if (post-hoc check, designed after the 2023 failures) setting uninsured deposits from 0.0% to 100.0% with other data unchanged, the best rank reached was 154 of 4,773, at 0.0%, showing the model did not treat a high uninsured share as a danger sign. A similar what-if (post-hoc check, designed after the 2023 failures) for losses on bonds held to maturity, from 0.0% to 150.0%, reached a best rank of 134 of 4,773, at 0.0%, and one for losses on bonds available for sale, from 0.0% to 100.0%, reached a best rank of 246, at 30.0%.

## What happened next

In hindsight, Signature Bank failed on 2023-03-12, shortly after the as-of date. The last quarter it reported was 2022-12-31, so there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Signature Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2022-12-31 · 246 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 94.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2022-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 11.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2022-12-31 · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2022-12-31 · 0.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2022-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 89.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 10.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2022-12-31 · 14.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2022-12-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 9.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 30.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2022-12-31 · -16.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2022-12-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 30.6%; contribution to the score · 2022-12-31 · +2.063 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 32.0%; contribution to the score · 2022-12-31 · +0.186 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: asset growth over the past four quarters, value -6.8%; contribution to the score · 2022-12-31 · +0.101 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F78 · Driver up #4: equity as a share of assets, value 7.3%; contribution to the score · 2022-12-31 · +0.029 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: net interest margin (the spread earned on lending and investing), value 2.2%; contribution to the score · 2022-12-31 · +0.009 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.9%; contribution to the score · 2022-12-31 · -0.854 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 2.8%; contribution to the score · 2022-12-31 · -0.793 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: the Tier 1 risk-based capital ratio, value 11.2%; contribution to the score · 2022-12-31 · -0.672 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 16.8%; contribution to the score · 2022-12-31 · -0.392 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.3%; contribution to the score · 2022-12-31 · -0.342 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F85 · Failure date · 2023-03-12 · 2023-03-12 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2022-12-31 · 247 · data/replay/replay_banks.csv: run_risk_rank
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 246 of 4,773, at 30.0% · 2022-12-31 · 246 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 134 of 4,773, at 0.0% · 2022-12-31 · 134 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F90 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 154 of 4,773, at 0.0% · 2022-12-31 · 154 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
