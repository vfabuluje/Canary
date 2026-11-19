---
cert: 57570
name: "Comenity Capital Bank"
as_of: 2026-06-30
rank: 80
n_banks: 4313
percentile: 98.1683283097612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:09:14"
writer_model: "claude-opus-5-5"
checked: true
---

# Comenity Capital Bank (cert 57570)

*Outcome not yet known.*

## Summary

As of June 30, 2026, Comenity Capital Bank, a Utah credit-card specialist with $13.9 billion in assets, ranked 80 out of 4,313 banks on Canary's risk score, where a lower rank means a higher score. That places it in the 98.2nd percentile, on a 0 to 100 scale where higher means riskier, and it is flagged on the watchlist. Its loan losses and late payments are far above the national median, while its capital and profits are mostly at or above typical levels.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90+ days past due or not accruing interest were 3.2% of loans, against a national median of 0.5%. Loans 30-89 days past due were 2.8% of assets versus a median of 0.2%, and annualized write-offs (loans given up as lost, net of recoveries) were 7.5% of loans versus a median of 0.0%. The provision for loan losses (money set aside for expected losses) ran at 6.5% of assets against a median of 0.1%, and loan-loss reserves stood at 11.4% of loans versus a median of 1.2%. The Texas ratio (troubled assets against capital plus reserves) was 12.0%, well above the median of 2.9%.

Capital, the cushion that absorbs losses, looks solid: equity was 13.0% of assets versus a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 12.8% versus 11.0%. The total risk-based capital ratio was 17.7% versus a median of 15.8%, while the Tier 1 risk-based capital ratio was 14.2%, slightly below the median of 14.6%.

On funding, brokered deposits (money placed through intermediaries) were 9.8% of deposits versus a median of 0.0%, and core deposits (stable everyday deposits) were 64.1% of assets versus 75.5%. Interest expense was 3.3% of assets, above the median of 1.6%, and loans were 95.0% of deposits versus 80.2%. Offsetting this, uninsured deposits were only 8.8% of deposits versus a median of 24.8%, and cash was 17.8% of assets versus 6.2%. Bond losses are small: losses on bonds available for sale were 0.6% of equity versus a median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median of 0.0%.

## Understanding the score

The bank ranked 80 out of 4,313 banks in Q2 2026, which is the 98.2nd percentile. It is flagged on the watchlist, which covers the top 2% of banks by score, or 87 banks that quarter.

The five factors that pushed the score up most were the provision for loan losses at 6.5% of assets (+0.625), interest expense at 3.3% of assets (+0.488), securities at 0.8% of assets (+0.406), loans 30-89 days past due at 2.8% of assets (+0.206), and brokered deposits at 9.8% of deposits (+0.194). The five factors that pulled it down most were the Tier 1 risk-based capital ratio at 14.2% (-0.967), return on equity at 12.7% (-0.544), the leverage ratio at 12.8% (-0.456), the total risk-based capital ratio at 17.7% (-0.447), and the Texas ratio at 12.0% (-0.377).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 45 | 4,589 | ▲ watchlist |
| 2024-12-31 | 54 | 4,560 | ▲ watchlist |
| 2025-03-31 | 90 | 4,536 | ▲ watchlist |
| 2025-06-30 | 79 | 4,494 | ▲ watchlist |
| 2025-09-30 | 70 | 4,452 | ▲ watchlist |
| 2025-12-31 | 111 | 4,411 |  |
| 2026-03-31 | 63 | 4,353 | ▲ watchlist |
| 2026-06-30 | 80 | 4,313 | ▲ watchlist |

## How its ratios moved

The model rated the bank about the same as a year earlier: it sat in the 98.3rd percentile at June 30, 2025, and the 98.2nd percentile at rank 80 out of 4,313 by June 30, 2026. Of 30 ratios compared with their own prior range, 14 were outside it, and the 6 furthest outside are shown. Most ratios are compared with the prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years.

Loans 90+ days past due or not accruing interest fell to 3.2% of loans, below their prior range of 3.4% to 4.5%, and contributed -0.090, which pushed the score down. Loans 30-89 days past due were 2.8% of assets, just below a prior range of 2.9% to 3.6%, yet contributed +0.206, which pushed the score up. Annualized write-offs were 7.5% of loans, below a prior range of 8.4% to 9.5% after a change of -1.2 pp over four quarters, and contributed -0.010, which had little effect on the score. Interest expense was 3.25% of assets, below its prior range of 3.34% to 3.9%, but contributed +0.488, which pushed the score up.

Core deposits rose to 64.1% of assets, above their prior range of 48.8% to 62.3%, and contributed -0.154, which pushed the score down. Uninsured deposits climbed to 8.8% of deposits, above a prior range of 4.4% to 8.3% with a change of +2.9 pp over four quarters, yet even though this sits outside its range, it contributed -0.109, which pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 7.5% | 8.4% to 9.5% | same quarter, prior 3 years | n/a | -1.2 pp | -0.010 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 3.2% | 3.4% to 4.5% | prior 12 quarters | -0.4 pp | -0.5 pp | -0.090 | pushed the score down |
| core deposits as a share of assets | 64.1% | 48.8% to 62.3% | prior 12 quarters | +1.8 pp | +3.4 pp | -0.154 | pushed the score down |
| uninsured deposits as a share of deposits | 8.8% | 4.4% to 8.3% | prior 12 quarters | +0.5 pp | +2.9 pp | -0.109 | pushed the score down |
| annualized interest expense as a share of assets | 3.25% | 3.34% to 3.9% | same quarter, prior 3 years | n/a | -0.4 pp | +0.488 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 2.8% | 2.9% to 3.6% | prior 12 quarters | -0.1 pp | -0.2 pp | +0.206 | pushed the score up |

14 of 30 ratios were outside their prior range; the 6 furthest are shown.

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
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 0.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | n/a | 50% or more | n/a |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this fact sheet contains no data from after the as-of quarter, so there is no later result to explain here. The bank's watchlist status therefore rests on the as-of figures described above, not on any later event.

## What happened next

Looking back with hindsight, no later ranks, flags or reporting status are included in this fact sheet. Whether the bank kept reporting, and how its rank moved afterward, cannot be stated from the data provided.

## Sources

- F1 · Bank name · n/a · Comenity Capital Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 80 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 12.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 95.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 64.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 17.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $13.9 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: annualized provision for loan losses as a share of assets, value 6.5%; contribution to the score · 2026-06-30 · +0.625 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · +0.406 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.206 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 9.8%; contribution to the score · 2026-06-30 · +0.194 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.2%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 12.7%; contribution to the score · 2026-06-30 · -0.544 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 12.8%; contribution to the score · 2026-06-30 · -0.456 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 17.7%; contribution to the score · 2026-06-30 · -0.447 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 12.0%; contribution to the score · 2026-06-30 · -0.377 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F90 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 9.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · -1.2 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F94 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F95 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F96 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F97 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F100 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.090 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F101 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F102 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 64.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F103 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 48.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F104 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 62.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F107 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.154 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F108 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F109 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F110 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F113 · Trend: uninsured deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +2.9 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F114 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.109 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F115 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F116 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 3.25% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F117 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 3.34% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F118 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F120 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F121 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F122 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F123 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F124 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F127 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.206 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F128 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: the FDIC specialty group at the as-of quarter · 2026-06-30 · Credit-card Specialization (group 3) · data/raw/specialty/: SPECGRP
