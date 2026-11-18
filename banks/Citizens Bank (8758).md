---
cert: 8758
name: "Citizens Bank"
as_of: 2023-09-30
rank: 1
n_banks: 4686
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2023-11-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Citizens Bank (cert 8758)

*Hindsight: failed 2023-11-03. Canary flagged it 2 quarters ahead.*

## Summary

As of 2023-09-30, Citizens Bank (cert 8758) in IA ranked 1 out of 4,686 banks nationally on Canary's risk score, placing it at the 100.0th percentile. It was flagged on Canary's watchlist, which covers the top 2% of banks by score. The bank's capital (the owners' cushion that absorbs losses) had fallen below zero, with equity at -4.5% of assets against a national median of 9.1%. Bad loans and heavy losses were also far above typical levels for a small bank of $65.6 million in assets.

## Warning signs in the data

Capital was the most striking problem: equity stood at -4.5% of assets versus a national median of 9.1%, and the leverage ratio (core capital as a share of average assets) was 0.0% versus 10.6%. Regulatory capital measures that weigh assets by riskiness were similarly depleted, with the Tier 1 risk-based capital ratio at 0.0% against a median of 14.2% and the total risk-based capital ratio at 1.3% against 15.4%.

Credit quality was poor: loans 90+ days past due or not accruing interest were 9.6% of loans, far above the national median of 0.3%, and nonaccrual assets plus foreclosed property were 5.9% of assets versus 0.1%. Annualized loan write-offs (loans written off as uncollectable, net of recoveries) reached 15.1% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 9.8% of assets against 0.0%. These losses drove return on assets to -10.0%, well below the national median of 1.0%.

On funding, uninsured deposits (balances above the deposit insurance limit) were 34.5% of deposits versus a median of 23.6%, volatile funding was 20.9% of assets versus 8.3%, and cash was 2.6% of assets versus 5.4%. Deposits shrank by -9.2% over the past four quarters, a steeper decline than the national median of -0.6%. Losses on bonds available for sale read -105.6% of equity against a median of 19.9%, a figure that is hard to interpret because the bank's equity was below zero.

## Understanding the score

Citizens Bank ranked 1 out of 4,686 banks on 2023-09-30, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score and contained 94 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 0.0%, return on equity (profit as a share of equity) at -596.8%, the total risk-based capital ratio at 1.3%, the leverage ratio at 0.0%, and equity as a share of assets at -4.5%. In short, the model's view was driven mainly by the near-total loss of capital and deep losses.

The five features that pulled the score down most were the Texas ratio (troubled assets against capital plus reserves) at -261.2%, securities as a share of assets at 38.2%, losses on bonds available for sale at -105.6% of equity, annualized interest expense at 1.1% of assets, and deposit growth over the past four quarters at -9.2%. The Texas ratio and bond-loss readings are negative because the bank's equity was below zero, so they offered limited reassurance despite lowering the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-12-31 | 297 | 4,904 |  |
| 2022-03-31 | 20 | 4,861 | ▲ watchlist |
| 2022-06-30 | 586 | 4,838 |  |
| 2022-09-30 | 261 | 4,813 |  |
| 2022-12-31 | 515 | 4,773 |  |
| 2023-03-31 | 303 | 4,740 |  |
| 2023-06-30 | 33 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 1 | 4,686 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Citizens Bank in the quarter ending 2023-06-30, and the bank failed on 2023-11-03, a lead time of 2 quarters. At that first flag, the top drivers pushing the score up were losses on bonds available for sale at 119.8% of equity, the Texas ratio at 143.5%, and loans 90+ days past due or not accruing at 9.7% of loans.

At that point capital still looked adequate on paper, with the Tier 1 risk-based capital ratio at 10.4% and the total risk-based capital ratio at 11.6%, both of which pulled the score down. The model flagged the bank based on bad loans and bond losses before its capital measures collapsed in the following quarter.

## What happened next

In hindsight, Citizens Bank failed on 2023-11-03. The last quarter it reported financial data was 2023-09-30, the same quarter as this memo, so no later ranks or flags exist. Canary's data records only that the bank stopped reporting, which on its own does not distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Citizens Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 8758 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-09-30 · 4,686 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-09-30 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-09-30 · -4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-09-30 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-09-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-09-30 · 1.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-09-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 9.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-09-30 · -10.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-09-30 · 34.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-09-30 · 20.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-09-30 · 8.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-09-30 · 2.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-09-30 · 5.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-09-30 · -105.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-09-30 · 19.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2023-09-30 · $65.6 million · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2023-09-30 · -9.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-09-30 · -0.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2023-09-30 · +2.465 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -596.8%; contribution to the score · 2023-09-30 · +2.131 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 1.3%; contribution to the score · 2023-09-30 · +0.728 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 0.0%; contribution to the score · 2023-09-30 · +0.618 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: equity as a share of assets, value -4.5%; contribution to the score · 2023-09-30 · +0.390 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value -261.2%; contribution to the score · 2023-09-30 · -0.910 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: securities as a share of assets, value 38.2%; contribution to the score · 2023-09-30 · -0.312 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -105.6%; contribution to the score · 2023-09-30 · -0.293 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2023-09-30 · -0.236 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -9.2%; contribution to the score · 2023-09-30 · -0.132 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Failure date · 2023-11-03 · 2023-11-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 119.8%; contribution to the score · 2023-06-30 · +1.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: the Texas ratio (troubled assets against capital plus reserves), value 143.5%; contribution to the score · 2023-06-30 · +1.045 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2023-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 9.7%; contribution to the score · 2023-06-30 · +0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F94 · Driver down #2 at 2023-06-30: the Tier 1 risk-based capital ratio, value 10.4%; contribution to the score · 2023-06-30 · -0.829 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F97 · Driver down #5 at 2023-06-30: the total risk-based capital ratio, value 11.6%; contribution to the score · 2023-06-30 · -0.253 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
