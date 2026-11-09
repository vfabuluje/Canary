# 0001 — Git repo setup and what we don't commit

**Date:** 2026-11-09
**Status:** Accepted

## Decision
The Obsidian vault folder is also the git repo, published as a public GitHub repo (`vfabuluje/Canary`) on branch `main`.

`.gitignore` excludes:
- **Secrets:** `.env`, `.env.*` (but keeps `.env.example`), `*.pem`, `.aws/`. API keys and AWS credentials must never reach a public repo.
- **Python/dbt build output:** `__pycache__/`, virtual envs, test caches, dbt `target/`, `logs/`. These are regenerated automatically and only add noise.
- **`data/`:** raw FDIC/FFIEC downloads are large and can be re-pulled from public sources (or live in S3). Git is for code and notes, not datasets.
- **Obsidian per-device state:** `.obsidian/workspace*.json` (which notes/panes are open). It changes every time the vault is opened, so it would create pointless diffs. Shared settings (`app.json`, `core-plugins.json`, `appearance.json`) *are* committed so the vault looks the same on any machine.

Commits use the GitHub noreply email so a personal email isn't exposed in the public history.

## Why
Keeps the public repo clean, small, and safe: only code, notes, and config that someone else would need to reproduce the project.
