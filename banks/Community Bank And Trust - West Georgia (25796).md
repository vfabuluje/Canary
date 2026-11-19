---
cert: 25796
name: "Community Bank And Trust - West Georgia"
as_of: 2026-03-31
rank: 2
n_banks: 4353
percentile: 99.97702733746841
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-05-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:07:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Community Bank And Trust - West Georgia (cert 25796)

*Hindsight: failed 2026-05-01. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of March 31, 2026, Community Bank And Trust - West Georgia (a bank in GA) ranked 2 out of 4,353 banks nationally on Canary's risk score, placing it in the 100.0th percentile. That puts it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital, the owners' money that absorbs losses, was very thin: equity was 1.3% of assets against a national median of 10.4%. Meanwhile 17.3% of its loans were 90 or more days late or no longer paying interest, against a national median of 0.5%.

## Warning signs in the data

Capital is the cushion of owners' money that absorbs losses, and here it was nearly gone: equity was 1.3% of assets, against a national median of 10.4%. The leverage ratio (core capital as a share of average assets) was 0.2%, against a national median of 10.9%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by riskiness, was 0.2%, against a national median of 14.5%. The broader total risk-based capital ratio was 1.5%, against a national median of 15.7%.

Loan quality was poor: 17.3% of loans were 90 or more days past due or not accruing interest (no longer counted as earning), against a national median of 0.5%. Loans 30-89 days past due equalled 5.5% of assets, against a median of 0.3%, and nonaccrual assets plus foreclosed property were 9.2% of assets, against a median of 0.3%. Net loan write-offs (loans given up as lost) ran at an annualized 6.3% of loans, against a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 8.7% of assets, against a median of 0.0%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 280.0%, against a national median of 2.9%. These costs left return on assets (profit as a share of assets) at -6.9%, against a national median of 1.2%.

Funding looked steadier: uninsured deposits, which are above the government insurance limit, were only 3.6% of deposits, against a national median of 24.4%. Core deposits, a stable everyday funding source, were 91.3% of assets against a median of 75.8%, and cash was 16.2% of assets against a median of 6.9%. Deposits grew 42.6% over the past four quarters, far above the national median of 4.0%. On bonds, the measure of losses on bonds available for sale as a share of equity read -177.9%, far from the national median of 5.8%, a reading distorted by the bank's very small equity base.

## Understanding the score

On March 31, 2026, the bank ranked 2 out of 4,353 banks, in the 100.0th percentile on a scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks and contained 88 banks that quarter. Its raw model score was 0.9972, but the rank is the more useful reading.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 0.2% (contribution +1.741) and return on equity, profit as a share of equity, at -191.5% (+1.318). Next came the Texas ratio at 280.0% (+1.050), loans 90+ days past due or not accruing at 17.3% of loans (+0.770), and the total risk-based capital ratio at 1.5% (+0.510).

The five factors that pulled the score down most were losses on bonds available for sale at -177.9% of equity (-0.273) and asset growth of 23.9% over the past four quarters (-0.219). The others were construction loans at 8.1% of loans (-0.179), total assets of $292.6 million (-0.160), and the efficiency ratio, operating costs as a share of revenue, at 92.4% (-0.129).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 6 | 4,610 | ▲ watchlist |
| 2024-09-30 | 4 | 4,589 | ▲ watchlist |
| 2024-12-31 | 5 | 4,560 | ▲ watchlist |
| 2025-03-31 | 3 | 4,536 | ▲ watchlist |
| 2025-06-30 | 1 | 4,494 | ▲ watchlist (first flag) |
| 2025-09-30 | 15 | 4,452 | ▲ watchlist |
| 2025-12-31 | 16 | 4,411 | ▲ watchlist |
| 2026-03-31 | 2 | 4,353 | ▲ watchlist |

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. By that test, 15 of the 30 ratios checked sat outside their own prior range at the as-of quarter. The model rated the bank about the same as a year earlier, when it was also in the 100.0th percentile, and it now ranks 2 out of 4,353 banks.

Return on equity fell to -191.5%, far below its prior range of 0.4% to 19.1%, and pushed the score up with a contribution of +1.318 model log-odds units. The leverage ratio dropped to 0.2%, below its prior range of 5.1% to 9.8%, after falling -6.5 pp in one quarter, and pushed the score up by +0.180. Return on assets was -6.9%, below its prior range of 0.0% to 0.7%, and pushed the score up by +0.166. The provision for loan losses reached 8.7% of assets, above its prior range of 0.3% to 1.7%, and pushed the score up by +0.144. Net interest margin, the spread earned on lending and investing, slipped to 2.4%, below its prior range of 4.7% to 6.3%, and pushed the score up by +0.094.

Net loan write-offs rose to 6.3% of loans, above their prior range of 0.0% to 2.6%, yet this ratio had little effect on the score, with a contribution of -0.005.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -191.5% | 0.4% to 19.1% | same quarter, prior 3 years | n/a | -191.9 pp | +1.318 | pushed the score up |
| return on assets (profit as a share of assets) | -6.9% | 0.0% to 0.7% | same quarter, prior 3 years | n/a | -6.9 pp | +0.166 | pushed the score up |
| annualized provision for loan losses as a share of assets | 8.7% | 0.3% to 1.7% | same quarter, prior 3 years | n/a | +7.0 pp | +0.144 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.4% | 4.7% to 6.3% | same quarter, prior 3 years | n/a | -2.3 pp | +0.094 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 6.3% | 0.0% to 2.6% | same quarter, prior 3 years | n/a | +3.7 pp | -0.005 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 0.2% | 5.1% to 9.8% | prior 12 quarters | -6.5 pp | -7.2 pp | +0.180 | pushed the score up |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-03-31: Commercial Lending Specialization.

Peers: 1457 banks in the same specialty group and size tier ($100 million to $1 billion).

The Texas ratio of 280.0% was in the 100.0th percentile nationally, unusually high, and in the 100.0th percentile among peers, whose median is 3.0%, so it is unusually high among its peers too. The total risk-based capital ratio of 1.5% was in the 0.0th percentile nationally, unusually low, and in the 0.1st percentile among peers, whose median is 15.3%, so it is unusually low among its peers too. The Tier 1 risk-based capital ratio of 0.2% was in the 0.0th percentile nationally, unusually low, and in the 0.1st percentile among peers, whose median is 14.2%, so it is unusually low among its peers too. Losses on bonds available for sale at -177.9% of equity were in the 0.0th percentile nationally, unusually low, and in the 0.0th percentile among peers, whose median is 5.6%, so the figure is unusually low among its peers too.

Return on equity of -191.5% was in the 0.1st percentile nationally, unusually low, and in the 0.0th percentile among peers, whose median is 11.4%, so it is unusually low among its peers too. Nonaccrual assets and foreclosed property at 9.2% of assets were in the 99.9th percentile nationally, unusually high, and in the 99.8th percentile among peers, whose median is 0.3%, so the figure is unusually high among its peers too. The provision for loan losses at 8.7% of assets was in the 99.9th percentile nationally, unusually high, and in the 99.9th percentile among peers, whose median is 0.1%, so it is unusually high among its peers too. Loans 30-89 days past due at 5.5% of assets were in the 99.9th percentile nationally, unusually high, and in the 99.9th percentile among peers, whose median is 0.3%, so the figure is unusually high among its peers too.

Overall, 21 of the bank's ratios were in the national top or bottom 10%, and 21 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 280.0% | 100.0th (unusually high) | 3.0% | 100.0th | unusually high among its peers too |
| the total risk-based capital ratio | 1.5% | 0.0th (unusually low) | 15.3% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 0.2% | 0.0th (unusually low) | 14.2% | 0.1st | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | -177.9% | 0.0th (unusually low) | 5.6% | 0.0th | unusually low among its peers too |
| return on equity (profit as a share of equity) | -191.5% | 0.1st (unusually low) | 11.4% | 0.0th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 9.2% | 99.9th (unusually high) | 0.3% | 99.8th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 8.7% | 99.9th (unusually high) | 0.1% | 99.9th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 5.5% | 99.9th (unusually high) | 0.3% | 99.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 181.9% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 319.3% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 128.6% | 50% or more | yes |

It crossed both lines: construction loans and total commercial real estate loans.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged this bank in the quarter ending June 30, 2025. The bank failed on May 1, 2026, giving a lead time of 4 quarters between the first flag and the failure.

At that first flag, the top factors pushing the score up were the Texas ratio at 158.3% (+1.113) and the Tier 1 risk-based capital ratio at 5.6% (+1.022). Loans 90+ days past due or not accruing were already 14.7% of loans (+0.948), and the total risk-based capital ratio was 6.9% (+0.510). So the same themes of weak capital and troubled loans were visible in the data well before the failure.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the last quarter the bank reported was the one ending March 31, 2026. The bank failed on May 1, 2026, shortly after that report, so there are no later ranks in our data.

## Sources

- F1 · Bank name · n/a · Community Bank And Trust - West Georgia · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F5 · Model score · 2026-03-31 · 0.9972 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 1.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 1.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 17.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 9.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-03-31 · 8.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 280.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 3.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 91.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 16.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · -177.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-03-31 · 42.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-03-31 · 4.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.2%; contribution to the score · 2026-03-31 · +1.741 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -191.5%; contribution to the score · 2026-03-31 · +1.318 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 280.0%; contribution to the score · 2026-03-31 · +1.050 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 17.3%; contribution to the score · 2026-03-31 · +0.770 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.5%; contribution to the score · 2026-03-31 · +0.510 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -177.9%; contribution to the score · 2026-03-31 · -0.273 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: asset growth over the past four quarters, value 23.9%; contribution to the score · 2026-03-31 · -0.219 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F82 · Driver down #3: construction loans as a share of loans, value 8.1%; contribution to the score · 2026-03-31 · -0.179 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $292.6 million; contribution to the score · 2026-03-31 · -0.160 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 92.4%; contribution to the score · 2026-03-31 · -0.129 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F85 · Failure date · 2026-05-01 · 2026-05-01 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-06-30 · 2025-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-06-30: the Texas ratio (troubled assets against capital plus reserves), value 158.3%; contribution to the score · 2025-06-30 · +1.113 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2025-06-30: the Tier 1 risk-based capital ratio, value 5.6%; contribution to the score · 2025-06-30 · +1.022 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F90 · Driver up #3 at 2025-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 14.7%; contribution to the score · 2025-06-30 · +0.948 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2025-06-30: the total risk-based capital ratio, value 6.9%; contribution to the score · 2025-06-30 · +0.510 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-03-31 · -191.5% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 19.1% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-03-31 · +1.318 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-03-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.166 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-03-31 · 8.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.144 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-03-31 · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-03-31 · +0.094 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-03-31 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F130 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 5.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), change over one quarter, in percentage points · 2026-03-31 · -6.5 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.180 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F135 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: ratios outside their own prior range · 2026-03-31 · 15 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2026-03-31 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-03-31 · 280.0% · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-03-31 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F152 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-03-31 · 1.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-03-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, peer median · 2026-03-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-03-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-03-31 · -177.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F165 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F166 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F167 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F168 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-03-31 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F169 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F170 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-03-31 · -191.5% · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), peer median · 2026-03-31 · 11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-03-31 · 9.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F177 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F178 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F179 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F180 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F181 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F182 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-03-31 · 8.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F183 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F184 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F185 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F186 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-03-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F187 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F188 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F189 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F190 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F191 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F192 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F193 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F195 · Peers: ratios in the national top or bottom 10% · 2026-03-31 · 21 · data/features/fct_bank_features.parquet
- F196 · Peers: those ratios also unusual among peers · 2026-03-31 · 21 · data/features/fct_bank_features.parquet
- F198 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-03-31 · 10% · data/features/fct_bank_features.parquet
