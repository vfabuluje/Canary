"""Home: the hero, what Canary is, the headline numbers, then the honest miss and links to the rest."""

import streamlit as st

from canary.dashboard import data, theme
from canary.dashboard.copy import HOME_CARDS, HOME_STATS, HOME_WHAT, HONEST_MISS

metrics = data.metrics()

theme.html_block(
    f'<div class="hero">{theme.bird_svg(104)}'
    '<h1 class="title">CANARY</h1>'
    '<div class="tag">Bank Failure Early-Warning System</div></div>'
)

with st.form("home-search", border=False), st.container(key="home-search", horizontal=True, vertical_alignment="bottom"):
    query = st.text_input("Find a bank", key="home-q", placeholder="Find a bank, e.g. SVB", label_visibility="collapsed")
    if st.form_submit_button("SEARCH", type="primary") and query.strip():
        st.switch_page("views/find.py", query_params={"q": query.strip()})

with st.container(key="home-themes", horizontal=True, vertical_alignment="center"):
    theme.html_block('<span class="theme-label">Theme:</span>')
    theme.theme_buttons("theme-home")

theme.html_block(f'<div class="box what">{theme.bold(HOME_WHAT)}</div>')


BIG = {
    "caught": f'{metrics["banks_caught"]} <small>of {metrics["eligible_banks"]}</small>',
    "lead": f'{metrics["lead_time_median"]:g} <small>quarters</small>',
    "auc": f'{metrics["auc"]:.2f}',
    "false_alarm": f'{metrics["false_alarm_rate"] * 100:.1f}%',
}


def _stat(key: str) -> str:
    label, note = HOME_STATS[key]
    return (f'<div class="box stat"><div class="lab">{label}</div><div class="big">{BIG[key]}</div>'
            f'<div class="note">{note.format_map(metrics)}</div></div>')


theme.html_block('<div class="stats">' + "".join(_stat(key) for key in BIG) + "</div>")

with st.container(key="box-miss"):
    theme.html_block(
        f'<div class="miss">{theme.bird_svg(78, sad=True)}'
        f'<div><h2 class="pix">THE BIG TEST IT FAILED</h2><p>{theme.bold(HONEST_MISS)}</p></div></div>'
    )
    st.page_link("views/cases.py", label="SEE WHAT IT MISSED ▶")

CARD_TARGETS = {"find": "views/find.py", "how": "views/how.py", "watch": "views/watchlist.py"}
report_count = len(data.report_certs())
for column, (key, target) in zip(st.columns(3, gap="medium"), CARD_TARGETS.items()):
    title, text = HOME_CARDS[key]
    with column, st.container(key=f"box-card-{key}"):
        theme.html_block(f'<h2 class="pix">{title}</h2><p>{text.format(report_count=report_count)}</p>')
        st.page_link(target, label="OPEN ▶")

theme.footer()
