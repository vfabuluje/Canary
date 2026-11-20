---
cert: 178
name: "Talbot State Bank"
as_of: 2026-06-30
rank: 22
n_banks: 4313
percentile: 99.51309993044285
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:43"
writer_model: "claude-opus-5-5"
checked: true
---

# Talbot State Bank (cert 178)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Canary ranked Talbot State Bank, a Georgia bank, 22 out of 4,313 banks nationally, the 99.5th percentile on a scale where higher means riskier, and it was flagged on the watchlist. The main concerns are a thin equity cushion of 4.5% of assets, losses on sellable bonds equal to 76.0% of equity, and loans 30-89 days behind on payments at 5.2% of assets, all far from national norms. Its risk-based capital ratios, which weigh capital against assets adjusted for riskiness, sit above the national median, so the capital picture points in two directions.

## Warning signs in the data

Capital, the owners' money that absorbs losses, looks thin by simple measures: equity was 4.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.8% against 11.0%. Measured against risk-weighted assets, though, the picture differs: the Tier 1 risk-based capital ratio was 16.8% versus a median of 14.6%, and the total risk-based capital ratio was 17.6% versus 15.8%. These two views of capital genuinely point different ways, and the reader should keep both in mind.

Credit quality is weak: loans 30-89 days past due were 5.2% of assets against a median of 0.2%, and loans 90+ days past due or no longer paying interest were 2.3% of loans against 0.5%. Loan-loss reserves, money set aside for expected bad loans, were only 0.6% of loans against a median of 1.2%, and the Texas ratio (troubled assets against capital plus reserves) was 30.9% against 2.9%. The bank was losing money, with return on assets of -0.9% against a median of 1.2%, and its efficiency ratio (operating costs as a share of revenue) was 123.7% against 62.1%.

Funding leans on less stable sources: brokered deposits, money placed through intermediaries, were 19.0% of deposits against a median of 0.0%, and volatile funding was 26.8% of assets against 9.0%. Federal Home Loan Bank borrowings were 7.7% of assets against 0.2%, while core deposits, the steadier everyday accounts, were 58.8% against 75.5%; uninsured deposits, at 19.4%, were below the median of 24.8%. Unrealized losses on bonds available for sale, the drop in market value of bonds the bank could sell, equaled 76.0% of equity against a national median of 5.6%.

## Understanding the score

As of 2026-06-30, Talbot State Bank ranked 22 out of 4,313 banks, the 99.5th percentile, where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter.

The five features that pushed the score up most were losses on bonds available for sale at 76.0% of equity, contributing +1.284, and brokered deposits at 19.0% of deposits, contributing +0.935. Next came loans 30-89 days past due at 5.2% of assets, contributing +0.445, commercial real estate loans at 1.6% of loans, contributing +0.171, and interest expense at 2.5% of assets, contributing +0.137.

The five features that pulled the score down most were the Tier 1 risk-based capital ratio at 16.8%, contributing -1.591, and the Texas ratio at 30.9%, contributing -0.505. They were followed by the total risk-based capital ratio at 17.6%, contributing -0.433, construction loans at 5.9% of loans, contributing -0.257, and nonaccrual assets and foreclosed property at 0.8% of assets, contributing -0.224.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 35 | 4,589 | ▲ watchlist |
| 2024-12-31 | 86 | 4,560 | ▲ watchlist |
| 2025-03-31 | 44 | 4,536 | ▲ watchlist |
| 2025-06-30 | 42 | 4,494 | ▲ watchlist |
| 2025-09-30 | 48 | 4,452 | ▲ watchlist |
| 2025-12-31 | 32 | 4,411 | ▲ watchlist |
| 2026-03-31 | 27 | 4,353 | ▲ watchlist |
| 2026-06-30 | 22 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Canary ranked Talbot State Bank 22 out of 4,313 banks nationally, placing it in the 99.5th percentile, where higher means riskier. A year earlier, at 2025-06-30, it sat in the 99.1th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own prior range over the previous 12 quarters, and 6 of the 30 ratios checked moved outside that range.

The total risk-based capital ratio (the bank's capital cushion measured against its loans and other assets weighted by risk) was 17.6%, below its prior range of 18.5% to 26.5%, yet it pushed the score down, with a contribution of -0.433 model log-odds units. The Tier 1 risk-based capital ratio (the same idea using only core capital) was 16.8%, below its prior range of 17.6% to 25.6%, and it also pushed the score down, by -1.591 model log-odds units. Both capital ratios fell by -0.9 pp over one quarter and -2.4 pp over four quarters. The leverage ratio (core capital as a share of average assets) was 7.8%, just below its prior range of 7.9% to 10.4%, and it pushed the score up, by +0.079 model log-odds units.

Nonaccrual assets and foreclosed property (loans that have stopped paying interest plus repossessed property) were 0.75% of assets, below their prior range of 0.77% to 1.4%, and this pushed the score down, by -0.224 model log-odds units. Loans as a share of deposits reached 72.5%, above its prior range of 63.9% to 71.4%, but it had little effect on the score, at -0.010 model log-odds units. Net interest margin (the spread earned on lending and investing) was 3.7%, above its prior range of 3.1% to 3.6%, but it too had little effect on the score, at -0.003 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| loans as a share of deposits | 72.5% | 63.9% to 71.4% | prior 12 quarters | +4.3 pp | +4.5 pp | -0.010 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.7% | 3.1% to 3.6% | same quarter, prior 3 years | n/a | +0.4 pp | -0.003 | little effect on the score |
| the total risk-based capital ratio | 17.6% | 18.5% to 26.5% | prior 12 quarters | -0.9 pp | -2.4 pp | -0.433 | pushed the score down |
| the Tier 1 risk-based capital ratio | 16.8% | 17.6% to 25.6% | prior 12 quarters | -0.9 pp | -2.4 pp | -1.591 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 7.8% | 7.9% to 10.4% | prior 12 quarters | -0.2 pp | -1.0 pp | +0.079 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 0.75% | 0.77% to 1.4% | prior 12 quarters | -0.01 pp | -0.3 pp | -0.224 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 76 banks in the same specialty group and size tier (under $100 million).

Equity as a share of assets, the owners' cushion that absorbs losses, is 4.5% at this bank, which places it at the 1.1st percentile nationally, unusually low; among its peers it sits at the 3.3rd percentile against a peer median of 13.1%, unusually low among its peers too. The leverage ratio, core capital as a share of average assets, is 7.8%, at the 2.2nd percentile nationally, unusually low; it ranks at the 5.9th percentile among its peers against a peer median of 12.7%, unusually low among its peers too. Losses on bonds available for sale, meaning the drop in market value of bonds the bank could sell, equal 76.0% of equity, at the 98.5th percentile nationally, unusually high; among its peers this is the 98.0th percentile against a peer median of 0.5%, unusually high among its peers too.

Loans 30-89 days past due, where borrowers have fallen behind on payments, equal 5.2% of assets, at the 99.8th percentile nationally, unusually high; among its peers this is the 96.7th percentile against a peer median of 0.5%, unusually high among its peers too. The Texas ratio, troubled assets measured against capital plus reserves, is 30.9%, at the 98.0th percentile nationally, unusually high; it sits at the 96.7th percentile among its peers against a peer median of 1.7%, unusually high among its peers too.

Return on equity, profit as a share of equity, is -18.5%, at the 0.9th percentile nationally, unusually low; among its peers it is at the 4.6th percentile against a peer median of 2.6%, unusually low among its peers too. Return on assets, profit as a share of assets, is -0.9%, at the 2.1st percentile nationally, unusually low; among its peers it is at the 9.9th percentile against a peer median of 0.3%, which is typical for its peer group. The efficiency ratio, operating costs as a share of revenue, is 123.7%, at the 98.4th percentile nationally, unusually high; among its peers it is at the 87.5th percentile against a peer median of 83.5%, which is typical for its peer group. Overall, 14 of the bank's ratios fall in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 5.2% | 99.8th (unusually high) | 0.5% | 96.7th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -18.5% | 0.9th (unusually low) | 2.6% | 4.6th | unusually low among its peers too |
| equity as a share of assets | 4.5% | 1.1st (unusually low) | 13.1% | 3.3rd | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | 76.0% | 98.5th (unusually high) | 0.5% | 98.0th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 123.7% | 98.4th (unusually high) | 83.5% | 87.5th | typical for its peer group |
| the Texas ratio (troubled assets against capital plus reserves) | 30.9% | 98.0th (unusually high) | 1.7% | 96.7th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -0.9% | 2.1st (unusually low) | 0.3% | 9.9th | typical for its peer group |
| the leverage ratio (core capital as a share of average assets) | 7.8% | 2.2nd (unusually low) | 12.7% | 5.9th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 45.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 52.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 46.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank's outcome case is that it remains open and on the watchlist. The fact sheet for this memo contains no data from after the as-of quarter, so there are no later figures to explain why it stays on the list beyond the warning signs already described.

## What happened next

In hindsight: the fact sheet provides no later ranks, watchlist flags, or reporting status for this bank after the as-of quarter. The bank's later path therefore cannot be described here beyond its outcome case of remaining open and on the watchlist.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 22 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.5% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 16.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 30.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 123.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 19.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 58.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 26.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 76.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 76.0%; contribution to the score · 2026-06-30 · +1.284 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 19.0%; contribution to the score · 2026-06-30 · +0.935 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: loans 30-89 days past due, as a share of assets, value 5.2%; contribution to the score · 2026-06-30 · +0.445 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 1.6%; contribution to the score · 2026-06-30 · +0.171 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.137 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 16.8%; contribution to the score · 2026-06-30 · -1.591 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 30.9%; contribution to the score · 2026-06-30 · -0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 17.6%; contribution to the score · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.257 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · -0.224 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F89 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 72.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F90 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 63.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F91 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 71.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F94 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F95 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F96 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F97 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F98 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F100 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.003 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F101 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F102 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F103 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 18.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F104 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 26.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F105 · Trend: the total risk-based capital ratio, change over one quarter, in percentage points · 2026-06-30 · -0.9 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F106 · Trend: the total risk-based capital ratio, change over four quarters, in percentage points · 2026-06-30 · -2.4 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F107 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F108 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F109 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 16.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F110 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 17.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F111 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 25.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F112 · Trend: the Tier 1 risk-based capital ratio, change over one quarter, in percentage points · 2026-06-30 · -0.9 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F113 · Trend: the Tier 1 risk-based capital ratio, change over four quarters, in percentage points · 2026-06-30 · -2.4 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F114 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -1.591 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F115 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F116 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F117 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F121 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.079 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F122 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.75% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.77% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F125 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F128 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.224 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F129 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.1% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F140 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F141 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F142 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F143 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F144 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F145 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F146 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -18.5% · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 4.6th · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F153 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F154 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F155 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 3.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F156 · Peers: equity as a share of assets, peer median · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F157 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F158 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 76.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F159 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.5th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F160 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F161 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F162 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F163 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F164 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 123.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F165 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F166 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F167 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 87.5th · data/features/fct_bank_features.parquet: efficiency_ratio
- F168 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 83.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F169 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: efficiency_ratio
- F170 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 30.9% · data/features/fct_bank_features.parquet: texas_ratio
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F173 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: texas_ratio
- F174 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F175 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F176 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 9.9th · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: return_on_assets
- F182 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F183 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F184 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F185 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 5.9th · data/features/fct_bank_features.parquet: leverage_ratio
- F186 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F187 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F189 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F190 · Peers: those ratios also unusual among peers · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F192 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
