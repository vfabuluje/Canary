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
written_at: "2026-11-18T19:45:02"
writer_model: "claude-opus-5-5"
checked: true
---

# First Republic Bank (cert 59017)

*Hindsight: failed 2023-05-01. Canary did not flag it.*

## Summary

As of 2023-03-31, First Republic Bank, a bank based in CA, ranked 809 out of 4,740 FDIC-insured banks on Canary's risk score, placing it in the 83.0th percentile, where higher means riskier. It was not on the watchlist, which covers the top 2% of banks by score. Its funding stood out: volatile funding (money that can leave the bank quickly) made up 53.0% of assets, far above the national median of 6.5%, and its capital cushion was thinner than the typical bank's. Its loan book, by contrast, showed very few problem loans.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below the national median on every measure: equity was 7.7% of assets against a median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 8.2% against 10.4%. Its Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 11.7% against a median of 14.2%, and its total risk-based capital ratio was 12.7% against 15.4%. Credit quality looked clean: loans 90+ days past due or not accruing interest were 0.1% of loans against a median of 0.2%, though loan-loss reserves (money set aside for bad loans) were a thin 0.5% of loans against a median of 1.2%.

Funding was the weak spot: core deposits, the stable everyday deposits, were only 25.2% of assets against a national median of 80.0%, and deposits shrank by -35.5% over the past four quarters while the median was 0.0%. Loans equaled 165.1% of deposits against a median of 73.4%, and uninsured deposits (balances above the federal insurance limit) were 48.7% of deposits against 24.2%. The bank leaned on other sources: brokered deposits (funds placed through middlemen) were 6.8% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 12.1% of assets against 0.5%. Its interest expense was 1.7% of assets against a median of 0.8%, and its net interest margin (the spread earned on lending and investing) was 1.7% against 3.5%.

On bonds, paper losses on bonds held to maturity equaled 22.7% of equity, far above the national median of 0.0%, while losses on bonds available for sale were 2.0% of equity against a median of 15.5%.

## Understanding the score

First Republic Bank ranked 809 of 4,740 banks as of 2023-03-31, in the 83.0th percentile on a scale from 0 to 100 where higher means riskier. It was not flagged on the watchlist, which holds the top 2% of banks and had 95 banks that quarter.

Five features pushed the score up the most, led by volatile funding at 53.0% of assets, which added +0.357. Next came commercial real estate loans at 7.0% of loans, adding +0.306, and core deposits at 25.2% of assets, adding +0.090. Loans at 165.1% of deposits added +0.072, and equity at 7.7% of assets added +0.053.

Five features pulled the score down, led by the Tier 1 risk-based capital ratio at 11.7%, which subtracted -0.986. The Texas ratio (troubled assets against capital plus reserves) at 0.7% subtracted -0.902, and loans 90+ days past due or not accruing interest at 0.1% of loans subtracted -0.546. Nonaccrual assets and foreclosed property at 0.1% of assets subtracted -0.286, and return on equity (profit as a share of equity) at 6.1% subtracted -0.259.

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

## How its ratios moved

The bank sat in the 83.0th percentile as of 2023-03-31, up from the 28.0th percentile at 2022-03-31, so the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, 13 were outside it, and the 6 furthest outside are discussed here. Most ratios are compared with the prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years.

Volatile funding was 53.0% of assets, far above its prior range of 2.4% to 11.4% after rising +41.6 pp in one quarter, and its contribution of +0.357 pushed the score up. Loans as a share of deposits reached 165.1%, above its prior range of 85.9% to 101.5%, and its contribution of +0.072 pushed the score up. Core deposits fell to 25.2% of assets, below its prior range of 68.5% to 84.0%, and its contribution of +0.090 pushed the score up.

Deposit growth was -35.5%, well below its prior range of 12.9% to 39.2%, yet its contribution of -0.136 pushed the score down. Uninsured deposits were 48.7% of deposits, below their prior range of 65.0% to 74.7%, and their contribution of -0.038 had little effect on the score. Brokered deposits were 6.8% of deposits, above their prior range of 0.4% to 3.0%, yet their contribution of -0.110 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| volatile funding as a share of assets | 53.0% | 2.4% to 11.4% | prior 12 quarters | +41.6 pp | +50.6 pp | +0.357 | pushed the score up |
| loans as a share of deposits | 165.1% | 85.9% to 101.5% | prior 12 quarters | +71.0 pp | +78.4 pp | +0.072 | pushed the score up |
| core deposits as a share of assets | 25.2% | 68.5% to 84.0% | prior 12 quarters | -48.3 pp | -58.9 pp | +0.090 | pushed the score up |
| deposit growth over the past four quarters | -35.5% | 12.9% to 39.2% | prior 12 quarters | -48.4 pp | -62.2 pp | -0.136 | pushed the score down |
| uninsured deposits as a share of deposits | 48.7% | 65.0% to 74.7% | prior 12 quarters | -19.0 pp | -24.9 pp | -0.038 | little effect on the score |
| brokered deposits as a share of deposits | 6.8% | 0.4% to 3.0% | prior 12 quarters | +3.8 pp | +6.2 pp | -0.110 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on 2023-05-01, while its last ranking of 809 kept it outside the watchlist of the top 2% of banks. The model learned from 539 failed banks, and 96% of those were credit-loss failures, driven by bad loans. Of those, 462 were credit-loss only and 53 combined credit losses with run-risk, so a bank with a clean loan book but fragile funding looked unlike most past failures. Its strong capital ratios and very low problem loans pulled its score down, offsetting the funding signals that pushed it up.

The Run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 895, so even that later measure did not rank it near the top. In a What-if (post-hoc check, designed after the 2023 failures) setting losses on bonds available for sale, as a share of equity to each value from 0.0% to 100.0%, other data unchanged, the best rank reached was 298 of 4,740, at 30.0%. In a What-if (post-hoc check, designed after the 2023 failures) setting losses on bonds held to maturity, as a share of equity to each value from 0.0% to 150.0%, other data unchanged, the best rank reached was 809 of 4,740, at 0.0%, meaning those losses did not move the rank higher. In a What-if (post-hoc check, designed after the 2023 failures) setting uninsured deposits as a share of deposits to each value from 0.0% to 100.0%, other data unchanged, the best rank reached was 543 of 4,740, at 0.0%.

## What happened next

In hindsight, First Republic Bank failed on May 1, 2023. Its last reported quarter was Q1 2023, so there are no later ranks or watchlist flags; in our data a bank that stops reporting may have merged or closed, and the two are not distinguished.

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
- F19 · Bank: the total risk-based capital ratio · 2023-03-31 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-03-31 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2023-03-31 · 0.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2023-03-31 · 73.4% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2023-03-31 · 6.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 12.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-03-31 · 6.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 22.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-03-31 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-03-31 · 15.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
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
- F95 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F96 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F97 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F98 · Trend: volatile funding as a share of assets, change over one quarter, in percentage points · 2023-03-31 · +41.6 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F100 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · +0.357 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F101 · Trend: volatile funding as a share of assets, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F102 · Trend: loans as a share of deposits, value at the as-of quarter · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F103 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 85.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F104 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 101.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F107 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · +0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F108 · Trend: loans as a share of deposits, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F109 · Trend: core deposits as a share of assets, value at the as-of quarter · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F110 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 68.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F111 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 84.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F114 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · +0.090 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F115 · Trend: core deposits as a share of assets, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F116 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F117 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F118 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F121 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2023-03-31 · -0.136 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F122 · Trend: deposit growth over the past four quarters, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F123 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F124 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 65.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F125 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 74.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F128 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · -0.038 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F129 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F130 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2023-03-31 · 6.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F131 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F132 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F135 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · -0.110 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F136 · Trend: brokered deposits as a share of deposits, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F137 · Trend: ratios outside their own prior range · 2023-03-31 · 13 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-03-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2023-03-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2022-03-31 · 28.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2023-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
