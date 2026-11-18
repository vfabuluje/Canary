# Runbook: the risk analyst (Phase 5a)

How to write bank notes and ask questions. Design: [[specs/2026-11-17-phase5a-risk-analyst-design]]. Decisions: [[decisions/0016-analyst-memo-design]], [[decisions/0017-analyst-agent-tool-runner]], [[decisions/0018-failures-after-test-window]]. Output formats: [[data-dictionary/bank_notes]], [[data-dictionary/analyst_outputs]].

This calls **Anthropic's API, not AWS**, so AWS cost is unchanged. It needs the Phase 3 feature export and saved model on disk (read only).

## Setup
1. `pip install -e '.[dev,model,analyst]'`
2. Credentials, either:
   - `brew install anthropics/tap/ant`, then `ant auth login`; or
   - put `ANTHROPIC_API_KEY=...` in `.env` (git-ignored).
   Never commit a key. With neither, commands exit 1 with "No Anthropic API key found".

## Commands
All run from the repo root as `python -m canary.analyst <command>`.

```
memo --cert 24735                       # one note; as-of defaults to last report before failure, or the latest quarter
memo --cert 24735 --as-of 2022-12-31    # a chosen quarter (must be a quarter it reported, from 2016-03-31 on)
ask "write up the bank in Santa Clara that failed in 2023"
showcase --dry-run --watchlist-top 20   # list banks and estimate cost; no API calls
showcase --watchlist-top 20             # real run: one Message Batches job, then failures retried one by one
showcase --resume BATCH_ID              # collect a batch already created (id is in the log and the .state.json file)
compare                                 # SVB, Signature, First Republic with each model in --models
```

Other options: `--model` (default `claude-opus-5-5`), `--out` (default `banks`; `data/analyst/compare` for compare), `--report`, `--replay-dir`. `showcase` without `--watchlist-top` covers every latest-watchlist bank (about 130 notes in all).

## Exit codes
- `0` success (for `showcase`, every bank written).
- `1` a memo failed the citation check twice, Claude refused, the answer was cut off, malformed JSON, missing input files, no credentials, a Claude API error, or (showcase) any bank failed.
- `2` bad cert or as-of date.

## Cost (measured 2026-11-17)
Opus 5.5 is about 9-10 cents per memo call at full price ($4 per million input tokens, $20 per million output), roughly half in a batch. Retries run at full price. `showcase --dry-run` prints an estimate at batch price, excluding retries. The three-bank model comparison cost $0.47 with Opus and $0.21 with Sonnet.

## When a memo fails the checker
The command prints the errors and writes no note. Each error names the section, the sentence and the reason (an unsupported number, a hindsight word in an as-of section, a missing post-hoc label). For `showcase`, the errors are in `data/analyst/showcase_report.json` under that bank's `errors`. Re-run `memo --cert N`: the model is not deterministic, so a second run often passes. If one bank fails repeatedly, read its errors; a recurring one may be a checker false rejection, which is a code fix, not a prompt change.

## If a showcase run stops
Do not start a new one: it refuses while `data/analyst/showcase_report.state.json` is incomplete (and would pay for a second batch). Run `showcase --resume BATCH_ID`.

## Example `ask` answers
<!-- PLACEHOLDER: the controller fills this section after live runs. -->
