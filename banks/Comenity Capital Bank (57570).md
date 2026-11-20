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
written_at: "2026-11-19T21:17:04"
writer_model: "claude-opus-5-5"
checked: true
---

# Comenity Capital Bank (cert 57570)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Comenity Capital Bank of UT ranked 80 out of 4,313 FDIC-insured banks, the 98.2nd percentile, which puts it on Canary's watchlist of the top 2% of banks by model score. The score is pushed up mainly by heavy loan-loss provisions, meaning money set aside for expected loan losses, and by high interest costs, while its strong capital and solid profits pull it down. Its FDIC specialty group is Credit-card Specialization (group 3), and its credit-quality ratios sit far from the national median even though several were below their own recent range.

## Warning signs in the data

Capital, the cushion that absorbs losses, looks healthy: equity was 13.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 12.8% against 11.0%. The total risk-based capital ratio was 17.7% against a median of 15.8%, while the Tier 1 risk-based capital ratio, a core capital measure weighted by asset riskiness, was 14.2%, slightly below the median of 14.6%.

Credit quality is the main concern: loans 90+ days past due or not accruing interest were 3.2% of loans versus a median of 0.5%, and loans 30-89 days past due were 2.8% of assets versus 0.2%. Net write-offs, loans the bank gave up collecting after recoveries, ran at 7.5% of loans against a median of 0.0%, and provisions for loan losses were 6.5% of assets against 0.1%. Loan-loss reserves were 11.4% of loans versus 1.2%, and the Texas ratio (troubled assets against capital plus reserves) was 12.0% versus 2.9%. The trend section points the other way on direction: these past-due and write-off figures were below their own prior range, so they were high nationally but improving for this bank. The real-estate concentration check found the bank did not cross either line.

On funding, interest expense was 3.3% of assets against a median of 1.6%, brokered deposits (money placed through middlemen) were 9.8% of deposits against 0.0%, and core deposits were 64.1% of assets against 75.5%. Offsetting this, uninsured deposits were only 8.8% of deposits against a median of 24.8%, and cash was 17.8% of assets against 6.2%. Bond losses are small: unrealized losses on bonds available for sale were 0.6% of equity versus a median of 5.6%, and losses on bonds held to maturity were 0.0% versus 0.0%.

## Understanding the score

As of 2026-06-30 the bank ranked 80 out of 4,313 banks, the 98.2nd percentile on a 0 to 100 scale where higher means riskier. That placed it on the watchlist, which covers the top 2% of banks, 87 banks that quarter.

The five factors pushing the score up were loan-loss provisions at 6.5% of assets (+0.625), interest expense at 3.3% of assets (+0.488), securities at only 0.8% of assets (+0.406), loans 30-89 days past due at 2.8% of assets (+0.206), and brokered deposits at 9.8% of deposits (+0.194). The five factors pulling it down were the Tier 1 risk-based capital ratio at 14.2% (-0.967), return on equity, or profit as a share of equity, at 12.7% (-0.544), the leverage ratio at 12.8% (-0.456), the total risk-based capital ratio at 17.7% (-0.447), and the Texas ratio at 12.0% (-0.377).

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

As of 2026-06-30, the bank ranked 80 out of 4,313 banks, placing it in the 98.2nd percentile on a scale where higher means riskier. On 2025-06-30 it sat in the 98.3rd percentile, and the model rated it about the same as a year earlier. Of 30 ratios compared with their own prior range, mostly the prior 12 quarters, 14 were outside that range, and the table shows the 6 furthest outside it.

Interest expense, what the bank pays on its deposits and borrowings, was 3.25% of assets, below its prior range of 3.34% to 3.9%, yet it contributed +0.488 model log-odds units and pushed the score up. Loans 30-89 days past due, meaning borrowers behind on payments but not yet seriously so, were 2.8% of assets, below their prior range of 2.9% to 3.6%, and contributed +0.206 model log-odds units, which pushed the score up.

Core deposits, the steadier everyday deposits a bank relies on, reached 64.1% of assets, above their prior range of 48.8% to 62.3%, but this contributed -0.154 model log-odds units and pushed the score down. Uninsured deposits, money above the deposit insurance limit, were 8.8% of deposits, above their prior range of 4.4% to 8.3%, yet this contributed -0.109 model log-odds units and pushed the score down. Loans 90+ days past due or not accruing interest were 3.2% of loans, below their prior range of 3.4% to 4.5%, and contributed -0.090 model log-odds units, which pushed the score down. Net loan write-offs, loans the bank gave up collecting after recoveries, were 7.5% of loans, below their prior range of 8.4% to 9.5%, but despite sitting outside that range they contributed only -0.010 model log-odds units and had little effect on the score.

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

With hindsight: Canary classes this bank as an open watchlist case, meaning it was flagged and no later outcome is recorded in this fact sheet. The fact sheet contains no data from after the as-of quarter, so it cannot confirm or rule out whether the concerns behind the flag played out. The flag rests on the as-of picture described above: heavy loan-loss provisions and past-due loans, offset in part by strong capital and profits.

## What happened next

With hindsight: this fact sheet includes no ranks, flags or filings from after the as-of quarter. It therefore cannot show how the bank's rank moved later or whether it kept reporting; the score history table added by code shows any later quarters available.

## Sources

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
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: the FDIC specialty group at the as-of quarter · 2026-06-30 · Credit-card Specialization (group 3) · data/raw/specialty/: SPECGRP
