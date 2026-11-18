---
cert: 91
name: "Allied Bank"
as_of: 2016-06-30
rank: 1
n_banks: 6129
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-09-23
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:05:53"
writer_model: "claude-opus-5-5"
checked: true
---

# Allied Bank (cert 91)

*Hindsight: failed 2016-09-23. Canary flagged it 2 quarters ahead.*

## Summary

As of 2016-06-30, Allied Bank (certificate 91), a bank in AR, ranked 1 out of 6,129 banks on Canary's risk score, which places it at the 100.0th percentile, the riskiest end of the scale. The bank was on Canary's watchlist, and its capital cushion was very thin: equity (the owners' stake) was 2.0% of assets, against a national median of 11.0%. Its loan book was in poor shape, with loans 90+ days past due or not accruing interest at 12.3% of loans, compared with a median of 0.7%. It was also losing money and shrinking, with return on assets of -12.4% and assets down -32.7% over the past four quarters.

## Warning signs in the data

Capital, the buffer that absorbs losses, was far below normal levels. The leverage ratio (core capital as a share of average assets) was 1.8%, against a national median of 10.5%. The Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was 2.7%, against a median of 15.1%, and the total risk-based capital ratio was 4.0%, against a median of 16.3%.

Credit quality was weak on every measure in the data. Nonaccrual assets and foreclosed property, meaning loans no longer paying interest plus property the bank had taken back, equaled 21.4% of assets, against a median of 0.6%. Loans 30-89 days past due were 2.1% of assets, against a median of 0.3%, and annualized loan write-offs (loans given up as lost, net of recoveries) were 14.6% of loans, against a median of 0.0%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 379.7%, far above the national median of 5.3%. These losses fed through to profits: return on equity was -223.2%, against a median of 7.9%, and the efficiency ratio (operating costs as a share of revenue) was 184.8%, against a median of 69.7%.

Funding looked steadier: core deposits, the stable everyday deposits banks rely on, made up 94.4% of assets, above the median of 78.4%, and uninsured deposits were 5.3% of deposits, below the median of 16.6%. Cash was 12.9% of assets, above the median of 6.4%, though deposits had fallen -28.6% over the past four quarters, against median growth of 3.2%. Unrealized losses on bonds available for sale were -4.5% of equity, deeper than the median of -1.6%, while losses on bonds held to maturity were small at -0.2%.

## Understanding the score

On 2016-06-30, Allied Bank ranked 1 of 6,129 banks, at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. Canary's watchlist covers the top 2% of banks by score; 123 banks were on it that quarter, and Allied Bank was flagged.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 2.7%, the Texas ratio at 379.7%, return on equity at -223.2%, the leverage ratio at 1.8%, and the total risk-based capital ratio at 4.0%. The weak Tier 1 capital ratio was the largest single push, contributing +2.117 to the score.

The five features that pulled the score down most were low interest expense at 0.3% of assets, losses on bonds available for sale at -4.5% of equity, construction loans at 6.6% of loans, deposit growth over the past four quarters at -28.6%, and volatile funding (money likely to leave quickly) at 3.2% of assets. The biggest of these, interest expense, subtracted -0.723, far less than the upward pushes added.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 25 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 1 | 6,129 | ▲ watchlist |

## How early Canary caught it

In hindsight, Allied Bank failed on 2016-09-23, and Canary had already flagged it. Its first flag came in the quarter ending 2016-03-31, giving a lead time of 2 quarters before the failure.

At that first flag, the main upward drivers were the Texas ratio at 212.6%, return on equity at -62.0%, and loans 90+ days past due or not accruing interest at 16.5% of loans. Shrinking assets, down -32.5% over the past four quarters, and return on assets of -4.4% also added to the score. At that point the Tier 1 risk-based capital ratio was still 9.4% and was pulling the score down, so the alarm rested mainly on loan problems and losses before capital eroded further.

## What happened next

In hindsight, the bank's last report was for the quarter ending 2016-06-30, the same quarter as this memo's as-of date. It failed on September 23, 2016, so there are no later ranks or flags in our data.

## Sources

- F1 · Bank name · n/a · Allied Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 91 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-06-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-06-30 · 6,129 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-06-30 · 123 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-06-30 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-06-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-06-30 · 2.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-06-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-06-30 · 4.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-06-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 21.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-06-30 · 2.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-06-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 14.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 379.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-06-30 · -12.4% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2016-06-30 · -223.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-06-30 · 7.9% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 184.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-06-30 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-06-30 · 94.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-06-30 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-06-30 · 12.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-06-30 · 6.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-06-30 · -0.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-06-30 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-06-30 · -32.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F73 · Bank: deposit growth over the past four quarters · 2016-06-30 · -28.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-06-30 · 3.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.7%; contribution to the score · 2016-06-30 · +2.117 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 379.7%; contribution to the score · 2016-06-30 · +1.418 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -223.2%; contribution to the score · 2016-06-30 · +1.284 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.8%; contribution to the score · 2016-06-30 · +0.678 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.0%; contribution to the score · 2016-06-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2016-06-30 · -0.723 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -4.5%; contribution to the score · 2016-06-30 · -0.255 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 6.6%; contribution to the score · 2016-06-30 · -0.181 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: deposit growth over the past four quarters, value -28.6%; contribution to the score · 2016-06-30 · -0.126 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 3.2%; contribution to the score · 2016-06-30 · -0.096 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2016-09-23 · 2016-09-23 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 212.6%; contribution to the score · 2016-03-31 · +1.267 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2016-03-31: return on equity (profit as a share of equity), value -62.0%; contribution to the score · 2016-03-31 · +1.089 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 16.5%; contribution to the score · 2016-03-31 · +0.756 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F91 · Driver up #4 at 2016-03-31: asset growth over the past four quarters, value -32.5%; contribution to the score · 2016-03-31 · +0.325 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F92 · Driver up #5 at 2016-03-31: return on assets (profit as a share of assets), value -4.4%; contribution to the score · 2016-03-31 · +0.176 · data/analyst/scores.parquet: feature return_on_assets contribution
- F94 · Driver down #2 at 2016-03-31: the Tier 1 risk-based capital ratio, value 9.4%; contribution to the score · 2016-03-31 · -1.415 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
