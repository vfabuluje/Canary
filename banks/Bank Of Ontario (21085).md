---
cert: 21085
name: "Bank Of Ontario"
as_of: 2026-06-30
rank: 23
n_banks: 4313
percentile: 99.4899142128449
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of Ontario (cert 21085)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Bank Of Ontario, a small bank in Wisconsin with $79.0 million in total assets, ranked 23 out of 4,313 banks on Canary's risk score, the 99.5th percentile, which puts it on the watchlist. The high rank comes mainly from troubled loans: loans 90+ days past due or no longer paying interest were 8.5% of loans against a national median of 0.5%, and its Texas ratio (troubled assets measured against capital plus reserves) was 44.6% against a median of 2.9%. Its capital and profits point the other way: equity was 14.0% of assets against a median of 10.6%, and return on assets matched the median at 1.2%.

## Warning signs in the data

Credit quality is the clear weak spot as of 2026-06-30. Loans 90+ days past due or not accruing interest (no longer paying) were 8.5% of loans, far above the national median of 0.5%, and nonaccrual assets plus foreclosed property were 7.1% of assets against a median of 0.3%. Earlier-stage late loans, 30-89 days past due, were 2.6% of assets against a median of 0.2%, and the Texas ratio stood at 44.6% against 2.9%. The bank was setting money aside for bad loans at a high pace, with provisions of 0.9% of assets against a median of 0.1%, and its loan-loss reserves (the cushion for bad loans) were 2.3% of loans against 1.2%. Actual losses so far were small: net write-offs were -0.1% of loans, near the median of 0.0%, meaning recoveries slightly exceeded write-offs.

Capital looks strong rather than weak: equity was 14.0% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 13.9% against 11.0%. Bond losses are modest: unrealized losses on bonds available for sale were 1.3% of equity against a median of 5.6%, and losses on bonds held to maturity were 0.0%, the same as the median. The separate real-estate screen found the bank did not cross either regulatory line.

On funding, the bank lends out more of its deposits than most, with loans at 94.8% of deposits against a median of 80.2%, and it held less cash, at 2.2% of assets against 6.2%. Brokered deposits (funds placed through middlemen) were 8.6% of deposits against a median of 0.0%, while uninsured deposits were only 8.0% against a median of 24.8%. The bank was also shrinking, with assets down -3.4% and deposits down -2.1% over the past four quarters, while the medians grew 4.5% and 4.2%.

## Understanding the score

As of 2026-06-30, Bank Of Ontario ranked 23 out of 4,313 banks, the 99.5th percentile on a 0 to 100 scale where higher means riskier, with a raw score of 0.2748. The watchlist covers the top 2% of banks by score, which was 87 banks that quarter, and this bank was flagged.

The five factors that pushed the score up most were the Texas ratio at 44.6%, adding +1.001; loans 90+ days past due or not accruing at 8.5% of loans, adding +0.979; loans 30-89 days past due at 2.6% of assets, adding +0.334; loan-loss provisions at 0.9% of assets, adding +0.114; and loan-loss reserves at 2.3% of loans, adding +0.092.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio (core capital against risk-weighted assets), at -0.626; return on equity (profit as a share of the owners' stake) at 8.5%, at -0.575; the leverage ratio at 13.9%, at -0.420; return on assets at 1.2%, at -0.393; and the total risk-based capital ratio, at -0.249. In short, strong capital and steady profits offset part of the weight from troubled loans, but not enough to move the bank off the watchlist.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 280 | 4,589 |  |
| 2024-12-31 | 539 | 4,560 |  |
| 2025-03-31 | 588 | 4,536 |  |
| 2025-06-30 | 354 | 4,494 |  |
| 2025-09-30 | 67 | 4,452 | ▲ watchlist |
| 2025-12-31 | 87 | 4,411 | ▲ watchlist |
| 2026-03-31 | 29 | 4,353 | ▲ watchlist |
| 2026-06-30 | 23 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Bank Of Ontario ranked 23 out of 4,313 banks nationally, placing it in the 99.5th percentile, where higher means riskier. A year earlier it sat in the 92.1st percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date figures. Of 28 ratios checked this way, 12 were outside their own prior range, and the 6 furthest outside are discussed here.

Provisions for loan losses (money set aside for loans expected to go bad) were 0.9% of assets on an annualized basis, above the prior range of 0.1% to 0.6%, and added +0.114 model log-odds units, which pushed the score up. Loan-loss reserves (the cushion held against bad loans) reached 2.3% of loans, above the prior range of 1.6% to 2.1%, and added +0.092 model log-odds units, which pushed the score up. Securities (bonds and similar investments) rose to 7.8% of assets, just above the prior range of 6.0% to 7.6%, yet at -0.033 model log-odds units this had little effect on the score.

Return on equity (profit as a share of the owners' stake) fell to 8.5%, below its prior range of 10.0% to 21.7%, but the model still pushed the score down with it, at -0.575 model log-odds units. Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) dropped to 0.0% of assets, below the prior range of 1.2% to 8.3%, yet at +0.014 model log-odds units this had little effect on the score. Net loan write-offs (loans written off as lost, minus recoveries) were -0.1% of loans on an annualized basis, below the prior range of 0.0% to 0.5%, and at +0.025 model log-odds units this too had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 0.9% | 0.1% to 0.6% | same quarter, prior 3 years | n/a | +0.3 pp | +0.114 | pushed the score up |
| loan-loss reserves as a share of loans | 2.3% | 1.6% to 2.1% | prior 12 quarters | +0.3 pp | +0.3 pp | +0.092 | pushed the score up |
| Federal Home Loan Bank borrowings as a share of assets | 0.0% | 1.2% to 8.3% | prior 12 quarters | -1.2 pp | -2.4 pp | +0.014 | little effect on the score |
| annualized loan write-offs, net of recoveries, as a share of loans | -0.1% | 0.0% to 0.5% | same quarter, prior 3 years | n/a | -0.6 pp | +0.025 | little effect on the score |
| return on equity (profit as a share of equity) | 8.5% | 10.0% to 21.7% | same quarter, prior 3 years | n/a | -1.5 pp | -0.575 | pushed the score down |
| securities as a share of assets | 7.8% | 6.0% to 7.6% | prior 12 quarters | +0.4 pp | +0.7 pp | -0.033 | little effect on the score |

12 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 227 banks in the same specialty group and size tier (under $100 million).

Nonaccrual assets and foreclosed property (loans that have stopped paying interest, plus property the bank has taken back) equal 7.1% of assets, which puts the bank at the 99.8th percentile nationally, unusually high, and at the 99.3rd percentile among its peers against a peer median of 0.1%, unusually high among its peers too. Loans 90+ days past due or not accruing interest make up 8.5% of loans, the 99.3rd percentile nationally and unusually high, and the 97.6th percentile among peers against a peer median of 0.4%, unusually high among its peers too. The Texas ratio, which weighs troubled assets against capital plus reserves, stands at 44.6%, the 99.2nd percentile nationally and unusually high, and the 97.6th percentile among peers against a peer median of 2.2%, unusually high among its peers too. Loans 30-89 days past due, an earlier stage of late payment, equal 2.6% of assets, the 98.1st percentile nationally and unusually high, and the 98.0th percentile among peers against a peer median of 0.2%, unusually high among its peers too.

The annualized provision for loan losses (money set aside this period for expected bad loans) is 0.9% of assets, the 98.1st percentile nationally and unusually high, and the 97.6th percentile among peers against a peer median of 0.0%, unusually high among its peers too. Loan-loss reserves (the cushion already held for bad loans) are 2.3% of loans, the 94.5th percentile nationally and unusually high, and the 82.6th percentile among peers against a peer median of 1.3%, typical for its peer group. Annualized loan write-offs net of recoveries are -0.1% of loans, meaning recoveries slightly exceeded write-offs, which is the 2.1st percentile nationally and unusually low, and the 6.8th percentile among peers against a peer median of 0.0%, unusually low among its peers too. Uninsured deposits (balances above the FDIC insurance limit) are 8.0% of deposits, the 5.0th percentile nationally and unusually low, and the 9.5th percentile among peers against a peer median of 16.2%, unusually low among its peers too.

Overall, 11 of the bank's ratios sit in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 7.1% | 99.8th (unusually high) | 0.1% | 99.3rd | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 8.5% | 99.3rd (unusually high) | 0.4% | 97.6th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 44.6% | 99.2nd (unusually high) | 2.2% | 97.6th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 0.9% | 98.1st (unusually high) | 0.0% | 97.6th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 2.6% | 98.1st (unusually high) | 0.2% | 98.0th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | -0.1% | 2.1st (unusually low) | 0.0% | 6.8th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 8.0% | 5.0th (unusually low) | 16.2% | 9.5th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 2.3% | 94.5th (unusually high) | 1.3% | 82.6th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.6% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 0.6% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -93.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

With hindsight: this bank is an open watchlist case, meaning the model flagged it and no later outcome is recorded in the data behind this note. The fact sheet contains no information from after the as-of quarter, so this section cannot say whether the troubled loans improved or worsened. Its place on the watchlist rests on the as-of picture described above, not on any later event.

## What happened next

With hindsight: no later quarters are included in the fact sheet, so there are no later ranks, watchlist flags or reporting status to show yet. The score history table added by code shows whatever later data becomes available.

## Sources

- F1 · Bank name · n/a · Bank Of Ontario · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.2748 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 23 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 14.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 44.6% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 94.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: total assets · 2026-06-30 · $79.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F67 · Bank: asset growth over the past four quarters · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F68 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -2.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 44.6%; contribution to the score · 2026-06-30 · +1.001 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 8.5%; contribution to the score · 2026-06-30 · +0.979 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: loans 30-89 days past due, as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · +0.334 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F74 · Driver up #4: annualized provision for loan losses as a share of assets, value 0.9%; contribution to the score · 2026-06-30 · +0.114 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F75 · Driver up #5: loan-loss reserves as a share of loans, value 2.3%; contribution to the score · 2026-06-30 · +0.092 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.626 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 8.5%; contribution to the score · 2026-06-30 · -0.575 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 13.9%; contribution to the score · 2026-06-30 · -0.420 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver down #4: return on assets (profit as a share of assets), value 1.2%; contribution to the score · 2026-06-30 · -0.393 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #5: the total risk-based capital ratio; contribution to the score · 2026-06-30 · -0.249 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F81 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F82 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F83 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F85 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.114 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F86 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F87 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F88 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F89 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F92 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.092 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F93 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F94 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F95 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F96 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F99 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.014 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F100 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F105 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.025 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F107 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 10.0% · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F111 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.575 · data/analyst/scores.parquet: feature return_on_equity contribution
- F112 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F113 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F114 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F115 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 7.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F118 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F119 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature securities_to_assets contribution
- F120 · Trend: ratios outside their own prior range · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F122 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F123 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F125 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 92.1% · data/analyst/scores.parquet: percentile
- F126 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F130 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F136 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F137 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F138 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F139 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F140 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F141 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 44.6% · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F155 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F156 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F157 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F159 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 6.8th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F165 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F166 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F167 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.0th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F168 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F169 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 9.5th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F170 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 16.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F171 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F172 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F173 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F174 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F175 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 82.6th · data/features/fct_bank_features.parquet: allowance_to_loans
- F176 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F177 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F179 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F180 · Peers: those ratios also unusual among peers · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F182 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
