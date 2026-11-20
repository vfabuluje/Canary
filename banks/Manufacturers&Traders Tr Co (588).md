---
cert: 588
name: "Manufacturers&Traders Tr Co"
as_of: 2026-06-30
rank: 3371
n_banks: 4313
percentile: 21.864131694875955
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Manufacturers&Traders Tr Co (cert 588)

## Summary

As of 2026-06-30, Manufacturers&Traders Tr Co, a New York bank, ranks 3,371 out of 4,313 banks nationally on Canary's model score, which puts it at the 21.9th percentile on a scale where higher means riskier. It is not on the watchlist, which holds the 2% of banks with the highest scores. The model rated it somewhat riskier than a year earlier, when it sat at the 12.4th percentile. Its capital ratios and problem-loan levels look weaker than the national median, and its share of uninsured deposits is high, but its problem-loan ratios have moved below their own recent lows.

## Warning signs in the data

Capital (the bank's own cushion against losses) is mixed: equity was 12.9% of assets, above the national median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 9.5% against a median of 11.0%. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by riskiness) was 11.8% against a median of 14.6%, and the total risk-based capital ratio was 13.9% against 15.8%, both below the national middle.

Credit quality is weaker than the typical bank: loans 90 or more days past due or not accruing interest were 1.4% of loans against a national median of 0.5%. Loans in the earlier stage of lateness, past due but not yet seriously late, were 0.7% of assets against a national median of 0.2%. Nonaccrual assets and foreclosed property were 0.6% of assets against a median of 0.3%, net loan write-offs ran at 0.3% of loans against 0.0%, and the Texas ratio (troubled assets against capital plus reserves) was 6.4% against 2.9%. These two views point different ways: against other banks these figures are high, but the trend section shows the bank's own problem-loan ratios have fallen below their past lows.

On funding, uninsured deposits (money above the government insurance limit) were 48.9% of deposits, well above the national median of 24.8%, though the peer section finds this typical for large commercial lenders. Brokered deposits were 4.3% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 2.1% of assets against 0.2%, while volatile funding was a low 3.5% of assets against 9.0% and cash was 7.9% of assets against 6.2%. Unrealized losses on bonds held to maturity were 2.8% of equity against a median of 0.0%, while losses on bonds available for sale were 0.4% of equity, well below the median of 5.6%.

## Understanding the score

The bank ranks 3,371 out of 4,313 banks for 2026-06-30, the 21.9th percentile on a 0 to 100 scale where higher means riskier. It was not flagged for the watchlist, which covers the top 2% of scores and held 87 banks that quarter.

Three measures pushed the score up: the efficiency ratio (operating costs as a share of revenue) at 53.6%, contributing +0.132; losses on bonds available for sale at 0.4% of equity, contributing +0.037; and net loan write-offs at 0.3% of loans, contributing +0.001.

The five largest measures pushing the score down were the Tier 1 risk-based capital ratio at 11.8%, contributing -0.927, and the Texas ratio at 6.4%, contributing -0.839. Return on equity (profit as a share of equity) at 10.7% contributed -0.626, annualized interest expense at 1.4% of assets contributed -0.361, and loans 90 or more days past due or not accruing interest at 1.4% of loans contributed -0.313. Overall, the downward pushes are much larger than the upward ones, which is why the bank sits in the lower part of the national ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3,518 | 4,589 |  |
| 2024-12-31 | 3,472 | 4,560 |  |
| 2025-03-31 | 4,020 | 4,536 |  |
| 2025-06-30 | 3,938 | 4,494 |  |
| 2025-09-30 | 3,960 | 4,452 |  |
| 2025-12-31 | 3,784 | 4,411 |  |
| 2026-03-31 | 3,640 | 4,353 |  |
| 2026-06-30 | 3,371 | 4,313 |  |

## How its ratios moved

Manufacturers&Traders Tr Co ranks 3,371 out of 4,313 banks nationally, which puts it at the 21.9th percentile on a scale where higher means riskier. A year earlier it sat at the 12.4th percentile, so the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, usually the prior 12 quarters, 6 fell outside that range, and the 6 shown here all sit below their past lows.

Brokered deposits (money placed with the bank through outside brokers) were 4.3% of deposits, below their prior range of 5.4% to 8.3%, and contributed -0.159 model log-odds units, which pushed the score down. Loan write-offs net of recoveries (loans given up as lost, minus money later recovered) ran at an annualized 0.26% of loans, below their prior range of 0.30% to 0.4%, and contributed +0.001 units, which had little effect on the score. Loans 90 or more days past due or no longer accruing interest were 1.35% of loans, below their prior range of 1.38% to 2.2%, and contributed -0.313 units, which pushed the score down. Nonaccrual assets and foreclosed property (troubled loans and repossessed real estate) were 0.56% of assets, below their prior range of 0.59% to 1.2%, and contributed -0.274 units, which pushed the score down. Construction loans were 2.3% of loans, below their prior range of 2.4% to 5.9%, and contributed -0.226 units, which pushed the score down. The annualized provision for loan losses (money set aside to cover expected bad loans) was 0.238% of assets, below its prior range of 0.242% to 0.3%, and contributed -0.066 units, which pushed the score down.

So while every one of these ratios is outside its own prior range, each moved to the low side, and the model pushed the score down for five of them and gave the write-off ratio little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| brokered deposits as a share of deposits | 4.3% | 5.4% to 8.3% | prior 12 quarters | -1.1 pp | -2.0 pp | -0.159 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.26% | 0.30% to 0.4% | same quarter, prior 3 years | n/a | -0.1 pp | +0.001 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 1.35% | 1.38% to 2.2% | prior 12 quarters | -0.1 pp | -0.2 pp | -0.313 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 0.56% | 0.59% to 1.2% | prior 12 quarters | -0.03 pp | -0.2 pp | -0.274 | pushed the score down |
| construction loans as a share of loans | 2.3% | 2.4% to 5.9% | prior 12 quarters | -0.1 pp | -1.0 pp | -0.226 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.238% | 0.242% to 0.3% | same quarter, prior 3 years | n/a | +0.00 pp | -0.066 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

As of 2026-06-30, the bank ranked 3,371 out of 4,313 banks nationally, which puts it at the 21.9th percentile on a scale where higher means a higher model score. Uninsured deposits (money held above the government deposit insurance limit) made up 48.9% of the bank's deposits, which sits at the 93.5th percentile nationally and is unusually high across all banks. Against its 114 peers, the same ratio sits at the 77.4th percentile, compared with a peer median of 40.3%, which is typical for its peer group.

Overall, 1 of the bank's ratios falls in the national top or bottom 10%, and 0 of those are also unusual among its peers, so the one standout figure looks ordinary next to similar large commercial lenders.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 48.9% | 93.5th (unusually high) | 40.3% | 77.4th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 15.3% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 132.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -26.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks at hindsight, meaning data after the as-of quarter. The fact sheet for this memo contains no later ranks, watchlist flags or reporting status, so no later details can be given here. The outcome for this bank is classed as quiet, and the score history table added below shows any later quarters on record.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,371 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 21.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 12.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 48.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the efficiency ratio (operating costs as a share of revenue), value 53.6%; contribution to the score · 2026-06-30 · +0.132 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 0.4%; contribution to the score · 2026-06-30 · +0.037 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized loan write-offs, net of recoveries, as a share of loans, value 0.3%; contribution to the score · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F78 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.8%; contribution to the score · 2026-06-30 · -0.927 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 6.4%; contribution to the score · 2026-06-30 · -0.839 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #3: return on equity (profit as a share of equity), value 10.7%; contribution to the score · 2026-06-30 · -0.626 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #4: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · -0.361 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 1.4%; contribution to the score · 2026-06-30 · -0.313 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F87 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F88 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 5.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F89 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F92 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.159 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F93 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F94 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.26% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.30% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F98 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F100 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.35% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F101 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.38% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F102 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.313 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F106 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F107 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.56% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F108 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.59% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F109 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F112 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.274 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F113 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F114 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F115 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F116 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F119 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.226 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F120 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F121 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.238% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F122 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.242% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F123 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F125 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.066 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F126 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 12.4% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 48.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F138 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.5th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F139 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F140 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 77.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F141 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F142 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F143 · Peers: banks in the peer group (including this bank) · 2026-06-30 · 114 · data/raw/specialty/: SPECGRP
- F144 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 1 · data/features/fct_bank_features.parquet
- F145 · Peers: those ratios also unusual among peers · 2026-06-30 · 0 · data/features/fct_bank_features.parquet
- F147 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
