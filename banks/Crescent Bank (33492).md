---
cert: 33492
name: "Crescent Bank"
as_of: 2024-12-31
rank: 59
n_banks: 4560
percentile: 98.7280701754386
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Crescent Bank (cert 33492)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2024-12-31, Crescent Bank ranked 59 out of 4,560 banks on Canary's risk score, which places it in the 98.7th percentile, where higher means riskier. That rank put it on the watchlist, the 2% of banks with the highest scores, which held 92 banks that quarter. The clearest strain was in its loans: loans 30-89 days past due equaled 17.6% of assets, against a national median of 0.2%, and net write-offs (loans given up as lost, minus recoveries) ran at 11.4% of loans, against a median of 0.0%. Its capital cushion against losses sat near or somewhat below typical levels, while its funding costs were well above the norm.

## Warning signs in the data

Credit quality, meaning how well borrowers are repaying, stands out most. Loans 90 or more days past due or no longer earning interest were 3.3% of loans, well above the national median of 0.4%. Loans 30-89 days past due equaled 17.6% of assets, far above the national median of 0.2%. Nonaccrual assets and foreclosed property were 1.3% of assets, against a national median of 0.2%. The bank set aside an annualized provision (money charged against profit for expected loan losses) of 8.4% of assets, versus a national median of 0.1%, and its loan-loss reserves stood at 11.2% of loans, versus 1.2%. Its Texas ratio, which weighs troubled assets against capital plus reserves, was 15.7%, well above the national median of 2.3%.

Capital, the owners' cushion that absorbs losses, was mixed. Equity was 9.1% of assets, a little below the national median of 9.7%, while the leverage ratio (core capital as a share of average assets) was 10.8%, slightly above the median of 10.6%. The Tier 1 risk-based capital ratio, which measures core capital against riskier assets, was 12.4% versus a national median of 14.3%, and the total risk-based capital ratio was 13.7% versus 15.5%. Profit was slightly negative, with a return on assets of -0.2% against a national median of 0.9%, even though its net interest margin (the spread earned on lending and investing) was 14.0% versus 3.4%.

On funding, annualized interest expense was 4.2% of assets, well above the national median of 1.8%, and deposits shrank by -19.5% over the past four quarters while the median bank grew them by 3.9%. Volatile funding, money that can leave quickly, was 18.3% of assets versus a median of 8.8%, and brokered deposits (funds placed through middlemen) were 3.6% of deposits versus 0.0%, though uninsured deposits were only 4.6% of deposits versus 24.1%. Unrealized losses on bonds available for sale were 10.0% of equity, close to the national median of 11.2%.

## Understanding the score

Crescent Bank ranked 59 out of 4,560 banks nationally as of 2024-12-31, which is the 98.7th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score and included 92 banks that quarter.

Five features pushed the score up the most. The largest was annualized interest expense as a share of assets, at 4.2%, adding +0.688. Next came losses on bonds available for sale, at 10.0% of equity, adding +0.673. The annualized provision for loan losses, at 8.4% of assets, added +0.562. The efficiency ratio (operating costs as a share of revenue), at 45.3%, added +0.290. Commercial real estate loans, at 1.9% of loans, added +0.147.

Five features pulled the score down the most. The Tier 1 risk-based capital ratio, at 12.4%, had the biggest effect at -1.220. Deposit growth over the past four quarters, at -19.5%, contributed -0.403. The Texas ratio, at 15.7%, contributed -0.402. Return on equity (profit as a share of equity), at -2.8%, contributed -0.363. The leverage ratio, at 10.8%, contributed -0.261.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 6 | 4,740 | ▲ watchlist |
| 2023-06-30 | 11 | 4,714 | ▲ watchlist |
| 2023-09-30 | 21 | 4,686 | ▲ watchlist |
| 2023-12-31 | 55 | 4,658 | ▲ watchlist |
| 2024-03-31 | 64 | 4,640 | ▲ watchlist |
| 2024-06-30 | 59 | 4,610 | ▲ watchlist |
| 2024-09-30 | 44 | 4,589 | ▲ watchlist |
| 2024-12-31 | 59 | 4,560 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked this way at 2024-12-31, 8 were outside their prior range, and the table shows the 6 furthest outside. Overall, the model rated the bank about the same as a year earlier, at the 98.7th percentile versus the 98.8th percentile then.

Annualized interest expense was 4.2% of assets, above its prior range of 1.2% to 3.1%, and it pushed the score up by +0.688 model log-odds units. Loans 30-89 days past due reached 17.6% of assets, above its prior range of 9.4% to 15.9%, and pushed the score up by +0.147. Net loan write-offs were 11.4% of loans, above their prior range of 3.5% to 8.8%, yet they had little effect on the score, at -0.023. Loans 90 or more days past due or not accruing interest were 3.3% of loans, just above the prior range of 2.0% to 3.2%, but this had little effect on the score, at +0.017.

Brokered deposits were 3.6% of deposits, above their prior range of 0.9% to 3.3%, yet the model pushed the score down for them, by -0.155. Deposit growth over the past four quarters was -19.5%, below its prior range of -14.7% to 51.3%, after a change of -21.7 pp, and even so it pushed the score down, by -0.403.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 4.2% | 1.2% to 3.1% | same quarter, prior 3 years | n/a | +1.1 pp | +0.688 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 11.4% | 3.5% to 8.8% | same quarter, prior 3 years | n/a | +2.6 pp | -0.023 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 17.6% | 9.4% to 15.9% | prior 12 quarters | +1.7 pp | +2.8 pp | +0.147 | pushed the score up |
| brokered deposits as a share of deposits | 3.6% | 0.9% to 3.3% | prior 12 quarters | +0.3 pp | +0.7 pp | -0.155 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 3.3% | 2.0% to 3.2% | prior 12 quarters | +0.4 pp | +0.1 pp | +0.017 | little effect on the score |
| deposit growth over the past four quarters | -19.5% | -14.7% to 51.3% | prior 12 quarters | -4.8 pp | -21.7 pp | -0.403 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2024-12-31: Consumer Lending Specialization.

Peers: 40 banks in the same specialty group (all sizes), because fewer than 15 shared its size tier.

Loans 30-89 days past due were 17.6% of assets, at the 100.0th national percentile, which is unusually high, and at the 98.8th percentile among peers against a peer median of 0.7%, unusually high among its peers too. The annualized provision for loan losses was 8.4% of assets, at the 99.9th national percentile, unusually high, and at the 96.2nd percentile among peers against a peer median of 0.1%, unusually high among its peers too. Net loan write-offs were 11.4% of loans, at the 99.9th national percentile, unusually high, and at the 98.8th percentile among peers against a peer median of 0.2%, unusually high among its peers too. Loan-loss reserves were 11.2% of loans, at the 99.9th national percentile, unusually high, and at the 98.8th percentile among peers against a peer median of 1.0%, unusually high among its peers too.

The net interest margin was 14.0%, at the 99.8th national percentile, unusually high, and at the 96.2nd percentile among peers against a peer median of 3.8%, unusually high among its peers too. Annualized interest expense was 4.2% of assets, at the 99.7th national percentile, unusually high, and at the 98.8th percentile among peers against a peer median of 2.1%, unusually high among its peers too. Deposit growth over the past four quarters was -19.5%, at the 0.5th national percentile, unusually low, and at the 3.8th percentile among peers against a peer median of 6.0%, unusually low among its peers too. Asset growth over the past four quarters was -18.2%, at the 0.5th national percentile, unusually low, and at the 3.8th percentile among peers against a peer median of 2.9%, unusually low among its peers too.

Overall, 18 of the bank's ratios fell in the national top or bottom 10%, and 12 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 17.6% | 100.0th (unusually high) | 0.7% | 98.8th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 8.4% | 99.9th (unusually high) | 0.1% | 96.2nd | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 11.4% | 99.9th (unusually high) | 0.2% | 98.8th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 11.2% | 99.9th (unusually high) | 1.0% | 98.8th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 14.0% | 99.8th (unusually high) | 3.8% | 96.2nd | unusually high among its peers too |
| annualized interest expense as a share of assets | 4.2% | 99.7th (unusually high) | 2.1% | 98.8th | unusually high among its peers too |
| deposit growth over the past four quarters | -19.5% | 0.5th (unusually low) | 6.0% | 3.8th | unusually low among its peers too |
| asset growth over the past four quarters | -18.2% | 0.5th (unusually low) | 2.9% | 3.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 8.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 16.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

In hindsight, this was a false alarm. At 2024-12-31 the bank ranked 59 and was flagged, driven mainly by high interest expense of 4.2% of assets, bond losses of 10.0% of equity and a loan-loss provision of 8.4% of assets. Looking at later data, it dropped off the watchlist by the next quarter, ranking 240 at 2025-03-31 without a flag. It kept reporting through 2026-06-30, when it ranked 4,037 and was still not flagged. Its heavy loan losses resembled the credit-loss pattern seen in 96% of the 539 training failures, which helps explain the high score, but the bank stayed open in our data.

## What happened next

With hindsight, the bank was not flagged in any later quarter in our data. It ranked 240 at 2025-03-31, 244 at 2025-06-30 and 299 at 2025-09-30. Its rank rose again to 145 at 2025-12-31, still below the watchlist cut, then fell sharply to 3,355 at 2026-03-31 and 4,037 at 2026-06-30. The bank was still filing reports as of 2026-06-30, the latest quarter in our data.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2025-03-31 | 240 | 4,536 |  |
| 2025-06-30 | 244 | 4,494 |  |
| 2025-09-30 | 299 | 4,452 |  |
| 2025-12-31 | 145 | 4,411 |  |
| 2026-03-31 | 3,355 | 4,353 |  |
| 2026-06-30 | 4,037 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Crescent Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-12-31 · 2024-12-31 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2024-12-31 · 59 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-12-31 · 4,560 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-12-31 · 98.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-12-31 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-12-31 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-12-31 · 9.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-12-31 · 12.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-12-31 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2024-12-31 · 13.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2024-12-31 · 15.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2024-12-31 · 1.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2024-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2024-12-31 · 8.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2024-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-12-31 · 15.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-12-31 · 2.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-12-31 · -0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 14.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2024-12-31 · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-12-31 · 4.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-12-31 · 24.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2024-12-31 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2024-12-31 · 18.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2024-12-31 · 8.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-12-31 · 10.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2024-12-31 · 3.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: annualized interest expense as a share of assets, value 4.2%; contribution to the score · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 10.0%; contribution to the score · 2024-12-31 · +0.673 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized provision for loan losses as a share of assets, value 8.4%; contribution to the score · 2024-12-31 · +0.562 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 45.3%; contribution to the score · 2024-12-31 · +0.290 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 1.9%; contribution to the score · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 12.4%; contribution to the score · 2024-12-31 · -1.220 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -19.5%; contribution to the score · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 15.7%; contribution to the score · 2024-12-31 · -0.402 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value -2.8%; contribution to the score · 2024-12-31 · -0.363 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 10.8%; contribution to the score · 2024-12-31 · -0.261 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F85 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 240 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 244 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 299 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 145 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 3,355 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 4,037 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F105 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · -0.023 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F108 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F109 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 15.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F112 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F113 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F114 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2024-12-31 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F119 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2024-12-31 · -0.155 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F120 · Trend: brokered deposits as a share of deposits, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F121 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F122 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F126 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · +0.017 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F127 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F128 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F129 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -14.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 51.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F132 · Trend: deposit growth over the past four quarters, change over four quarters, in percentage points · 2024-12-31 · -21.7 pp · data/features/fct_bank_features.parquet: deposit_growth_4q
- F133 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F134 · Trend: deposit growth over the past four quarters, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: ratios outside their own prior range · 2024-12-31 · 8 · data/features/fct_bank_features.parquet
- F136 · Trend: ratios shown in the table (the furthest outside their prior range) · 2024-12-31 · 6 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2024-12-31 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2023-12-31 · 98.8% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2024-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F145 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F146 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F147 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F148 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F149 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2024-12-31 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F150 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F151 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2024-12-31 · 8.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 96.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F155 · Peers: annualized provision for loan losses as a share of assets, peer median · 2024-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F164 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: allowance_to_loans
- F165 · Peers: loan-loss reserves as a share of loans, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F166 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F167 · Peers: loan-loss reserves as a share of loans, peer median · 2024-12-31 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F168 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2024-12-31 · 14.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F170 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2024-12-31 · 99.8th · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: net_interest_margin
- F172 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2024-12-31 · 96.2nd · data/features/fct_bank_features.parquet: net_interest_margin
- F173 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2024-12-31 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F174 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F175 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F176 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F177 · Peers: annualized interest expense as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F178 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F179 · Peers: annualized interest expense as a share of assets, peer median · 2024-12-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F180 · Peers: annualized interest expense as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F181 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F182 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2024-12-31 · 0.5th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F183 · Peers: deposit growth over the past four quarters, national reading · 2024-12-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F184 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2024-12-31 · 3.8th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F185 · Peers: deposit growth over the past four quarters, peer median · 2024-12-31 · 6.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F186 · Peers: deposit growth over the past four quarters, reading against its peers · 2024-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F187 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2024-12-31 · -18.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F188 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2024-12-31 · 0.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: asset growth over the past four quarters, national reading · 2024-12-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F190 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2024-12-31 · 3.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F191 · Peers: asset growth over the past four quarters, peer median · 2024-12-31 · 2.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, reading against its peers · 2024-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: ratios in the national top or bottom 10% · 2024-12-31 · 18 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2024-12-31 · 12 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2024-12-31 · 10% · data/features/fct_bank_features.parquet
