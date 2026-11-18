---
cert: 15426
name: "Almena State Bank"
as_of: 2020-09-30
rank: 1
n_banks: 5098
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-23
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Almena State Bank (cert 15426)

*Hindsight: failed 2020-10-23. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, Almena State Bank (certificate 15426, in KS) ranked 1 out of 5,098 banks on Canary's risk score, the highest-scoring bank in the country that quarter. That puts it at the 100.0th percentile, where higher means riskier, and it was flagged on Canary's watchlist. The data show a bank with almost no capital cushion, a large share of troubled loans and deep losses compared with typical US banks.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was nearly gone: equity as a share of assets was 0.0% against a national median of 10.9%. The leverage ratio (core capital as a share of average assets) was 0.0% versus a median of 10.2%, and the Tier 1 risk-based capital ratio was 0.0% versus 14.7%. The total risk-based capital ratio was 1.4%, far below the median of 15.9%.

Credit quality was very weak: loans 90+ days past due or not accruing interest made up 23.8% of loans, against a median of 0.5%. Nonaccrual assets and foreclosed property were 19.4% of assets versus a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) stood at 243.0% versus 3.4%. The bank was losing money, with a return on assets of -7.3% compared with a median of 1.0%.

On funding, brokered deposits (money placed through middlemen rather than local customers) were 31.4% of deposits, well above the median of 0.0%. Losses on bonds available for sale equaled -34.5% of equity, much deeper than the median of -2.5%. The bank was also shrinking, with assets changing by -23.7% over the past four quarters while the median bank grew 14.0%.

## Understanding the score

As of 2020-09-30, Almena State Bank ranked 1 of 5,098 banks, placing it at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 102 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 0.0%, return on equity (profit as a share of the owners' stake) at -233.5%, the Texas ratio at 243.0%, loans 90+ days past due or not accruing interest at 23.8% of loans, and the total risk-based capital ratio at 1.4%.

The five factors pulling the score down most were losses on bonds available for sale at -34.5% of equity, deposit growth at -15.7%, construction loans at 0.0% of loans, loans 30-89 days past due at 1.2% of assets, and volatile funding (money that can leave quickly) at 2.0% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 15 | 5,473 | ▲ watchlist |
| 2019-03-31 | 7 | 5,428 | ▲ watchlist |
| 2019-06-30 | 5 | 5,369 | ▲ watchlist |
| 2019-09-30 | 6 | 5,325 | ▲ watchlist |
| 2019-12-31 | 5 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 6 | 5,182 | ▲ watchlist |
| 2020-06-30 | 1 | 5,131 | ▲ watchlist |
| 2020-09-30 | 1 | 5,098 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Almena State Bank in the quarter ending 2019-12-31, a lead time of 4 quarters before the bank failed on 2020-10-23. At that first flag, the top factors raising the score were return on equity at -100.1%, the Texas ratio at 189.3%, and the Tier 1 risk-based capital ratio at 5.9%. Loans 90+ days past due or not accruing interest were already 22.9% of loans, and brokered deposits were 26.3% of deposits.

## What happened next

In hindsight, the last quarter Almena State Bank reported data was 2020-09-30, the same quarter as this memo. The bank failed on 2020-10-23, so no later ranks or flags exist after the as-of quarter.

## Sources

- F1 · Bank name · n/a · Almena State Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 15426 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-09-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 23.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 19.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 243.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-09-30 · -7.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-09-30 · 31.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2020-09-30 · -23.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2020-09-30 · 14.0% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2020-09-30 · +1.798 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -233.5%; contribution to the score · 2020-09-30 · +1.440 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 243.0%; contribution to the score · 2020-09-30 · +1.035 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 23.8%; contribution to the score · 2020-09-30 · +0.654 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.4%; contribution to the score · 2020-09-30 · +0.552 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -34.5%; contribution to the score · 2020-09-30 · -0.250 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.7%; contribution to the score · 2020-09-30 · -0.140 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.0%; contribution to the score · 2020-09-30 · -0.100 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2020-09-30 · -0.090 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 2.0%; contribution to the score · 2020-09-30 · -0.078 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-10-23 · 2020-10-23 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: return on equity (profit as a share of equity), value -100.1%; contribution to the score · 2019-12-31 · +1.351 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 189.3%; contribution to the score · 2019-12-31 · +0.934 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2019-12-31: the Tier 1 risk-based capital ratio, value 5.9%; contribution to the score · 2019-12-31 · +0.860 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2019-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 22.9%; contribution to the score · 2019-12-31 · +0.751 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-12-31: brokered deposits as a share of deposits, value 26.3%; contribution to the score · 2019-12-31 · +0.269 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
