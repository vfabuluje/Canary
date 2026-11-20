---
cert: 18734
name: "Newtek Bank National Assn"
as_of: 2026-06-30
rank: 21
n_banks: 4313
percentile: 99.53628564804082
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Newtek Bank National Assn (cert 18734)

*Outcome not yet known.*

## Summary

As of June 30, 2026, Newtek Bank National Assn, a Florida bank, ranked 21 out of 4,313 banks on Canary's risk score, which places it in the 99.5th percentile and on the watchlist. The main concern is loan trouble: loans 90+ days past due or not accruing interest were 7.2% of loans against a national median of 0.5%, and the Texas ratio (troubled assets compared with capital plus reserves) was 58.5% against a national median of 2.9%. The data points in two directions, because the bank was also highly profitable, with a return on assets (profit as a share of assets) of 4.4% against a national median of 1.2%. A separate commercial real estate concentration check found that it did not cross either regulatory screening line.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thinner than at most banks: equity was 8.3% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.6% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also below the medians, with a Tier 1 ratio of 11.5% against 14.6% and a total ratio of 12.7% against 15.8%.

Credit quality, meaning how well borrowers are repaying, stands out most: loans 90+ days past due or not accruing interest were 7.2% of loans against a national median of 0.5%, and early-stage late loans (30-89 days past due) were 3.0% of assets against 0.2%. Nonaccrual assets and foreclosed property (loans no longer earning interest plus repossessed property) were 5.9% of assets against a median of 0.3%, and the Texas ratio was 58.5% against 2.9%. The bank was setting aside and writing off more than usual, with a provision for loan losses of 1.8% of assets against 0.1%, net write-offs of 1.3% of loans against 0.0%, and loan-loss reserves of 2.6% of loans against 1.2%. Commercial real estate loans made up 38.0% of its loans, well above the national median of 23.6%.

On funding, the bank grew very fast, with deposits up 91.9% and assets up 83.7% over the past four quarters against national medians of 4.2% and 4.5%, and its interest expense was 2.8% of assets against 1.6%. Other liquidity figures look steadier: uninsured deposits (balances above the insurance limit) were 19.1% of deposits against a median of 24.8%, and cash was 15.4% of assets against 6.2%. Bond losses were not a concern, as losses on bonds available for sale were 0.0% of equity against a national median of 5.6%, and securities were only 0.6% of assets against 17.6%.

## Understanding the score

As of June 30, 2026, the bank ranked 21 out of 4,313 banks, which puts it in the 99.5th percentile on a scale where higher means riskier. The watchlist covers the riskiest 2% of banks, which meant 87 banks that quarter, and this bank was flagged.

Five features pushed the score up the most: seriously late or nonaccruing loans at 7.2% of loans (+0.875), the Texas ratio at 58.5% (+0.530), interest expense at 2.8% of assets (+0.505), deposit growth over the past four quarters at 91.9% (+0.380), and early-stage late loans at 3.0% of assets (+0.295). Five features pulled it down the most: the Tier 1 risk-based capital ratio at 11.5% (-1.267), return on assets at 4.4% (-0.646), return on equity (profit as a share of the owners' stake) at 50.5% (-0.574), the total risk-based capital ratio at 12.7% (-0.447), and construction loans at 5.1% of loans (-0.413).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 483 | 4,589 |  |
| 2024-12-31 | 204 | 4,560 |  |
| 2025-03-31 | 81 | 4,536 | ▲ watchlist |
| 2025-06-30 | 52 | 4,494 | ▲ watchlist |
| 2025-09-30 | 73 | 4,452 | ▲ watchlist |
| 2025-12-31 | 101 | 4,411 |  |
| 2026-03-31 | 78 | 4,353 | ▲ watchlist |
| 2026-06-30 | 21 | 4,313 | ▲ watchlist |

## How its ratios moved

As of June 30, 2026, the model ranked Newtek Bank National Assn 21 out of 4,313 banks nationally, which places it in the 99.5th percentile, where higher means riskier. A year earlier, on June 30, 2025, it sat in the 98.9th percentile, so the model's rating is about the same as a year earlier. Each ratio is compared with its own values over the prior 12 quarters, and 10 of the 30 ratios checked fell outside that prior range; the 6 furthest outside are discussed here.

Loans 90+ days past due or not accruing interest (loans where the borrower has stopped paying normally) reached 7.2% of loans, above their prior range of 1.3% to 6.1%, and this ratio contributed +0.875 model log-odds units, which pushed the score up. The Texas ratio (troubled assets compared with capital plus reserves) rose to 58.5%, above its prior range of 3.7% to 43.0%, and contributed +0.530, which pushed the score up. That Texas ratio climbed +15.5 pp over one quarter and +30.3 pp over four quarters. Loans 30-89 days past due (early-stage late payments) stood at 3.0% of assets, above their prior range of 0.0% to 2.2%, and contributed +0.295, which pushed the score up. The efficiency ratio (operating costs as a share of revenue) fell to 38.7%, below its prior range of 45.9% to 71.5%, and contributed +0.234, which pushed the score up.

Return on equity (profit as a share of the owners' stake) rose to 50.5%, above its prior range of 12.8% to 40.7%, yet in contrast to the ratios above it contributed -0.574, which pushed the score down. Nonaccrual assets and foreclosed property (loans no longer earning interest plus repossessed property) reached 5.9% of assets, above their prior range of 0.6% to 5.1%, but despite being outside that range they contributed only -0.010, which had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 58.5% | 3.7% to 43.0% | prior 12 quarters | +15.5 pp | +30.3 pp | +0.530 | pushed the score up |
| return on equity (profit as a share of equity) | 50.5% | 12.8% to 40.7% | same quarter, prior 3 years | n/a | +24.1 pp | -0.574 | pushed the score down |
| loans 30-89 days past due, as a share of assets | 3.0% | 0.0% to 2.2% | prior 12 quarters | +1.5 pp | +1.0 pp | +0.295 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 38.7% | 45.9% to 71.5% | same quarter, prior 3 years | n/a | -9.7 pp | +0.234 | pushed the score up |
| loans 90+ days past due or not accruing interest, as a share of loans | 7.2% | 1.3% to 6.1% | prior 12 quarters | +1.6 pp | +2.3 pp | +0.875 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 5.9% | 0.6% to 5.1% | prior 12 quarters | +1.4 pp | +1.9 pp | -0.010 | little effect on the score |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 753 banks in the same specialty group and size tier ($1 billion to $10 billion).

As of 2026-06-30, the bank ranked 21 out of 4,313 banks nationally, placing it in the 99.5th percentile of Canary's score. Its Texas ratio, which compares troubled assets with capital plus reserves, was 58.5%, at the 99.6th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 3.7%, which is unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) plus foreclosed property made up 5.9% of assets, at the 99.5th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 7.2% of loans, at the 99.0th percentile nationally (unusually high), and at the 99.7th percentile among its peers against a peer median of 0.5%, which is unusually high among its peers too. Loans that were behind on payments but not yet seriously overdue were 3.0% of assets, at the 98.7th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 0.2%, which is unusually high among its peers too. The annualized provision for loan losses, money set aside to cover expected bad loans, was 1.8% of assets, at the 99.0th percentile nationally (unusually high), and at the 98.7th percentile among its peers against a peer median of 0.1%, which is unusually high among its peers too.

Return on equity, profit as a share of the owners' stake, was 50.5%, at the 99.4th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 11.8%, which is unusually high among its peers too. Asset growth over the past four quarters was 83.7%, at the 99.4th percentile nationally (unusually high), and at the 99.5th percentile among its peers against a peer median of 5.3%, which is unusually high among its peers too. Deposit growth over the past four quarters was 91.9%, at the 99.4th percentile nationally (unusually high), and at the 99.4th percentile among its peers against a peer median of 5.0%, which is unusually high among its peers too. Overall, 15 of the bank's ratios fall in the national top or bottom 10%, and 15 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 58.5% | 99.6th (unusually high) | 3.7% | 99.9th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.9% | 99.5th (unusually high) | 0.4% | 99.9th | unusually high among its peers too |
| return on equity (profit as a share of equity) | 50.5% | 99.4th (unusually high) | 11.8% | 99.9th | unusually high among its peers too |
| asset growth over the past four quarters | 83.7% | 99.4th (unusually high) | 5.3% | 99.5th | unusually high among its peers too |
| deposit growth over the past four quarters | 91.9% | 99.4th (unusually high) | 5.0% | 99.4th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 7.2% | 99.0th (unusually high) | 0.5% | 99.7th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 1.8% | 99.0th (unusually high) | 0.1% | 98.7th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 3.0% | 98.7th (unusually high) | 0.2% | 99.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 42.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 202.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 296.7% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this memo's outcome case is a bank that sits on the watchlist and remains open. The fact sheet contains no data from after the as-of quarter, so the reasons for that outcome cannot be explained with later figures here.

## What happened next

In hindsight, the fact sheet holds no later ranks, watchlist flags or reporting status for this bank. This memo therefore cannot say how the bank's rank moved after the as-of quarter or whether it kept reporting.

## Sources

- F1 · Bank name · n/a · Newtek Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · FL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 21 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 38.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 58.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 19.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · 83.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 91.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 7.2%; contribution to the score · 2026-06-30 · +0.875 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 58.5%; contribution to the score · 2026-06-30 · +0.530 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.505 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: deposit growth over the past four quarters, value 91.9%; contribution to the score · 2026-06-30 · +0.380 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F79 · Driver up #5: loans 30-89 days past due, as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.295 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.5%; contribution to the score · 2026-06-30 · -1.267 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on assets (profit as a share of assets), value 4.4%; contribution to the score · 2026-06-30 · -0.646 · data/analyst/scores.parquet: feature return_on_assets contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 50.5%; contribution to the score · 2026-06-30 · -0.574 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 12.7%; contribution to the score · 2026-06-30 · -0.447 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: construction loans as a share of loans, value 5.1%; contribution to the score · 2026-06-30 · -0.413 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 58.5% · data/features/fct_bank_features.parquet: texas_ratio
- F86 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F87 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 43.0% · data/features/fct_bank_features.parquet: texas_ratio
- F88 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +15.5 pp · data/features/fct_bank_features.parquet: texas_ratio
- F89 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +30.3 pp · data/features/fct_bank_features.parquet: texas_ratio
- F90 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.530 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F92 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 50.5% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 12.8% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 40.7% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.574 · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F99 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F100 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.295 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F104 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 38.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 45.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 71.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.234 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F112 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F113 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F116 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.875 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F117 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F118 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F119 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F120 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 5.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F125 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F128 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.9% · data/analyst/scores.parquet: percentile
- F131 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 58.5% · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 50.5% · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 83.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F154 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: asset_growth_4q
- F155 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F156 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F157 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F158 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F159 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 91.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F160 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: deposit_growth_4q
- F162 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F163 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F164 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F167 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F168 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F169 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F170 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F171 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F172 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F173 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F174 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F175 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F176 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F177 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F178 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F179 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F180 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F181 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F182 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F184 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F185 · Peers: those ratios also unusual among peers · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F187 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
