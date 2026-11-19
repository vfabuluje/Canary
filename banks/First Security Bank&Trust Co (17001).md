---
cert: 17001
name: "First Security Bank&Trust Co"
as_of: 2026-06-30
rank: 13
n_banks: 4313
percentile: 99.7217713888245
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:55:28"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank&Trust Co (cert 17001)

*Outcome not yet known.*

## Summary

As of June 30, 2026, First Security Bank&Trust Co, an Oklahoma bank, ranked 13 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.7th percentile, where higher means riskier. That puts it on Canary's watchlist, the top 2% of banks by score, which held 87 banks that quarter. The main concern is troubled loans: 13.2% of its loans were seriously late or no longer paying interest, against a national median of 0.5%.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90 or more days late or not accruing interest (no longer earning interest because repayment is in doubt) were 13.2% of loans, versus a national median of 0.5%. Nonaccrual assets and foreclosed property were 8.0% of assets against a median of 0.3%. Loans in early-stage delinquency, meaning recently late but not yet seriously late, were 1.2% of assets against a median of 0.2%. The Texas ratio, which compares troubled assets with the capital and reserves available to absorb them, stood at 94.7%, far above the median of 2.9%. The bank did hold more loan-loss reserves (money set aside for expected bad loans) than typical, at 2.1% of loans versus 1.2%.

Capital, the owners' cushion against losses, was close to typical: equity was 10.5% of assets versus a median of 10.6%, and the leverage ratio (core capital against average assets) was 10.1% versus 11.0%. Profits were thin, with return on assets of 0.2% against a median of 1.2%.

On funding and liquidity, loans equaled 108.0% of deposits versus a median of 80.2%, and cash was only 0.8% of assets versus 6.2%. The bank leaned more on less stable funding: brokered deposits (money placed through intermediaries) were 8.6% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 9.0% of assets against 0.2%. By contrast, uninsured deposits were low at 4.8% versus 24.8%, and unrealized losses on bonds available for sale were just 0.1% of equity versus a median of 5.6%.

## Understanding the score

The bank ranked 13 of 4,313 banks as of 2026-06-30, the 99.7th percentile on a scale of 0 to 100 where higher means riskier, and it was flagged on the watchlist.

Five factors pushed the score up most. The largest was the share of loans 90 or more days late or not accruing interest, at 13.2%, contributing +1.091. Next came the Texas ratio at 94.7%, contributing +0.912, and interest expense at 3.4% of assets, contributing +0.461. Securities at only 1.1% of assets added +0.232, and commercial real estate loans at 11.8% of loans added +0.207.

Five factors pulled the score down most. The Tier 1 risk-based capital ratio (core capital against risk-weighted assets) contributed -0.717, and the total risk-based capital ratio contributed -0.339. Return on equity at 1.9% contributed -0.453, and construction loans at 13.7% of loans contributed -0.260. Loans in early-stage delinquency, recently late but not yet seriously late, were 1.2% of assets and contributed -0.200.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 416 | 4,589 |  |
| 2024-12-31 | 95 | 4,560 |  |
| 2025-03-31 | 33 | 4,536 | ▲ watchlist |
| 2025-06-30 | 59 | 4,494 | ▲ watchlist |
| 2025-09-30 | 22 | 4,452 | ▲ watchlist |
| 2025-12-31 | 10 | 4,411 | ▲ watchlist |
| 2026-03-31 | 13 | 4,353 | ▲ watchlist |
| 2026-06-30 | 13 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own prior 12 quarters, or for year-to-date ratios with the same quarter in the prior 3 years. Of 28 ratios compared this way, 13 were outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 13 and sat in the 99.7th percentile, up from the 98.7th percentile at 2025-06-30, so the model rated it riskier than a year earlier.

Loans 90 or more days late or not accruing interest reached 13.2% of loans, above a prior range of 0.4% to 8.9%, and contributed +1.091 model log-odds units, which pushed the score up. That share rose +4.3 pp in one quarter and +10.9 pp over four quarters. The Texas ratio reached 94.7%, above a prior range of 1.7% to 68.8%, and contributed +0.912, which pushed the score up. The Texas ratio rose +25.9 pp in one quarter and +76.2 pp over four quarters.

Return on equity fell to 1.9%, below its prior range of 6.3% to 11.4%, yet its contribution of -0.453 pushed the score down. Return on assets dropped to 0.2%, below its prior range of 0.9% to 2.2%, and its contribution of -0.184 also pushed the score down. Net interest margin, the spread earned on lending and investing, was 4.0%, below its prior range of 5.0% to 6.0%, and its contribution of -0.090 pushed the score down. The efficiency ratio rose to 74.6%, above its prior range of 50.6% to 65.1%, but its contribution of +0.005 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| net interest margin (the spread earned on lending and investing) | 4.0% | 5.0% to 6.0% | same quarter, prior 3 years | n/a | -1.5 pp | -0.090 | pushed the score down |
| return on equity (profit as a share of equity) | 1.9% | 6.3% to 11.4% | same quarter, prior 3 years | n/a | -6.0 pp | -0.453 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 74.6% | 50.6% to 65.1% | same quarter, prior 3 years | n/a | +24.0 pp | +0.005 | little effect on the score |
| return on assets (profit as a share of assets) | 0.2% | 0.9% to 2.2% | same quarter, prior 3 years | n/a | -0.7 pp | -0.184 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 13.2% | 0.4% to 8.9% | prior 12 quarters | +4.3 pp | +10.9 pp | +1.091 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 94.7% | 1.7% to 68.8% | prior 12 quarters | +25.9 pp | +76.2 pp | +0.912 | pushed the score up |

13 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank is an open watchlist case: it was flagged by the model and the fact sheet records no failure. The fact sheet contains no data from after the as-of quarter, so there is no hindsight evidence here to explain the outcome further.

## What happened next

In hindsight, the fact sheet provides no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. Without that later data, this memo cannot say whether the bank stayed on the watchlist or whether it is still filing reports.

## Sources

- F1 · Bank name · n/a · First Security Bank&Trust Co · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 13 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 108.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 13.2%; contribution to the score · 2026-06-30 · +1.091 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 94.7%; contribution to the score · 2026-06-30 · +0.912 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized interest expense as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · +0.461 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F74 · Driver up #4: securities as a share of assets, value 1.1%; contribution to the score · 2026-06-30 · +0.232 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 11.8%; contribution to the score · 2026-06-30 · +0.207 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.717 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 1.9%; contribution to the score · 2026-06-30 · -0.453 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: the total risk-based capital ratio; contribution to the score · 2026-06-30 · -0.339 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver down #4: construction loans as a share of loans, value 13.7%; contribution to the score · 2026-06-30 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #5: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · -0.200 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F81 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F82 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F83 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F85 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.090 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F86 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F87 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.453 · data/analyst/scores.parquet: feature return_on_equity contribution
- F92 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 74.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 50.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 65.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.005 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F100 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.184 · data/analyst/scores.parquet: feature return_on_assets contribution
- F104 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F106 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F107 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F108 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over one quarter, in percentage points · 2026-06-30 · +4.3 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F109 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +10.9 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F110 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +1.091 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 68.8% · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +25.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +76.2 pp · data/features/fct_bank_features.parquet: texas_ratio
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.912 · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F119 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F120 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F122 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F123 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F124 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.7% · data/analyst/scores.parquet: percentile
- F125 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
