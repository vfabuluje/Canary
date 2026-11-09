# Phase 1 Spec — FDIC Financials + Failed Bank List → Local Parquet

**Date:** 2026-11-09
**Status:** Draft (awaiting approval)
**Phase:** 1 (see `CLAUDE.md`)

## 1. Intent: why this exists

Canary has to score every FDIC-insured bank's risk of failing within the next 4 quarters, then show whether it would have flagged SVB, Signature Bank and First Republic in 2023. Everything later (features, labels, the XGBoost model, the SVB replay) is built on two raw tables:

1. **Quarterly financials** for every FDIC-insured bank, 2001 Q1 to the latest published quarter.
2. **The FDIC failed bank list**, the source of failure labels ("this bank failed on this date").

Phase 1 builds a **repeatable, tested Python pull** that saves both tables as local Parquet files. It must be simple enough to explain line by line in a data-engineering interview.

### What the data already shows (recon, 2026-11-09)
SVB's (CERT 24735) 2022 Q4 filing, the last one before it failed, already contains the warning signs:

| Signal | Field(s) | Value |
|---|---|---|
| Unrealized loss on long-term bonds | `SCHA` − `SCHF` | $91.3B cost − $76.2B fair value = **$15.2B loss** |
| Equity (the cushion) | `EQ` | $15.5B, so the bond loss was about the size of all equity |
| Uninsured deposits | `DEPUNINS` / `DEP` | $151.6B / $175.4B = **86%** |

So Phase 1 alone captures SVB's core story; Phase 2's FFIEC call reports add detail.

## 2. Goals
- G1. Pull the ~45 fields listed in §6 for **every bank and every quarter from 2001 Q1 to the latest available** (currently 2026 Q2 = 102 quarters, about 650k rows).
- G2. Pull the **full failed bank list** (all ~4,117 rows back to 1934; filtering to 2001+ happens later).
- G3. Save the financials as **one Parquet file per quarter**, and the failures as one Parquet file.
- G4. **Resumable and incremental:** a rerun skips quarters already saved, so a crash at quarter 80 doesn't restart from zero, and a new quarter costs one API call.
- G5. **Tests** for the pipeline code (no network) plus **data checks** on the saved files.
- G6. Every table and column documented in `data-dictionary/`; choices logged in `decisions/`.

## 3. Non-goals (later phases)
- No feature engineering, ratios, or failure labels (Phase 3).
- No S3 / Athena / dbt (Phase 2). The folder layout is chosen so Phase 2 can upload it unchanged.
- No FFIEC call reports or FRED data.
- No scheduling or automation (GitHub Actions comes later).

## 4. Anti-goals (a failure even if the code "works")
- **Silently missing data.** A quarter that returned fewer rows than the API reported, or a bank dropped by pagination, must be an error, not a smaller file.
- **Changing the values.** No filling blanks, no converting 0 to null or null to 0, no rescaling. Phase 1 stores what the FDIC published. Cleaning is a later, documented step.
- **Credentials or data in git.** `data/` stays gitignored. The FDIC API needs no key.
- **Unexplainable code.** No framework or abstraction Victor couldn't walk through in an interview.

## 5. Approaches considered

| # | Approach | Trade-off | Verdict |
|---|---|---|---|
| 1 | **One Parquet file per quarter** (`repdte=YYYYMMDD/`) | Resumable, incremental, same layout as S3/Athena partitions in Phase 2. About 100 small files. | **Chosen** |
| 2 | One big Parquet file rebuilt each run | Least code, but any failure restarts everything and every refresh re-downloads ~650k rows. | Rejected |
| 3 | Save raw JSON first, convert to Parquet in a second step | Textbook raw→clean pattern, but twice the code and storage. The FDIC API can simply be called again. | Rejected |

Field scope: **~45 hand-picked fields** (chosen) rather than the API's default ~160 or all 2,378. Small, fast, and fully documentable. The field list lives in one Python file, so adding a field is one line plus a re-pull.

## 6. Data sources and fields

### 6.1 Financials: `GET https://api.fdic.gov/banks/financials`
- Filter by quarter: `filters=REPDTE:YYYYMMDD`, `fields=<comma list>`, `limit=10000` (the API maximum).
- Row counts per quarter: about 9,940 (2001 Q1) down to 4,313 (2026 Q2). This is under the 10,000 limit, but **the code must still page with `offset` if `meta.total` exceeds `limit`**, and must check that rows received equals `meta.total`.
- One call takes about 5 s (measured: 2008 Q4, 8,395 rows, 6.6 MB of JSON).
- Response shape: `{"meta": {"total": N, ...}, "data": [{"data": {FIELD: value, ...}}, ...]}`.

**Units and caveats (to go in the data dictionary):**
- Dollar amounts are in **thousands of dollars** (SVB `ASSET` = 209,026,000, which is $209B).
- Ratios (`ROA`, `NIMY`, `RBC1AAJ`, …) are **percent** (7.96 means 7.96%).
- The dollar income fields (`NETINC`, `EINTEXP`, `ELNATR`, `NTLNLS`) are **year-to-date**: Q4 covers the full year and Q1 covers one quarter. Phase 3 must convert them to per-quarter values. `ROA`, `ROE` and `NIMY` are annualized year-to-date ratios, already comparable across quarters; `EEFFR` is a ratio of two YTD amounts and needs no conversion.
- **0 can mean "not reported yet".** Some fields didn't exist in early years. Example: SVB's `SCHF` (HTM fair value) is 0 in 2001. Phase 1 keeps the 0; Phase 3 decides how to treat it.

**Curated field list (45):**

| Group | Fields |
|---|---|
| Identity (6) | `CERT` (FDIC certificate #, the join key), `REPDTE` (report date), `NAME`, `STALP` (state), `BKCLASS` (charter class), `NAMEHCR` (holding company) |
| Size (6) | `ASSET`, `LIAB`, `DEP`, `EQ`, `LNLSGR` (gross loans), `SC` (total securities) |
| Capital (4) | `RBC1AAJ` (leverage ratio), `IDT1RWAJR` (tier 1 risk-based ratio), `RBCRWAJ` (total risk-based ratio), `EQV` (equity / assets) |
| Asset quality (8) | `NCLNLS` (noncurrent loans), `NAASSET` (nonaccrual assets), `P3ASSET` (30–89 days past due), `P9ASSET` (90+ days past due), `ORE` (foreclosed real estate), `LNATRES` (loan loss allowance), `NTLNLS` (net charge-offs), `ELNATR` (provision for credit losses) |
| Loan mix (4) | `LNRE` (real-estate loans), `LNRECONS` (construction and land development), `LNRENRES` (commercial real estate), `LNCI` (commercial and industrial) |
| Earnings (6) | `NETINC`, `ROA`, `ROE`, `NIMY` (net interest margin), `EINTEXP` (interest expense), `EEFFR` (efficiency ratio) |
| Liquidity and funding (7) | `DEPUNINS` (estimated uninsured deposits), `BRO` (brokered deposits), `COREDEP` (core deposits), `OTHBFHLB` (FHLB advances), `VOLIAB` (volatile liabilities), `CHBAL` (cash), `LNLSDEPR` (loans / deposits) |
| Securities / interest-rate risk (4) | `SCHA` (HTM at amortized cost), `SCHF` (HTM at fair value), `SCAA` (AFS at amortized cost), `SCAF` (AFS at fair value) |

All 45 were confirmed against the FDIC field catalog (`risview_properties.yaml`) and returned values for SVB in 2022 Q4.

### 6.2 Failures: `GET https://api.fdic.gov/banks/failures`
- One call, `limit=10000`, all 21 fields. Currently 4,117 rows.
- Key fields: `CERT`, `NAME`, `FAILDATE` (text like `"3/10/2023"`), `FAILYR`, `RESTYPE` (`FAILURE` vs `ASSISTANCE`), `RESTYPE1` (transaction type), `CHCLASS1`, `QBFASSET`/`QBFDEP` (assets and deposits at failure, in $thousands), `COST` (estimated cost to the deposit insurance fund, in $thousands), `CITYST`, `BIDNAME` (acquirer), `FIN`.
- Keep all rows, including `ASSISTANCE` (open-bank assistance, not a closure; 593 rows). Phase 3 decides which ones count as "failed". Don't filter it away now. For scale: 574 `FAILURE` rows since 2001.
- **`CERT` is blank for 488 old rows (1934–1976)** and present for every row since 2001 (checked 2026-11-09). So in this table `CERT` is a *nullable* integer (pandas `Int64`).

## 7. Design: the parts that are decided

### 7.1 Output layout
```
data/raw/
  financials/
    repdte=20010331/part.parquet
    repdte=20010630/part.parquet
    ...
    repdte=20260630/part.parquet
  failures/
    failures.parquet
```
`repdte=YYYYMMDD` is Hive-style partition naming, which Athena and pandas both understand. `data/` is already gitignored.

### 7.2 Column conventions
- **Keep FDIC's column names as-is** (`ASSET`, `DEPUNINS`, …) so every column can be looked up in the FDIC docs. Friendlier names come in dbt (Phase 2).
- Types are set by the field list, not guessed: identity text as `string`, `CERT` as `int64` in financials (nullable `Int64` in failures, see §6.2), dollar amounts and ratios as `float64` (nullable, values unchanged).
- `REPDTE`, `FAILDATE` and `RESDATE` are parsed from text and stored as a Parquet **timestamp at midnight (no time part)**, e.g. 2022-12-31 00:00.
- Add one lineage column, `ingested_at` (UTC timestamp of the pull), to both tables.

### 7.3 Behaviour
- **Quarters to pull:** every quarter-end from 2001-03-31 to the latest `REPDTE` the API reports (ask the API rather than guess from today's date).
- **Resume:** skip a quarter if its `part.parquet` already exists.
- **Refresh recent quarters:** banks amend recent filings, so each run re-pulls the **latest 2 quarters** even if the files exist, overwriting them (no snapshots kept). A `--force` flag re-pulls everything.
- **Known limitation, not a Phase 1 problem:** the FDIC API serves only the *current, amended* values for every quarter, not what was originally filed. So the SVB replay uses numbers as corrected later, not exactly what an analyst saw in early 2023. Log this in the decisions note and the README limitations.
- **Atomic writes:** write to a temporary file, then rename it, so a crash never leaves a half-written `part.parquet` that resume would trust.
- **Completeness check:** rows received must equal `meta.total`, otherwise raise an error and write nothing for that quarter.
- **Retries:** retry timeouts, HTTP 429 and 5xx up to 3 times with growing waits, then fail loudly. Add a short pause between calls to stay polite to the API.
- **Logging:** one log line per quarter (quarter, rows, seconds, skipped/pulled).

### 7.4 How it's run
Command-line entry points (exact names left to the builder), for example:
```
python -m canary.ingest financials            # resume + refresh latest 2
python -m canary.ingest financials --force    # re-pull everything
python -m canary.ingest failures              # always re-pull (one call)
```

### 7.5 Tests
- **Unit tests (no network, run every time):** HTTP responses are faked. They cover: building the quarter list; parsing the response into a typed DataFrame; the row-count-mismatch error; paging when `total > limit`; retry then give up; resume skips existing files; the latest-2 refresh; date parsing (`"3/10/2023"` → 2023-03-10); the atomic write leaving no partial file.
- **Data checks (run on the real saved files, skipped if `data/` is empty):** (`CERT`, `REPDTE`) is unique; every quarter has between 3,000 and 12,000 rows; no quarter is missing between 2001 Q1 and the latest; SVB 2022 Q4 `ASSET` = 209,026,000; SVB (3/10/2023), Signature Bank (CERT 57053, 3/12/2023) and First Republic (CERT 59017, 5/1/2023) are in the failures file with those dates; `CERT` is never null in financials, and never null in failures for `FAILYR` ≥ 2001. These play the role of dbt data tests until Phase 2.
- **Dictionary check:** a test fails if any field in the field list is missing from `data-dictionary/`.

### 7.6 Documentation outputs
- `data-dictionary/fdic_financials.md` and `data-dictionary/fdic_failures.md`: each column with its FDIC title, a plain-English meaning, units, and caveats from §6.
- `decisions/`: one note each for Parquet partitioned by quarter, the curated field list, and keeping raw values unchanged.
- `daily-log.md`: progress at the end of the session.
- `runbooks/`: how to run the pull and what to do if it fails partway.

## 8. Constraints
- Python 3.12 (installed). Local only, no AWS cost.
- Libraries: `pandas`, `pyarrow`, `requests`, `pytest`. Nothing heavier.
- The FDIC API is public with no key. Don't put any personal info in request headers.
- Full pull: about 102 calls × about 5 s, roughly 10 minutes.

## 9. Left to the builder
- Package layout and module names (expected: `src/canary/` with a small HTTP client, the field list, and one module per table).
- `pyproject.toml` vs `requirements.txt`, and virtual-env tooling.
- Exact CLI names and flags beyond §7.4's behaviour.
- Log format.

## 10. Open questions
- None at spec time. Recon resolved the field names, units, row counts and the latest quarter.
