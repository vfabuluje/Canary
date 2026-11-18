# 0017 — The `ask` agent runs on the SDK tool runner

**Date:** 2026-11-17
**Status:** Accepted (owner's choice)

## Decision
`python -m canary.analyst ask "..."` answers plain-English questions with an agent built on the Anthropic Python SDK's **tool runner** (`client.beta.messages.tool_runner`). Claude picks a tool, Canary's own Python runs it, the result goes back, and this repeats until Claude answers. The loop runs on the owner's machine. Code: `src/canary/analyst/agent.py`, `tools.py`.

## Options
- **Tool runner (chosen).** Pay only for tokens, no session history kept, the whole loop is code the owner can read, and it can be tested with a fake Claude client.
- **Claude Managed Agents.** Anthropic hosts the loop. It is in beta, bills for session time as well as tokens, and keeps session history on Anthropic's side. More than a small project needs, and harder to explain line by line.

The owner chose the tool runner on 2026-11-17 for simplicity, testability and explainability. Managed Agents stays an option for a *scheduled* agent later (Phase 5 follow-ups).

## The four tools (all local Python reading the same data)
- `find_bank(query, state?, failed_year?)`: by name, state or cert for any bank. **City search works for failed banks only**, because city is in the failures file but not in the financials. Up to 10 matches.
- `get_bank_facts(cert, as_of?)`: the same fact sheet the memo writer uses, so answers use checked facts.
- `list_watchlist(quarter?)`: the top 2% for a quarter, with ranks.
- `write_memo(cert, as_of?)`: runs the memo writer and citation checker ([[decisions/0016-analyst-memo-design]]) and returns the saved path.

## Guardrails
- **Memos only through the checked writer.** The agent cannot write a note file itself; `write_memo` is the only way, so every saved note passed the checker.
- **At most 10 tool iterations** per question (`MAX_ITERATIONS`); then the answer ends with "(Stopped after 10 steps without a final answer.)".
- The system prompt says: answer only from tool results, list matches and ask when several banks match, describe banks by rank, never as a probability. The chat answer itself is not saved and not citation-checked, only the memos it writes are.
- A refusal returns a short fixed line instead of an error.

Usage and cost are printed to stderr after each answer (memos the agent writes are not counted there). Runbook: [[runbooks/analyst]].
