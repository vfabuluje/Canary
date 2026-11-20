"""HOW IT WORKS (spec 5.5a): the replay of a showcase bank's real run (SVB by default), then Canary end to end."""

import html

import streamlit as st

from canary.dashboard import data, theme
from canary.dashboard.copy import HOW_LEDE, HOW_MARKS, HOW_PICK, HOW_STEPS, HOW_STRIP_TITLE, HOW_TITLE
from canary.dashboard.replay import render_replay

DEFAULT_CERT = 24735  # SVB

theme.page_title(HOW_TITLE, HOW_LEDE)

certs = data.report_certs()
if certs:
    banks = data.banks().set_index("cert")
    label = {c: f"{banks.at[c, 'name']} ({banks.at[c, 'state']})" if c in banks.index else str(c) for c in certs}
    certs = sorted(certs, key=lambda c: label[c].lower())
    with st.container(key="how-picker"):
        cert = st.selectbox(HOW_PICK, certs, index=certs.index(DEFAULT_CERT) if DEFAULT_CERT in certs else 0,
                            format_func=label.get, key="how-bank")
    report = data.report(cert)
    if report:
        render_replay(report, theme.current_theme())

steps = "".join(
    f'<div class="box step"><span class="mark {mark.lower()}">{mark}</span><div class="ct">{html.escape(title)}</div>'
    f'<p>{html.escape(line)}</p><div class="cst">{html.escape(HOW_MARKS[mark])}</div></div>'
    for title, line, mark in HOW_STEPS
)
theme.html_block(f'<h2 class="pix page-title how-strip-title">{html.escape(HOW_STRIP_TITLE)}</h2><div class="steps">{steps}</div>')

theme.footer()
