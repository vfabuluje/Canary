# Phase 6 Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A public, read-only Streamlit dashboard for Canary in the approved v6 pixel style, with search, the 2023 replay, the watchlist slider, the animated report replay and report page, Why Canary, and a capped Ask Canary box; plus the code (not the paid run) to expand the showcase to 100 banks.

**Architecture:** `python -m canary.dashboard export` reads the local pipeline data once and writes small committed files to `dashboard/data/`. The Streamlit app (`dashboard/app.py` + `dashboard/views/`) reads only those files. Pure logic (export, cards, search, ask guards) lives in `src/canary/dashboard/` and is unit-tested; the pixel replay and report screens are the v6 engine, made data-driven, rendered with `st.components.v1.html`.

**Tech Stack:** Python 3.12, pandas, Streamlit ≥ 1.46 (`st.navigation(position="top")`, `st.popover`, `AppTest`), Altair 5, rapidfuzz 3, anthropic 1.17 (Ask Canary only), existing `canary.analyst` / `canary.model` code.

**Spec:** `specs/2026-11-19-phase6-dashboard-design.md` (approved 2026-11-20). Visual reference: `dashboard/design/report-replay-v6.html` and the approved mockup `.superpowers/brainstorm/canary-dashboard-v6style.html` (local, gitignored; copy it to `dashboard/design/dashboard-mockup.html` in Task 5).

## Global Constraints

- No Claude call anywhere except `canary.dashboard.ask`; the app must run fully with Ask switched off or no API key. Only `src/canary/dashboard/ask.py` imports `anthropic`.
- The app reads only `dashboard/data/` (path overridable by env `CANARY_DASHBOARD_DATA` for tests); never `data/`.
- No hand-typed figures in the app except the fixed copy in `src/canary/dashboard/copy.py`, which a test checks against the data.
- Never a dual-axis chart. Score charts: y 0–100, watchlist line at the 98th percentile.
- Watchlist sizes: 0.005, 0.01, 0.02 (published, "★ Canary uses this"), 0.03, 0.05, 0.075, 0.10. At 0.02 the export must reproduce `metrics.json`: 21 of 29, false-alarm rate 0.9828178694158075, 3,783 rows.
- Case-study certs and weak-spot columns: 24735 `htm_unrealized_loss_to_equity`, 57053 `afs_unrealized_loss_to_equity`, 59017 `uninsured_to_deposits` (shown ×100 as %).
- Themes: `standard` (bg `#d5d7db`, replay uses detective cast), `detective` (cork board `#b4875a`, red pixel pin on each card, nav `#1a1a1a`), `basketball` (court `#b97a45`, white court lines, nav `#1c4e80`, headings on the court white with navy shadow). Navy `#1e2240`, yellow `#ffe066`, "Press Start 2P" headings. Cards stay white.
- Tabs, in order: Home · Find a bank · 2023 · Watchlist · How it works · Why Canary; a 🎨 popover on the right with the three themes. Theme in `st.session_state["theme"]`, default `standard`.
- Home hero: "CANARY" + "Bank Failure Early-Warning System". The honest miss sits below the headline numbers, never at the top. "Research tool, not financial advice." on every page footer. No "a data project by a student" line.
- Replay: ~5.5 s per scene, 6 scenes in pipeline order (numbers; rule check; trend+peer together; check of trend/peer; lead writes then is checked in the same scene; done + hoop shot in basketball). "Sent back once, fixed" only when the trace shows attempt 2 for that agent. A bank with no peer section shows Peer on the bench: "not enough similar banks to compare".
- Search: rapidfuzz; open directly if top score ≥ 90 and ≥ 10 points ahead of the next; else "Did you mean" up to 8 with name, state, status. Aliases: "svb"→24735, "signature"→57053, "first republic"/"frb"→59017.
- Ask Canary: model `claude-haiku-5-5`; 5 questions per session; 300/day (process-wide counter, reset at UTC midnight); question ≤ 300 characters; key from `st.secrets["ANTHROPIC_API_KEY"]`; switch `st.secrets["ASK_ENABLED"]` (default off); answers must pass `check_memo`; one retry, then "I couldn't answer that with checked facts."; off/cap/error text "Ask Canary is resting for today."; nothing stored.
- Showcase expansion: group `big_bank` with the 20 certs in spec §5.8, then `--watchlist-top 39`; existing notes are never redone; `--max-cost 7.00`; the paid run is not part of this plan.
- **Phones (Victor):** it's a website, no app; every page works in a phone browser ≥ 360 px wide with no horizontal page scroll; columns and cards stack; the replay scales to the container width (scene scaled to fit) and the "Who's on now" panel moves under the scene below 700 px; every hover tip also opens on tap.
- Tests run with `.venv.nosync/bin/python -m pytest` (plain `pytest` can't import `tests.*`). No network in tests.

## Review Focus

1. **Search inputs that aren't clean names:** empty or whitespace-only, one letter, punctuation ("M&T", "First-Citizens"), lowercase, and two banks with the same name in one state. Expected: no crash; an empty query shows the hint; identical names are told apart by city and cert. Tests: Task 4.
2. **Ask Canary unavailable:** no key, `ASK_ENABLED` false, daily cap hit, session limit hit, API error, refusal, malformed JSON. Expected: the box shows the resting/limit text and the rest of the page renders. Tests: Task 10.
3. **Unusual showcase traces:** Comenity (57570) with no peer call; a bank whose analyst needed attempt 2; a bank whose trend agent needed attempt 2. Expected: slim trace and replay scenes match the trace exactly. Tests: Task 3.
4. **Banks outside the scored years:** a bank that stopped reporting before 2016 (never scored) and a bank whose latest score is after 2024-12-31. Expected: the "not scored" page; the "after the test period" label. Tests: Tasks 1 and 7.
5. **Missing concentration inputs:** a bank whose `ConcentrationResult` has `reason` set (test can't be applied). Expected: the rule card and score page say it can't be applied, never show 0%. Tests: Tasks 1 and 3.

---

## File structure

| Path | Responsibility |
|---|---|
| `src/canary/dashboard/__init__.py`, `__main__.py` | CLI: `python -m canary.dashboard export [--out dashboard/data]` |
| `src/canary/dashboard/tables.py` | banks, scores history, concentration, metrics, threshold exports |
| `src/canary/dashboard/cases.py` | case-study export (quarters, weak spot, top-3 signals, phase) |
| `src/canary/dashboard/cards.py` | report-card text from a trace: sentence picking, headline, hover text, glossary |
| `src/canary/dashboard/reports.py` | `reports/<cert>.json` per showcase bank (slim trace, cards, facts, note) |
| `src/canary/dashboard/copy.py` | fixed copy: case captions, Why Canary, home text, flagship cards for the 3 case-study banks, glossary |
| `src/canary/dashboard/search.py` | fuzzy search + aliases |
| `src/canary/dashboard/data.py` | cached loaders for `dashboard/data/` |
| `src/canary/dashboard/theme.py` | theme CSS, nav, footer helpers for Streamlit pages |
| `src/canary/dashboard/replay.py` + `web/replay.js`, `web/sprites.js`, `web/replay.css` | the v6 engine as a data-driven component |
| `src/canary/dashboard/ask.py` | Ask Canary (guards, request, check, retry) |
| `dashboard/app.py`, `dashboard/views/{home,find,cases,watchlist,how,why}.py` | Streamlit app |
| `dashboard/data/` | committed exports |
| `requirements.txt` (repo root), `.streamlit/config.toml` | Streamlit Community Cloud deploy |
| `src/canary/analyst/showcase.py`, `__main__.py` | `big_bank` group and `--skip-done` |
| `tests/test_dashboard_*.py`, `tests/dashboard_fixtures.py` | tests |

---

### Task 1: Package, dependencies and table exports

**Files:**
- Modify: `pyproject.toml` (add `dashboard = ["streamlit>=1.46,<2", "altair>=5,<6", "rapidfuzz>=3,<4"]`)
- Create: `src/canary/dashboard/__init__.py`, `src/canary/dashboard/__main__.py`, `src/canary/dashboard/tables.py`
- Test: `tests/test_dashboard_tables.py`

**Interfaces:**
- Consumes: `canary.analyst.context.load_context(...) -> Context`; `canary.model.metrics.flag_watchlist/bank_recall/false_alarm_rate`; `canary.analyst.concentration.compute_concentration(rows, as_of) -> ConcentrationResult`, `render_concentration(result) -> list[str]`.
- Produces:
  - `WATCHLIST_SHARES: tuple[float, ...] = (0.005, 0.01, 0.02, 0.03, 0.05, 0.075, 0.10)`
  - `export_banks(ctx, showcase_certs: set[int]) -> pd.DataFrame` columns `cert, name, state, city, first_report, last_report, failure_date, scored, latest_report_date, latest_rank, latest_n, latest_percentile, latest_flagged, after_test_period, has_report`
  - `export_scores_history(ctx) -> pd.DataFrame` columns `cert, report_date, rank, n_banks, percentile, flagged` (report_date ≥ 2016-03-31)
  - `export_concentration(ctx) -> pd.DataFrame` columns `cert, as_of, measure, construction_pct, cre_pct, growth_pct, reason, lines` (lines = `"\n".join(render_concentration(r))`), one row per scored bank at its latest scored quarter
  - `threshold_table(scores_test: pd.DataFrame) -> list[dict]` keys `share, caught, eligible, false_alarm, rows, caught_case_studies` (sorted list of the 3 case-study certs caught)
  - `write_tables(ctx, model_dir: Path, out: Path, showcase_certs: set[int]) -> None` writing `banks.parquet`, `scores_history.parquet`, `concentration.parquet`, `metrics.json` (keys `auc, recall, banks_caught, eligible_banks, lead_time_median, false_alarm_rate, rows_flagged, baseline`), `threshold.json`
  - CLI `python -m canary.dashboard export --out dashboard/data` (Tasks 2–3 add to it); prints each file's size and the folder total; exits 1 if the folder exceeds 50 MB.

- [ ] **Step 1: Install the dashboard extras:** `.venv.nosync/bin/pip install -e ".[dashboard]"` → `pip list` shows streamlit, altair, rapidfuzz.
- [ ] **Step 2: Write failing tests** in `tests/test_dashboard_tables.py` using the `features_path`, `failures_path`, `financials_dir` fixtures from `tests/conftest.py` to build a small `Context` (as the analyst tests do):
  - `test_threshold_published_share_matches_metrics`: on `data/model/scores_test.parquet` (mark `@pytest.mark.data`, skip if absent), the 0.02 row is `caught == 21`, `eligible == 29`, `rows == 3783`, `false_alarm == pytest.approx(0.9828178694158075)`; the 0.10 row has `caught_case_studies == [57053]`.
  - `test_threshold_shares_in_order`: `[r["share"] for r in table] == list(WATCHLIST_SHARES)`.
  - `test_banks_never_scored`: a bank whose last report is before 2016-03-31 has `scored == False` and null latest fields.
  - `test_banks_after_test_period`: a bank whose latest score is after 2024-12-31 has `after_test_period == True`.
  - `test_concentration_reason_kept`: a bank with missing capital fields has `reason` set and `cre_pct` null.
  - `test_export_cli_size_guard`: with `--out` pointing at a folder holding a 51 MB dummy file, the CLI exits 1.
- [ ] **Step 3: Run** `.venv.nosync/bin/python -m pytest tests/test_dashboard_tables.py -v` → FAIL (module missing).
- [ ] **Step 4: Implement** `tables.py` and the CLI. `has_report` = cert in `showcase_certs` (certs from `banks/*.md` front matter). Names title-cased as `build_fact_sheet` does.
- [ ] **Step 5: Run** the tests → PASS.
- [ ] **Step 6: Commit** `feat(dashboard): export tables and watchlist-size results`.

### Task 2: Case-study export and fixed copy

**Files:**
- Create: `src/canary/dashboard/cases.py`, `src/canary/dashboard/copy.py`
- Test: `tests/test_dashboard_cases.py`

**Interfaces:**
- Consumes: `data/model/case_studies.csv`; `ctx.features`; `canary.analyst.labels.PLAIN_NAMES`.
- Produces:
  - `WEAK_SPOT: dict[int, str]` (Global Constraints values)
  - `phase_of(report_date: date, last: date) -> Literal["before", "rising", "last"]` (`last` if equal to the bank's final quarter; `before` if year 2021; else `rising`)
  - `export_cases(ctx, case_csv: Path) -> dict[int, list[dict]]`, each quarter `{"q": "YYYY-MM-DD", "pct": float, "rank": int, "n": int, "weak": float, "signals": [[plain_name, value], …3], "phase": str}`; written to `case_studies.json` by the CLI.
  - `copy.py`: `CASE_CAPTIONS: dict[int, dict[str, str]]` with the nine captions verbatim from spec §5.3; `CASE_LABELS` (chip name, failure date text, status label: SVB/First Republic "FAILED · NOT FLAGGED", Signature "FAILED · NEAR MISS"); `WEAK_SPOT_TITLES` (as in the mockup); `HOME_WHAT`, `HONEST_MISS`, `WHY_SECTIONS` (the mockup's Why Canary text minus the student line).

- [ ] **Step 1: Failing tests:**
  - `test_case_quarter_counts`: 24735 and 57053 have 8 quarters; 59017 has 9 ending `"2023-03-31"`.
  - `test_svb_last_quarter`: 24735's last quarter `rank == 3494`, `n == 4773`, `weak == pytest.approx(98.1, abs=0.05)`, `phase == "last"`.
  - `test_phases`: quarters in 2021 are `before`; 2022 non-final are `rising`.
  - `test_captions_have_no_digits`: no character of any `CASE_CAPTIONS` value is a digit.
  - `test_case_signals_plain_names`: every signal name is a value of `PLAIN_NAMES`.
  - `test_honest_miss_matches_data`: no quarter of 24735, 57053 or 59017 in the export has `pct >= 98` (the fixed `HONEST_MISS` copy says none was flagged).
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5: Commit** `feat(dashboard): export the 2023 case studies and fixed copy`.

### Task 3: Report export (cards, slim trace, facts, flagship copy)

**Files:**
- Create: `src/canary/dashboard/cards.py`, `src/canary/dashboard/reports.py`
- Modify: `src/canary/dashboard/copy.py` (add `GLOSSARY`, `HEADLINES`, `FLAGSHIP_CARDS`)
- Test: `tests/test_dashboard_reports.py`

**Interfaces:**
- Consumes: traces `data/analyst/traces/<cert>_<as_of>.json` (`calls[]` with `agent` ∈ {trend, peer, analyst}, `attempt`, `response_text` (memo JSON), `checker_errors`); `build_fact_sheet(ctx, cert, as_of)`; `canary.analyst.pipeline.IDENTITY_LABELS`; the note markdown in `banks/`.
- Produces:
  - `slim_trace(trace: dict) -> dict`: `{"agents": {name: {"ran": bool, "attempts": int, "first_try": bool}}}` for trend, peer, analyst (an agent with no call has `ran: False`).
  - `pick_sentences(memo_section: dict, facts: dict[str, Fact], n: int = 2) -> list[dict]`: the first `n` sentences whose cites are not all `IDENTITY_LABELS` facts; each `{"text", "numbers": [{"text": token, "label", "quarter", "explain"}]}`, numbers from `canary.analyst.checker.extract_tokens` matched to a cited fact's forms; `explain` from `GLOSSARY[fact.feature]` when present else the fact label.
  - `headline(outcome_kind: str, name: str) -> str` from `HEADLINES` (keys `caught, missed, false_alarm, open_watchlist, quiet`; no digits).
  - `build_report(ctx, cert: int, as_of: date, trace: dict, note_md: str) -> dict` keys `cert, name, as_of, outcome, failure_date, rank, n_banks, percentile, flagged, headline, cards, agents, facts, note_md`. `cards` = list of `{"key": "trend"|"peer"|"rule"|"summary", "who": key, "badge": "AI"|"RULE", "sentences": [...]}`; trend from the last trend response's `trends`, peer from `peers` (omitted when peer didn't run), summary from the analyst's `summary`, rule from the code-rendered concentration lines. For the three case-study certs, `cards`' text comes from `FLAGSHIP_CARDS[cert]` instead.
  - `facts`: every Fact as a dict (`id, label, quarter, value, display, forms, hindsight, source, feature, kind`), used by Ask Canary.
  - `write_reports(ctx, notes_dir: Path, trace_dir: Path, out: Path) -> list[int]` writes `reports/<cert>.json` for every note whose trace exists.
- `FLAGSHIP_CARDS`: Claude writes the v6-quality wording for 24735, 57053, 59017, using only numbers in that bank's note; Victor approves it before the branch is merged (note in the task report).

- [ ] **Step 1: Failing tests** (fixtures: small hand-made trace dicts plus the real SVB trace marked `data`):
  - `test_slim_trace_retry`: a trace with analyst attempts 1 and 2 → `agents["analyst"] == {"ran": True, "attempts": 2, "first_try": False}`.
  - `test_slim_trace_no_peer`: a trace with no peer call → `agents["peer"]["ran"] is False`.
  - `test_pick_sentences_skips_rank_only`: for the real SVB trend section, no picked sentence contains "3,494".
  - `test_numbers_match_cited_facts`: every `numbers[].text` in every card appears in one of the sentence's cited facts' forms.
  - `test_flagship_numbers_in_note`: every number token (via `extract_tokens`) in `FLAGSHIP_CARDS[c]` appears in the note text for c.
  - `test_headlines_no_digits`.
  - `test_reports_written_for_every_note_with_trace` (data): 61 files under a tmp out dir.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5: Run the full export** `.venv.nosync/bin/python -m canary.dashboard export --out dashboard/data` → prints sizes, total < 25 MB; commit `dashboard/data/`.
- [ ] **Step 6: Commit** `feat(dashboard): export report pages and slim traces`.

### Task 4: Search

**Files:** Create `src/canary/dashboard/search.py`; Test `tests/test_dashboard_search.py`

**Interfaces:**
- Produces: `ALIASES: dict[str, int]`; `search(query: str, banks: pd.DataFrame, limit: int = 8) -> SearchResult` where `SearchResult(direct: int | None, suggestions: list[dict])`, each suggestion `{"cert", "name", "state", "status", "label"}`; `status` = "Active" / "Failed <Mon D, YYYY>" / "Stopped reporting <YYYY>"; `label` = name, plus " — <city>, cert <n>" when another suggestion has the same name and state.

- [ ] **Step 1: Failing tests:** `test_alias_svb_direct` (`"SVB"` → direct 24735); `test_alias_case_insensitive` (`"  frb "` → 59017); `test_empty_query` (`""` and `"   "` → no direct, no suggestions); `test_one_letter` (no exception, ≤ 8 suggestions); `test_punctuation` (`"M&T"` finds "Manufacturers&Traders Tr Co" in a fixture frame); `test_same_name_disambiguated` (two "First National Bank" in one state → both labels include city and cert); `test_direct_needs_clear_win` (two names scoring within 10 → no direct).
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement** with `rapidfuzz.process.extract(..., scorer=fuzz.WRatio)` on lower-cased names. **Step 4: Run** → PASS.
- [ ] **Step 5: Commit** `feat(dashboard): fuzzy bank search with aliases`.

### Task 5: App shell, themes, Home and Why Canary

**Files:**
- Create: `src/canary/dashboard/data.py`, `src/canary/dashboard/theme.py`, `dashboard/app.py`, `dashboard/views/home.py`, `dashboard/views/why.py`, `tests/dashboard_fixtures.py`, `.streamlit/config.toml`
- Copy: mockup → `dashboard/design/dashboard-mockup.html`
- Test: `tests/test_dashboard_app.py`

**Interfaces:**
- `data.py`: `data_dir() -> Path` (env `CANARY_DASHBOARD_DATA` else `<repo>/dashboard/data`); `@st.cache_data` loaders `banks()`, `scores_history()`, `concentration()`, `metrics()`, `threshold()`, `cases()`, `report(cert: int) -> dict | None`, `report_certs() -> list[int]`.
- `theme.py`: `THEMES = ("standard", "detective", "basketball")`; `current_theme() -> str`; `apply_theme() -> None` (injects the theme CSS from Global Constraints); `theme_picker() -> None` (the 🎨 `st.popover`); `footer() -> None`.
- `app.py`: `st.navigation([...6 pages...], position="top")` in the Global Constraints order; calls `apply_theme()` and `theme_picker()`.
- `tests/dashboard_fixtures.py`: `write_fixture_data(root: Path) -> Path` builds a tiny valid `dashboard/data` (5 banks incl. one never scored, one report for 24735, case studies, threshold, metrics).

- [ ] **Step 1: Failing tests** (`AppTest.from_file("dashboard/views/home.py")` with `CANARY_DASHBOARD_DATA` set to fixture data):
  - `test_home_hero`: page markdown contains "CANARY" and "Bank Failure Early-Warning System"; the honest-miss text appears after the four headline numbers.
  - `test_home_numbers_from_metrics`: changing fixture `metrics.json` `banks_caught` to 7 shows "7" in the first number card.
  - `test_why_has_no_student_line`: why page text lacks "student".
  - `test_theme_css_switches`: setting `session_state["theme"] = "basketball"` injects `#b97a45`; `"detective"` injects `#b4875a`.
  - `test_app_never_reads_data_dir`: grep of `dashboard/` and `src/canary/dashboard/` (excluding `__main__.py`, `tables.py`, `cases.py`, `reports.py`) finds no `"data/"` path literal.
  - `test_only_ask_imports_anthropic`: only `src/canary/dashboard/ask.py` contains `import anthropic`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement**, matching the mockup's look (hero, pixel canary drawn by a small inline canvas component, cards). **Step 4: Run** → PASS.
- [ ] **Step 5: Look at it:** `.venv.nosync/bin/streamlit run dashboard/app.py`, screenshot Home in all three themes at desktop width and at 390 px; compare with the mockup; no horizontal scroll on the phone width.
- [ ] **Step 6: Commit** `feat(dashboard): app shell, themes, Home and Why Canary`.

### Task 6: 2023 and Watchlist pages

**Files:** Create `dashboard/views/cases.py`, `dashboard/views/watchlist.py`, `src/canary/dashboard/charts.py`; Test `tests/test_dashboard_charts.py`

**Interfaces:**
- `charts.py`: `score_chart(rows: list[dict], selected: int) -> alt.Chart` (y 0–100, rule at 98 labeled WATCHLIST, square points, tooltip quarter/percentile/rank); `weak_chart(rows, selected, title) -> alt.Chart`; `threshold_chart(table, selected) -> alt.Chart`. Each a single y-axis.
- Pages: chips (`st.segmented_control`) for the three banks, `st.select_slider` over quarters (default last), click-to-select via `st.altair_chart(..., on_select="rerun")`; side card (rank of N, percentile, weak value, watchlist yes/no, top-3 bars, caption from `CASE_CAPTIONS[cert][phase]`). Watchlist: the seven sizes as a segmented control, three number cards, chart, sentence naming Signature when `57053 in caught_case_studies`.

- [ ] **Step 1: Failing tests:** `test_charts_single_axis` (no chart spec has `resolve.scale.y == "independent"` and each has one y encoding); `test_score_chart_rule_at_98`; `test_cases_page_default_last_quarter` (AppTest: SVB side card shows "#3,494"); `test_cases_first_republic_nine_quarters`; `test_watchlist_page_published_default` (shows "21" and "of 29"); `test_watchlist_ten_percent_names_signature`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS; screenshot both pages in basketball theme.
- [ ] **Step 5: Commit** `feat(dashboard): 2023 replay and watchlist size pages`.

### Task 7: Find a bank and bank pages

**Files:** Create `dashboard/views/find.py`, `src/canary/dashboard/bankpage.py`; Test `tests/test_dashboard_find.py`

**Interfaces:**
- `bankpage.py`: `page_kind(bank: pd.Series) -> Literal["report", "scored", "unscored"]`; `render_bank(cert: int) -> None`.
  - report → the replay component (Task 8) for that cert, then "Read the full report" (`st.expander` with `note_md`), then Ask Canary (Task 10).
  - scored → "No written report for this bank", latest rank of N with quarter (plus "after the test period" when set), rank-history Altair line, concentration `lines` (or its reason).
  - unscored → spec §5.2 text with the last report year.
- `find.py`: text input (prefilled from `st.query_params["q"]`), suggestions as buttons; selecting sets `st.query_params["cert"]`; `?cert=N` opens that bank directly. Home search submits to this page.

- [ ] **Step 1: Failing tests:** `test_unscored_page_text` (fixture pre-2016 bank shows "Canary only scores banks from 2016 on"); `test_scored_page_no_report_label`; `test_after_test_period_label`; `test_svb_query_opens_report_page`; `test_bad_cert_param` (`?cert=abc` and an unknown cert show "No bank found" without error).
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5: Commit** `feat(dashboard): find a bank and bank pages`.

### Task 8: Replay component, report screen and How it works

**Files:** Create `src/canary/dashboard/replay.py`, `src/canary/dashboard/web/replay.js`, `web/sprites.js`, `web/replay.css`, `dashboard/views/how.py`; Test `tests/test_dashboard_replay.py`

**Interfaces:**
- `replay.py`: `scenes(report: dict) -> list[dict]` (6 scenes; each `{"key", "now", "who": {"detective": str, "basketball": str}, "active": [member ids], "note": str | None}`; scene 4 `note` lists Trend/Peer retries; scene 5 note for the lead's retry; scene 3 marks Peer benched when `agents.peer.ran` is False); `replay_html(report: dict, theme: str) -> str` (inlines `web/*` and a JSON payload; `standard` uses the detective cast and grey bg); `render_replay(report, theme, height=900) -> None`.
- `web/*`: the v6 engine (sprites, players, referee stripes, Replay Review, side panel, captions, progress, skip link, hoop shot, report screen with headline/cards/hover tips and "Watch how it was made") reading `window.CANARY` instead of hard-coded SVB text.
- `how.py`: a bank picker over `report_certs()` (default 24735), the replay, then the four-step strip (public FDIC data · CODE → model ranks every bank · CODE → AI team writes reports · AI → every number checked · CODE).

- [ ] **Step 1: Failing tests:** `test_replay_html_scales_and_stacks` (the HTML has a resize handler that scales the scene to its container and a `max-width:700px` rule that stacks the side panel); `test_tips_open_on_tap` (tip targets handle `click` as well as `mouseover`); `test_six_scenes_in_order` (keys `numbers, rule, specialists, check, lead, done`); `test_peer_benched_when_no_peer`; `test_retry_notes_only_when_retried` (first-try trace → no note; analyst attempt 2 → scene 5 note "sent back once, fixed"); `test_html_has_no_svb_literal_for_other_bank` (replay_html for a fixture bank 91 doesn't contain "Silicon Valley"); `test_standard_theme_uses_detectives`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement**, porting from `dashboard/design/report-replay-v6.html`. **Step 4: Run** → PASS.
- [ ] **Step 5: Look at it:** run the app; watch SVB in all three themes and Comenity (57570), at desktop width and at 390 px; check the hoop shot, the bench, tap tips on the phone width; console has no errors.
- [ ] **Step 6: Commit** `feat(dashboard): data-driven report replay and How it works`.

### Task 9: Docs and deploy files

**Files:** Create `requirements.txt` (`.[dashboard,model,analyst]`), `decisions/0023-dashboard.md`, `data-dictionary/dashboard-exports.md`, `runbooks/dashboard.md` (export, run locally, deploy on Streamlit Community Cloud, set secrets, turn Ask on/off); Modify `README.md` (dashboard section, live-app link placeholder `<!-- LIVE_APP_URL -->`), `canary-roadmap.md`.

- [ ] **Step 1:** Add `test_data_dictionary_covers_exports` to `tests/test_dashboard_tables.py`: every file and column written by the export appears in `data-dictionary/dashboard-exports.md`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Write the docs.** **Step 4: Run** → PASS.
- [ ] **Step 5: Commit** `docs: Phase 6 dashboard decision, data dictionary, runbook`.

### Task 10: Ask Canary

**Files:** Create `src/canary/dashboard/ask.py`, `src/canary/dashboard/askbox.py`; Test `tests/test_dashboard_ask.py`

**Interfaces:**
- `ask.py`:
  - `ASK_MODEL = "claude-haiku-5-5"`, `SESSION_LIMIT = 5`, `DAILY_LIMIT = 300`, `MAX_CHARS = 300`
  - `ANSWER_SECTION = Section("answer", "Answer", "hindsight", "...", True)`
  - `class DailyCounter` (thread-safe; `take(today: date) -> bool`, resets on a new UTC date)
  - `build_request(report: dict, question: str, errors: list[str] | None = None) -> dict` (system prompt: answer in plain English from this bank's facts only, cite fact ids per sentence, say "I can't tell from this bank's data" otherwise; user message = fact table + note; structured output schema `{"sections": [{"key": "answer", "paragraphs": [{"sentences": [{"text", "cites"}]}]}]}`; `max_tokens` 2000; `output_config={"effort": "low"}`)
  - `answer(report: dict, question: str, client) -> AskResult` (`AskResult(ok: bool, text: str, cost_usd: float)`): one call, `check_memo` against the report's facts; on errors one retry with the errors; then fail with "I couldn't answer that with checked facts."; refusal, API error or bad JSON → `ok=False`, `RESTING`.
  - `RESTING = "Ask Canary is resting for today."`
- `askbox.py`: `render_askbox(report: dict) -> None`: hidden unless `st.secrets.get("ASK_ENABLED")` is true and a key exists (then shows RESTING); enforces `MAX_CHARS`, `SESSION_LIMIT` (in `session_state`) and a module-level `DailyCounter`; shows the note "Answers are written by AI from this bank's public data, fact-checked, and not financial advice."

- [ ] **Step 1: Failing tests** (use `tests/analyst_fakes.FakeClient` and `fake_message`):
  - `test_good_answer_passes` (cited number matches a fact → `ok`, one call)
  - `test_bad_number_retries_once_then_fails` (two bad answers → `ok False`, text "I couldn't answer that with checked facts.", exactly 2 calls)
  - `test_refusal_is_resting`, `test_api_error_is_resting`, `test_bad_json_is_resting`
  - `test_daily_counter_resets_next_day`, `test_daily_counter_stops_at_limit`
  - `test_request_uses_haiku_and_low_effort`
  - `test_askbox_hidden_without_key` and `test_askbox_session_limit` (AppTest with secrets)
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5: No paid call.** A real smoke test (a few cents) happens only with Victor's go-ahead, after the merge.
- [ ] **Step 6: Commit** `feat(dashboard): Ask Canary with Haiku, caps and fact-checking`.

### Task 11: Showcase expansion code (no paid run)

**Files:** Modify `src/canary/analyst/showcase.py`, `src/canary/analyst/__main__.py`; Test `tests/test_analyst_showcase.py`

**Interfaces:**
- `BIG_BANK_CERTS: tuple[int, ...] = (628, 3510, 7213, 3511, 33124, 6548, 4297, 6384, 9846, 639, 32992, 14, 18409, 6672, 6560, 16571, 57450, 11063, 57957, 588)`
- `showcase_banks(...)` adds group `"big_bank"` (as of `ctx.latest_quarter`) after `after_window` and before `latest_watchlist`.
- `--skip-done`: drop banks whose trace `data/analyst/traces/<cert>_<as_of>.json` exists with `ok: true` before the dry-run estimate and before any batch.

- [ ] **Step 1: Failing tests:** `test_big_bank_group_order`; `test_big_bank_claims_before_watchlist` (a flagged big bank isn't double-counted and watchlist still takes N others); `test_skip_done_drops_finished` (dry run lists only banks without a passing trace); `test_skip_done_estimate_only_new`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5: Dry run (free):** `.venv.nosync/bin/python -m canary.analyst showcase --dry-run --watchlist-top 39 --skip-done --max-cost 7.00` → lists 39 banks (20 big, 19 watchlist) and an estimate. Save the output for Victor; **do not run without `--dry-run`.**
- [ ] **Step 6: Commit** `feat(analyst): big-bank showcase group and --skip-done`.

### Task 12: Whole-app check

- [ ] **Step 1:** `.venv.nosync/bin/python -m pytest -q` → all pass.
- [ ] **Step 2:** `streamlit run dashboard/app.py`; click every tab in all three themes on a desktop width and a 390 px width; search "svb", "indymac", "m&t"; open Comenity; check the console has no errors. Fix anything found in the owning task's files and commit `fix(dashboard): …`.
- [ ] **Step 3:** Update `daily-log.md`.
