# Phase 5e Spec: Three-agent memo pipeline

**Date:** 2026-11-19
**Status:** Built (approved by Victor 2026-11-19; decision [[decisions/0022-three-agent-memo-pipeline]])
**Phase:** Rework of the Phase 5 memo writer (5a-5d), before Phase 6. Branch `phase5e-three-agents`.

## 1. Intent: why this exists

Today a memo is **one Claude call**: code builds one fact sheet (5a facts plus the trend and peer
specialists' facts and the code-only concentration result) and one call writes every AI section,
including "How its ratios moved" (5b) and "Compared with similar banks" (5c).

Victor's intent from the start was **three real AI agents plus one code-only check**:
- a **trend agent** and a **peer agent**, each its own Claude call writing only its own section;
- the **concentration check**, code only (decided in 5d);
- a **risk analyst** that sees all three specialist outputs and writes the overall sections.

This spec changes the writer to that structure, rebuilds the 61 showcase notes with it, and saves
a real trace of each memo's calls, so the Phase 6 agent-handoff animation shows the pipeline as it
actually runs.

**The analyst never edits the specialists' text (Victor).** Where two sections genuinely disagree,
the analyst says so plainly instead of smoothing them into one voice: the project's rule of not
papering over something the data itself doesn't agree on.

## 2. Goals
- G1. **Trend agent call:** writes the `trends` section only, from the trend facts plus a small set of
  identity/rank facts (§4.1). Checked by the existing checker (including 5b's trend rules); one
  retry with the errors, as today.
- G2. **Peer agent call:** the same for the `peers` section, with 5c's peer rules.
- G3. **Concentration:** unchanged (code-only, 5d).
- G4. **Risk analyst call** (after G1-G3): sees the full fact sheet, the two specialists' **checked
  sections as written** and the concentration result; writes `summary`, `warning_signs`, `score`,
  the outcome section and `what_next`. Checked by the existing checker; one retry.
- G5. **Note assembly:** specialists' sections rendered verbatim (exactly the checked text); the
  analyst's sections; code-rendered parts unchanged (banner, score history, trend table, peer lines
  and table, concentration section, fixed sentences, sources).
- G6. **Trace:** for every memo written, save a JSON trace of each call (agent, request, response,
  checker errors per attempt, tokens, cost, served model) under `data/analyst/traces/` (gitignored),
  so one can later be copied into the dashboard's data.
- G7. **Showcase** runs as **two half-price batch rounds** (specialists, then analysts), with retries
  one by one at full price, a dry-run estimate for the new structure, and resume across both rounds.
- G8. The `memo` CLI, `compare` and the `ask` agent's `write_memo` tool use the same pipeline.
- G9. Tests for all non-AI code with a fake Claude (no network); docs (decision 0022, data dictionary,
  runbook, README).
- G10. **Then:** one paid **calibration memo** with the new pipeline (about $0.30-0.40, approved by
  Victor) whose measured tokens per call type become the dry-run constants → free dry run → Victor's
  OK → paid showcase re-run with a **$17 spending limit** (§6.1) → commit notes; pick one memo's
  trace for the animation (the calibration memo's trace is a candidate).

## 3. Non-goals
- Changing what any section says it covers, any fixed sentence, the checker's existing rules, the
  5b/5c/5d rules, the model, or the data.
- The analyst rewriting, trimming or "harmonizing" a specialist's section (anti-goal §4).
- Tool-calling between agents; hosted agent services.
- Phase 6 itself (dashboard, animation UI).

## 4. Anti-goals
- **A specialist's text changed after it passed the checker** (by the analyst or by code).
- **A memo saved with a missing or unchecked section.**
- **Blending a real disagreement** between sections into one smooth statement.
- **Hindsight in a specialist's section:** both specialist sections are as-of only, as today.
- **Spending on the re-run without Victor seeing the dry-run estimate first.**

### 4.1 What each call sees
- **Trend agent:** the trend facts (kinds `trend_*`) plus identity and rank facts: bank name,
  certificate number, as-of quarter, national rank, banks ranked, percentile, percentile scale, on
  the watchlist. Instructions: the existing `TREND_SECTION.instructions`.
- **Peer agent:** the peer facts (kinds `peer_*`) plus the same identity and rank facts. Instructions:
  the existing `PEER_SECTION.instructions`.
- Fact ids in a specialist request are the **same ids as in the full sheet** (a subset), so the
  analyst and the sources list refer to one numbering.
- **Analyst:** the full fact sheet (as today), plus:
  - "Trend agent's section (checked, do not rewrite)": the trend section's sentences with their
    cites;
  - "Peer agent's section (checked, do not rewrite)": likewise;
  - the concentration section's code-rendered lines;
  - a code-built list of the specialist sections that were code-only for this bank (e.g. no ratio
    outside its range), so the analyst doesn't invent them.
  New analyst instruction: "The trend, peer and concentration sections are written by other agents
  or code and appear in the note as they are. Don't repeat them at length; you may refer to their
  findings and cite the same fact ids for any number you use. If two sections genuinely point
  different ways, say so plainly in warning signs or the summary; never blend them into one
  statement." (The checker can't verify this wording; decision 0022 says so.)
- When a specialist section is code-only for a bank (5b/5c rules), that agent's call is **skipped**
  (no AI request), exactly as today.

## 5. Order, checking and failure
1. Build the fact sheet (all specialists' facts, as today) and the concentration result.
2. Trend and peer calls (independent; in the showcase, the same batch). Each: check → if errors, one
   retry with the errors (non-batch) → check.
3. If either specialist still fails, **the memo is not written**: no analyst call, nothing saved;
   the existing note (if any) stays; the run report lists the bank with the failing agent and errors.
4. Analyst call with the checked specialist sections → check → one retry → check. If it fails, not
   written (as above).
5. Render and save; save the trace.
- The checker runs per call on that call's sections only (`check_memo(memo, sheet, sections)` with
  the call's sections).
- Refusal/truncation/empty-response handling and cost accounting work per call as today; any
  exception after a call still reports that call's usage.

## 6. Showcase and dry run
- **Round 1 (batch):** one request per needed specialist call (up to 2 per bank). Collect, check;
  failures retried one by one at full price.
- **Round 2 (batch):** one analyst request per bank whose specialists all passed. Collect, check,
  retry one by one.
- **Resume:** the state file records both rounds' batch ids and progress; `--resume` continues from
  where it stopped without paying for a completed round again.
- **Dry run:** builds the real round-1 requests; estimates round-2 inputs from the analyst request
  built with **placeholder specialist sections of typical length** (builder's calibration, recorded
  in the runbook); reports tokens and cost per round at batch price, plus a retry allowance per call
  type, plus the total. Uses measured constants: first-try pass rate per call type defaults to the
  last showcase (51/61 memos passed first try ≈ 16% retried), applied per call.
- Report: per bank, per agent: ok, attempts, first-attempt errors; top-level tallies per agent.
- **Calibration (Victor):** the dry-run constants per call type (output tokens for trend, peer and
  analyst calls; round-2 input size) come from one real memo written with the new pipeline before the
  dry run, recorded in the runbook with the bank, date and token counts.

### 6.1 Spending limit (Victor: $17)
- `showcase --max-cost USD` (the showcase command's default for this run: 17.00). The run tracks
  actual spend (batch at half price, retries at full price).
- Checked (a) before submitting round 2, re-estimating round 2 from round 1's actual spend per bank,
  and (b) before every full-price retry. If the next step would push the total over the limit, the
  run **stops cleanly**: everything finished is saved (notes, traces, report), banks not reached keep
  their current notes, the report and state say "stopped at spending limit" with the spend so far,
  and `--resume` can continue later (with the same or a new limit).
- Tests cover: stop before round 2, stop before a retry, resume after a stop.

## 7. Approaches considered
- **A. Three-call pipeline inside the writer (chosen).** Deterministic order, every call checked,
  batchable at half price, testable with a fake client.
- **B. Analyst calls specialists as tools (rejected).** The analyst would decide when or whether to
  consult them; runs vary; no batch pricing; harder to test.
- **C. Hosted agent service (rejected, as in 5a).** Session costs and history for no gain.

## 8. Decided by Victor
- Trend and peer each their own Claude call writing their own section; concentration code-only;
  analyst sees all three outputs and writes summary, warning signs and outcome.
- The analyst never edits the specialists' text; genuine disagreements are stated plainly.
- Rebuild the showcase with this structure and capture the animation trace from a real run.
- Dry run and real cost estimate shown before any paid re-run.

## 9. Calls made by Claude (Victor to check)
- Specialists see only their own facts plus identity/rank facts (§4.1); same fact ids as the full
  sheet.
- The analyst also writes "Understanding the score" and "What happened next" (they were analyst
  sections already).
- A specialist that fails twice → the memo isn't written; the old note stays (§5).
- Showcase as two batch rounds with per-call retries; resume across rounds.
- Traces saved for every memo under `data/analyst/traces/` (gitignored); one is chosen for Phase 6
  later.
- Decision record 0022 (three-agent pipeline; analyst-never-edits rule; disagreement wording is a
  prompt rule the checker can't verify; failure policy; cost per memo).
- Calibration memo and the $17 limit are Victor's decisions (§6, §6.1); the limit stops the run
  cleanly rather than skipping retries.
- Cost expectation (to be replaced by the dry run): about $9-12 for 61 memos, against a balance of
  about $18.22; worst case could approach $20.

## 10. Left to the builder
- Module layout (e.g. a `pipeline.py` orchestrating calls, reusing `build_request`/`check_memo`),
  request/system-prompt wording for the specialist calls within §4.1, the trace JSON shape (as long
  as G6's contents are there), and the dry-run calibration of round-2 input.
