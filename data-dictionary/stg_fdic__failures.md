# stg_fdic__failures

Every bank failure and assistance event in the FDIC's records since 1934, with readable column names plus an `is_failure` flag. A **view** over the raw Athena table `canary_raw.fdic_failures`. All rows are kept.

| | |
|---|---|
| Grain | One row per failure or assistance event |
| Primary key | None guaranteed (`cert` is null for old rows; `resolution_number` is not unique per row) |
| Source | `canary_raw.fdic_failures` (raw dictionary: [[fdic_failures]]) |
| Where it lives | Athena view `canary_staging.stg_fdic__failures` |
| Rows | 4,117 (3,524 FAILURE, 593 ASSISTANCE; 574 FAILURE since 2001) |

Model code: `warehouse/models/staging/stg_fdic__failures.sql`. Design: [[specs/2026-11-09-phase2-warehouse-design]].

## Read this first

- **Failures and assistance are mixed.** `is_failure` is true when `resolution_type` is `FAILURE` (the bank closed) and false for `ASSISTANCE` (the FDIC helped a bank that stayed open). Filter on it before using a row as a failure label. [[dim_failed_banks]] does this for you.
- **`cert` is null for old rows** (before 1977), so it is not a key.
- **Dollar amounts are in thousands of dollars.**
- **`pass_through_receivership_date` is text,** not a date, and mostly null.
- **`insurance_fund` and `insurance_fund_code` overlap.** See the caveat below the table.

## Columns

| Column | Type | Raw field | Meaning, units and caveats |
|---|---|---|---|
| `institution_name` | string | `name` | Legal name of the failed or assisted bank. Text. |
| `cert` | bigint | `cert` | FDIC certificate number; joins to financials. Integer; null for old pre-1977 rows. |
| `resolution_number` | string | `fin` | FDIC resolution number (FIN). Text; not guaranteed unique per row. |
| `headquarters_location` | string | `cityst` | City and state of the headquarters in one field. Text. |
| `failure_date` | date | `faildate` | Date the bank failed or was taken over. Date. |
| `failure_year` | bigint | `failyr` | Four-digit year of failure_date. Integer. |
| `insurance_fund_code` | string | `savr` | Insurance fund that covered the bank (SAVR). Code. |
| `transaction_type` | string | `restype1` | How the failure was resolved (A/A, P&A, PA, PI, IDT, ...). Code. |
| `charter_class` | string | `chclass1` | Charter type and primary regulator. Code. |
| `resolution_date` | date | `resdate` | Date of resolution; usually equals failure_date. Date. |
| `resolution_type` | string | `restype` | FAILURE (bank closed) or ASSISTANCE (stayed open). Text; uppercase. |
| `total_deposits_at_failure` | double | `qbfdep` | Total deposits at the last report before failure. $ thousands. |
| `total_assets_at_failure` | double | `qbfasset` | Total assets at the last report before failure. $ thousands. |
| `estimated_loss` | double | `cost` | Estimated loss to the Deposit Insurance Fund. $ thousands. Null before 1986. |
| `state` | string | `pstalp` | Two-letter state of the failed bank. Text. |
| `acquirer_city` | string | `bidcity` | City of the acquiring bank. Text; null for payouts. |
| `acquirer_name` | string | `bidname` | Name of the acquiring bank. Text; null for payouts. |
| `acquirer_state` | string | `bidstate` | State of the acquiring bank. Text; null for payouts. |
| `city` | string | `city` | City of the failed bank's main office. Text. |
| `insurance_fund` | string | `fund` | Insurance fund as a number 1 to 5 stored as text (1 = BIF/FDIC, 2 = RTC, 3 = FSLIC, 4 = SAIF, 5 = DIF). Code; coarser than insurance_fund_code (many-to-one), so prefer that one. |
| `pass_through_receivership_date` | string | `ptrdate` | Pass-through receivership date (RTC cases only). Text, not parsed to a date; mostly null. |
| `is_failure` | boolean | (derived from `restype`) | True when resolution_type is FAILURE (bank closed), false for ASSISTANCE. Boolean. |
| `ingested_at` | timestamp | `ingested_at` | When Canary pulled this row from the FDIC API. UTC timestamp; not an FDIC field. |

## Caveat: insurance_fund vs insurance_fund_code

Both columns name the insurance fund involved, so they overlap. They look like the same information in two encodings, not two facts. In the saved data (all 4,117 rows) `insurance_fund_code` (raw `savr`) holds names (BIF, SAIF, FSLIC, RTC, DIF, FDIC) while `insurance_fund` (raw `fund`) holds a number stored as text (1 to 5), and the two never contain the same text. `insurance_fund_code` maps to `insurance_fund` many-to-one, so `insurance_fund` is the coarser field: BIF and FDIC are both 1, RTC is 2, FSLIC is 3, SAIF is 4, DIF is 5. So `insurance_fund_code` is the more detailed and readable one, and `insurance_fund` adds no detail. Prefer `insurance_fund_code`. I did not look up FDIC's own definition of the numbers; the pairing is read from the data.
