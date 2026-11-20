---
cert: 58665
name: "Live Oak Banking Co"
as_of: 2026-06-30
rank: 29
n_banks: 4313
percentile: 99.35079990725713
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Live Oak Banking Co (cert 58665)

*Outcome not yet known.*

## Summary

Live Oak Banking Co, a North Carolina bank, ranked 29 out of 4,313 FDIC-insured banks as of 2026-06-30, placing it in the 99.4th percentile of Canary's risk ranking and on its watchlist. Its capital cushion was thin next to the national median, with a leverage ratio (core capital as a share of average assets) of 8.0% against 11.0%, while troubled loans and reliance on brokered deposits were well above typical levels. On the other side, the bank was profitable, with a return on equity of 12.6% against a national median of 11.6%, and the model gave that some weight in its favor.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was low across every measure: equity was 7.6% of assets against a national median of 10.6%, and the leverage ratio was 8.0% against 11.0%. The risk-based measures, which weigh assets by how risky they are, told the same story: the Tier 1 ratio was 10.5% against 14.6%, and the total risk-based ratio was 11.7% against 15.8%.

Credit quality was the clearest weak spot: loans 90 or more days past due or no longer earning interest were 4.0% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 3.4% of assets against 0.3%, and the Texas ratio, which weighs troubled assets against capital plus reserves, was 38.3% against 2.9%. Net loan write-offs (loans given up as lost) ran at 0.7% of loans against a median of 0.0%, and the provision set aside for future loan losses was 0.6% of assets against 0.1%. Commercial real estate loans were 39.3% of loans, well above the national median of 23.6%, although the separate concentration section found the bank did not cross either regulatory screening line. Early-stage delinquencies were not elevated: loans 30-89 days past due were 0.1% of assets against a median of 0.2%.

On funding, brokered deposits, money placed through outside middlemen, made up 28.8% of deposits while the national median was 0.0%, and core deposits, the stable everyday kind, were 61.5% of assets against 75.5%. Funding was costly, with annualized interest expense at 2.9% of assets against 1.6%, and the bank grew quickly, with assets up 16.1% over the past four quarters against a median of 4.5%. Some funding signs were milder: uninsured deposits were 16.6% of deposits against 24.8%, and volatile funding was 4.0% of assets against 9.0%. Unrealized losses on bonds available for sale were 5.7% of equity, close to the national median of 5.6%, and losses on bonds held to maturity were 0.0%, matching the median.

## Understanding the score

As of 2026-06-30, the bank ranked 29 out of 4,313 banks nationally, the 99.4th percentile on a scale from 0 to 100 where higher means riskier. That placed it on Canary's watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were brokered deposits at 28.8% of deposits, interest expense at 2.9% of assets, loans 90 or more days past due or not accruing interest at 4.0% of loans, the efficiency ratio (operating costs as a share of revenue) at 53.2%, and losses on bonds available for sale at 5.7% of equity. Brokered deposits were by far the largest of these, contributing +1.189 to the score.

The five factors that pulled the score down most were return on equity at 12.6%, the Tier 1 risk-based capital ratio at 10.5%, construction loans at 7.4% of loans, loans 30-89 days past due at 0.1% of assets, and return on assets at 1.0%. The Tier 1 ratio lowered the score even though it sat well below the national median, which shows the model weighs each figure in combination with the others rather than one at a time.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 113 | 4,589 |  |
| 2024-12-31 | 110 | 4,560 |  |
| 2025-03-31 | 24 | 4,536 | ▲ watchlist |
| 2025-06-30 | 107 | 4,494 |  |
| 2025-09-30 | 55 | 4,452 | ▲ watchlist |
| 2025-12-31 | 27 | 4,411 | ▲ watchlist |
| 2026-03-31 | 50 | 4,353 | ▲ watchlist |
| 2026-06-30 | 29 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the bank ranked 29 out of 4,313 banks nationally, placing it in the 99.4th percentile, where a higher percentile means the model sees more risk. A year earlier it sat in the 97.6th percentile, so the model rated it riskier than a year earlier. Canary compared 30 of the bank's financial ratios with each ratio's own range over the prior 12 quarters, and 4 of them were outside that range.

The efficiency ratio (operating costs as a share of revenue) was 53.2%, below its prior range of 60.9% to 72.4%, after a change of -7.7 pp over four quarters. Even so, this ratio at 53.2% added +0.339 model log-odds units (the model's internal scoring units, where positive raises the score), which pushed the score up. Annualized interest expense as a share of assets (what the bank pays for its funding, relative to its size) was 2.85%, just below its prior range of 2.88% to 3.5%, and its contribution of +0.467 pushed the score up.

Securities as a share of assets (bonds and similar holdings) were 9.2%, below their prior range of 9.4% to 10.6%, yet their contribution of -0.042 had little effect on the score. Volatile funding as a share of assets (money that can leave the bank quickly) was 4.0%, below its prior range of 4.1% to 6.8%, and despite sitting outside that range its contribution of -0.091 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 53.2% | 60.9% to 72.4% | same quarter, prior 3 years | n/a | -7.7 pp | +0.339 | pushed the score up |
| securities as a share of assets | 9.2% | 9.4% to 10.6% | prior 12 quarters | -0.2 pp | -0.4 pp | -0.042 | little effect on the score |
| volatile funding as a share of assets | 4.0% | 4.1% to 6.8% | prior 12 quarters | -0.1 pp | -1.0 pp | -0.091 | pushed the score down |
| annualized interest expense as a share of assets | 2.85% | 2.88% to 3.5% | same quarter, prior 3 years | n/a | -0.4 pp | +0.467 | pushed the score up |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

The Texas ratio, which weighs troubled assets against capital plus reserves, was 38.3%, at the 98.7th percentile nationally, which is unusually high, and at the 98.6th percentile among its peers against a peer median of 4.1%, which is unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) and foreclosed property made up 3.4% of assets, at the 98.1st percentile nationally, which is unusually high, and at the 98.6th percentile among its peers against a peer median of 0.5%, which is unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 4.0% of loans, at the 96.4th percentile nationally, which is unusually high, and at the 97.8th percentile among its peers against a peer median of 0.7%, which is unusually high among its peers too. The annualized provision for loan losses, money set aside to cover expected bad loans, was 0.6% of assets, at the 96.5th percentile nationally, which is unusually high, and at the 95.9th percentile among its peers against a peer median of 0.1%, which is unusually high among its peers too.

Brokered deposits, money placed with the bank through outside middlemen, were 28.8% of deposits, at the 97.9th percentile nationally, which is unusually high, and at the 98.6th percentile among its peers against a peer median of 3.2%, which is unusually high among its peers too. Annualized interest expense, what the bank pays to borrow and hold deposits, was 2.9% of assets, at the 97.5th percentile nationally, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 1.6%, which is unusually high among its peers too.

The leverage ratio, core capital as a share of average assets and a basic cushion against losses, was 8.0%, at the 3.0th percentile nationally, which is unusually low, and at the 7.5th percentile among its peers against a peer median of 10.0%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio, core capital measured against assets weighted by their riskiness, was 10.5%, at the 3.8th percentile nationally, which is unusually low, and at the 2.3rd percentile among its peers against a peer median of 12.7%, which is unusually low among its peers too. Overall, 13 of the bank's ratios sit in the national top or bottom 10%, and 11 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 38.3% | 98.7th (unusually high) | 4.1% | 98.6th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 3.4% | 98.1st (unusually high) | 0.5% | 98.6th | unusually high among its peers too |
| brokered deposits as a share of deposits | 28.8% | 97.9th (unusually high) | 3.2% | 98.6th | unusually high among its peers too |
| annualized interest expense as a share of assets | 2.9% | 97.5th (unusually high) | 1.6% | 99.5th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 8.0% | 3.0th (unusually low) | 10.0% | 7.5th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 0.6% | 96.5th (unusually high) | 0.1% | 95.9th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 4.0% | 96.4th (unusually high) | 0.7% | 97.8th | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 10.5% | 3.8th (unusually low) | 12.7% | 2.3rd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 68.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 228.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 120.4% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank's case is an open watchlist case, meaning it was flagged and the fact sheet holds no later data showing what followed. The flag rests on the as-of picture of high troubled loans, heavy use of brokered deposits and a thin capital cushion, offset in part by solid profits. Without later data, this note cannot say whether those pressures eased or worsened.

## What happened next

In hindsight: the fact sheet contains no ranks, flags or reporting status after the as-of quarter of 2026-06-30. So this note cannot say where the bank ranked later or whether it still files reports; the score history table added by code shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Live Oak Banking Co · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NC · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 29 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 39.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 38.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 28.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 61.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · 16.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 28.8%; contribution to the score · 2026-06-30 · +1.189 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 2.9%; contribution to the score · 2026-06-30 · +0.467 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 4.0%; contribution to the score · 2026-06-30 · +0.357 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 53.2%; contribution to the score · 2026-06-30 · +0.339 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 5.7%; contribution to the score · 2026-06-30 · +0.176 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 12.6%; contribution to the score · 2026-06-30 · -0.697 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.5%; contribution to the score · 2026-06-30 · -0.648 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: construction loans as a share of loans, value 7.4%; contribution to the score · 2026-06-30 · -0.463 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.1%; contribution to the score · 2026-06-30 · -0.349 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.0%; contribution to the score · 2026-06-30 · -0.257 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 53.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 60.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 72.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · -7.7 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.339 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F96 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F97 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 10.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F100 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.042 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F101 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature securities_to_assets contribution
- F102 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F103 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 4.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F104 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 6.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F107 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.091 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F108 · Trend: volatile funding as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F109 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 2.85% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F110 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 2.88% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F111 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.467 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F114 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F115 · Trend: ratios outside their own prior range · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F117 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F118 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F120 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.6% · data/analyst/scores.parquet: percentile
- F121 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F125 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 38.3% · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: texas_ratio
- F127 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F128 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: texas_ratio
- F129 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 4.1% · data/features/fct_bank_features.parquet: texas_ratio
- F130 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F136 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F137 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 28.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F138 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.9th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F139 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F140 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F141 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F142 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F143 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F144 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F145 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F146 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F147 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F148 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F149 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 3.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F151 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 7.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F159 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F162 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.4th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F163 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F167 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.8th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 2.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F175 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F177 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
