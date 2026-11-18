---
cert: 35312
name: "First Cornerstone Bank"
as_of: 2016-03-31
rank: 2
n_banks: 6193
percentile: 99.98385273696108
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-05-06
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# First Cornerstone Bank (cert 35312)

*Hindsight: failed 2016-05-06. Canary flagged it 1 quarter ahead.*

## Summary

As of 2016-03-31, First Cornerstone Bank, a Pennsylvania bank with $103.3 million in total assets, ranked 2 out of 6,193 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile. That put it on Canary's watchlist, the small group of highest-scoring banks. Its capital cushion was very thin, with equity at 2.0% of assets against a national median of 10.9%, and its troubled loans and losses were far above typical levels.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was very low: equity was 2.0% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 2.0% against a median of 10.4%. The Tier 1 risk-based capital ratio, which weighs core capital against how risky the assets are, was 3.9% versus a median of 15.2%, and the total risk-based capital ratio was 5.1% versus 16.4%.

Credit quality was weak: loans 90 or more days past due or no longer accruing interest were 8.1% of loans, well above the national median of 0.7%. Nonaccrual assets and foreclosed property were 7.8% of assets against a median of 0.6%, and loans 30-89 days past due were 5.4% of assets against 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 299.1% against a median of 5.5%, and return on assets (profit as a share of assets) was -4.4% versus a median of 0.9%.

Funding looked steadier: cash was 37.8% of assets against a median of 7.0%, core deposits (stable, everyday deposits) were 96.9% of assets against 78.9%, and uninsured deposits were 9.5% of deposits against 16.6%. Losses on bonds available for sale were small at -0.3% of equity, milder than the median of -0.9%, while total assets shrank -10.0% over the past four quarters against median growth of 3.0%.

## Understanding the score

On 2016-03-31 the bank ranked 2 out of 6,193 banks, which is the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score, or 124 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 3.9% (contribution +2.057), the Texas ratio at 299.1% (+1.339), return on equity at -180.8% (+1.280), the total risk-based capital ratio at 5.1% (+0.446), and loans 90+ days past due or not accruing at 8.1% (+0.438). The five factors pulling the score down most were interest expense at 0.8% of assets (contribution -0.850), commercial real estate loans at 54.9% of loans (-0.399), volatile funding at 0.9% of assets (-0.242), construction loans at 3.0% of loans (-0.156), and losses on bonds available for sale at -0.3% of equity (-0.099).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 2 | 6,193 | ▲ watchlist (first flag) |

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2016-03-31, and the bank failed on 2016-05-06. That gave a lead time of 1 quarter before failure, so this counts as a case the model caught.

## What happened next

In hindsight, the last quarter the bank reported data was 2016-03-31, so there are no later ranks or flags. The bank failed on May 6, 2016, shortly after that final report.

## Sources

- F1 · Bank name · n/a · First Cornerstone Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-03-31 · 6,193 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-03-31 · 124 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-03-31 · 3.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-03-31 · 15.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-03-31 · 5.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-03-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 7.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 299.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-03-31 · 9.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-03-31 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-03-31 · 96.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-03-31 · 78.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-03-31 · 37.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2016-03-31 · $103.3 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2016-03-31 · -10.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-03-31 · 3.0% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.9%; contribution to the score · 2016-03-31 · +2.057 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 299.1%; contribution to the score · 2016-03-31 · +1.339 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -180.8%; contribution to the score · 2016-03-31 · +1.280 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 5.1%; contribution to the score · 2016-03-31 · +0.446 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2016-03-31 · +0.438 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.8%; contribution to the score · 2016-03-31 · -0.850 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: commercial real estate loans as a share of loans, value 54.9%; contribution to the score · 2016-03-31 · -0.399 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 0.9%; contribution to the score · 2016-03-31 · -0.242 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 3.0%; contribution to the score · 2016-03-31 · -0.156 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: losses on bonds available for sale, as a share of equity, value -0.3%; contribution to the score · 2016-03-31 · -0.099 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F85 · Failure date · 2016-05-06 · 2016-05-06 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Last quarter the bank reported · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
