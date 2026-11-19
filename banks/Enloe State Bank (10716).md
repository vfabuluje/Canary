---
cert: 10716
name: "Enloe State Bank"
as_of: 2019-03-31
rank: 1008
n_banks: 5428
percentile: 81.44804716285925
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2019-05-31
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:45:46"
writer_model: "claude-opus-5-5"
checked: true
---

# Enloe State Bank (cert 10716)

*Hindsight: failed 2019-05-31. Canary did not flag it.*

## Summary

Enloe State Bank, a small Texas bank, ranked 1,008 out of 5,428 banks on Canary's risk score as of 2019-03-31, which places it in the 81.4th percentile, where higher means riskier. It was not on the watchlist, which covers the top 2% of banks. Its reported loans showed no serious trouble and its profits were strong, but its capital cushion was thinner than at a typical bank and it lent out nearly all of its deposits.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below typical levels: equity was 9.2% of assets against a national median of 11.2%, and the leverage ratio, core capital as a share of average assets, was 9.2% against 10.9%. Its risk-based capital ratios, which weigh assets by how risky they are, were also well below the median, at 11.0% for Tier 1 against 15.4% and 11.5% in total against 16.6%.

On credit quality, seriously overdue loans or loans no longer paying interest were 0.0% of loans, below the median of 0.6%. However, loans that were recently overdue but not yet seriously late were 0.9% of assets, well above the median of 0.3%, and loan-loss reserves, money set aside for expected bad loans, were only 0.5% of loans against a median of 1.2%.

On funding, loans equaled 98.4% of deposits against a median of 81.2%, and borrowings from the Federal Home Loan Bank, a government-sponsored lender to banks, were 5.4% of assets against 0.2%. Volatile funding, money that can leave quickly, was 9.5% of assets against 6.0%, while cash was 4.7% of assets against 6.8%, and uninsured deposits were low at 4.5% against 18.7%. Unrealized losses on bonds held to maturity were 0.4% of equity against a median of 0.0%, while losses on bonds available for sale were 0.0% against 0.2%.

## Understanding the score

As of 2019-03-31, the bank ranked 1,008 out of 5,428 banks, placing it in the 81.4th percentile on a scale from 0 to 100 where higher means riskier. It was not flagged for the watchlist, which holds the top 2% of banks, or 109 banks that quarter.

The five factors that pushed the score up most were commercial real estate loans at 5.0% of loans (+0.193), the bank's small size of $36.7 million in total assets (+0.188), construction loans at 0.5% of loans (+0.042), uninsured deposits at 4.5% of deposits (+0.037), and securities at 5.4% of assets (+0.035).

The five factors that pushed it down most were a Texas ratio, troubled assets measured against capital plus reserves, of 0.0% (-1.026), a Tier 1 risk-based capital ratio of 11.0% (-0.883), return on equity, profit as a share of owners' money, of 17.6% (-0.693), interest expense at 1.1% of assets (-0.626), and seriously overdue or non-paying loans at 0.0% of loans (-0.473). The downward pushes were much larger than the upward ones.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-06-30 | 1,333 | 5,856 |  |
| 2017-09-30 | 1,556 | 5,806 |  |
| 2017-12-31 | 476 | 5,738 |  |
| 2018-03-31 | 458 | 5,674 |  |
| 2018-06-30 | 783 | 5,610 |  |
| 2018-09-30 | 475 | 5,544 |  |
| 2018-12-31 | 428 | 5,473 |  |
| 2019-03-31 | 1,008 | 5,428 |  |

## How its ratios moved

Of 30 ratios compared with their own history, 6 were outside their prior range, using a window of the prior 12 quarters for most ratios and the same quarter over the prior 3 years for year-to-date ratios. The bank's percentile was 91.9% at 2018-03-31 and the 81.4th percentile at 2019-03-31, meaning the model rated it safer than a year earlier.

The efficiency ratio, operating costs as a share of revenue, was 57.0%, above its prior range of 52.4% to 54.2% and up +2.8 pp, yet its contribution of -0.090 pushed the score down. Return on equity was 17.6%, above its prior range of 15.2% to 17.1%, and its contribution of -0.693 pushed the score down. Interest expense was 1.1% of assets, above its prior range of 0.7% to 1.0%, yet its contribution of -0.626 pushed the score down.

Cash was 4.7% of assets, below its prior range of 5.2% to 10.7% after a -2.9 pp change, yet its contribution of -0.105 pushed the score down. The provision for loan losses, new money set aside for bad loans, was 0.1% of assets, above its prior range of 0.0% to 0.0%, yet its contribution of -0.190 pushed the score down. Securities were 5.4% of assets, just below their prior range of 5.5% to 6.6%, and their contribution of +0.035 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 57.0% | 52.4% to 54.2% | same quarter, prior 3 years | n/a | +2.8 pp | -0.090 | pushed the score down |
| return on equity (profit as a share of equity) | 17.6% | 15.2% to 17.1% | same quarter, prior 3 years | n/a | +2.4 pp | -0.693 | pushed the score down |
| annualized interest expense as a share of assets | 1.1% | 0.7% to 1.0% | same quarter, prior 3 years | n/a | +0.2 pp | -0.626 | pushed the score down |
| cash as a share of assets | 4.7% | 5.2% to 10.7% | prior 12 quarters | -1.0 pp | -2.9 pp | -0.105 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.1% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.1 pp | -0.190 | pushed the score down |
| securities as a share of assets | 5.4% | 5.5% to 6.6% | prior 12 quarters | -0.03 pp | -0.2 pp | +0.035 | little effect on the score |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on 2019-05-31, while the model had ranked it 1,008 and had not placed it on the watchlist. The model learned mostly from credit-loss failures, which were 96% of the 539 failed banks in its training period. This bank's reported figures showed almost none of that pattern: its Texas ratio was 0.0% and its seriously overdue loans were 0.0% of loans, and these, along with strong profits, pulled the score down most. The weaker signs in the data, such as thin capital and high lending against deposits, were not strong enough to outweigh those clean numbers.

## What happened next

In hindsight, the bank's failure date was 2019-05-31. Its last reported quarter was 2019-03-31, so there are no later ranks or watchlist flags for it. Our data shows only that it stopped reporting, which happens when a bank merges or closes; the data does not distinguish between the two.

## Sources

- F1 · Bank name · n/a · Enloe State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-03-31 · 2019-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-03-31 · 1,008 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-03-31 · 5,428 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-03-31 · 81.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-03-31 · 109 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-03-31 · 11.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-03-31 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-03-31 · 11.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-03-31 · 15.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-03-31 · 11.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-03-31 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-03-31 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2019-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2019-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F49 · Bank: loans as a share of deposits · 2019-03-31 · 98.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2019-03-31 · 81.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-03-31 · 4.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-03-31 · 18.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2019-03-31 · 5.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2019-03-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2019-03-31 · 9.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2019-03-31 · 6.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-03-31 · 4.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-03-31 · 6.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-03-31 · 0.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-03-31 · 0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: commercial real estate loans as a share of loans, value 5.0%; contribution to the score · 2019-03-31 · +0.193 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver up #2: total assets, value $36.7 million; contribution to the score · 2019-03-31 · +0.188 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: construction loans as a share of loans, value 0.5%; contribution to the score · 2019-03-31 · +0.042 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver up #4: uninsured deposits as a share of deposits, value 4.5%; contribution to the score · 2019-03-31 · +0.037 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F79 · Driver up #5: securities as a share of assets, value 5.4%; contribution to the score · 2019-03-31 · +0.035 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2019-03-31 · -1.026 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 11.0%; contribution to the score · 2019-03-31 · -0.883 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 17.6%; contribution to the score · 2019-03-31 · -0.693 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2019-03-31 · -0.626 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2019-03-31 · -0.473 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F85 · Failure date · 2019-05-31 · 2019-05-31 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2019-03-31 · 2019-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-03-31 · 57.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 52.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 54.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2019-03-31 · +2.8 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-03-31 · -0.090 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F97 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-03-31 · 17.6% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 17.1% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-03-31 · -0.693 · data/analyst/scores.parquet: feature return_on_equity contribution
- F102 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F103 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2019-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F104 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F105 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F107 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.626 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F108 · Trend: annualized interest expense as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F109 · Trend: cash as a share of assets, value at the as-of quarter · 2019-03-31 · 4.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F110 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 5.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F111 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F113 · Trend: cash as a share of assets, change over four quarters, in percentage points · 2019-03-31 · -2.9 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.105 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F115 · Trend: cash as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-03-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F117 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F118 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F120 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.190 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F121 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F122 · Trend: securities as a share of assets, value at the as-of quarter · 2019-03-31 · 5.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F123 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 5.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F124 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 6.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F127 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · +0.035 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F128 · Trend: securities as a share of assets, what the model did with it · 2019-03-31 · little effect on the score · data/analyst/scores.parquet: feature securities_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2019-03-31 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2019-03-31 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2018-03-31 · 91.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2019-03-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
