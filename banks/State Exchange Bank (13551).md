---
cert: 13551
name: "State Exchange Bank"
as_of: 2026-06-30
rank: 31
n_banks: 4313
percentile: 99.30442847206122
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# State Exchange Bank (cert 13551)

*Outcome not yet known.*

## Summary

As of 2026-06-30, State Exchange Bank, a small Oklahoma lender with $89.6 million in assets, ranked 31 out of 4,313 banks nationally on Canary's risk score, placing it in the 99.3rd percentile, where higher means riskier. That rank put it on the watchlist, which covers the top 2% of banks. The main concern is loan quality: loans 90+ days past due or not accruing interest were 6.9% of loans, against a national median of 0.5%. Its capital cushion sits close to the national median, and it leans on brokered deposits (money placed through outside middlemen) at 18.4% of deposits, though that share has been falling.

## Warning signs in the data

Capital, the owners' cushion against losses, looks roughly average: equity was 10.9% of assets against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 10.7%, slightly below the national median of 11.0%.

Credit quality is the clearest weak spot. Loans 90+ days past due or not accruing interest were 6.9% of loans, far above the national median of 0.5%, and loans 30-89 days past due were 3.5% of assets against a median of 0.2%. Nonaccrual assets and foreclosed property were 3.3% of assets versus a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 37.5%, well above the median of 2.9%. The bank has set aside more than most: loan-loss reserves were 2.8% of loans against a median of 1.2%, while net write-offs ran at 0.6% of loans versus a median of 0.0%.

On funding, brokered deposits were 18.4% of deposits while the national median was 0.0%, and core deposits (steady, everyday customer deposits) were 64.2% of assets, below the median of 75.5%. Deposits shrank by -7.5% over the past four quarters while the national median grew 4.2%, and interest expense was 2.5% of assets against a median of 1.6%. Pointing the other way, cash was 22.1% of assets, well above the median of 6.2%, and the trend section shows the brokered share falling and core deposits rising. Bond losses are small: losses on bonds available for sale were 0.9% of equity, well below the median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median. Commercial real estate loans were a higher share of loans than the national median, yet the concentration section found the bank did not cross either regulatory screening line.

## Understanding the score

State Exchange Bank ranked 31 out of 4,313 banks on 2026-06-30, the 99.3rd percentile on a scale from 0 to 100 where higher means riskier. It was flagged for the watchlist, one of 87 banks in the top 2% that quarter.

Five features pushed the score up most: loans 90+ days past due or not accruing interest at 6.9% of loans (+1.050), brokered deposits at 18.4% of deposits (+0.760), loans 30-89 days past due at 3.5% of assets (+0.398), interest expense at 2.5% of assets (+0.355), and losses on bonds available for sale at 0.9% of equity (+0.084).

Five features pushed it down most: the Tier 1 risk-based capital ratio, a measure of core capital against the bank's riskier assets (-0.778), return on equity (profit as a share of equity) at 8.3% (-0.614), the Texas ratio at 37.5% (-0.471), return on assets at 0.9% (-0.419), and construction loans at 5.4% of loans (-0.319). Note that the Texas ratio of 37.5% is well above the national median of 2.9%, yet in this model it lowered the score rather than raising it; the two readings point different ways.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 5 | 4,589 | ▲ watchlist |
| 2024-12-31 | 11 | 4,560 | ▲ watchlist |
| 2025-03-31 | 9 | 4,536 | ▲ watchlist |
| 2025-06-30 | 5 | 4,494 | ▲ watchlist |
| 2025-09-30 | 11 | 4,452 | ▲ watchlist |
| 2025-12-31 | 28 | 4,411 | ▲ watchlist |
| 2026-03-31 | 36 | 4,353 | ▲ watchlist |
| 2026-06-30 | 31 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, State Exchange Bank ranked 31 out of 4,313 banks nationally, placing it in the 99.3rd percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 99.9th percentile, so the model's rating is about the same as a year earlier. Each ratio is compared with its own values over the prior 12 quarters, and 5 of the 28 ratios checked this way sat outside that prior range.

Brokered deposits (money placed with the bank through outside middlemen) were 18.4% of deposits, below their prior range of 25.0% to 31.4%, yet this ratio still pushed the score up, contributing +0.760 model log-odds units (the model's internal scoring scale, where positive raises the score). That share fell by -6.6 pp over one quarter and by -10.2 pp over four quarters. Core deposits (steady, everyday customer deposits) were 64.2% of assets, above their prior range of 51.0% to 58.7%, and this ratio pushed the score down, contributing -0.133. Construction loans were 5.4% of loans, just above their prior range of 0.0% to 5.2%, yet this ratio pushed the score down, contributing -0.319.

Commercial real estate loans (loans on business properties) were 29.2% of loans, below their prior range of 31.5% to 35.5%, but this ratio had little effect on the score, contributing -0.050. Equity (the owners' cushion against losses) was 10.9% of assets, above its prior range of 8.9% to 10.4%, yet it also had little effect on the score, contributing -0.030. So although several ratios moved outside their usual range, only the brokered deposit share pushed the score up, while the others pushed it down or barely moved it.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| brokered deposits as a share of deposits | 18.4% | 25.0% to 31.4% | prior 12 quarters | -6.6 pp | -10.2 pp | +0.760 | pushed the score up |
| core deposits as a share of assets | 64.2% | 51.0% to 58.7% | prior 12 quarters | +5.5 pp | +12.1 pp | -0.133 | pushed the score down |
| commercial real estate loans as a share of loans | 29.2% | 31.5% to 35.5% | prior 12 quarters | -3.5 pp | -6.3 pp | -0.050 | little effect on the score |
| equity as a share of assets | 10.9% | 8.9% to 10.4% | prior 12 quarters | +0.5 pp | +1.4 pp | -0.030 | little effect on the score |
| construction loans as a share of loans | 5.4% | 0.0% to 5.2% | prior 12 quarters | +0.3 pp | +1.1 pp | -0.319 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 227 banks in the same specialty group and size tier (under $100 million).

Loans 30-89 days past due (borrowers who are behind on payments, but not yet seriously) were 3.5% of assets, at the 99.2nd percentile nationally, which is unusually high; among its peers the bank sits at the 98.5th percentile against a peer median of 0.2%, unusually high among its peers too. Loans 90+ days past due or not accruing interest (loans the bank no longer expects to be paid normally) were 6.9% of loans, at the 98.9th percentile nationally, which is unusually high; among its peers it sits at the 94.9th percentile against a peer median of 0.4%, unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 37.5%, at the 98.6th percentile nationally, which is unusually high; among its peers it sits at the 96.7th percentile against a peer median of 2.2%, unusually high among its peers too. Nonaccrual assets and foreclosed property (bad loans plus property taken back from borrowers) were 3.3% of assets, at the 98.1st percentile nationally, which is unusually high; among its peers it sits at the 97.1st percentile against a peer median of 0.1%, unusually high among its peers too.

Loan-loss reserves (money set aside to cover expected loan losses) were 2.8% of loans, at the 97.0th percentile nationally, which is unusually high; among its peers it sits at the 89.2nd percentile against a peer median of 1.3%, typical for its peer group. The annualized provision for loan losses (the yearly rate at which the bank adds to those reserves) was 0.4% of assets, at the 95.0th percentile nationally, which is unusually high; among its peers it sits at the 95.4th percentile against a peer median of 0.0%, unusually high among its peers too.

Deposit growth over the past four quarters was -7.5%, at the 3.4th percentile nationally, which is unusually low; among its peers it sits at the 3.3rd percentile against a peer median of 3.4%, unusually low among its peers too. Asset growth over the past four quarters was -6.0%, at the 3.9th percentile nationally, which is unusually low; among its peers it sits at the 4.2nd percentile against a peer median of 4.0%, unusually low among its peers too. Overall, 12 of the bank's ratios fall in the national top or bottom 10%, and 10 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 3.5% | 99.2nd (unusually high) | 0.2% | 98.5th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 6.9% | 98.9th (unusually high) | 0.4% | 94.9th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 37.5% | 98.6th (unusually high) | 2.2% | 96.7th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 3.3% | 98.1st (unusually high) | 0.1% | 97.1st | unusually high among its peers too |
| loan-loss reserves as a share of loans | 2.8% | 97.0th (unusually high) | 1.3% | 89.2nd | typical for its peer group |
| deposit growth over the past four quarters | -7.5% | 3.4th (unusually low) | 3.4% | 3.3rd | unusually low among its peers too |
| asset growth over the past four quarters | -6.0% | 3.9th (unusually low) | 4.0% | 4.2nd | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 0.4% | 95.0th (unusually high) | 0.0% | 95.4th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 29.3% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 118.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -42.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank remains an open watchlist case, meaning it was flagged at the as-of quarter and our data records no failure. The fact sheet contains no data from after the as-of quarter, so we cannot say from it whether the weak loan quality behind the flag improved or worsened. A watchlist flag marks a bank whose figures resemble those of past failures; many flagged banks stay open.

## What happened next

In hindsight: no later ranks, flags or reporting status for this bank are included in this fact sheet. The score history table added below shows whatever later quarters are available. Until newer data arrives, the bank should be read as open and on the watchlist.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 31 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 37.5% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 18.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 64.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 22.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: total assets · 2026-06-30 · $89.6 million · data/features/fct_bank_features.parquet: log_total_assets
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -7.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 6.9%; contribution to the score · 2026-06-30 · +1.050 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 18.4%; contribution to the score · 2026-06-30 · +0.760 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: loans 30-89 days past due, as a share of assets, value 3.5%; contribution to the score · 2026-06-30 · +0.398 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.355 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: losses on bonds available for sale, as a share of equity, value 0.9%; contribution to the score · 2026-06-30 · +0.084 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.778 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 8.3%; contribution to the score · 2026-06-30 · -0.614 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 37.5%; contribution to the score · 2026-06-30 · -0.471 · data/analyst/scores.parquet: feature texas_ratio contribution
- F79 · Driver down #4: return on assets (profit as a share of assets), value 0.9%; contribution to the score · 2026-06-30 · -0.419 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #5: construction loans as a share of loans, value 5.4%; contribution to the score · 2026-06-30 · -0.319 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 18.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F82 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F83 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 31.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F84 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · -6.6 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F85 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · -10.2 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F86 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.760 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F87 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F88 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 64.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F89 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 51.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F90 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 58.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F93 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.133 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F94 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F95 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 29.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F96 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 31.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F97 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 35.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F100 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.050 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F101 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F102 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F103 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F104 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F107 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.030 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F108 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F109 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F110 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F111 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 5.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F114 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.319 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F115 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F116 · Trend: ratios outside their own prior range · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F118 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F119 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F121 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F122 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F126 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F127 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F128 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F129 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.5th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F130 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F131 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F132 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F133 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F134 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F135 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 94.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F136 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F137 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 37.5% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F148 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F149 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F150 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F151 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F152 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F153 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 89.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F154 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F155 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F156 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -7.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F157 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F158 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F159 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 3.3rd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F160 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F162 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -6.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F163 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.9th · data/features/fct_bank_features.parquet: asset_growth_4q
- F164 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F165 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 4.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F166 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F167 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F168 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F170 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F171 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.4th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F172 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F173 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F175 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F176 · Peers: those ratios also unusual among peers · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F178 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
