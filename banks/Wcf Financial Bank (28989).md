---
cert: 28989
name: "Wcf Financial Bank"
as_of: 2026-06-30
rank: 16
n_banks: 4313
percentile: 99.6522142360306
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:13"
writer_model: "claude-opus-5-5"
checked: true
---

# Wcf Financial Bank (cert 28989)

*Outcome not yet known.*

## Summary

Wcf Financial Bank, an Iowa bank, ranked 16 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, which places it in the 99.7th percentile. It is on Canary's watchlist, which covers about 2% of banks. Its capital cushion is thinner than the national median, and its troubled loans and reliance on less stable funding are well above typical levels.

## Warning signs in the data

Capital, the owners' money that absorbs losses, is below the national median: equity was 7.9% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.3% against 11.0%. The Tier 1 risk-based capital ratio, which measures capital against riskier assets, was 11.5% versus a median of 14.6%.

Credit quality is the weakest area: loans 90+ days past due or not accruing interest were 5.1% of loans, far above the 0.5% median. Loans 30-89 days past due, an earlier stage of trouble, were 3.0% of assets against a median of 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 45.9% against a national median of 2.9%.

On funding, brokered deposits (money placed through intermediaries, which can leave quickly) were 15.2% of deposits versus a median of 0.0%, and Federal Home Loan Bank borrowings were 13.4% of assets versus 0.2%. Volatile funding was 30.6% of assets against a 9.0% median, and loans were 100.3% of deposits against 80.2%. Unrealized losses on bonds available for sale equaled 6.9% of equity, somewhat above the 5.6% median, and return on assets, a profit measure, was 0.1% against a median of 1.2%.

## Understanding the score

As of 2026-06-30 the bank ranked 16 of 4,313 banks, in the 99.7th percentile on a scale where higher means riskier. It was flagged on the watchlist, one of 87 banks that quarter.

The five factors that pushed the score up most were the Texas ratio at 45.9% (contribution +0.781), losses on bonds available for sale at 6.9% of equity (+0.641), loans 30-89 days past due at 3.0% of assets (+0.481), brokered deposits at 15.2% of deposits (+0.423), and interest expense at 2.7% of assets (+0.387).

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 11.5% (contribution -1.448), the total risk-based capital ratio at 12.7% (-0.371), the efficiency ratio (operating costs as a share of revenue) at 95.3% (-0.303), return on equity at 1.3% (-0.272), and construction loans at 5.9% of loans (-0.271).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,377 | 4,589 |  |
| 2024-12-31 | 1,386 | 4,560 |  |
| 2025-03-31 | 799 | 4,536 |  |
| 2025-06-30 | 678 | 4,494 |  |
| 2025-09-30 | 128 | 4,452 |  |
| 2025-12-31 | 18 | 4,411 | ▲ watchlist |
| 2026-03-31 | 12 | 4,353 | ▲ watchlist |
| 2026-06-30 | 16 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compared 30 of the bank's ratios with their own history over the prior 12 quarters, and 4 were outside their prior range. A year earlier, on 2025-06-30, the bank sat in the 84.9th percentile, and by 2026-06-30 it was in the 99.7th percentile at rank 16 of 4,313, so the model rated it riskier than a year earlier.

Brokered deposits were 15.2% of deposits, above their prior range of 0.0% to 14.0% after a +15.2 pp change over four quarters, and this ratio pushed the score up with a contribution of +0.423 model log-odds units. Cash was 4.8% of assets, above its prior range of 1.1% to 4.5%, yet it pushed the score down with a contribution of -0.073.

Securities were 10.1% of assets, just below their prior range of 10.4% to 13.4%, and this ratio pushed the score down with a contribution of -0.053. Loan-loss reserves, money set aside for expected bad loans, were 1.14% of loans, slightly above their prior range of 0.7% to 1.13%, and this ratio pushed the score down with a contribution of -0.237.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| cash as a share of assets | 4.8% | 1.1% to 4.5% | prior 12 quarters | +2.4 pp | +0.3 pp | -0.073 | pushed the score down |
| securities as a share of assets | 10.1% | 10.4% to 13.4% | prior 12 quarters | -0.3 pp | -1.8 pp | -0.053 | pushed the score down |
| brokered deposits as a share of deposits | 15.2% | 0.0% to 14.0% | prior 12 quarters | +1.2 pp | +15.2 pp | +0.423 | pushed the score up |
| loan-loss reserves as a share of loans | 1.14% | 0.7% to 1.13% | prior 12 quarters | +0.01 pp | +0.4 pp | -0.237 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight: Canary classifies this bank as an open watchlist case, meaning it was flagged and no failure is recorded in our data. The fact sheet contains no data from after the as-of quarter, so this memo cannot describe how the bank's position changed later.

## What happened next

In hindsight: no later ranks, flags or reporting status are included in this fact sheet, so we cannot say here how the bank ranked afterward or whether it continued to report. Its case remains open on the watchlist in Canary's records.

## Sources

- F1 · Bank name · n/a · Wcf Financial Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 16 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 45.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 100.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 15.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 30.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 45.9%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.9%; contribution to the score · 2026-06-30 · +0.641 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: loans 30-89 days past due, as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.481 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 15.2%; contribution to the score · 2026-06-30 · +0.423 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.387 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.5%; contribution to the score · 2026-06-30 · -1.448 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 12.7%; contribution to the score · 2026-06-30 · -0.371 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 95.3%; contribution to the score · 2026-06-30 · -0.303 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 1.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.271 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F86 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F87 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F90 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.073 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F91 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F92 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F93 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 10.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F94 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F97 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.053 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F98 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F99 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 15.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F100 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F101 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 14.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F103 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +15.2 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F104 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.423 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F105 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F106 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 1.14% · data/features/fct_bank_features.parquet: allowance_to_loans
- F107 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F108 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.13% · data/features/fct_bank_features.parquet: allowance_to_loans
- F111 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.237 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F112 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F113 · Trend: ratios outside their own prior range · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F115 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F116 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F118 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 84.9% · data/analyst/scores.parquet: percentile
- F119 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
