---
cert: 33492
name: "Crescent Bank"
as_of: 2024-12-31
rank: 59
n_banks: 4560
percentile: 98.7280701754386
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:43"
writer_model: "claude-opus-5-5"
checked: true
---

# Crescent Bank (cert 33492)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2024-12-31, Crescent Bank, a Louisiana bank with $1.1 billion in assets, ranked 59 out of 4,560 banks on Canary's score, which places it in the 98.7th percentile and on the watchlist. Its clearest strains are in credit quality and funding costs: overdue loans, loan write-offs, money set aside for loan losses and interest expense were all far above the national median. Deposit growth over the past four quarters was -19.5%, against a national median of 3.9%. Its capital ratios were near or somewhat below the national median, and the model counted its capital as a point in the bank's favour.

## Warning signs in the data

Capital, the cushion that absorbs losses, was mixed: equity was 9.1% of assets against a national median of 9.7%, and the leverage ratio (core capital as a share of average assets) was 10.8% against 10.6%. The risk-based measures, which weight assets by riskiness, were below the median, with a Tier 1 ratio of 12.4% against 14.3% and a total ratio of 13.7% against 15.5%.

Credit quality stands out most: loans 30-89 days past due were 17.6% of assets against a national median of 0.2%, and loans 90+ days past due or not earning interest were 3.3% of loans against 0.4%. Net loan write-offs (loans recorded as losses, after recoveries) ran at an annualized 11.4% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 8.4% of assets against 0.1%. Offsetting this, loan-loss reserves were 11.2% of loans against a median of 1.2%, and the net interest margin (the spread earned on lending) was 14.0% against 3.4%. The bank still posted a return on assets of -0.2% against a median of 0.9%, and its Texas ratio (troubled assets against capital plus reserves) was 15.7% against 2.3%. Commercial real estate lending was small, at 1.9% of loans against a median of 23.2%, and the separate real-estate concentration check found it did not cross either line.

On funding, interest expense was an annualized 4.2% of assets against a median of 1.8%, and volatile funding (money that can leave quickly) was 18.3% of assets against 8.8%. Uninsured deposits, which are above the government guarantee limit, were low at 4.6% of deposits against 24.1%, while brokered deposits (placed through middlemen) were 3.6% against 0.0% and cash was 4.8% of assets against 6.1%. Unrealized losses on bonds available for sale were 10.0% of equity, slightly below the median of 11.2%, and losses on bonds held to maturity were 0.0% against 0.0%. The trend section notes that the sharp drop in deposits pushed the score down rather than up, so the raw figure and the model's reading of it point in different directions.

## Understanding the score

Crescent Bank ranked 59 out of 4,560 banks as of 2024-12-31, placing it in the 98.7th percentile on a 0 to 100 scale where higher means riskier. That put it on the watchlist, which covers the top 2% of banks, or 92 banks that quarter.

The five factors that pushed the score up most were interest expense at 4.2% of assets (+0.688), losses on bonds available for sale at 10.0% of equity (+0.673), and the provision for loan losses at 8.4% of assets (+0.562). The other two were the efficiency ratio (operating costs as a share of revenue) at 45.3% (+0.290) and commercial real estate loans at 1.9% of loans (+0.147).

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 12.4% (-1.220), deposit growth over the past four quarters at -19.5% (-0.403), and the Texas ratio at 15.7% (-0.402). The other two were return on equity at -2.8% (-0.363) and the leverage ratio at 10.8% (-0.261). Some of these, such as shrinking deposits and a loss, look weak on their own but lowered the score here, reflecting patterns the model learned rather than a simple good-or-bad reading.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 6 | 4,740 | ▲ watchlist |
| 2023-06-30 | 11 | 4,714 | ▲ watchlist |
| 2023-09-30 | 21 | 4,686 | ▲ watchlist |
| 2023-12-31 | 55 | 4,658 | ▲ watchlist |
| 2024-03-31 | 64 | 4,640 | ▲ watchlist |
| 2024-06-30 | 59 | 4,610 | ▲ watchlist |
| 2024-09-30 | 44 | 4,589 | ▲ watchlist |
| 2024-12-31 | 59 | 4,560 | ▲ watchlist |

## How its ratios moved

Crescent Bank ranked 59 out of 4,560 banks nationally, which puts it in the 98.7th percentile on a scale where higher means riskier. A year earlier it sat at the 98.8th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own prior range, mostly over the prior 12 quarters, and 8 of the 30 ratios checked sat outside that range.

Interest expense, meaning what the bank pays on deposits and borrowings, was 4.2% of assets on an annualized basis, above its prior range of 1.2% to 3.1%, and it pushed the score up with a contribution of +0.688 model log-odds units. Loans 30-89 days past due, meaning borrowers who are behind on payments, reached 17.6% of assets, above their prior range of 9.4% to 15.9%, and this ratio pushed the score up with a contribution of +0.147 model log-odds units. Net loan write-offs, meaning loans recorded as losses after any recoveries, were 11.4% of loans on an annualized basis, well above their prior range of 3.5% to 8.8%, yet this ratio had little effect on the score, contributing -0.023 model log-odds units. Loans 90+ days past due or no longer earning interest were 3.3% of loans, just above their prior range of 2.0% to 3.2%, but this ratio also had little effect on the score, contributing +0.017 model log-odds units.

Brokered deposits, meaning money placed at the bank through middlemen, were 3.6% of deposits, slightly above their prior range of 0.9% to 3.3%, yet this ratio pushed the score down with a contribution of -0.155 model log-odds units. Deposit growth over the past four quarters was -19.5%, below its prior range of -14.7% to 51.3%, but the model still pushed the score down on this ratio, with a contribution of -0.403 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 4.2% | 1.2% to 3.1% | same quarter, prior 3 years | n/a | +1.1 pp | +0.688 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 11.4% | 3.5% to 8.8% | same quarter, prior 3 years | n/a | +2.6 pp | -0.023 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 17.6% | 9.4% to 15.9% | prior 12 quarters | +1.7 pp | +2.8 pp | +0.147 | pushed the score up |
| brokered deposits as a share of deposits | 3.6% | 0.9% to 3.3% | prior 12 quarters | +0.3 pp | +0.7 pp | -0.155 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 3.3% | 2.0% to 3.2% | prior 12 quarters | +0.4 pp | +0.1 pp | +0.017 | little effect on the score |
| deposit growth over the past four quarters | -19.5% | -14.7% to 51.3% | prior 12 quarters | -4.8 pp | -21.7 pp | -0.403 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2024-12-31: Consumer Lending Specialization.

Peers: 40 banks in the same specialty group (all sizes), because fewer than 15 shared its size tier.

Crescent Bank ranks 59 out of 4,560 banks nationally on Canary's score, which places it in the 98.7th percentile, and it is on the watchlist. Loans 30-89 days past due (borrowers behind on payments) equal 17.6% of assets, at the 100.0th percentile nationally, which is unusually high; at the 98.8th percentile among peers, against a peer median of 0.7%, this is unusually high among its peers too. The provision for loan losses (money set aside to cover expected bad loans) runs at an annualized 8.4% of assets, at the 99.9th percentile nationally, which is unusually high; at the 96.2nd percentile among peers, against a peer median of 0.1%, it is unusually high among its peers too. Net write-offs (loans written off as uncollectable, minus later recoveries) run at an annualized 11.4% of loans, at the 99.9th percentile nationally, which is unusually high; at the 98.8th percentile among peers, against a peer median of 0.2%, they are unusually high among its peers too. Loan-loss reserves (a cushion held against future loan losses) equal 11.2% of loans, at the 99.9th percentile nationally, which is unusually high; at the 98.8th percentile among peers, against a peer median of 1.0%, they are unusually high among its peers too.

The net interest margin (the spread earned on lending and investing) is 14.0%, at the 99.8th percentile nationally, which is unusually high; at the 96.2nd percentile among peers, against a peer median of 3.8%, it is unusually high among its peers too. Interest expense (what the bank pays to borrow, including on deposits) equals an annualized 4.2% of assets, at the 99.7th percentile nationally, which is unusually high; at the 98.8th percentile among peers, against a peer median of 2.1%, it is unusually high among its peers too. Deposits changed by -19.5% over the past four quarters, at the 0.5th percentile nationally, which is unusually low; at the 3.8th percentile among peers, against a peer median of 6.0%, this is unusually low among its peers too. Total assets changed by -18.2% over the past four quarters, at the 0.5th percentile nationally, which is unusually low; at the 3.8th percentile among peers, against a peer median of 2.9%, this is unusually low among its peers too.

Overall, 18 of the bank's ratios sit in the national top or bottom 10%, and 12 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 17.6% | 100.0th (unusually high) | 0.7% | 98.8th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 8.4% | 99.9th (unusually high) | 0.1% | 96.2nd | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 11.4% | 99.9th (unusually high) | 0.2% | 98.8th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 11.2% | 99.9th (unusually high) | 1.0% | 98.8th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 14.0% | 99.8th (unusually high) | 3.8% | 96.2nd | unusually high among its peers too |
| annualized interest expense as a share of assets | 4.2% | 99.7th (unusually high) | 2.1% | 98.8th | unusually high among its peers too |
| deposit growth over the past four quarters | -19.5% | 0.5th (unusually low) | 6.0% | 3.8th | unusually low among its peers too |
| asset growth over the past four quarters | -18.2% | 0.5th (unusually low) | 2.9% | 3.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 8.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 16.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

In hindsight, this flag was a false alarm: the bank was on the watchlist as of 2024-12-31, mainly because of very high funding costs, bond losses and loan-loss provisions. In the following quarters it dropped off the watchlist, ranking 240 at 2025-03-31 and 244 at 2025-06-30, both not flagged. By 2026-06-30 it ranked 4,037, not flagged, and it was still reporting, so the data show no sign of the failure the flag warned about.

## What happened next

With hindsight, the bank's later ranks were 240 at 2025-03-31, 244 at 2025-06-30, 299 at 2025-09-30 and 145 at 2025-12-31, none of them flagged. Its rank then fell sharply to 3,355 at 2026-03-31 and 4,037 at 2026-06-30, also not flagged. The bank was still filing reports as of 2026-06-30, the latest quarter in our data.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2025-03-31 | 240 | 4,536 |  |
| 2025-06-30 | 244 | 4,494 |  |
| 2025-09-30 | 299 | 4,452 |  |
| 2025-12-31 | 145 | 4,411 |  |
| 2026-03-31 | 3,355 | 4,353 |  |
| 2026-06-30 | 4,037 | 4,313 |  |

## Sources

- F3 · As-of quarter · 2024-12-31 · 2024-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2024-12-31 · 59 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-12-31 · 4,560 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-12-31 · 98.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-12-31 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-12-31 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-12-31 · 9.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-12-31 · 12.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-12-31 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2024-12-31 · 13.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2024-12-31 · 15.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2024-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2024-12-31 · 8.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2024-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2024-12-31 · 1.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2024-12-31 · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-12-31 · 15.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-12-31 · 2.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-12-31 · -0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 14.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2024-12-31 · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-12-31 · 4.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-12-31 · 24.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2024-12-31 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2024-12-31 · 18.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2024-12-31 · 8.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2024-12-31 · 4.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2024-12-31 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-12-31 · 10.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2024-12-31 · $1.1 billion · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2024-12-31 · 3.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: annualized interest expense as a share of assets, value 4.2%; contribution to the score · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 10.0%; contribution to the score · 2024-12-31 · +0.673 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized provision for loan losses as a share of assets, value 8.4%; contribution to the score · 2024-12-31 · +0.562 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 45.3%; contribution to the score · 2024-12-31 · +0.290 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 1.9%; contribution to the score · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 12.4%; contribution to the score · 2024-12-31 · -1.220 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -19.5%; contribution to the score · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 15.7%; contribution to the score · 2024-12-31 · -0.402 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value -2.8%; contribution to the score · 2024-12-31 · -0.363 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 10.8%; contribution to the score · 2024-12-31 · -0.261 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F85 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 240 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 244 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 299 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 145 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 3,355 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 4,037 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F105 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · -0.023 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F108 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F109 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 15.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F112 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F113 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2024-12-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F114 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2024-12-31 · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F119 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2024-12-31 · -0.155 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F120 · Trend: brokered deposits as a share of deposits, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F121 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F122 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F126 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2024-12-31 · +0.017 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F127 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2024-12-31 · little effect on the score · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F128 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F129 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -14.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 51.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F133 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F134 · Trend: deposit growth over the past four quarters, what the model did with it · 2024-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: ratios outside their own prior range · 2024-12-31 · 8 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2024-12-31 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2023-12-31 · 98.8% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2024-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F145 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F146 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F147 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F148 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F149 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2024-12-31 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F150 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F151 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2024-12-31 · 8.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 96.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F155 · Peers: annualized provision for loan losses as a share of assets, peer median · 2024-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F164 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.9th · data/features/fct_bank_features.parquet: allowance_to_loans
- F165 · Peers: loan-loss reserves as a share of loans, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F166 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F167 · Peers: loan-loss reserves as a share of loans, peer median · 2024-12-31 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F168 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2024-12-31 · 14.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F170 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2024-12-31 · 99.8th · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: net_interest_margin
- F172 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2024-12-31 · 96.2nd · data/features/fct_bank_features.parquet: net_interest_margin
- F173 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2024-12-31 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F174 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F175 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F176 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2024-12-31 · 99.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F177 · Peers: annualized interest expense as a share of assets, national reading · 2024-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F178 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2024-12-31 · 98.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F179 · Peers: annualized interest expense as a share of assets, peer median · 2024-12-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F180 · Peers: annualized interest expense as a share of assets, reading against its peers · 2024-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F181 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F182 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2024-12-31 · 0.5th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F183 · Peers: deposit growth over the past four quarters, national reading · 2024-12-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F184 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2024-12-31 · 3.8th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F185 · Peers: deposit growth over the past four quarters, peer median · 2024-12-31 · 6.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F186 · Peers: deposit growth over the past four quarters, reading against its peers · 2024-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F187 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2024-12-31 · -18.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F188 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2024-12-31 · 0.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: asset growth over the past four quarters, national reading · 2024-12-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F190 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2024-12-31 · 3.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F191 · Peers: asset growth over the past four quarters, peer median · 2024-12-31 · 2.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, reading against its peers · 2024-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: ratios in the national top or bottom 10% · 2024-12-31 · 18 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2024-12-31 · 12 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2024-12-31 · 10% · data/features/fct_bank_features.parquet
