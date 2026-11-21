"""FIND A BANK: search by name; `?cert=N` opens a bank, `?q=text` pre-fills the search (Home's search box)."""

import html
import re

import pandas as pd
import streamlit as st

from canary.dashboard import bankpage, data, icons, search, suggest, theme
from canary.dashboard.copy import (FIND_BACK, FIND_BAD_CERT, FIND_DID_YOU_MEAN, FIND_HINT, FIND_LABEL, FIND_LEDE,
                                   FIND_NONE, FIND_NOT_CLOSE, FIND_PLACEHOLDER, FIND_START_TITLE,
                                   FIND_TITLE)

theme.page_title(FIND_TITLE, FIND_LEDE)
banks = data.banks()
params = st.query_params


def _open(cert: int) -> None:
    st.query_params["cert"] = str(cert)


def _plain(text: str) -> str:
    """Bank names as literal text on a Markdown button label: every ASCII punctuation mark is backslash-escaped
    (so "E*Trade" keeps its star instead of starting italics)."""
    return re.sub(r"([!-/:-@\[-`{-~])", r"\\\1", str(text))


def _pick_button(cert: int, name: str, where: str) -> None:
    st.button(f'**{_plain(name)}**\n\n:small[{_plain(where)}]', key=f"pick-{cert}", on_click=_open, args=(cert,),
              width="stretch")


def _starters() -> None:
    """The empty page: a few banks with full reports to start from."""
    groups = suggest.starter_groups(banks)
    if not groups:
        return
    theme.on_background(FIND_START_TITLE, bold=True)
    rows = [r for _, rs in groups for r in rs]
    if css := icons.results_css([{"cert": r["cert"], "website": r.get("website")} for r in rows]):
        theme.html_block(css)
    for col, (title, rs) in zip(st.columns(len(groups)), groups):
        with col, st.container(key=f"box-start-{len(title)}-{int(rs[0]['cert'])}"):
            theme.html_block(f'<h3 class="pix start-title">{html.escape(title)}</h3>')
            for r in rs:
                _pick_button(int(r["cert"]), str(r["name"]), suggest.status_line(r))


def _search_again() -> None:
    st.query_params.pop("cert", None)
    st.query_params.pop("q", None)  # otherwise the same query would reopen the same bank


with st.container(key="find-search"):  # styled as the big search box (theme.py)
    typed = st.text_input(FIND_LABEL, value=params.get("q", ""), placeholder=FIND_PLACEHOLDER,
                          label_visibility="collapsed").strip()
if typed != params.get("q", ""):  # a new search replaces any open bank
    st.query_params["q"] = typed
    st.query_params.pop("cert", None)
    st.rerun()

def _results() -> None:
    """The search results, or the starter banks when nothing is typed."""
    result = search.search(typed, banks)
    if result.direct is not None:
        _open(result.direct)
        st.rerun()
    elif result.suggestions:
        theme.on_background(FIND_DID_YOU_MEAN if result.close else FIND_NOT_CLOSE, bold=True)
        if css := icons.results_css(result.suggestions):
            theme.html_block(css)
        for s in result.suggestions:
            where = " · ".join(str(p) for p in (s["state"], s["status"]) if pd.notna(p) and p)
            _pick_button(s["cert"], s["label"], where)
    elif typed:
        theme.on_background(FIND_NONE)
        theme.on_background(FIND_HINT)
    else:
        theme.on_background(FIND_HINT)
        _starters()


# No st.stop() here: it would end the whole app run before app.py mounts the corner canary.
raw = params.get("cert")
cert = search.parse_cert(raw) if raw is not None else None
if cert is not None and (banks["cert"] == cert).any():
    st.button(FIND_BACK, on_click=_search_again, key="find-back")
    bankpage.render_bank(cert)
else:
    if raw is not None:
        st.warning(FIND_BAD_CERT)
    _results()
theme.footer()
