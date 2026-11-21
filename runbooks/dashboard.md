# Runbook: the dashboard (Phase 6)

How to refresh the dashboard's data, run it on your machine, and put it on Streamlit Community Cloud. Decision: [[decisions/0023-dashboard]]. Files it reads: [[data-dictionary/dashboard-exports]]. Spec: [[specs/2026-11-19-phase6-dashboard-design]].

The dashboard never calls AWS. Its only paid part is Ask Canary, the corner chat, which calls Anthropic (Claude Haiku 5.5).

## Setup
`pip install -e '.[dev,model,analyst,dashboard]'` (Streamlit 1.67 or newer).

## 1. Re-run the export
Run this whenever the model, the scores or the written notes change. It needs the Phase 3 files in `data/` and the notes in `banks/`, and makes no Claude calls. For the website icons it also reads `data/raw/websites/websites.parquet`; refresh that now and then with `python -m canary.ingest websites` (free FDIC API, one call). Without it the export still works and every bank shows the pixel bank.
```
python -m canary.dashboard export --out dashboard/data
```
It prints each file's size and the folder total, and exits 1 if the folder is over 50 MB. It also fails if a saved agent trace no longer passes the citation checker. Commit the changed files in `dashboard/data/` (these are small and safe to commit; nothing under `data/` ever is).

## 2. Run it locally
```
streamlit run dashboard/app.py
```
Streamlit hot-reloads the files in `dashboard/` but **not** the modules in `src/`. After editing anything in `src/canary/`, stop and restart it.

To try Ask Canary locally, copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` (git-ignored) and put a real key and `ASK_ENABLED = "true"` in it. Without it the corner bird stays off and the rest works.

## 3. Deploy on Streamlit Community Cloud
1. The code and `dashboard/data/` must be on GitHub in the public repo `vfabuluje/Canary`. The root `requirements.txt` (`.[dashboard,model,analyst]`) tells Streamlit what to install. That installs a copy of the `canary` package into site-packages, away from the repo, so `dashboard/app.py` points the loaders at the `dashboard/data/` folder beside itself (`CANARY_DASHBOARD_DATA`).
2. Go to share.streamlit.io, sign in with GitHub, choose **Create app**, and pick the repo `vfabuluje/Canary`, the branch (for example `main`) and the main file path `dashboard/app.py`.
3. Open **Advanced settings** and paste the secrets (below) into the Secrets box. Choose Python 3.12.
4. Deploy. When it is live, put the address in the README where `<!-- LIVE_APP_URL -->` is, and update the roadmap.

Pushing to the chosen branch redeploys the app. A refreshed export is just a new commit of `dashboard/data/`. Cloud installs the `canary` package only once and keeps that copy, so `dashboard/app.py` loads `canary` from the repo's `src/` and reloads it when a push changes any file there (`dashboard/repo_source.py`). If a push still doesn't show up, use **Manage app → Reboot app**.

## Secrets
Two values, set in the app's Secrets box (Settings, Secrets) and never in the repo:
```
ANTHROPIC_API_KEY = "sk-ant-..."
ASK_ENABLED = "false"
```
A placeholder copy is `.streamlit/secrets.toml.example`. `.streamlit/secrets.toml` is git-ignored. Never paste a real key into a file in the repo, a commit, an issue or a chat.

## Ask Canary: turn it on and off
Ask Canary is a small pixel canary in the bottom-right corner of every page. It opens a chat that answers questions about anything in the exported data, using Claude Haiku 5.5 with six read-only lookup tools. Why: [[decisions/0024-ask-canary-chat]]. Its limits: 5 questions per visitor (follow-ups count), 100 a day and $1.00 a day for the whole app, questions up to 300 characters, 4 model calls per attempt, one retry, and 80,000 input tokens per question. Answers are fact-checked against what was looked up in the visit (same citation checker as the reports, plus the link and forecast/advice rules). Nothing is stored. It is **off unless switched on**.
- **On:** set `ASK_ENABLED = "true"` in Secrets and save. The app restarts and the corner bird appears. **Note:** it is currently `true` on the live site, so merging the chat branch switches the live site to the chat at once.
- **Off:** set `ASK_ENABLED = "false"` (or delete the line). The bird disappears and the rest of the app is unaffected.
- **The bird sleeps** (eye closed, z's, "RESTING") when the day's question or dollar limit is reached, or after an API or unexpected error for that visitor. A visitor's own 5-question limit does not put it to sleep.
- **Cost per question:** an estimate for now, under about $0.01 typical and about $0.03 worst case. It is to be measured in a paid smoke test before merge. At 100 questions a day that is about $1 to $3 if the cap is hit daily.
- **The caps are soft:** the daily counts and dollars are kept in the app's memory, so a **reboot, a redeploy or the app going to sleep resets them to zero**; the 5-per-visitor limit resets when the visitor reloads the page.
- **A deploy that changes the bird needs a reboot.** The corner component is registered once per server process, so a change to `chatbird.js` or `chatbird.css` shows up only after Manage app, **Reboot app**. A reboot also resets the daily counters.
- **Spending can never pass the prepaid balance:** keep **auto-reload off** on the Anthropic account, so when the balance is used up the bird rests and nothing more is charged. If a key ever leaks, delete it in the Anthropic console and put a new one in Secrets.

## Ask Canary in the logs
Each question sent to the model writes one line to the app's log (share.streamlit.io, Manage app, the log panel), never the question, the answer or the key:
```
Ask Canary: outcome=answered calls=3 tools=2 cost=$0.00410; today 12/100 questions, $0.0452/$1.00 spent
```
`calls` is model calls, `tools` is lookups. `outcome` is one of:
- `answered`
- `checker_failed` (both tries broke a rule)
- `refusal`
- `truncated` (the reply ran out of tokens)
- `no_text`
- `bad_json`, or `bad_json:<type>` (a reply that broke in some other way, for example `bad_json:KeyError`)
- `turn_limit` (the model used its 4 calls without finishing)
- `token_ceiling` (the question hit 80,000 input tokens)
- `no_submit` (the model ended without submitting an answer)
- `api_error:<type>` (for example `api_error:RateLimitError`; a low balance shows as an API error)
- `error:<type>` (any other unexpected error)

`api_error:` and `error:` put that visitor's bird to sleep. Questions stopped before any call (a guard, or `daily_limit` when the day's cap is reached) are not logged. The day's spend is counted in memory, so it also restarts at zero after a reboot; the Anthropic console has the real total.

## Expanding the showcase
The paid step that writes more reports is in [[runbooks/analyst]], "Expanding the showcase". Never run it without the owner's yes on a fresh dry-run estimate.

## If something goes wrong
- **Export fails on a trace:** a note's saved trace no longer matches the data (for example the facts changed). Re-run that bank's note ([[runbooks/analyst]]), then export again.
- **Folder over 50 MB:** the export refuses; trim what grew before committing.
- **App shows old data on Cloud:** confirm the new `dashboard/data/` files are in the branch the app deploys from, then use Reboot app.
