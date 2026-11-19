# Phase 5d Real-estate Concentration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a code-only "Real-estate concentration (2006 regulator thresholds)" memo section that checks each bank against the 2006 interagency CRE lines, using a new separate FDIC pull.

**Architecture:** A separate raw table `data/raw/concentration/` mirrors 5c's specialty pull. Pure functions in `canary/analyst/concentration.py` compute the two lines and render the section's lines from one bank's rows. A `ConcentrationSpecialist` registers after `peers`, is always code-only, adds no facts, and renders through the existing `render` hook.

**Tech Stack:** Python 3.12, pandas, pytest; FDIC BankFind API via `FDICClient`. No new dependencies. No Claude API use anywhere in this plan.

**Spec:** `specs/2026-11-19-phase5d-concentration-design.md` (read it first; § numbers refer to it).

## Global Constraints

- Branch `phase5d-concentration`. Tests: `.venv.nosync/bin/python -m pytest`. No test calls the network or the Claude API. Baseline: 526 passed.
- Never touch `data/model/`, the features export, `data/raw/financials/`, `schema.FINANCIAL_FIELDS`, `data/raw/specialty/` or `schema.SPECIALTY_FIELDS`. No S3/Athena/dbt. AWS $0. Claude API $0 (no live memo).
- Raw fields, in this order: `CERT, REPDTE, LNRECONS, LNREMULT, LNRENROT, LNCOMRE, RBC, RBCT1J, LNATRES`. Stored at `data/raw/concentration/repdte=YYYYMMDD/part.parquet`.
- **The test is fixed by published sources (§5); do not change it:**
  - Construction = `LNRECONS`. Total CRE = `LNRECONS + LNREMULT + LNRENROT + LNCOMRE`. A null component makes that numerator missing; a reported 0 counts as 0.
  - Capital: as-of quarter before `2020-03-31` → `RBC`; on or after `2020-03-31` → `RBCT1J + LNATRES` (null if either is null). Missing, zero or negative capital → ratios can't be computed.
  - Line 1: construction ÷ capital × 100 ≥ 100. Line 2: total CRE ÷ capital × 100 ≥ 300 **and** growth ≥ 50.
  - Growth = (total CRE at as-of ÷ total CRE at the same calendar quarter 12 quarters earlier − 1) × 100; earlier figure missing (no row or a null component) → reason "there is no figure from 12 quarters earlier"; earlier total == 0 → reason "it reported no commercial real estate loans 12 quarters earlier".
  - Comparisons are `>=` on unrounded values.
- Section key `"concentration"`, title `"Real-estate concentration (2006 regulator thresholds)"`, window `"as_of"`, always in `sheet.code_only`, registered after `peers`; no facts added; the writer's user message doesn't mention it.
- **Section copy is spec §6, verbatim** (lead, both capital lines, table header and row labels, "yes"/"no"/"n/a", every summary sentence, both combined forms, the three `{reason}` and two `{growth reason}` strings, definitions line, closing). Percentages: one decimal, thousands separators, minus sign where needed (e.g. `1,234.5%`, `-12.0%`).
- No measured result for crossing a line anywhere. No "approaching" label.

## Review Focus

1. **No concentration row for the bank at the as-of quarter**: both lines "can't be checked: there is no concentration data for this bank this quarter", no crash. Test in Task 2 and Task 3.
2. **Capital zero, negative or null** (incl. `LNATRES` null after 2020): both lines can't be checked with the capital reason; table cells "n/a". Test in Task 2.
3. **The 2020-03-31 boundary**: 2019-12-31 uses `RBC` and the 2006 capital line; 2020-03-31 uses `RBCT1J + LNATRES` and the 2020 capital line. Test in Task 2.
4. **Growth base 0 vs missing**: two different growth reasons; a ratio ≥ 300 with either gives the "reached 300% … can't be checked" sentence. Test in Task 2.
5. **A null CRE component with construction present**: line 1 still judged and stated; line 2 says a loan figure is missing. Test in Task 2.

---

### Task 1: Concentration pull (raw table, CLI, dictionary, live pull)

**Files:**
- Modify: `src/canary/schema.py` (add `CONCENTRATION_FIELDS` after `SPECIALTY_FIELDS`), `src/canary/storage.py` (add `concentration_path`), `src/canary/ingest.py` (subcommand `concentration`)
- Create: `src/canary/ingest_concentration.py` (mirror `ingest_specialty.py`), `data-dictionary/fdic_concentration.md`, `tests/test_ingest_concentration.py`
- Modify: `tests/test_data_dictionary.py` (add `("fdic_concentration.md", CONCENTRATION_FIELDS)`), `tests/data_checks/test_raw_files.py` (two checks)

**Interfaces:**
- Produces: `CONCENTRATION_FIELDS = {"CERT": Field("int64", "FDIC Certificate #"), "REPDTE": Field("date_ymd", "Report Date"), "LNRECONS": Field("float64", "RE CONSTRUCTION & LAND DEVELOP"), "LNREMULT": Field("float64", "RE MULTIFAMILY"), "LNRENROT": Field("float64", "RE NONFARM NONRES OTHER (NON-OWNER-OCCUPIED)"), "LNCOMRE": Field("float64", "LOANS TO FINANCE CRE NOT SECURED BY RE"), "RBC": Field("float64", "TOTAL RISK-BASED CAPITAL"), "RBCT1J": Field("float64", "TIER 1 CAPITAL"), "LNATRES": Field("float64", "ALLOWANCE FOR LOAN AND LEASE LOSSES")}`; `concentration_path(root: Path, repdte: date) -> Path`; `run_concentration(root: Path, client: FDICClient, start: date = START, refresh_latest: int = 2, force: bool = False) -> list[QuarterResult]`; CLI `python -m canary.ingest concentration [--force] [--root data/raw]`.
- Same rules as the specialty pull: values unchanged, `ingested_at`, atomic writes, 0 rows or duplicate CERT → `IncompleteResponseError`, `quarters_to_pull(..., path_fn=concentration_path)`.

- [ ] **Step 1: Failing tests** in `tests/test_ingest_concentration.py`, mirroring `tests/test_ingest_specialty.py`: `test_pull_quarter_requests_concentration_fields` (fields param exactly the Global Constraints order); `test_run_writes_partitioned_parquet` (path, columns + `ingested_at`, float64 dollars, empty string → null); `test_skips_present_quarters_and_refreshes_latest_two` (and no `financials/` or `specialty/` dir created); `test_force_repulls_all`; `test_zero_rows_raises`; `test_duplicate_cert_raises`; `test_cli_concentration_subcommand`. Add the dictionary parametrize row.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement**; write `data-dictionary/fdic_concentration.md` (each field incl. `ingested_at`, the Call Report item from spec §4, units $ thousands, source endpoint, why separate, the 2022-12-31 coverage notes from spec §4).
- [ ] **Step 4: Data checks** (skip if `data/raw/concentration` absent): `test_concentration_covers_financials` (every financials (CERT, REPDTE) has a row); `test_concentration_dollars_non_negative` (no negative `LNRECONS`, `LNREMULT`, `LNRENROT`, `LNCOMRE`; report counts of nulls per field and of negative capital fields without failing on capital).
- [ ] **Step 5: Run** unit tests and full suite — PASS.
- [ ] **Step 6: Live pull (free FDIC API, a few minutes):** `.venv.nosync/bin/python -m canary.ingest concentration`. Run `tests/data_checks/test_raw_files.py -q` — PASS. Spot-check SVB 24735 at 2022-12-31: `RBC` 17,871,000, `RBCT1J` 16,995,000, `LNREMULT` 629,000, `LNRENROT` 1,339,000, `LNCOMRE` 24,000, `LNATRES` 636,000. Record rows, quarters, null counts and duration in the report.
- [ ] **Step 7: Commit** `"Concentration pull: FDIC CRE and capital fields per bank-quarter (separate raw table)"`.

---

### Task 2: Concentration core (pure test + section lines)

**Files:**
- Create: `src/canary/analyst/concentration.py`, `tests/test_analyst_concentration.py`

**Interfaces:**
- Produces (in `canary.analyst.concentration`):
  - Constants: `NEW_MEASURE_FROM = date(2020, 3, 31)`, `LINE1_PCT = 100.0`, `LINE2_PCT = 300.0`, `GROWTH_PCT = 50.0`, `GROWTH_QUARTERS = 12`, and every §6 string as a named constant (`LEAD`, `CAPITAL_2006`, `CAPITAL_2020`, `TABLE_HEADER`, row labels, `DEFINITIONS`, `CLOSING`, the summary sentences, `REASON_CAPITAL`, `REASON_LOAN`, `REASON_NO_DATA`, `GROWTH_NO_FIGURE`, `GROWTH_ZERO_BASE`).
  - `@dataclass ConcentrationResult`: `as_of: date`, `measure: Literal["rbc_2006", "t1_allowance_2020"]`, `construction_pct: float | None`, `cre_pct: float | None`, `growth_pct: float | None`, `reason: str | None` (why ratios can't be computed, one of the three reasons, or None), `cre_reason: str | None` (line-2-only loan reason when construction was computable), `growth_reason: str | None`.
  - `compute_concentration(rows: pd.DataFrame, as_of: date) -> ConcentrationResult` — `rows` = one bank's concentration rows (columns `report_date` datetime64 plus the raw dollar fields, any order, possibly empty).
  - `render_concentration(result: ConcentrationResult) -> list[str]` — the six §6 parts in order (lead, capital line, table, summary, definitions, closing), each a separate line with blank lines between paragraphs as the existing renderers do.
- [ ] **Step 1: Failing tests** (small synthetic rows):
  - `test_capital_measure_boundary`: as-of 2019-12-31 uses `RBC` (and `render` includes `CAPITAL_2006`); as-of 2020-03-31 uses `RBCT1J + LNATRES` (and `CAPITAL_2020`).
  - `test_ratios_and_lines`: construction 150 / capital 100 → 150.0, line 1 crossed; CRE 400 / capital 100 with CRE 12 quarters earlier 200 → 300.0% and growth 100.0 → line 2 crossed; summary is the both-crossed combined sentence.
  - `test_ge_comparisons`: exactly 100.0 / 300.0 / 50.0 count as met.
  - `test_ratio_300_growth_low`: CRE ≥ 300%, growth 30% → the "reached 300% … grew less than 50% …" sentence.
  - `test_growth_reasons`: no row 12 quarters earlier → `GROWTH_NO_FIGURE`; earlier total 0 → `GROWTH_ZERO_BASE`; with CRE ≥ 300% each yields the "reached 300% … can't be checked: {growth reason}" sentence.
  - `test_capital_missing_zero_negative`: each → both lines "can't be checked: the bank reported no usable capital figure for this quarter"; Bank cells and Meets-it cells "n/a".
  - `test_null_cre_component_keeps_line1`: `LNRENROT` null, construction 120% → "It crossed the construction line (100% or more of capital)." then "The total commercial real estate line can't be checked: a loan figure the test needs is missing for this quarter."
  - `test_no_row`: empty `rows` → both lines can't be checked with `REASON_NO_DATA`.
  - `test_neither_crossed_combined`: → "It did not cross either line."
  - `test_number_format`: 1234.56 → "1,234.6%"; -12.0 → "-12.0%".
  - `test_render_order_and_copy`: lines appear in §6 order; `LEAD`, `DEFINITIONS`, `CLOSING` exactly once; table header exact.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** — PASS; full suite — PASS.
- [ ] **Step 5: Commit** `"Phase 5d: concentration core (2006 lines, 2020 capital measure)"`.

---

### Task 3: Context, specialist and registration

**Files:**
- Modify: `src/canary/analyst/context.py` (`Context.concentration`, `load_context(..., concentration_dir: Path = Path("data/raw/concentration"))` as the last parameter; missing dir → `FileNotFoundError` naming `python -m canary.ingest concentration`), `src/canary/analyst/concentration.py` (specialist), `src/canary/analyst/writer.py` (`import canary.analyst.concentration` after peers), `tests/conftest.py` (`concentration_dir` fixture; `analyst_ctx` passes it), `tests/test_analyst_context.py` (direct `load_context` calls pass it)
- Create: `tests/test_analyst_concentration_section.py`, `tests/data_checks/test_concentration_real.py`

**Interfaces:**
- Consumes: Task 2 `compute_concentration`, `render_concentration`; `sections.Section`, `sections.register`, `sheet.code_only`, `sheet.extras`.
- Produces: `Context.concentration: pd.DataFrame` with `cert` (int64), `report_date` (datetime64), and the seven dollar fields under their raw names; `CONCENTRATION_KEY = "concentration"`, `CONCENTRATION_SECTION` (`ai_written=False`, `render=` a function of the sheet that renders `sheet.extras["concentration"]`), `class ConcentrationSpecialist` (`build_facts` stores the result in `sheet.extras["concentration"]`, adds the key to `sheet.code_only`, returns `[]`).
- Fixture `concentration_dir(raw, tmp_path)`: one parquet per quarter in `raw` for every cert, with values chosen so at least one cert crosses line 1 (e.g. cert 100: `LNRECONS` 150, `RBC`/`RBCT1J` 100, `LNATRES` 0), one crosses neither, and cert 101 has no rows at all.

- [ ] **Step 1: Failing tests:** `test_concentration_loaded` (dtypes); `test_missing_concentration_dir_raises`; `test_section_last_after_peers` (order in `sections_for(sheet)`: … "trends", "peers", "concentration", then the outcome section); `test_always_code_only_no_facts` (key in `sheet.code_only`; no fact added; the writer's request schema and user message don't contain it); `test_note_renders_section` (fake client `write_memo` note contains the title heading, `LEAD`, the table header and `CLOSING` once); `test_no_rows_bank` (cert 101 → `REASON_NO_DATA` lines); `test_registered_once`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** each `tests/test_analyst_*.py` alone and the full suite — PASS.
- [ ] **Step 5: Data check** (skip if `data/raw/concentration` or the features export is absent): `test_svb_2022q4_concentration_computes` builds SVB 24735's rows from the real table and asserts the 2020 measure is used, capital = 16,995,000 + 636,000, and `construction_pct` and `cre_pct` are finite. It asserts nothing about crossing.
- [ ] **Step 6: Commit** `"Phase 5d: concentration section (code-only, registered after peers)"`.

---

### Task 4: Docs and a free local check

**Files:**
- Create: `decisions/0021-cre-concentration-2006-thresholds.md`
- Modify: `data-dictionary/bank_notes.md`, `runbooks/fdic-ingestion.md`, `runbooks/analyst.md`, `reference/GLOSSARY.md` (CRE concentration guidance, total risk-based capital, Tier 1 capital, loan-loss allowance, community bank leverage ratio), `README.md` (Phase 5 lines: 5d built as a code-written section; test count), `RESULTS.md` (one line: descriptive screen, no measured result), `specs/2026-11-19-phase5d-concentration-design.md` (Status: built)
- [ ] **Step 1: Decision 0021:** sources (OCC Bulletin 2006-46 / 71 FR 74580; Federal Reserve 2013 CRE guidance analysis, appendix; FDIC FIL-31-2020; Federal Reserve SR 20-8) with what each supports; the fixed test (every value from Global Constraints); the as-of-quarter capital switch and its label; code-only and why; separate table and why; limits (`LNCOMRE` 0 for most small banks; owner-occupied split only from 2007, irrelevant for 2016+ memos; 2008-era failures have no memos; the guidance's "approaching" has no number, so none is used).
- [ ] **Step 2: Dictionary, runbooks, glossary, README, RESULTS.**
- [ ] **Step 3: Free local check (no API):** build SVB's fact sheet as of 2022-12-31 with `build_fact_sheet` on the real context (after importing `canary.analyst.writer` so specialists register) and print `render_concentration(sheet.extras["concentration"])`; paste the lines in the report. Do the same for one 2016 test-period failure. Do not write notes under `banks/`.
- [ ] **Step 4: Full suite; commit** `"Phase 5d docs: decision 0021, dictionary, runbooks, glossary, README/RESULTS"`.
