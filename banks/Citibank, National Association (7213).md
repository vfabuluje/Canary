---
cert: 7213
name: "Citibank, National Association"
as_of: 2026-06-30
rank: 248
n_banks: 4313
percentile: 94.27312775330397
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Citibank, National Association (cert 7213)

## Summary

As of 2026-06-30, Citibank, National Association, based in SD, ranked 248 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 94.3rd percentile, where a higher percentile means the model rated it riskier. It was not flagged on the watchlist, which covers the top 2% of banks. Its funding mix pushed the score up most: core deposits (stable, everyday customer deposits) were 40.2% of assets against a national median of 75.5%, and volatile funding (money that can leave quickly) was 40.7% of assets against a median of 9.0%. Low troubled assets and solid profits and capital pulled the score down, with a Texas ratio of 2.6% and a Tier 1 risk-based capital ratio of 14.0%.

## Warning signs in the data

Capital (the owners' cushion against losses) was thinner than at most banks: equity was 8.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.9% against 11.0%. Its risk-based capital ratios were slightly below the median, with a Tier 1 ratio of 14.0% against 14.6% and a total ratio of 14.7% against 15.8%. On credit quality, loans 90+ days past due or not accruing interest were 0.7% of loans against a median of 0.5%, and annualized net write-offs (loans written off as lost) were 1.0% of loans against 0.0%. The bank held larger loan-loss reserves than most, at 2.3% of loans against a median of 1.2%, while nonaccrual assets and foreclosed property were low at 0.1% of assets against 0.3%.

Funding was the most unusual area: uninsured deposits (balances above the government insurance limit) were 47.8% of deposits against a national median of 24.8%, and brokered deposits (funds placed through middlemen) were 3.6% against 0.0%. Against that, cash was 17.7% of assets against a median of 6.2%, and loans were only 47.8% of deposits against 80.2%. Unrealized losses on bonds held to maturity were 6.0% of equity against a median of 0.0%, while losses on bonds available for sale were 0.6% of equity, well below the 5.6% median. The bank is far larger than a typical bank, with total assets of $1976.2 billion against a median of $384.7 million, and no peer comparison was possible because its specialty group had only 4 banks. The separate real-estate check found it did not cross either supervisory line for commercial real estate lending.

## Understanding the score

Citibank ranked 248 out of 4,313 banks as of 2026-06-30, which is the 94.3rd percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which held 87 banks that quarter.

The five factors that pushed the score up most were core deposits at 40.2% of assets, volatile funding at 40.7% of assets, the efficiency ratio (operating costs as a share of revenue) at 51.4%, annualized interest expense at 2.2% of assets, and commercial real estate loans at 1.3% of loans. The five factors that pulled it down most were the Texas ratio (troubled assets against capital plus reserves) at 2.6%, the Tier 1 risk-based capital ratio at 14.0%, return on equity (profit as a share of the owners' stake) at 11.7%, return on assets at 1.1%, and loans 90+ days past due or not accruing interest at 0.7% of loans. The largest single push down, from the Texas ratio at -1.069, was bigger than the largest push up, from core deposits at +0.367.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 607 | 4,589 |  |
| 2024-12-31 | 1,316 | 4,560 |  |
| 2025-03-31 | 592 | 4,536 |  |
| 2025-06-30 | 496 | 4,494 |  |
| 2025-09-30 | 412 | 4,452 |  |
| 2025-12-31 | 461 | 4,411 |  |
| 2026-03-31 | 339 | 4,353 |  |
| 2026-06-30 | 248 | 4,313 |  |

## How its ratios moved

As of Q2 2026, Citibank ranked 248 out of 4,313 banks, which places it in the 94.3rd percentile, where a higher percentile means the model rated it riskier. A year earlier, on 2025-06-30, it sat in the 89.0th percentile, and the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, usually the prior 12 quarters, 13 were outside that range, and the 6 furthest outside are discussed here.

Return on equity (profit as a share of the owners' stake) was 11.7%, above its prior range of 8.4% to 9.4%, yet its contribution of -0.569 model log-odds units pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 51.4%, below its prior range of 54.7% to 57.4%, and its contribution of +0.249 pushed the score up. Core deposits (stable, everyday customer deposits) were 40.2% of assets, above their prior range of 36.3% to 39.2%, and their contribution of +0.367 pushed the score up. The leverage ratio (core capital as a share of average assets) was 7.9%, below its prior range of 8.2% to 9.2%, and its contribution of +0.075 pushed the score up.

Uninsured deposits (balances above the government insurance limit) were 47.8% of deposits, above their prior range of 43.4% to 46.6%, but their contribution of -0.063 pushed the score down rather than up. Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 1.5% of assets, above their prior range of 0.5% to 1.2%, yet their contribution of -0.011 had little effect on the score. Contributions are in model log-odds units, where a positive number pushes the score up and a negative number pushes it down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 11.7% | 8.4% to 9.4% | same quarter, prior 3 years | n/a | +3.2 pp | -0.569 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 51.4% | 54.7% to 57.4% | same quarter, prior 3 years | n/a | -3.3 pp | +0.249 | pushed the score up |
| uninsured deposits as a share of deposits | 47.8% | 43.4% to 46.6% | prior 12 quarters | +3.0 pp | +2.8 pp | -0.063 | pushed the score down |
| core deposits as a share of assets | 40.2% | 36.3% to 39.2% | prior 12 quarters | +1.4 pp | +3.2 pp | +0.367 | pushed the score up |
| Federal Home Loan Bank borrowings as a share of assets | 1.5% | 0.5% to 1.2% | prior 12 quarters | +0.7 pp | +0.6 pp | -0.011 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 7.9% | 8.2% to 9.2% | prior 12 quarters | -0.3 pp | -1.1 pp | +0.075 | pushed the score up |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

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
| Construction and land loans ÷ capital | 4.6% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 22.2% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 2.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: this case is marked as quiet, but the fact sheet for this note contains no data from after the as-of quarter. Later ranks, watchlist flags and whether the bank kept reporting therefore cannot be described here; the score history table added by code shows any later quarters available.

## Sources

- F1 · Bank name · n/a · Citibank, National Association · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · SD · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 248 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 94.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 47.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 47.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 40.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 40.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 17.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 6.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $1976.2 billion · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: core deposits as a share of assets, value 40.2%; contribution to the score · 2026-06-30 · +0.367 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F76 · Driver up #2: volatile funding as a share of assets, value 40.7%; contribution to the score · 2026-06-30 · +0.326 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F77 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 51.4%; contribution to the score · 2026-06-30 · +0.249 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.2%; contribution to the score · 2026-06-30 · +0.234 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 1.3%; contribution to the score · 2026-06-30 · +0.163 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 2.6%; contribution to the score · 2026-06-30 · -1.069 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 14.0%; contribution to the score · 2026-06-30 · -0.929 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 11.7%; contribution to the score · 2026-06-30 · -0.569 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.321 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2026-06-30 · -0.305 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.569 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 51.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 54.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 57.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.249 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 47.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F102 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 43.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F103 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 46.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F106 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.063 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F107 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F108 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 40.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F109 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 36.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F110 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F113 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.367 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F114 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F115 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F116 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F117 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F120 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.011 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F121 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F122 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F123 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F124 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F127 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.075 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F128 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 89.0% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: how the peer group was formed · 2026-06-30 · There are not enough comparable banks (4 in its specialty group) for a reliable comparison, so none is shown. · data/raw/specialty/: SPECGRP
- F139 · Peers: banks in the peer group (including this bank) · 2026-06-30 · 4 · data/raw/specialty/: SPECGRP
