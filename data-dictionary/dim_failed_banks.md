# dim_failed_banks

The banks that actually failed (not assisted) since 2001, with their failure date. A **table** built by dbt as Parquet under `s3://<bucket>/dbt/`. It exists so other tables can look up "did this bank fail, and when".

| | |
|---|---|
| Grain | One row per failed bank |
| Primary key | `cert`; tested `unique` and `not_null`, so a duplicate fails loudly instead of being picked silently |
| Source | [[stg_fdic__failures]], filtered to `is_failure`, `failure_year >= 2001` and `cert` not null |
| Where it lives | Athena table `canary_marts.dim_failed_banks` |
| Rows | 574 |

Model code: `warehouse/models/marts/dim_failed_banks.sql`.

## Read this first

- **Only real failures since 2001.** Assistance events, pre-2001 failures and rows with no `cert` are left out.
- **One expected warning.** A `relationships` test checks that each `cert` also appears in [[stg_fdic__financials]]. It is set to warn, not fail. It warns for cert 34264 (First Alliance Bank and Trust Co), which failed on 2001-02-02, before the first financials quarter (2001-03-31), so it has no financial rows. Nothing is wrong; that bank simply cannot be matched.
- **Dollar amounts are in thousands of dollars.**

## Columns

| Column | Type | Raw field | Meaning, units and caveats |
|---|---|---|---|
| `cert` | bigint | `cert` | FDIC certificate number; joins to financials. Integer; never null here (rows without a cert are filtered out). |
| `institution_name` | string | `name` | Legal name of the failed bank (assistance transactions are excluded). Text. |
| `failure_date` | date | `faildate` | Date the bank failed or was taken over. Date. |
| `estimated_loss` | double | `cost` | Estimated loss to the Deposit Insurance Fund. $ thousands. Null before 1986. |
| `total_assets_at_failure` | double | `qbfasset` | Total assets at the last report before failure. $ thousands. |
