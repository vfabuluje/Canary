---
cert: 17982
name: "Walton State Bank"
as_of: 2023-06-30
rank: 52
n_banks: 4714
percentile: 98.91811624946966
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:43"
writer_model: "claude-opus-5-5"
checked: true
---

# Walton State Bank (cert 17982)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2023-06-30, Walton State Bank, a very small Kansas bank with total assets of $11.0 million, ranked 52 out of 4,714 banks nationally, the 98.9th percentile, and was on Canary's watchlist. Its troubled loans and paper losses on bonds were well above national norms, and its leverage ratio, a basic capital cushion, was below the national median. The picture is mixed: its risk-based capital ratios, steady deposits and cash holdings were well above typical levels, and the trend section shows its troubled assets were shrinking and its capital ratios were rising compared with their own past ranges.

## Warning signs in the data

On capital, equity (the owners' stake, which absorbs losses) was 7.8% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 7.8% against a median of 10.5%. The risk-based measures point the other way: the Tier 1 risk-based capital ratio (core capital against assets weighted by their riskiness) was 23.1% versus a median of 14.2%, and the total risk-based capital ratio was 24.4% versus 15.4%.

On credit quality, loans 90+ days past due or not accruing interest were 4.1% of loans, far above the national median of 0.3%, and nonaccrual assets and foreclosed property were 1.6% of assets against a median of 0.1%. The Texas ratio (troubled assets compared with capital plus reserves) was 19.0%, well above the median of 1.8%. Losses on bonds held to maturity (paper losses on bonds the bank plans to keep until they repay) equaled 31.9% of equity, against a national median of 0.0%.

Funding looked steady: core deposits (everyday customer deposits) were 92.0% of assets against a median of 78.1%, volatile funding was 0.0% against 7.8%, and cash was 20.1% of assets against 5.3%. The bank was shrinking, with asset growth over the past four quarters of -11.8% against a median of 2.2%, and deposit growth of -13.0% against -1.1%. Profits were thin, with return on assets of 0.4% against a median of 1.0% and an efficiency ratio (operating costs as a share of revenue) of 86.3% against 65.5%.

## Understanding the score

Walton State Bank ranked 52 out of 4,714 banks in Q2 2023, placing it in the 98.9th percentile on a scale where higher means riskier. That put it on the watchlist, which covers the top 2% of banks by score; 95 banks were on it that quarter.

The five factors that pushed the score up most were core deposits as a share of assets at 92.0%, total assets of $11.0 million, loans 90+ days past due or not accruing interest at 4.1% of loans, construction loans at 0.0% of loans, and loans at 27.1% of deposits. Some of these sound reassuring on their own; the model is reflecting patterns it learned from past data, not judging each figure as good or bad.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 23.1%, interest expense at 0.3% of assets, the total risk-based capital ratio at 24.4%, the efficiency ratio at 86.3%, and return on equity (profit as a share of equity) at 5.9%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-09-30 | 4 | 4,979 | ▲ watchlist |
| 2021-12-31 | 6 | 4,904 | ▲ watchlist |
| 2022-03-31 | 9 | 4,861 | ▲ watchlist |
| 2022-06-30 | 13 | 4,838 | ▲ watchlist |
| 2022-09-30 | 37 | 4,813 | ▲ watchlist |
| 2022-12-31 | 6 | 4,773 | ▲ watchlist |
| 2023-03-31 | 90 | 4,740 | ▲ watchlist |
| 2023-06-30 | 52 | 4,714 | ▲ watchlist |

## How its ratios moved

As of June 30, 2023, Walton State Bank ranked 52 out of 4,714 banks nationally, which puts it in the 98.9th percentile on a scale where higher means riskier. A year earlier it stood at the 99.8th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own prior range, which for most ratios covers the previous 12 quarters, and 13 of the 30 ratios checked sat outside that range; the 6 furthest outside are described here.

The leverage ratio (core capital, the bank's loss-absorbing cushion, as a share of average assets) was 7.8%, above its prior range of 6.1% to 7.3%, and it pushed the score up with a contribution of +0.060 model log-odds units, the model's internal scale where positive raises the score. Equity as a share of assets was 7.8%, above its prior range of 6.0% to 7.4%, yet despite sitting outside that range it had little effect on the score, contributing -0.029. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by their riskiness) was 23.1%, above its prior range of 18.1% to 22.3%, but rather than raising concern it pushed the score down, contributing -0.894. The total risk-based capital ratio, a broader version that also counts some reserves, was 24.4%, above its prior range of 19.3% to 23.6%, and it likewise pushed the score down, contributing -0.544.

The Texas ratio (troubled assets compared with capital plus reserves) was 19.0%, below its prior range of 23.2% to 35.1%, and although outside that range it pushed the score down, contributing -0.245. Nonaccrual assets and foreclosed property (loans no longer collecting interest plus property taken back from borrowers) made up 1.6% of assets, below their prior range of 1.8% to 2.4%, and this outside-range reading also pushed the score down, contributing -0.103.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the leverage ratio (core capital as a share of average assets) | 7.8% | 6.1% to 7.3% | prior 12 quarters | +1.0 pp | +1.5 pp | +0.060 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 19.0% | 23.2% to 35.1% | prior 12 quarters | -12.8 pp | -13.8 pp | -0.245 | pushed the score down |
| equity as a share of assets | 7.8% | 6.0% to 7.4% | prior 12 quarters | +0.8 pp | +1.6 pp | -0.029 | little effect on the score |
| nonaccrual assets and foreclosed property, as a share of assets | 1.6% | 1.8% to 2.4% | prior 12 quarters | -0.8 pp | -0.6 pp | -0.103 | pushed the score down |
| the Tier 1 risk-based capital ratio | 23.1% | 18.1% to 22.3% | prior 12 quarters | +3.1 pp | +5.0 pp | -0.894 | pushed the score down |
| the total risk-based capital ratio | 24.4% | 19.3% to 23.6% | prior 12 quarters | +3.1 pp | +5.1 pp | -0.544 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2023-06-30: Other Specialized Under 1 Billion.

Peers: 132 banks in the same specialty group and size tier (under $100 million).

Loans 90+ days past due or not accruing interest (loans where payments have stopped or are far behind) were 4.1% of the bank's loans, the 98.3rd percentile nationally, which is unusually high, and the 92.6th percentile among peers against a peer median of 0.3%, which is unusually high among its peers too. Nonaccrual assets and foreclosed property (assets no longer earning interest, plus property taken back from borrowers) were 1.6% of assets, the 96.8th percentile nationally, which is unusually high, and the 96.6th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 19.0%, the 97.1st percentile nationally, which is unusually high, and the 96.6th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too.

Losses on bonds held to maturity (paper losses on bonds the bank intends to keep until they pay back) were 31.9% of equity, the 97.1st percentile nationally, which is unusually high, and the 95.8th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too. The leverage ratio (core capital as a share of average assets, a measure of the cushion against losses) was 7.8%, the 3.7th percentile nationally, which is unusually low, and the 1.9th percentile among peers against a peer median of 24.9%, which is unusually low among its peers too. Asset growth over the past four quarters was -11.8%, the 2.9th percentile nationally, which is unusually low, and the 6.7th percentile among peers against a peer median of 0.2%, which is unusually low among its peers too.

On funding, core deposits (steady everyday customer deposits) were 92.0% of assets, the 98.0th percentile nationally, which is unusually high, and the 92.0th percentile among peers against a peer median of 69.7%, which is unusually high among its peers too. Volatile funding (money that can leave the bank quickly) was 0.0% of assets, the 1.6th percentile nationally, which is unusually low, and the 22.3rd percentile among peers against a peer median of 0.8%, which is typical for its peer group. Overall, 14 of the bank's ratios were in the national top or bottom 10%, and 7 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| volatile funding as a share of assets | 0.0% | 1.6th (unusually low) | 0.8% | 22.3rd | typical for its peer group |
| loans 90+ days past due or not accruing interest, as a share of loans | 4.1% | 98.3rd (unusually high) | 0.3% | 92.6th | unusually high among its peers too |
| core deposits as a share of assets | 92.0% | 98.0th (unusually high) | 69.7% | 92.0th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 19.0% | 97.1st (unusually high) | 0.0% | 96.6th | unusually high among its peers too |
| losses on bonds held to maturity, as a share of equity | 31.9% | 97.1st (unusually high) | 0.0% | 95.8th | unusually high among its peers too |
| asset growth over the past four quarters | -11.8% | 2.9th (unusually low) | 0.2% | 6.7th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 1.6% | 96.8th (unusually high) | 0.0% | 96.6th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 7.8% | 3.7th (unusually low) | 24.9% | 1.9th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 19.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 44.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

With hindsight, this flag was a false alarm: the bank was off the watchlist by the next quarter, ranking 620 at 2023-09-30, and it was still reporting and not flagged at 2026-06-30. It was flagged mainly for its very small size, its high level of troubled loans, and a funding and lending mix the model associated with risk, while its strong risk-based capital held the score down. Since 96% of the failures the model learned from were credit-loss failures, elevated troubled loans weigh heavily in its score. The as-of data already hinted at improvement, with the Texas ratio and nonaccrual assets below their own prior ranges and capital ratios above them.

## What happened next

In hindsight, the bank's rank moved well away from the top after the as-of quarter: 620 at 2023-09-30, 1,470 at 2023-12-31, 2,241 at 2024-03-31 and 1,902 at 2024-06-30, none of them flagged. It moved closer to the top again at times, ranking 877 at 2024-09-30, 510 at 2024-12-31, 708 at 2025-03-31 and 529 at 2025-06-30, but was not flagged in any of those quarters. Later ranks were 1,462 at 2025-09-30, 1,029 at 2025-12-31, 2,650 at 2026-03-31 and 3,059 at 2026-06-30, all not flagged, and the bank was still reporting as of that last quarter.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-09-30 | 620 | 4,686 |  |
| 2023-12-31 | 1,470 | 4,658 |  |
| 2024-03-31 | 2,241 | 4,640 |  |
| 2024-06-30 | 1,902 | 4,610 |  |
| 2024-09-30 | 877 | 4,589 |  |
| 2024-12-31 | 510 | 4,560 |  |
| 2025-03-31 | 708 | 4,536 |  |
| 2025-06-30 | 529 | 4,494 |  |
| 2025-09-30 | 1,462 | 4,452 |  |
| 2025-12-31 | 1,029 | 4,411 |  |
| 2026-03-31 | 2,650 | 4,353 |  |
| 2026-06-30 | 3,059 | 4,313 |  |

## Sources

- F3 · As-of quarter · 2023-06-30 · 2023-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-06-30 · 52 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-06-30 · 4,714 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-06-30 · 98.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-06-30 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-06-30 · 23.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-06-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-06-30 · 24.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 4.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-06-30 · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 86.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 65.5% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-06-30 · 92.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-06-30 · 78.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-06-30 · 20.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-06-30 · 5.3% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 31.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2023-06-30 · $11.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2023-06-30 · -11.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2023-06-30 · 2.2% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-06-30 · -13.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-06-30 · -1.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: core deposits as a share of assets, value 92.0%; contribution to the score · 2023-06-30 · +0.730 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F76 · Driver up #2: total assets, value $11.0 million; contribution to the score · 2023-06-30 · +0.586 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 4.1%; contribution to the score · 2023-06-30 · +0.452 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: construction loans as a share of loans, value 0.0%; contribution to the score · 2023-06-30 · +0.226 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver up #5: loans as a share of deposits, value 27.1%; contribution to the score · 2023-06-30 · +0.198 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 23.1%; contribution to the score · 2023-06-30 · -0.894 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2023-06-30 · -0.792 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 24.4%; contribution to the score · 2023-06-30 · -0.544 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: the efficiency ratio (operating costs as a share of revenue), value 86.3%; contribution to the score · 2023-06-30 · -0.285 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 5.9%; contribution to the score · 2023-06-30 · -0.282 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Rank in a later quarter (2023-09-30), not flagged · 2023-09-30 · 620 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2023-12-31), not flagged · 2023-12-31 · 1,470 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2024-03-31), not flagged · 2024-03-31 · 2,241 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2024-06-30), not flagged · 2024-06-30 · 1,902 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2024-09-30), not flagged · 2024-09-30 · 877 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2024-12-31), not flagged · 2024-12-31 · 510 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F91 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 708 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F92 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 529 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F93 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 1,462 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F94 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 1,029 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 2,650 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F96 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 3,059 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F97 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F101 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F102 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F103 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F106 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2023-06-30 · +0.060 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F107 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2023-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F108 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F109 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 23.2% · data/features/fct_bank_features.parquet: texas_ratio
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 35.1% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2023-06-30 · -0.245 · data/analyst/scores.parquet: feature texas_ratio contribution
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F115 · Trend: equity as a share of assets, value at the as-of quarter · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F116 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F117 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F120 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2023-06-30 · -0.029 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F121 · Trend: equity as a share of assets, what the model did with it · 2023-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F127 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2023-06-30 · -0.103 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F128 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F129 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2023-06-30 · 23.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F130 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 18.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F131 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 22.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F134 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2023-06-30 · -0.894 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F135 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F136 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2023-06-30 · 24.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F137 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 19.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F138 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 23.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F141 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2023-06-30 · -0.544 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F142 · Trend: the total risk-based capital ratio, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F143 · Trend: ratios outside their own prior range · 2023-06-30 · 13 · data/features/fct_bank_features.parquet
- F144 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-06-30 · 6 · data/features/fct_bank_features.parquet
- F145 · Trend: ratios compared with their own prior range · 2023-06-30 · 30 · data/features/fct_bank_features.parquet
- F146 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F148 · Percentile a year earlier (100 = highest risk) · 2022-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F149 · Trend: how the model's rating compares with a year earlier · 2023-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F153 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F154 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2023-06-30 · 1.6th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F155 · Peers: volatile funding as a share of assets, national reading · 2023-06-30 · unusually low · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F156 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2023-06-30 · 22.3rd · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F157 · Peers: volatile funding as a share of assets, peer median · 2023-06-30 · 0.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F158 · Peers: volatile funding as a share of assets, reading against its peers · 2023-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F159 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2023-06-30 · 4.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F160 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2023-06-30 · 98.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F161 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2023-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F162 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2023-06-30 · 92.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F163 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2023-06-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2023-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2023-06-30 · 92.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F166 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2023-06-30 · 98.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F167 · Peers: core deposits as a share of assets, national reading · 2023-06-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F168 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2023-06-30 · 92.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F169 · Peers: core deposits as a share of assets, peer median · 2023-06-30 · 69.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F170 · Peers: core deposits as a share of assets, reading against its peers · 2023-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2023-06-30 · 97.1st · data/features/fct_bank_features.parquet: texas_ratio
- F173 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2023-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F174 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2023-06-30 · 96.6th · data/features/fct_bank_features.parquet: texas_ratio
- F175 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F176 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2023-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F177 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2023-06-30 · 31.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F178 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2023-06-30 · 97.1st · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F179 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2023-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F180 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2023-06-30 · 95.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F181 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F182 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2023-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F183 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2023-06-30 · -11.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F184 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2023-06-30 · 2.9th · data/features/fct_bank_features.parquet: asset_growth_4q
- F185 · Peers: asset growth over the past four quarters, national reading · 2023-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F186 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2023-06-30 · 6.7th · data/features/fct_bank_features.parquet: asset_growth_4q
- F187 · Peers: asset growth over the past four quarters, peer median · 2023-06-30 · 0.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F188 · Peers: asset growth over the past four quarters, reading against its peers · 2023-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F190 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2023-06-30 · 96.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F191 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2023-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F192 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2023-06-30 · 96.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F193 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F194 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2023-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F195 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F196 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2023-06-30 · 3.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F197 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2023-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F198 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2023-06-30 · 1.9th · data/features/fct_bank_features.parquet: leverage_ratio
- F199 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2023-06-30 · 24.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F200 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2023-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F202 · Peers: ratios in the national top or bottom 10% · 2023-06-30 · 14 · data/features/fct_bank_features.parquet
- F203 · Peers: those ratios also unusual among peers · 2023-06-30 · 7 · data/features/fct_bank_features.parquet
- F205 · Peers: cut-off for unusual (top or bottom share of banks) · 2023-06-30 · 10% · data/features/fct_bank_features.parquet
