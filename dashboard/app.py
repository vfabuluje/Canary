"""Canary dashboard: the app shell. Run with `streamlit run dashboard/app.py` from the repo root."""

import os
from pathlib import Path

import streamlit as st

from canary.dashboard import theme
from canary.dashboard.data import DATA_ENV

# The exported data sits beside this file. Pinning it here means the app finds it however the package was
# installed (requirements.txt installs a copy into site-packages, away from the repo). Tests set it first.
os.environ.setdefault(DATA_ENV, str(Path(__file__).resolve().parent / "data"))

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
