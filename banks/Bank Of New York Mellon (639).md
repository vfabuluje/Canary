---
cert: 639
name: "Bank Of New York Mellon"
as_of: 2026-06-30
rank: 2021
n_banks: 4313
percentile: 53.16485045212149
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of New York Mellon (cert 639)

## Summary

As of 2026-06-30, Bank Of New York Mellon (New York state) ranked 2,021 out of 4,313 FDIC-insured banks on Canary's score, placing it in the 53.2nd percentile, where higher means riskier, and it was not flagged on the watchlist. Its loan book was very clean and its profits were strong, which pushed the score down, while its thin capital relative to total assets and its high interest costs pushed the score up. It relied heavily on uninsured deposits (balances above the government insurance limit) at 68.2% of deposits, well above the national median of 24.8%, but it also held cash equal to 35.8% of assets, far above the median of 6.2%.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin against total assets: equity was 6.9% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.2% versus a median of 11.0%. Measured against risk-weighted assets, where safer holdings count for less, the picture was closer to normal: the Tier 1 risk-based capital ratio was 14.6%, equal to the national median of 14.6%, and the total risk-based ratio was 14.8% against a median of 15.8%.

Credit quality was not a concern: loans 90+ days past due or no longer collecting interest were 0.0% of loans versus a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 0.1% versus 2.9%. Loan-loss reserves, money set aside for expected bad loans, were 0.4% of loans against a median of 1.2%, and lending was a small part of the business, with loans at 12.5% of deposits versus a median of 80.2%. The separate real-estate concentration check found the bank did not cross either supervisory line.

Funding stood out most: uninsured deposits were 68.2% of deposits versus a median of 24.8%, volatile funding (money that can leave quickly) was 30.2% of assets versus 9.0%, and core deposits (stable everyday deposits) were 57.0% of assets versus 75.5%. Interest expense was 3.4% of assets, about double-digit-free but well above the median of 1.6%, while cash was a large buffer at 35.8% of assets versus 6.2%. Unrealized losses on bonds held to maturity (paper losses on bonds the bank plans to keep) were 10.0% of equity versus a median of 0.0%, while losses on bonds available for sale were 2.4% of equity, below the median of 5.6%. No peer comparison is available, because only 4 banks were in its specialty group, below the minimum of 15.

## Understanding the score

As of 2026-06-30, the bank ranked 2,021 of 4,313 banks, the 53.2nd percentile on a scale where higher means riskier. It was not flagged on the watchlist, which covers the riskiest 2% of banks, or 87 banks that quarter.

Five features pushed the score up: interest expense at 3.4% of assets (+0.295), losses on bonds available for sale at 2.4% of equity (+0.091), the leverage ratio at 6.2% (+0.082), equity at 6.9% of assets (+0.062), and commercial real estate loans at 4.0% of loans (+0.057). Five features pushed it down, by larger amounts: the Texas ratio at 0.1% (-1.260), the Tier 1 risk-based capital ratio at 14.6% (-0.929), return on equity at 19.6% (-0.642), seriously late or non-paying loans at 0.0% of loans (-0.465), and securities at 36.6% of assets (-0.404). The model learned mainly from bank failures driven by loan losses, which made up 96% of the 539 failures in its training period, so its strength on credit quality weighs heavily here.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,070 | 4,589 |  |
| 2024-12-31 | 2,753 | 4,560 |  |
| 2025-03-31 | 2,115 | 4,536 |  |
| 2025-06-30 | 1,686 | 4,494 |  |
| 2025-09-30 | 2,587 | 4,452 |  |
| 2025-12-31 | 2,354 | 4,411 |  |
| 2026-03-31 | 1,656 | 4,353 |  |
| 2026-06-30 | 2,021 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 2,021 out of 4,313 banks nationally, which places it in the 53.2nd percentile, where higher means riskier. A year earlier it sat in the 62.5th percentile, so the model rated it safer than a year earlier. Of 30 ratios compared with the bank's own prior range, 8 were outside that range, and the table shows the 6 furthest outside it. Most ratios are compared with the prior 12 quarters, while year-to-date ratios are compared with the same quarter in the prior 3 years.

Each ratio's contribution is given in model log-odds units, an internal score scale where negative numbers lower the score and positive numbers raise it. Return on equity (profit as a share of shareholders' equity) was 19.6%, above its prior range of 11.6% to 15.5%, and with a contribution of -0.642 it pushed the score down. Return on assets (profit as a share of total assets) was 1.4%, just above its prior range of 0.9% to 1.3%, and with a contribution of -0.288 it pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 57.5%, below its prior range of 61.5% to 68.1%, yet despite being outside its range it had little effect on the score, contributing -0.033.

The Texas ratio (troubled assets measured against capital plus reserves) was 0.07%, below its prior range of 0.13% to 0.9%, and with a contribution of -1.260 it pushed the score down. Loans 90+ days past due or no longer collecting interest were 0.0% of loans, below their prior range of 0.1% to 0.8%, and with a contribution of -0.465 they pushed the score down. Net loan write-offs (loans written off as losses, minus recoveries) were -0.1% of loans, below their prior range of 0.0% to 0.2%, yet despite being outside the range they had little effect on the score, contributing -0.033.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 19.6% | 11.6% to 15.5% | same quarter, prior 3 years | n/a | +4.2 pp | -0.642 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 57.5% | 61.5% to 68.1% | same quarter, prior 3 years | n/a | -4.0 pp | -0.033 | little effect on the score |
| return on assets (profit as a share of assets) | 1.4% | 0.9% to 1.3% | same quarter, prior 3 years | n/a | +0.1 pp | -0.288 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 0.07% | 0.13% to 0.9% | prior 12 quarters | -0.1 pp | -0.8 pp | -1.260 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | -0.1% | 0.0% to 0.2% | same quarter, prior 3 years | n/a | -0.1 pp | -0.033 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 0.0% | 0.1% to 0.8% | prior 12 quarters | -0.05 pp | -0.7 pp | -0.465 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: International Specialization.

There are not enough comparable banks (4 in its specialty group) for a reliable comparison, so none is shown.

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 6.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 24.2% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -5.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and whether the bank kept reporting cannot be described here. This bank is filed under Canary's quiet outcome case; the outcome banner and score history table added by code show what is known.

## Sources

- F1 · Bank name · n/a · Bank Of New York Mellon · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 2,021 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 53.2% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 12.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 68.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 57.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 30.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 35.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: annualized interest expense as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · +0.295 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 2.4%; contribution to the score · 2026-06-30 · +0.091 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: the leverage ratio (core capital as a share of average assets), value 6.2%; contribution to the score · 2026-06-30 · +0.082 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver up #4: equity as a share of assets, value 6.9%; contribution to the score · 2026-06-30 · +0.062 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 4.0%; contribution to the score · 2026-06-30 · +0.057 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 0.1%; contribution to the score · 2026-06-30 · -1.260 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 14.6%; contribution to the score · 2026-06-30 · -0.929 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 19.6%; contribution to the score · 2026-06-30 · -0.642 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.465 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: securities as a share of assets, value 36.6%; contribution to the score · 2026-06-30 · -0.404 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F85 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F86 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 19.6% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.6% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 15.5% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.642 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 57.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 61.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 68.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.288 · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F107 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 0.07% · data/features/fct_bank_features.parquet: texas_ratio
- F108 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.13% · data/features/fct_bank_features.parquet: texas_ratio
- F109 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -1.260 · data/analyst/scores.parquet: feature texas_ratio contribution
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F114 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F115 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F116 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F118 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F119 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F120 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F121 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F122 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F125 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.465 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F126 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 62.5% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: banks in the peer group (including this bank) · 2026-06-30 · 4 · data/raw/specialty/: SPECGRP
- F142 · Peers: minimum peer group size · 2026-06-30 · 15 · data/raw/specialty/: SPECGRP
