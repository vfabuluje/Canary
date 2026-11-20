"""Home: the hero, what Canary is, the headline numbers, then the honest miss and links to the rest."""

import streamlit as st

from canary.dashboard import data, theme
from canary.dashboard.copy import HOME_WHAT, HONEST_MISS

metrics = data.metrics()
baseline = metrics["baseline"]

theme.html_block(
    f'<div class="hero">{theme.bird_svg(104)}'
    '<h1 class="title">CANARY</h1>'
    '<div class="tag">Bank Failure Early-Warning System</div></div>'
)

with st.form("home-search", border=False), st.container(key="home-search", horizontal=True, vertical_alignment="bottom"):
    query = st.text_input("Find a bank", key="home-q", placeholder="Find a bank, e.g. SVB", label_visibility="collapsed")
    if st.form_submit_button("SEARCH", type="primary") and query.strip():
        st.switch_page("pages/find.py", query_params={"q": query.strip()})

with st.container(key="home-themes", horizontal=True, vertical_alignment="center"):
    theme.html_block('<span class="theme-label">Theme:</span>')
    theme.theme_buttons("theme-home")

theme.html_block(f'<div class="box what">{theme.bold(HOME_WHAT)}</div>')


def _stat(label: str, big: str, note: str) -> str:
    return f'<div class="box stat"><div class="lab">{label}</div><div class="big">{big}</div><div class="note">{note}</div></div>'


theme.html_block(
    '<div class="stats">'
    + _stat("FAILURES CAUGHT EARLY", f'{metrics["banks_caught"]} <small>of {metrics["eligible_banks"]}</small>',
            "Banks that failed 2016–2024 that Canary flagged up to a year before.")
    + _stat("TYPICAL HEADS-UP", f'{metrics["lead_time_median"]:g} <small>quarters</small>',
            "How far ahead it flagged the typical bank it caught.")
    + _stat("RANKING SCORE", f'{metrics["auc"]:.2f}',
            "How well it sorts risky from safe (1.00 is perfect). The classic rule of thumb, the Texas ratio, "
            f'scores {baseline["auc"]:.2f}.')
    + _stat("FALSE ALARMS", f'{metrics["false_alarm_rate"] * 100:.1f}%',
            "Most flagged banks don't fail. Failures are rare, so a watchlist is mostly “keep an eye on it”.")
    + "</div>"
)

with st.container(key="box-miss"):
    theme.html_block(
        f'<div class="miss">{theme.bird_svg(78, sad=True)}'
        f'<div><h2 class="pix">THE BIG TEST IT FAILED</h2><p>{theme.bold(HONEST_MISS)}</p></div></div>'
    )
    st.page_link("pages/cases.py", label="SEE WHAT IT MISSED ▶")

CARDS = [
    ("find", "pages/find.py", "🔎 FIND A BANK",
     f"Look up any bank's risk rank and history. {len(data.report_certs())} banks have a full written report."),
    ("how", "pages/how.py", "▶ HOW IT WORKS", "Watch the team of AI helpers and fact-checkers build one, step by step."),
    ("watch", "pages/watchlist.py", "🎚 WATCHLIST SIZE",
     "Flag more banks, catch more failures, raise more false alarms. Try it."),
]
for column, (key, target, title, text) in zip(st.columns(3, gap="medium"), CARDS):
    with column, st.container(key=f"box-card-{key}"):
        theme.html_block(f'<h2 class="pix">{title}</h2><p>{text}</p>')
        st.page_link(target, label="OPEN ▶")

theme.footer()
