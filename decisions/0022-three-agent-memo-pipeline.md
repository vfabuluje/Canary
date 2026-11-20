# 0022 — Three AI agents write each memo: trend, peer, then the risk analyst

**Date:** 2026-11-19
**Status:** Accepted (design approved by the owner; built in Phase 5e)

## Decision
A memo is no longer one Claude call. **Three AI agents** write it, in this order, and code checks each one:

1. **Trend agent** writes "How its ratios moved" (`trends`).
2. **Peer agent** writes "Compared with similar banks" (`peers`).
3. **Risk analyst** writes every other AI section: the summary, warning signs, the score, the outcome section when the bank has one, and what happened next.

The **real-estate concentration** section stays code-only ([[decisions/0021-cre-concentration-2006-thresholds]]). Phase 5 is therefore three AI agents plus one code-only check.

Code: `src/canary/analyst/pipeline.py` (`agent_sheet`, `agent_sections`, `build_agent_request`, `run_agent`, `AgentResult`), `writer.py` (`write_memo`), `showcase.py` (the two batch rounds). Formats: [[data-dictionary/bank_notes]], [[data-dictionary/analyst_outputs]]. Design: [[specs/2026-11-19-phase5e-three-agent-memos-design]]. How to run it: [[runbooks/analyst]].

## Why
The owner wanted the analyst to be a real agent that reads other agents' work, not one call that writes everything at once. The work is also split by kind: the trend and peer sections each rest on a narrow set of facts and have their own wording rules ([[decisions/0019-ratio-trends-descriptive]], [[decisions/0020-peer-comparison-descriptive]]), so each gets a call that sees only what it needs. The analyst then sees the finished specialist sections and can say so when the evidence points different ways.

## What each agent sees
- **A specialist (trend or peer)** sees only its own facts: those whose kind starts with `trend_` (or `peer_`), plus the identity and rank facts (bank name, certificate number, as-of quarter, national rank, banks ranked that quarter, percentile and its scale line, watchlist status). Fact ids are the same as in the full sheet. Its memo is **checked against that subset**, so it cannot cite a fact it was not shown (for example a model driver).
- **The analyst** sees the full fact sheet plus the two specialist memos, already checked.
- A specialist is **skipped** when its section is code-only for that bank (a bank with no unusual ratio, or too few peers). Its code-written text still appears, and the analyst's message says that section is code-only.

## The analyst never edits specialist text
The merged note renders each specialist section from that agent's checked memo, **exactly the checked text**. The analyst cannot change, shorten or reword it. This keeps each section's checks meaningful: what the checker passed is what the reader sees.

The analyst's user message carries this instruction, word for word:

> The trend, peer and concentration sections are written by other agents or code and appear in the note as they are. Don't repeat them at length; you may refer to their findings and cite the same fact ids for any number you use. If two sections genuinely point different ways, say so plainly in warning signs or the summary; never blend them into one statement.

Two consequences. A number from a specialist section can be used in the analyst's text only with that specialist's fact id; the same number without a cite is rejected. And **the checker cannot verify the "say so plainly" behavior**: it checks numbers, ids and wording rules, not whether the analyst noticed a disagreement or voiced it. That behavior rests on the instruction and on reading real notes.

## Failure policy
- Each agent gets **one retry** with its own checker errors, called directly (not in a batch) at full price.
- A specialist or the analyst that still fails its check after the retry means **no note** for that bank, and **no analyst call** if a specialist failed. A note already on disk is kept as it was; a new trace is saved anyway.
- A **refusal, truncation or unparseable response on a direct call is final** for that agent: it is recorded as failed and not paid for again on resume.
- A **transport or unexpected error** (network, API outage, a bug) leaves that agent unfinished, so a resumed run does it again.

## Batch rounds (showcase)
`showcase` runs two Message Batches rounds. **Round 1** sends every specialist request (custom ids `cert-YYYYMMDD-trend`, `cert-YYYYMMDD-peer`). **Round 2** sends one analyst request per bank whose specialists passed (`cert-YYYYMMDD-analyst`), built from the checked specialist memos. Batch results are half price; retries are full price. The state file holds `round1_batch_id` and `round2_batch_id` and a summary of each agent's result (`agents`); the per-agent detail (collected batch results, checked results, trace entries) lives in `<report>.progress/`, so a stop between rounds or a crash never pays for a round twice and never redoes a finished bank. Resume refuses: an unknown batch id, no state file, a complete state, a state from the old single-batch run (no `round1_batch_id`), and `--resume ""`.

## Traces
Every written-or-attempted memo saves `data/analyst/traces/<cert>_<as_of>.json` (git-ignored), one entry per call: `agent`, `attempt`, `request`, `response_text`, `checker_errors`, `input_tokens`, `output_tokens`, `cost_usd`, `served_model`, `source` (`batch` or `direct`). The request is the arguments sent to the API; **no API key or header is stored**. Running the same bank and quarter again overwrites its trace. Format: [[data-dictionary/analyst_outputs]].

## Spending limit
`showcase --max-cost USD` (none by default; the owner set 17.00 for the paid run). It is checked **before round 2** (spent so far plus a projection from round 1's actual spend per request, scaled to the analyst's larger request, plus the analyst retry allowance) and **before every direct call** (spent so far plus that call's estimate). On a breach the run stops cleanly with "stopped at spending limit": finished notes, traces and the report are saved, and the same command with `--resume` continues, with the same or a new limit. A stop just before a retry can repeat up to two direct calls for that agent on resume, because a call that was not paid for is not recorded. The round 2 projection is neutral (neither padded nor trimmed), so set `--max-cost` **a few percent above the calibrated dry-run total**, or a normal run can stop just short of finishing.

## Cost per memo
**To be filled from the Task 6 calibration memo.** The dry run estimates each round and each agent separately; the per-agent constants in `showcase.py` (output tokens, retry share, specialist text size in the analyst request) are placeholders until then. Placeholders, not measurements: 5,700 output tokens per call, 16% retry share, 6,000 characters of specialist text per section. Measured cost per memo and the calibrated numbers: TO BE FILLED.

## Limits (honest list)
- Three calls cost more than one: the analyst re-reads the full sheet and the specialist text, and every agent has its own retry.
- The checker cannot judge whether the analyst handled a disagreement between sections well (see above).
- The specialists do not see each other's sections, so the trend and peer agents cannot flag a disagreement; only the analyst can.
- Not a model or accuracy change. The score, the facts and every section's meaning are as before, with no new measured result.
