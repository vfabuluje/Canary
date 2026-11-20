---
cert: 6384
name: "Pnc Bank National Assn"
as_of: 2026-06-30
rank: 3480
n_banks: 4313
percentile: 19.336888476698356
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# Pnc Bank National Assn (cert 6384)

## Summary

As of 2026-06-30, Pnc Bank National Assn ranked 3,480 out of 4,313 banks nationally on Canary's risk score, which places it at the 19.3rd percentile, where higher means riskier. It is a very large bank, with total assets of $609.8 billion against a national median of $384.7 million, and it was not flagged on the watchlist. Its capital cushions sit below the national medians, with a Tier 1 risk-based capital ratio of 11.2% against a median of 14.6%, while its troubled loans are low in absolute terms and its commercial real estate lending is light. The model rated it riskier than a year earlier, when it sat at the 12.3rd percentile, but it remained in the lower-risk part of the list.

## Warning signs in the data

Capital, the owners' money that absorbs losses, is the clearest soft spot: equity was 10.4% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.0% against 11.0%. The risk-based measures, which weight assets by how risky they are, were further below the median, with a Tier 1 ratio of 11.2% against 14.6% and a total risk-based capital ratio of 12.8% against 15.8%. The peer section notes that the Tier 1 ratio is unusually low among similar large commercial lenders too.

Credit quality, meaning how well borrowers are repaying, was slightly weaker than the median: loans 90 or more days past due or not accruing interest were 0.7% of loans against 0.5%, and net write-offs were 0.2% of loans against 0.0%. The Texas ratio, troubled assets measured against capital plus reserves, was 4.1% against a national median of 2.9%, although the trend section shows it fell below its own prior range. Commercial real estate loans were only 7.3% of loans against a median of 23.6%, and the concentration section found the bank did not cross either regulatory screen line.

On funding, uninsured deposits (balances above the government insurance limit) were 44.8% of deposits against a national median of 24.8%, and Federal Home Loan Bank borrowings were 6.6% of assets against 0.2%. Cash was 4.7% of assets against a median of 6.2%, while volatile funding, money that can leave quickly, was lower than typical at 4.7% against 9.0%. Paper losses on bonds held to maturity equaled 4.6% of equity against a national median of 0.0%, while losses on bonds available for sale were 3.4% of equity against 5.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 3,480 out of 4,313 banks, at the 19.3rd percentile on a scale of 0 to 100 where higher means riskier. It was not on the watchlist, which covers the top 2% of banks by score and held 87 banks that quarter.

Two features pushed the score up: commercial real estate loans as a share of loans, at 7.3%, added +0.203, and losses on bonds available for sale as a share of equity, at 3.4%, added +0.036. Five features pushed it down, led by the Texas ratio at 4.1%, contributing -1.091, and the Tier 1 risk-based capital ratio at 11.2%, contributing -0.925. Return on equity (profit as a share of the owners' stake) at 12.6% contributed -0.733, loans 90 or more days past due or not accruing interest at 0.7% contributed -0.387, and interest expense as a share of assets at 1.5% contributed -0.314.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,636 | 4,589 |  |
| 2024-12-31 | 3,834 | 4,560 |  |
| 2025-03-31 | 3,798 | 4,536 |  |
| 2025-06-30 | 3,942 | 4,494 |  |
| 2025-09-30 | 3,311 | 4,452 |  |
| 2025-12-31 | 3,347 | 4,411 |  |
| 2026-03-31 | 3,522 | 4,353 |  |
| 2026-06-30 | 3,480 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 3,480 out of 4,313 banks nationally, placing it at the 19.3rd percentile, where higher means riskier. A year earlier it sat at the 12.3rd percentile, so the model rated it riskier than a year earlier, though it remained in the lower-risk part of the list. Each ratio is compared with its own prior range, usually the prior 12 quarters, and 14 of the 30 ratios checked sat outside that range. Contributions below are in model log-odds units, an internal scoring scale where negative numbers push the score down, toward lower risk.

Asset growth over the past four quarters reached 10.0%, well above its prior range of -2.2% to 3.7%, yet its contribution of -0.069 pushed the score down. Deposit growth over the past four quarters was 5.7%, above its prior range of -3.2% to 3.9%, and its contribution of -0.146 also pushed the score down. Loans as a share of deposits stood at 79.7%, above its prior range of 72.2% to 77.5%, but its contribution of -0.115 pushed the score down.

The efficiency ratio, operating costs as a share of revenue, was 59.2%, just above its prior range of 58.0% to 59.0%, while its contribution of -0.076 pushed the score down. Net interest margin, the spread earned on lending and investing, was 3.2%, above its prior range of 2.8% to 3.0%, but its contribution of -0.050 had little effect on the score. The Texas ratio, troubled assets measured against capital plus reserves, fell to 4.1%, below its prior range of 4.5% to 6.3%, and its contribution of -1.091 pushed the score down by the largest amount among these ratios.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| asset growth over the past four quarters | 10.0% | -2.2% to 3.7% | prior 12 quarters | +6.6 pp | +9.6 pp | -0.069 | pushed the score down |
| loans as a share of deposits | 79.7% | 72.2% to 77.5% | prior 12 quarters | +2.2 pp | +5.0 pp | -0.115 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 59.2% | 58.0% to 59.0% | same quarter, prior 3 years | n/a | +1.0 pp | -0.076 | pushed the score down |
| deposit growth over the past four quarters | 5.7% | -3.2% to 3.9% | prior 12 quarters | +2.9 pp | +3.4 pp | -0.146 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 4.1% | 4.5% to 6.3% | prior 12 quarters | -0.5 pp | -0.5 pp | -1.091 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.2% | 2.8% to 3.0% | same quarter, prior 3 years | n/a | +0.2 pp | -0.050 | little effect on the score |

14 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

The first ratio is losses on bonds held to maturity as a share of equity, meaning paper losses on bonds the bank plans to keep until they pay out, measured against the owners' cushion (equity). At 4.6%, this ratio sits at the 91.3rd percentile nationally, which is unusually high. Among its peers it sits at the 78.3rd percentile against a peer median of 1.5%, which is typical for its peer group.

The second ratio is the Tier 1 risk-based capital ratio, which compares the bank's core capital (its strongest loss-absorbing funds) with its assets weighted by how chancy they are. At 11.2%, this ratio sits at the 9.6th percentile nationally, which is unusually low. Among its peers it sits at the 6.0th percentile against a peer median of 12.7%, which is unusually low among its peers too.

Overall, 2 of the bank's ratios fall in the national top or bottom 10%, and 1 of those is also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 4.6% | 91.3rd (unusually high) | 1.5% | 78.3rd | typical for its peer group |
| the Tier 1 risk-based capital ratio | 11.2% | 9.6th (unusually low) | 12.7% | 6.0th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 9.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 88.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 2.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: this bank falls in the quiet outcome group, meaning no failure is recorded for it after the as-of quarter. The fact sheet does not include its later ranks, watchlist flags or reporting status, so this memo cannot say more about what followed.

## Sources

- F1 · Bank name · n/a · Pnc Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,480 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 19.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 44.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $609.8 billion · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: commercial real estate loans as a share of loans, value 7.3%; contribution to the score · 2026-06-30 · +0.203 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 3.4%; contribution to the score · 2026-06-30 · +0.036 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 4.1%; contribution to the score · 2026-06-30 · -1.091 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver down #2: the Tier 1 risk-based capital ratio, value 11.2%; contribution to the score · 2026-06-30 · -0.925 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver down #3: return on equity (profit as a share of equity), value 12.6%; contribution to the score · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2026-06-30 · -0.387 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #5: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2026-06-30 · -0.314 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F86 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F87 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · -2.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F88 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F91 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.069 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F92 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F93 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 79.7% · data/features/fct_bank_features.parquet: loans_to_deposits
- F94 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 72.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F95 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 77.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F98 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.115 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F99 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 59.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 58.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 59.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.076 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F106 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F107 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -3.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F108 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F111 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.146 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F112 · Trend: deposit growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: texas_ratio
- F118 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -1.091 · data/analyst/scores.parquet: feature texas_ratio contribution
- F119 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F120 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F122 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F124 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.050 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F125 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 12.3% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F137 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 91.3rd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F138 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F139 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 78.3rd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F140 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F141 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F143 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 9.6th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F144 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F145 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 6.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F146 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F147 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F149 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F150 · Peers: those ratios also unusual among peers · 2026-06-30 · 1 · data/features/fct_bank_features.parquet
- F152 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
