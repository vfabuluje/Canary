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
written_at: "2026-11-18T19:45:02"
writer_model: "claude-opus-5-5"
checked: true
---

# Signature Bank (cert 57053)

*Hindsight: failed 2023-03-12. Canary did not flag it.*

## Summary

As of 2022-12-31, Signature Bank in NY ranked 246 out of 4,773 FDIC-insured banks on Canary's risk score, placing it in the 94.9th percentile on a 0 to 100 scale where higher means riskier. That placed it high in the national ranking, but not on the watchlist, which covers the top 2% of banks, or 96 banks that quarter. The biggest factor raising its score was losses on bonds available for sale (bonds the bank may sell before they mature), equal to 30.6% of its equity, against a national median of 18.6%. Its funding also stood out: 89.7% of its deposits were uninsured (above the government insurance limit), far above the national median of 25.5%.

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, was thinner than at a typical bank: equity was 7.3% of assets against a national median of 9.0%. The leverage ratio (core capital as a share of average assets) was 8.8% against a median of 10.3%, and the Tier 1 risk-based capital ratio (core capital against risk-weighted assets) was 11.2% against 14.2%. Loan quality looked close to normal, with loans 90+ days past due or not accruing interest at 0.3% of loans against a median of 0.2%, though loan-loss reserves (money set aside for bad loans) were only 0.7% of loans against a median of 1.2%.

Funding was the most unusual area: uninsured deposits made up 89.7% of deposits, against a national median of 25.5%. Deposit growth over the past four quarters was -16.5%, while the national median was 2.6%. The bank leaned more on borrowed money, with Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) at 10.2% of assets against a median of 0.3%, and volatile funding (money that can leave quickly) at 14.7% of assets against 5.7%.

Bond losses were large relative to its capital: losses on bonds available for sale equaled 30.6% of equity against a median of 18.6%. Losses on bonds held to maturity (bonds the bank plans to keep until they pay out) equaled 9.5% of equity, while the national median was 0.0%.

## Understanding the score

Signature Bank ranked 246 of 4,773 banks as of 2022-12-31, the 94.9th percentile, where 100 is the highest risk. It was not flagged on the watchlist, which holds the top 2% of banks, or 96 banks that quarter.

Five factors pushed its score up the most. The largest by far was losses on bonds available for sale at 30.6% of equity, contributing +2.063. Next came the efficiency ratio (operating costs as a share of revenue) at 32.0%, contributing +0.186, and asset growth over the past four quarters of -6.8%, contributing +0.101. Equity at 7.3% of assets added +0.029, and the net interest margin (the spread earned on lending and investing) of 2.2% added +0.009.

Five factors pulled its score down the most. Annualized interest expense at 0.9% of assets contributed -0.854, and the Texas ratio (troubled assets against capital plus reserves) at 2.8% contributed -0.793. The Tier 1 risk-based capital ratio of 11.2% contributed -0.672, return on equity (profit as a share of equity) of 16.8% contributed -0.392, and loans 90+ days past due or not accruing interest at 0.3% of loans contributed -0.342.

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

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared this way, 8 sat outside their own prior range, and the 6 furthest outside are discussed here. Overall, the model rated it riskier than a year earlier: the bank was at the 79.9th percentile on 2021-12-31 and the 94.9th percentile on 2022-12-31.

Return on equity was 16.8%, above its prior range of 10.5% to 13.2% and up +3.6 pp over four quarters, with a contribution of -0.392 model log-odds units that pushed the score down. The efficiency ratio was 32.0%, below its prior range of 35.4% to 40.0% and down -3.3 pp over four quarters, with a contribution of +0.186 model log-odds units that pushed the score up.

Volatile funding was 14.7% of assets, well above its prior range of 2.6% to 9.9% after a +11.1 pp jump in one quarter, yet its contribution of -0.115 model log-odds units pushed the score down. Brokered deposits (deposits placed through middlemen) were 4.3% of deposits, above their prior range of 1.2% to 3.4%, yet their contribution of -0.182 model log-odds units pushed the score down. Deposit growth was -16.5%, below its prior range of 7.5% to 75.9% after a -84.2 pp change over four quarters, yet its contribution of -0.112 model log-odds units pushed the score down. Federal Home Loan Bank borrowings were 10.2% of assets, above their prior range of 1.3% to 8.3% after a +9.0 pp rise in one quarter, yet with a contribution of -0.007 model log-odds units they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 16.8% | 10.5% to 13.2% | same quarter, prior 3 years | n/a | +3.6 pp | -0.392 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 32.0% | 35.4% to 40.0% | same quarter, prior 3 years | n/a | -3.3 pp | +0.186 | pushed the score up |
| volatile funding as a share of assets | 14.7% | 2.6% to 9.9% | prior 12 quarters | +11.1 pp | +11.3 pp | -0.115 | pushed the score down |
| brokered deposits as a share of deposits | 4.3% | 1.2% to 3.4% | prior 12 quarters | +1.9 pp | +3.1 pp | -0.182 | pushed the score down |
| deposit growth over the past four quarters | -16.5% | 7.5% to 75.9% | prior 12 quarters | -24.1 pp | -84.2 pp | -0.112 | pushed the score down |
| Federal Home Loan Bank borrowings as a share of assets | 10.2% | 1.3% to 8.3% | prior 12 quarters | +9.0 pp | +8.0 pp | -0.007 | little effect on the score |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

Hindsight: Signature Bank failed on 2023-03-12, while the model had ranked it 246 of 4,773 and left it off the watchlist of 96 banks. The model learned from past failures, and 96% of the 539 failed banks in its training period were credit-loss failures, meaning bad loans drove them. Of those, 462 had a credit-loss-only profile and just 53 combined credit losses with run-risk, the risk that depositors pull money quickly. Signature Bank's loans looked fairly healthy, so the model had few cases like it to learn from.

Hindsight: the Run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 247, close to its model rank, so this check would not have singled it out either. In the What-if (post-hoc check, designed after the 2023 failures) that set uninsured deposits as a share of deposits to each value from 0.0% to 100.0%, the best rank reached was 154 of 4,773, at 0.0%, so the model ranked the bank riskier with fewer uninsured deposits, not more. In the What-if (post-hoc check, designed after the 2023 failures) that set losses on bonds held to maturity, as a share of equity to each value from 0.0% to 150.0%, the best rank reached was 134 of 4,773, at 0.0%. In the What-if (post-hoc check, designed after the 2023 failures) that set losses on bonds available for sale, as a share of equity to each value from 0.0% to 100.0%, the best rank reached was 246 of 4,773, at 30.0%.

## What happened next

Hindsight: Signature Bank failed on 2023-03-12. The last quarter it reported was 2022-12-31, so no later ranks or watchlist flags exist for it. In our data, a bank that stops reporting may have merged or closed, and the data does not distinguish between the two.

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
- F93 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2022-12-31 · 16.8% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 10.5% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.2% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2022-12-31 · +3.6 pp · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2022-12-31 · -0.392 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2022-12-31 · 32.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 35.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 40.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2022-12-31 · -3.3 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2022-12-31 · +0.186 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2022-12-31 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F107 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2022-12-31 · 14.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F108 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F109 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 9.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F110 · Trend: volatile funding as a share of assets, change over one quarter, in percentage points · 2022-12-31 · +11.1 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F112 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.115 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F113 · Trend: volatile funding as a share of assets, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F114 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2022-12-31 · 4.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F119 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2022-12-31 · -0.182 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F120 · Trend: brokered deposits as a share of deposits, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F121 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2022-12-31 · -16.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F122 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 7.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F123 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 75.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F125 · Trend: deposit growth over the past four quarters, change over four quarters, in percentage points · 2022-12-31 · -84.2 pp · data/features/fct_bank_features.parquet: deposit_growth_4q
- F126 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.112 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F127 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F128 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2022-12-31 · 10.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F129 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F130 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F131 · Trend: Federal Home Loan Bank borrowings as a share of assets, change over one quarter, in percentage points · 2022-12-31 · +9.0 pp · data/features/fct_bank_features.parquet: fhlb_to_assets
- F133 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.007 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F134 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F135 · Trend: ratios outside their own prior range · 2022-12-31 · 8 · data/features/fct_bank_features.parquet
- F136 · Trend: ratios shown in the table (the furthest outside their prior range) · 2022-12-31 · 6 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 79.9% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
