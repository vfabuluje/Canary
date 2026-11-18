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
written_at: "2026-11-17T22:05:29"
writer_model: "claude-opus-5-5"
checked: true
---

# Enloe State Bank (cert 10716)

*Hindsight: failed 2019-05-31. Canary did not flag it.*

## Summary

Enloe State Bank, a small Texas bank, ranked 1,008 out of 5,428 banks nationally on Canary's risk score as of 2019-03-31, placing it in the 81.4th percentile on a scale where higher means riskier. It was not flagged on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushions were thinner than the national median and it lent out more of its deposits than most banks, but its reported problem loans were near zero and its profits were strong.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below the national median on every measure: equity was 9.2% of assets versus a median of 11.2%, and the leverage ratio (core capital as a share of average assets) was 9.2% versus 10.9%. Its Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 11.0% versus a median of 15.4%, and its total risk-based capital ratio was 11.5% versus 16.6%.

Credit quality looked clean on serious problems, with loans 90+ days past due or not accruing interest at 0.0% of loans versus a median of 0.6%. However, loans 30-89 days past due, an early sign of trouble, were 0.9% of assets, well above the median of 0.3%, while loan-loss reserves (money set aside for bad loans) were 0.5% of loans versus a median of 1.2%.

On funding, loans equaled 98.4% of deposits versus a median of 81.2%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 5.4% of assets versus a median of 0.2%. Volatile funding, money that can leave quickly, was 9.5% of assets versus a median of 6.0%, and cash was 4.7% of assets versus 6.8%. Unrealized losses on bonds held to maturity were 0.4% of equity versus a median of 0.0%, a small figure, while losses on bonds available for sale were 0.0% versus a median of 0.2%.

## Understanding the score

As of 2019-03-31, Enloe State Bank ranked 1,008 out of 5,428 banks, which is the 81.4th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which held the top 2% of banks, or 109 banks that quarter.

The five features that pushed the score up most were commercial real estate loans at 5.0% of loans (+0.193), total assets of $36.7 million (+0.188), construction loans at 0.5% of loans (+0.042), uninsured deposits at 4.5% of deposits (+0.037), and securities at 5.4% of assets (+0.035).

The five features that pulled the score down most were the Texas ratio (troubled assets against capital plus reserves) at 0.0% (-1.026), the Tier 1 risk-based capital ratio at 11.0% (-0.883), return on equity (profit as a share of equity) at 17.6% (-0.693), interest expense at 1.1% of assets (-0.626), and loans 90+ days past due or not accruing interest at 0.0% of loans (-0.473).

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

## Why the model missed it

In hindsight, the bank failed on 2019-05-31, and its last reported quarter was 2019-03-31, the same quarter this memo describes. The model did not place the bank on its watchlist, so this counts as a miss.

The bank's last reported figures showed almost no troubled loans, strong profits and capital that, while below the median, was not alarmingly low, and those features pulled its score down. Whatever caused the failure did not show up clearly in the reported numbers, and the data cannot tell us what that cause was.

## What happened next

In hindsight, Enloe State Bank failed on 2019-05-31. Its last reported quarter was 2019-03-31, so there are no later ranks or watchlist flags, and the bank no longer reports.

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
