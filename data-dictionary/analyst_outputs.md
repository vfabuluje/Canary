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
| `batch_id` | Message Batches id (null if no batch was created). |
| `complete` | False if an error escaped. |
| `error` | Error text or null. |
| `banks_total`, `banks_done`, `written`, `failed` | Counts. |
| `input_tokens`, `output_tokens`, `cost_usd` | Totals; batch results are counted at half price, retries at full price. |
| `banks` | One entry per bank (below). |

Each `banks` entry: `cert`, `as_of`, `group` (`case_study`, `test_miss`, `test_catch`, `after_window`, `latest_watchlist`, `false_alarm`), `ok`, `attempts` (batch result counts as 1; a retry adds 1 or more), `path` (the note, or null), `errors` (checker errors if it failed), `source` (`batch` or `retry`), `served_model`.

## `showcase_report.state.json` (resume file)
Written the moment the batch is created: `batch_id`, `created_at`, `banks` (list of `[cert, as_of, group]`), `model`, `complete`. `complete` becomes true only after every result is collected and every failed bank retried. A new `showcase` run refuses to start while an incomplete state file exists; use `--resume BATCH_ID` ([[runbooks/analyst]]).

## `compare/compare.json` and `compare/<model>/`
From `python -m canary.analyst compare`. `compare/<model>/` holds that model's notes (never `banks/`). `compare.json`:

| Key | Meaning |
|---|---|
| `models` | Per model: `passed_first_try`, `passed_after_retry`, `failed`, `input_tokens`, `output_tokens`, `cost_usd`. |
| `memos` | One entry per model and bank: `cert`, `model`, `served_model`, `path`, `attempts`, `ok`, `errors`, `first_errors` (the checker's complaints about the first attempt; empty if it passed first try). |
