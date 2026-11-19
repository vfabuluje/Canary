# Phase 5b Ratio Trends Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a descriptive "How its ratios moved" section to every analyst memo: which of the bank's own ratios left their prior range at the as-of quarter, how fast, and the model's contribution for each, side by side.

**Architecture:** Pure functions in `canary/analyst/trends.py` compute ranges, changes and ordering from one bank's feature history. A `TrendSpecialist` registers with 5a's section registry, adds facts to the sheet and supplies a code-rendered table. The registry gains two small hooks: a per-sheet "code only" switch and a per-section render function. The checker gains three trend-only rules.

**Tech Stack:** Python 3.12, pandas, xgboost (existing, predict/contributions only), pytest. No new dependencies.

**Spec:** `specs/2026-11-18-phase5b-trend-design.md` (read it first; § numbers below refer to it). 5a background: `specs/2026-11-17-phase5a-risk-analyst-design.md`.

## Global Constraints

- Branch `phase5b-trend-agent`. Tests: `.venv.nosync/bin/python -m pytest`. No test calls the network or the API. Baseline: 400 passed.
- Never write into `data/model/`. No AWS. No new data files.
- **Range rule is fixed (§5); do not change any of these values after seeing results** (§4):
  - `TREND_RATIOS` = all of `canary.model.dataset.FEATURE_COLUMNS` except `log_total_assets` (30).
  - `YTD_RATIOS` = `return_on_assets`, `return_on_equity`, `net_interest_margin`, `efficiency_ratio`, `net_charge_offs_to_loans_ann`, `provision_to_assets_ann`, `interest_expense_to_assets_ann`.
  - Point-in-time window: the 12 calendar quarters before as-of (as-of excluded), at least 8 with a value.
  - Year-to-date window: the same calendar quarter in each of the 3 prior years, at least 2 with a value.
  - Outside = as-of value < min or > max (equal to a bound is inside). Excess in percentage points; order by excess ÷ max(range width, 1.0 pp), ties by plain name; show at most 6.
  - Changes: 1q and 4q for point-in-time; 4q only for year-to-date; in percentage points.
  - Direction: contribution ≥ +0.05 "pushed the score up"; ≤ -0.05 "pushed the score down"; else "little effect on the score".
  - Rank phrase by percentile vs. the same quarter a year earlier: higher by more than 1.0 → "the model rated it riskier than a year earlier"; lower by more than 1.0 → "the model rated it safer than a year earlier"; else "about the same as a year earlier". No year-earlier score → omitted.
- Percentage points: `pct`-unit ratios (`labels.UNIT[name] == "pct"`) are already percent, so pp = difference; `frac`-unit ratios: pp = difference × 100.
- Section key `"trends"`, title `"How its ratios moved"`, window `"as_of"`, placed by the registry after "Score history".
- Fixed sentence (exact copy, code-rendered at the end of the section): "This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure."
- None-outside line (exact copy): "None of this bank's ratios were outside their own prior range at {as_of}."
- Too-little-history line (exact copy): "This bank has too little history before {as_of} to compare its ratios with its own prior range."
- No measured result for trends anywhere (no recall, catches, AUC, lead time) in code output, notes or docs.
- Every new note part goes in `data-dictionary/bank_notes.md`; the range rule and its SVB consequence go in `decisions/0019-ratio-trends-descriptive.md`.

## Review Focus

1. **Bank with partial history** (a young bank, or as-of in early 2016 with gaps): some ratios have too little history, others don't; ratios with no as-of value are skipped; nothing crashes and no "nan" reaches a fact or the table. Test in Task 1 and Task 3.
2. **Flat ratio** (e.g. brokered deposits 0.0% for 12 quarters, then 0.3%): it counts as outside, but the 1 pp width floor keeps it below a large move on a wide range; a value exactly equal to the max is inside. Test in Task 1.
3. **Unit mix-up between `pct` and `frac` ratios**: a frac change of 0.418 is "+41.8 pp"; a pct change of 1.2 is "+1.2 pp" (not +120). Test in Task 1 and Task 3.
4. **Negative values and signs**: HTM loss of -11.7% (a gain) and a negative change render as "-11.7%" and "-41.8 pp", and the checker accepts them (including a Unicode minus). Test in Task 3.
5. **No year-earlier score** (as-of in 2016, or the bank didn't report a year earlier): the rank-phrase facts are absent, the section still writes. Test in Task 3.

---

### Task 1: Trend core (pure functions) and the SVB data checks

**Files:**
- Create: `src/canary/analyst/trends.py`
- Test: `tests/test_analyst_trends.py`
- Create: `tests/data_checks/test_trends_real.py`

**Interfaces:**
- Consumes: `canary.model.dataset.FEATURE_COLUMNS`; `canary.analyst.labels.PLAIN_NAMES`, `UNIT`.
- Produces (in `canary.analyst.trends`):
  - Constants `TREND_RATIOS: tuple[str, ...]`, `YTD_RATIOS: frozenset[str]`, `MAX_SHOWN = 6`, `WIDTH_FLOOR_PP = 1.0`, `DIRECTION_CUTOFF = 0.05`, `RANK_SAME_PP = 1.0`.
  - `@dataclass RatioTrend`: `feature: str`, `value: float`, `lo: float`, `hi: float`, `window: Literal["pit", "ytd"]`, `n_prior: int`, `excess_pp: float`, `score: float` (excess ÷ floored width), `change_1q_pp: float | None`, `change_4q_pp: float | None`, `contribution: float`, `direction: str`.
  - `@dataclass TrendResult`: `as_of: date`, `checked: int` (ratios with a value and enough history), `too_little: int`, `outside: list[RatioTrend]` (all outside, ordered), `shown` property → `outside[:MAX_SHOWN]`.
  - `to_pp(feature: str, delta: float) -> float`
  - `prior_values(history: pd.DataFrame, feature: str, as_of: date) -> pd.Series` (window per §5.2; NaN dropped)
  - `direction_label(contribution: float) -> str`
  - `rank_phrase(pct_now: float, pct_prior: float) -> str`
  - `compute_trends(history: pd.DataFrame, as_of: date, contributions: dict[str, float]) -> TrendResult` — `history` is one bank's feature rows (`report_date` datetime64 + feature columns), any order; a feature missing from `contributions` gets 0.0.

- [ ] **Step 1: Write failing tests** in `tests/test_analyst_trends.py`, building small synthetic one-bank histories with a helper `_hist(feature, values_by_quarter)`:
  - `test_pit_window_is_prior_12_quarters`: as-of 2022-03-31 uses 2019-03-31..2021-12-31 (12 values) and excludes as-of and 2018-12-31.
  - `test_pit_needs_8_of_12`: 7 values → counted in `too_little`, not `checked`; 8 → checked.
  - `test_ytd_window_same_quarter_prior_3_years`: `return_on_assets` at 2022-09-30 uses 2021-09-30, 2020-09-30, 2019-09-30 only; a big 2022-06-30 value is ignored.
  - `test_ytd_needs_2_of_3`.
  - `test_nan_skipped_not_zero`: NaNs in the window aren't treated as 0 (min stays the real min); NaN at as-of → ratio skipped.
  - `test_reporting_gap_shrinks_window`: missing quarters reduce `n_prior`; the window does not reach further back.
  - `test_equal_to_bound_is_inside`.
  - `test_excess_and_ordering_with_floor`: flat 0.0 → 0.003 (frac, excess 0.3 pp, width floored to 1 → score 0.3) ranks below a ratio 5 pp past a 10 pp-wide range (score 0.5); ties broken by plain name.
  - `test_cap_six_and_total`: 8 outside → `len(shown) == 6`, `len(outside) == 8`.
  - `test_changes_pp_units`: frac 0.066 → 0.484 gives `change_1q_pp == pytest.approx(41.8)`; pct `equity_to_assets` 7.2 → 8.4 gives `+1.2`; ytd ratio has `change_1q_pp is None`; missing prior quarter → `None`.
  - `test_direction_cutoffs`: 0.05 → up, 0.0499 → little effect, -0.05 → down.
  - `test_rank_phrase`: (56.0, 26.8) → "the model rated it safer than a year earlier"; (50.0, 50.9) → about the same; (60.0, 50.0) → riskier.
  - `test_log_total_assets_excluded`.

- [ ] **Step 2: Run** `.venv.nosync/bin/python -m pytest tests/test_analyst_trends.py -v` — expect FAIL (module not found).

- [ ] **Step 3: Implement `trends.py`** per the interfaces and Global Constraints. Window quarters come from calendar quarter-ends (`pd.Timestamp(as_of) - pd.offsets.QuarterEnd(k)` for k=1..12; for ytd, `pd.Timestamp(as_of) - pd.DateOffset(years=y)` for y=1..3, then snapped to quarter end).

- [ ] **Step 4: Run** the test file — expect PASS.

- [ ] **Step 5: Write the real-data checks** in `tests/data_checks/test_trends_real.py`, marked like `test_raw_files.py` (`pytest.mark.data`, skip if `data/features/fct_bank_features.parquet` is absent). They read SVB (cert 24735) rows from the parquet and call `compute_trends(history, as_of, {})`:
  - `test_svb_2022q1_htm_outside`: at 2022-03-31, `htm_unrealized_loss_to_equity` is in `outside` with `value ≈ 0.4836`, `lo ≈ -0.1172`, `hi ≈ 0.0659`, `change_1q_pp ≈ 41.8`, `change_4q_pp ≈ 48.6` (abs 0.1).
  - `test_svb_2022q4_htm_inside`: at 2022-12-31 it is **not** in `outside` (value ≈ 0.9808 within ≈ -0.1172..1.0526). Docstring: pins the known consequence in spec §1; do not change the rule to make this pass differently.

- [ ] **Step 6: Run** `.venv.nosync/bin/python -m pytest tests/data_checks/test_trends_real.py -v` — expect 2 PASS (locally, where data exists).

- [ ] **Step 7: Commit** `git add src/canary/analyst/trends.py tests/test_analyst_trends.py tests/data_checks/test_trends_real.py && git commit -m "Phase 5b: ratio trend core (fixed range rule) and SVB data checks"`

---

### Task 2: Registry hooks: code-only sections and code-rendered section bodies

**Files:**
- Modify: `src/canary/analyst/sections.py` (Section, new `sections_for`)
- Modify: `src/canary/analyst/facts.py` (`Fact`, `FactSheet` fields)
- Modify: `src/canary/analyst/render.py` (`render_note`)
- Modify: `src/canary/analyst/writer.py` (`write_memo` uses `sections_for`)
- Modify: `src/canary/analyst/showcase.py:211` (`build_request(sheet, sections_for(sheet), model)`)
- Modify tests: `tests/test_analyst_facts.py::test_section_order_and_specialists`, memo helpers in `tests/test_analyst_writer.py` (`_memo`) and `tests/test_analyst_showcase.py` (`_good`)
- Test: `tests/test_analyst_sections.py` (new)

**Interfaces:**
- Produces:
  - `Section` gains `render: Callable[[FactSheet], list[str]] | None = None` (last field, default None). Lines it returns are appended after the section's AI paragraphs.
  - `Fact` gains `feature: str | None = None` and `kind: str | None = None` (last fields, defaults None). Existing positional construction keeps working.
  - `FactSheet` gains `code_only: set[str] = field(default_factory=set)` and `extras: dict = field(default_factory=dict)` (defaults; last fields).
  - `sections.sections_for(sheet) -> list[Section]`: `all_sections(sheet.outcome.kind)` with `ai_written=False` for keys in `sheet.code_only`.
- Consumes: nothing from Task 1.

- [ ] **Step 1: Write failing tests** in `tests/test_analyst_sections.py`, using a dummy specialist registered with save/restore of `sections.SPECIALISTS` (fixture that copies the list and restores it after):
  - `test_sections_for_code_only`: a sheet whose `code_only == {"x"}` gives section "x" with `ai_written is False`; others unchanged.
  - `test_code_only_section_not_requested`: with the fake client, `write_memo` on `analyst_ctx` cert 3 where the dummy specialist sets `sheet.code_only.add("x")` in `build_facts`: the request schema enum has no "x", and the checker doesn't report "missing section 'x'".
  - `test_render_hook_output_in_note`: the dummy section's `render` returns `["RENDERED LINE"]`; it appears under `## X` after any AI paragraphs, and before the next section heading.

- [ ] **Step 2: Fix existing tests** so registering a specialist globally can't break them: `test_section_order_and_specialists` restores the saved list instead of `SPECIALISTS.clear()` and compares against the registry's 5a keys plus whatever is registered; `_memo` (writer tests) and `_good` (showcase tests) iterate `sections_for(sheet)` instead of `all_sections(sheet.outcome.kind)`.

- [ ] **Step 3: Run** `.venv.nosync/bin/python -m pytest tests/test_analyst_sections.py -v` — expect FAIL.

- [ ] **Step 4: Implement** the fields and `sections_for`; switch `write_memo` and showcase line 211 to `sections_for(sheet)`; in `render_note`, after a section's paragraphs, `out += sec.render(sheet) + [""]` when `sec.render` is set.

- [ ] **Step 5: Run** the full suite — expect 400 + new tests passing.

- [ ] **Step 6: Commit** `"Analyst registry: code-only sections per sheet and code-rendered section bodies"`

---

### Task 3: Trend specialist: facts, section, table, registration

**Files:**
- Modify: `src/canary/analyst/trends.py` (add specialist)
- Modify: `src/canary/analyst/writer.py` (import registers the specialist; one line in `_user_message`)
- Test: `tests/test_analyst_trends_facts.py`

**Interfaces:**
- Consumes: Task 1 `compute_trends`, `rank_phrase`, `TrendResult`; Task 2 `Fact.feature/kind`, `FactSheet.code_only/extras`, `Section.render`; `canary.replay.probe.contribution_matrix(ctx.model, rows)`; `canary.analyst.labels.display_forms`, `PLAIN_NAMES`, `UNIT`; `canary.analyst.facts.Fact`, `date_forms`.
- Produces:
  - `TREND_KEY = "trends"`, `TREND_SENTENCE` (exact copy from Global Constraints), `TREND_SECTION: Section` with `render=render_trends`.
  - `class TrendSpecialist` with `key = TREND_KEY`, `sections = [TREND_SECTION]`, `build_facts(self, ctx, sheet) -> list[Fact]`; stores the `TrendResult` in `sheet.extras["trends"]` and adds `TREND_KEY` to `sheet.code_only` when `shown` is empty.
  - `render_trends(sheet) -> list[str]`.
  - Fact `kind` values: `"trend_value"`, `"trend_lo"`, `"trend_hi"`, `"trend_change_1q"`, `"trend_change_4q"`, `"trend_contribution"`, `"trend_direction"` (each with `feature` set), plus sheet-level `"trend_count_outside"`, `"trend_count_checked"`, `"trend_window_pit"`, `"trend_window_ytd"`, `"trend_prior_percentile"`, `"trend_rank_phrase"` (`feature=None`).
  - `writer.py`: `import canary.analyst.trends` registers `TrendSpecialist()` once (guard against double registration by key).

Fact forms (all `hindsight=False`; value and change facts carry `quarter=as_of`; `lo`/`hi` carry `quarter=None`):
- value, lo, hi: `display_forms(feature, v)`.
- changes: display `f"{d:+.1f} pp"`; forms `[f"{d:+.1f}", f"{abs(d):.1f}", f"{d:+.0f}", f"{abs(d):.0f}"]` — **no `%` form**, so a change written as a level ("41.8%") fails the checker.
- contribution: same forms as 5a drivers (`f"{c:+.3f}"`, `f"{abs(c):.3f}"`, `f"{abs(c):.2f}"`, plus `f"{c:+.2f}"`).
- direction and rank phrase: text facts, `forms=[]`.
- windows: labels "Comparison window for most ratios: the prior 12 quarters (at least 8 with a value)" (forms `["12", "8"]`) and "Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value)" (forms `["3", "2"]`).
- prior percentile: label "Percentile a year earlier (100 = highest risk)", same forms as 5a's percentile fact, `quarter` = year-earlier quarter.

Section instructions (`TREND_SECTION.instructions`) carry §6.4: use only the trend facts and the as-of rank facts; for each ratio discussed give value, prior range and the model's contribution for **that same ratio** with its direction label; state the rank phrase; where a ratio is outside its range but its direction is "pushed the score down" or "little effect on the score", say the contrast plainly; never say a trend predicted, warned of or would have caught anything; don't mention the outcome; contributions are in "model log-odds units" (positive pushes the score up); changes are written with "percentage points" or "pp", never "%". `_user_message` gains: "Code adds the ratio table and the fixed sentence after your trends section."

Table (`render_trends`), when `shown` is non-empty: header `| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |`; window text "prior 12 quarters" / "same quarter, prior 3 years"; missing change → "n/a"; then a line "{len(outside)} of {checked} ratios were outside their prior range; the {len(shown)} furthest are shown." only when `len(outside) > len(shown)`. Then `TREND_SENTENCE`. Empty `shown` → the none-outside line (or too-little line when `checked == 0`), then `TREND_SENTENCE`.

- [ ] **Step 1: Write failing tests** in `tests/test_analyst_trends_facts.py` (use `analyst_ctx`; the synthetic features are random normals, so most banks have ratios outside range; to force cases, monkeypatch `trends.compute_trends` to return a hand-built `TrendResult`):
  - `test_trend_facts_paired_by_feature`: for each shown ratio there is exactly one fact of each per-ratio kind with that `feature`.
  - `test_contribution_matches_drivers`: a trend contribution fact equals `contribution_matrix(ctx.model, row)` for that feature (same numbers 5a's drivers use).
  - `test_change_forms_have_no_percent`: change facts' forms contain no "%"; frac change 0.418 displays "+41.8 pp"; pct change 1.2 displays "+1.2 pp".
  - `test_negative_forms`: value -0.1172 has form "-11.7%"; change -41.8 has "-41.8".
  - `test_no_nan_in_trend_facts`.
  - `test_no_year_earlier_score`: as-of 2016-03-31 → no `trend_prior_percentile` or `trend_rank_phrase` facts; section still in `sections_for(sheet)`.
  - `test_none_outside_is_code_only`: forced empty `outside` with `checked > 0` → `TREND_KEY in sheet.code_only`; `render_trends` returns the none-outside line and `TREND_SENTENCE`.
  - `test_too_little_history_line`: forced `checked == 0`.
  - `test_table_rendered_and_section_position`: a full `write_memo` with the fake client → note has `## How its ratios moved` after `## Score history` and before the outcome section, the table header, and `TREND_SENTENCE` exactly once.
  - `test_registered_once`: importing `canary.analyst.writer` twice leaves one `TrendSpecialist` in `SPECIALISTS`.

- [ ] **Step 2: Run** the file — expect FAIL.

- [ ] **Step 3: Implement** `TrendSpecialist`, `TREND_SECTION`, `render_trends`, the registration import and the `_user_message` line. History for the bank comes from `ctx.features` (all years); contributions from `contribution_matrix(ctx.model, at)` where `at` is the bank's `ctx.scored` row at as-of (as in `facts._drivers`); year-earlier percentile from `ctx.scored`.

- [ ] **Step 4: Run** the full suite — expect all passing.

- [ ] **Step 5: Commit** `"Phase 5b: trend specialist (facts, section, code-rendered table)"`

---

### Task 4: Checker rules for the trend section

**Files:**
- Modify: `src/canary/analyst/checker.py` (`_check_sentence`, module docstring)
- Test: `tests/test_analyst_checker_trends.py`

**Interfaces:**
- Consumes: Task 3 fact `kind`/`feature`, `TREND_KEY`, direction strings from Task 1.
- Produces: `checker.PREDICTION_PHRASES: re.Pattern`, `checker.OPPOSITE_DIRECTION: dict[str, re.Pattern]`; new errors only for sentences in section `TREND_KEY`.

Rules (§6.5), applied only when `key == TREND_KEY`:
1. **Pairing:** a sentence citing a `trend_contribution` fact must cite at least one `trend_value`/`trend_lo`/`trend_hi` fact with the same `feature`, and every cited per-ratio trend fact's `feature` must be one of the contribution facts' features. Error: `"pairs a contribution with a different ratio's figures"`.
2. **Direction words:** for each cited `trend_direction` or `trend_contribution` fact, the text must not match the opposite pattern: label "pushed the score down" or "little effect on the score" → reject `\b(pushed|raised|lifted|increased)\s+(the\s+)?(risk\s+)?score\s+up\b|\braised the score\b`; label "pushed the score up" → reject `\b(pushed|pulled|lowered)\s+(the\s+)?score\s+down\b|\btoward safe\b|\blowered the score\b`. Error names the code label.
3. **No prediction language:** case-insensitive `\bpredict\w*|\bforecast\w*|\bwarn(ed|ing|s)?\b|\bearly[- ]warning\b|\bwould have (caught|flagged|warned)\b|\bshould have (caught|flagged|been flagged)\b|\bforeshadow\w*|\bsign(al)?s? of (coming |impending )?failure\b`. Error: `"uses prediction language"`.
These are added to the normal error list, so the existing single retry carries them.

- [ ] **Step 1: Write failing tests** with hand-built `Fact`s (pattern of `tests/test_analyst_checker.py::_fact`) for HTM and AFS value/lo/hi/contribution/direction facts:
  - `test_contrast_sentence_passes`: "Losses on bonds held to maturity rose to 48.4% of equity, far above the prior range of -11.7% to 6.6%, yet the model's contribution for that ratio was -0.164, little effect on the score." citing HTM value, lo, hi, contribution, direction → no errors.
  - `test_htm_value_with_afs_contribution_rejected`.
  - `test_opposite_direction_rejected`: HTM direction "pushed the score down" and text "...which pushed the score up" → error.
  - `test_prediction_phrases_rejected` (parametrized over "predicted", "an early warning", "would have caught", "should have flagged", "a sign of failure").
  - `test_change_as_percent_rejected`: "rose 41.8% in one quarter" citing the change fact → number error.
  - `test_unicode_minus_ok`: "−11.7%" passes against the lo fact.
  - `test_rules_only_in_trend_section`: "predicted" in the summary section isn't flagged by rule 3.

- [ ] **Step 2: Run** — expect FAIL.

- [ ] **Step 3: Implement** the three rules in `_check_sentence` and update the module docstring.

- [ ] **Step 4: Run** the full suite — expect all passing.

- [ ] **Step 5: Commit** `"Analyst checker: trend pairing, direction and no-prediction rules"`

---

### Task 5: Docs and a live single-memo check

**Files:**
- Create: `decisions/0019-ratio-trends-descriptive.md`
- Modify: `data-dictionary/bank_notes.md`, `runbooks/analyst.md`, `reference/GLOSSARY.md` (prior range, percentage point, log-odds contribution if missing), `README.md` (Phase 5 line: 5b done, descriptive only), `RESULTS.md` (one short note: the trend section is descriptive and has no measured result), `canary-roadmap.md` (5b to Done after Task 6), `specs/2026-11-18-phase5b-trend-design.md` (status line)

- [ ] **Step 1: Write decision 0019**: descriptive only and why (threshold set after seeing SVB would be a worse hindsight problem than Phase 4 avoided); the fixed rule with every value from Global Constraints; the no-tuning rule; the SVB consequence (inside its range at 2022-12-31, seen during spec review and kept); the three checker rules and what they can't catch (paraphrased direction words, implied prediction without banned words); the possible post-launch measured version (rule set on 2001-2015 only, tested once on 2016-2024).

- [ ] **Step 2: Data dictionary and runbook**: section, table columns, fact kinds, fixed sentence and lines; runbook note that every memo now includes the section.

- [ ] **Step 3: Live single memo** (costs a few cents; normal API): `.venv.nosync/bin/python -m canary.analyst memo --cert 24735 --as-of 2022-03-31 --out data/analyst/trend_check` (gitignored folder, so the committed SVB note is untouched). Expected: checker passes; the note's trends section lists HTM loss to equity with 48.4%, -11.7% to 6.6%, +41.8 pp and its contribution, and states the contrast. Read it; do not commit a note for an as-of that differs from SVB's showcase as-of.

- [ ] **Step 4: Run** the full suite; **commit** docs `"Phase 5b docs: decision 0019, dictionary, runbook, glossary, README/RESULTS"`

---

### Task 6: Showcase re-run (needs Victor's cost approval)

- [ ] **Step 1: Dry run** `.venv.nosync/bin/python -m canary.analyst showcase --watchlist-top 20 --dry-run` and report the estimate to Victor. **Stop until Victor approves the cost.**
- [ ] **Step 2: Run** the showcase (batch) with the same set as 5a (61 banks). Expected: run report with written / failed counts; any failures retried per 5a's path.
- [ ] **Step 3: Read** SVB, Signature, First Republic and three random notes' trends sections; confirm SVB's note does not list HTM (expected, §1) and no note claims prediction.
- [ ] **Step 4: Update** README/RESULTS counts and cost, `canary-roadmap.md` (5b → Done), `daily-log.md`; full suite; **commit** `"Phase 5b: showcase notes with ratio trends"`.
