---
cert: 4297
name: "Capital One National Assn"
as_of: 2026-06-30
rank: 795
n_banks: 4313
percentile: 81.59054022722003
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# Capital One National Assn (cert 4297)

## Summary

As of 2026-06-30, Capital One National Assn ranked 795 out of 4,313 banks on Canary's risk score, placing it in the 81.6th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks by score. Its credit-loss figures, such as annualized loan write-offs (loans written off as uncollectable, net of recoveries) of 3.3% against a national median of 0.0%, were far above typical banks, while its profits and equity cushion were above the median. The model rated it safer than a year earlier, when it sat in the 96.5th percentile.

## Warning signs in the data

Credit quality is where the bank stands out most. Loans 90+ days past due or not accruing interest (no longer paying as agreed) were 1.5% of loans, against a national median of 0.5%, and loans 30-89 days past due were 1.4% of assets, against a median of 0.2%. Net loan write-offs ran at 3.3% of loans against a median of 0.0%, and the annualized provision for loan losses (money set aside for expected bad loans) was 2.1% of assets against a median of 0.1%. Its loan-loss reserves, the cushion already set aside for bad loans, were 5.0% of loans, well above the median of 1.2%.

Capital was mixed: equity was 14.9% of assets, well above the median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 10.6% against 11.0%, the Tier 1 risk-based capital ratio (core capital against risk-weighted assets) was 13.2% against 14.6%, and the total risk-based capital ratio was 14.9% against 15.8%, all slightly below the median. Unrealized losses on bonds available for sale (bonds worth less than their purchase price) equalled 7.0% of equity, somewhat above the median of 5.6%.

Funding looked steadier: uninsured deposits were 20.8% of deposits against a median of 24.8%, and volatile funding (money that can leave quickly) was 3.1% of assets against 9.0%, though brokered deposits (deposits placed through middlemen) were 3.3% of deposits against a median of 0.0%. Cash was 7.9% of assets, above the median of 6.2%. The bank sits in the FDIC's Credit-card Specialization (group 3) group, which had only 10 banks, below the minimum of 15 needed for a peer comparison, so these figures are compared with all banks nationally rather than similar lenders. The separate real-estate concentration check found it did not cross either supervisory line.

## Understanding the score

The bank ranked 795 out of 4,313 banks as of 2026-06-30, which is the 81.6th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which held 87 banks that quarter.

The five features that pushed the score up most were the annualized provision for loan losses at 2.1% of assets (contribution +0.538), the efficiency ratio (operating costs as a share of revenue) at 50.6% (+0.314), losses on bonds available for sale at 7.0% of equity (+0.279), annualized interest expense at 2.4% of assets (+0.258), and commercial real estate loans at 3.3% of loans (+0.211). The five that pushed it down most were the Texas ratio (troubled assets against capital plus reserves) at 5.7% (contribution -1.068), the Tier 1 risk-based capital ratio at 13.2% (-0.978), return on equity (profit as a share of equity) at 11.3% (-0.512), loans 90+ days past due or not accruing interest at 1.5% of loans (-0.345), and return on assets (profit as a share of assets) at 1.7% (-0.320). Some directions look counterintuitive, such as a low commercial real estate share adding to the score and a high past-due share lowering it, which reflects how the model weighs each figure alongside the others rather than on its own.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 355 | 4,589 |  |
| 2024-12-31 | 67 | 4,560 | ▲ watchlist |
| 2025-03-31 | 580 | 4,536 |  |
| 2025-06-30 | 158 | 4,494 |  |
| 2025-09-30 | 100 | 4,452 |  |
| 2025-12-31 | 106 | 4,411 |  |
| 2026-03-31 | 185 | 4,353 |  |
| 2026-06-30 | 795 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 795 out of 4,313 banks, placing it in the 81.6th percentile on a scale of 0 to 100 where higher means riskier. A year earlier, on 2025-06-30, it sat in the 96.5th percentile, so the model rated it safer than a year earlier. Each ratio is compared with its own prior range, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked, 8 sat outside their own prior range, and the 6 furthest outside are covered here.

A ratio's contribution is measured in model log-odds units, where a positive value pushes the score up and a negative value pushes it down. The Texas ratio (troubled assets against capital plus reserves) was 5.7%, below its prior range of 6.1% to 8.9%, and it pushed the score down with a contribution of -1.068. Return on equity (profit as a share of equity) was 11.3%, above its prior range of -7.4% to 10.1%, and it pushed the score down with a contribution of -0.512. Return on assets (profit as a share of assets) was 1.7%, above its prior range of -1.0% to 1.1%, and it pushed the score down with a contribution of -0.320. Volatile funding as a share of assets was 3.1%, below its prior range of 3.5% to 5.1%, and it pushed the score down with a contribution of -0.273. So although these four ratios moved outside their usual ranges, each one lowered the score rather than raising it.

The net interest margin (the spread earned on lending and investing) was 8.5%, above its prior range of 7.0% to 7.6%, yet it had little effect on the score, with a contribution of +0.046. The efficiency ratio (operating costs as a share of revenue) was 50.6%, below its prior range of 52.1% to 54.8%, and it pushed the score up with a contribution of +0.314. That efficiency ratio fell by -4.2 pp over four quarters, meaning costs took a smaller share of revenue, even though the model treated this ratio as adding to the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| net interest margin (the spread earned on lending and investing) | 8.5% | 7.0% to 7.6% | same quarter, prior 3 years | n/a | +0.9 pp | +0.046 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 50.6% | 52.1% to 54.8% | same quarter, prior 3 years | n/a | -4.2 pp | +0.314 | pushed the score up |
| return on assets (profit as a share of assets) | 1.7% | -1.0% to 1.1% | same quarter, prior 3 years | n/a | +2.6 pp | -0.320 | pushed the score down |
| volatile funding as a share of assets | 3.1% | 3.5% to 5.1% | prior 12 quarters | -0.6 pp | -0.8 pp | -0.273 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 5.7% | 6.1% to 8.9% | prior 12 quarters | -0.6 pp | -0.4 pp | -1.068 | pushed the score down |
| return on equity (profit as a share of equity) | 11.3% | -7.4% to 10.1% | same quarter, prior 3 years | n/a | +18.7 pp | -0.512 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Credit-card Specialization.

There are not enough comparable banks (10 in its specialty group) for a reliable comparison, so none is shown.

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 2.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 52.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -5.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks beyond the as-of quarter, and this case is classed as quiet. The fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and whether the bank kept reporting cannot be stated here. The score history table added by code shows any later quarters that are available.

## Sources

- F1 · Bank name · n/a · Capital One National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 795 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 81.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 14.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 20.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: annualized provision for loan losses as a share of assets, value 2.1%; contribution to the score · 2026-06-30 · +0.538 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 50.6%; contribution to the score · 2026-06-30 · +0.314 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: losses on bonds available for sale, as a share of equity, value 7.0%; contribution to the score · 2026-06-30 · +0.279 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.258 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 3.3%; contribution to the score · 2026-06-30 · +0.211 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 5.7%; contribution to the score · 2026-06-30 · -1.068 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 13.2%; contribution to the score · 2026-06-30 · -0.978 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 11.3%; contribution to the score · 2026-06-30 · -0.512 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.5%; contribution to the score · 2026-06-30 · -0.345 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.7%; contribution to the score · 2026-06-30 · -0.320 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F90 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 7.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F91 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 7.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F93 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · +0.046 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F94 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 50.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 52.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 54.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · -4.2 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.314 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.320 · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F107 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F108 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F109 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F112 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.273 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F113 · Trend: volatile funding as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: texas_ratio
- F119 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -1.068 · data/analyst/scores.parquet: feature texas_ratio contribution
- F120 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F121 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: return_on_equity
- F122 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -7.4% · data/features/fct_bank_features.parquet: return_on_equity
- F123 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 10.1% · data/features/fct_bank_features.parquet: return_on_equity
- F125 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.512 · data/analyst/scores.parquet: feature return_on_equity contribution
- F126 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.5% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: the FDIC specialty group at the as-of quarter · 2026-06-30 · Credit-card Specialization (group 3) · data/raw/specialty/: SPECGRP
- F137 · Peers: banks in the peer group (including this bank) · 2026-06-30 · 10 · data/raw/specialty/: SPECGRP
- F142 · Peers: minimum peer group size · 2026-06-30 · 15 · data/raw/specialty/: SPECGRP
