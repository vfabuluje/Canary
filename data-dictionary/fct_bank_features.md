# fct_bank_features

The model-ready table Phase 3 trains on: 31 CAMELS-style ratios per bank per quarter, computed from [[fct_bank_quarters]]. A **table** built by dbt as Parquet under `s3://<bucket>/dbt/`.

| | |
|---|---|
| Grain | One row per bank (`cert`) per quarter (`report_date`) |
| Primary key | (`cert`, `report_date`); tested with `unique_combination_of_columns` |
| Source | [[fct_bank_quarters]] (self-joined to itself for the 4-quarter growth features) |
| Where it lives | Athena table `canary_marts.fct_bank_features` |
| Rows | Same as [[fct_bank_quarters]] (710,691); a singular test checks the counts match |

Model code: `warehouse/models/marts/fct_bank_features.sql`. Reasons for each choice: [[decisions/0009-features-and-zero-handling]].

## Read this first

- **Not a label table.** It has no `failure_date`, `quarters_until_failure` or bank name. Phase 3 joins the label on from [[fct_bank_quarters]] by (`cert`, `report_date`).
- **Two units.** Ratios FDIC supplies (equity_to_assets, leverage_ratio, both risk-based ratios, return_on_assets, return_on_equity, net_interest_margin, efficiency_ratio, loans_to_deposits) stay in **percent** (8.5 = 8.5%). Ratios computed here are **fractions** (0.085 = 8.5%). Trees do not care, but a human reading the table must.
- **Annualized.** Fields ending `_ann` take year-to-date dollars x 4 / quarter number, so Q1 to Q4 are comparable.
- **Nulls.** Every division uses `nullif(denominator, 0)`, so a zero or null denominator gives null, never an error. XGBoost reads null as missing.
- **0 becomes null** for the two risk-based ratios (0 means "not reported" after the 2020 community bank leverage ratio option) and for uninsured deposits. The HTM and AFS loss features are null when cost is above 0 but fair value is 0 or missing. All other zeros stay zeros. Evidence in decision 0009.
- **Growth looks back only.** It uses the same bank's row exactly 12 months earlier (matched on date). No such row means null. Nothing looks forward.

## Columns

| Column | Type | Built from | Meaning, units and caveats |
|---|---|---|---|
| `cert` | bigint | `cert` | FDIC certificate number: the bank's unique ID. Key with report_date. Integer. |
| `report_date` | date | `report_date` | Quarter-end date of the snapshot. Date. |
| `equity_to_assets` | double | `eqv` | **Capital.** FDIC's equity capital as a share of total assets (passed through from equity_to_assets_ratio). Percent, e.g. 8.5 means 8.5%. |
| `leverage_ratio` | double | `leverage_ratio` | **Capital.** Core capital as a share of average assets (FDIC leverage ratio), unchanged. Percent. |
| `tier1_risk_based_ratio` | double | `tier1_risk_based_ratio` | **Capital.** Tier 1 capital as a share of risk-weighted assets, unchanged except 0 becomes null (community bank leverage ratio banks stop reporting it from 2020). Percent. |
| `total_risk_based_ratio` | double | `total_risk_based_ratio` | **Capital.** Total regulatory capital as a share of risk-weighted assets, unchanged except 0 becomes null (same 2020 reason). Percent. |
| `noncurrent_loans_to_loans` | double | `noncurrent_loans`, `gross_loans_and_leases` | **Asset quality.** Loans 90+ days past due or not accruing interest, divided by gross loans. Fraction (0.02 = 2%). Null if no loans. |
| `nonaccrual_ore_to_assets` | double | `nonaccrual_assets`, `other_real_estate_owned`, `total_assets` | **Asset quality.** (Nonaccrual assets + foreclosed real estate) divided by total assets. Fraction. |
| `past_due_30_89_to_assets` | double | `past_due_30_89_assets`, `total_assets` | **Asset quality.** Assets 30-89 days past due and still accruing, divided by total assets. Fraction. |
| `allowance_to_loans` | double | `loan_loss_allowance`, `gross_loans_and_leases` | **Asset quality.** Loan-loss reserve divided by gross loans. Fraction. |
| `net_charge_offs_to_loans_ann` | double | `net_charge_offs`, `gross_loans_and_leases` | **Asset quality.** Net charge-offs (year-to-date x 4 / quarter number) divided by gross loans. Annualized fraction. |
| `provision_to_assets_ann` | double | `provision_for_credit_losses`, `total_assets` | **Asset quality.** Provision for credit losses (year-to-date x 4 / quarter number) divided by total assets. Annualized fraction. |
| `construction_loans_to_loans` | double | `construction_land_loans`, `gross_loans_and_leases` | **Asset quality.** Construction and land development loans divided by gross loans. Fraction; expected between 0 and 1. |
| `cre_loans_to_loans` | double | `commercial_real_estate_loans`, `gross_loans_and_leases` | **Asset quality.** Nonfarm nonresidential (commercial real estate) loans divided by gross loans. Fraction; expected between 0 and 1. |
| `texas_ratio` | double | `noncurrent_loans`, `other_real_estate_owned`, `equity_capital`, `loan_loss_allowance` | **Asset quality.** (Noncurrent loans + foreclosed real estate) divided by (equity + loan-loss reserve): bad assets relative to the cushion that absorbs them. Fraction; 1.0 means bad assets equal the whole cushion. |
| `return_on_assets` | double | `return_on_assets` | **Earnings.** FDIC's annualized profit as a share of assets, unchanged. Percent. |
| `return_on_equity` | double | `return_on_equity` | **Earnings.** FDIC's annualized profit as a share of equity, unchanged. Percent. |
| `net_interest_margin` | double | `net_interest_margin` | **Earnings.** FDIC's annualized net interest income as a share of earning assets, unchanged. Percent. |
| `efficiency_ratio` | double | `efficiency_ratio` | **Earnings.** FDIC's operating cost per dollar of revenue, unchanged. Percent. |
| `interest_expense_to_assets_ann` | double | `total_interest_expense`, `total_assets` | **Earnings.** Total interest expense (year-to-date x 4 / quarter number) divided by total assets. Annualized fraction. |
| `loans_to_deposits` | double | `net_loans_to_deposits_ratio` | **Liquidity.** FDIC's net loans and leases as a share of deposits, unchanged. Percent. |
| `uninsured_to_deposits` | double | `uninsured_deposits`, `total_deposits` | **Liquidity.** Estimated uninsured deposits divided by total deposits. Fraction; expected between 0 and 1. Uninsured of 0 is treated as not reported (null). |
| `brokered_to_deposits` | double | `brokered_deposits`, `total_deposits` | **Liquidity.** Brokered deposits divided by total deposits. Fraction; expected between 0 and 1. A 0 is a real zero. |
| `core_deposits_to_assets` | double | `core_deposits`, `total_assets` | **Liquidity.** Stable core deposits divided by total assets. Fraction. |
| `fhlb_to_assets` | double | `fhlb_advances`, `total_assets` | **Liquidity.** Federal Home Loan Bank advances divided by total assets. Fraction. |
| `volatile_liabilities_to_assets` | double | `volatile_liabilities`, `total_assets` | **Liquidity.** Funding that can leave quickly divided by total assets. Fraction. |
| `cash_to_assets` | double | `cash_and_due_from_banks`, `total_assets` | **Liquidity.** Cash and balances at other banks divided by total assets. Fraction. |
| `htm_unrealized_loss_to_equity` | double | `htm_securities_amortized_cost`, `htm_securities_fair_value`, `equity_capital` | **Sensitivity.** (Held-to-maturity amortized cost - fair value) divided by equity: how much of the cushion the unrealized bond loss would eat. Fraction (SVB 2022-12-31 is about 0.98). 0 when cost is 0; null when cost is above 0 but fair value is 0 or missing. |
| `afs_unrealized_loss_to_equity` | double | `afs_securities_amortized_cost`, `afs_securities_fair_value`, `equity_capital` | **Sensitivity.** (Available-for-sale amortized cost - fair value) divided by equity. Fraction. Same 0/null rule as the HTM feature. |
| `securities_to_assets` | double | `total_securities`, `total_assets` | **Sensitivity.** Total securities divided by total assets. Fraction. |
| `log_total_assets` | double | `total_assets` | **Size and growth.** Natural log of total assets ($ thousands): a bank-size measure. Null if assets are 0 or less. |
| `asset_growth_4q` | double | `total_assets` | **Size and growth.** Total assets now divided by total assets 12 months earlier, minus 1. Fraction (0.10 = 10% growth). Null when the bank has no row exactly 12 months earlier. Looks backward only. |
| `deposit_growth_4q` | double | `total_deposits` | **Size and growth.** Total deposits now divided by total deposits 12 months earlier, minus 1. Fraction. Null with no row 12 months earlier. Looks backward only. |

## Known data quirks

- **Range warnings (kept as-is).** Four dbt range tests warn on the live table, 183 rows of 710,691 in all: `uninsured_to_deposits` 144 rows outside [0, 1] (from -1.62 to 52.1, years 2002-2026, reporting errors), `brokered_to_deposits` 28 (mostly 1.00000x, max 70), `cre_loans_to_loans` 5 and `construction_loans_to_loans` 6 (just above 1.0). The features were not changed: tree models are robust to a few outliers and the cost of being wrong is a few noisy rows.
- **`texas_ratio` can be negative** when equity plus the loan-loss reserve is below 0 (the bank has no cushion left).
- **`htm_unrealized_loss_to_equity` and `afs_unrealized_loss_to_equity` are 0 when the securities cost is 0**, so "no securities" looks the same as "no loss". `securities_to_assets` tells them apart.

