---
cert: 8889
name: "Midwest Regional Bank"
as_of: 2026-06-30
rank: 30
n_banks: 4313
percentile: 99.32761418965917
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Midwest Regional Bank (cert 8889)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Midwest Regional Bank ranked 30 out of 4,313 banks, in the 99.3rd percentile where higher means riskier, which put it on Canary's watchlist. Its troubled loans stood out: loans 90+ days past due or no longer earning interest were 6.6% of loans, against a national median of 0.5%. It was also losing money, with a return on equity (profit as a share of shareholders' capital) of -12.3% against a national median of 11.6%, and its assets shrank by -15.5% over the past four quarters. Its capital ratios were close to or below the national medians, yet the model treated its Tier 1 capital as the largest factor pulling the score down.

## Warning signs in the data

Credit quality is the clearest weak spot. Loans 90+ days past due or not accruing interest were 6.6% of loans, far above the national median of 0.5%, and nonaccrual assets plus foreclosed property were 5.4% of assets, against a median of 0.3%. Earlier-stage problems, loans 30-89 days past due, were 0.8% of assets against a median of 0.2%. Net write-offs (loans given up as lost, minus recoveries) ran at an annualized 3.2% of loans, against a median of 0.0%, and the Texas ratio (troubled assets against capital plus reserves) was 42.8%, against a median of 2.9%. Lending was concentrated in property: construction loans were 21.1% of loans against a median of 5.3%, and commercial real estate loans were 43.3% against a median of 23.6%, and the concentration section found the bank crossed the regulators' construction screen.

Capital (the owners' cushion against losses) was thinner than typical. Equity was 10.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.2% against 11.0%. The Tier 1 risk-based capital ratio was 11.4% against a median of 14.6%, and the total risk-based capital ratio was 12.7% against 15.8%. These two sides point different ways in the model: the capital ratios sit below the medians, yet the model counted them as lowering the score rather than raising it.

On funding, deposits fell by -14.5% over the past four quarters, while the national median grew 4.2%, and interest expense ran at an annualized 3.0% of assets against a median of 1.6%. Uninsured deposits (balances above the government insurance limit) were 26.8% of deposits against a median of 24.8%, and volatile funding was 11.8% of assets against 9.0%, while brokered deposits were 0.0%, the same as the median. Cash was 6.9% of assets against a median of 6.2%. Bond losses were not a concern: unrealized losses on bonds available for sale were 1.3% of equity, below the median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median.

## Understanding the score

As of 2026-06-30, Midwest Regional Bank ranked 30 out of 4,313 banks, in the 99.3rd percentile on a scale of 0 to 100 where higher means riskier. Canary's watchlist covers the riskiest 2% of banks, which was 87 banks that quarter, and this bank was flagged.

Five features pushed the score up the most. They were troubled loans (90+ days past due or not accruing interest) at 6.6% of loans, interest expense at 3.0% of assets, the Texas ratio at 42.8%, the provision for loan losses (money set aside for expected bad loans) at 3.1% of assets, and securities at 4.8% of assets.

Five features pulled the score down the most. They were the Tier 1 risk-based capital ratio at 11.4%, the total risk-based capital ratio at 12.7%, construction loans at 21.1% of loans, commercial real estate loans at 43.3% of loans, and return on equity at -12.3%. The Tier 1 capital ratio was by far the largest single factor in either direction, with a contribution of -1.660.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,681 | 4,589 |  |
| 2024-12-31 | 1,186 | 4,560 |  |
| 2025-03-31 | 26 | 4,536 | ▲ watchlist |
| 2025-06-30 | 251 | 4,494 |  |
| 2025-09-30 | 273 | 4,452 |  |
| 2025-12-31 | 119 | 4,411 |  |
| 2026-03-31 | 216 | 4,353 |  |
| 2026-06-30 | 30 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Midwest Regional Bank ranked 30 out of 4,313 banks, placing it in the 99.3rd percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 94.4th percentile, and the model rated it riskier than a year earlier. Each ratio is compared with the bank's own history: the prior 12 quarters for most ratios, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked, 15 were outside their own prior range, and the 6 furthest outside are discussed here.

The provision for loan losses (money set aside for loans expected to go bad) ran at an annualized 3.1% of assets, well above its prior range of 0.0% to 0.5%, and contributed +0.204 model log-odds units, which pushed the score up. Loan-loss reserves (the cushion held against bad loans) reached 2.5% of loans, above their prior range of 1.1% to 2.1%, and contributed +0.082, which pushed the score up. Net write-offs (loans written off as lost, minus recoveries) rose to an annualized 3.2% of loans, far above their prior range of 0.1% to 0.7%, yet contributed only -0.003, which had little effect on the score.

Return on equity (profit as a share of shareholders' capital) fell to -12.3%, below its prior range of 2.7% to 8.8%, yet it contributed -0.227 and pushed the score down. Return on assets (profit as a share of assets) dropped to -1.3%, below its prior range of 0.3% to 0.9%, but contributed +0.026, which had little effect on the score. Net interest margin (the spread earned on lending and investing) was 3.5%, just above its prior range of 3.0% to 3.3%, and contributed -0.095, which pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 3.1% | 0.0% to 0.5% | same quarter, prior 3 years | n/a | +2.6 pp | +0.204 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 3.2% | 0.1% to 0.7% | same quarter, prior 3 years | n/a | +3.1 pp | -0.003 | little effect on the score |
| return on equity (profit as a share of equity) | -12.3% | 2.7% to 8.8% | same quarter, prior 3 years | n/a | -15.1 pp | -0.227 | pushed the score down |
| return on assets (profit as a share of assets) | -1.3% | 0.3% to 0.9% | same quarter, prior 3 years | n/a | -1.6 pp | +0.026 | little effect on the score |
| loan-loss reserves as a share of loans | 2.5% | 1.1% to 2.1% | prior 12 quarters | +0.4 pp | +1.2 pp | +0.082 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 3.5% | 3.0% to 3.3% | same quarter, prior 3 years | n/a | +0.3 pp | -0.095 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Its annualized provision for loan losses (money set aside to cover expected bad loans) is 3.1% of assets, in the 99.5th percentile nationally, which is unusually high, and in the 99.5th percentile among its peers against a peer median of 0.1%, unusually high among its peers too. Its nonaccrual assets and foreclosed property (loans no longer earning interest plus repossessed real estate) are 5.4% of assets, in the 99.3rd percentile nationally, which is unusually high, and in the 99.1st percentile among its peers against a peer median of 0.3%, unusually high among its peers too. Its annualized loan write-offs, net of recoveries (loans given up as lost), are 3.2% of loans, in the 99.2nd percentile nationally, which is unusually high, and in the 99.4th percentile among its peers against a peer median of 0.0%, unusually high among its peers too. Its loans 90+ days past due or not accruing interest are 6.6% of loans, in the 98.8th percentile nationally, which is unusually high, and in the 99.1st percentile among its peers against a peer median of 0.4%, unusually high among its peers too. Its Texas ratio (troubled assets against capital plus reserves) is 42.8%, in the 99.0th percentile nationally, which is unusually high, and in the 98.8th percentile among its peers against a peer median of 3.0%, unusually high among its peers too.

Its return on equity (profit as a share of equity) is -12.3%, in the 1.2nd percentile nationally, which is unusually low, and in the 0.7th percentile among its peers against a peer median of 11.7%, unusually low among its peers too. Its asset growth over the past four quarters is -15.5%, in the 0.6th percentile nationally, which is unusually low, and in the 0.5th percentile among its peers against a peer median of 4.8%, unusually low among its peers too. Its deposit growth over the past four quarters is -14.5%, in the 1.0th percentile nationally, which is unusually low, and in the 0.9th percentile among its peers against a peer median of 4.3%, unusually low among its peers too. Overall, 12 of the bank's ratios fall in the national top or bottom 10%, and all 12 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 3.1% | 99.5th (unusually high) | 0.1% | 99.5th | unusually high among its peers too |
| asset growth over the past four quarters | -15.5% | 0.6th (unusually low) | 4.8% | 0.5th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.4% | 99.3rd (unusually high) | 0.3% | 99.1st | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 3.2% | 99.2nd (unusually high) | 0.0% | 99.4th | unusually high among its peers too |
| deposit growth over the past four quarters | -14.5% | 1.0th (unusually low) | 4.3% | 0.9th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 42.8% | 99.0th (unusually high) | 3.0% | 98.8th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -12.3% | 1.2nd (unusually low) | 11.7% | 0.7th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 6.6% | 98.8th (unusually high) | 0.4% | 99.1st | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 138.2% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 311.5% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -8.4% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank is recorded as an open watchlist case: it was flagged by the model and is not recorded as having left the data. The fact sheet contains no later facts, so this note cannot say whether its troubled loans, losses or shrinking deposits improved or worsened afterward. A watchlist flag is a ranking of relative risk, not a forecast that a bank will close.

## What happened next

In hindsight, the fact sheet holds no ranks, flags or reporting status for quarters after the as-of quarter. Any later scores appear in the score history table that accompanies this note, and readers should rely on that table rather than this text for what came next.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 30 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 21.1% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 43.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 42.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -12.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 26.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -15.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -14.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 6.6%; contribution to the score · 2026-06-30 · +0.989 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.804 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 42.8%; contribution to the score · 2026-06-30 · +0.528 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: annualized provision for loan losses as a share of assets, value 3.1%; contribution to the score · 2026-06-30 · +0.204 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F79 · Driver up #5: securities as a share of assets, value 4.8%; contribution to the score · 2026-06-30 · +0.186 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.4%; contribution to the score · 2026-06-30 · -1.660 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 12.7%; contribution to the score · 2026-06-30 · -0.432 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: construction loans as a share of loans, value 21.1%; contribution to the score · 2026-06-30 · -0.302 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 43.3%; contribution to the score · 2026-06-30 · -0.261 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value -12.3%; contribution to the score · 2026-06-30 · -0.227 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F86 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F87 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F89 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.204 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F90 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.003 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F97 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -12.3% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.227 · data/analyst/scores.parquet: feature return_on_equity contribution
- F102 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F103 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F104 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.026 · data/analyst/scores.parquet: feature return_on_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F109 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F110 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F111 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F114 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.082 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F115 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F116 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F117 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.095 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F121 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F123 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F125 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F126 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F127 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 94.4% · data/analyst/scores.parquet: percentile
- F128 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F132 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F133 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F134 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F135 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F136 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F137 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F138 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -15.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F143 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F148 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F149 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F150 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F151 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F152 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F153 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F154 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -14.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F157 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F158 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F159 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F160 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 42.8% · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F165 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: texas_ratio
- F166 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F167 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F168 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -12.3% · data/features/fct_bank_features.parquet: return_on_equity
- F169 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.7th · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F175 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F176 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F177 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F178 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F179 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F181 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F182 · Peers: those ratios also unusual among peers · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F184 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
