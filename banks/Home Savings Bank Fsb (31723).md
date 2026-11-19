---
cert: 31723
name: "Home Savings Bank Fsb"
as_of: 2026-06-30
rank: 18
n_banks: 4313
percentile: 99.6058428008347
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:37"
writer_model: "claude-opus-5-5"
checked: true
---

# Home Savings Bank Fsb (cert 31723)

*Outcome not yet known.*

## Summary

Home Savings Bank Fsb, a small Kentucky bank, ranked 18 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, which places it in the 99.6th percentile. That puts it on the watchlist, the 2% of banks with the highest scores. Its troubled loans stand out: 7.5% of its loans were 90+ days past due or no longer collecting interest, against a national median of 0.5%. It was also losing money, with a return on assets (profit as a share of assets) of -1.3% versus a median of 1.2%.

## Warning signs in the data

Credit quality is the clearest weak spot. Loans 90+ days past due or not accruing interest were 7.5% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 5.8% of assets, against a median of 0.3%. Loans 30-89 days past due, an earlier stage of trouble, were 0.9% of assets versus a median of 0.2%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 48.8%, far above the median of 2.9%. Loan-loss reserves, money set aside for expected bad loans, were 0.8% of loans, below the median of 1.2%.

Capital, the cushion that absorbs losses, looks roughly normal: equity was 11.3% of assets against a median of 10.6%, while the leverage ratio (core capital as a share of average assets) was 10.2%, a little below the median of 11.0%. Earnings are weak: return on equity was -11.4% versus a median of 11.6%, and the net interest margin (the spread earned on lending) was 2.6% versus 3.9%. The efficiency ratio, operating costs as a share of revenue, was 147.6%, well above the median of 62.1%, meaning costs exceeded revenue.

On funding, loans were 99.6% of deposits against a median of 80.2%, and Federal Home Loan Bank borrowings were 9.8% of assets versus a median of 0.2%. On the steadier side, uninsured deposits were only 2.0% of deposits versus a median of 24.8%, and cash was 19.2% of assets versus 6.2%. Bond losses are not a concern here: the bank held securities equal to 0.0% of assets, against a median of 17.6%, and showed 0.0% losses on bonds available for sale versus a median of 5.6% of equity. The bank is very small, with total assets of $25.7 million compared with a median of $384.7 million.

## Understanding the score

As of 2026-06-30 the bank ranked 18 of 4,313 banks, in the 99.6th percentile on a scale where higher means riskier. It was flagged for the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

Five features pushed the score up most. Loans 90+ days past due or not accruing interest, at 7.5%, added +0.914. The Texas ratio, at 48.8%, added +0.840. Securities as a share of assets, at 0.0%, added +0.365. Interest expense as a share of assets, at 2.4%, added +0.278. Commercial real estate loans as a share of loans, at 7.8%, added +0.248.

Five features pulled the score down most. The Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets, contributed -0.883. Construction loans as a share of loans, at 3.6%, contributed -0.463. The leverage ratio, at 10.2%, contributed -0.297. Return on equity, at -11.4%, contributed -0.248. Loan-loss reserves as a share of loans, at 0.8%, contributed -0.225.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 525 | 4,589 |  |
| 2024-12-31 | 511 | 4,560 |  |
| 2025-03-31 | 828 | 4,536 |  |
| 2025-06-30 | 404 | 4,494 |  |
| 2025-09-30 | 16 | 4,452 | ▲ watchlist |
| 2025-12-31 | 20 | 4,411 | ▲ watchlist |
| 2026-03-31 | 26 | 4,353 | ▲ watchlist |
| 2026-06-30 | 18 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios compared, 13 sat outside their own prior range, and the 6 furthest outside are shown in the table. The bank ranked 18 of 4,313 at 2026-06-30, up from the 91.0% percentile mark a year earlier, and the model rated it riskier than a year earlier.

Federal Home Loan Bank borrowings were 9.8% of assets, below their prior range of 15.0% to 21.0% after a -9.2 pp change over four quarters, yet this had little effect on the score, contributing -0.014 model log-odds units. Core deposits, stable everyday customer deposits, were 72.5% of assets, above their prior range of 62.5% to 68.7%, but this had little effect on the score, contributing -0.050 model log-odds units. The efficiency ratio reached 147.6%, above its prior range of 99.3% to 136.5%, yet it had little effect on the score, contributing -0.013 model log-odds units.

Return on equity fell to -11.4%, below its prior range of -8.5% to 0.1%, yet it pushed the score down, contributing -0.248 model log-odds units. Return on assets fell to -1.3%, below its prior range of -1.0% to 0.0%, yet it pushed the score down, contributing -0.126 model log-odds units. The leverage ratio slipped to 10.2%, below its prior range of 10.5% to 12.8%, yet it pushed the score down, contributing -0.297 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| Federal Home Loan Bank borrowings as a share of assets | 9.8% | 15.0% to 21.0% | prior 12 quarters | -5.2 pp | -9.2 pp | -0.014 | little effect on the score |
| core deposits as a share of assets | 72.5% | 62.5% to 68.7% | prior 12 quarters | +3.7 pp | +5.2 pp | -0.050 | little effect on the score |
| return on equity (profit as a share of equity) | -11.4% | -8.5% to 0.1% | same quarter, prior 3 years | n/a | -2.9 pp | -0.248 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 147.6% | 99.3% to 136.5% | same quarter, prior 3 years | n/a | +11.1 pp | -0.013 | little effect on the score |
| return on assets (profit as a share of assets) | -1.3% | -1.0% to 0.0% | same quarter, prior 3 years | n/a | -0.3 pp | -0.126 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 10.2% | 10.5% to 12.8% | prior 12 quarters | -0.3 pp | -0.5 pp | -0.297 | pushed the score down |

13 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

This section is written with hindsight. Canary records this bank's case as one that remains open and on the watchlist, but the fact sheet contains no later data describing why or how its situation developed. Without such facts, no further explanation can be given here.

## What happened next

This section is written with hindsight. The fact sheet provides no ranks, watchlist flags or reporting status for quarters after the as-of quarter, so later developments cannot be described from this data. The score history table added below shows whatever later readings are available.

## Sources

- F1 · Bank name · n/a · Home Savings Bank Fsb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 18 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 48.8% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F38 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F39 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F40 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 99.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F65 · Bank: total assets · 2026-06-30 · $25.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F66 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 7.5%; contribution to the score · 2026-06-30 · +0.914 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 48.8%; contribution to the score · 2026-06-30 · +0.840 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: securities as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · +0.365 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.278 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 7.8%; contribution to the score · 2026-06-30 · +0.248 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.883 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 3.6%; contribution to the score · 2026-06-30 · -0.463 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.297 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver down #4: return on equity (profit as a share of equity), value -11.4%; contribution to the score · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value 0.8%; contribution to the score · 2026-06-30 · -0.225 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F82 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 15.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F83 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 21.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F85 · Trend: Federal Home Loan Bank borrowings as a share of assets, change over four quarters, in percentage points · 2026-06-30 · -9.2 pp · data/features/fct_bank_features.parquet: fhlb_to_assets
- F86 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.014 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F87 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F88 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 72.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F89 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 62.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F90 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 68.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F93 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.050 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F94 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -8.5% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 99.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 136.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.013 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.126 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F114 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F115 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.297 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F119 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F120 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F122 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F123 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F125 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 91.0% · data/analyst/scores.parquet: percentile
- F126 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
