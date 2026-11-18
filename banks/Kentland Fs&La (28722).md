---
cert: 28722
name: "Kentland Fs&La"
as_of: 2026-03-31
rank: 1
n_banks: 4353
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-10
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:22"
writer_model: "claude-opus-5-5"
checked: true
---

# Kentland Fs&La (cert 28722)

*Hindsight: failed 2026-07-10. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

Kentland Fs&La (certificate 28722), a bank in IN, ranked 1 out of 4,353 banks in Canary's national risk ranking for the quarter ending 2026-03-31, which puts it at the 100.0th percentile. It is on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion is very thin, with equity (the owners' stake) at 1.8% of assets against a national median of 10.4%, and it is losing money, with a return on assets of -4.8%. Problem loans are also far above typical levels, with 6.3% of loans seriously overdue or not paying interest against a national median of 0.5%.

## Warning signs in the data

Capital, the cushion that absorbs losses, is the weakest area: equity is 1.8% of assets against a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) is 1.7% against a median of 10.9%. The risk-based capital ratios, which weigh assets by how risky they are, are also far below the typical bank, at 2.9% for Tier 1 against a median of 14.5% and 4.2% in total against a median of 15.7%.

Credit quality is poor: 6.3% of loans are seriously overdue or no longer accruing interest, against a national median of 0.5%, and loans in an earlier stage of delinquency equal 2.5% of assets against a median of 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, is 217.8% against a median of 2.9%, meaning troubled assets far exceed the bank's buffers. Earnings are deeply negative, with return on assets of -4.8% and return on equity of -201.1%, while the efficiency ratio (operating costs as a share of revenue) is 305.0% against a median of 63.1%.

Funding looks steadier: uninsured deposits are only 2.8% of deposits against a national median of 24.4%, brokered deposits are 0.0%, and core deposits make up 88.7% of assets against a median of 75.8%. Bond losses are not a concern here, with losses on bonds available for sale at 0.0% of equity against a median of 5.8%, partly because securities are only 0.4% of assets. The bank is very small, with total assets of $3.7 million against a national median of $381.7 million.

## Understanding the score

For the quarter ending 2026-03-31, the bank ranked 1 of 4,353 banks, placing it at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 88 banks on the list that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 2.9%, return on equity at -201.1%, the Texas ratio at 217.8%, the leverage ratio at 1.7%, and the total risk-based capital ratio at 4.2%.

The five factors pulling the score down, only slightly, were loan-loss reserves (money set aside for bad loans) at 1.0% of loans, cash at 5.5% of assets, brokered deposits at 0.0% of deposits, net loan write-offs at 0.0% of loans, and construction loans at 0.0% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 1 | 4,610 | ▲ watchlist |
| 2024-09-30 | 8 | 4,589 | ▲ watchlist |
| 2024-12-31 | 8 | 4,560 | ▲ watchlist |
| 2025-03-31 | 1 | 4,536 | ▲ watchlist |
| 2025-06-30 | 6 | 4,494 | ▲ watchlist |
| 2025-09-30 | 1 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 1 | 4,411 | ▲ watchlist |
| 2026-03-31 | 1 | 4,353 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2025-09-30, and the bank failed on 2026-07-10, giving a lead time of 4 quarters. This case counts as caught, with the failure arriving after the model's test window.

At that first flag, the main factors pushing the score up were return on equity at -154.3%, the Texas ratio at 130.8%, and the Tier 1 risk-based capital ratio at 7.5%. Problem loans at 7.6% of loans and interest expense at 3.6% of assets also added to the score then.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

Looking back with hindsight, the bank failed on 2026-07-10. Its last reported quarter was 2026-03-31, the same quarter as this memo, so no later ranks are available.

## Sources

- F1 · Bank name · n/a · Kentland Fs&La · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 28722 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 4.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.8% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 305.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 2.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 88.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-03-31 · 0.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F69 · Bank: total assets · 2026-03-31 · $3.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-03-31 · $381.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2026-03-31 · +1.457 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -201.1%; contribution to the score · 2026-03-31 · +1.409 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 217.8%; contribution to the score · 2026-03-31 · +0.921 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.7%; contribution to the score · 2026-03-31 · +0.562 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.2%; contribution to the score · 2026-03-31 · +0.460 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-03-31 · -0.143 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Driver down #2: cash as a share of assets, value 5.5%; contribution to the score · 2026-03-31 · -0.063 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F82 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-03-31 · -0.056 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Driver down #4: annualized loan write-offs, net of recoveries, as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.049 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.032 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2026-07-10 · 2026-07-10 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -154.3%; contribution to the score · 2025-09-30 · +1.328 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: the Texas ratio (troubled assets against capital plus reserves), value 130.8%; contribution to the score · 2025-09-30 · +0.806 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2025-09-30: the Tier 1 risk-based capital ratio, value 7.5%; contribution to the score · 2025-09-30 · +0.573 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2025-09-30: loans 90+ days past due or not accruing interest, as a share of loans, value 7.6%; contribution to the score · 2025-09-30 · +0.396 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2025-09-30: annualized interest expense as a share of assets, value 3.6%; contribution to the score · 2025-09-30 · +0.358 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
