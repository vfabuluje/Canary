# stg_fdic__financials

Quarterly financial snapshot of every FDIC-insured bank, with readable column names. This is the first dbt layer: a **view** (no stored copy) over the raw Athena table `canary_raw.fdic_financials`. It only renames and retypes; it does not clean anything.

| | |
|---|---|
| Grain | One row per bank (`cert`) per quarter (`report_date`) |
| Primary key | (`cert`, `report_date`); tested with `unique_combination_of_columns` |
| Source | `canary_raw.fdic_financials` (raw dictionary: [[fdic_financials]]) |
| Where it lives | Athena view `canary_staging.stg_fdic__financials` |
| Rows | 710,691 over 102 quarters (2001-03-31 to 2026-06-30). Equals the raw row count; a test checks nothing is dropped |

Model code: `warehouse/models/staging/stg_fdic__financials.sql`. Design: [[specs/2026-11-09-phase2-warehouse-design]].

## Read this first

- **Same numbers as the raw table, new names.** Only the names and the date type change. See [[fdic_financials]] for the full meaning of each FDIC field.
- **Dollar amounts are in thousands of dollars.** SVB's `total_assets` of 209,026,000 means $209 billion.
- **Ratios are percent.** A `leverage_ratio` of 7.96 means 7.96%.
- **Income fields are year-to-date** (`net_income`, `total_interest_expense`, `provision_for_credit_losses`, `net_charge_offs`): Q4 covers the whole year, Q1 one quarter. Phase 3 converts them to per-quarter values. `return_on_assets`, `return_on_equity` and `net_interest_margin` are annualized year-to-date ratios.
- **Zeros stay zeros.** A 0 can mean "not reported" (for example the securities fields in early years). Phase 3 decides how to treat it.
- **Amended values only.** The FDIC serves the latest corrected figures, not what a bank first filed.
- **`report_date`** comes from the raw partition text `repdte` (for example `20221231`), converted to a real date.

## Columns

| Column | Type | Raw field | Meaning, units and caveats |
|---|---|---|---|
| `cert` | bigint | `cert` | FDIC certificate number: the bank's unique ID. Key with report_date. Integer. |
| `report_date` | date | `repdte` | Quarter-end date of the snapshot (from raw repdte). Date, e.g. 2022-12-31. |
| `institution_name` | string | `name` | The bank's legal name as of that quarter. Text; names change over time. |
| `state` | string | `stalp` | Two-letter state where the bank is based. Text. |
| `institution_class` | string | `bkclass` | Charter class: type of bank charter and supervisor (FDIC class code). Code. |
| `holding_company_name` | string | `namehcr` | Regulatory top-holder holding company name. Text; null if no holding company. |
| `total_assets` | double | `asset` | Everything the bank owns; the standard size measure. $ thousands. |
| `total_liabilities` | double | `liab` | Everything the bank owes. $ thousands. |
| `total_deposits` | double | `dep` | Money customers have placed in the bank. $ thousands. |
| `equity_capital` | double | `eq` | Assets minus liabilities: the loss-absorbing cushion. $ thousands. |
| `gross_loans_and_leases` | double | `lnlsgr` | Total loans and leases before loss reserves. $ thousands. |
| `total_securities` | double | `sc` | Total bonds and other securities held. $ thousands. |
| `leverage_ratio` | double | `rbc1aaj` | Core capital as a share of average assets (PCA leverage ratio). Percent. |
| `tier1_risk_based_ratio` | double | `idt1rwajr` | Tier 1 capital as a share of risk-weighted assets. Percent. May be null or 0 in early years. |
| `total_risk_based_ratio` | double | `rbcrwaj` | Total regulatory capital as a share of risk-weighted assets. Percent. |
| `equity_to_assets_ratio` | double | `eqv` | Equity capital as a share of total assets. Percent. |
| `noncurrent_loans` | double | `nclnls` | Loans 90+ days past due or no longer accruing interest. $ thousands. |
| `nonaccrual_assets` | double | `naasset` | Assets on which interest is no longer being counted. $ thousands. |
| `past_due_30_89_assets` | double | `p3asset` | Assets 30-89 days past due and still accruing. $ thousands. |
| `past_due_90_plus_assets` | double | `p9asset` | Assets 90+ days past due and still accruing. $ thousands. |
| `other_real_estate_owned` | double | `ore` | Foreclosed property held by the bank. $ thousands. |
| `loan_loss_allowance` | double | `lnatres` | Reserve set aside for expected loan losses. $ thousands. |
| `net_charge_offs` | double | `ntlnls` | Loans written off minus recoveries. $ thousands, year-to-date (Q4 = full year). |
| `provision_for_credit_losses` | double | `elnatr` | Amount charged to earnings to add to the loss reserve. $ thousands, year-to-date (Q4 = full year). |
| `real_estate_loans` | double | `lnre` | Loans secured by real estate. $ thousands. |
| `construction_land_loans` | double | `lnrecons` | Real estate construction and land development loans. $ thousands. |
| `commercial_real_estate_loans` | double | `lnrenres` | Nonfarm nonresidential real estate loans. $ thousands. |
| `commercial_industrial_loans` | double | `lnci` | Commercial and industrial (business) loans. $ thousands. |
| `net_income` | double | `netinc` | Profit after all expenses and taxes. $ thousands, year-to-date (Q4 = full year). |
| `return_on_assets` | double | `roa` | Profit as a share of assets. Percent. Annualized, year-to-date. |
| `return_on_equity` | double | `roe` | Profit as a share of equity. Percent. Annualized, year-to-date. |
| `net_interest_margin` | double | `nimy` | Interest earned minus interest paid, as a share of earning assets. Percent. Annualized, year-to-date. |
| `total_interest_expense` | double | `eintexp` | Total interest paid on deposits and borrowings. $ thousands, year-to-date (Q4 = full year). |
| `efficiency_ratio` | double | `eeffr` | Operating costs per dollar of revenue. Percent. Ratio of two year-to-date amounts; not annualized. |
| `uninsured_deposits` | double | `depunins` | Estimated deposits above the federal insurance limit. $ thousands. Estimate; often 0 or null for small banks and early years. |
| `brokered_deposits` | double | `bro` | Deposits obtained through brokers. $ thousands. |
| `core_deposits` | double | `coredep` | Stable deposits (broadly total minus large time and brokered). $ thousands. |
| `fhlb_advances` | double | `othbfhlb` | Federal Home Loan Bank advances (other liabilities-FHLB). $ thousands. |
| `volatile_liabilities` | double | `voliab` | Funding that can leave quickly. $ thousands. |
| `cash_and_due_from_banks` | double | `chbal` | Cash and balances at other banks. $ thousands. |
| `net_loans_to_deposits_ratio` | double | `lnlsdepr` | Net loans and leases as a share of deposits. Percent. |
| `htm_securities_amortized_cost` | double | `scha` | Held-to-maturity securities at amortized cost. $ thousands. 0 may mean not reported. |
| `htm_securities_fair_value` | double | `schf` | Held-to-maturity securities at market value. $ thousands. 0 may mean not reported. |
| `afs_securities_amortized_cost` | double | `scaa` | Available-for-sale securities at amortized cost. $ thousands. 0 may mean not reported. |
| `afs_securities_fair_value` | double | `scaf` | Available-for-sale securities at market value. $ thousands. 0 may mean not reported. |
| `ingested_at` | timestamp | `ingested_at` | When Canary pulled this row from the FDIC API. UTC timestamp; not an FDIC field. |
