---
cert: 5520
name: "Santa Anna National Bank"
as_of: 2025-03-31
rank: 84
n_banks: 4536
percentile: 98.17019400352733
flagged: true
outcome: "missed"
after_test_window: false
failure_date: 2025-06-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:20"
writer_model: "claude-opus-5-5"
checked: true
---

# Santa Anna National Bank (cert 5520)

*Hindsight: failed 2025-06-27. Canary did not flag it.*

## Summary

As of 2025-03-31, Santa Anna National Bank, a Texas bank, ranked 84 out of 4,536 FDIC-insured banks on Canary's risk score, placing it in the 98.2nd percentile, where higher means riskier. That put it on the watchlist, which covers the riskiest 2% of banks. The biggest push upward came from losses on its bonds held available for sale, equal to 40.8% of its equity (the owners' loss-absorbing cushion), against a national median of 9.3%, alongside a thin equity cushion of 6.5% of assets. The picture is mixed: profits and loan quality looked strong and pulled the score down, while capital and bond losses looked weak and pushed it up.

## Warning signs in the data

Capital was the clearest weak spot: equity was 6.5% of assets, well below the national median of 9.9%. The leverage ratio, a regulatory measure of core capital against average assets, was 8.6%, below the national median of 10.7%. Losses on bonds available for sale (bonds the bank could sell, whose market value had fallen) equaled 40.8% of equity, far above the national median of 9.3%, and securities made up 29.5% of assets against a median of 18.3%.

Credit quality, meaning how well borrowers were repaying, looked broadly normal: loans 90+ days past due or not accruing interest were 0.5% of loans against a median of 0.4%, and loans 30-89 days past due were 0.0% of assets against 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 3.7%, a little above the national median of 2.5% but still low.

On funding, uninsured deposits (balances above the FDIC insurance limit) were 29.5% of deposits against a median of 23.9%, and volatile funding was 14.6% of assets against 8.6%. Cash was 3.7% of assets, below the median of 6.9%, while brokered deposits were 0.0%, in line with the median of 0.0%. The bank was also growing fast, with assets up 26.1% and deposits up 33.2% over the past four quarters, against national medians of 3.8% and 4.6%.

## Understanding the score

On 2025-03-31 the bank ranked 84 out of 4,536 banks, in the 98.2nd percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks; 91 banks were on it that quarter.

Five features pushed the score up most. Losses on bonds available for sale, at 40.8% of equity, added +1.665, by far the largest push. The efficiency ratio (operating costs as a share of revenue), at 52.9%, added +0.354, and deposit growth of 33.2% added +0.274. Commercial real estate loans at 6.0% of loans added +0.174, and loans at 56.9% of deposits added +0.119.

Five features pulled the score down most. The Texas ratio, at 3.7%, subtracted -1.296, and the Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets; no value is shown in our data) subtracted -0.914. Return on equity of 27.6% subtracted -0.439, loans 90+ days past due or not accruing interest at 0.5% of loans subtracted -0.304, and return on assets of 1.7% subtracted -0.281.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-06-30 | 525 | 4,714 |  |
| 2023-09-30 | 429 | 4,686 |  |
| 2023-12-31 | 346 | 4,658 |  |
| 2024-03-31 | 282 | 4,640 |  |
| 2024-06-30 | 388 | 4,610 |  |
| 2024-09-30 | 191 | 4,589 |  |
| 2024-12-31 | 297 | 4,560 |  |
| 2025-03-31 | 84 | 4,536 | ▲ watchlist |

## How its ratios moved

As of 2025-03-31, Santa Anna National Bank ranked 84 out of 4,536 banks nationally, placing it in the 98.2nd percentile, where higher means riskier. A year earlier, on 2024-03-31, it sat in the 93.9th percentile, and the model rated it riskier than a year earlier. Of 28 ratios compared with their own prior range, usually the prior 12 quarters, 9 sat outside that range.

Return on equity (profit as a share of the owners' stake) was 27.6%, above its prior range of 16.4% to 19.6%, yet its contribution of -0.439 model log-odds units pushed the score down. Return on assets (profit as a share of everything the bank owns) was 1.7%, above its prior range of 1.4% to 1.6%, and despite being outside that range its contribution of -0.281 pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 52.9%, below its prior range of 56.0% to 60.5%, and its contribution of +0.354 pushed the score up.

The leverage ratio (core capital as a share of average assets) was 8.6%, below its prior range of 8.9% to 11.2% after a change of -1.9 pp over four quarters, but its contribution of -0.082 still pushed the score down. Annualized interest expense as a share of assets was 1.9%, above its prior range of 0.2% to 1.7%, yet its contribution of -0.101 pushed the score down. Construction loans as a share of loans were 0.6%, below their prior range of 0.9% to 1.5%, but with a contribution of +0.038 they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 27.6% | 16.4% to 19.6% | same quarter, prior 3 years | n/a | +8.1 pp | -0.439 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 52.9% | 56.0% to 60.5% | same quarter, prior 3 years | n/a | -7.6 pp | +0.354 | pushed the score up |
| construction loans as a share of loans | 0.6% | 0.9% to 1.5% | prior 12 quarters | -0.9 pp | -0.9 pp | +0.038 | little effect on the score |
| return on assets (profit as a share of assets) | 1.7% | 1.4% to 1.6% | same quarter, prior 3 years | n/a | +0.2 pp | -0.281 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 8.6% | 8.9% to 11.2% | prior 12 quarters | -0.3 pp | -1.9 pp | -0.082 | pushed the score down |
| annualized interest expense as a share of assets | 1.9% | 0.2% to 1.7% | same quarter, prior 3 years | n/a | +0.2 pp | -0.101 | pushed the score down |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2025-03-31: Agricultural Specialization.

Peers: 269 banks in the same specialty group and size tier (under $100 million).

Deposits, the money customers keep at the bank, grew 33.2% over the past four quarters, which is unusually high nationally at the 96.7th percentile and unusually high among its peers too, at the 98.0th percentile of its peers against a peer median of 3.3%. Total assets, everything the bank owns such as loans and securities, grew 26.1% over the past four quarters, which is unusually high nationally at the 96.1st percentile and unusually high among its peers too, at the 98.0th percentile of its peers against a peer median of 2.4%. Return on equity, which is profit as a share of the owners' stake in the bank, was 27.6%, unusually high nationally at the 96.7th percentile and unusually high among its peers too, at the 96.8th percentile of its peers against a peer median of 9.8%.

Equity, the owners' cushion that absorbs losses, was 6.5% of assets, which is unusually low nationally at the 7.6th percentile and unusually low among its peers too, at the 6.1st percentile of its peers against a peer median of 10.9%. The leverage ratio, a regulatory measure of core capital as a share of average assets, was 8.6%, unusually low nationally at the 9.8th percentile and unusually low among its peers too, at the 6.5th percentile of its peers against a peer median of 12.3%. Loans 30-89 days past due, meaning borrowers who are behind on payments but not yet seriously delinquent, came to 0.0% of assets, which is unusually low nationally at the 5.0th percentile but typical for its peer group, at the 9.9th percentile of its peers against a peer median of 0.3%.

Overall, 6 of the bank's ratios sit in the national top or bottom 10%, and 5 of those are also unusual among its peers, pointing to a bank that is growing and earning far faster than similar small agricultural banks while holding a thinner capital cushion than most of them.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| deposit growth over the past four quarters | 33.2% | 96.7th (unusually high) | 3.3% | 98.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | 27.6% | 96.7th (unusually high) | 9.8% | 96.8th | unusually high among its peers too |
| asset growth over the past four quarters | 26.1% | 96.1st (unusually high) | 2.4% | 98.0th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 0.0% | 5.0th (unusually low) | 0.3% | 9.9th | typical for its peer group |
| equity as a share of assets | 6.5% | 7.6th (unusually low) | 10.9% | 6.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 8.6% | 9.8th (unusually low) | 12.3% | 6.5th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 3.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 35.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -14.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

With hindsight: the bank failed on 2025-06-27, and the model had in fact flagged it at the 2025-03-31 quarter. That flag came after the 2016-2024 test period, so under Canary's rules it is not counted in the reported results, which is why this case is filed as a miss rather than a catch. The flag was raised from the last quarter the bank ever reported, 2025-03-31, so there was no later data for the model to confirm or revise it.

## What happened next

With hindsight: the last quarter the bank reported was 2025-03-31, so there are no later ranks or watchlist flags in our data. The bank failed on 2025-06-27.

## Sources

- F1 · Bank name · n/a · Santa Anna National Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-03-31 · 84 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-03-31 · 4,536 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-03-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-03-31 · 91 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-03-31 · 6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-03-31 · 9.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2025-03-31 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2025-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2025-03-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2025-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2025-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2025-03-31 · 14.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2025-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2025-03-31 · 40.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2025-03-31 · 9.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2025-03-31 · 18.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F67 · Bank: asset growth over the past four quarters · 2025-03-31 · 26.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F68 · National median: asset growth over the past four quarters · 2025-03-31 · 3.8% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2025-03-31 · 33.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2025-03-31 · 4.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 40.8%; contribution to the score · 2025-03-31 · +1.665 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 52.9%; contribution to the score · 2025-03-31 · +0.354 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F73 · Driver up #3: deposit growth over the past four quarters, value 33.2%; contribution to the score · 2025-03-31 · +0.274 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F74 · Driver up #4: commercial real estate loans as a share of loans, value 6.0%; contribution to the score · 2025-03-31 · +0.174 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F75 · Driver up #5: loans as a share of deposits, value 56.9%; contribution to the score · 2025-03-31 · +0.119 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.7%; contribution to the score · 2025-03-31 · -1.296 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2025-03-31 · -0.914 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 27.6%; contribution to the score · 2025-03-31 · -0.439 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2025-03-31 · -0.304 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: return on assets (profit as a share of assets), value 1.7%; contribution to the score · 2025-03-31 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F81 · Failure date · 2025-06-27 · 2025-06-27 · data/raw/failures: FAILDATE
- F82 · Flagged at Q1 2025, after the 2016-2024 test period (not counted in the reported results) · 2025-03-31 · 2025-03-31 · data/analyst/scores.parquet: flagged
- F83 · Last quarter the bank reported · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
- F88 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-03-31 · 27.6% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 16.4% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 19.6% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-03-31 · -0.439 · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-03-31 · 52.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 56.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 60.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-03-31 · +0.354 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-03-31 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: construction loans as a share of loans, value at the as-of quarter · 2025-03-31 · 0.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F101 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F102 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F105 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2025-03-31 · +0.038 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F106 · Trend: construction loans as a share of loans, what the model did with it · 2025-03-31 · little effect on the score · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-03-31 · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-03-31 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F114 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F115 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 11.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F117 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2025-03-31 · -1.9 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2025-03-31 · -0.082 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F119 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F120 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2025-03-31 · 1.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F121 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F122 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F124 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2025-03-31 · -0.101 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F125 · Trend: annualized interest expense as a share of assets, what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F126 · Trend: ratios outside their own prior range · 2025-03-31 · 9 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2025-03-31 · 28 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2024-03-31 · 93.9% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2025-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2025-03-31 · 33.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F137 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2025-03-31 · 96.7th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F138 · Peers: deposit growth over the past four quarters, national reading · 2025-03-31 · unusually high · data/features/fct_bank_features.parquet: deposit_growth_4q
- F139 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2025-03-31 · 98.0th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F140 · Peers: deposit growth over the past four quarters, peer median · 2025-03-31 · 3.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F141 · Peers: deposit growth over the past four quarters, reading against its peers · 2025-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F142 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2025-03-31 · 27.6% · data/features/fct_bank_features.parquet: return_on_equity
- F143 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2025-03-31 · 96.7th · data/features/fct_bank_features.parquet: return_on_equity
- F144 · Peers: return on equity (profit as a share of equity), national reading · 2025-03-31 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F145 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2025-03-31 · 96.8th · data/features/fct_bank_features.parquet: return_on_equity
- F146 · Peers: return on equity (profit as a share of equity), peer median · 2025-03-31 · 9.8% · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), reading against its peers · 2025-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2025-03-31 · 26.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F149 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2025-03-31 · 96.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F150 · Peers: asset growth over the past four quarters, national reading · 2025-03-31 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F151 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2025-03-31 · 98.0th · data/features/fct_bank_features.parquet: asset_growth_4q
- F152 · Peers: asset growth over the past four quarters, peer median · 2025-03-31 · 2.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F153 · Peers: asset growth over the past four quarters, reading against its peers · 2025-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F154 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2025-03-31 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F155 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2025-03-31 · 5.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F156 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2025-03-31 · unusually low · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F157 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2025-03-31 · 9.9th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2025-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F159 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2025-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F160 · Peers: equity as a share of assets, bank value at the as-of quarter · 2025-03-31 · 6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F161 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2025-03-31 · 7.6th · data/features/fct_bank_features.parquet: equity_to_assets
- F162 · Peers: equity as a share of assets, national reading · 2025-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F163 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2025-03-31 · 6.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F164 · Peers: equity as a share of assets, peer median · 2025-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F165 · Peers: equity as a share of assets, reading against its peers · 2025-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F166 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F167 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2025-03-31 · 9.8th · data/features/fct_bank_features.parquet: leverage_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2025-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2025-03-31 · 6.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2025-03-31 · 12.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2025-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: ratios in the national top or bottom 10% · 2025-03-31 · 6 · data/features/fct_bank_features.parquet
- F174 · Peers: those ratios also unusual among peers · 2025-03-31 · 5 · data/features/fct_bank_features.parquet
- F176 · Peers: cut-off for unusual (top or bottom share of banks) · 2025-03-31 · 10% · data/features/fct_bank_features.parquet
