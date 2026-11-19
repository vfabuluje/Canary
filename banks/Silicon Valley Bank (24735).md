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
written_at: "2026-11-18T19:44:34"
writer_model: "claude-opus-5-5"
checked: true
---

# Silicon Valley Bank (cert 24735)

*Hindsight: failed 2023-03-10. Canary did not flag it.*

## Summary

As of 2022-12-31, Canary's model ranked Silicon Valley Bank, a California bank, 3,494 out of 4,773 FDIC-insured banks, placing it in the 26.8th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks by score. Its loan quality looked ordinary, but 86.4% of its deposits were uninsured (above the government insurance limit), and losses on bonds it planned to hold until they repay equalled 98.1% of its equity, its owners' cushion against losses.

## Warning signs in the data

Capital was mixed: equity was 7.4% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 8.0% against a median of 10.3%, both below typical levels. By contrast, the Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are judged to be, was 15.3%, above the median of 14.2%. Credit quality looked clean: loans 90+ days past due or not accruing interest were 0.2% of loans, matching the median of 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 0.9% against a median of 1.8%.

Funding stood out: uninsured deposits were 86.4% of deposits, far above the national median of 25.5%. Deposit growth over the past four quarters was -8.4%, while the median bank's was 2.6%. Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 7.2% of assets against a median of 0.3%, and volatile funding (money that can leave quickly) was 14.8% of assets against a median of 5.7%.

Securities made up 56.1% of assets, well above the median of 22.3%. Losses on bonds held to maturity were 98.1% of equity, while the median bank showed 0.0%. Losses on bonds available for sale (bonds the bank could sell) were 16.3% of equity, slightly below the median of 18.6%, and its net interest margin (the spread earned on lending and investing) was 2.2% against a median of 3.4%.

## Understanding the score

As of 2022-12-31 the bank ranked 3,494 of 4,773 banks, the 26.8th percentile, where higher means riskier. It was not flagged on the watchlist, which held 96 banks that quarter, the top 2% by score.

The factor that pushed the score up most was losses on bonds available for sale, at 16.3% of equity, contributing +0.804. Next came a low efficiency ratio (operating costs as a share of revenue) of 46.4% at +0.159, commercial real estate loans at 2.4% of loans at +0.118, equity at 7.4% of assets at +0.047, and construction loans at 0.6% of loans at +0.023.

Five factors pulled the score down more strongly: interest expense at 0.5% of assets contributed -1.065, and the Tier 1 risk-based capital ratio of 15.3% contributed -1.054. The Texas ratio of 0.9% contributed -0.987, securities at 56.1% of assets contributed -0.864, and return on equity (profit as a share of equity) of 13.4% contributed -0.506. For context, the model was trained on 539 historical cases, and 96% of them were credit-loss cases, driven by bad loans.

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

## How its ratios moved

A year earlier the bank sat at the 56.0th percentile, and by 2022-12-31 it was at the 26.8th percentile with a rank of 3,494 of 4,773, so the model rated it safer than a year earlier. Each ratio is compared with its own values over the prior 12 quarters, and 11 of 30 ratios checked were outside that prior range.

Interest expense was 0.5% of assets, above its prior range of 0.0% to 0.3%, yet its contribution of -1.065 pushed the score down. Volatile funding was 14.8% of assets, above its prior range of 7.4% to 13.4% after rising +6.9 pp over four quarters, yet its contribution of -0.089 pushed the score down. Core deposits (stable, everyday deposits) were 76.6% of assets, below their prior range of 77.6% to 84.1%, yet their contribution of -0.048 had little effect on the score.

Asset growth was 0.2%, below its prior range of 11.6% to 97.9%, and its contribution of -0.116 pushed the score down. Deposit growth was -8.4%, below its prior range of 3.8% to 99.7%, and its contribution of -0.125 pushed the score down. Federal Home Loan Bank borrowings were 7.2% of assets, above their prior range of 0.0% to 6.4%, yet their contribution of -0.004 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 0.5% | 0.0% to 0.3% | same quarter, prior 3 years | n/a | +0.5 pp | -1.065 | pushed the score down |
| volatile funding as a share of assets | 14.8% | 7.4% to 13.4% | prior 12 quarters | +1.3 pp | +6.9 pp | -0.089 | pushed the score down |
| core deposits as a share of assets | 76.6% | 77.6% to 84.1% | prior 12 quarters | -1.5 pp | -7.4 pp | -0.048 | little effect on the score |
| asset growth over the past four quarters | 0.2% | 11.6% to 97.9% | prior 12 quarters | -11.4 pp | -83.0 pp | -0.116 | pushed the score down |
| deposit growth over the past four quarters | -8.4% | 3.8% to 99.7% | prior 12 quarters | -12.2 pp | -93.9 pp | -0.125 | pushed the score down |
| Federal Home Loan Bank borrowings as a share of assets | 7.2% | 0.0% to 6.4% | prior 12 quarters | +0.8 pp | +7.2 pp | -0.004 | little effect on the score |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on 2023-03-10, while the model had ranked it 3,494 of 4,773 and left it off the watchlist. The model learned mostly from loan-driven failures: of 539 training failures, 462 were credit-loss only and 53 combined credit losses with run risk (depositors pulling money quickly). This bank's loans looked healthy, so the patterns the model knew best did not fit it.

Its run-risk rank (post-hoc check, designed after the 2023 failures) was 54, much nearer the top than its model rank. In a What-if (post-hoc check, designed after the 2023 failures) that varied losses on bonds held to maturity from 0.0% to 150.0% of equity, the best rank reached was 3,494 of 4,773, at 0.0%, so these losses did not move its rank up. In a What-if (post-hoc check, designed after the 2023 failures) that varied uninsured deposits from 0.0% to 100.0% of deposits, the best rank reached was 3,019 of 4,773, at 0.0%, meaning the model did not treat more uninsured deposits as riskier. In a What-if (post-hoc check, designed after the 2023 failures) that varied losses on bonds available for sale from 0.0% to 100.0% of equity, the best rank reached was 1,948 of 4,773, at 30.0%, still well short of the watchlist.

## What happened next

In hindsight, the bank failed on 2023-03-10. The last quarter it reported was 2022-12-31, so there are no later ranks or watchlist flags in our data.

## Sources

- F1 · Bank name · n/a · Silicon Valley Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2022-12-31 · 3,494 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 26.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2022-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 0.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 86.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2022-12-31 · 14.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2022-12-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 98.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 16.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2022-12-31 · 56.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2022-12-31 · 22.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2022-12-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 16.3%; contribution to the score · 2022-12-31 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 46.4%; contribution to the score · 2022-12-31 · +0.159 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 2.4%; contribution to the score · 2022-12-31 · +0.118 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: equity as a share of assets, value 7.4%; contribution to the score · 2022-12-31 · +0.047 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: construction loans as a share of loans, value 0.6%; contribution to the score · 2022-12-31 · +0.023 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.5%; contribution to the score · 2022-12-31 · -1.065 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2022-12-31 · -1.054 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.9%; contribution to the score · 2022-12-31 · -0.987 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: securities as a share of assets, value 56.1%; contribution to the score · 2022-12-31 · -0.864 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 13.4%; contribution to the score · 2022-12-31 · -0.506 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2023-03-10 · 2023-03-10 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2022-12-31 · 54 · data/replay/replay_banks.csv: run_risk_rank
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 1,948 of 4,773, at 30.0% · 2022-12-31 · 1,948 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 3,494 of 4,773, at 0.0% · 2022-12-31 · 3,494 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F90 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 3,019 of 4,773, at 0.0% · 2022-12-31 · 3,019 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2022-12-31 · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -1.065 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2022-12-31 · 14.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F102 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F103 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F105 · Trend: volatile funding as a share of assets, change over four quarters, in percentage points · 2022-12-31 · +6.9 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F106 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.089 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F107 · Trend: volatile funding as a share of assets, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F108 · Trend: core deposits as a share of assets, value at the as-of quarter · 2022-12-31 · 76.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F109 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 77.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F110 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 84.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F113 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.048 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F114 · Trend: core deposits as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F115 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F116 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · 11.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F117 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 97.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F120 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.116 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F121 · Trend: asset growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F122 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F123 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 3.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F124 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 99.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F127 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F128 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F129 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F130 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F131 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 6.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F134 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.004 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F135 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F136 · Trend: ratios outside their own prior range · 2022-12-31 · 11 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 56.0% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
