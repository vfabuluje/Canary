---
cert: 28266
name: "Connect Community Bank"
as_of: 2026-06-30
rank: 9
n_banks: 4313
percentile: 99.81451425921632
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Connect Community Bank (cert 28266)

*Outcome not yet known.*

## Summary

Connect Community Bank, a bank in WA, ranked 9 out of 4,313 banks nationally on Canary's score as of 2026-06-30, which puts it in the 99.8th percentile, where higher means riskier. That placed it on Canary's watchlist, which covers the top 2% of banks by score. Its capital cushion was thin, with equity at 3.7% of assets against a national median of 10.6%, and it was losing money, with a return on equity (profit as a share of the owners' stake) of -43.1%. Its problem loans were few: loans 90+ days past due or not earning interest were just 0.1% of loans.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was the weakest area: equity was 3.7% of assets, against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 3.6%, well below the national median of 11.0%. Risk-based capital ratios, which measure capital against assets weighted by their riskiness, were also low: the Tier 1 ratio was 7.7% against a median of 14.6%, and the total ratio was 8.9% against a median of 15.8%.

Earnings were negative, with a return on assets of -1.7% against a national median of 1.2%, and a return on equity of -43.1% against a median of 11.6%. The efficiency ratio, operating costs as a share of revenue, was 153.5%, far above the national median of 62.1%, and the net interest margin (the spread earned on lending and investing) was 2.9% against a median of 3.9%. Credit quality looked sound by comparison: loans 90+ days past due or not accruing interest were 0.1% of loans against a median of 0.5%, though annualized loan write-offs were 0.3% of loans against a median of 0.0%.

Unrealized losses on bonds the bank intends to hold until they mature equaled 36.6% of equity, while the national median was 0.0%. Funding looked stable: uninsured deposits, those above the government insurance limit, were only 3.3% of deposits against a median of 24.8%, and core deposits, the steady everyday kind, were 89.8% of assets against a median of 75.5%. Cash was 10.0% of assets against a median of 6.2%, and deposits grew 22.9% over the past four quarters against a median of 4.2%.

## Understanding the score

As of 2026-06-30, the bank ranked 9 out of 4,313 banks, placing it in the 99.8th percentile on a 0 to 100 scale where higher means riskier, with a model score of 0.6118. It was flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were return on equity at -43.1% (+1.775), the Tier 1 risk-based capital ratio at 7.7% (+0.537), commercial real estate loans at 1.1% of loans (+0.369), the total risk-based capital ratio at 8.9% (+0.327), and the leverage ratio at 3.6% (+0.149). The five factors that pulled the score down most were the Texas ratio (troubled assets against capital plus reserves) at 2.6% (-1.180), loans 90+ days past due or not accruing interest at 0.1% of loans (-0.995), nonaccrual assets and foreclosed property at 0.1% of assets (-0.613), loan-loss reserves at 1.0% of loans (-0.131), and loans at 82.8% of deposits (-0.092). In short, weak profits and thin capital raised the score, while the bank's low level of troubled loans held it back.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,206 | 4,589 |  |
| 2024-12-31 | 2,128 | 4,560 |  |
| 2025-03-31 | 428 | 4,536 |  |
| 2025-06-30 | 591 | 4,494 |  |
| 2025-09-30 | 108 | 4,452 |  |
| 2025-12-31 | 64 | 4,411 | ▲ watchlist |
| 2026-03-31 | 28 | 4,353 | ▲ watchlist |
| 2026-06-30 | 9 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history: most with the prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of the 30 ratios compared, 15 sat outside their own prior range at 2026-06-30. Return on equity was -43.1%, below its prior range of -29.9% to -2.1%, and it pushed the score up by +1.775 model log-odds units. Commercial real estate loans were 1.1% of loans, above a prior range of 0.0% to 0.1%, and this pushed the score up by +0.369 model log-odds units.

Some ratios moved outside their range yet did not raise the score. Core deposits were 89.8% of assets, above their prior range of 67.7% to 78.6% after a +15.3 pp change over four quarters, but they had little effect on the score at +0.004 model log-odds units. Losses on bonds held to maturity were 36.6% of equity, above their prior range of 19.0% to 32.7%, yet they pushed the score down at -0.057 model log-odds units. Nonaccrual assets and foreclosed property were 0.1% of assets, above a prior range of 0.0% to 0.0%, yet they pushed the score down at -0.613 model log-odds units. Annualized loan write-offs were 0.3% of loans, above a prior range of 0.0% to 0.0%, but had little effect on the score at +0.046 model log-odds units.

A year earlier, on 2025-06-30, the bank sat in the 86.9th percentile, compared with the 99.8th percentile and a rank of 9 at 2026-06-30, so the model rated it riskier than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| commercial real estate loans as a share of loans | 1.1% | 0.0% to 0.1% | prior 12 quarters | +1.1 pp | +1.1 pp | +0.369 | pushed the score up |
| core deposits as a share of assets | 89.8% | 67.7% to 78.6% | prior 12 quarters | +13.6 pp | +15.3 pp | +0.004 | little effect on the score |
| return on equity (profit as a share of equity) | -43.1% | -29.9% to -2.1% | same quarter, prior 3 years | n/a | -13.2 pp | +1.775 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.3% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.3 pp | +0.046 | little effect on the score |
| losses on bonds held to maturity, as a share of equity | 36.6% | 19.0% to 32.7% | prior 12 quarters | +5.2 pp | +3.9 pp | -0.057 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 0.1% | 0.0% to 0.0% | prior 12 quarters | +0.1 pp | +0.1 pp | -0.613 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 76 banks in the same specialty group and size tier (under $100 million).

The total risk-based capital ratio was 8.9%, at the 0.2nd national percentile, which is unusually low, and at the 3.8th percentile among peers against a peer median of 24.1%, unusually low among its peers too. The Tier 1 risk-based capital ratio was 7.7%, at the 0.2nd national percentile, unusually low, and at the 3.8th percentile among peers against a peer median of 23.2%, unusually low among its peers too. The leverage ratio was 3.6%, at the 0.5th national percentile, unusually low, and at the 0.7th percentile among peers against a peer median of 12.7%, unusually low among its peers too. Equity was 3.7% of assets, at the 0.8th national percentile, unusually low, and at the 2.0th percentile among peers against a peer median of 13.1%, unusually low among its peers too.

Return on equity was -43.1%, at the 0.4th national percentile, unusually low, and at the 2.0th percentile among peers against a peer median of 2.6%, unusually low among its peers too. The efficiency ratio was 153.5%, at the 99.1st national percentile, unusually high, and at the 98.0th percentile among peers against a peer median of 83.5%, unusually high among its peers too. Losses on bonds held to maturity were 36.6% of equity, at the 99.7th national percentile, unusually high, and at the 98.0th percentile among peers against a peer median of 0.0%, unusually high among its peers too. Uninsured deposits were 3.3% of deposits, at the 0.9th national percentile, unusually low, but at the 13.8th percentile among peers against a peer median of 9.9%, typical for its peer group.

Overall, 12 of the bank's ratios sat in the national top or bottom 10%, and 10 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 8.9% | 0.2nd (unusually low) | 24.1% | 3.8th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 7.7% | 0.2nd (unusually low) | 23.2% | 3.8th | unusually low among its peers too |
| losses on bonds held to maturity, as a share of equity | 36.6% | 99.7th (unusually high) | 0.0% | 98.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -43.1% | 0.4th (unusually low) | 2.6% | 2.0th | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 3.6% | 0.5th (unusually low) | 12.7% | 0.7th | unusually low among its peers too |
| equity as a share of assets | 3.7% | 0.8th (unusually low) | 13.1% | 2.0th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 3.3% | 0.9th (unusually low) | 9.9% | 13.8th | typical for its peer group |
| the efficiency ratio (operating costs as a share of revenue) | 153.5% | 99.1st (unusually high) | 83.5% | 98.0th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 59.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 79.3% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -13.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

With hindsight, this is an open watchlist case: the bank was flagged, and our fact sheet records no later outcome for it. The fact sheet contains no data from after the as-of quarter, so there is nothing in hindsight to confirm or contradict the reasons it was flagged. The flag rests on what the bank reported at the as-of quarter, chiefly its thin capital and its losses.

## What happened next

In hindsight, our fact sheet holds no later ranks, watchlist flags or reporting status for this bank. We therefore cannot say whether its standing changed or whether it is still filing reports; in our data, a bank that stops reporting could have merged or closed, and the two are not distinguished.

## Sources

- F1 · Bank name · n/a · Connect Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WA · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.6118 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 153.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 22.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -43.1%; contribution to the score · 2026-06-30 · +1.775 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 7.7%; contribution to the score · 2026-06-30 · +0.537 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.369 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.327 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 3.6%; contribution to the score · 2026-06-30 · +0.149 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 2.6%; contribution to the score · 2026-06-30 · -1.180 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2026-06-30 · -0.995 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2026-06-30 · -0.613 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.131 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: loans as a share of deposits, value 82.8%; contribution to the score · 2026-06-30 · -0.092 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F89 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F90 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F91 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F94 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.369 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F95 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F96 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 89.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F97 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 67.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F98 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 78.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F100 · Trend: core deposits as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +15.3 pp · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F101 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.004 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F102 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -29.9% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -2.1% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +1.775 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F113 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.046 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F114 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F115 · Trend: losses on bonds held to maturity, as a share of equity, value at the as-of quarter · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F116 · Trend: losses on bonds held to maturity, as a share of equity, lowest value in the comparison window · n/a · 19.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F117 · Trend: losses on bonds held to maturity, as a share of equity, highest value in the comparison window · n/a · 32.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F120 · Trend: losses on bonds held to maturity, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · -0.057 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F121 · Trend: losses on bonds held to maturity, as a share of equity, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F127 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.613 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F128 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 86.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F140 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F141 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F142 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 3.8th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F143 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F144 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F145 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F146 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F147 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F148 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 3.8th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F149 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 23.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F150 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F151 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F152 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F153 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F154 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F155 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F156 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F157 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F164 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F165 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F166 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F167 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F170 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: equity_to_assets
- F171 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F172 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F173 · Peers: equity as a share of assets, peer median · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F174 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F175 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F176 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F177 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F178 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 13.8th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F179 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F180 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F181 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 153.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F182 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: efficiency_ratio
- F183 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F184 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F185 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 83.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F186 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F188 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
