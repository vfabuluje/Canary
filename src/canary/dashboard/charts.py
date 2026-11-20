"""Altair charts for the 2023 and Watchlist pages. Each has a single y axis, so nothing is drawn twice.

Selecting a point (click) is exposed as a Vega-Lite point selection named PICK on the field `i`
(the row's position); the pages read it back through st.altair_chart(..., on_select=...).
"""

import math

import altair as alt
import pandas as pd

PICK = "pick"
SCORE_COLOR, WEAK_COLOR, LINE_COLOR, BAND_COLOR = "#1c7ed6", "#e8590c", "#1e2240", "#fff3bf"
HEIGHT = 190


def quarter_label(day: str) -> str:
    """'2022-12-31' -> 'Q4 2022'."""
    year, month, _ = day.split("-")
    return f"Q{math.ceil(int(month) / 3)} {year}"


def _frame(rows: list[dict]) -> pd.DataFrame:
    frame = pd.DataFrame(rows)[["q", "pct", "rank", "n", "weak"]]
    frame["i"] = range(len(frame))
    frame["quarter"] = frame["q"].map(quarter_label)
    frame["rank_text"] = [f"{r:,} of {n:,}" for r, n in zip(frame["rank"], frame["n"])]
    return frame


def _picker() -> alt.Parameter:
    return alt.selection_point(name=PICK, fields=["i"], on="click", clear="dblclick")


def _x(frame: pd.DataFrame, **kwargs) -> alt.X:
    """The ordinal quarter axis in data order (stated outright, so every layer agrees)."""
    return alt.X("quarter:O", sort=list(frame["quarter"]), **kwargs)


def _band(frame: pd.DataFrame, selected: int) -> alt.Chart:
    """The highlighted quarter: a pale band behind the lines."""
    return (alt.Chart(frame[frame["i"] == selected]).mark_rect(color=BAND_COLOR, opacity=1)
            .encode(x=_x(frame)))


def _line(frame: pd.DataFrame, selected: int, field: str, color: str, y: alt.Y, tooltip: list) -> alt.LayerChart:
    base = alt.Chart(frame).encode(x=_x(frame, title=None, axis=alt.Axis(labelAngle=-45, labelFontSize=11)),
                                   y=y)
    line = base.mark_line(color=color, strokeWidth=3)
    points = (base.mark_point(shape="square", filled=True, color=color, opacity=1, size=90)
              .encode(size=alt.condition(alt.datum.i == selected, alt.value(240), alt.value(90)), tooltip=tooltip)
              .add_params(_picker()))
    return _band(frame, selected) + line + points


def score_chart(rows: list[dict], selected: int, watchlist: float = 98.0) -> alt.LayerChart:
    """Canary's risk rating (percentile, 0-100) by quarter, with the watchlist line at `watchlist`."""
    frame = _frame(rows)
    y = alt.Y("pct:Q", title=None, scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(values=[0, 50, 100]))
    tooltip = [alt.Tooltip("quarter:O", title="Quarter"), alt.Tooltip("pct:Q", title="Risk rating", format=".1f"),
               alt.Tooltip("rank_text:N", title="Rank")]
    line = _line(frame, selected, "pct", SCORE_COLOR, y, tooltip)
    last = frame["quarter"].iloc[-1]
    rule_data = pd.DataFrame({"pct": [float(watchlist)], "quarter": [last], "label": ["WATCHLIST"]})
    rule = alt.Chart(rule_data).mark_rule(color=LINE_COLOR, strokeDash=[6, 4], strokeWidth=2).encode(y=alt.Y("pct:Q"))
    label = (alt.Chart(rule_data).mark_text(align="right", baseline="bottom", dy=-4, color=LINE_COLOR, font="monospace",
                                            fontSize=10, fontWeight="bold")
             .encode(x=_x(frame), y=alt.Y("pct:Q"), text="label:N"))
    return (line + rule + label).properties(height=HEIGHT).configure(background="#ffffff").configure_view(stroke=None)


def weak_chart(rows: list[dict], selected: int, title: str) -> alt.LayerChart:
    """The bank's real weak spot (a percentage) by quarter."""
    frame = _frame(rows)
    low, high = min(0.0, frame["weak"].min()), frame["weak"].max()
    step = 50 if high > 100 else 25
    domain = [math.floor(low / step) * step, max(step, math.ceil(high / step) * step)]
    y = alt.Y("weak:Q", title=None, scale=alt.Scale(domain=domain), axis=alt.Axis(tickCount=4, format=".0f", labelExpr="datum.label + '%'"))
    tooltip = [alt.Tooltip("quarter:O", title="Quarter"), alt.Tooltip("weak:Q", title=title[:40], format=".1f")]
    return _line(frame, selected, "weak", WEAK_COLOR, y, tooltip).properties(height=HEIGHT).configure(background="#ffffff").configure_view(stroke=None)


def threshold_chart(table: list[dict], selected: int) -> alt.LayerChart:
    """Banks caught early at each watchlist size; `selected` is the index of the chosen size."""
    frame = pd.DataFrame(table)
    frame["i"] = range(len(frame))
    frame["quarter"] = ["Top " + f"{s * 100:g}%" for s in frame["share"]]
    frame["false_text"] = [f"{f * 100:.1f}%" for f in frame["false_alarm"]]
    top = int(frame["eligible"].max())
    y = alt.Y("caught:Q", title=None, scale=alt.Scale(domain=[0, top]), axis=alt.Axis(tickCount=4, format="d"))
    tooltip = [alt.Tooltip("quarter:O", title="Watchlist size"), alt.Tooltip("caught:Q", title="Caught"),
               alt.Tooltip("false_text:N", title="False alarms")]
    return _line(frame, selected, "caught", LINE_COLOR, y, tooltip).properties(height=220).configure(background="#ffffff").configure_view(stroke=None)
