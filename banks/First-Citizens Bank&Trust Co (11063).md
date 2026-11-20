---
cert: 11063
name: "First-Citizens Bank&Trust Co"
as_of: 2026-06-30
rank: 3673
n_banks: 4313
percentile: 14.862044980292143
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:33"
writer_model: "claude-opus-5-5"
checked: true
---

# First-Citizens Bank&Trust Co (cert 11063)

## Summary

As of 2026-06-30, First-Citizens Bank&Trust Co ranked 3,673 out of 4,313 banks nationally on Canary's score, placing it at the 14.9th percentile on a 0 to 100 scale where higher means riskier. It was not on the watchlist, and the model rated it about the same as a year earlier. Its capital ratios sit below the national medians, and its troubled loans and uninsured deposits (balances above the government insurance limit) sit above them, yet its volatile funding, meaning money that can leave quickly, is unusually low. These figures point in different directions, and the model weighed them in a way that kept the bank in the lower-risk part of the ranking.

## Warning signs in the data

Capital, the owners' cushion against losses, is thinner than at the typical bank: equity was 9.8% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.7% against 11.0%. The Tier 1 risk-based capital ratio was 12.4% against a median of 14.6%, and the total risk-based capital ratio was 13.3% against 15.8%.

Credit quality is weaker than the median: loans 90+ days past due or not accruing interest were 1.1% of loans against 0.5%, and nonaccrual assets and foreclosed property were 0.7% of assets against 0.3%. The Texas ratio (troubled assets against capital plus reserves) was 7.4% against a median of 2.9%, and annualized loan write-offs, net of recoveries, were 0.3% of loans against 0.0%. Even so, the model treated these credit measures as lowering the score rather than raising it, so the raw comparison and the model's reading point different ways.

On funding, uninsured deposits were 37.4% of deposits against a median of 24.8%, brokered deposits (money placed through middlemen) were 6.3% against 0.0%, and core deposits were 67.5% of assets against 75.5%. Offsetting this, volatile funding was only 1.5% of assets against a median of 9.0%, and cash was 9.4% of assets against 6.2%. Losses on bonds held to maturity equaled 5.2% of equity against a national median of 0.0%, which the peer section found unusually high nationally but typical among similar large banks, while losses on bonds available for sale were 2.3% against a median of 5.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 3,673 out of 4,313 banks, at the 14.9th percentile on a 0 to 100 scale where higher means riskier. It was not flagged for the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

Two factors pushed the score up, both only slightly: losses on bonds available for sale at 2.3% of equity added +0.053, and Federal Home Loan Bank borrowings at 0.0% of assets added +0.004. Five factors pushed it down: the Texas ratio at 7.4% contributed -0.952, the Tier 1 risk-based capital ratio at 12.4% contributed -0.892, and return on equity (profit as a share of equity) at 10.3% contributed -0.787. Loans 90+ days past due or not accruing interest at 1.1% of loans contributed -0.363, and nonaccrual assets and foreclosed property at 0.7% of assets contributed -0.285.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3,062 | 4,589 |  |
| 2024-12-31 | 4,098 | 4,560 |  |
| 2025-03-31 | 3,906 | 4,536 |  |
| 2025-06-30 | 3,820 | 4,494 |  |
| 2025-09-30 | 3,652 | 4,452 |  |
| 2025-12-31 | 3,559 | 4,411 |  |
| 2026-03-31 | 3,718 | 4,353 |  |
| 2026-06-30 | 3,673 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 3,673 out of 4,313 banks nationally, placing it at the 14.9th percentile on a 0 to 100 scale where higher means riskier. A year earlier it sat at the 15.0th percentile, so the model rated it about the same as a year earlier. Each ratio is compared with its own prior range, usually over the prior 12 quarters, or over the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked, 12 were outside their own prior range, and the 6 furthest outside are discussed here.

Brokered deposits (money placed through middlemen rather than gathered directly) were 6.3% of deposits, above their prior range of 2.2% to 4.9%, yet their contribution of -0.147 model log-odds units pushed the score down. That share rose +1.4 pp over one quarter and +2.7 pp over four quarters. The Texas ratio (troubled assets against capital plus reserves) was 7.4%, just above its prior range of 4.8% to 7.1%, but its contribution of -0.952 pushed the score down.

The total risk-based capital ratio (the bank's cushion of capital against its risk-weighted assets) was 13.3%, below its prior range of 13.5% to 15.7%, and its contribution of -0.243 pushed the score down. Loans as a share of deposits were 86.0%, below their prior range of 86.5% to 93.1%, with a contribution of -0.071 that pushed the score down. The annualized provision for loan losses (money set aside for expected bad loans) was 0.05% of assets, below its prior range of 0.14% to 0.9%, and its contribution of -0.100 pushed the score down. Net interest margin (the spread earned on lending and investing) was 3.1%, below its prior range of 3.3% to 3.7%, with a contribution of -0.065 that pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| brokered deposits as a share of deposits | 6.3% | 2.2% to 4.9% | prior 12 quarters | +1.4 pp | +2.7 pp | -0.147 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.1% | 3.3% to 3.7% | same quarter, prior 3 years | n/a | -0.1 pp | -0.065 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 7.4% | 4.8% to 7.1% | prior 12 quarters | +0.2 pp | +0.9 pp | -0.952 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.05% | 0.14% to 0.9% | same quarter, prior 3 years | n/a | -0.2 pp | -0.100 | pushed the score down |
| the total risk-based capital ratio | 13.3% | 13.5% to 15.7% | prior 12 quarters | -0.2 pp | -0.7 pp | -0.243 | pushed the score down |
| loans as a share of deposits | 86.0% | 86.5% to 93.1% | prior 12 quarters | -0.4 pp | -1.2 pp | -0.071 | pushed the score down |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

Volatile funding, meaning money that can leave a bank quickly, made up 1.5% of the bank's assets, which puts it at the 6.2nd percentile nationally, an unusually low level. Within its peer group, volatile funding sat at the 1.4th percentile against a peer median of 6.9%, which is unusually low among its peers too.

Losses on bonds held to maturity are the drop in value of bonds the bank plans to keep until they are repaid. Here they equaled 5.2% of equity, the owners' cushion against losses, which puts the bank at the 92.3rd percentile nationally, an unusually high level. Within its peer group, this ratio sat at the 85.4th percentile against a peer median of 1.5%, which is typical for its peer group.

Overall, 2 of the bank's ratios fall in the national top or bottom 10%, and 1 of those is also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| volatile funding as a share of assets | 1.5% | 6.2nd (unusually low) | 6.9% | 1.4th | unusually low among its peers too |
| losses on bonds held to maturity, as a share of equity | 5.2% | 92.3rd (unusually high) | 1.5% | 85.4th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 30.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 94.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 20.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this memo contains no data from after the as-of quarter, so this section cannot report later ranks, watchlist flags or whether the bank kept reporting. The score history table added by code shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · First-Citizens Bank&Trust Co · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,673 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 14.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 37.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 6.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 67.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 2.3%; contribution to the score · 2026-06-30 · +0.053 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: Federal Home Loan Bank borrowings as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · +0.004 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F77 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 7.4%; contribution to the score · 2026-06-30 · -0.952 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver down #2: the Tier 1 risk-based capital ratio, value 12.4%; contribution to the score · 2026-06-30 · -0.892 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver down #3: return on equity (profit as a share of equity), value 10.3%; contribution to the score · 2026-06-30 · -0.787 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · -0.363 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.285 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F86 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 6.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F87 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F88 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F89 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +1.4 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F90 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +2.7 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F91 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.147 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F92 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F93 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F94 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F95 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F97 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.065 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F98 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 4.8% · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 7.1% · data/features/fct_bank_features.parquet: texas_ratio
- F104 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -0.952 · data/analyst/scores.parquet: feature texas_ratio contribution
- F105 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F106 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.05% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.14% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F108 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F110 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.100 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F112 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F113 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 13.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F114 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F117 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.243 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F118 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F119 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 86.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F120 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 86.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F121 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 93.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F124 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.071 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F125 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 15.0% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F137 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.2nd · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F138 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F139 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 1.4th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F140 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F141 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F142 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.3rd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F144 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F145 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 85.4th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F146 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F147 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F149 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F150 · Peers: those ratios also unusual among peers · 2026-06-30 · 1 · data/features/fct_bank_features.parquet
- F152 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
