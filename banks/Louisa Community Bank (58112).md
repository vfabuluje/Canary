---
cert: 58112
name: "Louisa Community Bank"
as_of: 2019-09-30
rank: 1
n_banks: 5325
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Louisa Community Bank (cert 58112)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

Louisa Community Bank (certificate 58112, based in KY) ranked 1 out of 5,325 banks in Canary's national ranking for the quarter ending 2019-09-30, placing it in the 100.0th percentile on a 0 to 100 scale where higher means riskier. That put it on Canary's watchlist, the top 2% of banks by score, which held 107 banks that quarter. Its cushion of owners' money was very thin, with equity at 3.9% of assets against a national median of 11.6%, while problem loans were far above typical levels. It was also losing money, with a return on assets of -6.4% compared with a national median of 1.1%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below normal: equity was 3.9% of assets versus a national median of 11.6%, and the leverage ratio (core capital as a share of average assets) was 1.2% versus 11.0%. Risk-based capital ratios, which measure capital against assets weighted by how risky they are, were also very low, with the Tier 1 ratio at 1.5% versus a median of 15.6% and the total ratio at 2.8% versus 16.7%.

Credit quality, meaning how well borrowers were repaying, was poor: loans 90+ days past due or not accruing interest were 11.9% of loans versus a national median of 0.6%, and loans 30-89 days past due were 4.8% of assets versus 0.3%. Nonaccrual assets and foreclosed property made up 11.2% of assets versus a median of 0.4%, and the Texas ratio (troubled assets against capital plus reserves) stood at 173.6% versus 3.7%. Losses showed up in earnings, with return on equity at -107.3% versus a median of 9.6% and the efficiency ratio (operating costs as a share of revenue) at 226.9% versus 66.8%.

On funding, brokered deposits (money placed through intermediaries) were 10.2% of deposits versus a national median of 0.0%, and volatile funding was 24.7% of assets versus 6.1%, while deposits shrank by -11.3% over the past four quarters against median growth of 4.4%. Bond losses were not a concern: losses on bonds held to maturity were 0.0% of equity, matching the median of 0.0%, losses on bonds available for sale were 0.5% versus -0.8%, and securities were only 2.4% of assets versus a median of 15.4%.

## Understanding the score

As of 2019-09-30, Louisa Community Bank ranked 1 out of 5,325 banks nationally, the 100.0th percentile, where 100 marks the highest risk. It was flagged on the watchlist, which covers the top 2% of banks and held 107 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 1.5%, return on equity at -107.3%, the Texas ratio at 173.6%, loans 90+ days past due or not accruing interest at 11.9% of loans, and the total risk-based capital ratio at 2.8%. The five features that pulled the score down most were annualized interest expense at 1.4% of assets, construction loans at 4.6% of loans, deposit growth of -11.3% over the past four quarters, total assets of $28.2 million, and uninsured deposits at 11.6% of deposits. These downward pulls were small next to the upward pushes, so the bank stayed at the top of the ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 29 | 5,738 | ▲ watchlist |
| 2018-03-31 | 22 | 5,674 | ▲ watchlist |
| 2018-06-30 | 15 | 5,610 | ▲ watchlist |
| 2018-09-30 | 11 | 5,544 | ▲ watchlist |
| 2018-12-31 | 7 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 4 | 5,428 | ▲ watchlist |
| 2019-06-30 | 1 | 5,369 | ▲ watchlist |
| 2019-09-30 | 1 | 5,325 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2018-12-31, 4 quarters before it failed on 2019-10-25. At that first flag, the top drivers pushing the score up were the Texas ratio at 139.0%, return on equity at -37.9%, and loans 90+ days past due or not accruing interest at 14.9% of loans. The Tier 1 risk-based capital ratio at 8.2% and loans 30-89 days past due at 4.1% of assets also added to the score then.

## What happened next

In hindsight, the bank's last regulatory report was for the quarter ending 2019-09-30, and it failed on 2019-10-25. Because it stopped reporting after that, it does not appear in later rankings.

## Sources

- F1 · Bank name · n/a · Louisa Community Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 58112 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 3.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 1.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 11.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 11.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 173.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -107.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 226.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-09-30 · 10.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2019-09-30 · 24.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2019-09-30 · 6.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 0.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2019-09-30 · 2.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -11.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.5%; contribution to the score · 2019-09-30 · +1.956 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -107.3%; contribution to the score · 2019-09-30 · +1.263 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 173.6%; contribution to the score · 2019-09-30 · +0.995 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 11.9%; contribution to the score · 2019-09-30 · +0.810 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 2.8%; contribution to the score · 2019-09-30 · +0.557 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2019-09-30 · -0.281 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 4.6%; contribution to the score · 2019-09-30 · -0.210 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -11.3%; contribution to the score · 2019-09-30 · -0.099 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: total assets, value $28.2 million; contribution to the score · 2019-09-30 · -0.065 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: uninsured deposits as a share of deposits, value 11.6%; contribution to the score · 2019-09-30 · -0.054 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 139.0%; contribution to the score · 2018-12-31 · +0.936 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -37.9%; contribution to the score · 2018-12-31 · +0.859 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.9%; contribution to the score · 2018-12-31 · +0.767 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F91 · Driver up #4 at 2018-12-31: the Tier 1 risk-based capital ratio, value 8.2%; contribution to the score · 2018-12-31 · +0.543 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F92 · Driver up #5 at 2018-12-31: loans 30-89 days past due, as a share of assets, value 4.1%; contribution to the score · 2018-12-31 · +0.355 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
