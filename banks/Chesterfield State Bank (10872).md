---
cert: 10872
name: "Chesterfield State Bank"
as_of: 2026-06-30
rank: 38
n_banks: 4313
percentile: 99.14212844887548
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:45"
writer_model: "claude-opus-5-5"
checked: true
---

# Chesterfield State Bank (cert 10872)

*Outcome not yet known.*

## Summary

Chesterfield State Bank, a small Illinois bank, ranked 38 of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.1st percentile, where higher means riskier, and it is flagged on the watchlist. The main concern is loan quality: loans 90 or more days late or no longer earning interest were 11.2% of loans, against a national median of 0.5%. Its funding looks steady, though, with uninsured deposits at only 4.4% of deposits and cash at 33.7% of assets, both far from typical in a reassuring direction.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, is thinner than at most banks: equity was 8.1% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.2% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also below the median, at 13.2% for Tier 1 against 14.6% and 14.5% in total against 15.8%.

Credit quality is the clearest weak spot: seriously late or non-earning loans were 11.2% of loans against a median of 0.5%, and loans 30-89 days late were 2.3% of assets against 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 78.7% against a national median of 2.9%, while reserves set aside for bad loans were 1.3% of loans, close to the 1.2% median. Net loan write-offs were -2.1% of loans and the provision for loan losses was -1.8% of assets, against medians of 0.0% and 0.1%, meaning recoveries outweighed write-offs and money was released from reserves rather than added. Those negative figures came alongside strong reported profit, with return on assets at 1.9% against 1.2%, yet operating costs ate 95.6% of revenue against a median of 62.1%, so the profit picture and the cost picture point different ways.

Funding and liquidity point the other way and look strong: uninsured deposits were 4.4% of deposits against 24.8%, core deposits (stable everyday deposits) were 87.9% of assets against 75.5%, and cash was 33.7% of assets against 6.2%. Unrealized losses on bonds available for sale were 3.4% of equity, below the 5.6% median, and the bank is very small, with total assets of $21.7 million against a median of $384.7 million, and shrinking, with assets down -4.8% over the past four quarters against median growth of 4.5%. The separate real-estate concentration check found the bank did not cross either supervisory line, so commercial property lending is not a concern here.

## Understanding the score

As of 2026-06-30 the bank ranked 38 of 4,313 banks, placing it in the 99.1st percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the riskiest 2% of banks, 87 banks that quarter, and this bank is flagged on it.

The five features pushing the score up most were seriously late or non-earning loans at 11.2% of loans (contribution +0.915), the Texas ratio at 78.7% (+0.587), small size with total assets of $21.7 million (+0.557), securities at only 2.7% of assets (+0.203), and loans 30-89 days late at 2.3% of assets (+0.190). The five features pulling it down most were the Tier 1 risk-based capital ratio at 13.2% (contribution -1.421), return on equity (profit as a share of the owners' stake) at 25.4% (-0.539), the total risk-based capital ratio at 14.5% (-0.458), interest expense at 1.5% of assets (-0.451), and return on assets at 1.9% (-0.340).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 126 | 4,589 |  |
| 2024-12-31 | 97 | 4,560 |  |
| 2025-03-31 | 53 | 4,536 | ▲ watchlist |
| 2025-06-30 | 60 | 4,494 | ▲ watchlist |
| 2025-09-30 | 81 | 4,452 | ▲ watchlist |
| 2025-12-31 | 13 | 4,411 | ▲ watchlist |
| 2026-03-31 | 23 | 4,353 | ▲ watchlist |
| 2026-06-30 | 38 | 4,313 | ▲ watchlist |

## How its ratios moved

This section compares each of the bank's financial ratios with its own history: for most ratios, the prior 12 quarters, and for year-to-date ratios, the same quarter in the prior 3 years. As of 2026-06-30, 7 of the 28 ratios checked sat outside their own prior range. The bank ranked 38 of 4,313 banks nationally, placing it in the 99.1st percentile, where higher means riskier. A year earlier, on 2025-06-30, it stood in the 98.7th percentile, and the model rates it about the same as a year earlier.

Return on equity, which is profit as a share of the owners' stake, was 25.4%, well above its prior range of 0.8% to 10.2%, yet this pushed the score down, with a contribution of -0.539 model log-odds units. That ratio rose by +19.4 pp over four quarters. Return on assets, which is profit as a share of total assets, was 1.9%, above its prior range of 0.1% to 1.0%, and it also pushed the score down, contributing -0.340 model log-odds units.

Net loan write-offs, meaning loans the bank gave up collecting minus any amounts recovered, ran at an annualized -2.1% of loans, outside a prior range of 0.0% to 0.0%, but this had little effect on the score, contributing -0.006 model log-odds units. The provision for loan losses, money set aside to cover expected bad loans, was an annualized -1.8% of assets, outside a prior range of 0.0% to 0.0%, and it likewise had little effect on the score, contributing -0.018 model log-odds units. Loans as a share of deposits fell to 67.3%, below its prior range of 73.2% to 90.8%, yet this had little effect on the score, contributing -0.041 model log-odds units. Cash as a share of assets rose to 33.7%, above its prior range of 8.4% to 27.5%, and this pushed the score up, contributing +0.102 model log-odds units. Much of that cash increase came recently, with a rise of +6.3 pp over one quarter.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | -2.1% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | -2.1 pp | -0.006 | little effect on the score |
| annualized provision for loan losses as a share of assets | -1.8% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | -1.8 pp | -0.018 | little effect on the score |
| return on equity (profit as a share of equity) | 25.4% | 0.8% to 10.2% | same quarter, prior 3 years | n/a | +19.4 pp | -0.539 | pushed the score down |
| return on assets (profit as a share of assets) | 1.9% | 0.1% to 1.0% | same quarter, prior 3 years | n/a | +1.4 pp | -0.340 | pushed the score down |
| loans as a share of deposits | 67.3% | 73.2% to 90.8% | prior 12 quarters | -5.9 pp | -8.6 pp | -0.041 | little effect on the score |
| cash as a share of assets | 33.7% | 8.4% to 27.5% | prior 12 quarters | +6.3 pp | +7.5 pp | +0.102 | pushed the score up |

7 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 227 banks in the same specialty group and size tier (under $100 million).

The provision for loan losses (money a bank sets aside to cover expected bad loans), annualized as a share of assets, was -1.8%, at the 0.1st percentile nationally, which is unusually low; it sat at the 0.2nd percentile among its peers against a peer median of 0.0%, which is unusually low among its peers too. Annualized loan write-offs net of recoveries (loans written off as uncollectable, minus money later recovered), as a share of loans, were -2.1%, at the 0.1st percentile nationally, which is unusually low; the bank was at the 0.2nd percentile among its peers against a peer median of 0.0%, which is unusually low among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 78.7%, at the 99.8th percentile nationally, which is unusually high; it was at the 98.9th percentile among its peers against a peer median of 2.2%, which is unusually high among its peers too. Loans 90 or more days past due or no longer earning interest made up 11.2% of loans, at the 99.6th percentile nationally, which is unusually high; this was the 98.9th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. Loans 30-89 days past due equaled 2.3% of assets, at the 97.6th percentile nationally, which is unusually high; among its peers this was the 96.3rd percentile against a peer median of 0.2%, which is unusually high among its peers too.

Uninsured deposits (balances above the government deposit insurance limit) were 4.4% of deposits, at the 1.6th percentile nationally, which is unusually low; among its peers this was the 2.9th percentile against a peer median of 16.2%, which is unusually low among its peers too. Core deposits (stable, everyday customer deposits) equaled 87.9% of assets, at the 97.2nd percentile nationally, which is unusually high; among its peers this was the 94.9th percentile against a peer median of 79.2%, which is unusually high among its peers too. Cash made up 33.7% of assets, at the 96.7th percentile nationally, which is unusually high; among its peers this was the 94.1st percentile against a peer median of 9.1%, which is unusually high among its peers too.

Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and 14 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -1.8% | 0.1st (unusually low) | 0.0% | 0.2nd | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | -2.1% | 0.1st (unusually low) | 0.0% | 0.2nd | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 78.7% | 99.8th (unusually high) | 2.2% | 98.9th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 11.2% | 99.6th (unusually high) | 0.4% | 98.9th | unusually high among its peers too |
| uninsured deposits as a share of deposits | 4.4% | 1.6th (unusually low) | 16.2% | 2.9th | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 2.3% | 97.6th (unusually high) | 0.2% | 96.3rd | unusually high among its peers too |
| core deposits as a share of assets | 87.9% | 97.2nd (unusually high) | 79.2% | 94.9th | unusually high among its peers too |
| cash as a share of assets | 33.7% | 96.7th (unusually high) | 9.1% | 94.1st | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 7.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -61.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank's case is classed as still open and on the watchlist, meaning it has not been recorded as failing. The fact sheet for this memo contains no data from after the as-of quarter, so it cannot explain the outcome beyond the warning signs already described.

## What happened next

In hindsight, no later ranks, watchlist flags or reporting status after the as-of quarter are included in the fact sheet for this memo. The score history table added by code shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Chesterfield State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 38 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · -2.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · -1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 78.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 95.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 33.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $21.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 11.2%; contribution to the score · 2026-06-30 · +0.915 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 78.7%; contribution to the score · 2026-06-30 · +0.587 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: total assets, value $21.7 million; contribution to the score · 2026-06-30 · +0.557 · data/analyst/scores.parquet: feature log_total_assets contribution
- F78 · Driver up #4: securities as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.203 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F79 · Driver up #5: loans 30-89 days past due, as a share of assets, value 2.3%; contribution to the score · 2026-06-30 · +0.190 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.2%; contribution to the score · 2026-06-30 · -1.421 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 25.4%; contribution to the score · 2026-06-30 · -0.539 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 14.5%; contribution to the score · 2026-06-30 · -0.458 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2026-06-30 · -0.451 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.9%; contribution to the score · 2026-06-30 · -0.340 · data/analyst/scores.parquet: feature return_on_assets contribution
- F85 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · -2.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F86 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F87 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.006 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F90 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F91 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · -1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F92 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F93 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F95 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.018 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F96 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F97 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 25.4% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 10.2% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · +19.4 pp · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.539 · data/analyst/scores.parquet: feature return_on_equity contribution
- F102 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F103 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F104 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.340 · data/analyst/scores.parquet: feature return_on_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F109 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 67.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F110 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 73.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F111 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 90.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F114 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.041 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F115 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F116 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 33.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F117 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F118 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 27.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F119 · Trend: cash as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +6.3 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F121 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.102 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F122 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cash_to_assets contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 7 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F127 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.7% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · -1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F134 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F135 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F136 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F137 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F138 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F139 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · -2.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F140 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F141 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F142 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F143 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F144 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 78.7% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F155 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F156 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F157 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F158 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F159 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F160 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 2.9th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F161 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 16.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F162 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F163 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F164 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F165 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F166 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.3rd · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F167 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F168 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F169 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F170 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F171 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F172 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 94.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F173 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 79.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F174 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: cash as a share of assets, bank value at the as-of quarter · 2026-06-30 · 33.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F176 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: cash_to_assets
- F177 · Peers: cash as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: cash_to_assets
- F178 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 94.1st · data/features/fct_bank_features.parquet: cash_to_assets
- F179 · Peers: cash as a share of assets, peer median · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F180 · Peers: cash as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: cash_to_assets
- F182 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F183 · Peers: those ratios also unusual among peers · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F185 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
