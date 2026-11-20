---
cert: 34995
name: "First Central Bank Mccook"
as_of: 2025-12-31
rank: 82
n_banks: 4411
percentile: 98.16368170482885
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:17:04"
writer_model: "claude-opus-5-5"
checked: true
---

# First Central Bank Mccook (cert 34995)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2025-12-31, Canary's model ranked First Central Bank Mccook, a Nebraska bank, 82 out of 4,411 FDIC-insured banks, placing it at the 98.2nd percentile and on the watchlist. The main concern is credit quality: loans 90 or more days past due or not accruing interest were 6.4% of loans, far above the national median of 0.4%. Funding also leaned on brokered deposits (money placed through outside middlemen) at 18.9% of deposits, against a national median of 0.0%. Pulling the other way, its capital ratios were close to the national medians and had risen above their own recent range, and the model rated it safer than a year earlier.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90 or more days past due or not accruing interest were 6.4% of loans, against a national median of 0.4%. Nonaccrual assets (loans that have stopped earning interest) plus foreclosed property were 4.5% of assets, well above the national median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 37.6%, far above the national median of 2.7%. Net loan write-offs (loans recorded as lost, net of recoveries) ran at 1.3% of loans against a national median of 0.0%, while loan-loss reserves (money set aside for bad loans) were 1.8% of loans, above the 1.2% median.

On funding, brokered deposits were 18.9% of deposits against a national median of 0.0%, and core deposits (stable everyday deposits) were 59.6% of assets, below the 75.4% median. Borrowings from the Federal Home Loan Bank (a lender to banks) were 3.3% of assets versus a 0.2% median, and interest expense was 2.4% of assets versus 1.7%. Uninsured deposits, which can leave quickly in a scare, were lower than typical at 12.4% of deposits against a 24.5% median.

Capital (the owners' cushion against losses) looks roughly typical: equity was 10.6% of assets against a 10.4% median, the leverage ratio was 10.7% against 10.8%, and the Tier 1 and total risk-based capital ratios were 13.7% and 14.9%, slightly below medians of 14.4% and 15.6%. Bond losses are mixed: unrealized losses on bonds held to maturity were 2.9% of equity versus a 0.0% median, while losses on bonds available for sale were -0.4% versus a 5.2% median. So the credit and funding figures point toward risk while the capital figures and the real-estate concentration check, which did not cross either regulatory line, point the other way.

## Understanding the score

As of 2025-12-31, the bank ranked 82 out of 4,411 banks, the 98.2nd percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 89 banks that quarter.

The five features that pushed the score up most were loans 90 or more days past due or not accruing interest at 6.4% of loans, brokered deposits at 18.9% of deposits, interest expense at 2.4% of assets, recently overdue loans not yet seriously delinquent at 0.0% of assets, and commercial real estate loans at 11.4% of loans. The last two are lower than the national medians of 0.2% and 23.5%, yet the model still counted them as small upward pushes.

The five features that pulled the score down most were the Tier 1 risk-based capital ratio at 13.7%, the total risk-based capital ratio at 14.9%, return on equity (profit as a share of equity) at 5.5%, return on assets (profit as a share of assets) at 0.6%, and deposit growth over the past four quarters at -0.8%. The Tier 1 capital ratio was the single largest influence, with a contribution of -1.178.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 1,257 | 4,640 |  |
| 2024-06-30 | 654 | 4,610 |  |
| 2024-09-30 | 895 | 4,589 |  |
| 2024-12-31 | 25 | 4,560 | ▲ watchlist |
| 2025-03-31 | 49 | 4,536 | ▲ watchlist |
| 2025-06-30 | 43 | 4,494 | ▲ watchlist |
| 2025-09-30 | 261 | 4,452 |  |
| 2025-12-31 | 82 | 4,411 | ▲ watchlist |

## How its ratios moved

As of 2025-12-31, the model ranked First Central Bank Mccook 82 out of 4,411 banks, which places it at the 98.2nd percentile on a scale of 0 to 100 where higher means riskier. A year earlier, on 2024-12-31, it sat at the 99.5th percentile, so the model rated it safer than a year earlier. Each ratio is compared with its own prior range, which for most ratios covers the prior 12 quarters and for year-to-date ratios covers the same quarter in the prior 3 years. Of 30 ratios compared this way, 13 were outside their own prior range, and the 6 furthest outside are discussed here.

Brokered deposits (money placed with the bank through outside middlemen) were 18.9% of deposits, below their prior range of 21.8% to 32.8%, yet this ratio pushed the score up, adding +0.677 model log-odds units. That share fell by -2.9 pp over one quarter and by -7.5 pp over four quarters.

The Tier 1 risk-based capital ratio (core capital as a cushion against riskier assets) reached 13.7%, above its prior range of 11.1% to 13.4%, and it pushed the score down by -1.178 model log-odds units. The total risk-based capital ratio (a broader capital cushion) was 14.9%, above its prior range of 12.3% to 14.6%, and it also pushed the score down, by -0.402 model log-odds units. Return on equity (profit as a share of equity) was 5.5%, above its prior range of -5.2% to 3.0%, and it pushed the score down by -0.384 model log-odds units. Return on assets (profit as a share of assets) was 0.6%, above its prior range of -0.6% to 0.3%, and it pushed the score down by -0.368 model log-odds units. Losses on bonds available for sale (unrealized losses on bonds the bank could sell, as a share of equity) stood at -0.4%, below their prior range of -0.1% to 1.0%, and they pushed the score down by -0.085 model log-odds units. So although these five ratios moved outside their usual ranges, the model treated each of those moves as lowering the score rather than raising it.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 5.5% | -5.2% to 3.0% | same quarter, prior 3 years | n/a | +10.8 pp | -0.384 | pushed the score down |
| brokered deposits as a share of deposits | 18.9% | 21.8% to 32.8% | prior 12 quarters | -2.9 pp | -7.5 pp | +0.677 | pushed the score up |
| losses on bonds available for sale, as a share of equity | -0.4% | -0.1% to 1.0% | prior 12 quarters | -0.3 pp | -0.9 pp | -0.085 | pushed the score down |
| return on assets (profit as a share of assets) | 0.6% | -0.6% to 0.3% | same quarter, prior 3 years | n/a | +1.1 pp | -0.368 | pushed the score down |
| the Tier 1 risk-based capital ratio | 13.7% | 11.1% to 13.4% | prior 12 quarters | +1.2 pp | +2.6 pp | -1.178 | pushed the score down |
| the total risk-based capital ratio | 14.9% | 12.3% to 14.6% | prior 12 quarters | +1.2 pp | +2.6 pp | -0.402 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2025-12-31: Agricultural Specialization.

Peers: 654 banks in the same specialty group and size tier ($100 million to $1 billion).

Nonaccrual assets (loans that have stopped earning interest) plus foreclosed property made up 4.5% of the bank's assets, the 99.2nd percentile nationally, which is unusually high; among its peers it sits at the 99.6th percentile against a peer median of 0.2%, unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 6.4% of loans, the 99.0th percentile nationally, which is unusually high; among peers it ranks at the 99.5th percentile against a peer median of 0.3%, unusually high among its peers too. The Texas ratio, which weighs troubled assets against capital plus reserves, was 37.6%, the 98.8th percentile nationally, which is unusually high; among peers it is at the 98.5th percentile against a peer median of 2.2%, unusually high among its peers too.

Annualized loan write-offs (loans recorded as lost, net of amounts later recovered) were 1.3% of loans, the 97.6th percentile nationally, which is unusually high; among peers it is at the 99.0th percentile against a peer median of 0.0%, unusually high among its peers too. The annualized provision for loan losses (money set aside to cover expected bad loans) was 0.5% of assets, the 95.3rd percentile nationally, which is unusually high; among peers it is at the 97.3rd percentile against a peer median of 0.1%, unusually high among its peers too. Brokered deposits (deposits placed through outside intermediaries) were 18.9% of deposits, the 94.3rd percentile nationally, which is unusually high; among peers it is at the 96.4th percentile against a peer median of 0.0%, unusually high among its peers too. Losses on bonds available for sale, as a share of equity, were -0.4%, the 4.3rd percentile nationally, which is unusually low; among peers it is at the 4.8th percentile against a peer median of 6.9%, unusually low among its peers too. Asset growth over the past four quarters was -2.3%, the 9.3rd percentile nationally, which is unusually low; among peers it is at the 5.7th percentile against a peer median of 4.5%, unusually low among its peers too.

Overall, 8 of the bank's ratios fall in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 4.5% | 99.2nd (unusually high) | 0.2% | 99.6th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 6.4% | 99.0th (unusually high) | 0.3% | 99.5th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 37.6% | 98.8th (unusually high) | 2.2% | 98.5th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.3% | 97.6th (unusually high) | 0.0% | 99.0th | unusually high among its peers too |
| losses on bonds available for sale, as a share of equity | -0.4% | 4.3rd (unusually low) | 6.9% | 4.8th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 0.5% | 95.3rd (unusually high) | 0.1% | 97.3rd | unusually high among its peers too |
| brokered deposits as a share of deposits | 18.9% | 94.3rd (unusually high) | 0.0% | 96.4th | unusually high among its peers too |
| asset growth over the past four quarters | -2.3% | 9.3rd (unusually low) | 4.5% | 5.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 49.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 93.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 102.5% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

With hindsight, this case is classed as a false alarm: the bank was flagged mainly for weak credit quality and reliance on brokered deposits, but later data shows it moving off the watchlist. In hindsight, at 2026-03-31 it ranked 271 and was not flagged, and at 2026-06-30 it ranked 534 and was not flagged. Its stronger capital and improving profits, which the model already weighed against the flag, are consistent with that easing, though the data cannot say why the ranking fell.

## What happened next

Looking back with hindsight, the bank kept reporting after the as-of quarter and kept being ranked. Its rank moved to 271 at 2026-03-31 and to 534 at 2026-06-30, and it was not flagged in either quarter. Our data does not show it stopping reporting through the latest quarter shown.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 271 | 4,353 |  |
| 2026-06-30 | 534 | 4,313 |  |

## Sources

- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NE · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-12-31 · 82 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 6.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F26 · National median: loans 30-89 days past due, as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2025-12-31 · 1.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2025-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F36 · National median: commercial real estate loans as a share of loans · 2025-12-31 · 23.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 37.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2025-12-31 · 24.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 59.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 2.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 6.4%; contribution to the score · 2025-12-31 · +0.867 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 18.9%; contribution to the score · 2025-12-31 · +0.677 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2025-12-31 · +0.340 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2025-12-31 · +0.163 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 11.4%; contribution to the score · 2025-12-31 · +0.097 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.7%; contribution to the score · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 14.9%; contribution to the score · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 5.5%; contribution to the score · 2025-12-31 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.6%; contribution to the score · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -0.8%; contribution to the score · 2025-12-31 · -0.298 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 271 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 534 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · 5.5% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -5.2% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F92 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F94 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 21.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F95 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 32.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F96 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2025-12-31 · -2.9 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F97 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2025-12-31 · -7.5 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F98 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2025-12-31 · +0.677 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F99 · Trend: brokered deposits as a share of deposits, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F100 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F102 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F105 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2025-12-31 · -0.085 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F114 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 11.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F115 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F118 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F119 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F120 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2025-12-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F122 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F125 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: the total risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F127 · Trend: ratios outside their own prior range · 2025-12-31 · 13 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 99.5% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F138 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 99.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F139 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F140 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 99.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2025-12-31 · 6.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F144 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2025-12-31 · 99.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F145 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F146 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2025-12-31 · 99.5th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F147 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2025-12-31 · 37.6% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2025-12-31 · 98.8th · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F152 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2025-12-31 · 98.5th · data/features/fct_bank_features.parquet: texas_ratio
- F153 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2025-12-31 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio
- F154 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2025-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2025-12-31 · 97.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2025-12-31 · 99.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F162 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2025-12-31 · 4.3rd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F163 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F164 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2025-12-31 · 4.8th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F165 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2025-12-31 · 6.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F166 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F167 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2025-12-31 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 95.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized provision for loan losses as a share of assets, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F170 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 97.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F171 · Peers: annualized provision for loan losses as a share of assets, peer median · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F172 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F173 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F174 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2025-12-31 · 94.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F175 · Peers: brokered deposits as a share of deposits, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F176 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2025-12-31 · 96.4th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F177 · Peers: brokered deposits as a share of deposits, peer median · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F178 · Peers: brokered deposits as a share of deposits, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F179 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2025-12-31 · -2.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F180 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2025-12-31 · 9.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F181 · Peers: asset growth over the past four quarters, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F182 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2025-12-31 · 5.7th · data/features/fct_bank_features.parquet: asset_growth_4q
- F183 · Peers: asset growth over the past four quarters, peer median · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F184 · Peers: asset growth over the past four quarters, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F186 · Peers: ratios in the national top or bottom 10% · 2025-12-31 · 8 · data/features/fct_bank_features.parquet
- F187 · Peers: those ratios also unusual among peers · 2025-12-31 · 8 · data/features/fct_bank_features.parquet
- F189 · Peers: cut-off for unusual (top or bottom share of banks) · 2025-12-31 · 10% · data/features/fct_bank_features.parquet
