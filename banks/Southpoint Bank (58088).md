---
cert: 58088
name: "Southpoint Bank"
as_of: 2026-06-30
rank: 4
n_banks: 4313
percentile: 99.93044284720612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:07:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Southpoint Bank (cert 58088)

*Outcome not yet known.*

## Summary

As of June 30, 2026, Southpoint Bank, an Alabama bank, ranked 4 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. The main pressures in the data were a sharp loss in profit, thin capital, heavy loan write-offs and a large reliance on brokered deposits, which are funds placed through middlemen rather than gathered directly from customers.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin: equity was 7.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.9% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also well below the norm, with a Tier 1 ratio of 8.9% against a median of 14.6% and a total ratio of 10.2% against 15.8%.

Credit quality was weak: loans 90 or more days past due or no longer accruing interest were 3.5% of loans, against a national median of 0.5%. Net loan write-offs, loans given up as uncollectable, ran at an annualized 4.5% of loans against a median of 0.0%, and the provision for future loan losses was 3.7% of assets against 0.1%. The Texas ratio, which sets troubled assets against capital plus reserves, was 32.5% against a median of 2.9%, and return on equity, profit as a share of equity, was -22.1% against 11.6%.

On funding, brokered deposits made up 23.4% of deposits against a national median of 0.0%, while core deposits, the stable everyday kind, were 55.0% of assets against 75.5%. Deposits shrank by -18.8% over the past four quarters, while the median bank grew them by 4.2%, though the bank held cash of 13.2% of assets, well above the median of 6.2%. Unrealized losses on bonds available for sale equalled 8.7% of equity, above the national median of 5.6%.

## Understanding the score

Southpoint Bank ranked 4 of 4,313 banks as of 2026-06-30, the 99.9th percentile on a scale where higher means riskier. It was flagged for the watchlist, which holds the top 2% of banks by score, or 87 banks that quarter.

The five features that pushed the score up most were return on equity at -22.1% (contribution +0.828), losses on bonds available for sale at 8.7% of equity (+0.762), brokered deposits at 23.4% of deposits (+0.511), the Tier 1 risk-based capital ratio at 8.9% (+0.419), and interest expense at 2.8% of assets (+0.376). The five that pulled it down most were construction loans at 10.0% of loans (-0.301), loans 30-89 days past due at 0.7% of assets (-0.233), the Texas ratio at 32.5% (-0.231), total assets of $1.4 billion (-0.178), and commercial real estate loans at 38.0% of loans (-0.165).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 31 | 4,589 | ▲ watchlist |
| 2024-12-31 | 7 | 4,560 | ▲ watchlist |
| 2025-03-31 | 18 | 4,536 | ▲ watchlist |
| 2025-06-30 | 13 | 4,494 | ▲ watchlist |
| 2025-09-30 | 7 | 4,452 | ▲ watchlist |
| 2025-12-31 | 6 | 4,411 | ▲ watchlist |
| 2026-03-31 | 6 | 4,353 | ▲ watchlist |
| 2026-06-30 | 4 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked, 8 were outside their own prior range at the as-of quarter. The model rated the bank about the same as a year earlier: it was in the 99.7th percentile on 2025-06-30 and the 99.9th percentile now.

Return on equity fell to -22.1%, far below its prior range of 7.2% to 13.7%, a change of -29.3 pp over four quarters, and it pushed the score up with a contribution of +0.828. The loan-loss provision rose to 3.7% of assets, above its prior range of 0.2% to 0.9%, and it pushed the score up with a contribution of +0.168.

Net loan write-offs reached 4.5% of loans, well above their prior range of 0.0% to 0.9%, yet they had little effect on the score, with a contribution of -0.005. Return on assets dropped to -1.7%, below its prior range of 0.5% to 1.2%, but it too had little effect on the score, contributing +0.043. The efficiency ratio, operating costs as a share of revenue, climbed to 65.3%, above its prior range of 53.7% to 57.9%, but had little effect on the score, contributing -0.044. Construction loans slipped to 10.0% of loans, below their prior range of 10.7% to 17.5%, and this pushed the score down with a contribution of -0.301.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -22.1% | 7.2% to 13.7% | same quarter, prior 3 years | n/a | -29.3 pp | +0.828 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.5% | 0.0% to 0.9% | same quarter, prior 3 years | n/a | +3.6 pp | -0.005 | little effect on the score |
| annualized provision for loan losses as a share of assets | 3.7% | 0.2% to 0.9% | same quarter, prior 3 years | n/a | +2.8 pp | +0.168 | pushed the score up |
| return on assets (profit as a share of assets) | -1.7% | 0.5% to 1.2% | same quarter, prior 3 years | n/a | -2.2 pp | +0.043 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 65.3% | 53.7% to 57.9% | same quarter, prior 3 years | n/a | +7.4 pp | -0.044 | little effect on the score |
| construction loans as a share of loans | 10.0% | 10.7% to 17.5% | prior 12 quarters | -0.7 pp | -4.2 pp | -0.301 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 753 banks in the same specialty group and size tier ($1 billion to $10 billion).

The bank's Tier 1 risk-based capital ratio of 8.9% sat at the 0.3rd percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 13.3%, unusually low among its peers too. Its total risk-based capital ratio of 10.2% was at the 0.3rd percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 14.5%, unusually low among its peers too. Its leverage ratio of 6.9% was at the 0.9th percentile nationally, unusually low, and at the 0.6th percentile among peers against a peer median of 10.5%, unusually low among its peers too.

Return on equity of -22.1% was at the 0.8th percentile nationally, unusually low, and at the 0.5th percentile among peers against a peer median of 11.8%, unusually low among its peers too. The loan-loss provision of 3.7% of assets was at the 99.6th percentile nationally, unusually high, and at the 99.5th percentile among peers against a peer median of 0.1%, unusually high among its peers too. Net loan write-offs of 4.5% of loans were at the 99.5th percentile nationally, unusually high, and at the 99.5th percentile among peers against a peer median of 0.0%, unusually high among its peers too.

Asset growth of -18.8% was at the 0.4th percentile nationally, unusually low, and at the 0.3rd percentile among peers against a peer median of 5.3%, unusually low among its peers too. Deposit growth of -18.8% was at the 0.6th percentile nationally, unusually low, and at the 0.3rd percentile among peers against a peer median of 5.0%, unusually low among its peers too. Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Tier 1 risk-based capital ratio | 8.9% | 0.3rd (unusually low) | 13.3% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | 10.2% | 0.3rd (unusually low) | 14.5% | 0.1st | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 3.7% | 99.6th (unusually high) | 0.1% | 99.5th | unusually high among its peers too |
| asset growth over the past four quarters | -18.8% | 0.4th (unusually low) | 5.3% | 0.3rd | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.5% | 99.5th (unusually high) | 0.0% | 99.5th | unusually high among its peers too |
| deposit growth over the past four quarters | -18.8% | 0.6th (unusually low) | 5.0% | 0.3rd | unusually low among its peers too |
| return on equity (profit as a share of equity) | -22.1% | 0.8th (unusually low) | 11.8% | 0.5th | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 6.9% | 0.9th (unusually low) | 10.5% | 0.6th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 85.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 306.0% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -21.7% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank's case is that it remained open and on Canary's watchlist rather than appearing among banks that closed. This fact sheet holds no data from after the as-of quarter, so we cannot add later figures that explain why it stayed flagged.

## What happened next

In hindsight, the bank is classed as still open and still on the watchlist in our data. The fact sheet does not include its later ranks or flags, so we cannot report how its position moved after the as-of quarter.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 32.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -18.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -22.1%; contribution to the score · 2026-06-30 · +0.828 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 8.7%; contribution to the score · 2026-06-30 · +0.762 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: brokered deposits as a share of deposits, value 23.4%; contribution to the score · 2026-06-30 · +0.511 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F78 · Driver up #4: the Tier 1 risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.419 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.376 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: construction loans as a share of loans, value 10.0%; contribution to the score · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.233 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 32.5%; contribution to the score · 2026-06-30 · -0.231 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: total assets, value $1.4 billion; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 38.0%; contribution to the score · 2026-06-30 · -0.165 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.2% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.7% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -29.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.828 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F101 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.168 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F106 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.043 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 65.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 53.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 57.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.044 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F119 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F120 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F121 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 17.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F124 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F125 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F137 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F138 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F139 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F140 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F141 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F142 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F143 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F144 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F145 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F146 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F147 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F148 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -18.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F155 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: asset_growth_4q
- F156 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F157 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F158 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F159 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F165 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F166 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -18.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F167 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F168 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F169 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F170 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F171 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F172 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F178 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F179 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: leverage_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F181 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F182 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F183 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F185 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F186 · Peers: those ratios also unusual among peers · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F188 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
