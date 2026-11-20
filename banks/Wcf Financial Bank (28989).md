---
cert: 28989
name: "Wcf Financial Bank"
as_of: 2026-06-30
rank: 16
n_banks: 4313
percentile: 99.6522142360306
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Wcf Financial Bank (cert 28989)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Wcf Financial Bank, an Iowa bank, ranked 16 out of 4,313 banks nationally on Canary's risk score, placing it in the 99.7th percentile, where higher means riskier. It was flagged on Canary's watchlist, which covers the top 2% of banks by score. The main concerns are a large share of troubled loans, capital ratios below the national median, and heavy use of funding sources that can be costly or leave quickly. Its lending tied to commercial real estate was low and did not cross either regulatory screen line, so the concerns sit with loan quality and funding rather than property concentration.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than at a typical bank: equity was 7.9% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.3% against 11.0%. The Tier 1 risk-based capital ratio was 11.5% against a median of 14.6%, and the total risk-based capital ratio was 12.7% against 15.8%.

Credit quality was the sharpest weak spot: loans 90+ days past due or not accruing interest were 5.1% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 4.0% of assets against a median of 0.3%, and loans 30-89 days past due were 3.0% of assets against 0.2%. The Texas ratio, which sets troubled assets against capital plus reserves, was 45.9%, versus a national median of 2.9%, while loan-loss reserves were 1.1% of loans, close to the median of 1.2%. Profitability was weak, with return on assets of 0.1% against a median of 1.2%.

On funding, brokered deposits (money placed through outside middlemen) were 15.2% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 13.4% of assets against 0.2%. Volatile funding was 30.6% of assets against a median of 9.0%, core deposits (stable everyday deposits) were 48.4% of assets against 75.5%, and loans were 100.3% of deposits against 80.2%. Unrealized losses on bonds available for sale were 6.9% of equity, somewhat above the median of 5.6%, while commercial real estate loans were only 4.8% of loans against a median of 23.6%, a point in the bank's favor.

## Understanding the score

As of 2026-06-30, the bank ranked 16 out of 4,313 banks, in the 99.7th percentile, and was one of 87 banks flagged on the watchlist that quarter.

The five features that pushed the score up most were the Texas ratio at 45.9%, losses on bonds available for sale at 6.9% of equity, loans 30-89 days past due at 3.0% of assets, brokered deposits at 15.2% of deposits, and interest expense at 2.7% of assets. The largest of these, the Texas ratio, added +0.781 to the score.

The five features that pushed the score down most were the Tier 1 risk-based capital ratio at 11.5%, the total risk-based capital ratio at 12.7%, the efficiency ratio at 95.3%, return on equity at 1.3%, and construction loans at 5.9% of loans. The Tier 1 ratio had the biggest downward effect at -1.448, even though it sits below the national median, which shows how the model weighs these figures in combination rather than one by one.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,377 | 4,589 |  |
| 2024-12-31 | 1,386 | 4,560 |  |
| 2025-03-31 | 799 | 4,536 |  |
| 2025-06-30 | 678 | 4,494 |  |
| 2025-09-30 | 128 | 4,452 |  |
| 2025-12-31 | 18 | 4,411 | ▲ watchlist |
| 2026-03-31 | 12 | 4,353 | ▲ watchlist |
| 2026-06-30 | 16 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Wcf Financial Bank ranked 16 out of 4,313 banks nationally, placing it in the 99.7th percentile, where a higher percentile means riskier. A year earlier, on 2025-06-30, it sat in the 84.9th percentile, so the model rated it riskier than a year earlier. Canary compares each ratio with that ratio's own history over the prior 12 quarters, and 4 of the 30 ratios checked were outside that prior range.

Brokered deposits are money placed with the bank through outside middlemen rather than directly by customers. They made up 15.2% of deposits, above their prior range of 0.0% to 14.0%, and this pushed the score up, adding +0.423 model log-odds units (positive values raise the score). That share rose +15.2 pp over four quarters, including +1.2 pp in the latest quarter.

Cash was 4.8% of assets, above its prior range of 1.1% to 4.5%, yet this pushed the score down, at -0.073 model log-odds units. Loan-loss reserves, money set aside to cover expected bad loans, were 1.14% of loans, just above their prior range of 0.7% to 1.13%, and this also pushed the score down, at -0.237 model log-odds units. Securities, such as bonds the bank holds, were 10.1% of assets, below their prior range of 10.4% to 13.4%, and this pushed the score down, at -0.053 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| cash as a share of assets | 4.8% | 1.1% to 4.5% | prior 12 quarters | +2.4 pp | +0.3 pp | -0.073 | pushed the score down |
| securities as a share of assets | 10.1% | 10.4% to 13.4% | prior 12 quarters | -0.3 pp | -1.8 pp | -0.053 | pushed the score down |
| brokered deposits as a share of deposits | 15.2% | 0.0% to 14.0% | prior 12 quarters | +1.2 pp | +15.2 pp | +0.423 | pushed the score up |
| loan-loss reserves as a share of loans | 1.14% | 0.7% to 1.13% | prior 12 quarters | +0.01 pp | +0.4 pp | -0.237 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 642 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2026-06-30, Wcf Financial Bank ranked 16 out of 4,313 banks nationally, which places it at the 99.7th percentile on a scale where higher means a higher score. Its Texas ratio (troubled assets set against capital plus reserves) was 45.9%, at the 99.3rd percentile nationally, which is unusually high, and at the 99.3rd percentile among its peers against a peer median of 2.5%, unusually high among its peers too. Volatile funding (money that can leave the bank quickly) made up 30.6% of assets, at the 99.0th percentile nationally, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 10.1%, unusually high among its peers too.

Loans 30-89 days past due equaled 3.0% of assets, at the 98.7th percentile nationally, which is unusually high, and at the 99.0th percentile among its peers against a peer median of 0.2%, unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) and foreclosed property equaled 4.0% of assets, at the 98.7th percentile nationally, which is unusually high, and at the 99.1st percentile among its peers against a peer median of 0.2%, unusually high among its peers too. Loans 90+ days past due or not accruing interest were 5.1% of loans, at the 97.7th percentile nationally, which is unusually high, and at the 98.1st percentile among its peers against a peer median of 0.4%, unusually high among its peers too.

Federal Home Loan Bank borrowings (loans the bank took from this lender to banks) were 13.4% of assets, at the 96.8th percentile nationally, which is unusually high, and at the 97.6th percentile among its peers against a peer median of 0.7%, unusually high among its peers too. The efficiency ratio (operating costs as a share of revenue) was 95.3%, at the 95.8th percentile nationally, which is unusually high, and at the 99.6th percentile among its peers against a peer median of 56.9%, unusually high among its peers too. Annualized interest expense was 2.7% of assets, at the 95.7th percentile nationally, which is unusually high, and at the 99.0th percentile among its peers against a peer median of 1.6%, unusually high among its peers too. Overall, 15 of the bank's ratios fall in the national top or bottom 10%, and 14 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 45.9% | 99.3rd (unusually high) | 2.5% | 99.3rd | unusually high among its peers too |
| volatile funding as a share of assets | 30.6% | 99.0th (unusually high) | 10.1% | 99.5th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 3.0% | 98.7th (unusually high) | 0.2% | 99.0th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 4.0% | 98.7th (unusually high) | 0.2% | 99.1st | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 5.1% | 97.7th (unusually high) | 0.4% | 98.1st | unusually high among its peers too |
| Federal Home Loan Bank borrowings as a share of assets | 13.4% | 96.8th (unusually high) | 0.7% | 97.6th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 95.3% | 95.8th (unusually high) | 56.9% | 99.6th | unusually high among its peers too |
| annualized interest expense as a share of assets | 2.7% | 95.7th (unusually high) | 1.6% | 99.0th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 50.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 78.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 10.1% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is listed as an open watchlist case, meaning it was flagged and our data do not record a failure for it. The fact sheet contains no data from after the as-of quarter, so this note cannot say whether the warning signs eased or worsened.

## What happened next

In hindsight: no later ranks, flags or filings for this bank are included in the fact sheet. Because of that, this note cannot say whether the bank kept reporting or how its score moved after the as-of quarter.

## Sources

- F1 · Bank name · n/a · Wcf Financial Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 16 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 45.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 100.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 15.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 30.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 45.9%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.9%; contribution to the score · 2026-06-30 · +0.641 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: loans 30-89 days past due, as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.481 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 15.2%; contribution to the score · 2026-06-30 · +0.423 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.387 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.5%; contribution to the score · 2026-06-30 · -1.448 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 12.7%; contribution to the score · 2026-06-30 · -0.371 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 95.3%; contribution to the score · 2026-06-30 · -0.303 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 1.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.271 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F86 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F87 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F90 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.073 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F91 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F92 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F93 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 10.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F94 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F97 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.053 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F98 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F99 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 15.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F100 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F101 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 14.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F102 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +1.2 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F103 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +15.2 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F104 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.423 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F105 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F106 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 1.14% · data/features/fct_bank_features.parquet: allowance_to_loans
- F107 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F108 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.13% · data/features/fct_bank_features.parquet: allowance_to_loans
- F111 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.237 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F112 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F113 · Trend: ratios outside their own prior range · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F115 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F116 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F118 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 84.9% · data/analyst/scores.parquet: percentile
- F119 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F123 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 45.9% · data/features/fct_bank_features.parquet: texas_ratio
- F124 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: texas_ratio
- F125 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: texas_ratio
- F127 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F128 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F129 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 30.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F130 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F131 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F132 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F133 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F134 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F135 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F136 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F137 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F138 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F139 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F140 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F150 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F154 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F155 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F156 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F157 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F158 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F159 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 95.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F160 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 95.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F161 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F162 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: efficiency_ratio
- F163 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 56.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F164 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F165 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F166 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F167 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F168 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F169 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F170 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F172 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F173 · Peers: those ratios also unusual among peers · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F175 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
