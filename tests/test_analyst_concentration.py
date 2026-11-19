from datetime import date

import pandas as pd

from canary.analyst import concentration as c

Q = date(2023, 12, 31)
Q_EARLY = date(2020, 12, 31)


def _row(d, con=0, mf=0, nr=0, cm=0, rbc=100, t1=None, allow=None):
    return {"report_date": pd.Timestamp(d), "LNRECONS": con, "LNREMULT": mf, "LNRENROT": nr,
            "LNCOMRE": cm, "RBC": rbc, "RBCT1J": t1, "LNATRES": allow}


def _df(*rows):
    return pd.DataFrame(list(rows))


def _both(cre_now, cre_then, con=0, as_of=Q, then=Q_EARLY):
    return _df(_row(as_of, con=con, nr=cre_now - con, t1=60, allow=40),
               _row(then, nr=cre_then, t1=60, allow=40))


def _text(res):
    return "\n".join(c.render_concentration(res))


def test_capital_measure_boundary():
    r19 = c.compute_concentration(_df(_row(date(2019, 12, 31), con=150, rbc=100, t1=10, allow=10)),
                                  date(2019, 12, 31))
    assert r19.measure == "rbc_2006" and r19.construction_pct == 150.0
    assert c.CAPITAL_2006 in c.render_concentration(r19)
    r20 = c.compute_concentration(_df(_row(date(2020, 3, 31), con=150, rbc=999, t1=60, allow=40)),
                                  date(2020, 3, 31))
    assert r20.measure == "t1_allowance_2020" and r20.construction_pct == 150.0
    assert c.CAPITAL_2020 in c.render_concentration(r20)


def test_ratios_and_lines():
    r = c.compute_concentration(_both(400, 200, con=150), Q)
    assert r.construction_pct == 150.0 and r.cre_pct == 400.0 and r.growth_pct == 100.0
    assert c.render_concentration(r).count(c.BOTH_CROSSED) == 1


def test_ge_comparisons():
    r = c.compute_concentration(_both(300, 200, con=100), Q)
    assert (r.construction_pct, r.cre_pct, r.growth_pct) == (100.0, 300.0, 50.0)
    assert c.BOTH_CROSSED in c.render_concentration(r)
    t = _text(r)
    assert t.count("| yes |") == 3


def test_ratio_300_growth_low():
    r = c.compute_concentration(_both(300, 230, con=10), Q)
    assert round(r.growth_pct, 1) == 30.4
    lines = c.render_concentration(r)
    assert c.L1_NOT_CROSSED in lines and c.L2_GROWTH_LOW in lines


def test_growth_reasons():
    no_row = c.compute_concentration(_df(_row(Q, nr=400, t1=60, allow=40)), Q)
    assert no_row.growth_reason == c.GROWTH_NO_FIGURE
    assert c.L2_GROWTH_UNKNOWN.format(growth_reason=c.GROWTH_NO_FIGURE) in c.render_concentration(no_row)
    zero = c.compute_concentration(_both(400, 0), Q)
    assert zero.growth_reason == c.GROWTH_ZERO_BASE
    assert c.L2_GROWTH_UNKNOWN.format(growth_reason=c.GROWTH_ZERO_BASE) in c.render_concentration(zero)
    null_then = _df(_row(Q, nr=400, t1=60, allow=40), _row(Q_EARLY, nr=None, t1=60, allow=40))
    assert c.compute_concentration(null_then, Q).growth_reason == c.GROWTH_NO_FIGURE


def test_capital_missing_zero_negative():
    for kw in ({"t1": None, "allow": 40}, {"t1": 60, "allow": None}, {"t1": 0, "allow": 0},
               {"t1": -50, "allow": 10}):
        r = c.compute_concentration(_df(_row(Q, con=150, nr=300, **kw)), Q)
        assert r.reason == c.REASON_CAPITAL
        lines = c.render_concentration(r)
        assert c.L1_CANT.format(reason=c.REASON_CAPITAL) in lines
        assert c.L2_CANT.format(reason=c.REASON_CAPITAL) in lines
        rows = [x for x in lines if x.startswith("| ") and "÷" in x or "Growth in" in x]
        assert all(x.count("n/a") == 2 for x in rows) and len(rows) == 3
    r = c.compute_concentration(_df(_row(date(2019, 12, 31), con=5, rbc=None)), date(2019, 12, 31))
    assert r.reason == c.REASON_CAPITAL


def test_null_cre_component_keeps_line1():
    r = c.compute_concentration(_df(_row(Q, con=120, nr=None, t1=60, allow=40)), Q)
    assert r.construction_pct == 120.0 and r.cre_pct is None
    lines = c.render_concentration(r)
    assert lines[lines.index(c.L1_CROSSED) + 1] == c.L2_CANT.format(reason=c.REASON_LOAN)


def test_no_row():
    for rows in (pd.DataFrame(), _df(_row(date(2022, 6, 30), con=1))):
        r = c.compute_concentration(rows, Q)
        lines = c.render_concentration(r)
        assert c.L1_CANT.format(reason=c.REASON_NO_DATA) in lines
        assert c.L2_CANT.format(reason=c.REASON_NO_DATA) in lines


def test_neither_crossed_combined():
    r = c.compute_concentration(_both(100, 100, con=10), Q)
    lines = c.render_concentration(r)
    assert c.BOTH_NOT_CROSSED in lines and c.L1_NOT_CROSSED not in lines


def test_number_format():
    assert c._pct(1234.56) == "1,234.6%"
    assert c._pct(-12.0) == "-12.0%"
    assert c._pct(None) == "n/a"


def test_render_order_and_copy():
    lines = c.render_concentration(c.compute_concentration(_both(400, 200, con=150), Q))
    order = [c.LEAD, c.CAPITAL_2020, c.TABLE_HEADER, c.BOTH_CROSSED, c.DEFINITIONS, c.CLOSING]
    idx = [lines.index(x) for x in order]
    assert idx == sorted(idx)
    for x in (c.LEAD, c.DEFINITIONS, c.CLOSING):
        assert lines.count(x) == 1
    assert c.TABLE_HEADER == "| Test | Bank | Line | Meets it? |"
