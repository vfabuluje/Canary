---
cert: 30570
name: "Washington Federal Bank For Savings"
as_of: 2017-09-30
rank: 3736
n_banks: 5806
percentile: 35.66999655528763
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2017-12-15
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:46:34"
writer_model: "claude-opus-5-5"
checked: true
---

# Washington Federal Bank For Savings (cert 30570)

*Hindsight: failed 2017-12-15. Canary did not flag it.*

## Summary

As of 2017-09-30, Washington Federal Bank For Savings, an Illinois bank, ranked 3,736 out of 5,806 banks on Canary's national risk ranking, which puts it at the 35.7th percentile on a scale where higher means riskier. It was not on Canary's watchlist, which covers the riskiest 2% of banks. Its reported capital (the owners' cushion against losses) was well above the national median, with a total risk-based capital ratio of 25.5% against a median of 16.3%. It reported no seriously late loans, at 0.0% of loans 90+ days past due or not accruing interest.

## Warning signs in the data

Capital looked strong as of 2017-09-30: equity (the owners' stake) was 12.7% of assets against a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was 12.6% against 10.6%. Its Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 24.7% against a median of 15.1%. Credit quality also looked clean: loans 90+ days past due or not accruing interest were 0.0% against a median of 0.6%, and the Texas ratio (troubled assets against capital plus reserves) was 0.0% against 4.5%. One thinner spot was loan-loss reserves (money set aside for expected bad loans), at 0.4% of loans against a median of 1.2%.

On funding, the bank leaned more on less stable money than most banks: volatile funding (money that can leave quickly) was 15.0% of assets against a median of 5.9%. Loans were 94.5% of deposits against a median of 80.7%, and interest expense was 1.0% of assets against 0.4%, meaning it paid more than typical for its funding. It held cash at 14.1% of assets, well above the median of 6.1%, but securities (bonds) at 0.0% of assets against a median of 17.4%. Losses on bonds were 0.0% of equity for both held-to-maturity and available-for-sale bonds, in line with the national medians of 0.0%.

## Understanding the score

As of 2017-09-30, the bank ranked 3,736 out of 5,806 banks, at the 35.7th percentile on a 0 to 100 scale where higher means riskier. It was not flagged for the watchlist, which holds the riskiest 2% of banks and had 117 banks that quarter.

The five factors that pushed its score up most were securities as a share of assets at 0.0%, adding +0.376, and commercial real estate loans as a share of loans at 6.7%, adding +0.118. Smaller upward pushes came from cash at 14.1% of assets, adding +0.006, Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) at 0.0% of assets, adding +0.004, and loan-loss reserves at 0.4% of loans, adding +0.004.

The five factors that pulled its score down most were the total risk-based capital ratio at 25.5%, contributing -0.919, and the Tier 1 risk-based capital ratio at 24.7%, contributing -0.916. The Texas ratio at 0.0% contributed -0.868, interest expense at 1.0% of assets contributed -0.607, and return on equity (profit as a share of equity) at 11.5% contributed -0.533.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 3,840 | 6,193 |  |
| 2016-06-30 | 4,173 | 6,129 |  |
| 2016-09-30 | 4,396 | 6,051 |  |
| 2016-12-31 | 5,383 | 5,983 |  |
| 2017-03-31 | 5,302 | 5,925 |  |
| 2017-06-30 | 4,039 | 5,856 |  |
| 2017-09-30 | 3,736 | 5,806 |  |

## How its ratios moved

Compared with a year earlier, the model rated the bank riskier than a year earlier, moving from the 27.4th percentile on 2016-09-30 to the 35.7th percentile, with a rank of 3,736. Most ratios were compared with their own values over the prior 12 quarters, and year-to-date ratios with the same quarter over the prior 3 years. Of 30 ratios checked, 15 sat outside their own prior range, and the 6 furthest outside are shown below.

Return on equity was 11.5%, below its prior range of 12.6% to 14.0% and down -1.1 pp over four quarters, yet it pushed the score down with a contribution of -0.533. Return on assets was 1.4%, below its prior range of 1.5% to 1.5%, yet it pushed the score down with a contribution of -0.193. Net interest margin was 4.57%, below its prior range of 4.63% to 4.9%, and it had little effect on the score, contributing -0.047.

Construction loans were 2.9% of loans, above their prior range of 0.4% to 2.2% after a +0.9 pp rise in one quarter, yet they pushed the score down with a contribution of -0.184. Volatile funding was 15.0% of assets, above its prior range of 11.0% to 14.6%, yet it pushed the score down with a contribution of -0.070. The leverage ratio was 12.6%, just above its prior range of 11.2% to 12.5%, and it pushed the score down with a contribution of -0.516.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 11.5% | 12.6% to 14.0% | same quarter, prior 3 years | n/a | -1.1 pp | -0.533 | pushed the score down |
| construction loans as a share of loans | 2.9% | 0.4% to 2.2% | prior 12 quarters | +0.9 pp | +1.0 pp | -0.184 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 12.6% | 11.2% to 12.5% | prior 12 quarters | +0.3 pp | +0.4 pp | -0.516 | pushed the score down |
| volatile funding as a share of assets | 15.0% | 11.0% to 14.6% | prior 12 quarters | +0.4 pp | +1.4 pp | -0.070 | pushed the score down |
| return on assets (profit as a share of assets) | 1.4% | 1.5% to 1.5% | same quarter, prior 3 years | n/a | -0.1 pp | -0.193 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 4.57% | 4.63% to 4.9% | same quarter, prior 3 years | n/a | -0.1 pp | -0.047 | little effect on the score |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on December 15, 2017, and its last report was for the quarter ending September 30, 2017. That means the figures discussed above were the last ones the model ever saw for this bank. Those reported figures showed high capital, no troubled loans and solid profits, so the model ranked the bank in the middle of the pack rather than among the riskiest. A model built only on reported financial data can miss a failure when the cause does not show up in those reported numbers.

## What happened next

In hindsight, the bank's failure date was 2017-12-15. Its last reported quarter was 2017-09-30, so there are no later ranks or watchlist flags for it in our data. After that, the bank stopped reporting; our data does not by itself distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Washington Federal Bank For Savings · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-09-30 · 3,736 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-09-30 · 5,806 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-09-30 · 35.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-09-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-09-30 · 117 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-09-30 · 12.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-09-30 · 24.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-09-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-09-30 · 25.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-09-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-09-30 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2017-09-30 · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2017-09-30 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2017-09-30 · 94.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2017-09-30 · 80.7% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-09-30 · 5.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2017-09-30 · 17.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: securities as a share of assets, value 0.0%; contribution to the score · 2017-09-30 · +0.376 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 6.7%; contribution to the score · 2017-09-30 · +0.118 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: cash as a share of assets, value 14.1%; contribution to the score · 2017-09-30 · +0.006 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F78 · Driver up #4: Federal Home Loan Bank borrowings as a share of assets, value 0.0%; contribution to the score · 2017-09-30 · +0.004 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F79 · Driver up #5: loan-loss reserves as a share of loans, value 0.4%; contribution to the score · 2017-09-30 · +0.004 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F80 · Driver down #1: the total risk-based capital ratio, value 25.5%; contribution to the score · 2017-09-30 · -0.919 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 24.7%; contribution to the score · 2017-09-30 · -0.916 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2017-09-30 · -0.868 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2017-09-30 · -0.607 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 11.5%; contribution to the score · 2017-09-30 · -0.533 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2017-12-15 · 2017-12-15 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2017-09-30 · 11.5% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 12.6% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.0% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2017-09-30 · -1.1 pp · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2017-09-30 · -0.533 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: construction loans as a share of loans, value at the as-of quarter · 2017-09-30 · 2.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F98 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F99 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F100 · Trend: construction loans as a share of loans, change over one quarter, in percentage points · 2017-09-30 · +0.9 pp · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F102 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2017-09-30 · -0.184 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F103 · Trend: construction loans as a share of loans, what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F104 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2017-09-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F105 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 11.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F106 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F109 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2017-09-30 · -0.516 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F110 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F111 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F112 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 11.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F113 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F116 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · -0.070 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F117 · Trend: volatile funding as a share of assets, what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-09-30 · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-09-30 · -0.193 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2017-09-30 · 4.57% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.63% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2017-09-30 · -0.047 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: ratios outside their own prior range · 2017-09-30 · 15 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-09-30 · 6 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2017-09-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2016-09-30 · 27.4% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2017-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
