# Phase 5a Spec: Risk Analyst (memo writer + on-request agent)

**Date:** 2026-11-17
**Status:** Approved by Victor 2026-11-17 (builder check done)
**Phase:** 5a of 5 (see `CLAUDE.md`). Phase 5 is split into four agents built one at a time:
5a risk analyst (this spec) → 5b trend/watchlist → 5c peer comparison → 5d concentration risk.

## 1. Intent: why this exists

Phases 3-4 produce numbers: a score, a rank and a watchlist flag for every bank-quarter, plus the reasons the model caught or missed specific failures. A number alone doesn't tell a reader *why* a bank looks risky. Phase 5a adds an AI risk analyst: Claude turns one bank's figures into a short memo in plain English, saved as an Obsidian note, where **every figure is cited and checked by code**.

Readers are a recruiter or interviewer skimming the repo, and Victor explaining it. A good memo
lets them see in one page what the bank looked like, what the model said, why, and (for banks that failed) how that call held up. It also keeps the project's discipline: a memo is written "as of" a quarter and uses no data from after that date, except in one clearly labeled hindsight section.

Phase 5a is also the base the other three agents plug into (§7).

## 2. Goals
- G1. **One memo writer.** Given `(cert, as_of)`, code builds a fact sheet, Claude writes the memo from it in one call, code checks every number, and the note is saved to `banks/`.
- G2. **Showcase run.** One command writes notes for the showcase set (§5.1), about 130 banks.
- G3. **On-request agent.** A plain-English command (`ask "..."`) where Claude chooses among four tools (§6) to find a bank, answer quick questions, or write a memo by calling G1.
- G4. **Explain the score** in every memo: rank and percentile, watchlist status, top drivers up and down (XGBoost contributions, as in Phase 4), and what the model can't see (§5.4).
- G5. **Outcome-aware section** (§5.3): caught / missed / false alarm / quiet.
- G6. **Citation checker** (§5.5) that refuses to save a memo with an unsupported number.
- G7. Tests for all non-AI code with no network; the AI calls are mocked in tests.
- G8. Docs: decision records, data dictionary for the note format, runbook, README and
  `reference/STACK.md` updated.

## 3. Non-goals
- The other three agents (5b-5d). Only their slots (§7).
- Retraining or changing the Phase 3 model, or any file in `data/model/`. The model is loaded to
  predict only.
- New FDIC fields (the specialty label comes with 5c).
- The Streamlit dashboard (Phase 6); it will later call the same writer function.
- Any AWS use. Everything reads local files; AWS cost for 5a is $0.
- Outside sources (news, filings). Memos say only what Canary's data shows.

## 4. Anti-goals (a failure even if it "works")
- **A memo states a number that isn't in its fact sheet**, or rounds/relabels one into something
  different. The checker exists to stop this; a memo that fails it is not saved.
- **Hindsight leaking into the "as of" part.** Only three places may use data after the as-of
  date: the outcome banner, the outcome section (§5.3) and "What happened next". The Summary,
  "Warning signs" and "Understanding the score" are as-of only.
- **Presenting the raw score as a probability.** The model was trained with extra weight on failed
  banks (`scale_pos_weight`), so the score ranks banks but isn't a chance of failure. Memos lead
  with rank and say this.
- **Post-hoc results presented as the model's.** The Phase 4 run-risk rank may appear only labeled
  "post-hoc check, designed after the 2023 failures".
- **Claims about things the data can't see** (who depositors are, fraud, management). If it's not
  in the fact sheet, the memo doesn't say it.
- **Writing into `data/model/`.**

## 5. What gets written

### 5.1 Which banks and which quarter
The model is fixed; scoring a quarter it never trained on is not leakage. 5a scores **every
bank-quarter from 2016-03-31 to the latest quarter in the feature export (2026-06-30 today)** with
the saved model, using the existing rank and 2% watchlist rule (decision 0011, `flag_watchlist`,
`national_rank`). Memos are allowed only for as-of dates in that range; earlier dates are refused
(those rows were training data, so their scores aren't a fair test).

| Group | Banks | As-of quarter |
|---|---|---|
| Case studies | SVB 24735, Signature 57053, First Republic 59017 | last report before failure |
| Other test misses | the other 5 of the 8 misses in `data/replay/test_misses.csv` | last report before failure |
| Test catches | the 21 caught certs in `data/model/metrics.json` | last report before failure |
| Failed after the test window | banks that failed after 2025-12-31 with a scored report 1-4 quarters before failure (today: 25796, 57488, 28722, 25744) | last report before failure |
| Latest watchlist | top 2% at the latest quarter (≈86 banks) | latest quarter |
| False alarms | the 10 banks in `data/replay/top_false_alarm_banks.csv` | their most recent flagged quarter |

About 130 notes (overlaps counted once). The groups only choose *which* banks get notes; each
note's outcome comes from the rules in §5.3, never from the group it was picked by. (Example: two
banks in `top_false_alarm_banks.csv`, 25796 and 57488, failed in 2026, so their outcome is
"caught", tagged as after the test window.) A bank that is both a past false alarm and on the latest
watchlist gets as-of = latest quarter and outcome `open_watchlist`. The default as-of for an
on-request memo is: last report before failure for a failed bank, otherwise the latest quarter.

### 5.2 The note
File: `banks/<Institution Name> (<cert>).md`, one per bank (re-running replaces it). YAML front
matter: `cert`, `name`, `as_of`, `rank`, `n_banks`, `percentile`, `flagged`, `outcome`
(caught / missed / false_alarm / quiet / open_watchlist), `after_test_window` (true for failures
after 2025-12-31), `failure_date`, `model_run`, `written_at`, `writer_model`, `checked: true`.

The note opens with a one-line, code-rendered **outcome banner**, labeled hindsight, e.g.
"*Hindsight: failed 2023-03-10. Canary did not flag it.*" For a failure after the test window it
adds: "*After the test window: not part of the reported 2016-2024 results.*" Sections in order:

1. **Summary**: 2-4 sentences, as-of only (no outcome).
2. **Warning signs in the data**: the bank's notable figures at as-of (capital, credit quality,
   liquidity/funding, bond losses), each compared with the national median for that quarter.
3. **Understanding the score**: (a) rank, percentile and watchlist line, plus the fixed sentence
   that the score ranks banks and is not a probability; (b) top 5 drivers up and down, in plain
   names, with the feature value; (c) what the model can't see (§5.4).
4. **Score history**: a code-rendered table (not AI-written) of rank and flag for the 8 quarters up
   to as-of, with "first flag" marked.
5. **Outcome section** (§5.3).
6. **What happened next** (hindsight, labeled; code + AI): for failed banks, failure date and the
   rank in each later quarter (none); for others, rank and flags after as-of through the latest
   quarter, and whether the bank still reports (still open / stopped reporting: merged or closed,
   not distinguished in our data).
7. **Sources**: code-rendered list of every cited fact (field, quarter, value, file).

Slots for 5b-5d (§7) sit between 4 and 5 and are empty in 5a.

### 5.3 Outcome section (by case)
| Model at as-of / before | What happened | Section |
|---|---|---|
| Flagged at a report 1-4 quarters before failure (Phase 3 recall rule, `bank_recall`) | Failed | "How early Canary caught it": first flag quarter and quarters ahead of failure, both by Phase 3's `lead_times` rule (earliest flag within the 1-4 quarter window, so at most 4), plus drivers at that quarter. Earlier flags (e.g. years before) show only in the score history. |
| Not flagged | Failed | "Why the model missed it": drivers, plus Phase 4 findings for that bank where they exist (training mix, what-if, post-hoc run-risk rank, labeled) |
| Flagged at as-of | No failure by data end | "Why it was flagged, and what happened" |
| Not flagged | No failure | none |
The latest-watchlist banks have no outcome yet; their section is "Why it's on the watchlist" and
says the outcome is unknown. Failures after 2025-12-31 get the same caught/missed rule, tagged
"after the test window" in the banner, front matter and section; they never change the reported
2016-2024 numbers.

### 5.4 What the model can't see
A fixed, code-chosen paragraph per case, from Phase 4 conclusions (decisions 0013-0015): for
banks without a credit-loss profile, that the training failures were 96% credit-loss failures and
the model is flat in HTM losses; for all banks, that FDIC data has no loan fair values, depositor
identity or non-financial causes (fraud, management). Claude may rephrase it but adds no claims.

### 5.5 Citation checker
- The fact sheet is a list of facts, each with an id (`F1`, `F2`, ...), a label, a quarter, a value
  and its allowed display forms (e.g. 0.9812 → "98%", "98.1%", "0.98").
- Claude returns **structured output** (JSON schema): for each AI-written section, a list of
  paragraphs; every sentence that contains a number carries the ids it cites.
- Code checks: every number in a sentence (digits, %, $, "x", ranks, dates) matches a display form
  of one of the facts that sentence cites; every cited id exists; dates are inside the allowed
  window for that section (≤ as-of, except the outcome section and "What happened next", which may
  go to the latest data).
- On failure: one retry with the checker's errors appended; if it fails again, the note is not
  written and the bank is logged in the run report.
- Counts like "5 quarters" are allowed only if they're facts (e.g. a computed lead time).

## 6. The on-request agent
`python -m canary.analyst ask "write up the bank in Santa Clara that failed in 2023"`

The loop runs locally with the Anthropic Python SDK's **tool runner** (`client.beta.messages.tool_runner`
with `@beta_tool` functions): Claude picks a tool, Canary's code runs it, the result goes back, until
Claude answers. Four tools, all local Python reading the same data:
- `find_bank(query, state?, failed_year?)`: search by name, state or cert for every bank; by city
  only for failed banks (city is in `failures.parquet` but not in the financials; city for all banks
  can come with 5c's data pull). Returns up to 10 matches with cert, name, state, city (if known),
  first/last report, failure date.
- `get_bank_facts(cert, as_of?)`: the same fact sheet the writer uses (so answers are checked
  facts).
- `list_watchlist(quarter?)`: top 2% for a quarter, with rank and name.
- `write_memo(cert, as_of?)`: runs the G1 writer and returns the note path and checker result.

The agent's own reply is plain chat, not saved, and its system prompt tells it to answer only from
tool results and to call `write_memo` for anything memo-sized. If several banks match a query, it
lists them and asks rather than guessing.

`python -m canary.analyst memo --cert 24735 [--as-of 2022-12-31]` writes one note directly (no agent). `python -m canary.analyst showcase` writes the §5.1 set.

## 7. Slots for 5b-5d
A section registry: each specialist is a module providing `build_facts(bank, as_of) -> list[Fact]`
and a section spec (title, position, instructions). The writer merges all registered specialists'
facts into one sheet and asks for all sections in one call, so one checker covers everything.
5a registers only the analyst sections. Each agent tool lives in `canary.analyst.tools` so later
agents reuse them.

## 8. Approaches considered
- **A. Fact sheet + one AI call (chosen for the memo).** Code decides the facts, AI writes, code
  checks. Reproducible inputs, cheap, testable without the API.
- **B. Fully tool-using agent writes memos (rejected for the memo, used for `ask`).** More flexible,
  but two runs on a bank could look at different facts, and it's harder to test and costs more.
  Victor wanted a real agent; it fronts the writer instead of replacing it.
- **C. Templates, no AI (rejected).** Reliable, but drops the AI analyst that Phase 5 exists for.

## 9. Decided by Victor
- Showcase set plus an on-request agent (§5.1, §6).
- Failed banks' memos are "as of" the last report before failure, hindsight in a labeled section.
- Every memo explains the score (§5.2 item 3).
- Outcome-aware section for caught / missed / false alarm (§5.3).
- Phase 5 order: risk analyst → trend/watchlist → peer comparison → concentration risk.
- Failures after the test window (2026) get their real caught/missed outcome, tagged "after the
  test window: not part of the reported 2016-2024 results"; the README headline is unchanged, with
  a short separate line on these as an extra out-of-sample check (§5.3).
- The `ask` agent runs on the SDK's local tool runner, not Managed Agents: tokens only, no session
  history kept, easy to test with a fake Claude, and the whole loop is code Victor can read (§6).
  Managed Agents stays an option for a scheduled agent later.

## 10. Calls made by Claude (Victor to check)
- **Model: Claude Opus 5.5** (`claude-opus-5-5`), effort `medium`, adaptive thinking, structured
  output for memos. Showcase run via the **Message Batches API** (half price), about $3 for ~130
  memos. Single memos and `ask` use the normal API, a few cents each. Sonnet 5.5 would be about
  half that; switch is one setting. **Before the showcase run**, a model comparison (Victor's
  request): memos for SVB, Signature and First Republic written with both Opus 5.5 and Sonnet 5.5
  (about $0.30), compared on checker pass rate (first try and after retry), tokens and cost, and
  read side by side by Victor. Victor picks the showcase model from that; the result goes in the
  memo-design decision record.
- **Refusal fallback** turned on (`fallbacks: "default"`), so a rare safety refusal retries on
  another model instead of failing.
- **"Caught early" uses Phase 3's rule** (earliest flag within the 4 quarters before failure,
  `lead_times`), so lead times match `metrics.json`; older flags show only in the score history.
- **Outcome banner at the top of every note** (hindsight, labeled); the Summary stays as-of only.
- **Outcome comes from rules, not from the showcase group**; a past false alarm now on the latest
  watchlist is `open_watchlist` (§5.1).
- **City search for failed banks only** in 5a (§6).
- Scores for 2016-03-31 to the latest quarter are computed on the fly from the saved model (no new
  file in `data/model/`); cached under `data/analyst/` (gitignored like other data).
- Notes are committed to the repo (`banks/` already exists), so they show on GitHub.
- Feature names are mapped to plain names in one table (e.g. `htm_unrealized_loss_to_equity` →
  "losses on bonds held to maturity, as a share of equity"), reused from `reference/GLOSSARY.md`.
- API key read from `ANTHROPIC_API_KEY` (in `.env`, never committed) or an `ant auth login` profile.
- New optional dependency group `analyst = ["anthropic>=..."]`.
- A decision record for the memo design (checker, as-of rule, score-not-a-probability), one for
  the agent (tool runner vs Managed Agents) and one for labeling failures after the test window.

## 11. Left to the builder
- Exact JSON schema, prompt wording, and the display-form rules (as long as §5.5 holds).
- Name-search matching details for `find_bank`.
- Run report format for the showcase (counts written / failed check / skipped).
- How the national medians in "Warning signs" are computed (all banks that quarter is fine).
