# Phase 5c Peer Comparison Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a descriptive "Compared with similar banks" memo section that shows, for each ratio where a bank is in the national top or bottom 10%, whether it is also unusual among banks in the same FDIC specialty group and size tier.

**Architecture:** A separate raw pull stores the FDIC specialty code and city per bank-quarter. Pure functions in `canary/analyst/peers.py` build the peer group and readings from one quarter's features. A `PeerSpecialist` registers with the 5a section registry (after 5b's trends), adds facts, code lines and a table; the checker gains peer-only rules reusing 5b's machinery.

**Tech Stack:** Python 3.12, pandas, pytest; FDIC BankFind API via the existing `FDICClient`. No new dependencies.

**Spec:** `specs/2026-11-18-phase5c-peers-design.md` (read it first; § numbers refer to it). Background: `specs/2026-11-18-phase5b-trend-design.md`.

## Global Constraints

- Branch `phase5c-peers`. Tests: `.venv.nosync/bin/python -m pytest`. No test calls the network or the Claude API. Baseline: 471 passed.
- Never touch `data/model/`, the features export, `data/raw/financials/` or `schema.FINANCIAL_FIELDS`. No S3/Athena/dbt changes. AWS cost $0.
- **Peer rule is fixed (§6); do not change any value after seeing results** (§4):
  - Specialty = `SPECGRP` at the as-of quarter from `data/raw/specialty/` (never the `institutions` endpoint).
  - Names: 1 "International Specialization", 2 "Agricultural Specialization", 3 "Credit-card Specialization", 4 "Commercial Lending Specialization", 5 "Mortgage Lending Specialization", 6 "Consumer Lending Specialization", 7 "Other Specialized Under 1 Billion", 8 "All Other Under 1 Billion", 9 "All Other Over 1 Billion".
  - Size tiers (assets = `exp(log_total_assets) * 1000` dollars; lower bound inclusive): "under $100 million" (< 1e8), "$100 million to $1 billion" (< 1e9), "$1 billion to $10 billion" (< 1e10), "over $10 billion".
  - `MIN_PEERS = 15` (bank included). Order: specialty + tier → specialty (all sizes) → no comparison.
  - Ratios: `canary.analyst.trends.TREND_RATIOS` (30).
  - Banks counted per ratio: those with a value (NaN excluded from set and count).
  - Displayed percentile: `rank(pct=True, method="average") * 100` (mid-rank).
  - Unusually low: share of banks with value ≤ bank's ≤ 0.10. Unusually high: share with value ≥ bank's ≤ 0.10. `UNUSUAL_SHARE = 0.10`.
  - Readings (exact): "unusually high among its peers too", "unusually high among its peers", "unusually low among its peers too", "unusually low among its peers", "typical for its peer group", "too few peers with this figure". National words (exact): "unusually high", "unusually low".
  - Order rows by `abs(national mid-rank percentile - 50)` descending, ties by plain name; show at most `MAX_SHOWN_PEERS = 8`.
- Section key `"peers"`, title `"Compared with similar banks"`, window `"as_of"`, registered after 5b's trends section.
- Exact code lines (§7.1):
  - "The FDIC's specialty group for this bank at {as_of}: {name}."
  - groups 8 and 9 only: "This is a general group: the FDIC did not record a lending specialty for this bank."
  - "Peers: {n} banks in the same specialty group and size tier ({tier})."
  - "Peers: {n} banks in the same specialty group (all sizes), because fewer than 15 shared its size tier."
  - "There are not enough comparable banks ({n} in its specialty group) for a reliable comparison, so none is shown."
  - no specialty value: "The FDIC recorded no specialty group for this bank at {as_of}, so no peer comparison is shown."
  - nothing nationally unusual: "None of this bank's ratios were in the national top or bottom 10% at {as_of}."
- Fixed sentence (exact): "This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal."
- No measured result for peers anywhere. No showcase re-run in this plan. One live memo only (Task 6).

## Review Focus

1. **Bank with no specialty row for the as-of quarter** (or a null `SPECGRP`): the no-specialty line, no comparison, no crash. Test in Task 3 and Task 4.
2. **Group size exactly at the minimum** (15 → used; 14 → fallback; specialty group 14 → no comparison). Test in Task 3.
3. **Tied values** (e.g. 15% of banks at 0.0): not unusual on either side, nationally or among peers. Test in Task 3.
4. **High nationally, low among peers**: reading "unusually low among its peers", and the checker rejects "unusually high among its peers" for it. Test in Task 3 and Task 5.
5. **Specialty table missing on disk**: `load_context` raises a clear error naming `python -m canary.ingest specialty`. Test in Task 2.

---

### Task 1: Specialty pull (raw table, CLI, dictionary, live pull)

**Files:**
- Modify: `src/canary/schema.py` (add `SPECIALTY_FIELDS`), `src/canary/storage.py` (add `specialty_path`), `src/canary/ingest.py` (subcommand), `src/canary/ingest_financials.py` (`quarters_to_pull` gains a `path_fn` parameter, default `financials_path`)
- Create: `src/canary/ingest_specialty.py`, `data-dictionary/fdic_specialty.md`, `tests/test_ingest_specialty.py`
- Modify: `tests/test_data_dictionary.py` (add `("fdic_specialty.md", SPECIALTY_FIELDS)`), `tests/data_checks/test_raw_files.py` (two checks)

**Interfaces:**
- Produces: `SPECIALTY_FIELDS = {"CERT": Field("int64", "FDIC Certificate #"), "REPDTE": Field("date_ymd", "Report Date"), "SPECGRP": Field("Int64", "Asset concentration specialty group"), "CITY": Field("string", "City")}` (order = API `fields=` order); `specialty_path(root: Path, repdte: date) -> Path` = `root / "specialty" / f"repdte={repdte:%Y%m%d}" / "part.parquet"`; `run_specialty(root: Path, client: FDICClient, start: date = START, refresh_latest: int = 2, force: bool = False) -> list[QuarterResult]`; CLI `python -m canary.ingest specialty [--force] [--root data/raw]`.
- Same rules as financials: values unchanged, `ingested_at` added, atomic writes, 0 rows or duplicate CERT in a quarter → `IncompleteResponseError`.

- [ ] **Step 1: Failing tests** in `tests/test_ingest_specialty.py` with the existing fake FDIC client pattern (see `tests/test_ingest_financials.py`): `test_pull_quarter_requests_specialty_fields` (fields param is `CERT,REPDTE,SPECGRP,CITY`); `test_run_writes_partitioned_parquet` (path `specialty/repdte=YYYYMMDD/part.parquet`, columns + `ingested_at`, `SPECGRP` dtype Int64); `test_skips_present_quarters_and_refreshes_latest_two`; `test_force_repulls_all`; `test_zero_rows_raises`; `test_cli_specialty_subcommand`. Add the dictionary parametrize row (fails until the doc exists).
- [ ] **Step 2: Run** `.venv.nosync/bin/python -m pytest tests/test_ingest_specialty.py tests/test_data_dictionary.py -q` — expect FAIL.
- [ ] **Step 3: Implement** the interfaces; write `data-dictionary/fdic_specialty.md` (table per field incl. `ingested_at`, the code-name list from Global Constraints, source endpoint, why separate from the 45-field pull per spec §5).
- [ ] **Step 4: Data checks** in `tests/data_checks/test_raw_files.py` (skip if `data/raw/specialty` absent): `test_specialty_covers_financials` (every financials (CERT, REPDTE) has a specialty row; report the count of null `SPECGRP`); `test_specgrp_codes_valid` (non-null codes within 1-9).
- [ ] **Step 5: Run** unit tests — PASS; full suite — PASS.
- [ ] **Step 6: Live pull (free FDIC API, a few minutes):** `.venv.nosync/bin/python -m canary.ingest specialty`. Then run `tests/data_checks/test_raw_files.py -q` — expect the two new checks to pass. Spot-check: SVB 24735 at 2022-12-31 has `SPECGRP` 9 and `CITY` "SANTA CLARA". Record the row count, quarters and null count in the report. Do not look at peer results (none exist yet).
- [ ] **Step 7: Commit** `"Specialty pull: FDIC SPECGRP and CITY per bank-quarter (separate raw table)"`.

---

### Task 2: Context loads specialty; city search for every bank

**Files:**
- Modify: `src/canary/analyst/context.py` (`Context.specialty`, `load_context(..., specialty_dir: Path = Path("data/raw/specialty"))`, bank city), `src/canary/analyst/tools.py` (`find_bank` city for all banks; tool description), `src/canary/analyst/__main__.py` (if needed, pass the default), `tests/conftest.py` (`specialty_dir` fixture; `analyst_ctx` passes it), `tests/test_analyst_context.py` (its two direct `load_context` calls pass it), `runbooks/analyst.md` (one line on city search)
- Test: `tests/test_analyst_context.py`, `tests/test_analyst_tools.py`

**Interfaces:**
- Produces: `Context.specialty: pd.DataFrame` with columns `cert` (int64), `report_date` (datetime64), `specgrp` (Int64), `city` (string); `ctx.banks["city"]` = `CITY` at the bank's last specialty row, else the failures list's city.
- Missing `specialty_dir` → `FileNotFoundError` whose message includes `python -m canary.ingest specialty`.
- Fixture `specialty_dir(raw, tmp_path)`: one parquet per quarter in `raw`, `SPECGRP`: certs 100-119 → 4, 120-127 → 9, 128-133 → 3, 24735 → 9, 57053 → 4, 59017 → 6, 1-3 → 8; `CITY` `f"City {cert}"`, except 24735 → "SANTA CLARA".

- [ ] **Step 1: Failing tests:** `test_specialty_loaded` (dtypes, rows per quarter); `test_missing_specialty_dir_raises` (message names the ingest command); `test_bank_city_from_specialty` (24735 → "SANTA CLARA"; a non-failed bank gets its city); `test_find_bank_by_city_any_bank` (query "City 105" finds cert 105, which never failed).
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** the files and the full suite — PASS.
- [ ] **Step 5: Commit** `"Analyst context: specialty table and city search for every bank"`.

---

### Task 3: Peer core (pure functions)

**Files:**
- Create: `src/canary/analyst/peers.py`, `tests/test_analyst_peers.py`

**Interfaces:**
- Consumes: `trends.TREND_RATIOS`, `labels.PLAIN_NAMES`.
- Produces (in `canary.analyst.peers`):
  - Constants `SPECIALTY_NAMES: dict[int, str]`, `GENERAL_GROUPS = frozenset({8, 9})`, `TIERS: list[tuple[float, str]]`, `MIN_PEERS = 15`, `UNUSUAL_SHARE = 0.10`, `MAX_SHOWN_PEERS = 8`, the six reading strings and two national words as named constants.
  - `size_tier(log_total_assets: float) -> str`
  - `midrank_pct(values: pd.Series, v: float) -> float` (values already NaN-free)
  - `unusual_side(values: pd.Series, v: float) -> Literal["high", "low"] | None`
  - `@dataclass PeerRow`: `feature: str`, `value: float`, `nat_pct: float`, `nat_side: Literal["high","low"]`, `peer_pct: float | None`, `peer_median: float | None`, `reading: str`.
  - `@dataclass PeerResult`: `as_of: date`, `specgrp: int | None`, `specialty_name: str | None`, `tier: str`, `basis: Literal["specialty_tier", "specialty", "too_few", "no_specialty"]`, `n_peers: int` (size of the group used; for "too_few" the specialty group size), `rows: list[PeerRow]` (all nationally unusual, ordered), `shown` property (`rows[:MAX_SHOWN_PEERS]`), `n_unusual_peers` property (rows whose reading starts "unusually").
  - `compute_peers(quarter: pd.DataFrame, cert: int, as_of: date) -> PeerResult` — `quarter` = one quarter's features rows for all banks with columns `cert`, `log_total_assets`, the 30 ratios, and `specgrp` (nullable). National set = all rows; peer set per §6.1. For basis "too_few"/"no_specialty", `rows` still lists nationally unusual ratios with `peer_pct=None`, reading not set (empty string), so the specialist can show the count but no table.

- [ ] **Step 1: Failing tests** with small synthetic quarters:
  - `test_size_tier_bounds`: ln(1e5) → "under $100 million" ($100M exactly → "$100 million to $1 billion"); 209e9 dollars → "over $10 billion".
  - `test_unusual_side_ties`: 100 values with 15 zeros: 0.0 → None; the single max → "high"; with 10 lowest distinct values, the 10th lowest → "low", the 11th → None.
  - `test_midrank_pct`: [1,2,3,4] at 4 → 87.5.
  - `test_group_order`: specialty+tier group of 15 → basis "specialty_tier", n 15; 14 in tier but 20 in specialty → "specialty", n 20; specialty group 14 → "too_few", n 14; `specgrp` NA → "no_specialty".
  - `test_bank_counted_in_its_group`: the bank itself is one of the 15.
  - `test_readings`: national high + peer high → "unusually high among its peers too"; national high + peer low → "unusually low among its peers"; national low + peer neither → "typical for its peer group"; ratio with 14 peers having a value → "too few peers with this figure", `peer_pct is None`.
  - `test_nan_excluded`: bank value NaN → ratio skipped; peer NaNs excluded from count and median.
  - `test_order_and_cap`: 10 unusual ratios → `len(shown) == 8`, ordered by distance from 50, ties by plain name.
  - `test_log_total_assets_not_a_ratio`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** — PASS; full suite — PASS.
- [ ] **Step 5: Data check** (no readings looked at): `tests/data_checks/test_peers_real.py`, marked `data`, skipped without `data/raw/specialty`: SVB 24735 at 2022-12-31 has `specgrp == 9`, tier "over $10 billion", basis in {"specialty_tier", "specialty"}. Assert nothing about rows. Run it.
- [ ] **Step 6: Commit** `"Phase 5c: peer core (fixed peer rule)"`.

---

### Task 4: Peer specialist (facts, section, code lines, table, registration)

**Files:**
- Modify: `src/canary/analyst/sections.py` (`Section.render_before: Callable[[Any], list[str]] | None = None`, last field), `src/canary/analyst/render.py` (render `render_before` lines right after the heading, before AI paragraphs), `src/canary/analyst/peers.py` (specialist), `src/canary/analyst/writer.py` (`import canary.analyst.peers` after trends; generalize the user-message line so each AI-written specialist section with a table says code adds it)
- Test: `tests/test_analyst_peers_facts.py`

**Interfaces:**
- Consumes: Task 2 `ctx.specialty`; Task 3 `compute_peers`, constants; `facts.Fact`, `facts.decimal_ordinal_forms`, `facts._count_forms`, `labels.display_forms`; 5b hooks (`code_only`, `extras`, `render`).
- Produces: `PEER_KEY = "peers"`, `PEER_SENTENCE` (exact fixed sentence), `PEER_SECTION`, `class PeerSpecialist` (`build_facts(ctx, sheet)` stores `PeerResult` in `sheet.extras["peers"]`; adds `PEER_KEY` to `sheet.code_only` when basis is "too_few"/"no_specialty" or `shown` is empty), `render_peer_lines(sheet) -> list[str]` (code lines, as `render_before`), `render_peer_table(sheet) -> list[str]` (table + fixed sentence, as `render`).
- Fact kinds (all `hindsight=False`, `quarter=as_of` unless noted): per shown ratio with `feature` set: `peer_value`, `peer_nat_pct`, `peer_nat_dir` (text), `peer_pct`, `peer_median`, `peer_reading` (text); sheet-level: `peer_specialty` (text: code and name), `peer_tier` (text), `peer_basis` (text = the code line used), `peer_count`, `peer_count_unusual`, `peer_count_unusual_peers`, `peer_count_shown`.
- Forms: values and medians `display_forms(feature, v)`; percentiles `[f"{p:.1f}", f"{p:.0f}", f"{p:.1f}%", f"{p:.0f}%", _ordinal(round(p)), *decimal_ordinal_forms(p)]`; counts `_count_forms`. No NaN anywhere.
- Table: `| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |`; "n/a" where `peer_pct` is None.
- Instructions (§7.4): use only peer facts and as-of rank facts; one ratio per sentence when stating its peer reading or peer percentile; use the reading and national words with the same meaning; say "unusually high/low", never "risky", "warning", "predict" or "forecast" (even negated); don't write a disclaimer; don't mention the outcome; end with one sentence on the overall picture using the two counts. Must not contain "fixed sentence".

- [ ] **Step 1: Failing tests:** `test_section_after_trends` (order in `sections_for(sheet)`: ... "score_history", "trends", "peers", ...); `test_facts_per_ratio_paired`; `test_percentile_forms_include_ordinals` (e.g. 98.2 → "98.2nd"); `test_no_nan_facts`; `test_code_lines_general_group` (group 9 → general-group line; group 7 forced → none); `test_basis_lines` (each of the three peer lines and the no-specialty line, exact copy, via monkeypatched `compute_peers`); `test_code_only_cases` (too_few, no_specialty, nothing unusual → `PEER_KEY in sheet.code_only`, no AI request in `write_memo` with the fake client); `test_full_note_layout` (fake client: heading, code lines before AI text, table, `PEER_SENTENCE` exactly once); `test_registered_once`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** each `tests/test_analyst_*.py` alone and the full suite — PASS.
- [ ] **Step 5: Commit** `"Phase 5c: peer specialist (facts, code lines, table)"`.

---

### Task 5: Checker rules for the peer section

**Files:**
- Modify: `src/canary/analyst/checker.py` (peer rules for `key == PEER_KEY`, reusing 5b's helpers where they fit)
- Test: `tests/test_analyst_checker_peers.py`

**Interfaces:**
- Consumes: Task 4 fact kinds, `PEER_KEY`, reading constants.
- Rules (errors join the normal list; only in the peers section):
  1. A sentence citing a `peer_reading` or `peer_pct` fact cites those for exactly one feature, and every per-ratio peer fact it cites is that feature; error text: "give one ratio per sentence when stating its peer reading".
  2. Opposite reading: citing a "typical for its peer group" reading → reject `\bunusual(ly)?\b[^.]*\bamong its peers\b`; citing an "unusually high among its peers…" reading → reject "unusually low among its peers" and "typical for its peer group"; low likewise. National words: citing `peer_nat_dir` "unusually high" → reject `\bunusually low\b(?!\s+among its peers)`; low likewise.
  3. 5b's prediction phrases plus `\brisk(y|ier)\b`.
- [ ] **Step 1: Failing tests:** correct sentence passes (value, national pct, peer pct, reading for one ratio); two ratios' readings in one sentence → one-ratio error; typical-reading sentence saying "unusual among its peers" → rejected; high-nationally/low-among-peers reading with "unusually high among its peers" → rejected; "risky" → rejected; rules don't fire in other sections.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** checker tests and full suite — PASS.
- [ ] **Step 5: Commit** `"Analyst checker: peer section rules"`.

---

### Task 6: Docs and one live memo

**Files:**
- Create: `decisions/0020-peer-comparison-descriptive.md`
- Modify: `data-dictionary/bank_notes.md`, `runbooks/analyst.md`, `runbooks/fdic-ingestion.md`, `reference/GLOSSARY.md` (specialty group, size tier, peer group, mid-rank percentile), `README.md` (Phase 5 line; test count), `RESULTS.md` (one line: peer section is descriptive, no measured result), `specs/2026-11-18-phase5c-peers-design.md` (Status: built)
- [ ] **Step 1: Decision 0020:** separate pull and why; FDIC label as published, per quarter (First Republic 6 → 9 example); SVB in group 9 stated as a finding; every fixed rule value from Global Constraints; tie handling; readings with their own peer direction; no tuning after results; QBP (not UBPR) as the source of the grouping; checker rules and their limits; no showcase re-run until 5d.
- [ ] **Step 2: Dictionary, runbooks, glossary, README, RESULTS.**
- [ ] **Step 3: Live memo (one paid call, about $0.25-0.30):** `.venv.nosync/bin/python -m canary.analyst memo --cert 24735 --out data/analyst/peer_check` (gitignored). If auth fails, don't retry more than once and don't look for credentials; report it. Put the "Compared with similar banks" section verbatim in the report; confirm the checker passed, the group-9 lines appear, no risk or prediction words. Do not commit anything under `data/` or `banks/`.
- [ ] **Step 4: Full suite; commit** `"Phase 5c docs: decision 0020, dictionary, runbooks, glossary, README/RESULTS"`.
