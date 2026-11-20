# Runbook: the dashboard (Phase 6)

How to refresh the dashboard's data, run it on your machine, and put it on Streamlit Community Cloud. Decision: [[decisions/0023-dashboard]]. Files it reads: [[data-dictionary/dashboard-exports]]. Spec: [[specs/2026-11-19-phase6-dashboard-design]].

The dashboard never calls AWS. Its only paid part is Ask Canary, which calls Anthropic (Claude Haiku 5.5).

## Setup
`pip install -e '.[dev,model,analyst,dashboard]'` (Streamlit 1.67 or newer).

## 1. Re-run the export
Run this whenever the model, the scores or the written notes change. It needs the Phase 3 files in `data/` and the notes in `banks/`, and makes no Claude calls.
```
python -m canary.dashboard export --out dashboard/data
```
It prints each file's size and the folder total, and exits 1 if the folder is over 50 MB. It also fails if a saved agent trace no longer passes the citation checker. Commit the changed files in `dashboard/data/` (these are small and safe to commit; nothing under `data/` ever is).

## 2. Run it locally
```
streamlit run dashboard/app.py
```
Streamlit hot-reloads the files in `dashboard/` but **not** the modules in `src/`. After editing anything in `src/canary/`, stop and restart it.

To try Ask Canary locally, copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` (git-ignored) and put a real key and `ASK_ENABLED = "true"` in it. Without it the Ask box stays off and the rest works.

## 3. Deploy on Streamlit Community Cloud
1. The code and `dashboard/data/` must be on GitHub in the public repo `vfabuluje/Canary`. The root `requirements.txt` (`.[dashboard,model,analyst]`) tells Streamlit what to install. That installs a copy of the `canary` package into site-packages, away from the repo, so `dashboard/app.py` points the loaders at the `dashboard/data/` folder beside itself (`CANARY_DASHBOARD_DATA`).
2. Go to share.streamlit.io, sign in with GitHub, choose **Create app**, and pick the repo `vfabuluje/Canary`, the branch (for example `main`) and the main file path `dashboard/app.py`.
3. Open **Advanced settings** and paste the secrets (below) into the Secrets box. Choose Python 3.12.
4. Deploy. When it is live, put the address in the README where `<!-- LIVE_APP_URL -->` is, and update the roadmap.

Pushing to the chosen branch redeploys the app. A refreshed export is just a new commit of `dashboard/data/`.

## Secrets
Two values, set in the app's Secrets box (Settings, Secrets) and never in the repo:
```
ANTHROPIC_API_KEY = "sk-ant-..."
ASK_ENABLED = "false"
```
A placeholder copy is `.streamlit/secrets.toml.example`. `.streamlit/secrets.toml` is git-ignored. Never paste a real key into a file in the repo, a commit, an issue or a chat.

## Ask Canary: turn it on and off
Ask Canary (built in Phase 6 Task 10) answers questions on the report pages with Claude Haiku 5.5, about $0.002 a question. Its guards: 5 questions per visitor, 300 a day for the whole app, questions up to 300 characters, answers fact-checked by the same citation checker (plus a check for prediction and advice wording), nothing stored. It is **off by default**.
- **On:** set `ASK_ENABLED = "true"` in Secrets and save. The app restarts.
- **Off:** set `ASK_ENABLED = "false"` (or delete the line). The box disappears and the rest of the app is unaffected.
- **Cost per question:** one call, or two when the first answer fails the check and is retried, so the worst case is about twice the daily estimate (about $1.20 for 300 questions instead of $0.60).
- **The caps are soft:** the daily counter (300) is kept in the app's memory, so a **reboot, a redeploy or the app going to sleep resets it to zero**; the 5-per-visitor limit resets when the visitor reloads the page.
- **Spending can never pass the prepaid balance:** keep **auto-reload off** on the Anthropic account, so when the balance is used up the box says "Ask Canary is resting for today" and nothing more is charged. If a key ever leaks, delete it in the Anthropic console and put a new one in Secrets.

## Ask Canary in the logs
Each question writes one line to the app's log (share.streamlit.io, Manage app, the log panel), never the question, the answer or the key:
```
Ask Canary: outcome=answered calls=1 cost=$0.00110; today 12/300 questions, $0.0152 spent
```
`outcome` is `answered`, `checker_failed` (both tries broke a rule), `refusal`, `truncated` (the reply ran out of tokens), `no_text`, `bad_json`, `bad_json:<type>` (a reply that broke in some other way, for example `bad_json:KeyError`) or `api_error:<type>` (for example `api_error:RateLimitError`; a low balance shows as an API error). The day's spend is counted in memory, so it also restarts at zero after a reboot; the Anthropic console has the real total.

## Expanding the showcase
The paid step that writes more reports is in [[runbooks/analyst]], "Expanding the showcase". Never run it without the owner's yes on a fresh dry-run estimate.

## If something goes wrong
- **Export fails on a trace:** a note's saved trace no longer matches the data (for example the facts changed). Re-run that bank's note ([[runbooks/analyst]]), then export again.
- **Folder over 50 MB:** the export refuses; trim what grew before committing.
- **App shows old data on Cloud:** confirm the new `dashboard/data/` files are in the branch the app deploys from, then use Reboot app.
