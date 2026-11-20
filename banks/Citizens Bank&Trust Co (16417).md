---
cert: 16417
name: "Citizens Bank&Trust Co"
as_of: 2026-06-30
rank: 27
n_banks: 4313
percentile: 99.39717134245305
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:26"
writer_model: "claude-opus-5-5"
checked: true
---

# Citizens Bank&Trust Co (cert 16417)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Citizens Bank&Trust Co, a Louisiana bank, ranked 27 out of 4,313 banks nationally on Canary's risk score, which places it in the 99.4th percentile, and it is flagged on the watchlist. The main concern is loan quality: loans 90+ days past due or not accruing interest were 7.2% of loans, and its Texas ratio (troubled assets measured against capital plus reserves) was 42.7%, both far above the national medians. Its capital and cash cushions point the other way: its leverage ratio (core capital as a share of average assets) of 11.1% is close to the national median, and cash made up 20.8% of assets. The separate real-estate concentration check found that it did not cross either regulatory screening line.

## Warning signs in the data

Credit quality is where this bank stands out most. Loans 90+ days past due or not accruing interest were 7.2% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property (loans that have stopped earning interest, plus property taken back from borrowers) were 4.9% of assets, against a national median of 0.3%. Loans 30-89 days past due, an earlier stage of late payment, were 2.2% of assets versus a national median of 0.2%, and the Texas ratio was 42.7% versus a national median of 2.9%. Loan-loss reserves (money set aside for bad loans) were 1.3% of loans, only slightly above the national median of 1.2%.

Capital looks ordinary rather than weak: equity was 10.6% of assets, the same as the national median of 10.6%, and the leverage ratio was 11.1% against a median of 11.0%. Profitability is thinner than typical, with return on assets (profit as a share of assets) of 0.6% versus a national median of 1.2%, and an efficiency ratio (operating costs as a share of revenue) of 73.5% versus 62.1%. On bonds, unrealized losses on bonds available for sale equaled 8.3% of equity, above the national median of 5.6%, while losses on bonds held to maturity were 0.0%, matching the median of 0.0%.

Liquidity and funding mostly look sturdier than the loan book: cash was 20.8% of assets against a national median of 6.2%, uninsured deposits (balances above the insurance limit) were 20.1% of deposits versus a median of 24.8%, and brokered deposits were 0.0%. One exception is volatile funding (money that can leave quickly), at 12.7% of assets versus a national median of 9.0%. So the data point in two directions: troubled loans are well above normal, while capital and cash cushions are at or above typical levels.

## Understanding the score

As of 2026-06-30, the bank ranked 27 out of 4,313 banks, placing it in the 99.4th percentile on a 0 to 100 scale where higher means riskier. It is flagged on the watchlist, which covers 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were the Texas ratio at 42.7% (contribution +1.033), loans 90+ days past due or not accruing at 7.2% of loans (+0.906), unrealized losses on bonds available for sale at 8.3% of equity (+0.624), loans 30-89 days past due at 2.2% of assets (+0.091), and Federal Home Loan Bank borrowings, a common type of wholesale borrowing by banks, at 0.0% of assets (+0.015).

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio, a measure of core capital against riskier assets (contribution -0.707), the leverage ratio at 11.1% (-0.443), return on equity (profit as a share of the owners' stake) at 6.0% (-0.396), return on assets at 0.6% (-0.373), and loan-loss reserves at 1.3% of loans (-0.283).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,727 | 4,589 |  |
| 2024-12-31 | 1,054 | 4,560 |  |
| 2025-03-31 | 2,155 | 4,536 |  |
| 2025-06-30 | 1,579 | 4,494 |  |
| 2025-09-30 | 570 | 4,452 |  |
| 2025-12-31 | 61 | 4,411 | ▲ watchlist |
| 2026-03-31 | 42 | 4,353 | ▲ watchlist |
| 2026-06-30 | 27 | 4,313 | ▲ watchlist |

## How its ratios moved

As of its latest quarter, the bank ranked 27 out of 4,313 banks nationally, which puts it in the 99.4th percentile on a scale of 0 to 100 where higher means riskier. A year earlier it sat in the 64.9th percentile, and the model rated it riskier than a year earlier. Of 28 ratios compared with their own prior range, 5 were outside it, and those 5 are discussed below. The prior range covers the previous 12 quarters for most ratios, or the same quarter in the prior 3 years for year-to-date ratios.

Return on equity (profit as a share of the owners' stake) was 6.0%, below its prior range of 7.4% to 11.0%, yet its contribution of -0.396 model log-odds units pushed the score down. That ratio changed by -4.9 pp over four quarters. The annualized provision for loan losses (money set aside to cover expected bad loans) was 0.3% of assets, above its prior range of 0.0% to 0.1%, but its contribution of -0.105 model log-odds units pushed the score down. Net loan write-offs (loans written off as uncollectable, minus amounts later recovered) were 0.2% of loans, above a prior range of 0.0% to 0.0%, yet with a contribution of -0.001 model log-odds units they had little effect on the score.

Securities (bonds and similar investments) were 14.0% of assets, above their prior range of 12.1% to 13.8%, but with a contribution of -0.042 model log-odds units they had little effect on the score. Uninsured deposits (balances above the government deposit insurance limit) were 20.1% of deposits, above their prior range of 15.4% to 19.6%, yet with a contribution of +0.006 model log-odds units they had little effect on the score. That share rose by +0.5 pp over one quarter and by +2.3 pp over four quarters.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 6.0% | 7.4% to 11.0% | same quarter, prior 3 years | n/a | -4.9 pp | -0.396 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.2% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.2 pp | -0.001 | little effect on the score |
| annualized provision for loan losses as a share of assets | 0.3% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +0.2 pp | -0.105 | pushed the score down |
| securities as a share of assets | 14.0% | 12.1% to 13.8% | prior 12 quarters | +2.0 pp | +1.6 pp | -0.042 | little effect on the score |
| uninsured deposits as a share of deposits | 20.1% | 15.4% to 19.6% | prior 12 quarters | +0.5 pp | +2.3 pp | +0.006 | little effect on the score |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Nonaccrual assets and foreclosed property (loans that have stopped earning interest, plus property taken back from borrowers) made up 4.9% of the bank's assets, which is unusually high nationally at the 99.2nd percentile; at the 98.9th percentile among its peers, against a peer median of 0.3%, it is unusually high among its peers too. Loans 90+ days past due or not accruing interest were 7.2% of loans, unusually high nationally at the 99.0th percentile; at the 99.3rd percentile among its peers, against a peer median of 0.4%, this is unusually high among its peers too. The Texas ratio (troubled assets measured against capital plus loan-loss reserves) stood at 42.7%, unusually high nationally at the 99.0th percentile; at the 98.6th percentile among its peers, against a peer median of 3.0%, it is unusually high among its peers too.

Loans 30-89 days past due (early-stage late payments) equaled 2.2% of assets, unusually high nationally at the 97.3rd percentile; at the 97.6th percentile among its peers, against a peer median of 0.2%, this is unusually high among its peers too. Cash made up 20.8% of assets, unusually high nationally at the 91.6th percentile; at the 94.9th percentile among its peers, against a peer median of 6.5%, it is unusually high among its peers too. Overall, 5 of the bank's ratios sit in the national top or bottom 10%, and all 5 of those are also unusual when the bank is compared with its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 4.9% | 99.2nd (unusually high) | 0.3% | 98.9th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 7.2% | 99.0th (unusually high) | 0.4% | 99.3rd | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 42.7% | 99.0th (unusually high) | 3.0% | 98.6th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 2.2% | 97.3rd (unusually high) | 0.2% | 97.6th | unusually high among its peers too |
| cash as a share of assets | 20.8% | 91.6th (unusually high) | 6.5% | 94.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 51.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 158.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -26.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank's case is that it remains open and on the watchlist, and the fact sheet for this memo holds no data from after the as-of quarter. That means there is no later result yet to judge the flag against; its watchlist place rests on the troubled-loan figures described above, not on any known later event.

## What happened next

In hindsight: the fact sheet contains no ranks, flags or filings from after the as-of quarter, so we cannot report how the bank's rank moved or whether it kept reporting. The score history table added below shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Citizens Bank&Trust Co · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 27 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 42.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 73.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 20.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 42.7%; contribution to the score · 2026-06-30 · +1.033 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 7.2%; contribution to the score · 2026-06-30 · +0.906 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: losses on bonds available for sale, as a share of equity, value 8.3%; contribution to the score · 2026-06-30 · +0.624 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F74 · Driver up #4: loans 30-89 days past due, as a share of assets, value 2.2%; contribution to the score · 2026-06-30 · +0.091 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F75 · Driver up #5: Federal Home Loan Bank borrowings as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · +0.015 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.707 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: the leverage ratio (core capital as a share of average assets), value 11.1%; contribution to the score · 2026-06-30 · -0.443 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 6.0%; contribution to the score · 2026-06-30 · -0.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: return on assets (profit as a share of assets), value 0.6%; contribution to the score · 2026-06-30 · -0.373 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value 1.3%; contribution to the score · 2026-06-30 · -0.283 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 6.0% · data/features/fct_bank_features.parquet: return_on_equity
- F82 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: return_on_equity
- F83 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 11.0% · data/features/fct_bank_features.parquet: return_on_equity
- F84 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -4.9 pp · data/features/fct_bank_features.parquet: return_on_equity
- F85 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F86 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F87 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F88 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F93 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F94 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F95 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F97 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.105 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F98 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F99 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 14.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F100 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 12.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F101 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 13.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F104 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.042 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F105 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature securities_to_assets contribution
- F106 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 20.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F107 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 15.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F108 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 19.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F109 · Trend: uninsured deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +0.5 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F110 · Trend: uninsured deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +2.3 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.006 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F112 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F113 · Trend: ratios outside their own prior range · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F114 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F115 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F116 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F117 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F118 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 64.9% · data/analyst/scores.parquet: percentile
- F119 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F123 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F125 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F126 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F127 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F128 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F129 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F130 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F131 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F132 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F133 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F134 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 42.7% · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F142 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.3rd · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F143 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F144 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.6th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F145 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F146 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F147 · Peers: cash as a share of assets, bank value at the as-of quarter · 2026-06-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F148 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 91.6th · data/features/fct_bank_features.parquet: cash_to_assets
- F149 · Peers: cash as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: cash_to_assets
- F150 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 94.9th · data/features/fct_bank_features.parquet: cash_to_assets
- F151 · Peers: cash as a share of assets, peer median · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F152 · Peers: cash as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: cash_to_assets
- F154 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F155 · Peers: those ratios also unusual among peers · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F157 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
