---
cert: 27567
name: "Glen Burnie Mutual Sb"
as_of: 2022-12-31
rank: 36
n_banks: 4773
percentile: 99.26670856903415
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:43"
writer_model: "claude-opus-5-5"
checked: true
---

# Glen Burnie Mutual Sb (cert 27567)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2022-12-31, Glen Burnie Mutual Sb ranked 36 out of 4,773 banks on Canary's risk score, placing it in the 99.3rd percentile and on the watchlist, the short list of highest-scoring banks. Its weak points were thin earnings and thin capital against its assets: its net interest margin (the spread earned on lending and investing) was 1.0% against a national median of 3.4%, and its leverage ratio (core capital as a share of average assets) was 7.6% against 10.3%. Its funding looked steady, with uninsured deposits (balances above the government insurance limit) at 5.5% of deposits against a national median of 25.5%. Its risk-based capital ratios, which weigh assets by how risky they are, were above the national medians, so the capital picture points two ways.

## Warning signs in the data

Capital: equity was 7.6% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 7.6% against 10.3%. The risk-based measures point the other way: the Tier 1 risk-based capital ratio was 16.1% against a median of 14.2%, and the total risk-based capital ratio was 16.8% against 15.3%. Earnings were weak, with return on assets (profit as a share of assets) at 0.1% against a median of 1.0%, interest expense at 2.2% of assets against 0.3%, and an efficiency ratio (operating costs as a share of revenue) of 88.5% against 65.1%.

Credit quality: loans 90 or more days past due or not accruing interest were 0.7% of loans against a national median of 0.2%, and nonaccrual assets plus foreclosed property were 0.5% of assets against 0.1%. The Texas ratio (troubled assets against capital plus reserves) was 7.2% against a median of 1.8%, while loan-loss reserves (money set aside for bad loans) were 0.4% of loans against 1.2%. The separate real-estate concentration check found the bank did not cross either supervisory line.

Liquidity and funding looked sound: core deposits (stable, everyday deposits) were 91.7% of assets against a median of 81.6%, and cash was 9.9% of assets against 5.2%, although the trend section notes cash had fallen below its own usual range. Loans were 86.2% of deposits against a median of 72.5%. Bond losses were small: securities were only 1.4% of assets against a median of 22.3%, losses on bonds held to maturity were 0.8% of equity against 0.0%, and losses on bonds available for sale were 0.0% against 18.6%.

## Understanding the score

As of 2022-12-31, the bank ranked 36 out of 4,773 banks, in the 99.3rd percentile on a scale of 0 to 100 where higher means riskier, and its model score was 0.0930. It was flagged for the watchlist, which covers the top 2% of banks, or 96 banks that quarter.

The five features that pushed the score up most were: low securities holdings at 1.4% of assets (+0.520), a high share of core deposits at 91.7% of assets (+0.430), very little commercial real estate lending at 0.1% of loans (+0.359), high interest expense at 2.2% of assets (+0.281), and a leverage ratio of 7.6% (+0.136). Some of these, such as plentiful core deposits, look reassuring on their own; the model reacts to how they combine with the bank's other figures, not to each one alone.

The five features that pulled the score down most were: a Tier 1 risk-based capital ratio of 16.1% (-1.006), a Texas ratio of 7.2% (-0.818), loans 90 or more days past due or not accruing interest at 0.7% of loans (-0.401), return on equity (profit as a share of the owners' stake) of 1.1% (-0.365), and a total risk-based capital ratio of 16.8% (-0.321). The model learned from 539 bank failures in its training period, 96% of which were credit-loss failures.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-03-31 | 11 | 5,044 | ▲ watchlist |
| 2021-06-30 | 11 | 5,015 | ▲ watchlist |
| 2021-09-30 | 8 | 4,979 | ▲ watchlist |
| 2021-12-31 | 7 | 4,904 | ▲ watchlist |
| 2022-03-31 | 32 | 4,861 | ▲ watchlist |
| 2022-06-30 | 31 | 4,838 | ▲ watchlist |
| 2022-09-30 | 33 | 4,813 | ▲ watchlist |
| 2022-12-31 | 36 | 4,773 | ▲ watchlist |

## How its ratios moved

As of 2022-12-31, Glen Burnie Mutual Sb ranked 36 out of 4,773 banks nationally, placing it in the 99.3rd percentile, where higher means riskier. A year earlier, on 2021-12-31, it sat in the 99.9th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own range over the prior 12 quarters, and 10 of the 30 ratios checked were outside that range.

Cash as a share of assets fell to 9.9%, below its prior range of 15.6% to 22.7%, and it added +0.082 model log-odds units (the model's internal scoring units), so it pushed the score up. The efficiency ratio, meaning operating costs as a share of revenue, rose to 88.5%, above its prior range of 71.7% to 80.5%, yet its contribution of -0.115 pushed the score down. Return on equity, meaning profit as a share of the owners' stake, dropped to 1.1%, below its prior range of 2.4% to 4.2%, but its contribution of -0.365 also pushed the score down.

Deposit growth slowed to 1.6%, below its prior range of 2.1% to 4.7%, and its contribution of -0.167 pushed the score down. Construction loans rose to 4.0% of all loans, above their prior range of 2.0% to 3.7%, while their contribution of -0.229 pushed the score down. In several of these cases the ratio moved outside its usual range, but the model still treated it as lowering the score rather than raising it.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 88.5% | 71.7% to 80.5% | same quarter, prior 3 years | n/a | +8.3 pp | -0.115 | pushed the score down |
| cash as a share of assets | 9.9% | 15.6% to 22.7% | prior 12 quarters | -10.4 pp | -9.1 pp | +0.082 | pushed the score up |
| return on equity (profit as a share of equity) | 1.1% | 2.4% to 4.2% | same quarter, prior 3 years | n/a | -3.1 pp | -0.365 | pushed the score down |
| asset growth over the past four quarters | 1.6% | 2.2% to 4.6% | prior 12 quarters | -1.4 pp | -2.5 pp | -0.051 | pushed the score down |
| deposit growth over the past four quarters | 1.6% | 2.1% to 4.7% | prior 12 quarters | -1.5 pp | -2.5 pp | -0.167 | pushed the score down |
| construction loans as a share of loans | 4.0% | 2.0% to 3.7% | prior 12 quarters | +0.3 pp | +0.7 pp | -0.229 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2022-12-31: Mortgage Lending Specialization.

Peers: 179 banks in the same specialty group and size tier ($100 million to $1 billion).

Interest expense, what the bank pays on its deposits and borrowings, was 2.2% of assets, the 100.0th percentile nationally and unusually high; at the 99.7th percentile among its peers, against a peer median of 0.3%, it was unusually high among its peers too. Net interest margin, the spread earned on lending and investing, was 1.0%, the 1.0th percentile nationally and unusually low; at the 0.8th percentile among its peers, against a peer median of 3.0%, it was unusually low among its peers too. Return on assets, profit as a share of assets, was 0.1%, the 4.8th percentile nationally and unusually low; at the 8.7th percentile among its peers, against a peer median of 0.5%, it was unusually low among its peers too. The leverage ratio, core capital as a share of average assets, was 7.6%, the 3.4th percentile nationally and unusually low; at the 4.7th percentile among its peers, against a peer median of 12.2%, it was unusually low among its peers too.

Volatile funding, money that can leave the bank quickly, was 0.0% of assets, the 1.8th percentile nationally and unusually low; at the 0.6th percentile among its peers, against a peer median of 6.6%, it was unusually low among its peers too. Uninsured deposits, balances above the government insurance limit, were 5.5% of deposits, the 2.3rd percentile nationally and unusually low; at the 8.7th percentile among its peers, against a peer median of 14.3%, they were unusually low among its peers too. Commercial real estate loans, loans backed by business property, were 0.1% of loans, the 2.4th percentile nationally and unusually low; at the 9.4th percentile among its peers, against a peer median of 8.9%, they were unusually low among its peers too. Loan-loss reserves, money set aside to cover loans that may go bad, were 0.4% of loans, the 2.8th percentile nationally and unusually low; at the 13.4th percentile among its peers, against a peer median of 0.9%, they were typical for its peer group.

Overall, 13 of the bank's ratios fell in the national top or bottom 10%, and 9 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 2.2% | 100.0th (unusually high) | 0.3% | 99.7th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 1.0% | 1.0th (unusually low) | 3.0% | 0.8th | unusually low among its peers too |
| volatile funding as a share of assets | 0.0% | 1.8th (unusually low) | 6.6% | 0.6th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 5.5% | 2.3rd (unusually low) | 14.3% | 8.7th | unusually low among its peers too |
| commercial real estate loans as a share of loans | 0.1% | 2.4th (unusually low) | 8.9% | 9.4th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 0.4% | 2.8th (unusually low) | 0.9% | 13.4th | typical for its peer group |
| the leverage ratio (core capital as a share of average assets) | 7.6% | 3.4th (unusually low) | 12.2% | 4.7th | unusually low among its peers too |
| return on assets (profit as a share of assets) | 0.1% | 4.8th (unusually low) | 0.5% | 8.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 39.6% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 41.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 59.9% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

With hindsight, this flag was a false alarm: the bank kept reporting and was not flagged again in any later quarter in our data, through 2026-06-30. Its rank eased to 101 by 2023-03-31 and to 273 by 2023-12-31, both outside the watchlist. The flag reflected an unusual profile of thin earnings and thin capital against assets rather than signs of heavy loan losses, and the later quarters show that profile did not lead to the outcome the model screens for.

## What happened next

In hindsight, the bank stayed off the watchlist in every later quarter we have, ranking 101 on 2023-03-31, 108 on 2023-06-30, 199 on 2023-09-30 and 273 on 2023-12-31. In 2024 it ranked 289 on 2024-03-31, 541 on 2024-06-30, 189 on 2024-09-30 and 426 on 2024-12-31. In 2025 it ranked 253 on 2025-03-31, 141 on 2025-06-30, 322 on 2025-09-30 and 255 on 2025-12-31.

It was still reporting in the latest quarters in our data, ranking 266 on 2026-03-31 and 209 on 2026-06-30, neither flagged.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 101 | 4,740 |  |
| 2023-06-30 | 108 | 4,714 |  |
| 2023-09-30 | 199 | 4,686 |  |
| 2023-12-31 | 273 | 4,658 |  |
| 2024-03-31 | 289 | 4,640 |  |
| 2024-06-30 | 541 | 4,610 |  |
| 2024-09-30 | 189 | 4,589 |  |
| 2024-12-31 | 426 | 4,560 |  |
| 2025-03-31 | 253 | 4,536 |  |
| 2025-06-30 | 141 | 4,494 |  |
| 2025-09-30 | 322 | 4,452 |  |
| 2025-12-31 | 255 | 4,411 |  |
| 2026-03-31 | 266 | 4,353 |  |
| 2026-06-30 | 209 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Glen Burnie Mutual Sb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F5 · Model score · 2022-12-31 · 0.0930 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2022-12-31 · 36 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2022-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 16.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2022-12-31 · 16.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2022-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2022-12-31 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2022-12-31 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2022-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2022-12-31 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2022-12-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 1.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2022-12-31 · 88.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2022-12-31 · 65.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2022-12-31 · 86.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2022-12-31 · 72.5% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 5.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2022-12-31 · 91.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2022-12-31 · 81.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2022-12-31 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2022-12-31 · 5.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2022-12-31 · 1.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2022-12-31 · 22.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: securities as a share of assets, value 1.4%; contribution to the score · 2022-12-31 · +0.520 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: core deposits as a share of assets, value 91.7%; contribution to the score · 2022-12-31 · +0.430 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 0.1%; contribution to the score · 2022-12-31 · +0.359 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.2%; contribution to the score · 2022-12-31 · +0.281 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 7.6%; contribution to the score · 2022-12-31 · +0.136 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 16.1%; contribution to the score · 2022-12-31 · -1.006 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 7.2%; contribution to the score · 2022-12-31 · -0.818 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2022-12-31 · -0.401 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 1.1%; contribution to the score · 2022-12-31 · -0.365 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 16.8%; contribution to the score · 2022-12-31 · -0.321 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F85 · Rank in a later quarter (2023-03-31), not flagged · 2023-03-31 · 101 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2023-06-30), not flagged · 2023-06-30 · 108 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2023-09-30), not flagged · 2023-09-30 · 199 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2023-12-31), not flagged · 2023-12-31 · 273 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2024-03-31), not flagged · 2024-03-31 · 289 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2024-06-30), not flagged · 2024-06-30 · 541 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F91 · Rank in a later quarter (2024-09-30), not flagged · 2024-09-30 · 189 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F92 · Rank in a later quarter (2024-12-31), not flagged · 2024-12-31 · 426 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F93 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 253 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F94 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 141 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 322 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F96 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 255 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F97 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 266 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F98 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 209 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F99 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F100 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2022-12-31 · 88.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 71.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 80.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2022-12-31 · -0.115 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F108 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F109 · Trend: cash as a share of assets, value at the as-of quarter · 2022-12-31 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F110 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 15.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F111 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 22.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · +0.082 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F115 · Trend: cash as a share of assets, what the model did with it · 2022-12-31 · pushed the score up · data/analyst/scores.parquet: feature cash_to_assets contribution
- F116 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2022-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_equity
- F117 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: return_on_equity
- F118 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: return_on_equity
- F120 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2022-12-31 · -0.365 · data/analyst/scores.parquet: feature return_on_equity contribution
- F121 · Trend: return on equity (profit as a share of equity), what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F129 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2022-12-31 · 1.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F131 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F134 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.167 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F136 · Trend: construction loans as a share of loans, value at the as-of quarter · 2022-12-31 · 4.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F137 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F138 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F141 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2022-12-31 · -0.229 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F142 · Trend: construction loans as a share of loans, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F143 · Trend: ratios outside their own prior range · 2022-12-31 · 10 · data/features/fct_bank_features.parquet
- F145 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F146 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F148 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F149 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F153 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F154 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2022-12-31 · 100.0th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F155 · Peers: annualized interest expense as a share of assets, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F156 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2022-12-31 · 99.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F157 · Peers: annualized interest expense as a share of assets, peer median · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F158 · Peers: annualized interest expense as a share of assets, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F159 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2022-12-31 · 1.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F160 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2022-12-31 · 1.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F161 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F162 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2022-12-31 · 0.8th · data/features/fct_bank_features.parquet: net_interest_margin
- F163 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2022-12-31 · 3.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F164 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F165 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F166 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2022-12-31 · 1.8th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F167 · Peers: volatile funding as a share of assets, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F168 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2022-12-31 · 0.6th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F169 · Peers: volatile funding as a share of assets, peer median · 2022-12-31 · 6.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F170 · Peers: volatile funding as a share of assets, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F171 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2022-12-31 · 5.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F172 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2022-12-31 · 2.3rd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F173 · Peers: uninsured deposits as a share of deposits, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F174 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2022-12-31 · 8.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F175 · Peers: uninsured deposits as a share of deposits, peer median · 2022-12-31 · 14.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F176 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F177 · Peers: commercial real estate loans as a share of loans, bank value at the as-of quarter · 2022-12-31 · 0.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F178 · Peers: commercial real estate loans as a share of loans, national percentile (100 = highest value among all banks) · 2022-12-31 · 2.4th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F179 · Peers: commercial real estate loans as a share of loans, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F180 · Peers: commercial real estate loans as a share of loans, percentile among its peers (100 = highest value) · 2022-12-31 · 9.4th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F181 · Peers: commercial real estate loans as a share of loans, peer median · 2022-12-31 · 8.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F182 · Peers: commercial real estate loans as a share of loans, reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F183 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2022-12-31 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F184 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2022-12-31 · 2.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F185 · Peers: loan-loss reserves as a share of loans, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F186 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2022-12-31 · 13.4th · data/features/fct_bank_features.parquet: allowance_to_loans
- F187 · Peers: loan-loss reserves as a share of loans, peer median · 2022-12-31 · 0.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F188 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F189 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F190 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2022-12-31 · 3.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F191 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F192 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2022-12-31 · 4.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F193 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2022-12-31 · 12.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F194 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F195 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2022-12-31 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F196 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2022-12-31 · 4.8th · data/features/fct_bank_features.parquet: return_on_assets
- F197 · Peers: return on assets (profit as a share of assets), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F198 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2022-12-31 · 8.7th · data/features/fct_bank_features.parquet: return_on_assets
- F199 · Peers: return on assets (profit as a share of assets), peer median · 2022-12-31 · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F200 · Peers: return on assets (profit as a share of assets), reading against its peers · 2022-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F202 · Peers: ratios in the national top or bottom 10% · 2022-12-31 · 13 · data/features/fct_bank_features.parquet
- F203 · Peers: those ratios also unusual among peers · 2022-12-31 · 9 · data/features/fct_bank_features.parquet
- F205 · Peers: cut-off for unusual (top or bottom share of banks) · 2022-12-31 · 10% · data/features/fct_bank_features.parquet
