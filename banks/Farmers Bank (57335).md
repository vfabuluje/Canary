---
cert: 57335
name: "Farmers Bank"
as_of: 2026-06-30
rank: 37
n_banks: 4313
percentile: 99.16531416647345
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:45"
writer_model: "claude-opus-5-5"
checked: true
---

# Farmers Bank (cert 57335)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Farmers Bank of CO ranked 37 out of 4,313 FDIC-insured banks, which puts it in the 99.2nd percentile, where higher means riskier, and it is flagged on Canary's watchlist. The main concerns are paper losses on bonds it could sell equal to 107.7% of equity, a Texas ratio (troubled assets against capital plus reserves) of 51.1%, and equity of only 6.7% of assets against a national median of 10.6%. Pulling the other way, the bank is very profitable, with a return on equity of 26.4%, and its leverage ratio (core capital as a share of average assets) of 13.0% is above the national median of 11.0%.

## Warning signs in the data

Capital, the owners' cushion against losses, sends mixed signals. Equity was 6.7% of assets, well below the national median of 10.6%. Yet the leverage ratio, a regulatory capital measure, was 13.0%, above the national median of 11.0%, so these two capital readings point in different directions. The bond picture helps explain the thin equity: unrealized losses on bonds available for sale equaled 107.7% of equity, far above the national median of 5.6%.

Credit quality is weak. Loans 90 or more days past due or no longer earning interest were 6.3% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property were 3.9% of assets, against a national median of 0.3%, and the Texas ratio was 51.1%, against a national median of 2.9%. Loans at an earlier stage of lateness were 0.7% of assets, above the national median of 0.2%, while construction loans made up 15.5% of loans, well above the national median of 5.3%, though the real-estate concentration check found the bank did not cross either supervisory line.

On funding, uninsured deposits (balances above the government insurance limit) were 51.2% of deposits, well above the national median of 24.8%, and volatile funding, money that can leave quickly, was 22.5% of assets against a national median of 9.0%. Deposits changed by -1.8% over the past four quarters, while the national median grew 4.2%. On the positive side, cash was 14.5% of assets, well above the national median of 6.2%.

## Understanding the score

Farmers Bank ranked 37 out of 4,313 banks on 2026-06-30, placing it in the 99.2nd percentile on a scale of 0 to 100 where higher means riskier. That puts it on Canary's watchlist, which covers about 2% of banks and held 87 banks that quarter.

Five features pushed the score up most. Losses on bonds available for sale were 107.7% of equity, adding +1.307, and the Texas ratio of 51.1% added +0.889. Loans 90 or more days past due or not accruing interest at 6.3% of loans added +0.248, the efficiency ratio (operating costs as a share of revenue) of 56.2% added +0.197, and loans at 60.6% of deposits added +0.107.

Five features pulled the score down most. The Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets), whose value is not shown in our data, contributed -0.986. Return on equity of 26.4% contributed -0.626 and return on assets of 1.8% contributed -0.436. Interest expense at 1.5% of assets contributed -0.347, and the leverage ratio of 13.0% contributed -0.339.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 174 | 4,589 |  |
| 2024-12-31 | 286 | 4,560 |  |
| 2025-03-31 | 411 | 4,536 |  |
| 2025-06-30 | 308 | 4,494 |  |
| 2025-09-30 | 21 | 4,452 | ▲ watchlist |
| 2025-12-31 | 30 | 4,411 | ▲ watchlist |
| 2026-03-31 | 45 | 4,353 | ▲ watchlist |
| 2026-06-30 | 37 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Farmers Bank ranked 37 out of 4,313 banks nationally, placing it in the 99.2nd percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 93.2nd percentile, so the model rated it riskier than a year earlier. Each ratio is compared with its own history, mostly the prior 12 quarters, and 8 of the 28 ratios checked ended outside that prior range.

The efficiency ratio (operating costs as a share of revenue) reached 56.2%, above its prior range of 46.0% to 53.2%, and contributed +0.197 model log-odds units (positive values push the score up), which pushed the score up. Volatile funding, meaning money that can leave the bank quickly, rose to 22.5% of assets, above its prior range of 9.3% to 20.9%, and contributed +0.063, which pushed the score up. That volatile funding share was up +1.7 pp over one quarter and +3.5 pp over four quarters.

Return on equity (profit as a share of the owners' stake) fell to 26.4%, below its prior range of 35.5% to 45.1%, yet its contribution of -0.626 pushed the score down, because the level is still high profit. Return on assets (profit as a share of assets) was 1.8%, just below its prior range of 1.9% to 2.2%, but its contribution of -0.436 also pushed the score down. Brokered deposits, which are deposits placed through outside middlemen, dropped to 1.7% of deposits, below their prior range of 3.6% to 22.0%, and contributed -0.157, which pushed the score down. Net loan write-offs (loans written off as losses, minus recoveries) rose to 0.2% of loans, above their prior range of -0.1% to 0.0%, but contributed only +0.002, which had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 26.4% | 35.5% to 45.1% | same quarter, prior 3 years | n/a | -10.3 pp | -0.626 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 56.2% | 46.0% to 53.2% | same quarter, prior 3 years | n/a | +4.1 pp | +0.197 | pushed the score up |
| return on assets (profit as a share of assets) | 1.8% | 1.9% to 2.2% | same quarter, prior 3 years | n/a | -0.4 pp | -0.436 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.2% | -0.1% to 0.0% | same quarter, prior 3 years | n/a | +0.2 pp | +0.002 | little effect on the score |
| volatile funding as a share of assets | 22.5% | 9.3% to 20.9% | prior 12 quarters | +1.7 pp | +3.5 pp | +0.063 | pushed the score up |
| brokered deposits as a share of deposits | 1.7% | 3.6% to 22.0% | prior 12 quarters | -1.9 pp | -5.5 pp | -0.157 | pushed the score down |

8 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 642 banks in the same specialty group and size tier ($100 million to $1 billion).

Farmers Bank ranked 37 out of 4,313 banks nationally as of June 30, 2026, and the ratios below show where its numbers sit against banks of similar type and size. Its Texas ratio (troubled assets measured against capital plus reserves) was 51.1%, at the 99.5th percentile nationally, which is unusually high, and at the 99.6th percentile among its peers against a peer median of 2.5%, unusually high among its peers too. Losses on bonds available for sale (paper losses on bonds the bank could sell) equaled 107.7% of equity, at the 99.4th percentile nationally, which is unusually high, and at the 99.1st percentile among its peers against a peer median of 7.2%, unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) plus foreclosed property made up 3.9% of assets, at the 98.6th percentile nationally, which is unusually high, and at the 99.0th percentile among its peers against a peer median of 0.2%, unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 6.3% of loans, at the 98.6th percentile nationally, which is unusually high, and at the 99.0th percentile among its peers against a peer median of 0.4%, unusually high among its peers too.

Return on equity (profit as a share of the owners' stake) was 26.4%, at the 96.8th percentile nationally, which is unusually high, and at the 97.1st percentile among its peers against a peer median of 13.9%, unusually high among its peers too. Equity (the owners' cushion against losses) was 6.7% of assets, at the 4.3rd percentile nationally, which is unusually low, and at the 4.1st percentile among its peers against a peer median of 10.5%, unusually low among its peers too. Volatile funding (money that can leave the bank quickly) was 22.5% of assets, at the 95.4th percentile nationally, which is unusually high, and at the 97.1st percentile among its peers against a peer median of 10.1%, unusually high among its peers too. Uninsured deposits (balances above the government insurance limit) were 51.2% of deposits, at the 94.8th percentile nationally, which is unusually high, and at the 98.8th percentile among its peers against a peer median of 22.6%, unusually high among its peers too.

Overall, 9 of the bank's ratios fall in the national top or bottom 10%, and all 9 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 51.1% | 99.5th (unusually high) | 2.5% | 99.6th | unusually high among its peers too |
| losses on bonds available for sale, as a share of equity | 107.7% | 99.4th (unusually high) | 7.2% | 99.1st | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 3.9% | 98.6th (unusually high) | 0.2% | 99.0th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 6.3% | 98.6th (unusually high) | 0.4% | 99.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | 26.4% | 96.8th (unusually high) | 13.9% | 97.1st | unusually high among its peers too |
| equity as a share of assets | 6.7% | 4.3rd (unusually low) | 10.5% | 4.1st | unusually low among its peers too |
| volatile funding as a share of assets | 22.5% | 95.4th (unusually high) | 10.1% | 97.1st | unusually high among its peers too |
| uninsured deposits as a share of deposits | 51.2% | 94.8th (unusually high) | 22.6% | 98.8th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 59.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 85.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -20.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, the fact sheet for this note contains no data from after the as-of quarter, so it adds nothing to the picture described above. The bank's place on the watchlist rests on its as-of figures: large paper bond losses, heavy troubled loans and thin equity, partly offset by strong profits.

## What happened next

In hindsight, our fact sheet holds no later ranks, watchlist flags or reporting status for this bank, so this note cannot say how its rank moved or whether it still reports. Any later quarters that are available appear in the score history table that accompanies this memo.

## Sources

- F1 · Bank name · n/a · Farmers Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CO · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 37 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 6.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: construction loans as a share of loans · 2026-06-30 · 15.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F30 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 51.1% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 26.4% · data/features/fct_bank_features.parquet: return_on_equity
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 51.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 107.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -1.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 107.7%; contribution to the score · 2026-06-30 · +1.307 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 51.1%; contribution to the score · 2026-06-30 · +0.889 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 6.3%; contribution to the score · 2026-06-30 · +0.248 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F74 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 56.2%; contribution to the score · 2026-06-30 · +0.197 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F75 · Driver up #5: loans as a share of deposits, value 60.6%; contribution to the score · 2026-06-30 · +0.107 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.986 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 26.4%; contribution to the score · 2026-06-30 · -0.626 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: return on assets (profit as a share of assets), value 1.8%; contribution to the score · 2026-06-30 · -0.436 · data/analyst/scores.parquet: feature return_on_assets contribution
- F79 · Driver down #4: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2026-06-30 · -0.347 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 13.0%; contribution to the score · 2026-06-30 · -0.339 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F81 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 26.4% · data/features/fct_bank_features.parquet: return_on_equity
- F82 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 35.5% · data/features/fct_bank_features.parquet: return_on_equity
- F83 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 45.1% · data/features/fct_bank_features.parquet: return_on_equity
- F85 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.626 · data/analyst/scores.parquet: feature return_on_equity contribution
- F86 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F87 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 56.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 46.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 53.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.197 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F93 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: return_on_assets
- F94 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F95 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F97 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.436 · data/analyst/scores.parquet: feature return_on_assets contribution
- F98 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.002 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F106 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 9.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F107 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 20.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F108 · Trend: volatile funding as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +1.7 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F109 · Trend: volatile funding as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +3.5 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F110 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.063 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F111 · Trend: volatile funding as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F112 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F113 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F114 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 22.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F117 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.157 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F118 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F119 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F122 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 93.2% · data/analyst/scores.parquet: percentile
- F125 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F129 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 51.1% · data/features/fct_bank_features.parquet: texas_ratio
- F130 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 107.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F136 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F137 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F138 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F139 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F140 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 6.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F150 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 26.4% · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F160 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 4.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F161 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F162 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 4.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F163 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F164 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F165 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F166 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.4th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F167 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F168 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F169 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F170 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F171 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 51.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F172 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.8th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F173 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F174 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F175 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 22.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F176 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F178 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F179 · Peers: those ratios also unusual among peers · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F181 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
