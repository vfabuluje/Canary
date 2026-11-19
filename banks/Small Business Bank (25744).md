---
cert: 25744
name: "Small Business Bank"
as_of: 2026-03-31
rank: 10
n_banks: 4353
percentile: 99.79324603721571
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-17
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Small Business Bank (cert 25744)

*Hindsight: failed 2026-07-17. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

Small Business Bank, based in KS, ranked 10 out of 4,353 banks nationally as of 2026-03-31, which places it in the 99.8th percentile of Canary's risk ranking. That puts it on Canary's watchlist, which covers the top 2% of banks by score. Its capital cushion is thin and it is losing money: equity equals 4.9% of assets against a national median of 10.4%, and return on assets (profit as a share of assets) is -4.3% against a median of 1.2%.

## Warning signs in the data

Capital, the cushion that absorbs losses, is thin: equity equals 4.9% of assets versus a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) is 4.8% versus a median of 10.9%. Its risk-based capital ratios, which weight assets by how risky they are, sit close to the median, with Tier 1 capital at 14.0% versus 14.5% and total capital at 15.3% versus 15.7%.

Credit quality, meaning how well borrowers are repaying, is weak: loans 90+ days past due or not accruing interest are 4.8% of loans versus a national median of 0.5%, and loans 30-89 days past due equal 9.4% of assets versus 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, is 55.5% against a median of 2.9%, and reserves set aside for loan losses are 2.9% of loans versus 1.2%. Earnings are deeply negative, with return on equity (profit as a share of equity) at -79.5% versus a median of 11.2% and the efficiency ratio (operating costs as a share of revenue) at 249.0% versus 63.1%.

Funding looks steadier by comparison: core deposits, the stable everyday deposits, are 94.3% of assets versus a median of 75.8%, uninsured deposits are 9.9% of deposits versus 24.4%, and cash is 13.2% of assets versus 6.9%. Total assets changed by -14.3% over the past four quarters, while the median bank grew 4.3%. The bank holds no securities, 0.0% of assets versus a median of 17.5%, so its losses on bonds available for sale are 0.0% of equity versus a median of 5.8%.

## Understanding the score

Small Business Bank ranks 10 out of 4,353 banks as of 2026-03-31, placing it in the 99.8th percentile on a 0 to 100 scale where higher means riskier. That puts it on the watchlist, which holds the top 2% of banks, or 88 banks that quarter.

Five factors pushed the score up the most. Return on equity of -79.5% added the most, +1.253. Core deposits at 94.3% of assets added +0.516. The Texas ratio of 55.5% added +0.505. Interest expense equal to 2.4% of assets added +0.351. Return on assets of -4.3% added +0.306.

Five factors pulled the score down. The Tier 1 risk-based capital ratio of 14.0% pulled it down the most, -1.507. Construction loans at 2.7% of loans contributed -0.283. The total risk-based capital ratio of 15.3% contributed -0.273. Uninsured deposits at 9.9% of deposits contributed -0.192. Commercial real estate loans at 28.0% of loans contributed -0.125.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 441 | 4,610 |  |
| 2024-09-30 | 799 | 4,589 |  |
| 2024-12-31 | 374 | 4,560 |  |
| 2025-03-31 | 106 | 4,536 |  |
| 2025-06-30 | 440 | 4,494 |  |
| 2025-09-30 | 65 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 8 | 4,411 | ▲ watchlist |
| 2026-03-31 | 10 | 4,353 | ▲ watchlist |

## How its ratios moved

Canary compared 28 of the bank's ratios with their own prior range, mostly over the prior 12 quarters, and 9 were outside that range. Overall, the model rated it riskier than a year earlier: it was in the 97.7th percentile at 2025-03-31 and in the 99.8th percentile now, ranked 10 of 4,353.

Loans 30-89 days past due reached 9.4% of assets, above their prior range of 0.0% to 6.2%, and this pushed the score up, contributing +0.273 model log-odds units. That share rose +3.2 pp over one quarter and +8.5 pp over four quarters. The Texas ratio stood at 55.5%, above its prior range of 4.3% to 49.7%, and pushed the score up, contributing +0.505. Loan-loss reserves rose to 2.9% of loans, above their prior range of 0.6% to 2.7%, and pushed the score up, contributing +0.077.

Equity fell to 4.9% of assets, below its prior range of 5.9% to 10.7%, and pushed the score up, contributing +0.104. The leverage ratio fell to 4.8%, below its prior range of 5.7% to 10.1%, and pushed the score up, contributing +0.105. Core deposits rose to 94.3% of assets, above their prior range of 88.6% to 93.3%, and pushed the score up, contributing +0.516.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 9.4% | 0.0% to 6.2% | prior 12 quarters | +3.2 pp | +8.5 pp | +0.273 | pushed the score up |
| equity as a share of assets | 4.9% | 5.9% to 10.7% | prior 12 quarters | -1.1 pp | -5.2 pp | +0.104 | pushed the score up |
| core deposits as a share of assets | 94.3% | 88.6% to 93.3% | prior 12 quarters | +1.0 pp | +5.4 pp | +0.516 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 4.8% | 5.7% to 10.1% | prior 12 quarters | -0.9 pp | -3.5 pp | +0.105 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 55.5% | 4.3% to 49.7% | prior 12 quarters | +5.8 pp | +40.7 pp | +0.505 | pushed the score up |
| loan-loss reserves as a share of loans | 2.9% | 0.6% to 2.7% | prior 12 quarters | +0.2 pp | +1.2 pp | +0.077 | pushed the score up |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-03-31: Agricultural Specialization.

Peers: 232 banks in the same specialty group and size tier (under $100 million).

Loans 30-89 days past due, at 9.4% of assets, sit in the 100.0th national percentile, unusually high, and in the 99.8th percentile among peers against a peer median of 0.2%, unusually high among its peers too. The Texas ratio of 55.5% is in the 99.5th national percentile, unusually high, and in the 98.5th percentile among peers against a peer median of 1.4%, unusually high among its peers too. The efficiency ratio of 249.0% is in the 99.6th national percentile, unusually high, and in the 99.4th percentile among peers against a peer median of 65.7%, unusually high among its peers too. Core deposits at 94.3% of assets are in the 99.9th national percentile, unusually high, and in the 99.8th percentile among peers against a peer median of 79.8%, unusually high among its peers too.

Return on equity of -79.5% is in the 0.2nd national percentile, unusually low, and in the 0.6th percentile among peers against a peer median of 9.8%, unusually low among its peers too. Return on assets of -4.3% is in the 0.7th national percentile, unusually low, and in the 0.6th percentile among peers against a peer median of 1.2%, unusually low among its peers too. The leverage ratio of 4.8% is in the 0.6th national percentile, unusually low, and in the 0.6th percentile among peers against a peer median of 12.1%, unusually low among its peers too. Asset growth of -14.3% is in the 0.6th national percentile, unusually low, and in the 1.1st percentile among peers against a peer median of 3.5%, unusually low among its peers too.

Overall, 19 of the bank's ratios fall in the national top or bottom 10%, and 17 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 9.4% | 100.0th (unusually high) | 0.2% | 99.8th | unusually high among its peers too |
| core deposits as a share of assets | 94.3% | 99.9th (unusually high) | 79.8% | 99.8th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -79.5% | 0.2nd (unusually low) | 9.8% | 0.6th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 249.0% | 99.6th (unusually high) | 65.7% | 99.4th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 55.5% | 99.5th (unusually high) | 1.4% | 98.5th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 4.8% | 0.6th (unusually low) | 12.1% | 0.6th | unusually low among its peers too |
| asset growth over the past four quarters | -14.3% | 0.6th (unusually low) | 3.5% | 1.1st | unusually low among its peers too |
| return on assets (profit as a share of assets) | -4.3% | 0.7th (unusually low) | 1.2% | 0.6th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 30.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 82.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -56.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged the bank at 2025-09-30, 4 quarters before it failed on 2026-07-17. At that first flag, the biggest drivers pushing the score up were return on equity of -66.8%, adding +1.081, and interest expense at 2.5% of assets, adding +0.347. Loan-loss provisions, money set aside for expected bad loans, equal to 2.5% of assets also added +0.319. At that time its Tier 1 risk-based capital ratio was still 21.6%, which pulled the score down by -1.700.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the last quarter the bank reported was 2026-03-31, and it failed on 2026-07-17. Because it stopped reporting after that quarter, there are no later ranks or flags to show. In our data, stopping reporting can mean either a merger or a closure, but here the recorded failure date shows how the story ended.

## Sources

- F1 · Bank name · n/a · Small Business Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 4.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -79.5% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-03-31 · 11.2% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 249.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-03-31 · 17.5% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-03-31 · -14.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-03-31 · 4.3% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -79.5%; contribution to the score · 2026-03-31 · +1.253 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: core deposits as a share of assets, value 94.3%; contribution to the score · 2026-03-31 · +0.516 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 55.5%; contribution to the score · 2026-03-31 · +0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-03-31 · +0.351 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: return on assets (profit as a share of assets), value -4.3%; contribution to the score · 2026-03-31 · +0.306 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.0%; contribution to the score · 2026-03-31 · -1.507 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 2.7%; contribution to the score · 2026-03-31 · -0.283 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 15.3%; contribution to the score · 2026-03-31 · -0.273 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 9.9%; contribution to the score · 2026-03-31 · -0.192 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 28.0%; contribution to the score · 2026-03-31 · -0.125 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2026-07-17 · 2026-07-17 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -66.8%; contribution to the score · 2025-09-30 · +1.081 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.347 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F90 · Driver up #3 at 2025-09-30: annualized provision for loan losses as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.319 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F93 · Driver down #1 at 2025-09-30: the Tier 1 risk-based capital ratio, value 21.6%; contribution to the score · 2025-09-30 · -1.700 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F104 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F105 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 6.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2026-03-31 · +3.2 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F107 · Trend: loans 30-89 days past due, as a share of assets, change over four quarters, in percentage points · 2026-03-31 · +8.5 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F108 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.273 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F109 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F110 · Trend: equity as a share of assets, value at the as-of quarter · 2026-03-31 · 4.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F111 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F112 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F115 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.104 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F116 · Trend: equity as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 88.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 93.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.516 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F125 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 5.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F126 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 10.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F129 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.105 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 49.7% · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-03-31 · +0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F137 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F138 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F139 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F140 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F143 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-03-31 · +0.077 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F144 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F145 · Trend: ratios outside their own prior range · 2026-03-31 · 9 · data/features/fct_bank_features.parquet
- F147 · Trend: ratios compared with their own prior range · 2026-03-31 · 28 · data/features/fct_bank_features.parquet
- F148 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F150 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 97.7% · data/analyst/scores.parquet: percentile
- F151 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F155 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F156 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F157 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F159 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F160 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F161 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F162 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F163 · Peers: core deposits as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F164 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.8th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F165 · Peers: core deposits as a share of assets, peer median · 2026-03-31 · 79.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F166 · Peers: core deposits as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F167 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-03-31 · -79.5% · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F169 · Peers: return on equity (profit as a share of equity), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), peer median · 2026-03-31 · 9.8% · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-03-31 · 249.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-03-31 · 99.6th · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-03-31 · 99.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-03-31 · 65.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-03-31 · 99.5th · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F182 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-03-31 · 98.5th · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-03-31 · 1.4% · data/features/fct_bank_features.parquet: texas_ratio
- F184 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F185 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F186 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F187 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F188 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F189 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-03-31 · 12.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F190 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F191 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-03-31 · -14.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: asset_growth_4q
- F193 · Peers: asset growth over the past four quarters, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-03-31 · 1.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F195 · Peers: asset growth over the past four quarters, peer median · 2026-03-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F196 · Peers: asset growth over the past four quarters, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F197 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-03-31 · -4.3% · data/features/fct_bank_features.parquet: return_on_assets
- F198 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.7th · data/features/fct_bank_features.parquet: return_on_assets
- F199 · Peers: return on assets (profit as a share of assets), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F200 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: return_on_assets
- F201 · Peers: return on assets (profit as a share of assets), peer median · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F202 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F204 · Peers: ratios in the national top or bottom 10% · 2026-03-31 · 19 · data/features/fct_bank_features.parquet
- F205 · Peers: those ratios also unusual among peers · 2026-03-31 · 17 · data/features/fct_bank_features.parquet
- F207 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-03-31 · 10% · data/features/fct_bank_features.parquet
