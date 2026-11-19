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
written_at: "2026-11-19T14:04:14"
writer_model: "claude-opus-5-5"
checked: true
---

# Signature Bank (cert 57053)

*Hindsight: failed 2023-03-12. Canary did not flag it.*

## Summary

As of 2022-12-31, Signature Bank (certificate 57053, based in NY) ranked 246 of 4,773 banks on Canary's risk score, which puts it in the 94.9th percentile on a scale where higher means riskier. It was not flagged on the watchlist, which held 96 banks that quarter, about 2% of all banks. The biggest factor raising its score was paper losses on bonds held for possible sale, equal to 30.6% of its equity, well above the national median of 18.6%. Its uninsured deposits (balances above the government insurance limit) made up 89.7% of deposits, far above the national median of 25.5%.

## Warning signs in the data

Capital, the cushion of owners' money that absorbs losses, was thinner than at a typical bank. Equity was 7.3% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 8.8% against 10.3%. The Tier 1 risk-based capital ratio was 11.2% against a median of 14.2%, and the total risk-based capital ratio was 12.3% against 15.3%.

Loan problems were small: loans 90+ days past due or not accruing interest were 0.3% of loans, close to the national median of 0.2%. Reserves set aside for loan losses were 0.7% of loans, below the median of 1.2%, and the Texas ratio (troubled assets against capital plus reserves) was 2.8% against a median of 1.8%.

Funding stood out most: uninsured deposits were 89.7% of deposits against a national median of 25.5%, and deposits shrank by -16.5% over the past four quarters while the median bank grew 2.6%. Borrowings from the Federal Home Loan Bank (a lender to banks) were 10.2% of assets against a median of 0.3%, and volatile funding was 14.7% of assets against 5.7%. Unrealized losses on bonds available for sale equaled 30.6% of equity against a median of 18.6%, and losses on bonds held to maturity equaled 9.5% of equity against a median of 0.0%.

## Understanding the score

At 2022-12-31 the bank ranked 246 of 4,773 banks, the 94.9th percentile, with a model score of 0.0296. It was not flagged on the watchlist, which covered 96 banks, about 2% of the total.

The five factors that pushed the score up were: losses on bonds available for sale at 30.6% of equity (+2.063), the efficiency ratio (operating costs as a share of revenue) at 32.0% (+0.186), asset growth of -6.8% (+0.101), equity at 7.3% of assets (+0.029), and net interest margin (the spread earned on lending and investing) at 2.2% (+0.009).

The five factors that pushed the score down were: interest expense at 0.9% of assets (-0.854), the Texas ratio at 2.8% (-0.793), the Tier 1 risk-based capital ratio at 11.2% (-0.672), return on equity (profit as a share of equity) at 16.8% (-0.392), and seriously late or non-paying loans at 0.3% of loans (-0.342).

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

Canary compared 30 of the bank's ratios with their own history over the prior 12 quarters (or, for year-to-date ratios, the same quarter in the prior 3 years); 8 fell outside their prior range, and the 6 furthest outside are shown in the table. The model rated it riskier than a year earlier, with its percentile moving from the 79.9th at 2021-12-31 to the 94.9th at 2022-12-31.

Return on equity was 16.8%, above its prior range of 10.5% to 13.2% after a +3.6 pp change over four quarters, and it pushed the score down with a contribution of -0.392. The efficiency ratio was 32.0%, below its prior range of 35.4% to 40.0%, and it pushed the score up with a contribution of +0.186.

Volatile funding was 14.7% of assets, well above its prior range of 2.6% to 9.9% after a +11.1 pp jump in one quarter, yet it pushed the score down with a contribution of -0.115. Brokered deposits (deposits placed through middlemen) were 4.3% of deposits, above their prior range of 1.2% to 3.4%, yet they pushed the score down with a contribution of -0.182. Deposit growth was -16.5%, below its prior range of 7.5% to 75.9%, yet it pushed the score down with a contribution of -0.112. Federal Home Loan Bank borrowings were 10.2% of assets, above their prior range of 1.3% to 8.3%, yet they had little effect on the score, with a contribution of -0.007.

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

## Compared with similar banks

The FDIC's specialty group for this bank at 2022-12-31: Commercial Lending Specialization.

Peers: 113 banks in the same specialty group and size tier (over $10 billion).

Uninsured deposits were 89.7% of deposits, at the 99.7th national percentile, which is unusually high, and at the 99.6th percentile among peers against a peer median of 44.3%, unusually high among its peers too. Deposit growth was -16.5%, at the 1.8th national percentile, which is unusually low, and at the 2.2nd percentile among peers against a peer median of -0.6%, unusually low among its peers too. Asset growth was -6.8%, at the 9.0th national percentile, which is unusually low, and at the 9.3rd percentile among peers against a peer median of 3.7%, unusually low among its peers too.

Interest expense was 0.9% of assets, at the 97.0th national percentile, which is unusually high, and at the 96.8th percentile among peers against a peer median of 0.4%, unusually high among its peers too. Net interest margin was 2.2%, at the 5.6th national percentile, which is unusually low, and at the 4.9th percentile among peers against a peer median of 3.3%, unusually low among its peers too. The efficiency ratio was 32.0%, at the 1.8th national percentile, which is unusually low, and at the 6.6th percentile among peers against a peer median of 54.0%, unusually low among its peers too. Federal Home Loan Bank borrowings were 10.2% of assets, at the 93.5th national percentile, which is unusually high, and at the 93.2nd percentile among peers against a peer median of 3.8%, unusually high among its peers too. Loan-loss reserves were 0.7% of loans, at the 7.4th national percentile, which is unusually low, and at the 9.5th percentile among peers against a peer median of 1.1%, unusually low among its peers too.

Overall, 8 of the bank's ratios were in the national top or bottom 10%, and 8 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 89.7% | 99.7th (unusually high) | 44.3% | 99.6th | unusually high among its peers too |
| deposit growth over the past four quarters | -16.5% | 1.8th (unusually low) | -0.6% | 2.2nd | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 32.0% | 1.8th (unusually low) | 54.0% | 6.6th | unusually low among its peers too |
| annualized interest expense as a share of assets | 0.9% | 97.0th (unusually high) | 0.4% | 96.8th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 2.2% | 5.6th (unusually low) | 3.3% | 4.9th | unusually low among its peers too |
| Federal Home Loan Bank borrowings as a share of assets | 10.2% | 93.5th (unusually high) | 3.8% | 93.2nd | unusually high among its peers too |
| loan-loss reserves as a share of loans | 0.7% | 7.4th (unusually low) | 1.1% | 9.5th | unusually low among its peers too |
| asset growth over the past four quarters | -6.8% | 9.0th (unusually low) | 3.7% | 9.3rd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 15.6% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 314.5% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 24.6% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, the bank failed on 2023-03-12, while at 2022-12-31 the model had ranked it 246 of 4,773 and not flagged it, so this counts as a miss. The model learned from 539 past failures, and 96% of them were credit-loss failures, caused by bad loans; 462 were credit-loss only and just 53 combined credit losses with run risk. This bank's loan problems were small, so the patterns the model knew best did not fit it.

On the run-risk rank (post-hoc check, designed after the 2023 failures), the bank placed 247. In a what-if (post-hoc check, designed after the 2023 failures) setting uninsured deposits as a share of deposits to each value from 0.0% to 100.0%, other data unchanged, the best rank reached was 154 of 4,773, at 0.0%, still outside the 96-bank watchlist. In a what-if (post-hoc check, designed after the 2023 failures) for losses on bonds held to maturity, as a share of equity, from 0.0% to 150.0%, the best rank reached was 134 of 4,773, at 0.0%. In a what-if (post-hoc check, designed after the 2023 failures) for losses on bonds available for sale, as a share of equity, from 0.0% to 100.0%, the best rank reached was 246 of 4,773, at 30.0%. These checks suggest the model did not treat the bank's heavy reliance on uninsured deposits as a strong sign of trouble.

## What happened next

In hindsight, the bank failed on 2023-03-12. Its last reported quarter was 2022-12-31, so there are no later ranks or watchlist flags. In our data, a bank that stops reporting has either merged or closed, and the two are not distinguished.

## Sources

- F1 · Bank name · n/a · Signature Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 57053 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F5 · Model score · 2022-12-31 · 0.0296 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2022-12-31 · 246 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 94.9% · data/analyst/scores.parquet: percentile
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
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 2.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
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
- F126 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.112 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F127 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F128 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2022-12-31 · 10.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F129 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F130 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F133 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.007 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F134 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F135 · Trend: ratios outside their own prior range · 2022-12-31 · 8 · data/features/fct_bank_features.parquet
- F136 · Trend: ratios shown in the table (the furthest outside their prior range) · 2022-12-31 · 6 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 79.9% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F145 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2022-12-31 · 89.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F146 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2022-12-31 · 99.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F147 · Peers: uninsured deposits as a share of deposits, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F148 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2022-12-31 · 99.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F149 · Peers: uninsured deposits as a share of deposits, peer median · 2022-12-31 · 44.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F150 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F151 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2022-12-31 · -16.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F152 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2022-12-31 · 1.8th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F153 · Peers: deposit growth over the past four quarters, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F154 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2022-12-31 · 2.2nd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F155 · Peers: deposit growth over the past four quarters, peer median · 2022-12-31 · -0.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F156 · Peers: deposit growth over the past four quarters, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F157 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2022-12-31 · 32.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F158 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2022-12-31 · 1.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F159 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F160 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2022-12-31 · 6.6th · data/features/fct_bank_features.parquet: efficiency_ratio
- F161 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2022-12-31 · 54.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F162 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F163 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2022-12-31 · 0.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F164 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2022-12-31 · 97.0th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F165 · Peers: annualized interest expense as a share of assets, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F166 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2022-12-31 · 96.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F167 · Peers: annualized interest expense as a share of assets, peer median · 2022-12-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F168 · Peers: annualized interest expense as a share of assets, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F169 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F170 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2022-12-31 · 5.6th · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F172 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2022-12-31 · 4.9th · data/features/fct_bank_features.parquet: net_interest_margin
- F173 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2022-12-31 · 3.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F174 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F175 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2022-12-31 · 10.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F176 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2022-12-31 · 93.5th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F177 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F178 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2022-12-31 · 93.2nd · data/features/fct_bank_features.parquet: fhlb_to_assets
- F179 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2022-12-31 · 3.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F180 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F181 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2022-12-31 · 0.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F182 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2022-12-31 · 7.4th · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: loan-loss reserves as a share of loans, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F184 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2022-12-31 · 9.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F185 · Peers: loan-loss reserves as a share of loans, peer median · 2022-12-31 · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F186 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F187 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2022-12-31 · -6.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F188 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2022-12-31 · 9.0th · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: asset growth over the past four quarters, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F190 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2022-12-31 · 9.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F191 · Peers: asset growth over the past four quarters, peer median · 2022-12-31 · 3.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: ratios in the national top or bottom 10% · 2022-12-31 · 8 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2022-12-31 · 8 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2022-12-31 · 10% · data/features/fct_bank_features.parquet
