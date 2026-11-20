"""Canary dashboard: the app shell. Run with `streamlit run dashboard/app.py` from the repo root."""

import os
import sys
from pathlib import Path

import streamlit as st

# Run the repo's current `canary` code, not the copy Streamlit Cloud installed at first deploy (repo_source.py).
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from repo_source import use_repo_source  # noqa: E402

use_repo_source(HERE.parent / "src")

from canary.dashboard import theme  # noqa: E402
from canary.dashboard.data import DATA_ENV  # noqa: E402

# The exported data sits beside this file. Pinning it here means the app finds it however the package was
# installed (requirements.txt installs a copy into site-packages, away from the repo). Tests set it first.
os.environ.setdefault(DATA_ENV, str(HERE / "data"))

st.set_page_config(page_title="Canary: bank failure early warning", page_icon="🐤", layout="wide")
st.logo(theme.bird_svg(26), link=None)

PAGES = [
    st.Page("views/home.py", title="Home", default=True),
    st.Page("views/find.py", title="Find a bank", url_path="find"),
    st.Page("views/cases.py", title="2023", url_path="cases"),
    st.Page("views/watchlist.py", title="Watchlist", url_path="watchlist"),
    st.Page("views/how.py", title="How it works", url_path="how"),
    st.Page("views/why.py", title="Why Canary", url_path="why"),
]

theme.apply_theme()
theme.theme_picker()
st.navigation(PAGES, position="top").run()
