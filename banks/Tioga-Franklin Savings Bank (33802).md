---
cert: 33802
name: "Tioga-Franklin Savings Bank"
as_of: 2026-06-30
rank: 1
n_banks: 4313
percentile: 100.0
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:40"
writer_model: "claude-opus-5-5"
checked: true
---

# Tioga-Franklin Savings Bank (cert 33802)

*Outcome not yet known.*

## Summary

Tioga-Franklin Savings Bank ranked 1 out of 4,313 banks nationally as of 2026-06-30, placing it at the 100.0th percentile, where higher means riskier, and it is flagged on Canary's watchlist. Its capital, the bank's own money that absorbs losses, is very thin: its leverage ratio (core capital as a share of average assets) was 2.1% against a national median of 11.0%. At the same time, troubled loans are heavy and the bank is losing money, with a Texas ratio (troubled assets against capital plus reserves) of 257.0% against a median of 2.9%, and return on equity of -121.2% against a median of 11.6%. Its funding looks steadier by contrast, with uninsured deposits at 6.4% of deposits, well below the national median of 24.8%.

## Warning signs in the data

Capital is the clearest weak spot: equity was 2.0% of assets against a national median of 10.6%, and the leverage ratio was 2.1% against 11.0%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by riskiness, was 2.9% against a median of 14.6%, and the total risk-based capital ratio was 4.1% against 15.8%.

Credit quality is also poor: loans 90 or more days past due or no longer accruing interest were 9.2% of loans against a median of 0.5%, and nonaccrual assets plus foreclosed property were 6.8% of assets against 0.3%. The Texas ratio reached 257.0% against a median of 2.9%, and net loan write-offs, loans given up on minus later recoveries, ran at 0.9% of loans against 0.0%. The provision for loan losses, money set aside for expected bad loans, was -0.5% of assets against a median of 0.1%, meaning the bank reduced rather than added to its set-aside. Earnings were deeply negative, with return on assets of -3.4% against 1.2%, an efficiency ratio (operating costs as a share of revenue) of 188.7% against 62.1%, and interest expense of 3.4% of assets against 1.6%. Commercial real estate loans were 31.8% of loans against a median of 23.6%; the concentration section finds the bank met the regulators' commercial real estate size screen but not the growth test, so it did not cross the second line.

Funding and bonds point the other way and look comparatively calm: uninsured deposits were 6.4% of deposits against 24.8%, core deposits, the stable everyday kind, were 83.1% of assets against 75.5%, and cash was 8.0% of assets against 6.2%. Volatile funding, money that can leave quickly, was somewhat higher at 13.1% of assets against 9.0%, and brokered deposits were 1.1% of deposits against 0.0%. Losses on bonds available for sale were 1.6% of equity, below the median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median of 0.0%.

## Understanding the score

The bank ranked 1 out of 4,313 banks as of 2026-06-30, the 100.0th percentile, with a model score of 0.9965. It is flagged on the watchlist, which covers the riskiest 2% of banks, or 87 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 2.9% (+1.705), return on equity at -121.2% (+1.638), the Texas ratio at 257.0% (+1.153), loans 90 or more days past due or not accruing interest at 9.2% of loans (+0.544), and the total risk-based capital ratio at 4.1% (+0.488). The five factors pulling it down most were construction loans at 2.4% of loans (-0.265), loans that are recently overdue but not yet seriously delinquent at 0.4% of assets (-0.239), loan-loss reserves at 1.3% of loans (-0.098), commercial real estate loans at 31.8% of loans (-0.070), and deposit growth over the past four quarters of 9.5% (-0.069). The upward pushes are far larger than the downward ones, which is why thin capital, losses and troubled loans dominate the result.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3 | 4,589 | ▲ watchlist |
| 2024-12-31 | 4 | 4,560 | ▲ watchlist |
| 2025-03-31 | 4 | 4,536 | ▲ watchlist |
| 2025-06-30 | 2 | 4,494 | ▲ watchlist |
| 2025-09-30 | 5 | 4,452 | ▲ watchlist |
| 2025-12-31 | 4 | 4,411 | ▲ watchlist |
| 2026-03-31 | 4 | 4,353 | ▲ watchlist |
| 2026-06-30 | 1 | 4,313 | ▲ watchlist |

## How its ratios moved

Tioga-Franklin Savings Bank ranked 1 out of 4,313 banks nationally, placing it at the 100.0th percentile on a scale where higher means riskier. A year earlier it was also at the 100.0th percentile, so the model rated it about the same as a year earlier. Of 30 ratios compared with their own prior range, which for most ratios is the prior 12 quarters, 16 were outside that range.

Return on equity, which is profit as a share of the owners' stake, was -121.2%, well below its prior range of -36.6% to -0.9%, and it pushed the score up with a contribution of +1.638 model log-odds units. The Texas ratio, which weighs troubled assets against capital plus reserves, was 257.0%, well above its prior range of 31.1% to 168.6%, and it pushed the score up with a contribution of +1.153. That ratio rose +88.5 pp over one quarter. Return on assets, which is profit as a share of everything the bank owns, was -3.4%, below its prior range of -2.2% to -0.1%, and it pushed the score up with a contribution of +0.259. The provision for loan losses, money set aside for expected bad loans, was -0.5% of assets, below its prior range of 0.0% to 0.1%, and it pushed the score up with a contribution of +0.051.

Loan write-offs net of recoveries, meaning loans the bank gave up on minus amounts later collected, were 0.9% of loans, above a prior range of 0.0% to 0.0%, yet they had little effect on the score, contributing +0.031. Losses on bonds available for sale, as a share of equity, were 1.6%, above a prior range of -2.3% to 0.2%, but this too had little effect on the score, contributing +0.029.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -121.2% | -36.6% to -0.9% | same quarter, prior 3 years | n/a | -84.6 pp | +1.638 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.9% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.9 pp | +0.031 | little effect on the score |
| the Texas ratio (troubled assets against capital plus reserves) | 257.0% | 31.1% to 168.6% | prior 12 quarters | +88.5 pp | +171.4 pp | +1.153 | pushed the score up |
| losses on bonds available for sale, as a share of equity | 1.6% | -2.3% to 0.2% | prior 12 quarters | +2.3 pp | +1.7 pp | +0.029 | little effect on the score |
| return on assets (profit as a share of assets) | -3.4% | -2.2% to -0.1% | same quarter, prior 3 years | n/a | -1.2 pp | +0.259 | pushed the score up |
| annualized provision for loan losses as a share of assets | -0.5% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | -0.5 pp | +0.051 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 95 banks in the same specialty group and size tier (under $100 million).

The bank's capital, the cushion of its own money that absorbs losses, stands out as thin on every measure shown. Its total risk-based capital ratio (capital measured against assets weighted by type) was 4.1%, at the 0.0th percentile nationally, which is unusually low, and at the 1.1st percentile among its peers against a peer median of 17.2%, unusually low among its peers too. Its Tier 1 risk-based capital ratio, which counts only the core layer of capital, was 2.9%, at the 0.0th percentile nationally, which is unusually low, and at the 1.1st percentile among its peers against a peer median of 16.5%, unusually low among its peers too. Its leverage ratio (core capital as a share of average assets) was 2.1%, at the 0.4th percentile nationally, which is unusually low, and at the 0.5th percentile among its peers against a peer median of 12.6%, unusually low among its peers too.

Its Texas ratio, which compares troubled assets with capital plus reserves, was 257.0%, at the 100.0th percentile nationally, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 3.0%, unusually high among its peers too. Nonaccrual assets and foreclosed property, meaning loans no longer paying interest plus property taken back from borrowers, were 6.8% of assets, at the 99.7th percentile nationally, which is unusually high, and at the 98.4th percentile among its peers against a peer median of 0.3%, unusually high among its peers too. Return on equity, profit as a share of the owners' stake, was -121.2%, at the 0.1st percentile nationally, which is unusually low, and at the 0.5th percentile among its peers against a peer median of 7.0%, unusually low among its peers too. The annualized provision for loan losses, the amount set aside for expected bad loans, was -0.5% of assets, at the 0.3rd percentile nationally, which is unusually low, and at the 1.6th percentile among its peers against a peer median of 0.0%, unusually low among its peers too. Annualized interest expense, what the bank pays to fund itself, was 3.4% of assets, at the 99.6th percentile nationally, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 1.5%, unusually high among its peers too.

Overall, 14 of the bank's ratios fall in the national top or bottom 10%, and 14 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 4.1% | 0.0th (unusually low) | 17.2% | 1.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 2.9% | 0.0th (unusually low) | 16.5% | 1.1st | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 257.0% | 100.0th (unusually high) | 3.0% | 99.5th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -121.2% | 0.1st (unusually low) | 7.0% | 0.5th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 6.8% | 99.7th (unusually high) | 0.3% | 98.4th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | -0.5% | 0.3rd (unusually low) | 0.0% | 1.6th | unusually low among its peers too |
| annualized interest expense as a share of assets | 3.4% | 99.6th (unusually high) | 1.5% | 99.5th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 2.1% | 0.4th (unusually low) | 12.6% | 0.5th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 63.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 781.8% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 32.7% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank's case is that it remains open and on the watchlist. The fact sheet holds no later figures, so this memo cannot add hindsight evidence beyond the weaknesses already described as of the as-of quarter.

## What happened next

Looking ahead with hindsight, our fact sheet contains no ranks, watchlist flags or reporting data from after the as-of quarter. We therefore cannot yet say how its rank moved or whether it has kept filing reports; if it stops reporting, our data would not distinguish a merger from a closure.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F5 · Model score · 2026-06-30 · 0.9965 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 6.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · -0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 31.8% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 257.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -121.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 188.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 83.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2026-06-30 · +1.705 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -121.2%; contribution to the score · 2026-06-30 · +1.638 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 257.0%; contribution to the score · 2026-06-30 · +1.153 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 9.2%; contribution to the score · 2026-06-30 · +0.544 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.1%; contribution to the score · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: construction loans as a share of loans, value 2.4%; contribution to the score · 2026-06-30 · -0.265 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.4%; contribution to the score · 2026-06-30 · -0.239 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: loan-loss reserves as a share of loans, value 1.3%; contribution to the score · 2026-06-30 · -0.098 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 31.8%; contribution to the score · 2026-06-30 · -0.070 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value 9.5%; contribution to the score · 2026-06-30 · -0.069 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -121.2% · data/features/fct_bank_features.parquet: return_on_equity
- F86 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F87 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -0.9% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +1.638 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.031 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F97 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 257.0% · data/features/fct_bank_features.parquet: texas_ratio
- F98 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 31.1% · data/features/fct_bank_features.parquet: texas_ratio
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 168.6% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +88.5 pp · data/features/fct_bank_features.parquet: texas_ratio
- F102 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +1.153 · data/analyst/scores.parquet: feature texas_ratio contribution
- F103 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F104 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F105 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -2.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F106 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F109 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · +0.029 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F110 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F111 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F113 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F115 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.259 · data/analyst/scores.parquet: feature return_on_assets contribution
- F116 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F117 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · -0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F118 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F119 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F121 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.051 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F122 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F134 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F135 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F136 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F137 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 17.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F138 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F139 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F140 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F141 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F142 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F143 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 16.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F144 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 257.0% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -121.2% · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 6.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F158 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F159 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F160 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F161 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F162 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F163 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · -0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F164 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F165 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F166 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 1.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F170 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F171 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F172 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F173 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F174 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F175 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F176 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F177 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F178 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F179 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F182 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F183 · Peers: those ratios also unusual among peers · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F185 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
