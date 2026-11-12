# README Layers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the README so a bank tech recruiter understands the project from the first screen and a bank engineer still finds the full detail, moving only the case-study signal strings and long contribution analysis to `RESULTS.md`.

**Architecture:** Documentation only. `RESULTS.md` is created first from today's README sections, then `README.md` is rewritten as a plain top section plus a technical part. A throwaway number check confirms no figure was lost.

**Tech Stack:** Markdown; a shell one-liner for the number check.

**Spec:** `specs/2026-11-11-readme-layers-design.md`

## Global Constraints
- No number lost or changed; every number traceable to `metrics.json`, `case_studies.csv` or the data.
- No overclaiming: "caught" means flagged at least once 1-4 quarters before failure.
- "Research tool, not financial advice." stays near the top of README.md.
- Nothing personal in committed files. No Phase 4 results.
- Every technical term explained in plain words where it first appears.

## Review Focus
1. A number in the old README missing from both new files (Task 2, Step 3 check).
2. A friendlier phrase that changes meaning ("caught", "a year early", "98% false alarms") (Task 2, Step 4 read-through).
3. Broken relative links after the move (Task 2, Step 3 link check).
4. GitHub rendering of tables and the divider (Task 2, Step 4).
5. Jargon left unexplained in the top section (Task 2, Step 4).

---

### Task 1: Create `RESULTS.md`

**Files:** Create `RESULTS.md`

- [ ] **Step 1:** Save the current README for checking: `git show main:README.md > "$SCRATCH/README.old.md"` (scratchpad dir).
- [ ] **Step 2:** Create `RESULTS.md`: title "Canary: detailed results (Phase 3)", a one-paragraph intro linking back to README, then moved verbatim from today's README: the three full case-study tables with top signals and their footnote paragraph, and the full "What was caught, what wasn't, and why" (both paragraphs). Include the "Research tool, not financial advice." line.

### Task 2: Rewrite `README.md`

**Files:** Modify `README.md`, `daily-log.md`

- [ ] **Step 1:** Top section per spec "Design → Top, plain", headed with plain titles (What Canary is / The SVB story / What I found / Why it missed SVB, Signature and First Republic / What's next / Built with), each technical term glossed once.
- [ ] **Step 2:** `---` divider and "Technical detail" heading; then results table + tightened "Reading the numbers" (all facts kept), compact case-study tables (columns: Report, Qtrs before failure, Percentile, Rank / banks, Flagged), a short "What was caught and why" linking `RESULTS.md`, then Limitations, How it works, Run it yourself, Status and roadmap, Reference as today (wording fixes only).
- [ ] **Step 3: Check.** Every number in the old README appears in README.md or RESULTS.md:
```bash
grep -oE '[0-9][0-9,.%$-]*[0-9%]' "$SCRATCH/README.old.md" | sort -u > /tmp-scratch/old.txt
cat README.md RESULTS.md | grep -oE '[0-9][0-9,.%$-]*[0-9%]' | sort -u > new.txt
comm -23 old.txt new.txt   # expected: empty, or only items explained in the report
```
and every relative link target exists (`grep -oE '\]\(([^)#]+)' README.md RESULTS.md` → `ls` each).
- [ ] **Step 4:** Read the top section as a non-specialist and the rest as an engineer; fix meaning drift and unexplained jargon. Preview in Obsidian or `gh markdown-preview` if available.
- [ ] **Step 5:** Daily log entry (what changed and why); commit README.md, RESULTS.md, the spec, the plan, daily-log.md on `readme-layers`.
