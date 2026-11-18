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
written_at: "2026-11-17T21:17:47"
writer_model: "claude-opus-5-5"
checked: true
---

# Signature Bank (cert 57053)

*Hindsight: failed 2023-03-12. Canary did not flag it.*

## Summary

As of 2022-12-31, Signature Bank (certificate 57053, based in NY) ranked 246 out of 4,773 FDIC-insured banks on Canary's risk score, a percentile of 94.9%. It was not flagged on Canary's watchlist, which covers the top 2% of banks. Its most unusual features were large paper losses on its bonds, a very high share of deposits above the insurance limit, and thinner capital than a typical bank, while its loans showed few signs of trouble.

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, was below typical levels: equity was 7.3% of assets against a national median of 9.0%. The leverage ratio (core capital as a share of average assets) was 8.8% against a median of 10.3%, and the Tier 1 risk-based capital ratio was 11.2% against a median of 14.2%. Credit quality looked close to normal: loans 90+ days past due or not accruing interest were 0.3% of loans against a median of 0.2%, though loan-loss reserves, money set aside for bad loans, were 0.7% of loans against a median of 1.2%.

Funding stood out most: uninsured deposits, balances above the FDIC insurance limit, were 89.7% of deposits, far above the national median of 25.5%. Deposits shrank by -16.5% over the past four quarters, while the median bank grew deposits by 2.6%. The bank leaned more on borrowed and less stable money, with Federal Home Loan Bank borrowings at 10.2% of assets against a median of 0.3%, and volatile funding at 14.7% of assets against a median of 5.7%.

Unrealized losses on bonds available for sale, meaning drops in market value not yet booked as losses, equaled 30.6% of equity, well above the median of 18.6%. Losses on bonds held to maturity equaled 9.5% of equity, while the median bank had 0.0%.

## Understanding the score

On 2022-12-31 Signature Bank ranked 246 of 4,773 banks, a percentile of 94.9%, where higher percentiles mean higher risk. It was not on the watchlist, which held 96 banks that quarter, the top 2% by score.

The five features that pushed its score up most were losses on bonds available for sale at 30.6% of equity (+2.063), a low efficiency ratio, meaning operating costs as a share of revenue, of 32.0% (+0.186), asset growth of -6.8% (+0.101), equity at 7.3% of assets (+0.029), and a net interest margin, the spread earned on lending and investing, of 2.2% (+0.009).

The five features that pulled its score down most were interest expense at 0.9% of assets (-0.854), a Texas ratio, troubled assets against capital plus reserves, of 2.8% (-0.793), a Tier 1 risk-based capital ratio of 11.2% (-0.672), return on equity of 16.8% (-0.392), and loans 90+ days past due or not accruing at 0.3% of loans (-0.342).

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

In hindsight, Signature Bank failed on 2023-03-12, yet at its last pre-failure rank of 246 it sat outside the watchlist of 96 banks. The model learned mostly from credit-loss failures: of 539 failed banks in its training period, 96% were credit-loss failures, with 462 showing credit losses only and just 53 combining credit losses with run risk, the danger of depositors pulling money quickly. This bank's loans looked healthy, so the patterns the model knew best did not fire strongly.

The Run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 247, so even this later check did not put it near the top. In the What-if (post-hoc check, designed after the 2023 failures) that set uninsured deposits as a share of deposits to each value from 0.0% to 100.0%, the best rank reached was only 154 of 4,773, at 0.0%, showing the model gave little weight to uninsured deposits. Similar What-if (post-hoc check, designed after the 2023 failures) tests reached a best rank of 246 of 4,773 at 30.0% for losses on bonds available for sale, and 134 of 4,773 at 0.0% for losses on bonds held to maturity, both still outside the watchlist.

## What happened next

In hindsight, Signature Bank failed on 2023-03-12. Its last reported quarter was 2022-12-31, so there are no later ranks or watchlist flags in our data. The bank stopped reporting after that point; our data does not distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Signature Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 57053 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2022-12-31 · 246 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 94.9% · data/analyst/scores.parquet: percentile
- F9 · On the watchlist · 2022-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F10 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F11 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F12 · Bank: equity as a share of assets · 2022-12-31 · 7.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F13 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F14 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F15 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F16 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 11.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F17 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F20 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F21 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F26 · Bank: loan-loss reserves as a share of loans · 2022-12-31 · 0.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F27 · National median: loan-loss reserves as a share of loans · 2022-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F50 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 89.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F51 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F56 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 10.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F57 · National median: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F58 · Bank: volatile funding as a share of assets · 2022-12-31 · 14.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F59 · National median: volatile funding as a share of assets · 2022-12-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F62 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 9.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F63 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F64 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 30.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F65 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F72 · Bank: deposit growth over the past four quarters · 2022-12-31 · -16.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F73 · National median: deposit growth over the past four quarters · 2022-12-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F74 · Driver up #1: losses on bonds available for sale, as a share of equity, value 30.6%; contribution to the score · 2022-12-31 · +2.063 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F75 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 32.0%; contribution to the score · 2022-12-31 · +0.186 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F76 · Driver up #3: asset growth over the past four quarters, value -6.8%; contribution to the score · 2022-12-31 · +0.101 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F77 · Driver up #4: equity as a share of assets, value 7.3%; contribution to the score · 2022-12-31 · +0.029 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver up #5: net interest margin (the spread earned on lending and investing), value 2.2%; contribution to the score · 2022-12-31 · +0.009 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F79 · Driver down #1: annualized interest expense as a share of assets, value 0.9%; contribution to the score · 2022-12-31 · -0.854 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 2.8%; contribution to the score · 2022-12-31 · -0.793 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #3: the Tier 1 risk-based capital ratio, value 11.2%; contribution to the score · 2022-12-31 · -0.672 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #4: return on equity (profit as a share of equity), value 16.8%; contribution to the score · 2022-12-31 · -0.392 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.3%; contribution to the score · 2022-12-31 · -0.342 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Failure date · 2023-03-12 · 2023-03-12 · data/raw/failures: FAILDATE
- F85 · Last quarter the bank reported · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F86 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2022-12-31 · 247 · data/replay/replay_banks.csv: run_risk_rank
- F87 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 246 of 4,773, at 30.0% · 2022-12-31 · 246 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 134 of 4,773, at 0.0% · 2022-12-31 · 134 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 154 of 4,773, at 0.0% · 2022-12-31 · 154 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F90 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
