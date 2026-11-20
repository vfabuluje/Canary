---
cert: 35495
name: "Proficio Bank"
as_of: 2016-12-31
rank: 6
n_banks: 5983
percentile: 99.91642988467324
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-03-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Proficio Bank (cert 35495)

*Hindsight: failed 2017-03-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Proficio Bank, a Utah bank with $68.2 million in assets, ranked 6 out of 5,983 banks nationally on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. That put it on Canary's watchlist, which covers about 2% of banks, or 120 banks that quarter. Its capital cushion was very thin, with equity (the owners' stake) at 3.4% of assets against a national median of 10.7%, and it was losing money, with return on assets of -4.5% against a median of 0.9%. The bank was also shrinking fast, with asset growth over the past four quarters of -37.7% against a national median of 3.5%.

## Warning signs in the data

Capital, the money that absorbs losses before depositors are at risk, was far below typical levels. The leverage ratio (core capital as a share of average assets) was 3.1% against a national median of 10.4%. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by risk) was 3.6% against a median of 15.0%, and the total risk-based capital ratio was 4.7% against a median of 16.2%. Earnings were deeply negative, with return on equity (profit as a share of the owners' stake) at -133.2% against a median of 8.0%, and the efficiency ratio (operating costs as a share of revenue) at 179.2% against a median of 69.7%.

Credit quality, meaning how well borrowers were repaying, was weak. Seriously late loans or loans no longer accruing interest were 2.2% of loans against a national median of 0.6%, and nonaccrual assets plus foreclosed property were 5.0% of assets against a median of 0.5%. The Texas ratio (troubled assets against capital plus reserves) was 114.1%, far above the median of 4.9%. Lending leaned heavily on property: construction loans were 13.5% of loans against a median of 4.2%, and commercial real estate loans were 60.6% against a median of 22.5%. The real-estate concentration section points the same way, finding that the bank crossed the supervisors' construction screen though not the second, growth-based screen. Some credit figures looked calmer: loan-loss reserves were 1.5% of loans against a median of 1.2%, and net loan write-offs were -0.3% of loans against a median of 0.1%.

Funding signals were mixed. Uninsured deposits were only 0.8% of deposits against a median of 17.3%, brokered deposits were 0.0% in line with the median of 0.0%, and core deposits (stable, everyday deposits) were 80.0% of assets against a median of 78.8%. On the other hand, volatile funding was 15.4% of assets against a median of 5.2%, interest expense was 1.3% of assets against a median of 0.4%, and deposit growth over the past four quarters was -32.8% against a median of 3.6%. Cash was 11.1% of assets against a median of 6.6%, and the bond-loss measure for bonds available for sale was -4.9% of equity against a median of 0.7%, while the measure for bonds held to maturity was 0.0%, matching the median of 0.0%.

## Understanding the score

As of 2016-12-31, Proficio Bank ranked 6 out of 5,983 banks, the 99.9th percentile on a 0 to 100 scale where higher means riskier. That placed it on the watchlist, which holds about 2% of banks, or 120 banks that quarter.

The five features that pushed the score up most were led by the Tier 1 risk-based capital ratio at 3.6%, contributing +2.373, and return on equity at -133.2%, contributing +1.406. Next came the Texas ratio at 114.1%, contributing +0.569, the total risk-based capital ratio at 4.7%, contributing +0.495, and asset growth over the past four quarters at -37.7%, contributing +0.370.

The five features that pushed the score down most were seriously late or non-accruing loans at 2.2% of loans, contributing -0.414, and interest expense at 1.3% of assets, contributing -0.333. The others were the bond-loss measure for bonds available for sale at -4.9% of equity, contributing -0.327, loans in the early stage of being past due at 0.4% of assets, contributing -0.293, and commercial real estate loans at 60.6% of loans, contributing -0.275. Several of these downward pushes come from figures that look weak on their own, so the very high rank rests mainly on thin capital and heavy losses.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 9 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 7 | 6,129 | ▲ watchlist |
| 2016-09-30 | 14 | 6,051 | ▲ watchlist |
| 2016-12-31 | 6 | 5,983 | ▲ watchlist |

## How its ratios moved

As of 2016-12-31, Proficio Bank ranked 6 out of 5,983 banks nationally, placing it in the 99.9th percentile, where higher means riskier. Of the 30 ratios compared with the bank's own prior range, 11 sat outside that range, and the table shows the 6 furthest outside it. For most ratios the prior range covers the previous 12 quarters, while year-to-date ratios are compared with the same quarter in the prior 3 years.

Return on equity (profit as a share of the owners' stake) stood at -133.2%, below its prior range of -95.5% to 3.4%, and it pushed the score up, contributing +1.406 model log-odds units (the model's internal scale, where positive raises the score). The efficiency ratio (operating costs as a share of revenue) was 179.2%, above its prior range of 98.9% to 150.9%, yet it had little effect on the score, contributing +0.021 model log-odds units.

Annualized interest expense as a share of assets was 1.3%, above its prior range of 0.6% to 0.9%, but it pushed the score down, contributing -0.333 model log-odds units. Deposit growth over the past four quarters was -32.8%, below its prior range of -28.6% to 1.8%, but it pushed the score down, contributing -0.110 model log-odds units. Commercial real estate loans (loans backed by business property) made up 60.6% of loans, above their prior range of 9.4% to 55.5%, but this pushed the score down, contributing -0.275 model log-odds units. The annualized provision for loan losses (money set aside for loans that may not be repaid) was 0.0% of assets, above its prior range of -0.5% to -0.1%, but it pushed the score down, contributing -0.057 model log-odds units.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 179.2% | 98.9% to 150.9% | same quarter, prior 3 years | n/a | +28.2 pp | +0.021 | little effect on the score |
| return on equity (profit as a share of equity) | -133.2% | -95.5% to 3.4% | same quarter, prior 3 years | n/a | -37.7 pp | +1.406 | pushed the score up |
| annualized interest expense as a share of assets | 1.3% | 0.6% to 0.9% | same quarter, prior 3 years | n/a | +0.4 pp | -0.333 | pushed the score down |
| deposit growth over the past four quarters | -32.8% | -28.6% to 1.8% | prior 12 quarters | -8.0 pp | -4.2 pp | -0.110 | pushed the score down |
| commercial real estate loans as a share of loans | 60.6% | 9.4% to 55.5% | prior 12 quarters | +5.3 pp | +12.6 pp | -0.275 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.0% | -0.5% to -0.1% | same quarter, prior 3 years | n/a | +0.6 pp | -0.057 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-12-31: Commercial Lending Specialization.

Peers: 346 banks in the same specialty group and size tier (under $100 million).

Return on equity (profit as a share of the owners' stake) was -133.2%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.1st percentile of its peers against a peer median of 6.1%, unusually low among its peers too. Return on assets (profit as a share of assets) was -4.5%, at the 0.2nd percentile nationally, which is unusually low; it sat at the 0.7th percentile of its peers against a peer median of 0.7%, unusually low among its peers too. The efficiency ratio (operating costs as a share of revenue, where higher means costlier) was 179.2%, at the 99.7th percentile nationally, which is unusually high; it sat at the 97.8th percentile of its peers against a peer median of 79.0%, unusually high among its peers too. Annualized interest expense as a share of assets was 1.3%, at the 99.6th percentile nationally, which is unusually high; it sat at the 99.6th percentile of its peers against a peer median of 0.4%, unusually high among its peers too.

The total risk-based capital ratio (the bank's capital cushion measured against its loans and other assets weighted by risk) was 4.7%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.4th percentile of its peers against a peer median of 16.4%, unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the core, highest-quality capital) was 3.6%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.4th percentile of its peers against a peer median of 15.3%, unusually low among its peers too.

Asset growth over the past four quarters was -37.7%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.4th percentile of its peers against a peer median of 2.6%, unusually low among its peers too. Deposit growth over the past four quarters was -32.8%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.4th percentile of its peers against a peer median of 2.9%, unusually low among its peers too. Overall, 18 of the bank's ratios were in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -133.2% | 0.1st (unusually low) | 6.1% | 0.1st | unusually low among its peers too |
| asset growth over the past four quarters | -37.7% | 0.1st (unusually low) | 2.6% | 0.4th | unusually low among its peers too |
| deposit growth over the past four quarters | -32.8% | 0.1st (unusually low) | 2.9% | 0.4th | unusually low among its peers too |
| the total risk-based capital ratio | 4.7% | 0.1st (unusually low) | 16.4% | 0.4th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 3.6% | 0.1st (unusually low) | 15.3% | 0.4th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -4.5% | 0.2nd (unusually low) | 0.7% | 0.7th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 179.2% | 99.7th (unusually high) | 79.0% | 97.8th | unusually high among its peers too |
| annualized interest expense as a share of assets | 1.3% | 99.6th (unusually high) | 0.4% | 99.6th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 220.0% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 395.7% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -13.4% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged Proficio Bank in the quarter ending 2016-03-31, and the bank failed on 2017-03-03, a lead time of 4 quarters. At that first flag, the main drivers pushing the score up were already the Tier 1 risk-based capital ratio at 4.2%, contributing +2.485, and return on equity at -197.5%, contributing +1.496. The Texas ratio at 175.8%, contributing +1.038, the total risk-based capital ratio at 5.0%, contributing +0.427, and the leverage ratio at 2.4%, contributing +0.316, rounded out the top five. The same story of thin capital and heavy losses showed up early and persisted through later quarters.

## What happened next

In hindsight, the last quarter Proficio Bank reported was 2016-12-31, so there are no later ranks or flags. The bank failed on 2017-03-03.

## Sources

- F1 · Bank name · n/a · Proficio Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 3.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 4.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 2.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 5.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2016-12-31 · 1.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2016-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · -0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2016-12-31 · 13.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2016-12-31 · 4.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2016-12-31 · 60.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-12-31 · 22.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 114.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2016-12-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 0.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-12-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-12-31 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 15.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 11.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · -4.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2016-12-31 · $68.2 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -37.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -32.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.6%; contribution to the score · 2016-12-31 · +2.373 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -133.2%; contribution to the score · 2016-12-31 · +1.406 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 114.1%; contribution to the score · 2016-12-31 · +0.569 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 4.7%; contribution to the score · 2016-12-31 · +0.495 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: asset growth over the past four quarters, value -37.7%; contribution to the score · 2016-12-31 · +0.370 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 2.2%; contribution to the score · 2016-12-31 · -0.414 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2016-12-31 · -0.333 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -4.9%; contribution to the score · 2016-12-31 · -0.327 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.4%; contribution to the score · 2016-12-31 · -0.293 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 60.6%; contribution to the score · 2016-12-31 · -0.275 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-03-03 · 2017-03-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +2.485 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: return on equity (profit as a share of equity), value -197.5%; contribution to the score · 2016-03-31 · +1.496 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 175.8%; contribution to the score · 2016-03-31 · +1.038 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2016-03-31: the total risk-based capital ratio, value 5.0%; contribution to the score · 2016-03-31 · +0.427 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F92 · Driver up #5 at 2016-03-31: the leverage ratio (core capital as a share of average assets), value 2.4%; contribution to the score · 2016-03-31 · +0.316 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 98.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 150.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · +0.021 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -95.5% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-12-31 · +1.406 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F112 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F115 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.333 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F116 · Trend: annualized interest expense as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F117 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2016-12-31 · -32.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F118 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -28.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F119 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F122 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2016-12-31 · -0.110 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F123 · Trend: deposit growth over the past four quarters, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F124 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2016-12-31 · 60.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F125 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F126 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 55.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F129 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2016-12-31 · -0.275 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F130 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F131 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F132 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · -0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F133 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F135 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.057 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F136 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F137 · Trend: ratios outside their own prior range · 2016-12-31 · 11 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F145 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F146 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), peer median · 2016-12-31 · 6.1% · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2016-12-31 · -37.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F152 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F153 · Peers: asset growth over the past four quarters, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F154 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2016-12-31 · 0.4th · data/features/fct_bank_features.parquet: asset_growth_4q
- F155 · Peers: asset growth over the past four quarters, peer median · 2016-12-31 · 2.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F156 · Peers: asset growth over the past four quarters, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F157 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2016-12-31 · -32.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F158 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F159 · Peers: deposit growth over the past four quarters, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F160 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2016-12-31 · 0.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: deposit growth over the past four quarters, peer median · 2016-12-31 · 2.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F162 · Peers: deposit growth over the past four quarters, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F163 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · 4.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.4th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, peer median · 2016-12-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.4th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-12-31 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-12-31 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-12-31 · 0.7th · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), peer median · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F182 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2016-12-31 · 99.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F183 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F184 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2016-12-31 · 97.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F185 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2016-12-31 · 79.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F186 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F187 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F188 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 99.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F189 · Peers: annualized interest expense as a share of assets, national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F190 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 99.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F191 · Peers: annualized interest expense as a share of assets, peer median · 2016-12-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F192 · Peers: annualized interest expense as a share of assets, reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F194 · Peers: ratios in the national top or bottom 10% · 2016-12-31 · 18 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2016-12-31 · 17 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-12-31 · 10% · data/features/fct_bank_features.parquet
