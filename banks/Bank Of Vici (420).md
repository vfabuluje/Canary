---
cert: 420
name: "Bank Of Vici"
as_of: 2026-06-30
rank: 19
n_banks: 4313
percentile: 99.58265708323673
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:57"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of Vici (cert 420)

*Outcome not yet known.*

## Summary

Bank Of Vici, a small Oklahoma bank, ranked 19 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. That puts it on Canary's watchlist, the riskiest 2% of banks. The main reasons are large paper losses on its bond holdings, a high share of seriously overdue loans, and a high Texas ratio, a measure of troubled assets against the cushion available to absorb them.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, is thin: equity was 7.1% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.2% against a median of 11.0%. Unrealized losses on bonds available for sale equaled 56.7% of equity, far above the national median of 5.6%.

Credit quality is weak: loans 90 or more days past due or no longer accruing interest were 12.3% of loans, versus a national median of 0.5%. The Texas ratio was 69.0%, compared with a national median of 2.9%. The bank was losing money, with a return on assets of -0.9% against a median of 1.2%, and its efficiency ratio (operating costs as a share of revenue) was 118.5% against a median of 62.1%.

On funding, deposits shrank by -13.5% over the past four quarters while the national median grew 4.2%, and volatile funding was 15.7% of assets against a median of 9.0%. Uninsured deposits, those above the FDIC insurance limit, were lower than typical at 15.7% versus a median of 24.8%.

## Understanding the score

As of 2026-06-30, Bank Of Vici ranked 19 of 4,313 banks, in the 99.6th percentile. It was flagged as one of 87 banks on the watchlist that quarter, which covers the top 2% of banks by score.

The five factors pushing the score up most were bond losses at 56.7% of equity (+0.920), seriously overdue loans at 12.3% of loans (+0.917), the Texas ratio at 69.0% (+0.830), asset growth of -11.7% (+0.125), and loans at 50.3% of deposits (+0.122).

The five factors pulling the score down most were the Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets (-0.744), nonaccrual assets and foreclosed property at 0.9% of assets (-0.385), the efficiency ratio at 118.5% (-0.282), the leverage ratio at 10.2% (-0.272), and return on equity at -13.2% (-0.237).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 21 | 4,589 | ▲ watchlist |
| 2024-12-31 | 18 | 4,560 | ▲ watchlist |
| 2025-03-31 | 11 | 4,536 | ▲ watchlist |
| 2025-06-30 | 9 | 4,494 | ▲ watchlist |
| 2025-09-30 | 25 | 4,452 | ▲ watchlist |
| 2025-12-31 | 34 | 4,411 | ▲ watchlist |
| 2026-03-31 | 197 | 4,353 |  |
| 2026-06-30 | 19 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios compared, 6 were outside their prior range. The Texas ratio reached 69.0%, above its prior range of 15.2% to 64.5% after rising 53.5 pp in one quarter, and it pushed the score up by +0.830 model log-odds units. Loan-loss reserves were 3.2% of loans, just above their prior range of 0.1% to 3.1%, and pushed the score up by +0.058. Commercial real estate loans fell to 9.7% of loans, below their prior range of 13.4% to 23.2%, and still pushed the score up by +0.102.

Loans in the early stages of being overdue fell to 0.6% of assets, below their prior range of 1.4% to 5.5%, and this pushed the score down by -0.192. Construction loans dropped to 0.0% of loans, below their prior range of 1.0% to 3.3%, and pushed the score down by -0.176. Net loan write-offs fell to 0.3% of loans, below their prior range of 3.1% to 4.0%, yet had little effect on the score at +0.007.

Overall, the model rated the bank about the same as a year earlier, when it sat in the 99.8th percentile on 2025-06-30, compared with the 99.6th percentile now.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 0.3% | 3.1% to 4.0% | same quarter, prior 3 years | n/a | -3.7 pp | +0.007 | little effect on the score |
| construction loans as a share of loans | 0.0% | 1.0% to 3.3% | prior 12 quarters | -1.3 pp | -2.1 pp | -0.176 | pushed the score down |
| commercial real estate loans as a share of loans | 9.7% | 13.4% to 23.2% | prior 12 quarters | -6.9 pp | -7.8 pp | +0.102 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 0.6% | 1.4% to 5.5% | prior 12 quarters | -4.0 pp | -0.8 pp | -0.192 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 69.0% | 15.2% to 64.5% | prior 12 quarters | +53.5 pp | +28.0 pp | +0.830 | pushed the score up |
| loan-loss reserves as a share of loans | 3.2% | 0.1% to 3.1% | prior 12 quarters | +0.3 pp | +1.0 pp | +0.058 | pushed the score up |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank's outcome case is that it remains open and on the watchlist. The fact sheet contains no hindsight data from after the as-of quarter, so we cannot add anything beyond the as-of picture described above.

## What happened next

In hindsight, no later ranks, flags or reporting status are included in this fact sheet. Any later scores, if available, appear in the score history table added below.

## Sources

- F1 · Bank name · n/a · Bank Of Vici · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 19 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 118.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 56.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -13.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 56.7%; contribution to the score · 2026-06-30 · +0.920 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 12.3%; contribution to the score · 2026-06-30 · +0.917 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 69.0%; contribution to the score · 2026-06-30 · +0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F74 · Driver up #4: asset growth over the past four quarters, value -11.7%; contribution to the score · 2026-06-30 · +0.125 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F75 · Driver up #5: loans as a share of deposits, value 50.3%; contribution to the score · 2026-06-30 · +0.122 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.744 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2026-06-30 · -0.385 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F78 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 118.5%; contribution to the score · 2026-06-30 · -0.282 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: return on equity (profit as a share of equity), value -13.2%; contribution to the score · 2026-06-30 · -0.237 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F82 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F83 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F85 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.007 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F86 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F87 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F88 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F89 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F92 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.176 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F93 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F94 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F95 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F96 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.102 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F100 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 5.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.192 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F109 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: texas_ratio
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 64.5% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +53.5 pp · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F115 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F116 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F117 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F120 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.058 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F121 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F122 · Trend: ratios outside their own prior range · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F125 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F126 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F127 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F128 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
