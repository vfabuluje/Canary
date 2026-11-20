---
cert: 57336
name: "Drake Bank"
as_of: 2026-06-30
rank: 15
n_banks: 4313
percentile: 99.67539995362856
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Drake Bank (cert 57336)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Drake Bank, a Minnesota bank, ranked 15 out of 4,313 banks nationally on Canary's risk score, placing it in the 99.7th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. The main pressures were thin capital (the owners' cushion that absorbs losses), a sharp rise in troubled loans, and losses on its earnings, alongside heavy use of brokered deposits (money placed through middlemen rather than gathered directly). Its commercial real estate lending did not cross either of the regulators' concentration screens, so that is not where the strain shows.

## Warning signs in the data

Capital was well below typical levels: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.3% against 11.0%. The risk-based measures, which weigh capital against the riskiness of what the bank holds, were also low, with a Tier 1 ratio of 9.8% against 14.6% and a total ratio of 11.1% against 15.8%.

Credit quality was the sharpest problem: loans 90 or more days past due or no longer earning interest were 4.5% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 5.4% of assets against a median of 0.3%, and the Texas ratio (troubled assets measured against capital plus reserves) was 57.8% against 2.9%. The bank set aside an annualized 2.2% of assets for expected loan losses against a median of 0.1%, and its loan-loss reserves stood at 3.0% of loans against 1.2%. Profit turned negative, with return on assets at -1.2% against a median of 1.2%. One point runs the other way: loans 30-89 days past due, an early sign of trouble, were 0.0% of assets, below the median of 0.2%.

On funding, brokered deposits made up 20.2% of deposits against a national median of 0.0%, and Federal Home Loan Bank borrowings were 6.9% of assets against 0.2%. Deposits shrank by -9.5% over the past four quarters while the median bank grew by 4.2%, though uninsured deposits, which can leave quickly in a scare, were a modest 14.2% of deposits against 24.8%, and cash was 9.2% of assets against 6.2%. Unrealized losses on bonds available for sale equaled 7.9% of equity, somewhat above the median of 5.6%, while losses on bonds held to maturity were 0.0%, in line with the median.

## Understanding the score

Drake Bank ranked 15 out of 4,313 banks at 2026-06-30, in the 99.7th percentile on a 0 to 100 scale where higher means riskier, with a raw model score of 0.5029. It was flagged for the watchlist, one of 87 banks that quarter, a list that covers the top 2% of banks by score.

Five features pushed the score up most: the Texas ratio at 57.8% contributed +0.781, and unrealized losses on bonds available for sale at 7.9% of equity contributed +0.580. Interest expense at 2.6% of assets added +0.444, brokered deposits at 20.2% of deposits added +0.320, and return on equity at -17.7% added +0.212.

Five features pulled the score down most: the Tier 1 risk-based capital ratio at 9.8% contributed -0.824, even though that ratio is low next to other banks. Loans 30-89 days past due at 0.0% of assets contributed -0.433, construction loans at 5.9% of loans contributed -0.380, total assets of $247.4 million contributed -0.208, and volatile funding at 5.7% of assets contributed -0.151.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,960 | 4,589 |  |
| 2024-12-31 | 895 | 4,560 |  |
| 2025-03-31 | 154 | 4,536 |  |
| 2025-06-30 | 357 | 4,494 |  |
| 2025-09-30 | 80 | 4,452 | ▲ watchlist |
| 2025-12-31 | 83 | 4,411 | ▲ watchlist |
| 2026-03-31 | 14 | 4,353 | ▲ watchlist |
| 2026-06-30 | 15 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Drake Bank ranked 15 out of 4,313 banks nationally, which places it in the 99.7th percentile on a scale where higher means riskier. On 2025-06-30 it sat in the 92.1st percentile, and the model rated it riskier than a year earlier. Of the 28 ratios compared with their own prior range, mostly the prior 12 quarters, 9 were outside that range at the as-of quarter.

The Texas ratio (troubled assets measured against capital plus reserves) reached 57.8%, above its prior range of 0.2% to 43.7% and up +41.8 pp over four quarters, and at +0.781 model log-odds units it pushed the score up. Return on equity (profit as a share of the owners' stake) fell to -17.7%, below its prior range of 5.9% to 13.2%, and at +0.212 it pushed the score up. Loans 90 or more days past due or no longer earning interest rose to 4.5% of loans, above their prior range of 0.0% to 3.2%, and at +0.165 this pushed the score up. The provision for loan losses (money set aside to cover expected bad loans) ran at 2.2% of assets, above its prior range of 0.0% to 0.6%, and at +0.125 it pushed the score up.

Return on assets was -1.2%, below its prior range of 0.4% to 1.0%, yet at -0.007 it had little effect on the score. Nonaccrual assets and foreclosed property (loans no longer earning interest plus repossessed real estate) reached 5.4% of assets, above their prior range of 0.0% to 3.4%, but at -0.005 they also had little effect on the score. So although both of these ratios moved outside their usual range, the model gave them almost no weight.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -17.7% | 5.9% to 13.2% | same quarter, prior 3 years | n/a | -31.0 pp | +0.212 | pushed the score up |
| return on assets (profit as a share of assets) | -1.2% | 0.4% to 1.0% | same quarter, prior 3 years | n/a | -2.2 pp | -0.007 | little effect on the score |
| annualized provision for loan losses as a share of assets | 2.2% | 0.0% to 0.6% | same quarter, prior 3 years | n/a | +1.6 pp | +0.125 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 5.4% | 0.0% to 3.4% | prior 12 quarters | +1.9 pp | +4.0 pp | -0.005 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 4.5% | 0.0% to 3.2% | prior 12 quarters | +2.3 pp | +2.8 pp | +0.165 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 57.8% | 0.2% to 43.7% | prior 12 quarters | +18.3 pp | +41.8 pp | +0.781 | pushed the score up |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

The Texas ratio, which weighs troubled loans and foreclosed property against the bank's capital plus reserves, was 57.8%, at the 99.6th national percentile and unusually high; at the 99.7th percentile among peers, against a peer median of 3.0%, it is unusually high among its peers too. The provision for loan losses, money set aside to cover expected bad loans, ran at an annualized 2.2% of assets, at the 99.2nd national percentile and unusually high; at the 99.3rd percentile among peers, against a peer median of 0.1%, it is unusually high among its peers too. Nonaccrual assets (loans no longer paying interest) plus foreclosed property came to 5.4% of assets, at the 99.2nd national percentile and unusually high; at the 99.0th percentile among peers, against a peer median of 0.3%, it is unusually high among its peers too.

Return on equity, profit as a share of the owners' stake, was -17.7%, at the 0.9th national percentile and unusually low; at the 0.5th percentile among peers, against a peer median of 11.7%, it is unusually low among its peers too. Return on assets, profit as a share of everything the bank owns, was -1.2%, at the 1.7th national percentile and unusually low; at the 1.0th percentile among peers, against a peer median of 1.2%, it is unusually low among its peers too. The Tier 1 risk-based capital ratio, a measure of core capital against the bank's loans and other holdings, was 9.8%, at the 1.1st national percentile and unusually low; at the 1.7th percentile among peers, against a peer median of 14.3%, it is unusually low among its peers too. The leverage ratio, core capital as a share of average assets, was 7.3%, at the 1.2nd national percentile and unusually low; at the 0.6th percentile among peers, against a peer median of 10.8%, it is unusually low among its peers too. Asset growth over the past four quarters was -9.4%, meaning the bank shrank, at the 1.8th national percentile and unusually low; at the 1.8th percentile among peers, against a peer median of 4.8%, it is unusually low among its peers too.

Overall, 16 of the bank's ratios sit in the national top or bottom 10%, and all 16 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 57.8% | 99.6th (unusually high) | 3.0% | 99.7th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 2.2% | 99.2nd (unusually high) | 0.1% | 99.3rd | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.4% | 99.2nd (unusually high) | 0.3% | 99.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -17.7% | 0.9th (unusually low) | 11.7% | 0.5th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 9.8% | 1.1st (unusually low) | 14.3% | 1.7th | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 7.3% | 1.2nd (unusually low) | 10.8% | 0.6th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -1.2% | 1.7th (unusually low) | 1.2% | 1.0th | unusually low among its peers too |
| asset growth over the past four quarters | -9.4% | 1.8th (unusually low) | 4.8% | 1.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 46.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 167.3% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 8.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank falls in the open watchlist case: it was flagged by the model and, as far as this note's data goes, it remains an open bank rather than one that has closed. The fact sheet holds no data from after the as-of quarter, so this note cannot confirm whether the troubles seen in the data deepened or eased. Its place on the watchlist rests on the as-of picture described above: weak capital, rising troubled loans, losses and reliance on brokered funding.

## What happened next

In hindsight, no later ranks, watchlist flags or reporting status for Drake Bank appear in this fact sheet. Because of that, this note cannot say how its rank moved after the as-of quarter or whether it kept filing reports, and it makes no claim either way. Readers can check the score history table that accompanies this note for any later quarters as they become available.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MN · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.5029 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 15 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.8%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 7.9%; contribution to the score · 2026-06-30 · +0.580 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · +0.444 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.320 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: return on equity (profit as a share of equity), value -17.7%; contribution to the score · 2026-06-30 · +0.212 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.8%; contribution to the score · 2026-06-30 · -0.824 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.380 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $247.4 million; contribution to the score · 2026-06-30 · -0.208 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 5.7%; contribution to the score · 2026-06-30 · -0.151 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.212 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F96 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F97 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F99 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.007 · data/analyst/scores.parquet: feature return_on_assets contribution
- F100 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F101 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.125 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F106 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F107 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F108 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F109 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F112 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.005 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F113 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F114 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F115 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F116 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F119 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.165 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F120 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F121 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F122 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: texas_ratio
- F123 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 43.7% · data/features/fct_bank_features.parquet: texas_ratio
- F125 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +41.8 pp · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 92.1% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F145 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F146 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F147 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F148 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F151 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F152 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F153 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F154 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F155 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F156 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.7th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F175 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.7th · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -9.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F181 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F182 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F183 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F184 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F185 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
