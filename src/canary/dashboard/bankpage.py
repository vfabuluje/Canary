"""One bank's page. Three kinds: a written report (a showcase bank), scored without a report, or never scored."""

import html
from typing import Literal

import pandas as pd
import streamlit as st

from canary.dashboard import charts, data, theme
from canary.dashboard.copy import (BANK_AFTER_TEST, BANK_CONCENTRATION_NONE, BANK_CONCENTRATION_REASON,
                                   BANK_CONCENTRATION_TITLE, BANK_FAILED, BANK_FLAGGED, BANK_FULL_REPORT,
                                   BANK_HISTORY_TITLE, BANK_LATEST, BANK_NO_REPORT, BANK_NO_REPORT_NOTE,
                                   BANK_REPLAY_SLOT, BANK_UNSCORED)

Kind = Literal["report", "scored", "unscored"]


def page_kind(bank: pd.Series) -> Kind:
    if bool(bank["has_report"]):
        return "report"
    return "scored" if bool(bank["scored"]) else "unscored"


def _header(bank: pd.Series, title: str | None = None) -> None:
    place = ", ".join(str(p) for p in (bank["city"], bank["state"]) if pd.notna(p) and p)
    failed = f' · {BANK_FAILED.format(date=bank["failure_date"].strftime("%B %d, %Y").replace(" 0", " "))}' if pd.notna(bank["failure_date"]) else ""
    theme.html_block(f'<h2 class="pix">{html.escape(str(bank["name"]).upper())}</h2>'
                     f'<div class="note">{html.escape(place)}{html.escape(failed)} · cert {int(bank["cert"])}</div>')
    if title:
        theme.html_block(f'<h3>{html.escape(title)}</h3>')


def _render_report(bank: pd.Series) -> None:
    with st.container(key="replay-slot"):  # Task 8 puts the replay here
        theme.html_block(f'<p class="note">{html.escape(BANK_REPLAY_SLOT)}</p>')
    report = data.report(int(bank["cert"]))
    if report:
        with st.expander(BANK_FULL_REPORT):
            st.markdown(report["note_md"])


def _render_scored(bank: pd.Series) -> None:
    quarter = charts.quarter_label(str(bank["latest_report_date"].date()))
    with st.container(key="box-bank-latest"):
        theme.html_block(f'<h3>{html.escape(BANK_NO_REPORT)}</h3><p class="note">{html.escape(BANK_NO_REPORT_NOTE)}</p>')
        st.markdown(BANK_LATEST.format(quarter=quarter, rank=int(bank["latest_rank"]), n=int(bank["latest_n"]),
                                       rating=float(bank["latest_percentile"]), scale=100))
        if bool(bank["after_test_period"]):
            st.markdown(f"*{BANK_AFTER_TEST}*")
        if bank["latest_flagged"] is True or bank["latest_flagged"] == True:  # noqa: E712 (nullable bool)
            st.markdown(f"**{BANK_FLAGGED}**")
    history = data.scores_history()
    history = history[history["cert"] == int(bank["cert"])].sort_values("report_date")
    if len(history) > 1:
        with st.container(key="box-bank-history"):
            theme.html_block(f'<div class="ct">{html.escape(BANK_HISTORY_TITLE)}</div>')
            st.altair_chart(charts.history_chart(history), width="stretch")
    with st.container(key="box-bank-concentration"):
        theme.html_block(f'<div class="ct">{html.escape(BANK_CONCENTRATION_TITLE)}</div>')
        rows = data.concentration()
        rows = rows[rows["cert"] == int(bank["cert"])]
        row = rows.iloc[0] if len(rows) else None
        if row is not None and not pd.isna(row["lines"]):
            st.markdown(row["lines"])
        elif row is not None and not pd.isna(row["reason"]):
            st.markdown(BANK_CONCENTRATION_REASON.format(reason=row["reason"]))
        else:
            st.markdown(BANK_CONCENTRATION_NONE)


def _render_unscored(bank: pd.Series) -> None:
    with st.container(key="box-bank-unscored"):
        st.markdown(BANK_UNSCORED.format(year=bank["last_report"].year))


def render_bank(cert: int) -> None:
    """Draw the page for `cert`. Task 8 adds the replay to the report kind; Task 10 adds the Ask box."""
    banks = data.banks()
    match = banks[banks["cert"] == int(cert)]
    if match.empty:
        return
    bank = match.iloc[0]
    _header(bank)
    {"report": _render_report, "scored": _render_scored, "unscored": _render_unscored}[page_kind(bank)](bank)
