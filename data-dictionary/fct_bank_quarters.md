# fct_bank_quarters

The main table Phase 3 reads: every [[stg_fdic__financials]] column, plus the bank's failure date and how many quarters away that failure was. A **table** built by dbt as Parquet under `s3://<bucket>/dbt/`.

| | |
|---|---|
| Grain | One row per bank (`cert`) per quarter (`report_date`) |
| Primary key | (`cert`, `report_date`); tested with `unique_combination_of_columns` |
| Source | [[stg_fdic__financials]] left-joined to [[dim_failed_banks]] on `cert` |
| Where it lives | Athena table `canary_marts.fct_bank_quarters` |
| Rows | 710,691 (same as [[stg_fdic__financials]]; the join adds no rows) |

Model code: `warehouse/models/marts/fct_bank_quarters.sql`.

## Read this first

- **`failure_date` and `quarters_until_failure` are LABELS ONLY. Never use them as model inputs.** They are only known after the fact. Using them as features would leak the answer to the model. Phase 3 builds the training label from them; it does not feed them in.
- **This table does not define the training label.** It only stores the facts; Phase 3 decides what counts as "fails within 4 quarters".
- **`quarters_until_failure`** counts calendar quarters from the report quarter to the failure quarter (0 = the bank failed in the same quarter as the report). Null for banks that never failed since 2001. A data test requires it to be 0 or more. Check: SVB (cert 24735) and Signature (57053) at 2022-12-31 have 1, and First Republic (59017) at 2023-03-31 has 1.
- **Same unit caveats as staging:** dollars in thousands, ratios in percent, income fields year-to-date, zeros stay zeros, amended values only. See [[stg_fdic__financials]].
- **Banks that failed before 2001 never get a failure date,** because [[dim_failed_banks]] only covers 2001 onward.

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
| `failure_date` | date | (from [[dim_failed_banks]]) | LABEL ONLY, never a model input. Date this bank failed, from dim_failed_banks. Date; null if the bank never failed (or failed before 2001). |
| `quarters_until_failure` | integer | (calculated) | LABEL ONLY, never a model input. Calendar quarters from report_date to the failure quarter (0 = failed in the same quarter). Integer; null if the bank never failed. Negative would mean a report after failure. |
