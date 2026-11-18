---
cert: 19328
name: "Seaway Bank And Trust Company"
as_of: 2016-12-31
rank: 7
n_banks: 5983
percentile: 99.89971586160789
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:30"
writer_model: "claude-opus-5-5"
checked: true
---

# Seaway Bank And Trust Company (cert 19328)

*Hindsight: failed 2017-01-27. Canary flagged it 4 quarters ahead.*

## Summary

Seaway Bank And Trust Company, based in IL, ranked 7 out of 5,983 banks in Canary's national risk ranking as of 2016-12-31, placing it in the 99.9th percentile, where higher means riskier. Its capital, the cushion that absorbs losses, had turned negative, with equity at -1.9% of assets against a national median of 10.7%. Problem loans, meaning loans 90 or more days late or no longer paying interest, were 8.8% of loans versus a median of 0.6%, and the bank lost money, with a return on assets of -7.2% against a median of 0.9%. The bank was flagged on Canary's watchlist, which covers the top 2% of banks by score.

## Warning signs in the data

Capital was the clearest problem: the leverage ratio, core capital as a share of average assets, was -1.8% against a national median of 10.4%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was -3.1% versus a median of 15.0%, and the total risk-based capital ratio was -1.8% versus 16.2%. Earnings were deeply negative, with return on equity at -156.0% against a median of 8.0%, and the efficiency ratio, operating costs as a share of revenue, at 249.2% versus 69.7%.

Credit quality was weak across the board: loans 90 or more days past due or not accruing interest were 8.8% of loans versus a median of 0.6%. Loans that were recently past due but not yet seriously late, an early sign of trouble, were 5.4% of assets against a median of 0.3%, and nonaccrual assets plus foreclosed property were 4.1% of assets versus 0.5%. Net loan write-offs, loans given up as lost, ran at 1.3% of loans against a median of 0.1%, and commercial real estate loans made up 42.2% of loans versus 22.5%.

On funding, the bank leaned on Federal Home Loan Bank borrowings, a form of secured wholesale loan, at 14.3% of assets versus a median of 0.7%, and volatile funding was 17.7% of assets versus 5.2%. The bank was shrinking, with asset growth of -19.5% and deposit growth of -12.3% over the past four quarters, while the medians were 3.5% and 3.6%. It held cash of 17.1% of assets, well above the median of 6.6%, and unrealized losses on bonds available for sale were 1.7% of equity, above the median of 0.7%.

## Understanding the score

As of 2016-12-31, the bank ranked 7 out of 5,983 banks, the 99.9th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks, or 120 banks that quarter.

The five features pushing the score up most were the Tier 1 risk-based capital ratio at -3.1% (contribution +1.908), return on equity at -156.0% (+1.554), the total risk-based capital ratio at -1.8% (+0.881), the leverage ratio at -1.8% (+0.669), and loans 90 or more days past due or not accruing at 8.8% (+0.508).

The five features pulling the score down most were interest expense at 0.6% of assets (contribution -1.391), the Texas ratio, troubled assets against capital plus reserves, at -2563.3% (-1.043), construction loans at 4.1% of loans (-0.199), total assets of $297.8 million (-0.162), and commercial real estate loans at 42.2% of loans (-0.099).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 7 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 9 | 6,129 | ▲ watchlist |
| 2016-09-30 | 2 | 6,051 | ▲ watchlist |
| 2016-12-31 | 7 | 5,983 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged the bank in Q1 2016, at 2016-03-31, giving a lead time of 4 quarters before the bank failed on 2017-01-27. At that first flag, the main drivers were a Tier 1 risk-based capital ratio of 5.5% (contribution +1.369), a Texas ratio of 167.1% (+1.342), and return on equity of -63.1% (+1.324). Loans 90 or more days past due or not accruing were then 19.5% of loans (+0.741), and the total risk-based capital ratio was 6.8% (+0.472).

Looking back, capital was already thin and problem loans high at the first flag, and by the as-of quarter capital had turned negative.

## What happened next

In hindsight, the bank's last regulatory report covered the quarter ending 2016-12-31, and it failed on 2017-01-27. Because it stopped reporting after that, Canary has no later ranks or flags for it.

## Sources

- F1 · Bank name · n/a · Seaway Bank And Trust Company · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · -1.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 8.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 4.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-12-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2016-12-31 · 42.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-12-31 · 22.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 14.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 17.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 17.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 1.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -19.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -12.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2016-12-31 · +1.908 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -156.0%; contribution to the score · 2016-12-31 · +1.554 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value -1.8%; contribution to the score · 2016-12-31 · +0.881 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.8%; contribution to the score · 2016-12-31 · +0.669 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2016-12-31 · +0.508 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2016-12-31 · -1.391 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value -2563.3%; contribution to the score · 2016-12-31 · -1.043 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: construction loans as a share of loans, value 4.1%; contribution to the score · 2016-12-31 · -0.199 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $297.8 million; contribution to the score · 2016-12-31 · -0.162 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 42.2%; contribution to the score · 2016-12-31 · -0.099 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-01-27 · 2017-01-27 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 5.5%; contribution to the score · 2016-03-31 · +1.369 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 167.1%; contribution to the score · 2016-03-31 · +1.342 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -63.1%; contribution to the score · 2016-03-31 · +1.324 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 19.5%; contribution to the score · 2016-03-31 · +0.741 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 6.8%; contribution to the score · 2016-03-31 · +0.472 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
