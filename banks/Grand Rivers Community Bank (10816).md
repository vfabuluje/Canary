---
cert: 10816
name: "Grand Rivers Community Bank"
as_of: 2026-06-30
rank: 12
n_banks: 4313
percentile: 99.74495710642243
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Grand Rivers Community Bank (cert 10816)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Grand Rivers Community Bank, a small Illinois bank, ranked 12 out of 4,313 banks nationally on Canary's score, placing it in the 99.7th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its loan problems and losses were far worse than at a typical bank: 19.0% of its loans were 90 or more days past due or no longer earning interest, against a national median of 0.5%, and its return on assets was -3.4% against a median of 1.2%. Its funding and cash position, by contrast, looked steadier than the typical bank's.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thinner than at most banks: equity was 8.6% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.4% against 11.0%. The Tier 1 risk-based capital ratio was 10.7% against a median of 14.6%, and the total risk-based capital ratio was 12.0% against 15.8%.

Credit quality, meaning whether borrowers repay, was the weakest area: nonaccrual assets (loans no longer earning interest) plus foreclosed property equaled 12.6% of assets against a national median of 0.3%, and loans 30-89 days past due equaled 6.4% of assets against 0.2%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 113.1% against a median of 2.9%, and loan-loss reserves (money set aside for bad loans) were 5.0% of loans against 1.2%. The bank was also losing money, with a return on equity of -38.7% against a median of 11.6%, and it was shrinking, with assets down -14.0% over four quarters while the median bank grew 4.5%. Commercial real estate loans made up 42.0% of its loans against a median of 23.6%, though the separate concentration check found it did not cross either regulatory screening line.

Liquidity and funding point the other way: core deposits, the stable everyday deposits, funded 89.2% of assets against a median of 75.5%, volatile funding was 0.0% against 9.0%, and cash was 13.8% of assets against 6.2%. Uninsured deposits were 21.6% of deposits against a median of 24.8%, although deposits fell -13.6% over four quarters while the median bank's grew 4.2%. Unrealized losses on bonds available for sale were small at 0.1% of equity, well below the national median of 5.6%.

## Understanding the score

Grand Rivers Community Bank ranked 12 out of 4,313 banks as of 2026-06-30, which is the 99.7th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, the riskiest 2% of banks, which held 87 banks that quarter.

The five features that pushed its score up most were loans 90+ days past due or not accruing interest at 19.0% of loans, return on equity at -38.7%, the Texas ratio at 113.1%, loans 30-89 days past due at 6.4% of assets, and its small size, with total assets of $15.1 million. The five that pulled it down most were the Tier 1 risk-based capital ratio at 10.7%, interest expense at 1.0% of assets, the total risk-based capital ratio at 12.0%, commercial real estate loans at 42.0% of loans, and construction loans at 0.0% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 7 | 4,589 | ▲ watchlist |
| 2024-12-31 | 207 | 4,560 |  |
| 2025-03-31 | 17 | 4,536 | ▲ watchlist |
| 2025-06-30 | 14 | 4,494 | ▲ watchlist |
| 2025-09-30 | 13 | 4,452 | ▲ watchlist |
| 2025-12-31 | 12 | 4,411 | ▲ watchlist |
| 2026-03-31 | 17 | 4,353 | ▲ watchlist |
| 2026-06-30 | 12 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Grand Rivers Community Bank ranked 12 out of 4,313 banks nationally, placing it in the 99.7th percentile, where 100 marks the highest model score. On 2025-06-30 it also sat at the 99.7th percentile, and the model rated it about the same as a year earlier. Of 30 ratios compared with their own history, usually the prior 12 quarters, 8 were outside their prior range. Each ratio's contribution is given in model log-odds units, an internal scale where a positive number raises the score and a negative one lowers it.

Return on equity (profit as a share of shareholders' money) was -38.7%, below its prior range of -28.3% to -9.1%, and at +0.701 it pushed the score up. Return on assets (profit as a share of everything the bank owns) was -3.4%, below its prior range of -2.4% to -0.9%, and at +0.080 it pushed the score up. Loan-loss reserves (money set aside for loans that may not be repaid) reached 5.0% of loans, just above their prior range of 2.7% to 4.9%, and at +0.073 they pushed the score up.

The efficiency ratio (operating costs as a share of revenue) was 169.4%, above its prior range of 112.8% to 154.1%, yet at -0.033 it had little effect on the score. Net interest margin (the spread earned on lending and investing) was 4.4%, slightly below its prior range of 4.5% to 4.8%, but at -0.117 it pushed the score down. Losses on bonds available for sale were 0.1% of equity, below their prior range of 0.2% to 1.0%, and at +0.010 they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on assets (profit as a share of assets) | -3.4% | -2.4% to -0.9% | same quarter, prior 3 years | n/a | -1.4 pp | +0.080 | pushed the score up |
| return on equity (profit as a share of equity) | -38.7% | -28.3% to -9.1% | same quarter, prior 3 years | n/a | -17.5 pp | +0.701 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 169.4% | 112.8% to 154.1% | same quarter, prior 3 years | n/a | +15.3 pp | -0.033 | little effect on the score |
| losses on bonds available for sale, as a share of equity | 0.1% | 0.2% to 1.0% | prior 12 quarters | -0.1 pp | -0.4 pp | +0.010 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 4.4% | 4.5% to 4.8% | same quarter, prior 3 years | n/a | -0.1 pp | -0.117 | pushed the score down |
| loan-loss reserves as a share of loans | 5.0% | 2.7% to 4.9% | prior 12 quarters | +0.1 pp | +0.4 pp | +0.073 | pushed the score up |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 95 banks in the same specialty group and size tier (under $100 million).

Grand Rivers Community Bank ranks 12 out of 4,313 banks nationally on Canary's score, which places it in the 99.7th percentile. Loans 30-89 days past due (borrowers who are behind on payments) equal 6.4% of assets, in the 100.0th percentile nationally, which is unusually high, and in the 99.5th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) plus foreclosed property equal 12.6% of assets, in the 99.9th percentile nationally, which is unusually high, and in the 99.5th percentile among its peers against a peer median of 0.3%, which is unusually high among its peers too. Loans 90+ days past due or not accruing interest make up 19.0% of loans, in the 99.9th percentile nationally, which is unusually high, and in the 99.5th percentile among its peers against a peer median of 0.5%, which is unusually high among its peers too. The Texas ratio (troubled assets measured against capital plus reserves) is 113.1%, in the 99.9th percentile nationally, which is unusually high, and in the 98.4th percentile among its peers against a peer median of 3.0%, which is unusually high among its peers too.

Return on equity (profit as a share of the owners' stake) is -38.7%, in the 0.5th percentile nationally, which is unusually low, and in the 3.7th percentile among its peers against a peer median of 7.0%, which is unusually low among its peers too. Return on assets (profit as a share of everything the bank owns) is -3.4%, in the 0.8th percentile nationally, which is unusually low, and in the 5.8th percentile among its peers against a peer median of 0.8%, which is unusually low among its peers too. The efficiency ratio (operating costs as a share of revenue) is 169.4%, in the 99.2nd percentile nationally, which is unusually high, and in the 94.2nd percentile among its peers against a peer median of 75.6%, which is unusually high among its peers too. Loan-loss reserves (money set aside to cover expected bad loans) equal 5.0% of loans, in the 99.2nd percentile nationally, which is unusually high, and in the 98.4th percentile among its peers against a peer median of 1.3%, which is unusually high among its peers too.

Overall, 16 of the bank's ratios sit in the national top or bottom 10%, and 15 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 6.4% | 100.0th (unusually high) | 0.4% | 99.5th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 12.6% | 99.9th (unusually high) | 0.3% | 99.5th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 113.1% | 99.9th (unusually high) | 3.0% | 98.4th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 19.0% | 99.9th (unusually high) | 0.5% | 99.5th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -38.7% | 0.5th (unusually low) | 7.0% | 3.7th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 5.0% | 99.2nd (unusually high) | 1.3% | 98.4th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -3.4% | 0.8th (unusually low) | 0.8% | 5.8th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 169.4% | 99.2nd (unusually high) | 75.6% | 94.2nd | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 132.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -15.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, the fact sheet holds no data from after the as-of quarter, so it cannot confirm how this bank's situation developed. Its place on the watchlist rests on the figures described above, chiefly its severe loan problems and ongoing losses.

## What happened next

With hindsight, later ranks, flags or reporting status for this bank are not included in the fact sheet, so this memo cannot say what happened next. The score history table added below shows whatever later data Canary holds.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 12 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 42.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 113.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 21.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -14.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -13.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 19.0%; contribution to the score · 2026-06-30 · +1.079 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -38.7%; contribution to the score · 2026-06-30 · +0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 113.1%; contribution to the score · 2026-06-30 · +0.672 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 6.4%; contribution to the score · 2026-06-30 · +0.550 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: total assets, value $15.1 million; contribution to the score · 2026-06-30 · +0.459 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.7%; contribution to the score · 2026-06-30 · -1.502 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2026-06-30 · -0.902 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 12.0%; contribution to the score · 2026-06-30 · -0.318 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 42.0%; contribution to the score · 2026-06-30 · -0.240 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.198 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F86 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F87 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.080 · data/analyst/scores.parquet: feature return_on_assets contribution
- F90 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -28.3% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -9.1% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 169.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 112.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 154.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F105 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F108 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · +0.010 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F109 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F110 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F111 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F112 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F114 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.117 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F115 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F116 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F117 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F118 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F121 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.073 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F122 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F134 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F135 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F136 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F137 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F138 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F139 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F140 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 113.1% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F155 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F156 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F157 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 3.7th · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F164 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F165 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F166 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: allowance_to_loans
- F167 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F168 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F170 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: return_on_assets
- F171 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F172 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 5.8th · data/features/fct_bank_features.parquet: return_on_assets
- F173 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F174 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 169.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 94.2nd · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 75.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F180 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F182 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F183 · Peers: those ratios also unusual among peers · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F185 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
