---
cert: 57488
name: "Metropolitan Capital B&T"
as_of: 2025-12-31
rank: 2
n_banks: 4411
percentile: 99.97732940376332
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-01-30
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:20"
writer_model: "claude-opus-5-5"
checked: true
---

# Metropolitan Capital B&T (cert 57488)

*Hindsight: failed 2026-01-30. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2025-12-31, Metropolitan Capital B&T, a bank in IL, ranked 2 out of 4,411 banks nationally on Canary's risk score, placing it at the 100.0th percentile and on the watchlist. Its capital, the owners' cushion against losses, had run out: equity was -0.8% of assets, against a national median of 10.4%. The bank was also losing money heavily and writing off loans at a far higher rate than typical banks, while leaning more than most on borrowed and brokered funding.

## Warning signs in the data

Capital was the weakest area, with all three regulatory capital ratios far below national medians. The leverage ratio (core capital as a share of average assets) was 1.8% against a median of 10.8%, the Tier 1 risk-based capital ratio (strongest capital against risk-adjusted assets) was 3.0% against 14.4%, and the total risk-based capital ratio was 4.3% against 15.6%. Earnings were deeply negative: return on assets (profit as a share of assets) was -6.9% against a median of 1.1%, and the efficiency ratio (operating costs as a share of revenue) was 123.3% against 63.8%, meaning costs exceeded revenue.

Credit quality was poor: loans 90 or more days past due or not accruing interest (nonaccrual, meaning the bank has stopped counting interest as income) were 2.8% of loans against a median of 0.4%. Net loan write-offs were 12.4% of loans against a median of 0.0%, and the annualized provision for loan losses (money set aside for expected bad loans) was 6.1% of assets against 0.1%. The Texas ratio, which compares troubled assets with capital plus reserves, was 152.5% against a median of 2.7%, meaning troubled assets exceeded the bank's loss-absorbing resources.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) were 22.0% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 14.0% of assets against 0.2%. Deposits shrank by -7.3% over the past four quarters, while the median bank grew deposits by 4.1%; on the other side, cash was a relatively high 16.7% of assets against a median of 6.5%. Losses on bonds available for sale were -684.7% of equity against a median of 5.2%, but because equity was below zero this ratio is hard to read. The separate real-estate concentration check found that the bank did not cross either supervisory line, so commercial property lending is not where the strain shows.

## Understanding the score

Metropolitan Capital B&T ranked 2 out of 4,411 banks as of 2025-12-31, which is the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 89 banks that quarter. Its percentile a year earlier, on 2024-12-31, was also the 100.0th, so the rating was about the same as a year earlier.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 3.0% (contribution +1.701), return on equity at -672.4% (+1.537), the Texas ratio at 152.5% (+1.021), the total risk-based capital ratio at 4.3% (+0.524), and the leverage ratio at 1.8% (+0.364). The five that pushed it down most were nonaccrual assets and foreclosed property at 2.2% of assets (-0.489), net interest margin (the spread earned on lending and investing) at 4.9% (-0.426), losses on bonds available for sale at -684.7% of equity (-0.368), loans 90+ days past due or nonaccrual at 2.8% of loans (-0.262), and construction loans at 4.7% of loans (-0.227). Some of these downward drivers, such as the bad-loan measures, look weak next to national medians, so the model's treatment of them points a different way from the plain comparison; the capital and earnings drivers far outweighed them.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 95 | 4,640 |  |
| 2024-06-30 | 38 | 4,610 | ▲ watchlist |
| 2024-09-30 | 40 | 4,589 | ▲ watchlist |
| 2024-12-31 | 2 | 4,560 | ▲ watchlist |
| 2025-03-31 | 5 | 4,536 | ▲ watchlist (first flag) |
| 2025-06-30 | 4 | 4,494 | ▲ watchlist |
| 2025-09-30 | 2 | 4,452 | ▲ watchlist |
| 2025-12-31 | 2 | 4,411 | ▲ watchlist |

## How its ratios moved

As of 2025-12-31, Metropolitan Capital B&T ranked 2 out of 4,411 banks nationally, which places it at the 100.0th percentile on a scale where higher means riskier. A year earlier, on 2024-12-31, it also sat at the 100.0th percentile, and the model's rating is about the same as a year earlier. Each ratio is compared with the bank's own prior range, usually the previous 12 quarters, or the same quarter in the prior 3 years for year-to-date figures. Of 30 ratios checked, 15 were outside their prior range, and the 6 furthest outside are shown in the table.

Return on equity (profit as a share of the owners' stake) was -672.4%, far below its prior range of -91.0% to 14.6%, and it pushed the score up by +1.537 model log-odds units. Its change over four quarters was -581.5 pp. The efficiency ratio (operating costs as a share of revenue) was 123.3%, above its prior range of 76.3% to 91.0%, yet it had little effect on the score, contributing -0.044 model log-odds units. Net loan write-offs (loans written off as unrecoverable, minus recoveries) were 12.4% of loans, above the prior range of 0.0% to 4.5%, but this had little effect on the score, at -0.024 model log-odds units.

Losses on bonds available for sale (bonds the bank may sell) measured -684.7% of equity, outside the prior range of 73.1% to 505.3%, yet this ratio pushed the score down by -0.368 model log-odds units. Construction loans were 4.7% of loans, above the prior range of 0.0% to 3.2%, but this ratio pushed the score down, contributing -0.227 model log-odds units. Net interest margin (the spread earned on lending and investing) was 4.9%, below its prior range of 5.7% to 7.4%, and it also pushed the score down, by -0.426 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -672.4% | -91.0% to 14.6% | same quarter, prior 3 years | n/a | -581.5 pp | +1.537 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 123.3% | 76.3% to 91.0% | same quarter, prior 3 years | n/a | +32.3 pp | -0.044 | little effect on the score |
| losses on bonds available for sale, as a share of equity | -684.7% | 73.1% to 505.3% | prior 12 quarters | -982.2 pp | -1189.9 pp | -0.368 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 12.4% | 0.0% to 4.5% | same quarter, prior 3 years | n/a | +7.8 pp | -0.024 | little effect on the score |
| construction loans as a share of loans | 4.7% | 0.0% to 3.2% | prior 12 quarters | +1.5 pp | +4.7 pp | -0.227 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 4.9% | 5.7% to 7.4% | same quarter, prior 3 years | n/a | -1.7 pp | -0.426 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2025-12-31: Commercial Lending Specialization.

Peers: 1473 banks in the same specialty group and size tier ($100 million to $1 billion).

Metropolitan Capital B&T ranked 2 out of 4,411 banks nationally on Canary's score as of 2025-12-31, and its financial ratios set it far apart from similar banks. Equity as a share of assets, the owners' cushion against losses, was -0.8%, at the 0.0th percentile nationally (unusually low) and the 0.0th percentile among its peers against a peer median of 10.1%, unusually low among its peers too. The total risk-based capital ratio, which measures capital against assets adjusted for their credit quality, was 4.3%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among its peers against a peer median of 15.3%, unusually low among its peers too. The Tier 1 risk-based capital ratio, a similar measure using only the strongest form of capital, was 3.0%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among its peers against a peer median of 14.1%, unusually low among its peers too.

Losses on bonds available for sale (bonds the bank can sell before they mature) as a share of equity stood at -684.7%, at the 0.0th percentile nationally (unusually low) and the 0.0th percentile among its peers against a peer median of 5.0%, unusually low among its peers too. Return on equity, profit as a share of equity, was -672.4%, at the 0.0th percentile nationally (unusually low) and the 0.0th percentile among its peers against a peer median of 11.3%, unusually low among its peers too. The Texas ratio, which compares troubled assets with capital plus reserves, was 152.5%, at the 99.9th percentile nationally (unusually high) and the 99.9th percentile among its peers against a peer median of 2.8%, unusually high among its peers too. The annualized provision for loan losses, money set aside for expected bad loans, was 6.1% of assets, at the 99.9th percentile nationally (unusually high) and the 100.0th percentile among its peers against a peer median of 0.1%, unusually high among its peers too. Annualized loan write-offs, net of recoveries, were 12.4% of loans, at the 99.9th percentile nationally (unusually high) and the 100.0th percentile among its peers against a peer median of 0.0%, unusually high among its peers too.

Overall, 20 of the bank's ratios fall in the national top or bottom 10%, and 19 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| equity as a share of assets | -0.8% | 0.0th (unusually low) | 10.1% | 0.0th | unusually low among its peers too |
| the total risk-based capital ratio | 4.3% | 0.0th (unusually low) | 15.3% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 3.0% | 0.0th (unusually low) | 14.1% | 0.1st | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | -684.7% | 0.0th (unusually low) | 5.0% | 0.0th | unusually low among its peers too |
| return on equity (profit as a share of equity) | -672.4% | 0.0th (unusually low) | 11.3% | 0.0th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 152.5% | 99.9th (unusually high) | 2.8% | 99.9th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 6.1% | 99.9th (unusually high) | 0.1% | 100.0th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 12.4% | 99.9th (unusually high) | 0.0% | 100.0th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 64.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 743.9% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -2.7% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, this is a case Canary caught: the bank failed on 2026-01-30, after the model's test window. Under the lead-time rule, the bank was first flagged in the quarter ending 2025-03-31, which gave a lead time of 4 quarters before the failure.

At that first flag, the top drivers pushing the score up were return on equity at -72.9% (+1.052), the Texas ratio at 138.8% (+0.874), the Tier 1 risk-based capital ratio at 6.3% (+0.666), losses on bonds available for sale at 388.4% of equity (+0.566), and loans 90+ days past due or nonaccrual at 8.8% of loans (+0.454). So, looking back, weak earnings, troubled assets and thin capital were already visible in the data well before the failure.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, Metropolitan Capital B&T failed on 2026-01-30. The last quarter it reported was 2025-12-31, so there are no later ranks or watchlist flags to show.

## Sources

- F1 · Bank name · n/a · Metropolitan Capital B&T · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-12-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · -0.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 3.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 4.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 2.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2025-12-31 · 6.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 152.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2025-12-31 · -6.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2025-12-31 · 123.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2025-12-31 · 63.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 22.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 14.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2025-12-31 · 16.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2025-12-31 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · -684.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2025-12-31 · -7.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2025-12-31 · 4.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.0%; contribution to the score · 2025-12-31 · +1.701 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -672.4%; contribution to the score · 2025-12-31 · +1.537 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 152.5%; contribution to the score · 2025-12-31 · +1.021 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 4.3%; contribution to the score · 2025-12-31 · +0.524 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 1.8%; contribution to the score · 2025-12-31 · +0.364 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: nonaccrual assets and foreclosed property, as a share of assets, value 2.2%; contribution to the score · 2025-12-31 · -0.489 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F81 · Driver down #2: net interest margin (the spread earned on lending and investing), value 4.9%; contribution to the score · 2025-12-31 · -0.426 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -684.7%; contribution to the score · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 2.8%; contribution to the score · 2025-12-31 · -0.262 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: construction loans as a share of loans, value 4.7%; contribution to the score · 2025-12-31 · -0.227 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2026-01-30 · 2026-01-30 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-03-31 · 2025-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-03-31: return on equity (profit as a share of equity), value -72.9%; contribution to the score · 2025-03-31 · +1.052 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-03-31: the Texas ratio (troubled assets against capital plus reserves), value 138.8%; contribution to the score · 2025-03-31 · +0.874 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2025-03-31: the Tier 1 risk-based capital ratio, value 6.3%; contribution to the score · 2025-03-31 · +0.666 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2025-03-31: losses on bonds available for sale, as a share of equity, value 388.4%; contribution to the score · 2025-03-31 · +0.566 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F92 · Driver up #5 at 2025-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2025-03-31 · +0.454 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · -672.4% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -91.0% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2025-12-31 · -581.5 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · +1.537 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-12-31 · 123.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 76.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 91.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-12-31 · -0.044 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2025-12-31 · -684.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F112 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · 73.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F113 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 505.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F116 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F118 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F119 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F120 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F122 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · -0.024 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F124 · Trend: construction loans as a share of loans, value at the as-of quarter · 2025-12-31 · 4.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F125 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F126 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F129 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · -0.227 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F130 · Trend: construction loans as a share of loans, what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F131 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2025-12-31 · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F132 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 5.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F133 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F135 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2025-12-31 · -0.426 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F136 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F137 · Trend: ratios outside their own prior range · 2025-12-31 · 15 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: equity as a share of assets, bank value at the as-of quarter · 2025-12-31 · -0.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F148 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F149 · Peers: equity as a share of assets, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F150 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F151 · Peers: equity as a share of assets, peer median · 2025-12-31 · 10.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F152 · Peers: equity as a share of assets, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F153 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2025-12-31 · 4.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2025-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, peer median · 2025-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the total risk-based capital ratio, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2025-12-31 · 3.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2025-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, peer median · 2025-12-31 · 14.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2025-12-31 · -684.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F166 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F167 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F168 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F169 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2025-12-31 · 5.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F170 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F171 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2025-12-31 · -672.4% · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2025-12-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), peer median · 2025-12-31 · 11.3% · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2025-12-31 · 152.5% · data/features/fct_bank_features.parquet: texas_ratio
- F178 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2025-12-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2025-12-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2025-12-31 · 2.8% · data/features/fct_bank_features.parquet: texas_ratio
- F182 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2025-12-31 · 6.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F184 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F185 · Peers: annualized provision for loan losses as a share of assets, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F186 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 100.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F187 · Peers: annualized provision for loan losses as a share of assets, peer median · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F188 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F189 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2025-12-31 · 12.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F190 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2025-12-31 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F191 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F192 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2025-12-31 · 100.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F193 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F194 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F196 · Peers: ratios in the national top or bottom 10% · 2025-12-31 · 20 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2025-12-31 · 19 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2025-12-31 · 10% · data/features/fct_bank_features.parquet
