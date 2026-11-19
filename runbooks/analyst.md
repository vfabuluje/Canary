# Runbook: the risk analyst (Phase 5a)

How to write bank notes and ask questions. Design: [[specs/2026-11-17-phase5a-risk-analyst-design]]. Decisions: [[decisions/0016-analyst-memo-design]], [[decisions/0017-analyst-agent-tool-runner]], [[decisions/0018-failures-after-test-window]], [[decisions/0019-ratio-trends-descriptive]], [[decisions/0020-peer-comparison-descriptive]]. Output formats: [[data-dictionary/bank_notes]], [[data-dictionary/analyst_outputs]].

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

## City search
`find_bank` matches a city for every bank, not just failed ones. The city is the FDIC's `CITY` at the bank's last row in `data/raw/specialty/` (falling back to the failures list); the context needs that table, so run `python -m canary.ingest specialty` first or loading fails with a message saying so.

## The trends section (Phase 5b)
Every memo now includes "How its ratios moved" after Score history, so no new command or flag. It makes each memo a little more expensive: a live memo for SVB as of 2022-03-31 cost $0.27 (2 attempts, 22,571 in / 9,233 out tokens), against about 9-10 cents for a 5a memo, because the facts list is longer and a retry costs a full call. A bank with no ratio outside its own range gets a single code-written line and no extra AI work. The section is descriptive only ([[decisions/0019-ratio-trends-descriptive]]); its format is in [[data-dictionary/bank_notes]]. If a memo is rejected for this section, the error mentions pairing, direction or prediction language: re-run, and if one bank keeps failing, read the error before suspecting the prompt.

To try one memo without touching the committed notes, write it elsewhere: `memo --cert 24735 --as-of 2022-03-31 --out data/analyst/trend_check` (`data/` is git-ignored). Notes already in `banks/` do not have the section until the showcase is re-run.

## The peer section (Phase 5c)
Every memo now includes "Compared with similar banks" after "How its ratios moved". It needs the specialty table, so run `python -m canary.ingest specialty` once first (see [[runbooks/fdic-ingestion]]); without it the context fails with a message naming that command. It is descriptive only ([[decisions/0020-peer-comparison-descriptive]]); the format is in [[data-dictionary/bank_notes]]. Banks with no nationally unusual ratio, or too few peers, get code-written lines and no extra AI work.

One live test memo (SVB, 2022-12-31, written to `data/analyst/peer_check`, git-ignored) cost $0.3457 (2 attempts, 29,965 in / 11,292 out tokens), so expect roughly $0.25-0.35 per memo with both sections and the second attempt. Try one without touching the committed notes: `memo --cert 24735 --out data/analyst/peer_check`. If a memo is rejected for this section, the error mentions one ratio per sentence, an opposite reading or prediction language; a false rejection of "unusually low among peers" (no "its") is a known limit and a retry usually clears it. **Notes already in `banks/` do not have this section.** The showcase is not re-run until Phase 5d is built, then once, with a dry-run estimate approved first.

## Exit codes
- `0` success (for `showcase`, every bank written).
- `1` a memo failed the citation check twice, Claude refused, the answer was cut off, malformed JSON, missing input files, no credentials, a Claude API error, or (showcase) any bank failed.
- `2` bad cert or as-of date.

## Cost (measured 2026-11-17)
Opus 5.5 is about 9-10 cents per memo call at full price ($4 per million input tokens, $20 per million output), roughly half in a batch. Retries run at full price. `showcase --dry-run` builds the real requests (no API calls) and prints an estimate at batch price, then a separate retry allowance at full price, then the total. Derivation (Phase 5b): the live SVB 2022-03-31 memo used 22,571 input and 9,233 output tokens over 2 calls, so about 4,600 output tokens per call (`EST_OUTPUT_TOKENS`, adaptive thinking included). Input = `len(json.dumps(request)) / CHARS_PER_TOKEN`. The SVB first request is 22,979 characters; assuming the retry's extra (the rejected memo plus error text) was about 3,200 tokens, the first request was about 9,600 input tokens, which gives `CHARS_PER_TOKEN = 2.4` (the memo size is an assumption, so this is approximate; a plain 3.5 would under-count input by about 30%). Retry allowance: 30% of banks (5a: 18 of 61 needed one) at full price, each with input about 2x the first request and 4,600 output. For the 61-bank `--watchlist-top 20` showcase: about 552k input and 281k output tokens, $3.91 at batch price, plus $2.96 retries, $6.87 total. The 5a figures (7,300 in / 3,200 out) are retired. `ask`'s `get_bank_facts` now returns about 45 more facts (prompt about 50% larger, so slightly higher cost per question). The three-bank model comparison cost $0.47 with Opus and $0.21 with Sonnet.

## When a memo fails the checker
The command prints the errors and writes no note. Each error names the section, the sentence and the reason (an unsupported number, a hindsight word in an as-of section, a missing post-hoc label). For `showcase`, the errors are in `data/analyst/showcase_report.json` under that bank's `errors`. Re-run `memo --cert N`: the model is not deterministic, so a second run often passes. If one bank fails repeatedly, read its errors; a recurring one may be a checker false rejection, which is a code fix, not a prompt change.

## If a showcase run stops
Do not start a new one: it refuses while `data/analyst/showcase_report.state.json` is incomplete (and would pay for a second batch). Run `showcase --resume BATCH_ID`.

## Example `ask` answers
Live runs on 2026-11-17 (Claude Opus 5.5).

**Q: write up the bank in Santa Clara that failed in 2023**

(claude-opus-5-5, 4,955 in / 345 out tokens, $0.0267; memos written by the agent are not included)

I wrote the memo for **Silicon Valley Bank** in Santa Clara, CA (FDIC cert 24735) and saved it to:
**`banks/Silicon Valley Bank (24735).md`**

It's the only bank in Santa Clara that failed in 2023. It failed on March 10, 2023, and its last report was for the quarter ending December 31, 2022, so the memo uses that quarter.

The memo passed its checks with no errors, though it took two tries. You can open the file to read it, or I can pull specific numbers like its national rank.

**Q: which banks are on the watchlist right now? just the top 5**

(claude-opus-5-5, 6,082 in / 271 out tokens, $0.0297; memos written by the agent are not included)

Here are the top 5 banks on the current watchlist (the top 2% of all banks by risk score):

| Rank | Bank | FDIC Cert |
|---|---|---|
| 1 | Tioga-Franklin Savings Bank | 33802 |
| 2 | Lamont Bank of St John | 8681 |
| 3 | Nano Banc | 58590 |
| 4 | Southpoint Bank | 58088 |
| 5 | Columbia Savings & Loan Assn | 28480 |

The full watchlist has 87 banks. These rankings compare banks with each other. They aren't probabilities that a bank will fail.

(Note: "right now" = the latest quarter in the data, 2026-06-30.)
