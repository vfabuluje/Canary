# analyst_outputs (Phase 5a working files)

Files `python -m canary.analyst` writes under `data/analyst/` (git-ignored; on the owner's machine possibly a `.nosync` copy). They are **local files, not warehouse tables**. The notes themselves are in [[bank_notes]]. Runbook: [[runbooks/analyst]].

## `scores.parquet` and `scores.json` (score cache)
Built by `context.py` so repeated runs do not re-predict. `scores.parquet` has one row per bank-quarter from 2016-03-31 on: every column of [[fct_bank_features]] plus `quarters_until_failure`, `failure_date`, `institution_name`, `label`, `split`, and the model columns:

| Column | Meaning |
|---|---|
| `score` | The saved model's output. A ranking number, not a probability ([[decisions/0016-analyst-memo-design]]). |
| `rank` | Rank among all banks scored that quarter; 1 = highest score, ties by `cert`. |
| `n_banks` | Banks scored that quarter. |
| `percentile` | `100 * (1 - (rank - 1) / n_banks)`. |
| `flagged` | True if on the top-2% watchlist that quarter ([[decisions/0011-watchlist-flag-and-metrics]]). |

`scores.json` is the **invalidation key**: `model_run` (hash of `model.json`), `features_size` and `features_mtime` of the feature export. If any differs from the current files, the cache is rebuilt.

## `showcase_report.json` (run report)
Always written, partial if the run stopped. Top level:

| Key | Meaning |
|---|---|
| `model` | Writer model asked for. |
| `batch_id` | Same as `round1_batch_id` (kept for older readers). |
| `round1_batch_id`, `round2_batch_id` | Message Batches ids: round 1 = trend and peer requests, round 2 = analyst requests. Null if that round was never created. |
| `complete` | False if an error escaped, the run stopped at the spending limit, or a bank is unfinished. |
| `stopped` | `"spending limit"` if the run stopped there, else null. |
| `max_cost` | The spending limit in force in USD (the `--max-cost` given, or the one saved in the state on a resume), or null. |
| `error` | Error text or null. |
| `banks_total`, `banks_done`, `written`, `failed` | Counts. |
| `first_try_passed`, `first_try_passed_by_agent` | Banks written with no first-attempt errors; and, per agent (`trend`, `peer`, `analyst`), how many of its memos passed the checker on the first attempt (code-only skips not counted). |
| `spend_by_round` | `round1` and `round2`, each with `batch`, `direct` and `total` USD plus `input` and `output` tokens. Batch results at half price, direct calls (retries) at full price. |
| `input_tokens`, `output_tokens`, `cost_usd` | Totals across both rounds. |
| `banks` | One entry per bank (below). |

Each `banks` entry: `cert`, `as_of`, `group` (`case_study`, `test_miss`, `test_catch`, `after_window`, `latest_watchlist`, `false_alarm`), `ok`, `attempts` (batch result counts as 1; a retry adds 1 or more), `path` (the note, or null), `errors` (checker errors if it failed), `source`, `served_model`, `first_errors` (the checker's complaints about each agent's first attempt, each prefixed `[agent] `; empty if all passed first try), and `agents`: per agent (`trend`, `peer`, `analyst`) `ok`, `attempts`, `first_errors` and `source` (`batch`, `direct`, `code` when the agent was skipped because its section is code-only, or null for an agent that did not finish). `attempts` counts a batch result as 1; a retry adds 1. Top level also has `first_try_passed` (banks written with no first-attempt errors) and `first_error_sections` (first-attempt errors counted by memo section, most first), so a high retry rate can be traced to the section causing it.

## `showcase_report.state.json` (resume file)
Written the moment round 1 is created: `batch_id` and `round1_batch_id` (the same), `round2_batch_id` (null until round 2 is created), `created_at`, `banks` (list of `[cert, as_of, group]`), `model`, `spend` (per round: batch and direct USD and tokens, saved before each result file so a crash is never under-counted), `agents` (per bank, each agent's checked result summary), `max_cost` (the limit in force, saved so a resume reuses it unless `--max-cost` overrides it), `complete`, and `stopped` (`"spending limit"` while stopped, else absent). `complete` becomes true only after both rounds are collected and every bank is finished. A new `showcase` run refuses to start while an incomplete state file exists; use `--resume BATCH_ID` with either round's id ([[runbooks/analyst]]). Resume is refused, with nothing changed, for: an id the state does not name, no state file, a complete state, a state from the old single-batch run (no `round1_batch_id`), and an empty id (`--resume ""`).

## `showcase_report.progress/` (resume detail)
A folder beside the report: each round's collected batch results and, per bank and agent, the checked result and its trace entries. It is what lets a resumed run skip finished work. A fresh run clears it.

## `traces/<cert>_<as_of>.json` (call traces)
One file per written-or-attempted memo, under `data/analyst/traces/` (git-ignored), written by `memo`, `showcase` and `compare`. Top level: `cert`, `as_of`, `ok` (true if a note was written), `calls`. Each call:

| Key | Meaning |
|---|---|
| `agent` | `trend`, `peer` or `analyst`. |
| `attempt` | 1, or 2 for the retry; 0 for a paid-but-unusable batch result (such an entry has an `error` key and no usable response). |
| `request` | The arguments sent to the API (system prompt, messages, output format). No API key or header is stored. |
| `response_text` | What the model returned (empty if the call failed before a reply). For a direct call, the reply text; for a batch call, the parsed memo re-serialized with `json.dumps`, not the raw model text. |
| `checker_errors` | The checker's errors for this attempt (empty if it passed). |
| `input_tokens`, `output_tokens`, `cost_usd` | This call's usage and cost; a batch call is at half price. |
| `served_model` | The model that actually answered. |
| `source` | `batch` or `direct`. |

Running the same bank and quarter again overwrites its file (compare runs too, per cert and as-of). A failed memo keeps its trace, so a rejection can be read afterwards.

## `compare/compare.json` and `compare/<model>/`
From `python -m canary.analyst compare`. `compare/<model>/` holds that model's notes (never `banks/`). `compare.json`:

| Key | Meaning |
|---|---|
| `models` | Per model: `passed_first_try`, `passed_after_retry`, `failed`, `input_tokens`, `output_tokens`, `cost_usd`. |
| `memos` | One entry per model and bank: `cert`, `model`, `served_model`, `path`, `attempts`, `ok`, `errors`, `first_errors` (the checker's complaints about the first attempt; empty if it passed first try). |
