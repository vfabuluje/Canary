# 0009 — Model features and how zeros are handled

**Date:** 2026-11-11
**Status:** Accepted

## Decision
`fct_bank_features` holds 31 features per bank per quarter, built in dbt from `fct_bank_quarters`. Features are grouped by CAMELS (Capital, Asset quality, Management/Earnings, Liquidity, Sensitivity), plus size and growth.

**Units rule.** Ratios FDIC already supplies stay in percent, unchanged (8.5 means 8.5%). Ratios computed here are fractions (0.085). Every division uses `nullif(denominator, 0)`, so a zero or missing denominator gives null instead of an error. Dollar fields are in thousands, so ratios have no unit. Year-to-date dollar fields are annualized as value x 4 / quarter number.

**Features, one plain line each**
- Capital: `equity_to_assets` (cushion vs size); `leverage_ratio` (core capital vs average assets); `tier1_risk_based_ratio`, `total_risk_based_ratio` (capital vs risk-weighted assets).
- Asset quality: `noncurrent_loans_to_loans` (share of loans 90+ days late); `nonaccrual_ore_to_assets` (stopped-paying assets plus foreclosed property vs size); `past_due_30_89_to_assets` (early late payments); `allowance_to_loans` (reserve vs loans); `net_charge_offs_to_loans_ann` (loans written off per year); `provision_to_assets_ann` (loss reserve top-ups per year); `construction_loans_to_loans`, `cre_loans_to_loans` (concentration in risky real estate); `texas_ratio` (see below).
- Earnings: `return_on_assets`, `return_on_equity`, `net_interest_margin`, `efficiency_ratio` (FDIC profit measures); `interest_expense_to_assets_ann` (cost of funding).
- Liquidity: `loans_to_deposits`; `uninsured_to_deposits` (share of deposits above the $250K limit, the SVB run risk); `brokered_to_deposits`; `core_deposits_to_assets`; `fhlb_to_assets` (borrowing from the Home Loan Banks); `volatile_liabilities_to_assets`; `cash_to_assets`.
- Sensitivity: `htm_unrealized_loss_to_equity`, `afs_unrealized_loss_to_equity` (bond losses vs cushion; SVB 2022-12-31 HTM is about 0.98); `securities_to_assets`.
- Size and growth: `log_total_assets`; `asset_growth_4q`, `deposit_growth_4q` (vs the same bank's row exactly 12 months earlier, matched on date; null if absent; never forward-looking).

**Why `texas_ratio` is included.** It is a classic failure screen from the early-1990s Texas banking crisis: bad assets (noncurrent loans + foreclosed property) divided by the cushion that absorbs them (equity + loan-loss reserve). It is one line to explain and combines asset quality and capital in a way no single feature does.

## Zero handling: 0 becomes null only where "0" means "not reported"
XGBoost treats null as "missing" and learns from it; a fake 0 would teach it something false. I profiled the share of banks with exactly 0 in each raw field at every year-end 2001-2025 (local `data/raw/financials`, pandas, read-only). Rules adopted:

| Field | Evidence | Rule |
|---|---|---|
| `idt1rwajr` (tier 1 risk-based) | 0 for about 1.2% of banks every year to 2019, then 38.6% in 2020, 36.1% in 2022, 38.6% in 2024 | 0 to null. The jump is the 2020 community bank leverage ratio option: small banks stop reporting risk-based ratios |
| `rbcrwaj` (total risk-based) | 0.2-0.3% to 2019, then 37.9% in 2020, 35.3% in 2022, 37.7% in 2024 | 0 to null, same reason |
| `depunins` (uninsured deposits) | 0 for 1-3% of banks, never null; no regime change | 0 to null (spec rule): a bank with real deposits and exactly 0 uninsured is not believable |
| HTM `scha`/`schf`, AFS `scaa`/`scaf` | `schf` is **null** (not 0) for about 8% of banks with cost above 0 in 2001-2010 (786 banks at 2001-12-31, 521 at 2010-12-31, 0 at 2022-12-31). Cost > 0 with fair value exactly 0 is rare (at most 2 banks per sampled year-end); cost 0 with fair value above 0 also at most 2. Zero-share of `scha` is about 47% in 2001 rising to about 60-66% later (banks with no HTM bonds: a real 0) | Loss feature is 0 when cost is 0; null when cost > 0 and fair value is 0 **or null**; otherwise (cost - fair value) / equity. AFS likewise |

The profile found the case the spec expected (cost above 0, fair value missing) mostly shows as null in the raw data, not 0, so the CASE treats both the same. A secondary effect: the loss feature is null for roughly 8% of early-year banks that hold HTM bonds.

**Left as real zeros (no "not reported" pattern):**
- `brokered_deposits` (bro) 52-82% zeros, `fhlb_advances` 35-53%, `other_real_estate_owned` 22-73%, `past_due_90_plus_assets` 32-57%, `nonaccrual_assets` 12-25%, `past_due_30_89_assets` 6-14%, `net_charge_offs` 6-14%, `provision_for_credit_losses` 7-26%, `construction_land_loans` 10-16%: these move smoothly with the economy (e.g. ORE zeros fall in 2009-2011 and climb after) and zero is a normal value for a small bank.
- `leverage_ratio`, `equity_to_assets_ratio`, `return_on_assets`, `return_on_equity`, `net_interest_margin`, `efficiency_ratio`, assets, deposits, equity, loans: 0-1% zeros in every year with no jump. Denominators of 0 are already protected by `nullif`.
- README check: the data shows `depunins` filled for about 99% of banks at every year-end, so the README line "mainly available for $1B+ banks" looks wrong and should be corrected (README is not edited in this task).

## Alternatives
1. **Convert every 0 to null.** Rejected: brokered deposits and HTM bonds are truly 0 for most banks; nulling them hides that signal.
2. **Leave all zeros.** Rejected: a 0 risk-based ratio would look like a catastrophically capitalized bank in 2020+ when it only means "not reported".
3. **Percent everywhere.** Rejected: rewriting FDIC's own ratios adds code for no gain; the two-unit rule is documented in the data dictionary.

Related: [[decisions/0004-store-raw-values-unchanged]], [[data-dictionary/fct_bank_features]].
