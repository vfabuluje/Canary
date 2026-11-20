"""Why "Canary": the name, the story behind it, the goal and the honest answer."""

import streamlit as st

from canary.dashboard import data, theme
from canary.dashboard.copy import WHY_SECTIONS

metrics = data.metrics()

theme.html_block(f'<div class="why-hero">{theme.cage_svg(136)}<h1 class="pix page-title">WHY "CANARY"?</h1></div>')

for i, (title, body) in enumerate(WHY_SECTIONS):
    last = i == len(WHY_SECTIONS) - 1
    with st.container(key="box-why-answer" if last else f"box-why-{i}"):
        theme.html_block(f'<h2 class="pix">{title}</h2><p>{theme.bold(body.format_map(metrics))}</p>')
        if last:
            st.page_link("pages/cases.py", label="SEE THE 2023 COLLAPSES ▶")

theme.footer()
