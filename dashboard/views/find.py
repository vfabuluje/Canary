"""FIND A BANK: search by name; `?cert=N` opens a bank, `?q=text` pre-fills the search (Home's search box)."""

import streamlit as st

from canary.dashboard import bankpage, data, search, theme
from canary.dashboard.copy import (FIND_BACK, FIND_BAD_CERT, FIND_DID_YOU_MEAN, FIND_HINT, FIND_LABEL, FIND_LEDE,
                                   FIND_NONE, FIND_PLACEHOLDER, FIND_TITLE)

theme.page_title(FIND_TITLE, FIND_LEDE)
banks = data.banks()
params = st.query_params


def _open(cert: int) -> None:
    st.query_params["cert"] = str(cert)


def _search_again() -> None:
    st.query_params.pop("cert", None)


typed = st.text_input(FIND_LABEL, value=params.get("q", ""), placeholder=FIND_PLACEHOLDER, label_visibility="collapsed").strip()
if typed != params.get("q", ""):  # a new search replaces any open bank
    st.query_params["q"] = typed
    st.query_params.pop("cert", None)
    st.rerun()

raw = params.get("cert")
if raw is not None:
    cert = int(raw) if raw.isdigit() else None
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
    st.markdown(f"**{FIND_DID_YOU_MEAN}**")
    for s in result.suggestions:
        st.button(f'{s["label"]} · {s["state"]} · {s["status"]}', key=f'pick-{s["cert"]}', on_click=_open, args=(s["cert"],))
else:
    if typed:
        st.markdown(FIND_NONE)
    st.markdown(FIND_HINT)

theme.footer()
