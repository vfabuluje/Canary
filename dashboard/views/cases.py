"""THE 2023 COLLAPSES: the three failed banks, quarter by quarter, with Canary's rating against the real weak spot."""

import html

import streamlit as st

from canary.dashboard import charts, data, theme
from canary.dashboard.copy import (CASE_CAPTIONS, CASE_LABELS, CASES_LEDE, CASES_SCORE_NOTE, CASES_SCORE_TITLE,
                                   CASES_SIDE, CASES_SLIDER_LABEL, CASES_TITLE, WEAK_SHORT_LABELS, WEAK_SPOT_TITLES)
from canary.dashboard.watch import published_share

theme.page_title(CASES_TITLE, CASES_LEDE)

cases = data.cases()
certs = [int(c) for c in cases]
watch_line = round(100 * (1 - published_share(data.metrics(), data.threshold())), 6)

cert = st.segmented_control("Bank", certs, default=certs[0], required=True, format_func=lambda c: CASE_LABELS[c]["chip"],
                            key="case-bank", label_visibility="collapsed")
rows = cases[str(cert)]
labels = [charts.quarter_label(r["q"]) for r in rows]
slider_key = f"case-q-{cert}"


def _pick_from_chart(chart_key: str) -> None:
    """A click on a chart point moves this bank's quarter slider to that point."""
    picked = (st.session_state.get(chart_key) or {}).get("selection", {}).get(charts.PICK) or []
    if picked:
        st.session_state[slider_key] = labels[picked[0]["i"]]


label = CASE_LABELS[cert]
theme.html_block(
    f'<div class="cs-head"><div><h2 class="pix">{html.escape(label["name"].upper())}</h2>'
    f'<div class="note">Failed {html.escape(label["failed"])}</div></div>'
    f'<span class="status {"near" if "NEAR" in label["status"] else "failed"}">{html.escape(label["status"])}</span></div>'
)

main, side = st.columns([2.2, 1], gap="medium")
with main, st.container(key="box-cases-charts"):
    # The slider is drawn last, but its value decides the highlighted quarter: read it from state first.
    chosen = st.session_state.get(slider_key, labels[-1])
    index = labels.index(chosen) if chosen in labels else len(labels) - 1
    theme.html_block(f'<div class="ct">{html.escape(CASES_SCORE_TITLE)}</div><div class="cst">{html.escape(CASES_SCORE_NOTE)}</div>')
    st.altair_chart(charts.score_chart(rows, index, watch_line), width="stretch", key=f"case-score-{cert}",
                    on_select=lambda: _pick_from_chart(f"case-score-{cert}"), selection_mode=charts.PICK)
    weak = WEAK_SPOT_TITLES[cert]
    theme.html_block(f'<div class="ct">{html.escape(weak["title"])}</div><div class="cst">{html.escape(weak["note"])}</div>')
    st.altair_chart(charts.weak_chart(rows, index, weak["title"]), width="stretch", key=f"case-weak-{cert}",
                    on_select=lambda: _pick_from_chart(f"case-weak-{cert}"), selection_mode=charts.PICK)
    st.select_slider(CASES_SLIDER_LABEL, options=labels, value=labels[-1], key=slider_key)

row = rows[labels.index(st.session_state[slider_key])]
rating, flagged = f'{row["pct"]:.1f} / 100', row["pct"] >= watch_line
top = max(value for _, value in row["signals"])
bars = "".join(
    f'<div class="bar">{html.escape(name.removeprefix("the ").capitalize())}'
    f'<div class="track"><div class="fill" style="width:{value / top * 100:.0f}%"></div></div></div>'
    for name, value in row["signals"][:3]
)
S = CASES_SIDE
with side, st.container(key="box-side"):
    theme.html_block(
        f'<div class="side-q">{html.escape(S["report"].format(quarter=charts.quarter_label(row["q"]).upper()))}</div>'
        f'<div class="side-rank">#{row["rank"]:,}</div><div class="note">{html.escape(S["of"].format(n=row["n"]))}</div>'
        f'<div class="side-row"><span>{S["rating"]}</span><b>{rating}</b></div>'
        f'<div class="side-row"><span>{html.escape(WEAK_SHORT_LABELS[cert])}</span><b>{row["weak"]:.1f}%</b></div>'
        f'<div class="side-row"><span>{S["on_list"]}</span><b>{S["yes"] if flagged else S["no"]}</b></div>'
        f'<div class="side-bars">{S["bars"]}</div>{bars}'
        f'<div class="say">{html.escape(CASE_CAPTIONS[cert][row["phase"]])}</div>'
    )

theme.footer()
