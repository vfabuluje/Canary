"""WATCHLIST SIZE: flag more banks and catch more failures, at the cost of more false alarms."""

import html

import streamlit as st

from canary.dashboard import charts, data, theme
from canary.dashboard.copy import (CASE_LABELS, WATCH_CARDS, WATCH_CASES_CAUGHT, WATCH_CASES_MISSED, WATCH_CASES_NONE,
                                   WATCH_CHART_NOTE, WATCH_CHART_TITLE, WATCH_LEDE, WATCH_PUBLISHED, WATCH_SAY,
                                   WATCH_TITLE)
from canary.dashboard.watch import published_share

theme.page_title(WATCH_TITLE, WATCH_LEDE)

table = data.threshold()
published = published_share(data.metrics(), table)
shares = [t["share"] for t in table]


def _size_label(share: float) -> str:
    text = f"TOP {share * 100:g}%"
    return f"{text}  {WATCH_PUBLISHED}" if share == published else text


def _pick_from_chart() -> None:
    picked = (st.session_state.get("watch-chart") or {}).get("selection", {}).get(charts.PICK) or []
    if picked:
        st.session_state["watch-size"] = shares[picked[0]["i"]]


share = st.segmented_control("Watchlist size", shares, default=published, required=True, format_func=_size_label,
                             key="watch-size", label_visibility="collapsed")
index = shares.index(share)
row = table[index]

BIG = {
    "caught": f'{row["caught"]} <small>of {row["eligible"]}</small>',
    "false_alarm": f'{row["false_alarm"] * 100:.1f}%',
    "flags": f'{row["rows"]:,}',
}
cards = "".join(
    f'<div class="box stat"><div class="lab">{label}</div><div class="big">{BIG[key]}</div>'
    f'<div class="note">{html.escape(note.format(**row))}</div></div>'
    for key, (label, note) in WATCH_CARDS.items()
)
theme.html_block(f'<div class="three">{cards}</div>')

with st.container(key="box-watch-chart"):
    theme.html_block(f'<div class="ct">{html.escape(WATCH_CHART_TITLE)}</div><div class="cst">{html.escape(WATCH_CHART_NOTE)}</div>')
    st.altair_chart(charts.threshold_chart(table, index), width="stretch", key="watch-chart",
                    on_select=_pick_from_chart, selection_mode=charts.PICK)

names = [CASE_LABELS[c] for c in map(int, data.cases())]
caught = [CASE_LABELS[c]["name"] for c in row["caught_case_studies"]]
missed = [lab["chip"] for lab in names if lab["name"] not in caught]
if caught:
    missed_text = WATCH_CASES_MISSED.format(missed=" and ".join(missed)) if missed else ""
    cases_text = WATCH_CASES_CAUGHT.format(caught=" and ".join(caught), missed=missed_text)
else:
    cases_text = WATCH_CASES_NONE
theme.html_block(
    '<div class="say" style="box-shadow:5px 5px 0 var(--navy)">'
    + theme.bold(WATCH_SAY.format(share=f"{share * 100:g}", caught=row["caught"], eligible=row["eligible"], cases=cases_text))
    + "</div>"
)
theme.footer()
