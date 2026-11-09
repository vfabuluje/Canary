# fdic_failures

Every bank failure and assistance event in the FDIC's records since 1934. These are the failure labels for the model.

| | |
|---|---|
| Grain | One row per failure or assistance event |
| Primary key | None guaranteed. `CERT` is blank for old rows; `FIN` (FDIC's resolution number) is the closest identifier |
| Source | `GET https://api.fdic.gov/banks/failures` (FDIC BankFind) |
| File | `data/raw/failures/failures.parquet` |
| Rows | _filled in after the first full pull_ |

Design and reasoning: [[specs/2026-11-09-phase1-fdic-ingestion-design]]. Column names are FDIC's own. Values are stored exactly as published; the only conversion is blank to null.

## Read this before using the data

- **`CERT` is blank for 488 old rows (1934 to 1976)** and present for every row since 2001, so it is a nullable integer. Do not assume it is a key.
- **`RESTYPE` separates real failures from assistance.** `FAILURE` means the bank closed. `ASSISTANCE` means the FDIC helped a bank that stayed open (593 such rows). Both are kept; Phase 3 decides which count as "failed". For scale, there are 574 `FAILURE` rows since 2001.
- **Dollar amounts are in thousands of dollars** (`QBFASSET`, `QBFDEP`, `COST`).
- **Current, amended values only.** The API serves the latest figures, which may differ from what was first reported.
- **Dates are parsed to real dates.** `FAILDATE` and `RESDATE` arrive as text like `3/10/2023` and are stored as dates (2023-03-10). `PTRDATE` is left as text.
- **Blank is stored as null**, not as an empty string.

## Columns

| Column | Type | FDIC title | Meaning (plain English) | Units / caveats |
|---|---|---|---|---|
| `NAME` | string | Institution Name | Legal name of the failed or assisted bank. | |
| `CERT` | Int64 (nullable) | Cert | The bank's FDIC certificate number; the key for joining to the financials table. | Null for 488 pre-1977 rows; present for every row since 2001. |
| `FIN` | string | FIN | Financial Institution Number: an ID FDIC assigns to each assistance agreement, conservatorship, bridge bank or receivership (the resolution number). | Text. Not guaranteed unique per row: 61 FIN values appear on more than one row in the live API. |
| `CITYST` | string | Location | City and state of the bank's headquarters, in one field. | |
| `FAILDATE` | date | Effective Date | The date the bank stopped being a privately run going concern, i.e. when it failed or was taken over. SVB's is 2023-03-10. | Stored as a date. Source text format `m/d/yyyy`. |
| `FAILYR` | Int64 | Year | The four-digit year of `FAILDATE`. | |
| `SAVR` | string | Insurance Fund | Which insurance fund covered the bank: BIF, SAIF, FSLIC, RTC, DIF (merged the older funds in 2006), or FDIC (the pre-1989 FDIC fund). | Code. Historical. |
| `RESTYPE1` | string | Transaction Type | How the failure was resolved. Codes: A/A (assistance, bank stays open), REP (reprivatization), P&A, PA, PI (purchase and assumption: another bank takes over deposits and some assets), IDT (insured deposit transfer), MGR (FSLIC management takeover), PO (payout). PA = acquirer assumed all deposits; PI = insured deposits only. | Code. |
| `CHCLASS1` | string | Charter Class | The bank's charter type and primary regulator, such as national bank or state-chartered nonmember bank. | Code (e.g. `N`, `NM`, `SM`, `SA`, `SB`). |
| `RESDATE` | date | Date of Resolution | The date of resolution; usually the same as `FAILDATE`, except for open-bank assistance. | Stored as a date. |
| `RESTYPE` | string | Resolution | Whether this row is a `FAILURE` (the bank closed) or `ASSISTANCE` (the FDIC helped it stay open). | Uppercase values: `FAILURE` (3,524 rows) and `ASSISTANCE` (593 rows) in the live API. |
| `QBFDEP` | float64 | Total Deposits | Total deposits at the bank's last report before failure. | $ thousands. May not match the very last report filed. |
| `QBFASSET` | float64 | Total Assets | Total assets at the bank's last report before failure. | $ thousands. Excludes off-balance-sheet items. |
| `COST` | float64 | Estimated Loss | The estimated loss to the FDIC's Deposit Insurance Fund from this failure. | $ thousands. An estimate; not available for failures before 1986 or for FSLIC failures 1934 to 1988 (null). |
| `PSTALP` | string | State | Two-letter state code of the failed bank. | |
| `BIDCITY` | string | BIDCITY | City of the winning bidder (the bank that took over the failed one). | Null for payouts. |
| `BIDNAME` | string | BIDNAME | Name of the bank that took over the failed bank, the acquirer. | Null for payouts; sometimes missing for branch sales. |
| `BIDSTATE` | string | BIDSTATE | State of the winning bidder. | Null for payouts. |
| `CITY` | string | CITY | City of the failed bank's main office. | |
| `FUND` | string | Insurance fund | Insurance fund (BIF, RTC, FSLIC or SAIF); overlaps with `SAVR`. | Code. |
| `PTRDATE` | string | PTRDATE | Date of the pass-through receivership, which applied to RTC cases only. | Text, not parsed to a date. Mostly null. |
| `ingested_at` | datetime (UTC) | (added by Canary) | When Canary pulled this row from the FDIC API. | Not an FDIC field. Same value for every row in a pull. |
