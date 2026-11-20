"""FIND A BANK: search by name; `?cert=N` opens a bank, `?q=text` pre-fills the search (Home's search box)."""

import re

import pandas as pd
import streamlit as st

from canary.dashboard import bankpage, data, icons, search, theme
from canary.dashboard.copy import (FIND_BACK, FIND_BAD_CERT, FIND_DID_YOU_MEAN, FIND_HINT, FIND_LABEL, FIND_LEDE,
                                   FIND_NONE, FIND_NOT_CLOSE, FIND_PLACEHOLDER, FIND_TITLE)

theme.page_title(FIND_TITLE, FIND_LEDE)
banks = data.banks()
params = st.query_params


def _open(cert: int) -> None:
    st.query_params["cert"] = str(cert)


def _cert(raw: str) -> int | None:
    """A cert from the address bar: ASCII digits only ("²" passes str.isdigit but not int), at most 10 of them."""
    return int(raw) if re.fullmatch(r"[0-9]{1,10}", raw) else None


def _plain(text: str) -> str:
    """Bank names as literal text on a Markdown button label: every ASCII punctuation mark is backslash-escaped
    (so "E*Trade" keeps its star instead of starting italics)."""
    return re.sub(r"([!-/:-@\[-`{-~])", r"\\\1", str(text))


def _search_again() -> None:
    st.query_params.pop("cert", None)
    st.query_params.pop("q", None)  # otherwise the same query would reopen the same bank


typed = st.text_input(FIND_LABEL, value=params.get("q", ""), placeholder=FIND_PLACEHOLDER, label_visibility="collapsed").strip()
if typed != params.get("q", ""):  # a new search replaces any open bank
    st.query_params["q"] = typed
    st.query_params.pop("cert", None)
    st.rerun()

raw = params.get("cert")
if raw is not None:
    cert = _cert(raw)
    if cert is not None and (banks["cert"] == cert).any():
        st.button(FIND_BACK, on_click=_search_again, key="find-back")
        bankpage.render_bank(cert)
        theme.footer()
        st.stop()
    st.warning(FIND_BAD_CERT)

result = search.search(typed, banks)
if result.direct is not None:
    _open(result.direct)
    st.rerun()
elif result.suggestions:
    theme.on_background(FIND_DID_YOU_MEAN if result.close else FIND_NOT_CLOSE, bold=True)
    if css := icons.results_css(result.suggestions):
        theme.html_block(css)
    for s in result.suggestions:
        where = " · ".join(_plain(p) for p in (s["state"], s["status"]) if pd.notna(p) and p)
        st.button(f'**{_plain(s["label"])}**\n\n:small[{where}]', key=f'pick-{s["cert"]}', on_click=_open,
                  args=(s["cert"],), width="stretch")
else:
    if typed:
        theme.on_background(FIND_NONE)
    theme.on_background(FIND_HINT)

theme.footer()
