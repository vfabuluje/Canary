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
written_at: "2026-11-19T14:08:50"
writer_model: "claude-opus-5-5"
checked: true
---

# First Central Bank Mccook (cert 34995)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

First Central Bank Mccook, a Nebraska bank (certificate 34995), ranked 82 out of 4,411 banks nationally on Canary's score as of December 31, 2025, placing it in the 98.2nd percentile, where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. The main concern is credit quality: 6.4% of its loans were 90 or more days past due or no longer earning interest, against a national median of 0.4%. Its capital ratios sat close to national medians, and the model treated its capital as a factor that lowered the score.

## Warning signs in the data

Capital, the cushion of owners' money that absorbs losses, was near typical levels: equity was 10.6% of assets against a national median of 10.4%, and the Tier 1 risk-based capital ratio (core capital measured against assets weighted by their riskiness) was 13.7% against 14.4%. Profitability was thinner than usual, with return on assets of 0.6% against a national median of 1.1%.

Credit quality, meaning how well borrowers are repaying, stands out. Loans 90+ days past due or not accruing interest were 6.4% of loans, against a national median of 0.4%. Nonaccrual assets and foreclosed property were 4.5% of assets against 0.3%, and the Texas ratio, which compares troubled assets with capital plus reserves, was 37.6% against 2.7%. Net loan write-offs, loans recorded as uncollectable after recoveries, ran at 1.3% of loans against a national median of 0.0%.

On funding, brokered deposits, money gathered through third-party brokers rather than directly from customers, made up 18.9% of deposits, where the national median was 0.0%. Core deposits, the steadier everyday funding base, were 59.6% of assets against 75.4%, and interest expense ran at 2.4% of assets against 1.7%. Bond losses were modest: losses on bonds held to maturity were 2.9% of equity against a median of 0.0%, while losses on bonds available for sale were -0.4% of equity against 5.2%.

## Understanding the score

First Central Bank Mccook ranked 82 of 4,411 banks as of December 31, 2025, the 98.2nd percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score, or 89 banks that quarter.

Five features pushed the score up the most: loans 90+ days past due or not accruing interest at 6.4% of loans (contribution +0.867), brokered deposits at 18.9% of deposits (+0.677), and annualized interest expense at 2.4% of assets (+0.340). The other two were loans 30-89 days past due at 0.0% of assets (+0.163) and commercial real estate loans at 11.4% of loans (+0.097).

Five features pulled the score down the most: the Tier 1 risk-based capital ratio at 13.7% (contribution -1.178), the total risk-based capital ratio at 14.9% (-0.402), and return on equity, profit as a share of equity, at 5.5% (-0.384). The other two were return on assets at 0.6% (-0.368) and deposit growth over the past four quarters at -0.8% (-0.298).

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

Canary compares each ratio with its own prior range, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared, 13 were outside their own prior range at 2025-12-31. The model rated the bank safer than a year earlier: it sat at the 99.5th percentile at 2024-12-31 and the 98.2nd percentile at the as-of quarter.

The Tier 1 risk-based capital ratio was 13.7%, above its prior range of 11.1% to 13.4%, yet it pushed the score down, with a contribution of -1.178 model log-odds units. That ratio rose by +2.6 pp over four quarters. The total risk-based capital ratio was 14.9%, above its prior range of 12.3% to 14.6%, and it also pushed the score down, contributing -0.402.

Return on equity was 5.5%, above its prior range of -5.2% to 3.0%, and it pushed the score down, contributing -0.384. Return on assets was 0.6%, above its prior range of -0.6% to 0.3%, and it pushed the score down, contributing -0.368. Brokered deposits were 18.9% of deposits, below their prior range of 21.8% to 32.8%, but this ratio still pushed the score up, contributing +0.677. Losses on bonds available for sale were -0.4% of equity, below their prior range of -0.1% to 1.0%, and pushed the score down, contributing -0.085.

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

Nonaccrual assets and foreclosed property were 4.5% of assets, at the 99.2nd national percentile, which is unusually high, and at the 99.6th percentile among peers against a peer median of 0.2%, unusually high among its peers too. Loans 90+ days past due or not accruing interest were 6.4% of loans, at the 99.0th national percentile, unusually high, and at the 99.5th percentile among peers against a peer median of 0.3%, unusually high among its peers too. The Texas ratio was 37.6%, at the 98.8th national percentile, unusually high, and at the 98.5th percentile among peers against a peer median of 2.2%, unusually high among its peers too. Net loan write-offs were 1.3% of loans, at the 97.6th national percentile, unusually high, and at the 99.0th percentile among peers against a peer median of 0.0%, unusually high among its peers too.

The provision for loan losses, money set aside for expected bad loans, was 0.5% of assets, at the 95.3rd national percentile, unusually high, and at the 97.3rd percentile among peers against a peer median of 0.1%, unusually high among its peers too. Brokered deposits were 18.9% of deposits, at the 94.3rd national percentile, unusually high, and at the 96.4th percentile among peers against a peer median of 0.0%, unusually high among its peers too. Losses on bonds available for sale were -0.4% of equity, at the 4.3rd national percentile, unusually low, and at the 4.8th percentile among peers against a peer median of 6.9%, unusually low among its peers too. Asset growth over the past four quarters was -2.3%, at the 9.3rd national percentile, unusually low, and at the 5.7th percentile among peers against a peer median of 4.5%, unusually low among its peers too.

Overall, 8 of the bank's ratios were in the national top or bottom 10%, and all 8 of those were also unusual among its peers.

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

In hindsight, Canary classes this case as a false alarm. The bank was flagged at 2025-12-31 with a rank of 82, driven mainly by its high share of problem loans and its reliance on brokered deposits. Looking back, the flag did not persist: by 2026-03-31 its rank had moved to 271 and it was no longer flagged. By 2026-06-30 it ranked 534, again not flagged.

## What happened next

With hindsight, the bank kept reporting after the as-of quarter and moved off the watchlist. It ranked 271 at 2026-03-31 and 534 at 2026-06-30, not flagged in either quarter. It was still reporting as of 2026-06-30.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 271 | 4,353 |  |
| 2026-06-30 | 534 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · First Central Bank Mccook · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 34995 · data/features/fct_bank_features.parquet: cert
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
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 6.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 37.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 59.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
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
- F117 · Trend: the Tier 1 risk-based capital ratio, change over four quarters, in percentage points · 2025-12-31 · +2.6 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F118 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F119 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F120 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2025-12-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F122 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F125 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: the total risk-based capital ratio, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F127 · Trend: ratios outside their own prior range · 2025-12-31 · 13 · data/features/fct_bank_features.parquet
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
