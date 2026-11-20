# 0023 — A read-only Streamlit dashboard on exported files, with a capped Ask Canary

**Date:** 2026-11-20
**Status:** Accepted (design approved by the owner; built in Phase 6, not yet deployed)

## Decision
Canary gets a public web dashboard, built with **Streamlit** and hosted free on **Streamlit Community Cloud**. In plain English:

- **What it is.** A web page where anyone can look up a bank, see how Canary ranked it over time, read the 2023 stories (SVB, Signature, First Republic), see how the size of the watchlist trades failures caught against false alarms, and, for the showcase banks, watch the three AI agents "write" the report and then read it. Tabs: Home, Find a bank, 2023, Watchlist, How it works, Why Canary.
- **Read-only.** Visitors cannot change anything. The one exception is **Ask Canary**.
- **Ask Canary.** On each written-report page, a visitor can ask a question about that bank. Each question is one Claude call on the cheap **Claude Haiku 5.5** model, sent only that bank's fact sheet and note, plus one retry call if the first answer fails the check, so **up to 2 calls per question**. The answer goes through the same citation checker as the memos, plus a check for prediction and advice wording; if it does not pass after the retry it says it could not answer with checked facts. Guards: **5 questions per visitor, 300 a day for the whole app**, questions up to 300 characters, nothing stored. It is **off by default** (a switch in the app's secrets), the key lives only in Streamlit's secrets, and **auto-reload stays off on the Anthropic account**, so spending can never pass the prepaid balance. When a cap or the balance is hit the box says it is resting and the rest of the app carries on. The caps are soft: the daily counter lives in the app's memory, so a reboot, a redeploy or the app going to sleep resets it, and the per-visitor limit resets when the visitor reloads the page. **The prepaid balance, with auto-reload off, is the hard ceiling.**
- **Exported files, not the pipeline data.** The app reads a small folder of files, `dashboard/data/`, made by `python -m canary.dashboard export`. It never touches AWS, the warehouse, the model or `data/`. Formats: [[data-dictionary/dashboard-exports]].
- **Look and feel.** The pixel-art "v6" style, with three themes the visitor can switch between: Standard (grey), Detectives, and Basketball. The themes change the page and the cast of characters, not the numbers.
- **Showcase plan.** The report replay and report page exist for the 61 banks that already have written notes. A separate, paid step, only with the owner's yes, writes 39 more with the existing three-agent pipeline, as of 2026-06-30: the 20 largest banks people will search, plus 19 more from today's watchlist, for **100 banks**. Its free dry run (2026-11-20, `--watchlist-top 40 --skip-done`) estimates **$9.02 in the worst case**: $5.49 for first tries plus a $3.53 allowance for retries. That is over the planned $7.00 limit (a run with that limit refuses to start) and over the current prepaid balance of $8.06, so the owner decides the limit, a top-up or a smaller set before any run ([[runbooks/analyst]], "Expanding the showcase"). The dashboard works with 61 or 100. Every other bank still gets a page, with its score history and real-estate concentration check, but no written report and no Ask box.

Code: `dashboard/app.py`, `dashboard/views/`, `src/canary/dashboard/`. Run and deploy: [[runbooks/dashboard]]. Design: [[specs/2026-11-19-phase6-dashboard-design]].

## Why
- **Free and simple to host.** Streamlit Community Cloud serves a public GitHub repo for nothing and keeps secrets out of the code. Search and data handling are simpler in Python than in a hand-built static site, which the owner rejected for that reason.
- **Exported files keep it safe and light.** The app has no credentials to the owner's AWS account and cannot reach private data. The files are small (the export fails above 50 MB), can be committed, and the export refuses to run if a saved agent trace no longer passes the citation checker, so the page cannot show a number the checker would reject.
- **Haiku with hard caps keeps Ask Canary cheap and bounded.** About $0.002 a call, so 300 questions a day is about $0.60, and about $1.20 in the worst case where every question needs its retry. The counters reset on a reboot or redeploy, so a prepaid balance with auto-reload off is the final backstop.
- **Honesty stays visible.** The dashboard repeats the project's stance: a research tool, not financial advice; the model missed SVB, Signature and First Republic; the watchlist is mostly false alarms.

## Alternatives rejected
- **A plain static site:** harder to do search and data work in; the owner chose Streamlit.
- **A modern "professional" look:** the owner rejected it after a full draft in favor of the pixel style.
- **Reading the warehouse or `data/` from the live app:** needs credentials in a public app and is slow; exported files avoid both.
- **Ask Canary always on, or with auto-reload:** risks open-ended spend.

## Consequences
- The data is a snapshot: after any new scores or notes, re-run the export and commit it.
- Streamlit does not hot-reload `src/` modules; restart after editing them.
- Deployment is a manual, one-time setup on share.streamlit.io; until then the README link is a placeholder.
