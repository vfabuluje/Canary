---
cert: 91
name: "Allied Bank"
as_of: 2016-06-30
rank: 1
n_banks: 6129
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-09-23
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:39"
writer_model: "claude-opus-5-5"
checked: true
---

# Allied Bank (cert 91)

*Hindsight: failed 2016-09-23. Canary flagged it 2 quarters ahead.*

## Summary

As of 2016-06-30, Allied Bank (cert 91, based in AR) ranked 1 out of 6,129 banks nationally on Canary's risk score, the 100.0th percentile, and it was on the watchlist. Its capital cushion, the owners' money that absorbs losses, was very thin: equity was 2.0% of assets against a national median of 11.0%. Problem loans and losses were severe, with nonaccrual assets and foreclosed property at 21.4% of assets against a national median of 0.6%, and a return on assets of -12.4% against 0.9%. Funding pointed the other way, looking stable rather than strained, with core deposits at 94.4% of assets against a national median of 78.4%.

## Warning signs in the data

Capital was far below normal levels. Equity was 2.0% of assets against a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was 1.8% against 10.5%. The Tier 1 risk-based capital ratio (the strongest capital measured against assets weighted by riskiness) was 2.7% against a national median of 15.1%, and the total risk-based capital ratio was 4.0% against 16.3%.

Credit quality, meaning how well borrowers were repaying, was very weak. Loans 90+ days past due or no longer accruing interest were 12.3% of loans against a national median of 0.7%, and nonaccrual assets and foreclosed property were 21.4% of assets against 0.6%. The Texas ratio, which compares troubled assets with capital plus reserves, was 379.7% against a national median of 5.3%. Net loan write-offs (loans given up on, after recoveries) ran at an annualized 14.6% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 10.2% of assets against 0.1%. Those costs showed up in earnings: return on equity was -223.2% against a national median of 7.9%, and the efficiency ratio (operating costs as a share of revenue) was 184.8% against 69.7%.

Liquidity and funding, by contrast, did not look strained. Core deposits (stable, everyday customer deposits) were 94.4% of assets against a national median of 78.4%, uninsured deposits were 5.3% of deposits against 16.6%, and cash was 12.9% of assets against 6.4%. The bank was shrinking, though: assets changed by -32.7% over the past four quarters against a national median of 3.8%, and deposits by -28.6% against 3.2%. Unrealized losses on bonds available for sale (paper losses on bonds the bank could sell) were -4.5% of equity against a national median of -1.6%, while those on bonds held to maturity were -0.2% against 0.0%. The real-estate concentration section found the bank crossed the construction-lending screen but not the broader commercial real estate screen.

## Understanding the score

As of 2016-06-30, Allied Bank ranked 1 out of 6,129 banks, the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged as one of 123 banks on the watchlist that quarter, which covers the top 2% of banks.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 2.7% (+2.117), the Texas ratio at 379.7% (+1.418), return on equity at -223.2% (+1.284), the leverage ratio at 1.8% (+0.678), and the total risk-based capital ratio at 4.0% (+0.562). The five that pulled it down most were annualized interest expense at 0.3% of assets (-0.723), losses on bonds available for sale at -4.5% of equity (-0.255), construction loans at 6.6% of loans (-0.181), deposit growth over the past four quarters at -28.6% (-0.126), and volatile funding at 3.2% of assets (-0.096).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 25 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 1 | 6,129 | ▲ watchlist |

## How its ratios moved

As of 2016-06-30, Allied Bank ranked 1 out of 6,129 banks nationally, which places it at the 100.0th percentile on a 0 to 100 scale where higher means riskier. Of the 30 ratios compared with their own prior range, 18 sat outside it; for most ratios that range is what the bank itself showed over the prior 12 quarters.

Return on equity, meaning profit as a share of the owners' stake, was -223.2%, far below its prior range of -22.2% to -6.7%, and it pushed the score up with a contribution of +1.284 model log-odds units. Return on assets, meaning profit as a share of everything the bank owns, was -12.4% against a prior range of -1.9% to -0.5%, and it pushed the score up by +0.184 model log-odds units. The total risk-based capital ratio, a measure of the bank's loss-absorbing cushion relative to its riskier assets, was 4.0%, well below its prior range of 10.7% to 13.6%, and it pushed the score up by +0.562 model log-odds units. That capital ratio changed by -6.7 pp over one quarter and by -9.4 pp over four quarters. The annualized provision for loan losses, money set aside to cover expected bad loans, was 10.2% of assets compared with a prior range of 0.0% to 2.0%, and it pushed the score up by +0.122 model log-odds units.

By contrast, annualized net loan write-offs, loans the bank gave up on after any recoveries, were 14.6% of loans, well above the prior range of -0.3% to 2.9%, yet they had little effect on the score, at -0.016 model log-odds units. Likewise, the efficiency ratio, operating costs as a share of revenue, was 184.8% against a prior range of 120.0% to 138.2%, but it had little effect on the score, at -0.024 model log-odds units.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -223.2% | -22.2% to -6.7% | same quarter, prior 3 years | n/a | -216.6 pp | +1.284 | pushed the score up |
| return on assets (profit as a share of assets) | -12.4% | -1.9% to -0.5% | same quarter, prior 3 years | n/a | -11.9 pp | +0.184 | pushed the score up |
| annualized provision for loan losses as a share of assets | 10.2% | 0.0% to 2.0% | same quarter, prior 3 years | n/a | +10.2 pp | +0.122 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 14.6% | -0.3% to 2.9% | same quarter, prior 3 years | n/a | +12.1 pp | -0.016 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 184.8% | 120.0% to 138.2% | same quarter, prior 3 years | n/a | +64.8 pp | -0.024 | little effect on the score |
| the total risk-based capital ratio | 4.0% | 10.7% to 13.6% | prior 12 quarters | -6.7 pp | -9.4 pp | +0.562 | pushed the score up |

18 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-06-30: Commercial Lending Specialization.

Peers: 359 banks in the same specialty group and size tier (under $100 million).

Allied Bank's return on assets (profit as a share of assets) was -12.4%, at the 0.0th national percentile, which is unusually low; among its peers it sat at the 0.1st percentile against a peer median of 0.6%, unusually low among its peers too. Its return on equity (profit as a share of the owners' stake) was -223.2%, at the 0.0th national percentile, which is unusually low; it sat at the 0.1st percentile of its peers against a peer median of 5.5%, unusually low among its peers too.

Annualized loan write-offs, net of recoveries (loans the bank gave up on collecting), were 14.6% of loans, at the 100.0th national percentile, which is unusually high; it sat at the 99.9th percentile of its peers against a peer median of 0.0%, unusually high among its peers too. The annualized provision for loan losses (money set aside for expected loan losses) was 10.2% of assets, at the 100.0th national percentile, which is unusually high; it sat at the 99.9th percentile of its peers against a peer median of 0.0%, unusually high among its peers too. Nonaccrual assets and foreclosed property (loans no longer paying interest, plus property taken back from borrowers) were 21.4% of assets, at the 100.0th national percentile, which is unusually high; it sat at the 99.9th percentile of its peers against a peer median of 0.9%, unusually high among its peers too.

The total risk-based capital ratio (the bank's loss-absorbing cushion measured against its assets weighted by riskiness) was 4.0%, at the 0.0th national percentile, which is unusually low; it sat at the 0.1st percentile of its peers against a peer median of 16.6%, unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the strongest form of capital) was 2.7%, at the 0.0th national percentile, which is unusually low; it sat at the 0.1st percentile of its peers against a peer median of 15.5%, unusually low among its peers too. Core deposits (stable, everyday customer deposits) were 94.4% of assets, at the 99.9th national percentile, which is unusually high; it sat at the 99.9th percentile of its peers against a peer median of 81.3%, unusually high among its peers too. Overall, 18 of the bank's ratios were in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| return on assets (profit as a share of assets) | -12.4% | 0.0th (unusually low) | 0.6% | 0.1st | unusually low among its peers too |
| return on equity (profit as a share of equity) | -223.2% | 0.0th (unusually low) | 5.5% | 0.1st | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 14.6% | 100.0th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 10.2% | 100.0th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 21.4% | 100.0th (unusually high) | 0.9% | 99.9th | unusually high among its peers too |
| the total risk-based capital ratio | 4.0% | 0.0th (unusually low) | 16.6% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 2.7% | 0.0th (unusually low) | 15.5% | 0.1st | unusually low among its peers too |
| core deposits as a share of assets | 94.4% | 99.9th (unusually high) | 81.3% | 99.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 144.9% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 676.3% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -47.7% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Allied Bank failed on 2016-09-23. Canary first flagged it in the quarter ending 2016-03-31, a lead time of 2 quarters before the failure.

At that first flag, the top drivers pushing the score up were the Texas ratio at 212.6% (+1.267), return on equity at -62.0% (+1.089), and loans 90+ days past due or not accruing interest at 16.5% of loans (+0.756). At that point the Tier 1 risk-based capital ratio, at 9.4%, still pulled the score down (-1.415); by 2016-06-30 it had fallen to 2.7% and become the largest driver pushing the score up (+2.117).

## What happened next

In hindsight, the last quarter Allied Bank reported was 2016-06-30, the as-of quarter of this memo, so there are no later ranks or flags. Our data alone does not distinguish a merger from a closure when a bank stops reporting, but the fact sheet records a failure date of 2016-09-23.

## Sources

- F1 · Bank name · n/a · Allied Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 91 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-06-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-06-30 · 6,129 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-06-30 · 123 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-06-30 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-06-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-06-30 · 2.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-06-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-06-30 · 4.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-06-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 21.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 14.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2016-06-30 · 10.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2016-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 379.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-06-30 · -12.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-06-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-06-30 · -223.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-06-30 · 7.9% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 184.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-06-30 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-06-30 · 94.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-06-30 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-06-30 · 12.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-06-30 · 6.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-06-30 · -0.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-06-30 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-06-30 · -32.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-06-30 · 3.8% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-06-30 · -28.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-06-30 · 3.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.7%; contribution to the score · 2016-06-30 · +2.117 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 379.7%; contribution to the score · 2016-06-30 · +1.418 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -223.2%; contribution to the score · 2016-06-30 · +1.284 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.8%; contribution to the score · 2016-06-30 · +0.678 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.0%; contribution to the score · 2016-06-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2016-06-30 · -0.723 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -4.5%; contribution to the score · 2016-06-30 · -0.255 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 6.6%; contribution to the score · 2016-06-30 · -0.181 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: deposit growth over the past four quarters, value -28.6%; contribution to the score · 2016-06-30 · -0.126 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 3.2%; contribution to the score · 2016-06-30 · -0.096 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2016-09-23 · 2016-09-23 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 212.6%; contribution to the score · 2016-03-31 · +1.267 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2016-03-31: return on equity (profit as a share of equity), value -62.0%; contribution to the score · 2016-03-31 · +1.089 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 16.5%; contribution to the score · 2016-03-31 · +0.756 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F94 · Driver down #2 at 2016-03-31: the Tier 1 risk-based capital ratio, value 9.4%; contribution to the score · 2016-03-31 · -1.415 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-06-30 · -223.2% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -22.2% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -6.7% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-06-30 · +1.284 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-06-30 · -12.4% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-06-30 · +0.184 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2016-06-30 · 10.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2016-06-30 · +0.122 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2016-06-30 · 14.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F118 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · -0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F119 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F121 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2016-06-30 · -0.016 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F122 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2016-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-06-30 · 184.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 120.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 138.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F127 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-06-30 · -0.024 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2016-06-30 · 4.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F130 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F131 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 13.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F132 · Trend: the total risk-based capital ratio, change over one quarter, in percentage points · 2016-06-30 · -6.7 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F133 · Trend: the total risk-based capital ratio, change over four quarters, in percentage points · 2016-06-30 · -9.4 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F134 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2016-06-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F135 · Trend: the total risk-based capital ratio, what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F136 · Trend: ratios outside their own prior range · 2016-06-30 · 18 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2016-06-30 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-06-30 · -12.4% · data/features/fct_bank_features.parquet: return_on_assets
- F145 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_assets
- F146 · Peers: return on assets (profit as a share of assets), national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F147 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F148 · Peers: return on assets (profit as a share of assets), peer median · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F149 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F150 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-06-30 · -223.2% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), peer median · 2016-06-30 · 5.5% · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2016-06-30 · 14.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2016-06-30 · 100.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2016-06-30 · 10.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F163 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2016-06-30 · 100.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F164 · Peers: annualized provision for loan losses as a share of assets, national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F165 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F166 · Peers: annualized provision for loan losses as a share of assets, peer median · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2016-06-30 · 21.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F169 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2016-06-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F170 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F171 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F172 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2016-06-30 · 0.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F173 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F174 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-06-30 · 4.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F175 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F176 · Peers: the total risk-based capital ratio, national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F177 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F178 · Peers: the total risk-based capital ratio, peer median · 2016-06-30 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F179 · Peers: the total risk-based capital ratio, reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F180 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-06-30 · 2.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F181 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F182 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F183 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F184 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-06-30 · 15.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F185 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F186 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2016-06-30 · 94.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F187 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F188 · Peers: core deposits as a share of assets, national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F189 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F190 · Peers: core deposits as a share of assets, peer median · 2016-06-30 · 81.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F191 · Peers: core deposits as a share of assets, reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F193 · Peers: ratios in the national top or bottom 10% · 2016-06-30 · 18 · data/features/fct_bank_features.parquet
- F194 · Peers: those ratios also unusual among peers · 2016-06-30 · 17 · data/features/fct_bank_features.parquet
- F196 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-06-30 · 10% · data/features/fct_bank_features.parquet
