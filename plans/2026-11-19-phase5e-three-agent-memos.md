# Phase 5e Three-agent Memo Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write each memo with three Claude calls (trend agent, peer agent, risk analyst) plus the code-only concentration check, run the showcase in two batch rounds under a spending limit, and save a trace of every memo's calls.

**Architecture:** A new `canary/analyst/pipeline.py` builds per-agent requests from subsets of the one fact sheet (same fact ids) and runs check-and-retry per call; `writer.write_memo` keeps its signature and orchestrates trend → peer → analyst, merges the three checked memos, renders the note and saves a trace. `showcase.py` runs round 1 (specialists) and round 2 (analysts) as batches with per-call retries, resume across rounds, a per-call-type dry-run estimate and a `--max-cost` limit.

**Tech Stack:** Python 3.12, pandas, `anthropic` SDK (Messages, Message Batches), pytest. No new dependencies.

**Spec:** `specs/2026-11-19-phase5e-three-agent-memos-design.md` (read it first; § numbers refer to it).

## Global Constraints

- Branch `phase5e-three-agents`. Tests: `.venv.nosync/bin/python -m pytest`. **No test calls the network or the Claude API** (use `tests/analyst_fakes.FakeClient` / the showcase `BatchClient`). Baseline: 561 passed.
- **Paid calls happen only in Task 6, run by the controller**, never by an implementer.
- Agents and their sections: `trend` → `trends`; `peer` → `peers`; `analyst` → every other AI-written section (`summary`, `warning_signs`, `score`, the outcome section when present, `what_next`). Concentration stays code-only.
- A specialist's call is skipped when its section is in `sheet.code_only` (5b/5c rules).
- Specialist fact subset = facts whose `kind` starts with `trend_` (or `peer_`) **plus** the identity/rank facts with labels: "Bank name", "Certificate number", "As-of quarter", "National rank (1 = highest score)", "Banks ranked that quarter", "Percentile (100 = highest risk)", `facts.PERCENTILE_SCALE_LABEL`, "On the watchlist". Same fact ids as the full sheet. A specialist's memo is checked against its subset (it cannot cite a fact it wasn't shown).
- **The analyst never edits specialist text.** The merged note renders each specialist section from that agent's checked memo, byte for byte.
- Analyst instruction (exact, added to its user message): "The trend, peer and concentration sections are written by other agents or code and appear in the note as they are. Don't repeat them at length; you may refer to their findings and cite the same fact ids for any number you use. If two sections genuinely point different ways, say so plainly in warning signs or the summary; never blend them into one statement."
- Failure policy: a specialist that still fails after its one retry → **no analyst call, no note written**, existing note untouched; same for the analyst.
- Retries: one per call, with that call's checker errors, non-batch, full price.
- Traces: one JSON file per written-or-attempted memo at `data/analyst/traces/<cert>_<as_of>.json` (gitignored), containing per call: `agent`, `attempt`, `request` (the kwargs sent), `response_text`, `checker_errors`, `input_tokens`, `output_tokens`, `cost_usd`, `served_model`, `source` ("batch" or "direct").
- Spending limit: `showcase --max-cost USD` (Victor: **17.00** for the paid run). Checked before submitting round 2 (re-estimating round 2 from round 1's actual spend per bank) and before every full-price retry; on breach, stop cleanly (§6.1).
- Model, effort, prices, fallbacks, refusal/truncation handling: unchanged from `writer.py`.

## Review Focus

1. **A specialist cites a fact outside its subset** (e.g. a 5a driver): rejected by its own check, retried with that error. Test in Task 1/2.
2. **Bank where trends and/or peers is code-only**: no request for that agent; the analyst's message lists it as code-only; the note still renders. Test in Task 2.
3. **Specialist fails twice**: no analyst call is made (fake client receives no third call), no note written, an existing note file is untouched, trace still saved with the failure. Test in Task 2.
4. **Resume after a stop between rounds** (spending limit or crash): no round is paid twice; finished banks aren't redone. Test in Task 4.
5. **Analyst output quoting a specialist number** citing the specialist's fact id: accepted; quoting it without a cite: rejected. Test in Task 1.

---

### Task 1: Per-agent requests (pure)

**Files:**
- Create: `src/canary/analyst/pipeline.py`, `tests/test_analyst_pipeline_requests.py`
- Modify: `src/canary/analyst/writer.py` (factor the shared rules out of `SYSTEM_PROMPT` so specialists reuse them)

**Interfaces:**
- Produces (in `canary.analyst.pipeline`):
  - `AGENTS = ("trend", "peer", "analyst")`; `AGENT_SECTIONS: dict[str, str] = {"trend": "trends", "peer": "peers"}`; `IDENTITY_LABELS: tuple[str, ...]` (Global Constraints).
  - `agent_sheet(sheet: FactSheet, agent: str) -> FactSheet` — a copy with `facts` filtered per Global Constraints (analyst → unchanged).
  - `agent_sections(sheet: FactSheet, agent: str) -> list[Section]` — from `sections_for(sheet)`: the specialist's one AI section, or for the analyst every AI-written section except `trends`/`peers`; `[]` when the specialist's section is code-only.
  - `build_agent_request(sheet: FactSheet, agent: str, model: str, specialist_memos: dict[str, dict] | None = None, errors: list[str] | None = None, previous: dict | None = None) -> dict` — kwargs for `messages.create` (same shape as `writer.build_request`). Specialist system prompt: role line ("You are Canary's trend agent…" / "…peer agent…") + the shared rules; user message: their fact table + their section's instructions. Analyst: the existing system prompt and user message, plus the checked specialist sections (each sentence's text with its cites), the concentration section's code lines (`render_concentration(sheet.extras["concentration"])` when present), the list of code-only specialist sections, and the exact analyst instruction from Global Constraints.
- [ ] **Step 1: Failing tests:** `test_trend_subset_has_trend_and_identity_facts_only` (ids preserved); `test_peer_subset`; `test_analyst_sheet_unchanged`; `test_agent_sections_split` (trend → [trends]; analyst excludes trends/peers; code-only trends → []); `test_specialist_request_schema_only_its_section`; `test_analyst_request_contains_specialist_text_and_instruction` (exact instruction string present; specialist sentences present; concentration lead line present); `test_specialist_cite_outside_subset_rejected` (check against `agent_sheet` rejects an unknown id); `test_analyst_can_cite_specialist_fact` (Review Focus 5).
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** file + full suite — PASS. **Step 5: Commit** `"Pipeline: per-agent fact subsets and requests"`.

---

### Task 2: `write_memo` as a three-call pipeline, with traces

**Files:**
- Modify: `src/canary/analyst/pipeline.py` (call runner), `src/canary/analyst/writer.py` (`write_memo` orchestration; `MemoResult` gains `agents`), `src/canary/analyst/__main__.py` (memo output shows per-agent attempts), `src/canary/analyst/compare.py`, `src/canary/analyst/tools.py` (only if result fields they read change)
- Modify tests: `tests/test_analyst_writer.py`, `tests/test_analyst_compare.py`, `tests/test_analyst_tools.py` and any test building single-call fake responses (now three responses in order trend, peer, analyst — skipping code-only agents)
- Create: `tests/test_analyst_pipeline_write.py`

**Interfaces:**
- Consumes: Task 1.
- Produces:
  - `@dataclass AgentResult`: `agent`, `ok: bool`, `attempts: int`, `errors: list[str]`, `first_errors: list[str]`, `memo: dict | None`, `input_tokens`, `output_tokens`, `cost_usd`, `served_model`, `skipped: bool`.
  - `run_agent(sheet, agent, *, client, model, specialist_memos=None, first_memo=None, trace: list) -> AgentResult` — one call (or the given batch `first_memo`), check against `agent_sheet`, one retry with errors, check; appends trace entries.
  - `write_memo(ctx, cert, as_of=None, *, client, model=DEFAULT_MODEL, out_dir=Path("banks"), first_memos: dict[str, dict] | None = None, replay_dir=Path("data/replay"), trace_dir=Path("data/analyst/traces")) -> MemoResult` (`first_memo` → `first_memos` keyed by agent; callers updated). `MemoResult` keeps its fields (`attempts` = max attempts over agents; `errors`/`first_errors` = concatenated, each prefixed `"[agent] "`; tokens/cost summed) and adds `agents: dict[str, AgentResult]`.
  - Order: trend, peer (skipped if code-only), stop if either not ok; analyst with `{"trend": memo, "peer": memo}`; merge `{"sections": trend + peer + analyst sections}`; `render_note` unchanged; write trace (always, including failures).
- [ ] **Step 1: Failing tests** (`tests/test_analyst_pipeline_write.py`, FakeClient): `test_three_calls_in_order` (call kwargs' schema enums = [trends], [peers], analyst sections); `test_specialist_text_verbatim_in_note` (trend/peer paragraphs appear exactly as the fake returned them); `test_code_only_specialist_skipped` (two calls only); `test_specialist_retry_then_ok`; `test_specialist_fails_twice_no_analyst_call_no_note` (Review Focus 3; existing note file bytes unchanged); `test_analyst_fails_twice_no_note`; `test_trace_written` (file exists, one entry per call with required keys; also on failure); `test_usage_summed_and_on_exception` (a refusal in the peer call still reports trend + peer usage on `exc.usage`); `test_ask_write_memo_tool_uses_pipeline`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement; update existing tests to three-call fakes** (helpers in `tests/analyst_fakes.py`: `fake_agent_memo(sheet, agent)` returning a valid memo for that agent's sections). **Step 4: Run** each `tests/test_analyst_*.py` alone and the full suite — PASS.
- [ ] **Step 5: Commit** `"Writer: three-agent pipeline (trend, peer, analyst) with traces"`.

---

### Task 3: Showcase in two batch rounds, with resume

**Files:**
- Modify: `src/canary/analyst/showcase.py` (`run_showcase`, `_run_batch`, state, report), `tests/test_analyst_showcase.py` (`BatchClient` returns per-agent results keyed by `custom_id`)

**Interfaces:**
- Consumes: Task 2 `run_agent`, `build_agent_request`, `write_memo(first_memos=...)`.
- Produces: custom ids `f"{cert}-{as_of:%Y%m%d}-{agent}"`; round 1 = one request per bank per non-skipped specialist; round 2 = one analyst request per bank whose specialists passed (after round-1 checks and retries); state file records `round1_batch_id`, `round2_batch_id`, per-bank per-agent status and spend; report: per bank `agents: {agent: {ok, attempts, first_errors, source}}`, top-level `first_try_passed_by_agent`, `first_error_sections` (kept), `spend_by_round`.
- [ ] **Step 1: Failing tests:** `test_two_rounds_created` (round 2 requests only after round 1 ended; analyst requests include specialist text); `test_specialist_failure_excludes_bank_from_round2`; `test_retries_are_direct_calls`; `test_report_per_agent`; `test_resume_after_round1` (state with round 1 done → only round 2 submitted; no second round-1 batch); `test_resume_mid_round2`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** — PASS; full suite — PASS.
- [ ] **Step 5: Commit** `"Showcase: two batch rounds (specialists, analysts) with resume"`.

---

### Task 4: Dry-run estimate per call type and the spending limit

**Files:**
- Modify: `src/canary/analyst/showcase.py` (`estimate_run`, constants, limit), `src/canary/analyst/__main__.py` (`--max-cost`), `tests/test_analyst_showcase.py`

**Interfaces:**
- Constants (placeholders until Task 6 calibration; marked `# calibrated in Task 6`): `EST_OUTPUT_TOKENS_BY_AGENT = {"trend": 5700, "peer": 5700, "analyst": 5700}`, `EST_ANALYST_SPECIALIST_CHARS = 6000` (placeholder text length added to analyst requests), `RETRY_SHARE_BY_AGENT = {"trend": 0.16, "peer": 0.16, "analyst": 0.16}`.
- `estimate_run(...)` returns per round: input tokens (round 1 from the real requests; round 2 from analyst requests built with placeholder specialist sections of `EST_ANALYST_SPECIALIST_CHARS`), output tokens, batch cost; retry allowance per agent; total. CLI dry run prints each line.
- `run_showcase(..., max_cost: float | None = None)`; CLI `--max-cost USD`. Before round 2: projected total = spent + estimated round-2 batch cost (from round 1's actual per-bank average scaled by the analyst/specialist estimate ratio) + its retry allowance; if > limit → stop. Before each full-price retry: spent + that call's estimated full-price cost > limit → stop. Stop = save notes/traces finished so far, report `"stopped": "spending limit"`, state resumable.
- [ ] **Step 1: Failing tests:** `test_dry_run_prints_rounds_and_total`; `test_stop_before_round2_when_projected_over_limit` (no round-2 batch created; report says stopped; state resumable); `test_stop_before_retry`; `test_resume_after_limit_stop_with_higher_limit`; `test_no_limit_runs_through`.
- [ ] **Step 2: Run** — FAIL. **Step 3: Implement.** **Step 4: Run** — PASS; full suite — PASS.
- [ ] **Step 5: Commit** `"Showcase: per-agent dry-run estimate and --max-cost spending limit"`.

---

### Task 5: Docs

**Files:**
- Create: `decisions/0022-three-agent-memo-pipeline.md`
- Modify: `data-dictionary/analyst_outputs.md` (trace file format; report's new fields; state file), `data-dictionary/bank_notes.md` (which agent writes which section), `runbooks/analyst.md` (pipeline, dry run, `--max-cost`, resume, calibration placeholder), `README.md` (Phase 5: three AI agents plus one code-only check; how a memo is written; test count), `reference/STACK.md` if it describes the single call, `specs/2026-11-19-phase5e-three-agent-memos-design.md` (Status: built)
- [ ] **Step 1: Decision 0022:** why (Victor's intent: real agents), the order, what each agent sees, the analyst-never-edits rule and the "state disagreements plainly" instruction (exact text; the checker can't verify it), failure policy, batch rounds, traces, spending limit, cost per memo (to be filled from Task 6's calibration).
- [ ] **Step 2: The rest.** **Step 3: Full suite; commit** `"Phase 5e docs: decision 0022, dictionary, runbook, README"`.

---

### Task 6: Calibration memo, dry run, STOP (controller; paid)

Run by the controller after the final whole-branch review and its fixes.
- [ ] **Step 1: Calibration memo (Victor approved, about $0.30-0.40):** `memo --cert <a latest-watchlist showcase bank> --out data/analyst/calibration`. Record per-agent input/output tokens and cost from the trace.
- [ ] **Step 2:** Set `EST_OUTPUT_TOKENS_BY_AGENT` and `EST_ANALYST_SPECIALIST_CHARS` from the trace; record bank, date and numbers in `runbooks/analyst.md` and decision 0022; tests; commit.
- [ ] **Step 3: Free dry run:** `showcase --watchlist-top 20 --dry-run`. **STOP and show Victor the estimate.** The paid re-run (`--max-cost 17`) happens only after his OK.
