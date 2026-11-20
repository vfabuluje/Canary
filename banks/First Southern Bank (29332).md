---
cert: 29332
name: "First Southern Bank"
as_of: 2026-06-30
rank: 8
n_banks: 4313
percentile: 99.83769997681429
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:01"
writer_model: "claude-opus-5-5"
checked: true
---

# First Southern Bank (cert 29332)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Southern Bank, an Alabama bank, ranked 8 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.8th percentile, and it was flagged on the watchlist. The ranking is driven mainly by credit problems: loans 90+ days past due or not accruing interest made up 10.9% of loans against a national median of 0.5%, and its Texas ratio (troubled assets against capital plus reserves) was 70.5% against a median of 2.9%. The bank was also losing money, with a return on assets (profit as a share of assets) of -2.5% against a median of 1.2%. By contrast, the separate real-estate concentration check found the bank did not cross either supervisory line, so its stress shows up in loan quality and earnings rather than in heavy commercial property lending.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thinner than at a typical bank: equity was 8.8% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.9% against 11.0%. These two measures point a different way from the model's single largest downward driver, the Tier 1 risk-based capital ratio, which lowered the score; the fact sheet does not give that ratio's value.

Credit quality was the clearest weak spot: nonaccrual assets and foreclosed property were 7.4% of assets against a median of 0.3%, and loans 30-89 days past due, an early sign of trouble, were 1.7% of assets against 0.2%. Net loan write-offs (loans recorded as lost, minus recoveries) ran at an annualized 4.7% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 4.5% of assets against 0.1%. Losses showed up in earnings, with return on equity (profit as a share of the owners' stake) at -27.8% against a median of 11.6%.

On funding, uninsured deposits (balances above the FDIC insurance limit) were 52.8% of deposits, well above the median of 24.8%, and Federal Home Loan Bank borrowings were 5.9% of assets against 0.2%. Offsetting points: cash was 13.4% of assets against a median of 7.4% is not right to compare loosely, so in plain terms cash at 13.4% of assets sat well above the median of 6.2%, and brokered deposits were 0.0%, matching the median of 0.0%. Bond losses were modest: unrealized losses on bonds available for sale equaled 1.5% of equity against a median of 5.6%, and losses on bonds held to maturity were 0.0%, the same as the median of 0.0%.

## Understanding the score

As of 2026-06-30, First Southern Bank ranked 8 out of 4,313 banks, in the 99.8th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were loans 90+ days past due or not accruing interest at 10.9% of loans (+1.076), the Texas ratio at 70.5% (+0.904), the provision for loan losses at 4.5% of assets (+0.316), return on equity at -27.8% (+0.198), and interest expense at 2.3% of assets (+0.127). The five factors that pulled it down most were the Tier 1 risk-based capital ratio, a measure of core capital against riskier assets (-1.071), construction loans at 6.4% of loans (-0.362), brokered deposits at 0.0% of deposits (-0.163), total assets of $679.2 million (-0.163), and deposit growth over the past four quarters of 6.4% (-0.125).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,089 | 4,589 |  |
| 2024-12-31 | 1,068 | 4,560 |  |
| 2025-03-31 | 29 | 4,536 | ▲ watchlist |
| 2025-06-30 | 50 | 4,494 | ▲ watchlist |
| 2025-09-30 | 35 | 4,452 | ▲ watchlist |
| 2025-12-31 | 105 | 4,411 |  |
| 2026-03-31 | 7 | 4,353 | ▲ watchlist |
| 2026-06-30 | 8 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, First Southern Bank ranked 8 out of 4,313 banks nationally, placing it in the 99.8th percentile, where higher means riskier. A year earlier it sat in the 98.9th percentile, and the model rates the bank as about the same as a year earlier. Canary compared 28 of the bank's ratios with their own prior range, and 17 of them were outside that range. For most ratios the prior range covers the previous 12 quarters, and for year-to-date ratios it covers the same quarter in the prior 3 years.

The provision for loan losses (money set aside to cover expected bad loans) ran at an annualized 4.5% of assets, well above its prior range of 0.2% to 1.3%, and its contribution of +0.316 model log-odds units pushed the score up. Return on assets (profit as a share of assets) was -2.5%, below its prior range of 0.1% to 1.3%, and its contribution of +0.081 pushed the score up. Return on equity (profit as a share of the owners' stake) was -27.8%, far below its prior range of 0.5% to 14.8%, and its contribution of +0.198 pushed the score up. Loan-loss reserves (the cushion held against bad loans) stood at 2.7% of loans, above their prior range of 1.1% to 1.9%, and their contribution of +0.086 pushed the score up.

Net loan write-offs (loans recorded as lost, minus recoveries) reached an annualized 4.7% of loans, above their prior range of 0.2% to 2.1%, yet their contribution of +0.001 had little effect on the score. Core deposits (steady, everyday customer deposits) rose to 79.6% of assets, above their prior range of 70.4% to 75.8%, but in contrast this ratio's contribution of -0.064 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 4.5% | 0.2% to 1.3% | same quarter, prior 3 years | n/a | +3.3 pp | +0.316 | pushed the score up |
| return on assets (profit as a share of assets) | -2.5% | 0.1% to 1.3% | same quarter, prior 3 years | n/a | -2.6 pp | +0.081 | pushed the score up |
| return on equity (profit as a share of equity) | -27.8% | 0.5% to 14.8% | same quarter, prior 3 years | n/a | -28.3 pp | +0.198 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.7% | 0.2% to 2.1% | same quarter, prior 3 years | n/a | +2.7 pp | +0.001 | little effect on the score |
| loan-loss reserves as a share of loans | 2.7% | 1.1% to 1.9% | prior 12 quarters | +0.8 pp | +1.6 pp | +0.086 | pushed the score up |
| core deposits as a share of assets | 79.6% | 70.4% to 75.8% | prior 12 quarters | +4.3 pp | +7.3 pp | -0.064 | pushed the score down |

17 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 642 banks in the same specialty group and size tier ($100 million to $1 billion).

First Southern Bank's nonaccrual assets and foreclosed property (loans that have stopped paying interest, plus property taken back from borrowers) equal 7.4% of assets, at the 99.8th national percentile, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.2%, this is unusually high among its peers too. Its annualized provision for loan losses (money set aside to cover loans expected to go bad) is 4.5% of assets, at the 99.7th national percentile, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.1%, this is unusually high among its peers too. Its Texas ratio (troubled assets against capital plus reserves) is 70.5%, at the 99.7th national percentile, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 2.5%, this is unusually high among its peers too. Loans 90+ days past due or not accruing interest make up 10.9% of its loans, at the 99.6th national percentile, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.4%, this is unusually high among its peers too.

Its annualized loan write-offs (loans declared uncollectible, net of amounts later recovered) are 4.7% of loans, at the 99.6th national percentile, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.0%, this is unusually high among its peers too. Its return on equity (profit as a share of the owners' stake) is -27.8%, at the 0.6th national percentile, which is unusually low; at the 0.1st percentile among its peers, against a peer median of 13.9%, this is unusually low among its peers too. Its return on assets (profit as a share of assets) is -2.5%, at the 0.9th national percentile, which is unusually low; at the 0.1st percentile among its peers, against a peer median of 1.5%, this is unusually low among its peers too. Its loan-loss reserves (a cushion held against future loan losses) equal 2.7% of loans, at the 96.5th national percentile, which is unusually high; at the 97.1st percentile among its peers, against a peer median of 1.2%, this is unusually high among its peers too. Overall, 10 of the bank's ratios fall in the national top or bottom 10%, and 10 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 7.4% | 99.8th (unusually high) | 0.2% | 99.9th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 4.5% | 99.7th (unusually high) | 0.1% | 99.9th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 70.5% | 99.7th (unusually high) | 2.5% | 99.9th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 10.9% | 99.6th (unusually high) | 0.4% | 99.9th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.7% | 99.6th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -27.8% | 0.6th (unusually low) | 13.9% | 0.1st | unusually low among its peers too |
| return on assets (profit as a share of assets) | -2.5% | 0.9th (unusually low) | 1.5% | 0.1st | unusually low among its peers too |
| loan-loss reserves as a share of loans | 2.7% | 96.5th (unusually high) | 1.2% | 97.1st | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 41.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 145.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 9.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, this bank's case is an open watchlist case: it was flagged by the model and the note records no closure. The fact sheet contains no data from after the as-of quarter, so this section cannot add later evidence about how the bank's loan problems or earnings developed.

## What happened next

In hindsight, the fact sheet holds no later ranks, watchlist flags or reporting status for this bank. Because of that, this note cannot say whether the bank's rank improved or worsened afterward, or whether it kept filing reports; the score history table added by code shows any later quarters that are available.

## Sources

- F1 · Bank name · n/a · First Southern Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 8 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 70.5% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -27.8% · data/features/fct_bank_features.parquet: return_on_equity
- F38 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 52.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · +1.076 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 70.5%; contribution to the score · 2026-06-30 · +0.904 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized provision for loan losses as a share of assets, value 4.5%; contribution to the score · 2026-06-30 · +0.316 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F74 · Driver up #4: return on equity (profit as a share of equity), value -27.8%; contribution to the score · 2026-06-30 · +0.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F75 · Driver up #5: annualized interest expense as a share of assets, value 2.3%; contribution to the score · 2026-06-30 · +0.127 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -1.071 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 6.4%; contribution to the score · 2026-06-30 · -0.362 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver down #4: total assets, value $679.2 million; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #5: deposit growth over the past four quarters, value 6.4%; contribution to the score · 2026-06-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F81 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F82 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F83 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F85 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.316 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F86 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F87 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F88 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F91 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.081 · data/analyst/scores.parquet: feature return_on_assets contribution
- F92 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -27.8% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.8% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F106 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F107 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F110 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.086 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F111 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F112 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 79.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F113 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 70.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F114 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F117 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.064 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F118 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F119 · Trend: ratios outside their own prior range · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F122 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F123 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F124 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.9% · data/analyst/scores.parquet: percentile
- F125 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F129 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F130 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F136 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F137 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F138 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F139 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F140 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 70.5% · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F150 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F154 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -27.8% · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F166 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: return_on_assets
- F167 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F168 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F169 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F170 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F171 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F172 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F173 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F174 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: allowance_to_loans
- F175 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F176 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F178 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F179 · Peers: those ratios also unusual among peers · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F181 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
