---
cert: 4134
name: "First Nb Of Lindsay"
as_of: 2024-09-30
rank: 9
n_banks: 4589
percentile: 99.82567008062759
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2024-10-18
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:47:26"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of Lindsay (cert 4134)

*Hindsight: failed 2024-10-18. Canary flagged it 1 quarter ahead.*

## Summary

As of 2024-09-30, First Nb Of Lindsay ranked 9 out of 4,589 banks on Canary's risk score, which puts it in the 99.8th percentile, where higher means riskier. That placed it on Canary's watchlist, which covers the top 2% of banks by score. The figures that stood out most were a Texas ratio (troubled assets against the bank's capital cushion) of 133.7% against a national median of 2.2%, and seriously late or non-paying loans at 10.6% of loans against a median of 0.4%.

## Warning signs in the data

Capital, the bank's own cushion against losses, looked roughly normal on paper: equity was 11.1% of assets against a national median of 10.0%, and the leverage ratio (core capital as a share of average assets) was 10.0% against a median of 10.7%. Credit quality was the clear problem. Loans 90 or more days past due or no longer earning interest made up 10.6% of loans, far above the national median of 0.4%, and loans 30-89 days past due were 10.4% of assets against a median of 0.2%. Annualized loan write-offs (loans written off as losses, net of recoveries) were 20.6% of loans against a median of 0.0%, and loan-loss reserves (money set aside for expected bad loans) were reported at -11.2% of loans against a median of 1.2%. The Texas ratio stood at 133.7%, compared with a national median of 2.2%.

Earnings were weak: return on assets was -0.7% against a median of 0.9%, and the efficiency ratio (operating costs as a share of revenue) was 126.6% against a median of 67.8%, meaning costs exceeded revenue. Funding and liquidity looked comparatively steady, with cash at 21.4% of assets against a median of 6.2%, core deposits (stable, everyday deposits) at 83.6% of assets against a median of 75.0%, and brokered deposits at 0.0%. Losses on bonds available for sale were small, at 0.1% of equity against a national median of 8.5%.

## Understanding the score

On 2024-09-30 the bank ranked 9 of 4,589 banks, in the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 92 banks that quarter, which is the top 2% by score.

Five features pushed the score up most. The largest were the Texas ratio at 133.7%, adding +1.563, and loans 90 or more days past due or not earning interest at 10.6% of loans, adding +1.261. Smaller upward pushes came from loans 30-89 days past due at 10.4% of assets (+0.296), losses on bonds available for sale at 0.1% of equity (+0.104), and deposit growth over the past four quarters of 17.8% (+0.097).

Five features pulled the score down most. The Tier 1 risk-based capital ratio, a capital measure weighted by how risky the assets are, had the largest effect at -0.670, though its value is not shown in the fact sheet. The others were return on equity at -6.9% (-0.526), construction loans at 3.9% of loans (-0.461), nonaccrual assets and foreclosed property at 0.9% of assets (-0.254), and loan-loss reserves at -11.2% of loans (-0.251).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-12-31 | 2,776 | 4,773 |  |
| 2023-03-31 | 1,256 | 4,740 |  |
| 2023-06-30 | 1,082 | 4,714 |  |
| 2023-09-30 | 2,298 | 4,686 |  |
| 2023-12-31 | 2,335 | 4,658 |  |
| 2024-03-31 | 799 | 4,640 |  |
| 2024-06-30 | 573 | 4,610 |  |
| 2024-09-30 | 9 | 4,589 | ▲ watchlist (first flag) |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the previous 12 quarters, and 17 of the 28 ratios checked sat outside that range at 2024-09-30. The model rated the bank riskier than a year earlier: it was in the 51.0th percentile on 2023-09-30 and ranked 9 of 4,589 at the as-of quarter.

The Texas ratio reached 133.7%, far above its prior range of 10.3% to 14.9% after a jump of +120.9 pp in one quarter, and with a contribution of +1.563 it pushed the score up. Loans 90 or more days past due or not earning interest rose to 10.6% of loans, above a prior range of 1.7% to 2.8%, and with a contribution of +1.261 this ratio pushed the score up.

Some ratios moved far outside their range yet worked the other way in the model. Loan-loss reserves fell to -11.2% of loans, below a prior range of 2.8% to 3.6%, yet with a contribution of -0.251 this ratio pushed the score down. Return on equity dropped to -6.9%, below a prior range of 14.6% to 18.0%, yet with a contribution of -0.526 it pushed the score down. The efficiency ratio climbed to 126.6%, above a prior range of 42.3% to 50.5%, yet with a contribution of -0.062 it pushed the score down. Annualized loan write-offs rose to 20.6% of loans, above a prior range of 0.0% to 0.1%, but with a contribution of -0.005 they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 133.7% | 10.3% to 14.9% | prior 12 quarters | +120.9 pp | +121.8 pp | +1.563 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 20.6% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +20.5 pp | -0.005 | little effect on the score |
| loan-loss reserves as a share of loans | -11.2% | 2.8% to 3.6% | prior 12 quarters | -14.8 pp | -14.7 pp | -0.251 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 126.6% | 42.3% to 50.5% | same quarter, prior 3 years | n/a | +76.1 pp | -0.062 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 10.6% | 1.7% to 2.8% | prior 12 quarters | +8.6 pp | +8.5 pp | +1.261 | pushed the score up |
| return on equity (profit as a share of equity) | -6.9% | 14.6% to 18.0% | same quarter, prior 3 years | n/a | -21.5 pp | -0.526 | pushed the score down |

17 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2024-09-30, which was also the last quarter it reported. The bank failed on October 18, 2024, giving a lead time of 1 quarter between the first flag and the failure. This is a caught case: the bank was on the watchlist before it failed, though the warning came close to the event.

## What happened next

With hindsight, the bank's last reported quarter was 2024-09-30, so no later ranks or flags exist. The bank failed on October 18, 2024. Our data only shows that it stopped reporting and does not by itself distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · First Nb Of Lindsay · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2024-09-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-09-30 · 4,589 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-09-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-09-30 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-09-30 · 11.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 10.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2024-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F51 · Bank: core deposits as a share of assets · 2024-09-30 · 83.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2024-09-30 · 75.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2024-09-30 · 21.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2024-09-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2024-09-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2024-09-30 · 8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 133.7%; contribution to the score · 2024-09-30 · +1.563 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 10.6%; contribution to the score · 2024-09-30 · +1.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: loans 30-89 days past due, as a share of assets, value 10.4%; contribution to the score · 2024-09-30 · +0.296 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F74 · Driver up #4: losses on bonds available for sale, as a share of equity, value 0.1%; contribution to the score · 2024-09-30 · +0.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 17.8%; contribution to the score · 2024-09-30 · +0.097 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2024-09-30 · -0.670 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value -6.9%; contribution to the score · 2024-09-30 · -0.526 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 3.9%; contribution to the score · 2024-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2024-09-30 · -0.254 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value -11.2%; contribution to the score · 2024-09-30 · -0.251 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Failure date · 2024-10-18 · 2024-10-18 · data/raw/failures: FAILDATE
- F82 · First flag quarter (Phase 3 lead-time rule) · 2024-09-30 · 2024-09-30 · data/analyst/scores.parquet: flagged
- F83 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F84 · Last quarter the bank reported · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F85 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F86 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 10.3% · data/features/fct_bank_features.parquet: texas_ratio
- F87 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 14.9% · data/features/fct_bank_features.parquet: texas_ratio
- F88 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2024-09-30 · +120.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F90 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2024-09-30 · +1.563 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2024-09-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F94 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2024-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F98 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F99 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F100 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F103 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · -0.251 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F104 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 42.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 50.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2024-09-30 · -0.062 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F112 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F113 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F116 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · +1.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F117 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2024-09-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F118 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2024-09-30 · -6.9% · data/features/fct_bank_features.parquet: return_on_equity
- F119 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: return_on_equity
- F120 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 18.0% · data/features/fct_bank_features.parquet: return_on_equity
- F122 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2024-09-30 · -0.526 · data/analyst/scores.parquet: feature return_on_equity contribution
- F123 · Trend: return on equity (profit as a share of equity), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F124 · Trend: ratios outside their own prior range · 2024-09-30 · 17 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2024-09-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2023-09-30 · 51.0% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2024-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
