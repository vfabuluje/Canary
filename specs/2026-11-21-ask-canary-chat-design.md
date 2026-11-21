# Ask Canary chat: one site-wide chat behind a corner canary

Date: 2026-11-21. Status: approved by Victor 2026-11-21. Mockups: https://claude.ai/artifact/Bvv2p4yyPa1hMYGnYk8EnX (private; option **A1**, "real size" section, and the chat panel).

## 1. Intent

Today Ask Canary is a question box under the replay on the 100 written-report pages, and it can only answer about that one bank. Victor wants **one Ask Canary for the whole site**: a small pixel canary in the bottom-right corner of every page that opens a chat about anything in Canary's data.

**Why:** to give the project depth (a real tool-using AI agent on the public site, not just a box) and to be a centrepiece of the demo video and LinkedIn post.

## 2. Goals, non-goals, anti-goals

**Goals**
- A visitor on any page can click the canary and ask about: any bank in the data (11,243, including closed ones), its risk rank history, the watchlist in any quarter, the 2023 failures, the model's results, and how Canary works. They can ask follow-ups within the visit.
- Every number in an answer is checked against facts Canary's own data returned for this conversation, as the reports and today's box are.
- It looks like the mockup: option A1 at the "real size" (see section 5).
- Its cost stays small and bounded. The prepaid balance is about $7.11 and the owner is cost-sensitive.

**Non-goals**
- No memory across visits, accounts or saved chats. Nothing is stored.
- No new data, no web search and no outside knowledge. It doesn't write new reports (the CLI `ask` agent's `write_memo` tool is **not** offered).
- No streaming of answer text word by word.

**Anti-goals (a failure even if it works)**
- It forecasts or advises ("X will fail", "move your money") or gives a number the data doesn't contain.
- It's noisy or big: a bird that covers content, chirps constantly, or nags.
- Spend can run past what Victor expects. A visitor must not be able to make it loop.

## 3. Constraints

- The live app runs on Streamlit Community Cloud with Streamlit 1.67. The `canary` code is loaded from the repo's `src/` (`dashboard/repo_source.py`).
- It reads only `dashboard/data/` (banks, scores history, concentration, metrics, threshold, case studies, the 100 report JSONs with their fact tables). No warehouse or AWS access.
- Model: **Claude Haiku 5.5** (`claude-haiku-5-5`, $0.10 / $0.50 per million input/output tokens per `PRICES` in `canary/analyst/writer.py`). Same key, `ANTHROPIC_API_KEY`, in Streamlit secrets.
- Owner rules: show a dry-run estimate and get approval before any paid run; keep auto-reload off; never commit or print the key.
- The safety rules already built for Ask stay: the citation checker (`check_memo`), the link check, the forecast/advice wording rule with its allowed caveats and allowed "whether … will fail" refusals (PRs #17 and #18), untrusted-question handling, and a question limit of 300 characters.

## 4. Approaches considered

**How it answers**
- **A. Agent with lookup tools (chosen).** Haiku gets a few read-only tools over `dashboard/data/` and decides what to look up. Every tool returns numbered facts, and the checker verifies the answer against all facts returned so far in the conversation. It handles unplanned questions ("which Texas banks are on the watchlist?", "compare SVB and Signature", "which banks failed in 2010?") and can show what it looked up. It costs about $0.01 a question (estimate, see section 8), about 3× today's measured $0.003.
- **B. Code picks the facts, one call.** Code finds bank names with the existing search and attaches those banks' facts, the current page's bank and the latest watchlist. It's cheaper ($0.003–0.005) and reuses today's checker almost as-is, but can't answer anything the code didn't anticipate (state filters, old quarters, "failures in 2010"). That works against "chat about anything in the data". Rejected.

**How it's drawn**
- **A. A Streamlit v2 custom component (chosen).** `st.components.v2.component` in 1.67 is two-way (JS ↔ Python) and renders in the page itself inside a shadow root, not an iframe, so a `position: fixed` corner widget can float over the page. It gives full control of the hop, tweet and panel, matches the mockup, and opening or typing doesn't redraw the page.
- **B. Native `st.popover` or `st.dialog` plus `st.chat_input`, pinned with CSS.** Less code, but it looks like Streamlit rather than the mockup, the dialog is a centred modal, and typing redraws the page. Rejected.

**Budget:** Victor chose **100 questions a day** (down from 300), a **$1 a day** spending limit, and kept 5 per visit.

## 5. What the visitor sees (decided)

**The corner canary (option A1)**
- Bottom-right of **every page**, above page content (but below Streamlit's own top bar and menus). It's the site's pixel bird (`theme.BIRD`) drawn crisply at whole-pixel scale.
  - Computer: bird **39px** wide (3 screen px per sprite pixel), with a yellow speech-bubble button saying **"ASK CANARY"** with a small blinking orange dot. Whole button about 140 × 40px.
  - Phone (narrow screens): bird **26px** (2 px per sprite pixel), bubble says **"ASK"**. **The tappable area stays at least 44px tall.**
- The bubble has the v6 look: yellow fill, navy 2px border, hard navy shadow, Press Start 2P text.
- **Hop and tweet:** the bird hops and a small "tweet!" appears every few seconds until the visitor has opened the chat once this visit. After that, only occasionally (about once a minute). Never while the panel is open, and never with "reduce motion" on (then it's still, and "tweet!" isn't shown).
- **Asleep when resting (Victor, 2026-11-21):** when Ask Canary is resting (the daily question or dollar limit is reached, the balance is used up, or an API error made it rest), the corner bird goes to sleep: its eye closes (the eye pixel becomes a short line) and pixel **"z z Z"** float up beside its head, growing as they rise. It doesn't hop or tweet, the blinking dot is gone, and the bubble says **"RESTING"** ("ZZZ" on phones). Clicking still opens the panel, which shows the sleeping bird and "Ask Canary is resting for today." With "reduce motion" on, the z's stay still. The visitor's own 5-per-visit limit is not "asleep": the bird stays awake and the panel says they've used their questions for this visit.
- The three themes don't change the button or the panel. Cards stay white with navy borders in every theme, as now.
- Hidden entirely when Ask is switched off or has no key (same rule as today, ruling R22).

**The chat panel (as in the mockup)**
- Opens above the bird. About 400px wide on a computer. On a phone it fills the width as a sheet from the bottom (builder's call on exact height). It has a navy header with the small bird, "ASK CANARY" and a close X, plus Escape to close.
- **First open:** a greeting from the bird ("Tweet! I know every FDIC bank's risk rank since 2016 and the written reports for 100 banks. What do you want to know?") and **three starter questions** as chips. On a bank's page the first chip is about that bank (for example "Why wasn't SVB flagged?"); elsewhere they're general ("Who's on the watchlist now?", "How does the score work?", "Why didn't Canary flag SVB?"). A chip sends its question.
- **Each answer** is plain sentences in a white bubble from the bird. Under it, a grey source line lists the bank(s), quarter(s) and key numbers it used, built by code from the cited facts (not written by the model).
- **While it works:** the bird shows a "thinking" state (for example a hop loop and "…"). If the component can be updated mid-run, it shows the lookups as they happen ("Looking up Signature Bank…"). If not, it shows them after the answer as a "What I looked up" line. Builder checks which is possible; either is acceptable.
- Footer: "N questions left this visit · Research tool, not financial advice."
- Visitors' questions show in yellow bubbles. The input is limited to 300 characters with an ASK button, and Enter sends.
- When resting (cap reached, balance used, an API error): the bird says "Ask Canary is resting for today." The rest of the site is unaffected.

**It knows which page you're on.** The current page (and, on a bank page, the bank's name and cert) is passed with each question, so "why wasn't it flagged?" on SVB's page means SVB.

**The per-bank box goes away.** `askbox.py`'s box is removed from report pages. The chat replaces it.

## 6. How it answers (decided in outline)

**Tools** (six, read-only, over `dashboard/data/`, each returning JSON with numbered facts in the same shape as report facts: `id, label, quarter, value, display, forms, hindsight, source, feature, kind`):
1. `find_bank(query, state=None)`: the existing dashboard search (`search.py`, with nicknames and ranking), up to 8 matches: name, cert, city, state, status (active, failed on date, or closed), whether it has a written report.
2. `bank_profile(cert)`: identity and status, latest rank / banks / percentile / flagged, score history (latest 12 quarters by default, or an asked range, capped), and the latest concentration check. Banks never scored (stopped reporting before 2016) say so, with the reason the site gives.
3. `bank_report(cert)`: for the 100 report banks, the report's headline and a **slim** fact table: only `id, label, quarter, display, hindsight` per fact (about 34 KB, roughly 9k tokens for SVB's 199 facts, against about 80 KB for the full JSON). The checker still uses the full facts on the Python side. The written note (`note_md`, about 39 KB) is **not** sent; the facts carry the numbers, and `canary_facts` carries the "why the model missed 2023" story. *(Claude's call after the builder check; today's box sends the full table plus `note_md`, which is too big to resend on every turn of a tool loop.)* For other banks it returns an error saying there's no written report.
4. `failures(year=None, state=None)`: banks that failed (FDIC closures in the data), by year and/or state, sorted by date, capped at about 25 rows plus the total count. So "Which banks failed in 2023?" lists all five: SVB, Signature, First Republic, Citizens Bank (cert 8758) and Heartland Tri-State (cert 25851). *(Claude's call.)* "Biggest" can't be answered: the export has no size column, and none is added. The model says it can't tell.
5. `watchlist(quarter=None, state=None)`: the flagged banks that quarter (latest by default), sorted by rank, capped at about 25 rows plus the total count.
6. `canary_facts()`: the model's test results (`metrics.json`), the 2023 case-study summary, the flag threshold, and fixed plain-English text on how the score works and what it isn't (from `copy.py`, so it matches the site).

Fact ids are unique across the whole conversation (F1, F2, … continuing over turns), so a cite always means one fact. **Follow-ups carry forward only each earlier turn's question, answer text and the facts it cited**, not the full tool results; the model looks things up again if it needs more. This keeps later questions from growing without limit. *(Claude's call.)*

**One question, step by step**
1. Guards first (section 7). Nothing is sent if a guard says no.
2. The tool loop (Haiku 5.5, low effort, like the CLI `ask` agent's `tool_runner`) with the system prompt below, the current-page line, the conversation so far and the new question in `<question>` tags. At most **4 model turns** per attempt. Then a final answer in the existing answer JSON shape (sentences with cites).
3. Code checks the answer against all facts returned so far: `check_memo`, the link check, the forecast/advice wording rule, and a non-empty answer. The same rules and allowed caveats as today.
4. If the check fails, **one retry** with the checker's errors, reusing the facts already fetched (no new lookups needed). If that still fails: "I couldn't answer that with checked facts."
5. A refusal, a truncated reply, malformed JSON, hitting the turn limit or an API error shows the resting line, as today's outcomes.

**System prompt:** adapted from today's `ask.SYSTEM_PROMPT` rules 1–11, changed from "this bank" to "Canary's data, through the tools". It adds: look things up rather than guess; if the tools don't have it, say "I can't tell from Canary's data" plus what it does show; small talk is fine in one short sentence but steer back to the data; anything outside the data (credit unions, stock picks, news) gets a polite "that's outside what Canary covers".

## 7. Guards and spending (decided)

- **$1 a day spending limit** for the whole app (Victor, 2026-11-21): once the day's counted spend (`DailyCounter`'s running total) reaches $1.00, no new question is sent and the bird says "Ask Canary is resting for today." A question already running may finish, so a day can end slightly over $1. Same in-memory reset as the counts.
- **5 questions per visit** (follow-ups count) and **100 questions a day** for the whole app, both as today (in memory; reset on reboot, redeploy or sleep; the per-visit count resets on reload).
- At most 4 model turns per attempt and one retry attempt, so a single question is bounded in calls. Add a **per-question token ceiling**, counted as input tokens summed over every call for that question, the retry included. The builder sets it from measurements; a starting point is 80k (about $0.008 at Haiku's input price). Over it, the loop stops with the resting line.
- Questions up to 300 characters. Conversation history sent to the model is the visit's earlier questions, answers and facts (5 questions at most, so bounded).
- `ASK_ENABLED` and `ANTHROPIC_API_KEY` in secrets, unchanged: the switch now shows or hides the corner bird.
- **Auto-reload off** stays the hard ceiling.
- **Log line per question**, as today: outcome, calls, tool calls, cost, and today's count and spend. Never the question, answer or key.

## 8. Cost (estimate, to be measured)

- Today's box measured about $0.003 a question (one call, one fact sheet, Haiku thinking).
- The chat makes about 2–4 calls per question with growing context. The flagship "Why didn't Canary flag SVB?" (find_bank, bank_report with 9k tokens of slim facts, the answer) comes to roughly 25–30k input tokens over three calls: about $0.003, plus about $0.001 of output. **Estimate under $0.01 typical, worst case about $0.03** (two banks' reports and a retry). At 100 a day that's about $1–3 a day if the cap is hit daily. The $7.11 balance covers about 500–700 typical questions.
- **Paid smoke test before merge, with Victor's OK on its estimate:** about 10 questions covering a bank lookup, a follow-up, the watchlist by state, a page-context question, an off-topic question, a forecast-bait question and a prompt-injection attempt. Expected under $0.30. The measured cost per question goes into the decision and README. **Merge bar:** if the measured typical cost is above $0.02 a question, stop and come back to Victor before merging.

## 9. Rollout

- **Important:** `ASK_ENABLED` is **true** on the live site now (the per-bank box is live). Merging this switches the live site to the chat at once, so the paid smoke test runs locally before merge, and Victor decides when to merge.
- Docs: a new decision `decisions/0024-ask-canary-chat.md` (why site-wide, why tools, the guards, cost); update decision 0023's Ask paragraph to point to 0024; `runbooks/dashboard.md` (the Ask section: what the switch does now, the caps, the log line, the outcomes); README (Dashboard section, cost total after the smoke test); data dictionary only if a new export is added (not expected); daily log; roadmap.
- Tests: tools (facts and caps; unscored banks; banks without a report; state filter); fact ids across turns; guards (per-visit, daily, length, turn limit, token ceiling); the check and retry with fake clients (as `tests/analyst_fakes.py` does); the forecast/advice and injection cases from PRs #17–#18 carried over; component wiring (Python side: payload and the returned question); the old box is gone from report pages. The full suite still passes.

## 10. Left to the builder

- The exact component code, the progress display mechanism (live versus after the answer), the phone sheet height, and animation timing within the rules above.
- Whether the tool runner can return the structured answer JSON directly, or whether a final no-tools call or a JSON-in-text parse is needed. Check against the current Anthropic SDK (`anthropic` 1.17) and the claude-api reference before writing it.
- The token ceiling value, and the exact starter-question wording (Victor may tweak it).
- First step: a **throwaway spike** proving a v2 component can float fixed in the corner on the live Streamlit version and send a question to Python and get an answer back, before building the rest.
