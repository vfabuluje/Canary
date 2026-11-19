---
cert: 8681
name: "Lamont Bank Of St John"
as_of: 2026-06-30
rank: 2
n_banks: 4313
percentile: 99.97681428240203
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:07:49"
writer_model: "claude-opus-5-5"
checked: true
---

# Lamont Bank Of St John (cert 8681)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Lamont Bank Of St John in WA ranked 2 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile, where higher means riskier. That rank puts it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was thin, with equity at 1.8% of assets against a national median of 10.6%, and 49.8% of its loans were 90+ days past due or no longer earning interest.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was far below typical levels: equity was 1.8% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 3.0% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also low, with the Tier 1 ratio at 3.2% against a median of 14.6% and the total ratio at 4.5% against 15.8%.

Credit quality was very weak: 49.8% of loans were 90+ days past due or not accruing interest, against a national median of 0.5%, and nonaccrual assets plus foreclosed property were 33.9% of assets against 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 519.1% against a median of 2.9%. Annualized loan write-offs were 4.3% of loans against a median of 0.0%, and the annualized provision for loan losses (money set aside for expected bad loans) was 5.2% of assets against 0.1%. The bank was losing money, with return on assets at -6.2% against a national median of 1.2%.

Funding looked steadier: uninsured deposits were 8.7% of deposits against a median of 24.8%, and core deposits, the stable everyday kind, were 91.3% of assets against 75.5%, though cash was 3.8% of assets against 6.2%. Unrealized losses on bonds available for sale were 87.8% of equity, well above the national median of 5.6%, and total assets shrank by -15.2% over the past four quarters against median growth of 4.5%.

## Understanding the score

As of 2026-06-30, the bank ranked 2 of 4,313 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, or 87 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 3.2% (+1.776), return on equity at -228.8% (+1.190), the Texas ratio at 519.1% (+1.019), loans 90+ days past due or not accruing at 49.8% (+0.505), and the total risk-based capital ratio at 4.5% (+0.445). The five factors pulling it down most were interest expense at 1.7% of assets (-0.193), the efficiency ratio at 165.5% (-0.149), loans 30-89 days past due at 0.7% of assets (-0.146), construction loans at 0.0% of loans (-0.124), and securities at 25.9% of assets (-0.115).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 246 | 4,589 |  |
| 2024-12-31 | 128 | 4,560 |  |
| 2025-03-31 | 153 | 4,536 |  |
| 2025-06-30 | 149 | 4,494 |  |
| 2025-09-30 | 8 | 4,452 | ▲ watchlist |
| 2025-12-31 | 7 | 4,411 | ▲ watchlist |
| 2026-03-31 | 3 | 4,353 | ▲ watchlist |
| 2026-06-30 | 2 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, and 11 of 28 ratios checked were outside that range at the as-of quarter. Return on equity was -228.8%, far below its prior range of -39.3% to 18.1%, and contributed +1.190 model log-odds units, which pushed the score up. The Texas ratio reached 519.1%, above its prior range of 5.6% to 245.1%, and contributed +1.019, which pushed the score up. Loans 90+ days past due or not accruing were 49.8% of loans, above a prior range of 0.8% to 21.9%, contributing +0.505, which pushed the score up. Net interest margin was 1.6%, below its prior range of 2.6% to 3.1%, and contributed +0.085, which pushed the score up.

Nonaccrual assets and foreclosed property were 33.9% of assets, well above the prior range of 0.5% to 11.7%, yet contributed only +0.050, which had little effect on the score. The efficiency ratio was 165.5%, above its prior range of 54.5% to 92.1%, but its contribution of -0.149 pushed the score down, a contrast with how far it moved.

A year earlier, on 2025-06-30, the bank sat in the 96.7% percentile, and at its rank of 2 of 4,313 the model rated it riskier than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -228.8% | -39.3% to 18.1% | same quarter, prior 3 years | n/a | -189.5 pp | +1.190 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 33.9% | 0.5% to 11.7% | prior 12 quarters | +22.2 pp | +32.5 pp | +0.050 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 165.5% | 54.5% to 92.1% | same quarter, prior 3 years | n/a | +73.4 pp | -0.149 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 49.8% | 0.8% to 21.9% | prior 12 quarters | +27.9 pp | +47.8 pp | +0.505 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 519.1% | 5.6% to 245.1% | prior 12 quarters | +274.0 pp | +504.7 pp | +1.019 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 1.6% | 2.6% to 3.1% | same quarter, prior 3 years | n/a | -1.0 pp | +0.085 | pushed the score up |

11 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 227 banks in the same specialty group and size tier (under $100 million).

Nonaccrual assets and foreclosed property were 33.9% of assets, at the 100.0th percentile nationally (unusually high) and the 99.8th percentile among peers, whose median is 0.1%, making it unusually high among its peers too. The Texas ratio of 519.1% sat at the 100.0th percentile nationally (unusually high) and the 99.8th percentile among peers, against a peer median of 2.2%, so it is unusually high among its peers too. Return on equity of -228.8% was at the 0.0th percentile nationally (unusually low) and the 0.2nd percentile among peers, against a peer median of 10.2%, so it is unusually low among its peers too. Loans 90+ days past due or not accruing were 49.8% of loans, at the 100.0th percentile nationally (unusually high) and the 99.8th among peers, against a peer median of 0.4%, so it is unusually high among its peers too.

The total risk-based capital ratio of 4.5% was at the 0.1st percentile nationally (unusually low) and the 0.5th among peers, against a peer median of 20.4%, so it is unusually low among its peers too. The Tier 1 risk-based capital ratio of 3.2% was at the 0.1st percentile nationally (unusually low) and the 0.5th among peers, against a peer median of 19.4%, so it is unusually low among its peers too. The annualized provision for loan losses of 5.2% of assets was at the 99.8th percentile nationally (unusually high) and the 99.8th among peers, against a peer median of 0.0%, so it is unusually high among its peers too. Loan-loss reserves of 7.1% of loans were at the 99.7th percentile nationally (unusually high) and the 99.3rd among peers, against a peer median of 1.3%, so they are unusually high among its peers too.

Overall, 21 of the bank's ratios were in the national top or bottom 10%, and 19 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 33.9% | 100.0th (unusually high) | 0.1% | 99.8th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 519.1% | 100.0th (unusually high) | 2.2% | 99.8th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -228.8% | 0.0th (unusually low) | 10.2% | 0.2nd | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 49.8% | 100.0th (unusually high) | 0.4% | 99.8th | unusually high among its peers too |
| the total risk-based capital ratio | 4.5% | 0.1st (unusually low) | 20.4% | 0.5th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 3.2% | 0.1st (unusually low) | 19.4% | 0.5th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 5.2% | 99.8th (unusually high) | 0.0% | 99.8th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 7.1% | 99.7th (unusually high) | 1.3% | 99.3rd | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 0.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -100.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is treated as an open watchlist case, meaning it was flagged by the model and our data records no failure. The fact sheet contains no hindsight data after the as-of quarter, so this section cannot say anything more about how the bank fared.

## What happened next

In hindsight: no later ranks, watchlist flags or reporting status after the as-of quarter are included in the fact sheet. Whether the bank continues to report, and how its rank changes, will only be known once newer quarterly data is added.

## Sources

- F1 · Bank name · n/a · Lamont Bank Of St John · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 49.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 33.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 519.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -6.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 91.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 87.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -15.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.2%; contribution to the score · 2026-06-30 · +1.776 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -228.8%; contribution to the score · 2026-06-30 · +1.190 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 519.1%; contribution to the score · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 49.8%; contribution to the score · 2026-06-30 · +0.505 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.5%; contribution to the score · 2026-06-30 · +0.445 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.7%; contribution to the score · 2026-06-30 · -0.193 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the efficiency ratio (operating costs as a share of revenue), value 165.5%; contribution to the score · 2026-06-30 · -0.149 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.146 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.124 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: securities as a share of assets, value 25.9%; contribution to the score · 2026-06-30 · -0.115 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F85 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -228.8% · data/features/fct_bank_features.parquet: return_on_equity
- F86 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -39.3% · data/features/fct_bank_features.parquet: return_on_equity
- F87 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 18.1% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +1.190 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 33.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F92 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F93 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 11.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F96 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.050 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F97 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 165.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 54.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 92.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.149 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F104 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 49.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F106 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 21.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F109 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.505 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F110 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 519.1% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 5.6% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 245.1% · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F122 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · +0.085 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F124 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.7% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 33.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F136 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F137 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F138 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F139 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 519.1% · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -228.8% · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 49.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F155 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F156 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F157 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F158 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F160 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 20.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 19.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F171 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F172 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F173 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F174 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F175 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F176 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F177 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: allowance_to_loans
- F178 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F179 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: allowance_to_loans
- F180 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F181 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 21 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2026-06-30 · 19 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
