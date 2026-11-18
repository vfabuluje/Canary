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
written_at: "2026-11-17T22:05:53"
writer_model: "claude-opus-5-5"
checked: true
---

# Washington Federal Bank For Savings (cert 30570)

*Hindsight: failed 2017-12-15. Canary did not flag it.*

## Summary

As of 2017-09-30, Washington Federal Bank For Savings, an Illinois savings bank, ranked 3,736 out of 5,806 banks nationally on Canary's risk score, placing it in the 35.7th percentile. It was not flagged on the watchlist, which covers the riskiest 2% of banks. Its reported capital cushion was well above the national median, and it reported no seriously late or non-paying loans.

## Warning signs in the data

Capital, the owners' money that absorbs losses, looked strong: equity was 12.7% of assets against a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was 12.6% against 10.6%. The total risk-based capital ratio, which weighs assets by riskiness, was 25.5% compared with a median of 16.3%. Credit quality also looked clean, with loans 90+ days past due or not accruing interest at 0.0% of loans versus a median of 0.6%, and the Texas ratio (troubled assets against capital plus reserves) at 0.0% versus 4.5%. One soft spot was loan-loss reserves, money set aside for expected bad loans, at 0.4% of loans, well below the median of 1.2%.

On funding, loans were 94.5% of deposits, above the median of 80.7%, and volatile funding, money that can leave quickly, was 15.0% of assets against a median of 5.9%. Interest expense was 1.0% of assets, more than the median of 0.4%, suggesting the bank paid relatively high rates for its money. On the other hand, uninsured deposits were only 10.6% of deposits versus a median of 17.8%, and cash was 14.1% of assets versus 6.1%.

The bank held no bonds: securities were 0.0% of assets against a median of 17.4%, so losses on bonds available for sale were 0.0% of equity, matching the median of 0.0%.

## Understanding the score

For Q3 2017 the bank ranked 3,736 of 5,806 banks, in the 35.7th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged; the watchlist held 117 banks that quarter.

The five features pushing the score up were holding no securities (0.0% of assets, +0.376), commercial real estate loans at 6.7% of loans (+0.118), cash at 14.1% of assets (+0.006), no Federal Home Loan Bank borrowings, a common wholesale funding source (0.0% of assets, +0.004), and loan-loss reserves at 0.4% of loans (+0.004).

The five features pulling it down were the total risk-based capital ratio of 25.5% (-0.919), the Tier 1 risk-based capital ratio of 24.7% (-0.916), a Texas ratio of 0.0% (-0.868), interest expense at 1.0% of assets (-0.607), and return on equity, profit as a share of equity, of 11.5% (-0.533).

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

## Why the model missed it

In hindsight, the bank failed on 2017-12-15, and the model did not flag it beforehand. Its last report was for 2017-09-30, the same quarter scored here, so the model had no later filings to react to. The reported figures showed strong capital, profits and almost no troubled loans, so whatever led to the failure did not appear in the numbers the model could read.

## What happened next

With hindsight, the bank failed on 2017-12-15. It stopped reporting after 2017-09-30, so there are no later ranks or watchlist flags for it.

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
- F51 · Bank: uninsured deposits as a share of deposits · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-09-30 · 17.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-09-30 · 5.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
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
