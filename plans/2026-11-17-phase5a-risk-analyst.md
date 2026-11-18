# Phase 5a Risk Analyst Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A memo writer that turns one bank's checked facts into a cited Obsidian note, a showcase run of ~130 notes, a model comparison, and a plain-English `ask` agent that fronts the writer.

**Architecture:** Code builds a fact sheet (ids F1..), Claude writes the AI sections as structured JSON citing fact ids, a checker verifies every number against the cited facts, and code renders the note (banner, score history, sources). The `ask` agent is a local tool-runner loop over four plain Python tools. Specialist sections for 5b-5d plug into a registry.

**Tech Stack:** Python 3.12, pandas, xgboost (existing), `anthropic` Python SDK (Messages API, structured output, Message Batches, beta tool runner), pytest.

**Spec:** `specs/2026-11-17-phase5a-risk-analyst-design.md` (read it first; section numbers below refer to it).

## Global Constraints

- Branch `phase5a-risk-analyst`. Tests: `.venv.nosync/bin/python -m pytest`. No test calls the network or the API.
- Never write into `data/model/`; the model is loaded with `xgboost.XGBClassifier().load_model` and only predicts.
- Memo as-of dates only from `2016-03-31` to the latest `report_date` in the feature export; earlier dates raise `ValueError`.
- Watchlist rule: `canary.model.metrics.flag_watchlist` (top 2%, `WATCHLIST_SHARE`); rank: `canary.replay.probe.national_rank`.
- Test window end for outcomes: `TEST_END = date(2024, 12, 31)` from `canary.model.dataset`; "after the test window" = `failure_date > date(2025, 12, 31)` (Phase 3 `horizon_end`).
- Writer model default `claude-opus-5-5`; compare models `("claude-opus-5-5", "claude-sonnet-5-5")`; `output_config.effort = "medium"`; `max_tokens = 16000`; non-batch calls use `client.beta.messages.create(..., betas=["server-side-fallback-2026-07-01"], fallbacks="default")`. Batch requests can't set `fallbacks`.
- Prices for cost reporting (per million tokens, input/output): Opus 5.5 4.00/20.00, Sonnet 5.5 2.00/10.00; batch = half.
- Fixed sentence in every note's score section (exact copy): "The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed."
- Post-hoc label (exact copy): "post-hoc check, designed after the 2023 failures".
- After-window banner (exact copy): "*After the test window: not part of the reported 2016-2024 results.*"
- API key from `ANTHROPIC_API_KEY` (`.env`, gitignored) or an `ant auth login` profile; never committed.
- Every new table/file format goes in `data-dictionary/`; decisions 0016-0018 in `decisions/`.
- Notes go to `banks/<Title Case Name> (<cert>).md`; compare and cache outputs go to `data/analyst/` (not committed).

## Review Focus

1. **Missing values** (tier 1 ratio null after 2020 for community-bank-leverage banks, uninsured null): facts skip nulls and the note shows "not reported", never "nan". Test in Task 3.
2. **Bad as-of** (before 2016, after the last report, or a quarter the bank didn't report): a clear `ValueError` naming the bank and its valid range. Test in Task 2.
3. **Bank names unsafe for file names** (`/`, `:`, `#`, quotes): sanitized, and two runs give the same path. Test in Task 5.
4. **Dates and years in prose** ("2023", "Q4 2022", "2022-12-31") must be checked like numbers, and a spelled-out date of a cited fact must pass. Test in Task 4.
5. **Batch partial failure** (errored, expired, refused or failed-check results) are retried one by one through the normal path, never dropped silently; the run report lists anything still failing. Test in Task 8.

---

### Task 1: Package, plain names, and scored context

**Files:**
- Modify: `pyproject.toml` (add optional group `analyst = ["anthropic>=1.1,<2"]`; install with `.venv.nosync/bin/pip install -e '.[dev,model,analyst]'`)
- Create: `src/canary/analyst/__init__.py`, `src/canary/analyst/labels.py`, `src/canary/analyst/context.py`
- Modify: `tests/conftest.py` (add fixtures below)
- Test: `tests/test_analyst_labels.py`, `tests/test_analyst_context.py`

**Interfaces:**
- Produces:
  - `labels.PLAIN_NAMES: dict[str, str]` for all 31 `FEATURE_COLUMNS` (e.g. `htm_unrealized_loss_to_equity` → "losses on bonds held to maturity, as a share of equity").
  - `labels.UNIT: dict[str, str]` with values `"pct"` (already percent: equity_to_assets, leverage_ratio, tier1_risk_based_ratio, total_risk_based_ratio, return_on_assets, return_on_equity, net_interest_margin, efficiency_ratio, loans_to_deposits), `"frac"` (all other ratios), `"assets"` (log_total_assets: dollars = exp(v) * 1000).
  - `labels.display_forms(feature: str, value: float) -> list[str]`: first item is the primary display; all allowed forms for the checker. `frac` 0.9812 → `["98.1%", "98%", "0.98"]`; `pct` 8.53 → `["8.5%", "9%", "8.53"]`; `assets` → `["$209.0 billion", "$209 billion"]` (use million below $1B). Negative values keep the sign.
  - `context.Context` dataclass: `features: pd.DataFrame` (from `load_dataset`), `scored: pd.DataFrame` (rows ≥ 2016-03-31 with `score`, `rank`, `n_banks`, `percentile`, `flagged`), `failures: pd.DataFrame` (cert, name, city, state, failure_date), `model: xgboost.XGBClassifier`, `model_run: str` (first 12 hex of model.json sha256), `latest_quarter: date`.
  - `Context` also has `banks: pd.DataFrame` (one row per cert: `cert`, `name`, `state` = `STALP` at the bank's last report read from `financials_dir` partitions with `columns=["CERT", "STALP", "REPDTE"]`, `first_report`, `last_report`, `failure_date`, `city` from failures or null).
  - `context.load_context(features: Path, model_dir: Path, failures: Path, financials_dir: Path = Path("data/raw/financials"), cache_dir: Path = Path("data/analyst")) -> Context`. Scores are cached at `cache_dir/scores.parquet` with `cache_dir/scores.json` holding `{"model_run", "features_size", "features_mtime"}`; recomputed when any differ.
  - `context.score_rows(features: pd.DataFrame, model) -> pd.DataFrame`: the scoring used above (percentile = 100 × (1 − (rank − 1) / n_banks), matching `case_studies.csv`).
- Test fixtures added to `tests/conftest.py`: `trained_model` (module scope, same small-grid training as `tests/test_replay_probe.py::model`), `failures_path` (tmp parquet with `CERT, NAME, CITY, PSTALP, FAILDATE` for certs 3, 24735, 57053, 59017 from `raw`), `financials_dir` (tmp `repdte=YYYYMMDD/part.parquet` partitions with `CERT, STALP, REPDTE` for the last two quarters), `analyst_ctx` (a `Context` built from `raw`, `trained_model`, `failures_path` and a tmp cache dir).

- [ ] **Step 1: Write failing tests**

```python
def test_plain_names_cover_all_features():
    assert set(PLAIN_NAMES) == set(FEATURE_COLUMNS) == set(UNIT)

def test_display_forms():
    assert display_forms("htm_unrealized_loss_to_equity", 0.9812) == ["98.1%", "98%", "0.98"]
    assert display_forms("equity_to_assets", 8.53)[0] == "8.5%"
    assert display_forms("log_total_assets", math.log(209_000_000))[0] == "$209.0 billion"

def test_scored_only_from_2016(analyst_ctx):
    assert analyst_ctx.scored["report_date"].min() == pd.Timestamp("2016-03-31")

def test_flags_match_phase3_for_test_rows(analyst_ctx, trained_model, df):
    phase3 = _score_test(df, trained_model).set_index(["cert", "report_date"])["flagged"]
    ours = analyst_ctx.scored.set_index(["cert", "report_date"])["flagged"]
    assert ours.reindex(phase3.index).equals(phase3)

def test_cache_reused_then_invalidated(tmp_path, ...):
    # second load reads the cache (monkeypatch score_rows to raise); touching the features file recomputes
```

- [ ] **Step 2:** Run `.venv.nosync/bin/python -m pytest tests/test_analyst_labels.py tests/test_analyst_context.py -v`; expect import errors.
- [ ] **Step 3:** Implement `labels.py` and `context.py` with the interfaces above. `test_flags_match_phase3_for_test_rows` holds only if flags are computed per report date over the same banks as Phase 3, so rank each quarter over all scored banks that quarter.
- [ ] **Step 4:** Re-run; expect PASS. Run the full suite; expect all 179 existing tests still pass.
- [ ] **Step 5:** Commit `"Analyst: plain names, display forms and scored context"`.

### Task 2: Outcomes and as-of rules

**Files:**
- Create: `src/canary/analyst/outcome.py`
- Test: `tests/test_analyst_outcome.py`

**Interfaces:**
- Consumes: `Context` (Task 1).
- Produces:
  - `Outcome` dataclass: `kind: Literal["caught", "missed", "false_alarm", "quiet", "open_watchlist"]`, `after_test_window: bool`, `failure_date: date | None`, `first_flag: date | None`, `lead_quarters: int | None`, `still_reporting: bool`, `last_report: date`.
  - `default_as_of(ctx, cert: int) -> date`: last report before failure for a failed bank, else `ctx.latest_quarter`.
  - `validate_as_of(ctx, cert: int, as_of: date) -> None`: raises `ValueError` mentioning the cert and its valid range when as_of < 2016-03-31, after the bank's last report, or not a quarter it reported.
  - `classify(ctx, cert: int, as_of: date) -> Outcome`, rules from spec §5.3: failed + flagged at a report 1-4 quarters before failure → `caught` with `first_flag`/`lead_quarters` from `canary.model.metrics.lead_times` on that bank's rows; failed + not → `missed`; not failed + flagged at as-of + as_of == latest quarter → `open_watchlist`; not failed + flagged at as-of → `false_alarm`; else `quiet`. `after_test_window` when failure_date > 2025-12-31.

- [ ] **Step 1: Write failing tests** using `analyst_ctx` (synthetic failures are caught strongly via `STRONG`):

```python
def test_default_as_of_failed_bank(analyst_ctx):
    assert default_as_of(analyst_ctx, 3) == date(2019, 9, 30)

def test_default_as_of_open_bank(analyst_ctx):
    assert default_as_of(analyst_ctx, 100) == analyst_ctx.latest_quarter

@pytest.mark.parametrize("as_of", [date(2015, 12, 31), date(2019, 12, 31), date(2019, 8, 15)])
def test_bad_as_of_raises(analyst_ctx, as_of):
    with pytest.raises(ValueError, match="cert 3"):
        validate_as_of(analyst_ctx, 3, as_of)

def test_caught_uses_phase3_lead_time(analyst_ctx): ...      # kind == "caught", 1 <= lead_quarters <= 4
def test_missed(analyst_ctx, monkeypatch): ...               # force flagged False for cert 3 rows → "missed"
def test_after_test_window_flag(analyst_ctx): ...            # set a failure_date 2026-05-01 → after_test_window True
def test_open_watchlist_vs_false_alarm(analyst_ctx): ...     # same bank flagged at latest vs earlier quarter
```

- [ ] **Step 2:** Run; expect FAIL.
- [ ] **Step 3:** Implement `outcome.py`.
- [ ] **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: outcome classification and as-of rules"`.

### Task 3: Fact sheet and section registry

**Files:**
- Create: `src/canary/analyst/facts.py`, `src/canary/analyst/sections.py`
- Modify: `src/canary/replay/probe.py` (rename `_contribs` to public `contribution_matrix(model, rows) -> np.ndarray`; keep `_contribs = contribution_matrix` so Phase 4 code is unchanged)
- Test: `tests/test_analyst_facts.py`

**Interfaces:**
- Consumes: `Context`, `Outcome`, `classify`, `validate_as_of`, `display_forms`, `PLAIN_NAMES`.
- Produces:
  - `Fact` dataclass: `id: str`, `label: str`, `quarter: date | None`, `value: float | str`, `display: str`, `forms: list[str]`, `hindsight: bool`, `source: str` (file path and column).
  - `FactSheet` dataclass: `cert`, `name` (title case), `as_of`, `outcome: Outcome`, `facts: list[Fact]`, `history: pd.DataFrame` (8 quarters to as-of: report_date, rank, n_banks, flagged), `after_history: pd.DataFrame` (quarters after as-of), `cant_see: str` (fixed paragraph, spec §5.4), `section_keys: list[str]`; method `by_id(id) -> Fact`.
  - `build_fact_sheet(ctx, cert: int, as_of: date | None = None) -> FactSheet`. Facts, ids assigned in this order: bank identity and as-of; score, rank, n_banks, percentile, flagged; watchlist share 2%; each non-null feature at as-of with the national median that quarter (two facts); top 5 drivers up and down from `contribution_matrix` (feature, value, contribution); outcome facts (`hindsight=True`): failure date, first flag quarter and lead quarters, later ranks; for certs in `data/replay/replay_banks.csv`, the run-risk rank at as-of labeled with the post-hoc label; training-mix facts from `data/replay/posthoc_metrics.json` `failure_mix` when the bank lacks a credit-loss profile (`canary.replay.analysis.credit_loss_profile`). Every fact with a date gets forms for "YYYY-MM-DD", "Q<n> YYYY", "Month D, YYYY" and "YYYY".
  - `sections.Section` dataclass: `key`, `title`, `window: Literal["as_of", "hindsight"]`, `instructions: str`, `ai_written: bool`.
  - `sections.ANALYST_SECTIONS: list[Section]` in spec §5.2 order: summary, warning_signs, score (as_of, AI); score_history (code); outcome (hindsight, AI; title chosen from §5.3 by `Outcome.kind`, none for `quiet`); what_next (hindsight, AI); sources (code).
  - `sections.SPECIALISTS: list[Specialist]` (empty in 5a); `Specialist` protocol: `key`, `sections: list[Section]`, `build_facts(ctx, sheet) -> list[Fact]`; `sections.register(specialist)`; `sections.all_sections(kind) -> list[Section]` inserting specialist sections after score_history.

- [ ] **Step 1: Write failing tests**

```python
def test_fact_ids_unique_and_sequential(analyst_ctx): ...       # F1..Fn
def test_no_nan_facts(analyst_ctx):                             # Review Focus 1
    sheet = build_fact_sheet(analyst_ctx, 100)                   # set tier1 NaN for cert 100 at as-of first
    assert all(f.display != "nan" for f in sheet.facts)
    assert not any("tier 1" in f.label.lower() and f.quarter == sheet.as_of for f in sheet.facts)
def test_as_of_facts_not_after_as_of(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3)
    assert all(f.quarter is None or f.quarter <= sheet.as_of for f in sheet.facts if not f.hindsight)
def test_drivers_match_phase4_contributions(analyst_ctx): ...    # same top feature as replay.probe.contributions
def test_posthoc_fact_labeled(analyst_ctx, tmp_replay_dir): ...  # run-risk fact label contains the post-hoc label
def test_quiet_bank_has_no_outcome_section(): ...
def test_contribution_matrix_alias():
    assert probe._contribs is probe.contribution_matrix
```

- [ ] **Step 2:** Run; expect FAIL.
- [ ] **Step 3:** Implement. Paths to `data/replay/*` come from a `replay_dir: Path = Path("data/replay")` parameter on `build_fact_sheet` so tests pass a tmp dir; missing replay files mean those facts are skipped.
- [ ] **Step 4:** Run this file and `tests/test_replay_probe.py`; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: fact sheet and section registry"`.

### Task 4: Citation checker

**Files:**
- Create: `src/canary/analyst/checker.py`
- Test: `tests/test_analyst_checker.py`

**Interfaces:**
- Consumes: `FactSheet`, `Section`.
- Produces:
  - Memo shape (also the JSON schema in Task 6): `{"sections": [{"key": str, "paragraphs": [{"sentences": [{"text": str, "cites": [str]}]}]}]}`.
  - `extract_tokens(text: str) -> list[str]`: numbers (`-?\$?\d[\d,]*(\.\d+)?` with an optional `%`, `x`, ` billion`, ` million` suffix), ISO dates, "Q<n> YYYY", "Month D, YYYY", bare years. Normalized: commas removed, lower case.
  - `check_memo(memo: dict, sheet: FactSheet, sections: list[Section]) -> list[str]`: error strings, empty when OK. Errors for: a token not in the normalized forms of that sentence's cited facts; an unknown fact id; a hindsight fact cited in an `as_of` section; a missing or unexpected section key; a sentence with a number but no cites.

- [ ] **Step 1: Write failing tests** (build a small `FactSheet` by hand in the test file):

```python
def test_passes_when_numbers_match_cited_facts(): ...       # "Bond losses were 98% of equity." cites F7 (0.9812) → []
def test_number_not_in_cited_fact(): ...                     # "97%" → one error naming the sentence and "97%"
def test_number_without_cites(): ...
def test_unknown_id(): ...
def test_hindsight_fact_in_as_of_section(): ...              # failure date cited in summary → error
@pytest.mark.parametrize("text", ["as of 2022-12-31", "in Q4 2022", "on December 31, 2022", "in 2022"])
def test_date_forms_pass(text): ...                          # Review Focus 4
def test_uncited_year_fails(): ...                           # "in 2023" citing only a 2022 fact → error
def test_missing_section(): ...
```

- [ ] **Step 2:** Run; expect FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: citation checker"`.

### Task 5: Note renderer

**Files:**
- Create: `src/canary/analyst/render.py`
- Test: `tests/test_analyst_render.py`

**Interfaces:**
- Consumes: `FactSheet`, memo dict, `Section`.
- Produces:
  - `note_path(out_dir: Path, name: str, cert: int) -> Path`: `out_dir / f"{safe} ({cert}).md"`, `safe` = title-cased name with `/\:*?"<>|#^[]` replaced by `-`.
  - `render_note(sheet, memo, sections, meta: dict) -> str`. `meta` keys: `writer_model`, `written_at` (ISO), `model_run` (`Context.model_run`). Output: YAML front matter (spec §5.2 fields; `checked: true`), `# <Name> (cert <cert>)`, the outcome banner (hindsight line; plus the after-window line from Global Constraints when `after_test_window`; no banner for `quiet` and `open_watchlist` banks other than "*Outcome not yet known.*" for open_watchlist), AI sections from the memo in registry order with sentences joined into paragraphs and cite ids removed from the text, the fixed score sentence (Global Constraints) appended to the score section, the code-rendered score-history table (mark "▲ watchlist" and "(first flag)"), "What happened next" with an `after_history` table, and Sources listing each cited fact `id · label · quarter · display · source`.

- [ ] **Step 1: Write failing tests**

```python
def test_unsafe_names(tmp_path):                                    # Review Focus 3
    p = note_path(tmp_path, "BANK OF A/B: #1", 7)
    assert p.name == "Bank Of A-B- -1 (7).md" and p == note_path(tmp_path, "BANK OF A/B: #1", 7)
def test_front_matter_fields(): ...
def test_after_window_banner_exact(): ...
def test_fixed_score_sentence_present(): ...
def test_first_flag_marked_in_history(): ...
def test_sources_list_only_cited_facts(): ...
```

- [ ] **Step 2:** Run; expect FAIL. **Step 3:** Implement. **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: note renderer"`.

### Task 6: Memo writer and `memo` command

**Files:**
- Create: `src/canary/analyst/writer.py`, `src/canary/analyst/__main__.py`, `tests/analyst_fakes.py`
- Test: `tests/test_analyst_writer.py`

**Interfaces:**
- Consumes: Tasks 1-5.
- Produces:
  - Constants: `DEFAULT_MODEL = "claude-opus-5-5"`, `EFFORT = "medium"`, `MAX_TOKENS = 16000`, `FALLBACK_BETA = "server-side-fallback-2026-07-01"`, `PRICES = {"claude-opus-5-5": (4.0, 20.0), "claude-sonnet-5-5": (2.0, 10.0)}`.
  - `memo_schema(sections: list[Section]) -> dict`: JSON schema for the memo shape (Task 4), `additionalProperties: false`, `key` an enum of the AI-written section keys.
  - `build_request(sheet, sections, model: str, errors: list[str] | None = None) -> dict`: kwargs for `messages.create` (no fallbacks): `model`, `max_tokens`, `system` (role, rules: cite ids on every sentence with a number, use only facts, no hindsight in as-of sections, rank not probability, keep the post-hoc label, 2-4 sentence summary, plain English for a non-banker), `messages` (the fact sheet as a compact table plus section instructions; when `errors`, the previous memo's errors appended), `output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": memo_schema(...)}}`.
  - `parse_response(message) -> dict`: raises `RefusalError` when `stop_reason == "refusal"`, `TruncatedError` on `"max_tokens"`; else `json.loads` of the first text block.
  - `MemoResult` dataclass: `cert`, `as_of`, `path: Path | None`, `ok: bool`, `attempts: int`, `errors: list[str]`, `input_tokens: int`, `output_tokens: int`, `model: str`, `cost_usd: float`.
  - `write_memo(ctx, cert: int, as_of: date | None = None, *, client, model: str = DEFAULT_MODEL, out_dir: Path = Path("banks"), first_memo: dict | None = None) -> MemoResult`: build sheet → (use `first_memo` if given, else one `client.beta.messages.create(**build_request(...), betas=[FALLBACK_BETA], fallbacks="default")`) → check → on errors, one retry with errors → render and write only if the check passes. Usage summed over attempts; cost from `PRICES`.
  - CLI `python -m canary.analyst memo --cert N [--as-of YYYY-MM-DD] [--model M] [--out banks]` with shared args `--features data/features/fct_bank_features.parquet --model-dir data/model --failures data/raw/failures/failures.parquet`; exits 1 with the errors when the memo fails the check.
  - `tests/analyst_fakes.py`: `FakeClient(responses: list[dict | str])` exposing `beta.messages.create(**kw)` (records kwargs, returns a message with `stop_reason`, `content=[text block]`, `usage`), plus `beta.messages.tool_runner` and `messages.batches.{create,retrieve,results}` used by Tasks 7-8.

- [ ] **Step 1: Write failing tests**

```python
def test_good_memo_written(analyst_ctx, tmp_path): ...        # one call; file exists; ok, attempts == 1
def test_bad_then_good_retries_once(analyst_ctx, tmp_path):
    # first memo cites a wrong number; second is right → attempts == 2, second request's last message contains the error text
def test_bad_twice_not_written(analyst_ctx, tmp_path): ...    # ok False, no file
def test_refusal_raises_clean_error(analyst_ctx, tmp_path): ...
def test_request_shape(analyst_ctx):
    kw = build_request(build_fact_sheet(analyst_ctx, 3), all_sections("caught"), "claude-opus-5-5")
    assert kw["output_config"]["effort"] == "medium" and "fallbacks" not in kw
def test_create_called_with_fallbacks(analyst_ctx, tmp_path): ...  # betas and fallbacks="default" passed
def test_cost(): ...                                          # 1M in + 1M out on Opus = 24.0
```

- [ ] **Step 2:** Run; expect FAIL. **Step 3:** Implement. **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: memo writer and memo command"`.

### Task 7: Agent tools and `ask` command

**Files:**
- Create: `src/canary/analyst/tools.py`, `src/canary/analyst/agent.py`
- Modify: `src/canary/analyst/__main__.py` (add `ask`)
- Test: `tests/test_analyst_tools.py`

**Interfaces:**
- Consumes: `Context`, `build_fact_sheet`, `write_memo`.
- Produces:
  - Plain functions returning JSON strings: `find_bank(ctx, query: str, state: str | None = None, failed_year: int | None = None) -> str` (case-insensitive substring on name for all banks, on city for failed banks, exact on cert when the query is digits; up to 10: cert, name, state, city or null, first_report, last_report, failure_date); `get_bank_facts(ctx, cert, as_of=None) -> str` (facts as id/label/quarter/display, plus outcome kind); `list_watchlist(ctx, quarter=None) -> str` (default latest; cert, name, rank); `write_memo_tool(ctx, client, model, cert, as_of=None) -> str` (path, ok, errors). Errors such as a bad as-of come back as `{"error": "..."}`, never raised.
  - `find_bank` searches `ctx.banks` (Task 1).
  - `agent.make_tools(ctx, client, model) -> list`: the four wrapped with `anthropic.beta_tool` (closures over ctx/client), names `find_bank`, `get_bank_facts`, `list_watchlist`, `write_memo`.
  - `agent.SYSTEM`: answer only from tool results; call `write_memo` for anything memo-sized; if several banks match, list them and ask; say when the data can't answer.
  - `agent.ask(question: str, ctx, client, model: str = DEFAULT_MODEL) -> str`: `client.beta.messages.tool_runner(model=model, max_tokens=MAX_TOKENS, system=SYSTEM, tools=make_tools(...), messages=[{"role": "user", "content": question}], output_config={"effort": EFFORT}).until_done()`; returns the text; a refusal returns a short apology line.
  - CLI `python -m canary.analyst ask "question" [--model M]` prints the answer.

- [ ] **Step 1: Write failing tests**

```python
def test_find_bank_by_city_failed_only(analyst_ctx): ...        # city match for a failed bank; open banks not matched by city
def test_find_bank_by_cert_and_name(analyst_ctx): ...
def test_find_bank_caps_at_10(analyst_ctx): ...                  # "bank" matches many
def test_get_bank_facts_bad_as_of_returns_error(analyst_ctx): ...
def test_list_watchlist_size(analyst_ctx): ...                   # ceil(n * 0.02) banks
def test_make_tools_names(analyst_ctx): ...
def test_ask_uses_tool_runner(analyst_ctx): ...                  # FakeClient.tool_runner records kwargs, returns final text
```

- [ ] **Step 2:** Run; expect FAIL. **Step 3:** Implement. **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: agent tools and ask command"`.

### Task 8: Showcase set and batch run

**Files:**
- Create: `src/canary/analyst/showcase.py`
- Modify: `src/canary/analyst/__main__.py` (add `showcase`)
- Test: `tests/test_analyst_showcase.py`

**Interfaces:**
- Consumes: `Context`, `default_as_of`, `classify`, `build_fact_sheet`, `build_request`, `write_memo` (with `first_memo`).
- Produces:
  - `showcase_banks(ctx, model_dir: Path, replay_dir: Path) -> list[tuple[int, date, str]]` (cert, as_of, group), groups and as-of per spec §5.1; deduplicated with first group winning in this order: case study, test miss, test catch, after window, latest watchlist, false alarm; a past false alarm on the latest watchlist uses the latest quarter.
  - `run_showcase(ctx, client, model: str, out_dir: Path, report_path: Path, poll_seconds: int = 60) -> dict`: one `client.messages.batches.create` with `custom_id = f"{cert}-{as_of}"` and `build_request(...)` params; poll `retrieve` until `processing_status == "ended"`; for each result: succeeded → `write_memo(..., first_memo=parsed)` (which retries normally on a failed check); errored, expired, canceled or refusal → `write_memo(...)` from scratch (normal path with fallbacks). Report JSON: counts written / failed, per-bank attempts, errors, tokens, cost (batch tokens at half price).
  - CLI `python -m canary.analyst showcase [--model M] [--dry-run]`; `--dry-run` prints the bank list and an estimated cost (2,000 output and fact-sheet input tokens per bank) without calling the API.

- [ ] **Step 1: Write failing tests**

```python
def test_groups_and_dedup(analyst_ctx, tmp_model_dir, tmp_replay_dir): ...
def test_past_false_alarm_on_latest_watchlist_uses_latest(analyst_ctx, ...): ...
def test_partial_batch_failures_retried(analyst_ctx, tmp_path):   # Review Focus 5
    # FakeClient batch: one succeeded, one errored, one expired, one refusal → 3 normal retries, all 4 written
def test_still_failing_listed_in_report(analyst_ctx, tmp_path): ...
def test_dry_run_makes_no_calls(analyst_ctx, capsys): ...
```

- [ ] **Step 2:** Run; expect FAIL. **Step 3:** Implement. **Step 4:** Run; expect PASS.
- [ ] **Step 5:** Commit `"Analyst: showcase set and batch run"`.

### Task 9: Model comparison command

**Files:**
- Create: `src/canary/analyst/compare.py`
- Modify: `src/canary/analyst/__main__.py` (add `compare`)
- Test: `tests/test_analyst_compare.py`

**Interfaces:**
- Consumes: `write_memo`, `CASE_STUDY_CERTS`, `PRICES`.
- Produces:
  - `compare_models(ctx, client, models=("claude-opus-5-5", "claude-sonnet-5-5"), certs=(24735, 57053, 59017), out_dir=Path("data/analyst/compare")) -> dict`: for each model and cert, `write_memo(..., model=m, out_dir=out_dir / m)` (normal API, not batch); returns and writes `out_dir/compare.json` with per model: passed first try, passed after retry, failed, input/output tokens, cost; per memo: path and attempts.
  - CLI `python -m canary.analyst compare` prints a small table and the memo paths for side-by-side reading.

- [ ] **Step 1: Write failing test** `test_compare_counts_and_cost` with a FakeClient: Opus passes all first try, Sonnet needs one retry on one bank → counts and costs as expected; files under each model folder.
- [ ] **Step 2:** Run; FAIL. **Step 3:** Implement. **Step 4:** Run; PASS; full suite PASS.
- [ ] **Step 5:** Commit `"Analyst: model comparison command"`.

### Task 10: Live model comparison (needs Victor)

**Files:**
- Create: `analysis/phase5a-model-compare.md`
- Modify: `.env` (Victor adds `ANTHROPIC_API_KEY`; not committed)

- [ ] **Step 1:** Ask Victor to create an API key at console.anthropic.com with a few dollars of credit, or run `ant auth login`, and add it to `.env`. Check: `.venv.nosync/bin/python -c "import anthropic; anthropic.Anthropic().models.retrieve('claude-opus-5-5')"` prints the model.
- [ ] **Step 2:** Run `.venv.nosync/bin/python -m canary.analyst compare`. Expected: 6 memos under `data/analyst/compare/`, cost about $0.30.
- [ ] **Step 3:** Write `analysis/phase5a-model-compare.md`: the compare table, links to the 6 memos (copied into `analysis/phase5a-model-compare/` so they're committed), and plain-English observations. Ask Victor to read them side by side and pick the showcase model. **Stop until Victor picks.**
- [ ] **Step 4:** Commit `"Phase 5a: Opus vs Sonnet memo comparison"`.

### Task 11: Live showcase run and docs

**Files:**
- Create: `banks/*.md` (generated), `decisions/0016-analyst-memo-design.md`, `decisions/0017-analyst-agent-tool-runner.md`, `decisions/0018-failures-after-test-window.md`, `data-dictionary/bank_notes.md`, `data-dictionary/analyst_outputs.md`, `runbooks/analyst.md`
- Modify: `README.md`, `reference/STACK.md` (Claude API no longer "planned"), `reference/GLOSSARY.md` (fact sheet, citation checker, tool runner), `canary-roadmap.md`, `RESULTS.md` (the 2026 failures as an extra out-of-sample line), `daily-log.md`

- [ ] **Step 1:** `python -m canary.analyst showcase --dry-run --model <Victor's pick>`; show Victor the count and estimate; run without `--dry-run` after his OK.
- [ ] **Step 2:** Check: the run report shows every bank written or listed as failed; open 3 notes (SVB, a caught bank, a latest-watchlist bank) and confirm banner, score sentence, history table and sources render in Obsidian.
- [ ] **Step 3:** Try `ask` live with "write up the bank in Santa Clara that failed in 2023" and "which banks are on the watchlist right now?"; paste the answers into the runbook as examples.
- [ ] **Step 4:** Write decisions 0016 (fact sheet + one call + checker; as-of rule; score not a probability; model comparison result), 0017 (tool runner vs Managed Agents), 0018 (post-test-window labels; README headline unchanged). Data dictionary for the note front matter and `data/analyst/` files. Runbook with the four commands, costs and the API-key setup. README: Phase 5a done, the two 2026 catches as a separate out-of-sample line, link to a sample note. Roadmap card and daily log.
- [ ] **Step 5:** Full suite passes; commit `"Phase 5a: showcase notes and docs"`.
