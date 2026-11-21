# 0024 — Ask Canary becomes one site-wide chat with lookup tools

**Date:** 2026-11-21
**Status:** Accepted (design approved by the owner; built on branch `ask-canary-chat`; paid smoke test and merge still to do)

## Decision
The old Ask box, which sat on the 100 written-report pages and knew one bank, is replaced by **one Ask Canary for the whole site**. It is a small pixel canary in the bottom-right corner of every page. Click it and a chat opens. It can answer questions about anything in Canary's exported data. In plain English:

- **Six lookup tools, all read-only.** The AI model (Claude Haiku 5.5, low effort) does not get a fixed fact sheet. It gets six tools over `dashboard/data/` and decides what to look up: `find_bank`, `bank_profile`, `bank_report` (a slim fact list, no report text), `failures`, `watchlist` and `canary_facts`. Lists are capped (25 rows, 12 quarters, 8 search matches). Each tool returns numbered facts.
- **Every number is checked.** The answer must pass the same citation checker as the reports, against the facts looked up in this visit. It must also pass the link rule and the forecast and advice rule (it allows "not a prediction" and "warning signs", and rejects "likely to fail" and "you should withdraw"). If the check fails, the model gets **one retry**. If that fails too, the visitor sees "I couldn't answer that with checked facts."
- **What it cannot answer:** bank sizes (the export has no size column), credit unions (NCUA, not FDIC), news, stock advice and forecasts. It says so politely.
- **Limits:** 5 questions per visit (follow-ups count), 100 a day for the whole app, **$1.00 a day** for the whole app, 300 characters a question, 4 model calls per attempt, one retry, at most 4 lookups per model reply and 3 written reports per question, and a token ceiling checked **before** every call: the call's size is projected (the last call's tokens plus the new lookup results at about 3 characters a token) and it is not sent if it would take the question past 80,000 input tokens in all (retry included) or is over 100,000 by itself (where Haiku's long-prompt rate of $0.50 / $2.50 per million starts; the cost counter prices it too). Past the ceiling the question stops with "I couldn't answer that one. Try asking it another way."
- **The bird sleeps** (eye closed, z's, "RESTING") when the day's question or dollar limit is reached, for the rest of the UTC day after a key, permission or credit-balance error, or after any other API or unexpected error for that visitor. A question that fails on its own (refused, cut off, malformed, never submitted, out of turns or over the token ceiling) leaves the bird awake and says "I couldn't answer that one. Try asking it another way." A visitor who reaches their own 5-question limit sees the bird awake with a note instead.
- **Same switch.** `ASK_ENABLED` and `ANTHROPIC_API_KEY` in Streamlit secrets work as before. The switch now shows or hides the corner bird. **Auto-reload stays off** on the Anthropic account, so the prepaid balance is still the hard ceiling. Nothing is stored. The counters live in memory and reset on a reboot, redeploy or sleep.
- **One log line per question:** outcome, model calls, tool calls, cost, and today's count and spend. Never the question, the answer or the key. Format and outcomes: [[runbooks/dashboard]].

## Why
- **Site-wide, because the owner wanted depth.** A real tool-using agent on the public site is more convincing than a box on 100 pages, and it is the centrepiece of the demo video and post.
- **Tools instead of a fixed fact sheet.** The alternative was code that guesses which banks you mean, attaches their facts and makes one call. That is cheaper (about $0.003 to $0.005) but cannot answer what the code did not plan for: "which Texas banks are on the watchlist?", "compare SVB and Signature", "which banks failed in 2010?". Tools can. They cost about three times as much per question, which the caps absorb.
- **A Streamlit v2 component for the bird, not a popover.** The component renders in the page itself (no iframe), so a fixed corner widget can float over every page, it matches the pixel mockup, and typing does not redraw the page. Streamlit's own popover or dialog would look like Streamlit, open as a centred modal and redraw on every keystroke.
- **Slim facts, no report text.** `bank_report` sends only the fact id, label, quarter, display and hindsight flag (about 9,000 tokens for SVB), not the full table and the 39 KB note. The checker still uses the full facts in Python. This keeps each turn of the tool loop small.
- **Follow-ups carry only earlier questions, answers and the facts they cited**, not the full tool results, so a long visit does not grow without limit.
- **A dollar limit as well as a count.** The owner cut the day from 300 questions to 100 and added $1.00. A question already running may finish, so a day can end slightly over $1.

## Cost
An estimate only, not yet measured: **under about $0.01 a typical question, about $0.03 worst case** (two banks' reports and a retry). At 100 a day that is about $1 to $3 if the cap is hit every day. The old box measured about $0.003 a question. A paid smoke test of about 10 questions (a lookup, a follow-up, a watchlist by state, an off-topic question, forecast bait, a prompt-injection attempt) runs before merge, with the owner's yes on its estimate. Its measured cost replaces this estimate here and in the README. If the typical cost is above $0.02 a question, stop and ask the owner before merging.

## Alternatives rejected
- **Code picks the facts, one call:** cheaper, but cannot answer unplanned questions.
- **Native Streamlit popover or dialog:** less code, but it looks generic and redraws as you type.
- **Keeping 300 questions a day:** the owner chose 100 plus $1.00 for a tighter ceiling.

## Consequences
- **Merging switches the live site to the chat at once**, because `ASK_ENABLED` is already true there.
- **A deploy that changes the bird needs no reboot.** `chatbird.js` and `chatbird.css` are under `src/`, so a push that changes them makes `dashboard/repo_source.py` drop the loaded `canary` modules; the re-imported `chatbird` registers the component again, which replaces the old JS and CSS. The same re-import starts the in-memory daily counters from zero, as a reboot does.
- New outcomes appear in the logs: `turn_limit`, `token_ceiling`, `no_submit`, `error:<Type>` and `api_error:<Type>:account`. Questions stopped by the daily limit are not logged.

Replaces the Ask paragraph of [[decisions/0023-dashboard]]. Design: [[specs/2026-11-21-ask-canary-chat-design]]. Run and manage: [[runbooks/dashboard]].
