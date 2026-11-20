---
cert: 15779
name: "Farmers&Merchants Bank"
as_of: 2026-06-30
rank: 25
n_banks: 4313
percentile: 99.44354277764896
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:07"
writer_model: "claude-opus-5-5"
checked: true
---

# Farmers&Merchants Bank (cert 15779)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Canary's model ranked Farmers&Merchants Bank, a Wisconsin lender, at number 25 out of 4,313 banks, which puts it in the 99.4th percentile, where higher means riskier. That places it on the watchlist, the 2% of banks with the highest scores. The main reason is its funding: brokered deposits, money placed through outside middlemen, made up 51.3% of deposits, against a national median of 0.0%. Problem loans and bond losses are also well above typical levels, while solid profits and capital ratios pulled the score down somewhat.

## Warning signs in the data

Capital, the cushion that absorbs losses, sits below the national median on every measure shown. Equity was 9.2% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.0% against 11.0%. The Tier 1 risk-based capital ratio was 12.8% against 14.6%, and the total risk-based capital ratio was 14.0% against 15.8%.

Credit quality is weaker than at most banks. Loans 90 or more days past due or no longer paying interest were 2.0% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property were 1.9% of assets against 0.3%, and the Texas ratio, troubled assets against capital plus reserves, was 18.7% against 2.9%. Commercial real estate loans were 29.9% of loans against a median of 23.6%, though the code-written concentration check found the bank did not cross either supervisory line.

Funding is where the bank stands out most: brokered deposits were 51.3% of deposits against a median of 0.0%, and core deposits, steady everyday accounts, were only 38.2% of assets against 75.5%. Federal Home Loan Bank borrowings were 7.6% of assets against 0.2%, cash was 1.7% of assets against 6.2%, and deposit growth over the past four quarters was -5.7% against a median of 4.2%. Paper losses on bonds available for sale equaled 12.0% of equity against a median of 5.6%, and on bonds held to maturity 5.6% against 0.0%. Pointing the other way, uninsured deposits were a low 7.4% of deposits against 24.8%, and return on equity was 14.2% against 11.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 25 of 4,313 banks, in the 99.4th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were brokered deposits at 51.3% of deposits, losses on bonds available for sale at 12.0% of equity, and the efficiency ratio (operating costs as a share of revenue) at 50.7%. The other two were core deposits at only 38.2% of assets and annualized interest expense at 2.8% of assets.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 12.8%, return on equity at 14.2%, and losses on bonds held to maturity at 5.6% of equity. The remaining two were return on assets (profit as a share of assets) at 1.2% and the total risk-based capital ratio at 14.0%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 69 | 4,589 | ▲ watchlist |
| 2024-12-31 | 100 | 4,560 |  |
| 2025-03-31 | 100 | 4,536 |  |
| 2025-06-30 | 44 | 4,494 | ▲ watchlist |
| 2025-09-30 | 38 | 4,452 | ▲ watchlist |
| 2025-12-31 | 41 | 4,411 | ▲ watchlist |
| 2026-03-31 | 46 | 4,353 | ▲ watchlist |
| 2026-06-30 | 25 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the model ranked Farmers&Merchants Bank 25 out of 4,313 banks, placing it in the 99.4th percentile, where higher means riskier. On 2025-06-30 it sat in the 99.0th percentile, and the model's rating is about the same as a year earlier. Of 30 ratios checked against the bank's own prior range, usually its previous 12 quarters, 11 were outside that range, and the 6 furthest out are discussed here.

The efficiency ratio (operating costs as a share of revenue) was 50.7%, above its prior range of 43.9% to 46.2%, and at +0.458 model log-odds units it pushed the score up. Equity as a share of assets, a cushion against losses, was 9.2%, above its prior range of 7.2% to 8.5%, and at +0.051 it pushed the score up. Return on equity (profit as a share of equity) fell to 14.2%, below its prior range of 16.2% to 19.2%, yet at -0.577 it pushed the score down.

Deposit growth over the past four quarters was -5.7%, below its prior range of 0.4% to 30.9%, but at -0.189 it pushed the score down. Securities (bonds the bank holds) made up 18.0% of assets, above their prior range of 15.9% to 17.4%, and at -0.105 they pushed the score down. The leverage ratio (core capital as a share of average assets) was 10.0%, above its prior range of 8.8% to 9.8%, and at -0.051 it pushed the score down. So although these last four ratios moved outside their usual ranges, the model treated each of them as lowering the score rather than raising it.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 50.7% | 43.9% to 46.2% | same quarter, prior 3 years | n/a | +6.5 pp | +0.458 | pushed the score up |
| return on equity (profit as a share of equity) | 14.2% | 16.2% to 19.2% | same quarter, prior 3 years | n/a | -5.0 pp | -0.577 | pushed the score down |
| equity as a share of assets | 9.2% | 7.2% to 8.5% | prior 12 quarters | +0.7 pp | +1.7 pp | +0.051 | pushed the score up |
| securities as a share of assets | 18.0% | 15.9% to 17.4% | prior 12 quarters | +0.7 pp | +2.1 pp | -0.105 | pushed the score down |
| deposit growth over the past four quarters | -5.7% | 0.4% to 30.9% | prior 12 quarters | -6.2 pp | -14.3 pp | -0.189 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 10.0% | 8.8% to 9.8% | prior 12 quarters | +0.2 pp | +0.8 pp | -0.051 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Brokered deposits, money placed with the bank through outside middlemen, made up 51.3% of deposits, the 99.4th percentile nationally, which is unusually high. Against its peers, that share sat at the 99.6th percentile versus a peer median of 0.0%, unusually high among its peers too. Interest expense, what the bank pays to borrow and hold deposits, ran at an annualized 2.8% of assets, the 97.1st percentile nationally (unusually high), and the 96.6th percentile among peers against a peer median of 1.7%, unusually high among its peers too. Core deposits, the steady everyday accounts of local customers, were 38.2% of assets, the 3.2nd percentile nationally (unusually low), and the 0.6th percentile among peers against a peer median of 75.6%, unusually low among its peers too. Uninsured deposits, balances above the government insurance limit, were 7.4% of deposits, the 4.2nd percentile nationally (unusually low), and the 1.1st percentile among peers against a peer median of 26.0%, unusually low among its peers too. Deposit growth over the past four quarters was -5.7%, the 5.5th percentile nationally (unusually low), and the 6.1st percentile among peers against a peer median of 4.3%, unusually low among its peers too.

Nonaccrual assets and foreclosed property, meaning loans that have stopped paying interest plus repossessed real estate, were 1.9% of assets, the 93.8th percentile nationally (unusually high), and the 91.6th percentile among peers against a peer median of 0.3%, unusually high among its peers too. The Texas ratio, troubled assets measured against capital plus reserves, was 18.7%, the 93.8th percentile nationally (unusually high), and the 90.8th percentile among peers against a peer median of 3.0%, unusually high among its peers too. Losses on bonds held to maturity, the paper losses on bonds the bank plans to keep until they are repaid, equaled 5.6% of equity, the 92.7th percentile nationally (unusually high), and the 94.5th percentile among peers against a peer median of 0.0%, unusually high among its peers too.

Overall, 10 of the bank's ratios fall in the national top or bottom 10%, and all 10 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| brokered deposits as a share of deposits | 51.3% | 99.4th (unusually high) | 0.0% | 99.6th | unusually high among its peers too |
| annualized interest expense as a share of assets | 2.8% | 97.1st (unusually high) | 1.7% | 96.6th | unusually high among its peers too |
| core deposits as a share of assets | 38.2% | 3.2nd (unusually low) | 75.6% | 0.6th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 7.4% | 4.2nd (unusually low) | 26.0% | 1.1st | unusually low among its peers too |
| deposit growth over the past four quarters | -5.7% | 5.5th (unusually low) | 4.3% | 6.1st | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 1.9% | 93.8th (unusually high) | 0.3% | 91.6th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 18.7% | 93.8th (unusually high) | 3.0% | 90.8th | unusually high among its peers too |
| losses on bonds held to maturity, as a share of equity | 5.6% | 92.7th (unusually high) | 0.0% | 94.5th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 63.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 310.5% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 17.3% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, this bank belongs to the open-watchlist group: the model flagged it, and our data does not record it as having failed. The fact sheet contains no figures from after the as-of quarter, so this memo cannot say whether the warning signs eased or worsened later. Its place on the watchlist rests on the as-of picture described above, led by its heavy reliance on brokered deposits.

## What happened next

In hindsight, the fact sheet provides no later ranks, flags or reporting status for this bank after the as-of quarter. Its outcome case is open on the watchlist, meaning no failure is recorded in our data; the score history table added by code shows any later quarters that are available.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 25 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 29.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 18.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 51.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 38.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 51.3%; contribution to the score · 2026-06-30 · +1.311 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 12.0%; contribution to the score · 2026-06-30 · +0.674 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 50.7%; contribution to the score · 2026-06-30 · +0.458 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F78 · Driver up #4: core deposits as a share of assets, value 38.2%; contribution to the score · 2026-06-30 · +0.413 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.311 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 12.8%; contribution to the score · 2026-06-30 · -0.939 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 14.2%; contribution to the score · 2026-06-30 · -0.577 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: losses on bonds held to maturity, as a share of equity, value 5.6%; contribution to the score · 2026-06-30 · -0.416 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 1.2%; contribution to the score · 2026-06-30 · -0.273 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 14.0%; contribution to the score · 2026-06-30 · -0.273 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 50.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 43.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 46.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.458 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 16.2% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 19.2% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.577 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F102 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 7.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F103 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 8.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F106 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.051 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F107 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F108 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 18.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F109 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 15.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F110 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 17.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F113 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.105 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F114 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F115 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2026-06-30 · -5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F116 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F117 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 30.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F120 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.189 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F121 · Trend: deposit growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F122 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F123 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F124 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F127 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.051 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F128 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.0% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 51.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F140 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F141 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F142 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F143 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F144 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F145 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F146 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F147 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F148 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F149 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F150 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F151 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 38.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F152 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F153 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F154 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F155 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 75.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F156 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F157 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F158 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 4.2nd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F159 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F160 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F161 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F162 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F163 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F164 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.5th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F165 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F166 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 6.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F167 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F168 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F169 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F170 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F171 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F172 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 91.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F173 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F174 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F175 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 18.7% · data/features/fct_bank_features.parquet: texas_ratio
- F176 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 93.8th · data/features/fct_bank_features.parquet: texas_ratio
- F177 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F178 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 90.8th · data/features/fct_bank_features.parquet: texas_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F182 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.7th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F183 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F184 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 94.5th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F185 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F186 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F188 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
