# Phase 1 FDIC Ingestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A tested Python pull that saves FDIC quarterly financials (45 fields, 2001 Q1 → latest) as one Parquet file per quarter, plus the full FDIC failed bank list as one Parquet file.

**Architecture:** A small HTTP client (paging, retries, completeness check) feeds two ingest modules, financials and failures. Each one turns API records into a typed DataFrame using a single field list, then writes Parquet atomically. The financials run is resumable: it skips quarters already on disk and re-pulls the latest 2. A thin CLI wraps both. Unit tests fake the HTTP layer; separate data checks run against the real files.

**Tech Stack:** Python 3.12, pandas, pyarrow, requests, pytest. Virtual env in `.venv/`.

**Spec:** `specs/2026-11-09-phase1-fdic-ingestion-design.md` (read it alongside this plan).

## Global Constraints

- Python ≥ 3.12. Runtime deps: `pandas`, `pyarrow`, `requests` only. Dev dep: `pytest`. Nothing heavier.
- API base: `https://api.fdic.gov/banks`. Endpoints `financials` and `failures`. `limit` max = 10000. No API key.
- HTTP `User-Agent: canary-research-pipeline`. No personal info in any request.
- Store values exactly as published: no imputing, no 0↔null conversion, no rescaling. The only allowed conversion is `""` → null (an empty string means missing).
- Keep FDIC column names as-is (upper case). Add one column, `ingested_at` (UTC timestamp), to both tables.
- Output: `data/raw/financials/repdte=YYYYMMDD/part.parquet` and `data/raw/failures/failures.parquet`. `data/` is gitignored and must never be committed.
- Financials start at 2001-03-31; end at the latest `REPDTE` the API reports (2026-06-30 at spec time).
- Each run re-pulls the latest 2 quarters; `--force` re-pulls all.
- Retry timeouts / connection errors / HTTP 429 / 5xx up to 3 retries (4 attempts), waits 1s, 2s, 4s; 0.5s pause between calls.
- Rows received must equal `meta.total`, else raise and write nothing.
- Every column documented in `data-dictionary/`; choices in `decisions/`; progress in `daily-log.md`.
- Unit tests must not touch the network.

## Review Focus

1. **A requested field comes back null for an entire quarter** (FDIC renamed or retired it). Expect a logged WARNING naming the column, not a silent all-null column. Test: Task 3 `test_all_null_column_logs_warning`.
2. **A numeric field holds a non-numeric string** (e.g. `"N/A"`). Expect a `SchemaError` naming the field. `""` becomes null. Test: Task 3 `test_non_numeric_string_raises` and `test_empty_string_becomes_null`.
3. **The API answers 200 with a non-JSON body or JSON without `meta`** (maintenance page). Expect `FDICAPIError`, not a `KeyError`/`JSONDecodeError` traceback. Test: Task 2 `test_non_json_body_raises_api_error`.
4. **A rerun after a crash finds a leftover `part.parquet.tmp`.** Expect that quarter to count as missing and be pulled again; only `part.parquet` counts as done. Test: Task 5 `test_leftover_tmp_file_counts_as_missing`.
5. **Paging returns the same bank twice** (offset paging over a shifting index), so the row count matches but the data is wrong. Expect `IncompleteResponseError` on a duplicate `CERT` within a quarter. Test: Task 5 `test_duplicate_cert_in_quarter_raises`.

---

## File Map

| File | Responsibility |
|---|---|
| `pyproject.toml` | Package metadata, deps, pytest config (`pythonpath=src`, marker `data`) |
| `src/canary/__init__.py` | Package marker |
| `src/canary/quarters.py` | Quarter-end date list |
| `src/canary/fdic_client.py` | HTTP: one page with retries; all pages with completeness check |
| `src/canary/schema.py` | The two field lists (name → dtype, FDIC title) and `to_typed_frame` |
| `src/canary/storage.py` | Partition paths and atomic Parquet write |
| `src/canary/ingest_financials.py` | Latest date, which quarters to pull, pull one quarter, run all |
| `src/canary/ingest_failures.py` | Pull and save failures |
| `src/canary/ingest.py` | CLI (`python -m canary.ingest financials|failures [--force]`) |
| `tests/conftest.py` | `FakeSession` / `FakeResponse` |
| `tests/test_*.py` | Unit tests per module |
| `tests/data_checks/test_raw_files.py` | Data checks on real files (marker `data`) |
| `tests/test_data_dictionary.py` | Every field is documented |
| `data-dictionary/fdic_financials.md`, `fdic_failures.md` | Column docs |
| `decisions/0002…0004-*.md`, `runbooks/fdic-ingestion.md`, `README.md`, `daily-log.md` | Vault docs |

---

### Task 1: Project setup + quarter list

**Files:**
- Create: `pyproject.toml`, `src/canary/__init__.py`, `src/canary/quarters.py`, `tests/test_quarters.py`

**Interfaces:**
- Produces: `quarter_ends(start: date, end: date) -> list[date]` (inclusive, ascending; `start`/`end` must be quarter-end dates, else `ValueError`).

- [ ] **Step 1: Branch and commit the spec + plan**

```bash
git checkout -b phase1-fdic-ingestion
git add specs/ plans/ && git commit -m "docs: Phase 1 FDIC ingestion spec and plan"
```

- [ ] **Step 2: Write `pyproject.toml` and create the venv**

setuptools, src layout, `name="canary"`, `requires-python=">=3.12"`, deps `pandas>=2.2`, `pyarrow>=15`, `requests>=2.31`; optional `dev = ["pytest>=8"]`. `[tool.pytest.ini_options]`: `pythonpath=["src"]`, `testpaths=["tests"]`, `markers=["data: checks on real files in data/raw (skipped if absent)"]`.

Run: `python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"`
Expected: `Successfully installed ... canary ...`

- [ ] **Step 3: Write the failing tests**

```python
from datetime import date
import pytest
from canary.quarters import quarter_ends

def test_quarter_ends_inclusive_range():
    assert quarter_ends(date(2022, 9, 30), date(2023, 3, 31)) == [
        date(2022, 9, 30), date(2022, 12, 31), date(2023, 3, 31)]

def test_full_phase1_range_is_102_quarters():
    q = quarter_ends(date(2001, 3, 31), date(2026, 6, 30))
    assert len(q) == 102 and q[0] == date(2001, 3, 31) and q[-1] == date(2026, 6, 30)

def test_rejects_non_quarter_end():
    with pytest.raises(ValueError):
        quarter_ends(date(2022, 10, 1), date(2023, 3, 31))
```

- [ ] **Step 4: Run, expect FAIL** — `.venv/bin/pytest tests/test_quarters.py -v` → `ModuleNotFoundError: canary.quarters`

- [ ] **Step 5: Implement `quarter_ends` in `src/canary/quarters.py`.** Quarter-ends are 3/31, 6/30, 9/30, 12/31.

- [ ] **Step 6: Run, expect PASS** (3 passed)

- [ ] **Step 7: Commit** — `git add pyproject.toml src tests && git commit -m "feat: project setup and quarter-end list"`

---

### Task 2: FDIC HTTP client

**Files:**
- Create: `src/canary/fdic_client.py`, `tests/conftest.py`, `tests/test_fdic_client.py`

**Interfaces:**
- Produces:
  - `class FDICAPIError(Exception)`; `class IncompleteResponseError(FDICAPIError)`
  - `FDICClient(session=None, base_url="https://api.fdic.gov/banks", max_retries=3, backoff=1.0, pause=0.5, timeout=60, sleep=time.sleep)`; `session` defaults to a `requests.Session` with `User-Agent: canary-research-pipeline`.
  - `FDICClient.get_page(endpoint: str, params: dict) -> dict` returns the parsed JSON (must contain `meta.total` and `data`).
  - `FDICClient.get_all(endpoint: str, params: dict, page_size: int = 10000) -> list[dict]` returns the inner `data` dicts across all pages.
  - `tests/conftest.py`: `FakeResponse(status_code: int, payload: dict | None = None, text: str = "")` with `.json()` (raises `ValueError` if `payload is None`); `FakeSession(responses: list)` whose `.get(url, params=None, timeout=None)` pops the next item (a `FakeResponse` or an exception instance to raise) and records `(url, params)` in `.calls`. Helper `page(rows: list[dict], total: int) -> FakeResponse` builds `{"meta": {"total": total}, "data": [{"data": r} for r in rows]}`.

- [ ] **Step 1: Write the failing tests**

```python
def test_get_all_single_page_unwraps_rows():          # total=2, 2 rows -> [{"CERT":1},{"CERT":2}]
def test_get_all_pages_with_offset():                  # page_size=2, total=5 -> 3 calls, offsets 0,2,4; 5 rows
def test_row_count_mismatch_raises():                  # total=3, page returns 2 then [] -> IncompleteResponseError
def test_retries_then_succeeds():                      # 503, Timeout(), 200 -> rows returned; sleep calls == [1.0, 2.0]
def test_gives_up_after_three_retries():               # four 503s -> FDICAPIError; 4 calls made
def test_client_error_not_retried():                   # 400 -> FDICAPIError after 1 call
def test_non_json_body_raises_api_error():             # 200 with payload=None -> FDICAPIError
def test_missing_meta_raises_api_error():              # 200 with {"data": []} -> FDICAPIError
def test_sends_limit_offset_and_user_agent():          # params include limit=10000, offset=0; default session UA == "canary-research-pipeline"
```
Use `sleep=recorder.append` and `pause=0` so tests don't wait. Assert pause calls separately: with `pause=0.5`, a 2-page pull records one `0.5` between pages.

- [ ] **Step 2: Run, expect FAIL** — `.venv/bin/pytest tests/test_fdic_client.py -v`

- [ ] **Step 3: Implement `fdic_client.py`.** Retryable: `requests.Timeout`, `requests.ConnectionError`, status 429 or ≥500. Wait `backoff * 2**attempt`. Paging loop: request `offset=len(rows)` until `len(rows) >= total`; an empty page before that → `IncompleteResponseError`; finally `len(rows) != total` → `IncompleteResponseError` with both numbers in the message.

- [ ] **Step 4: Run, expect PASS** (9 passed)

- [ ] **Step 5: Commit** — `git commit -m "feat: FDIC API client with paging, retries, completeness check"`

---

### Task 3: Field lists + typed DataFrame

**Files:**
- Create: `src/canary/schema.py`, `tests/test_schema.py`

**Interfaces:**
- Produces:
  - `class SchemaError(Exception)`
  - `Field = NamedTuple("Field", [("dtype", str), ("title", str)])`; dtype ∈ `{"string", "int64", "Int64", "float64", "date_ymd", "date_mdy"}`
  - `FINANCIAL_FIELDS: dict[str, Field]`: exactly the 45 fields in spec §6.1, in that order. `CERT`→`int64`, `REPDTE`→`date_ymd`, `NAME`/`STALP`/`BKCLASS`/`NAMEHCR`→`string`, other 39→`float64`. Titles are the FDIC titles from the catalog (e.g. `ASSET`: "Total assets", `DEPUNINS`: "Estimated uninsured deposits…").
  - `FAILURE_FIELDS: dict[str, Field]`: the 21 fields `NAME, CERT, FIN, CITYST, FAILDATE, FAILYR, SAVR, RESTYPE1, CHCLASS1, RESDATE, RESTYPE, QBFDEP, QBFASSET, COST, PSTALP, BIDCITY, BIDNAME, BIDSTATE, CITY, FUND, PTRDATE`. `CERT`/`FAILYR`→`Int64`, `FAILDATE`/`RESDATE`→`date_mdy`, `QBFDEP`/`QBFASSET`/`COST`→`float64`, rest→`string`.
  - `to_typed_frame(records: list[dict], fields: dict[str, Field], ingested_at: pd.Timestamp) -> pd.DataFrame`: columns = `fields` keys in order + `ingested_at`. Extra keys (e.g. `ID`) are dropped; missing keys become null. Dates become `datetime64[ns]` (midnight); `ingested_at` is tz-aware UTC.

- [ ] **Step 1: Write the failing tests**

```python
def test_columns_ordered_extras_dropped():   # record has ID -> not in df; columns == list(fields)+["ingested_at"]
def test_types_applied():                    # CERT int64, ASSET float64, NAME string, REPDTE "20221231" -> Timestamp("2022-12-31")
def test_values_unchanged():                 # ASSET 209026000 -> 209026000.0; 0 stays 0.0 (not null)
def test_empty_string_becomes_null():        # COST "" -> NaN; RESDATE "" -> NaT
def test_non_numeric_string_raises():        # ASSET "N/A" -> SchemaError mentioning "ASSET"
def test_bad_date_raises():                  # FAILDATE "13/45/2023" -> SchemaError mentioning "FAILDATE"
def test_mdy_date_parsed():                  # FAILDATE "3/10/2023" -> Timestamp("2023-03-10")
def test_nullable_int_allows_missing():      # failures CERT None -> <NA>, dtype Int64
def test_null_in_int64_raises():             # financials CERT None -> SchemaError
def test_all_null_column_logs_warning(caplog):  # 2 records, no LNCI key -> WARNING containing "LNCI"
def test_field_lists_match_spec():           # len(FINANCIAL_FIELDS)==45, len(FAILURE_FIELDS)==21, "DEPUNINS","SCHA","SCHF" in FINANCIAL_FIELDS
```

- [ ] **Step 2: Run, expect FAIL**
- [ ] **Step 3: Implement `schema.py`.** Use `pd.to_numeric(errors="raise")` and `pd.to_datetime(format="%Y%m%d" | "%m/%d/%Y", errors="raise")` per column, after `replace("", pd.NA)`. Wrap their errors in `SchemaError(f"{field}: ...")`. Log via `logging.getLogger("canary")`.
- [ ] **Step 4: Run, expect PASS** (11 passed)
- [ ] **Step 5: Commit** — `git commit -m "feat: curated field lists and typed DataFrame conversion"`

---

### Task 4: Partition paths + atomic Parquet write

**Files:**
- Create: `src/canary/storage.py`, `tests/test_storage.py`

**Interfaces:**
- Produces:
  - `financials_path(root: Path, repdte: date) -> Path` returns `root/"financials"/f"repdte={repdte:%Y%m%d}"/"part.parquet"`
  - `failures_path(root: Path) -> Path` returns `root/"failures"/"failures.parquet"`
  - `write_parquet_atomic(df: pd.DataFrame, path: Path) -> None`: creates parents, writes `path` + `.tmp` (i.e. `part.parquet.tmp`), then `os.replace`. On any exception it deletes the tmp file and re-raises; `path` is untouched.

- [ ] **Step 1: Write the failing tests**

```python
def test_financials_path(tmp_path):   # date(2022,12,31) -> tmp_path/"financials/repdte=20221231/part.parquet"
def test_round_trip(tmp_path):        # write then pd.read_parquet equals df (dtypes kept)
def test_failed_write_leaves_nothing(tmp_path, monkeypatch):
    # monkeypatch pd.DataFrame.to_parquet to write a few bytes then raise OSError
    # -> raises OSError; neither part.parquet nor part.parquet.tmp exists
def test_failed_overwrite_keeps_old_file(tmp_path, monkeypatch):  # existing file content unchanged after a failed rewrite
```

- [ ] **Step 2: Run, expect FAIL** · **Step 3: Implement** · **Step 4: Run, expect PASS** (4 passed)
- [ ] **Step 5: Commit** — `git commit -m "feat: partition paths and atomic parquet writes"`

---

### Task 5: Financials ingest

**Files:**
- Create: `src/canary/ingest_financials.py`, `tests/test_ingest_financials.py`

**Interfaces:**
- Consumes: `FDICClient.get_page/get_all`, `IncompleteResponseError` (Task 2); `FINANCIAL_FIELDS`, `to_typed_frame` (Task 3); `financials_path`, `write_parquet_atomic` (Task 4); `quarter_ends` (Task 1).
- Produces:
  - `START = date(2001, 3, 31)`
  - `latest_report_date(client: FDICClient) -> date`: one `get_page("financials", {"fields": "REPDTE", "sort_by": "REPDTE", "sort_order": "DESC", "limit": 1})`
  - `quarters_to_pull(quarters: list[date], root: Path, refresh_latest: int = 2, force: bool = False) -> list[date]`: ascending, no duplicates. Force → all. Otherwise quarters whose `part.parquet` doesn't exist, plus the last `refresh_latest`.
  - `pull_quarter(client: FDICClient, repdte: date, ingested_at: pd.Timestamp) -> pd.DataFrame`: `get_all("financials", {"filters": f"REPDTE:{repdte:%Y%m%d}", "fields": ",".join(FINANCIAL_FIELDS)})` then `to_typed_frame`. A duplicate `CERT` → `IncompleteResponseError`.
  - `QuarterResult = NamedTuple(repdte: date, status: str, rows: int, seconds: float)`; status ∈ `{"pulled", "skipped"}`
  - `run_financials(root: Path, client: FDICClient, start: date = START, refresh_latest: int = 2, force: bool = False) -> list[QuarterResult]`: one result per quarter in `quarter_ends(start, latest)`; logs one INFO line per quarter: `"2022-12-31 pulled 4,740 rows in 5.1s"` / `"... skipped"`. An error stops the run (quarters already written stay).

- [ ] **Step 1: Write the failing tests** (fake `client` object or `FDICClient(session=FakeSession(...), pause=0, sleep=lambda s: None)`)

```python
def test_latest_report_date():                      # payload REPDTE "20260630" -> date(2026,6,30)
def test_quarters_to_pull_resume_and_refresh(tmp_path):
    # 6 quarters q1..q6; files exist for q1, q2, q4, q5, q6 (q3 missing)
    # -> [q3, q5, q6]: missing q3 pulled, latest 2 always re-pulled, q1/q2/q4 skipped
def test_quarters_to_pull_force(tmp_path):          # all existing -> force returns all
def test_leftover_tmp_file_counts_as_missing(tmp_path):  # only part.parquet.tmp present for q1 -> q1 included
def test_pull_quarter_requests_fields_and_filter(): # params["filters"]=="REPDTE:20221231"; params["fields"] has 45 names
def test_duplicate_cert_in_quarter_raises():        # 2 rows CERT 24735, total=2 -> IncompleteResponseError
def test_run_financials_writes_and_skips(tmp_path): # latest=2023-03-31, start=2022-09-30, q1 file exists
    # -> results statuses ["skipped","pulled","pulled"]; files exist for all 3
def test_run_stops_on_error_keeps_written(tmp_path):# 2nd quarter raises -> exception; 1st quarter file exists, 2nd doesn't
```

- [ ] **Step 2: Run, expect FAIL** · **Step 3: Implement** · **Step 4: Run, expect PASS** (8 passed)
- [ ] **Step 5: Commit** — `git commit -m "feat: resumable per-quarter financials ingest"`

---

### Task 6: Failures ingest

**Files:**
- Create: `src/canary/ingest_failures.py`, `tests/test_ingest_failures.py`

**Interfaces:**
- Consumes: `FDICClient.get_all`, `FAILURE_FIELDS`, `to_typed_frame`, `failures_path`, `write_parquet_atomic`.
- Produces: `run_failures(root: Path, client: FDICClient) -> int` (rows written). One `get_all("failures", {"fields": ",".join(FAILURE_FIELDS)})`; always overwrites.

- [ ] **Step 1: Write the failing tests**

```python
def test_run_failures_writes_typed_file(tmp_path):
    # rows: SVB {"CERT":24735,"NAME":"SILICON VALLEY BANK","FAILDATE":"3/10/2023","FAILYR":"2023","COST":18744254.463,...}
    #       old {"CERT":None,"FAILDATE":"1/5/1934","FAILYR":"1934",...}
    # -> returns 2; file has FAILDATE 2023-03-10, CERT dtype Int64 with one <NA>
def test_run_failures_requests_21_fields(tmp_path): # params["fields"].split(",") == list(FAILURE_FIELDS)
```

- [ ] **Step 2–4:** FAIL → implement → PASS (2 passed)
- [ ] **Step 5: Commit** — `git commit -m "feat: failed bank list ingest"`

---

### Task 7: CLI

**Files:**
- Create: `src/canary/ingest.py`, `tests/test_cli.py`

**Interfaces:**
- Consumes: `run_financials`, `run_failures`, `FDICClient`.
- Produces: `main(argv: list[str] | None = None, client: FDICClient | None = None) -> int`. Subcommands `financials [--force] [--root PATH]` and `failures [--root PATH]`; default root `data/raw`. Sets up logging (INFO, `%(asctime)s %(levelname)s %(message)s`). Returns 0 on success; on `FDICAPIError`/`SchemaError` it logs the error and returns 1. `if __name__ == "__main__": raise SystemExit(main())`.

- [ ] **Step 1: Write the failing tests**

```python
def test_cli_financials_passes_force(monkeypatch, tmp_path):  # monkeypatch canary.ingest.run_financials -> captures force=True, root=tmp_path; returns 0
def test_cli_failures(monkeypatch, tmp_path):                 # run_failures called with root
def test_cli_returns_1_on_api_error(monkeypatch, tmp_path):   # run_financials raises FDICAPIError -> 1
```

- [ ] **Step 2–4:** FAIL → implement → PASS (3 passed). Then run the full unit suite: `.venv/bin/pytest -v`, all green.
- [ ] **Step 5: Commit** — `git commit -m "feat: ingest CLI"`

---

### Task 8: Data dictionary

**Files:**
- Create: `data-dictionary/fdic_financials.md`, `data-dictionary/fdic_failures.md`, `tests/test_data_dictionary.py`

**Interfaces:**
- Consumes: `FINANCIAL_FIELDS`, `FAILURE_FIELDS`.

- [ ] **Step 1: Write the failing test**

```python
@pytest.mark.parametrize("doc,fields", [("fdic_financials.md", FINANCIAL_FIELDS), ("fdic_failures.md", FAILURE_FIELDS)])
def test_every_field_documented(doc, fields):
    text = (REPO / "data-dictionary" / doc).read_text()
    missing = [f for f in [*fields, "ingested_at"] if f"| `{f}` |" not in text]
    assert missing == []
```

- [ ] **Step 2: Run, expect FAIL** (file not found)
- [ ] **Step 3: Write both docs.** Header: table name, file path, grain (one row per bank per quarter / per failure event), primary key, source endpoint, row count (fill in after Task 9). Then a table `| Column | Type | FDIC title | Meaning (plain English) | Units / caveats |`. Must include the spec §6.1 caveats: $ in thousands, ratios in %, income fields year-to-date, 0 may mean "not reported", and for failures: 488 pre-1977 rows have no CERT, `RESTYPE` FAILURE vs ASSISTANCE, values are current amended data.
- [ ] **Step 4: Run, expect PASS** (2 passed)
- [ ] **Step 5: Commit** — `git commit -m "docs: data dictionary for FDIC financials and failures"`

---

### Task 9: Real pull + data checks

**Files:**
- Create: `tests/data_checks/test_raw_files.py`

**Interfaces:**
- Consumes: the files written by the CLI; `quarter_ends`.
- Data root: env `CANARY_DATA_ROOT`, default `<repo>/data/raw`. Module-level `pytestmark = [pytest.mark.data, pytest.mark.skipif(<financials dir missing>, reason="no local data")]`. Load with `pd.read_parquet(root/"financials", columns=[...])`.

- [ ] **Step 1: Write the data checks**

```python
def test_cert_repdte_unique():          # no duplicated (CERT, REPDTE)
def test_cert_never_null_financials():
def test_no_missing_quarters():         # set(REPDTE) == set(quarter_ends(2001-03-31, max REPDTE))
def test_rows_per_quarter_in_range():   # every quarter 3,000 <= n <= 12,000
def test_svb_2022q4_assets():           # CERT 24735, REPDTE 2022-12-31 -> ASSET == 209_026_000
def test_2023_failures_present():       # {24735: 2023-03-10, 57053: 2023-03-12, 59017: 2023-05-01} in failures FAILDATE
def test_failures_cert_present_since_2001():  # FAILYR >= 2001 -> CERT not null
```

- [ ] **Step 2: Confirm they skip with no data** — `.venv/bin/pytest tests/data_checks -v` → 7 skipped
- [ ] **Step 3: Run the real pull** (~10 min):
`.venv/bin/python -m canary.ingest failures && .venv/bin/python -m canary.ingest financials`
Expected: `failures` writes ~4,117 rows; `financials` logs 102 `pulled` lines, exit 0.
- [ ] **Step 4: Rerun financials to prove resume** — expect 100 `skipped`, 2 `pulled`, in seconds.
- [ ] **Step 5: Run data checks** — `.venv/bin/pytest tests/data_checks -v` → 7 passed. Record total rows, quarter count and on-disk size (`du -sh data/raw`) for the docs.
- [ ] **Step 6: Commit** — `git status` must show nothing under `data/`. `git add tests/data_checks && git commit -m "test: data checks on raw FDIC files"`

---

### Task 10: Vault docs and wrap-up

**Files:**
- Create: `decisions/0002-parquet-partitioned-by-quarter.md`, `decisions/0003-curated-45-financial-fields.md`, `decisions/0004-store-raw-values-unchanged.md`, `runbooks/fdic-ingestion.md`, `README.md`
- Modify: `data-dictionary/*.md` (row counts), `daily-log.md`

- [ ] **Step 1: Decision notes** in the 0001 format (Date, Status, Decision, Why, plus Alternatives). 0002: the 3 approaches from spec §5. 0003: 45 vs 160 vs 2,378 fields, and how to add one. 0004: no imputation, keep 0s, keep FDIC names, re-pull latest 2 overwrites, **API serves amended values only** (point-in-time limitation).
- [ ] **Step 2: Runbook**: setup (venv, install), the commands, expected runtime, what resume/`--force` do, what to do on an `IncompleteResponseError`/`FDICAPIError` (rerun; it resumes), how to run the unit tests vs the data checks.
- [ ] **Step 3: README**: what Canary is (2–3 sentences, SVB story), Phase 1 status, quickstart, the measured scale from Task 9, a Limitations section (amended data, 0 = not reported in early years), and the line **"Research tool, not financial advice."**
- [ ] **Step 4: Fill row counts in the data dictionary; add the session entry to `daily-log.md`** (done / next / open questions).
- [ ] **Step 5: Full check** — `.venv/bin/pytest -v` → all unit tests + 7 data checks + dictionary tests pass.
- [ ] **Step 6: Commit** — `git add decisions runbooks README.md data-dictionary daily-log.md && git commit -m "docs: Phase 1 decisions, runbook, README, log"`. Then use superpowers:finishing-a-development-branch to merge `phase1-fdic-ingestion` into `main` and push.
