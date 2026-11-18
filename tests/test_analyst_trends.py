from datetime import date

import pandas as pd
import pytest

from canary.analyst.trends import (
    MAX_SHOWN,
    TREND_RATIOS,
    compute_trends,
    direction_label,
    prior_values,
    rank_phrase,
    to_pp,
)


def _hist(feature, values_by_quarter):
    """One-bank history; values_by_quarter maps 'YYYY-MM-DD' -> value."""
    rows = [{"report_date": pd.Timestamp(d), feature: v} for d, v in values_by_quarter.items()]
    return pd.DataFrame(rows)


def _quarters(start, end):
    return [d.strftime("%Y-%m-%d") for d in pd.date_range(start, end, freq="QE")]


def _flat(feature, start, end, value):
    return {q: value for q in _quarters(start, end)}


def _merge(*frames):
    out = frames[0]
    for f in frames[1:]:
        out = out.merge(f, on="report_date", how="outer")
    return out


def test_pit_window_is_prior_12_quarters():
    vals = {q: float(i) for i, q in enumerate(_quarters("2018-12-31", "2022-03-31"))}
    s = prior_values(_hist("equity_to_assets", vals), "equity_to_assets", date(2022, 3, 31))
    assert len(s) == 12
    assert min(s.index) == pd.Timestamp("2019-03-31")
    assert max(s.index) == pd.Timestamp("2021-12-31")


def test_pit_needs_8_of_12():
    base = _quarters("2019-03-31", "2021-12-31")
    for n, expect_checked in ((7, 0), (8, 1)):
        vals = {q: 8.0 for q in base[-n:]}
        vals["2022-03-31"] = 9.0
        r = compute_trends(_hist("equity_to_assets", vals), date(2022, 3, 31), {})
        assert r.checked == expect_checked
        assert r.too_little == 1 - expect_checked


def test_ytd_window_same_quarter_prior_3_years():
    vals = {"2021-09-30": 1.0, "2020-09-30": 2.0, "2019-09-30": 3.0,
            "2018-09-30": 50.0, "2022-06-30": 99.0, "2022-09-30": 1.5}
    s = prior_values(_hist("return_on_assets", vals), "return_on_assets", date(2022, 9, 30))
    assert sorted(s.values) == [1.0, 2.0, 3.0]


def test_ytd_needs_2_of_3():
    for vals, expect in (({"2021-09-30": 1.0, "2022-09-30": 5.0}, 0),
                         ({"2021-09-30": 1.0, "2020-09-30": 1.2, "2022-09-30": 5.0}, 1)):
        r = compute_trends(_hist("return_on_assets", vals), date(2022, 9, 30), {})
        assert r.checked == expect
        assert r.too_little == 1 - expect


def test_nan_skipped_not_zero():
    vals = _flat("equity_to_assets", "2019-03-31", "2021-12-31", 8.0)
    vals["2020-06-30"] = float("nan")
    vals["2020-09-30"] = 6.0
    vals["2022-03-31"] = 5.0
    h = _hist("equity_to_assets", vals)
    s = prior_values(h, "equity_to_assets", date(2022, 3, 31))
    assert len(s) == 11 and s.min() == 6.0
    r = compute_trends(h, date(2022, 3, 31), {})
    assert r.outside[0].lo == 6.0
    vals["2022-03-31"] = float("nan")
    r = compute_trends(_hist("equity_to_assets", vals), date(2022, 3, 31), {})
    assert r.checked == 0 and r.too_little == 0 and r.outside == []


def test_reporting_gap_shrinks_window():
    vals = {q: 8.0 for q in _quarters("2019-03-31", "2021-12-31")}
    for gap in ("2020-03-31", "2020-06-30"):
        del vals[gap]
    vals["2018-12-31"] = 1.0
    vals["2022-03-31"] = 9.0
    r = compute_trends(_hist("equity_to_assets", vals), date(2022, 3, 31), {})
    assert r.outside[0].n_prior == 10
    assert r.outside[0].lo == 8.0


def test_equal_to_bound_is_inside():
    vals = _flat("equity_to_assets", "2019-03-31", "2021-12-31", 8.0)
    vals["2021-12-31"] = 10.0
    vals["2022-03-31"] = 10.0
    r = compute_trends(_hist("equity_to_assets", vals), date(2022, 3, 31), {})
    assert r.checked == 1 and r.outside == []


def test_excess_and_ordering_with_floor():
    q = _quarters("2019-03-31", "2021-12-31")
    flat = {d: 0.0 for d in q}
    flat["2022-03-31"] = 0.003  # frac: +0.3 pp over a zero-width range
    wide = {d: (i % 2) * 10.0 for i, d in enumerate(q)}  # 0..10 pp
    wide["2022-03-31"] = 15.0  # 5 pp past a 10 pp range
    h = _merge(_hist("brokered_to_deposits", flat), _hist("equity_to_assets", wide))
    r = compute_trends(h, date(2022, 3, 31), {})
    names = [t.feature for t in r.outside]
    assert names == ["equity_to_assets", "brokered_to_deposits"]
    assert r.outside[0].excess_pp == pytest.approx(5.0)
    assert r.outside[0].score == pytest.approx(0.5)
    assert r.outside[1].excess_pp == pytest.approx(0.3)
    assert r.outside[1].score == pytest.approx(0.3)


def test_tie_broken_by_plain_name():
    from canary.analyst.labels import PLAIN_NAMES

    q = _quarters("2019-03-31", "2021-12-31")
    frames = []
    for f in ("equity_to_assets", "leverage_ratio"):
        v = {d: 5.0 for d in q}
        v["2022-03-31"] = 6.0
        frames.append(_hist(f, v))
    r = compute_trends(_merge(*frames), date(2022, 3, 31), {})
    names = [PLAIN_NAMES[t.feature] for t in r.outside]
    assert names == sorted(names)


def test_cap_six_and_total():
    q = _quarters("2019-03-31", "2021-12-31")
    frames = []
    for f in TREND_RATIOS[:8]:
        v = {d: 5.0 for d in q}
        v["2022-03-31"] = 6.0
        frames.append(_hist(f, v))
    r = compute_trends(_merge(*frames), date(2022, 3, 31), {})
    assert len(r.outside) == 8
    assert len(r.shown) == MAX_SHOWN == 6


def test_changes_pp_units():
    vals = _flat("htm_unrealized_loss_to_equity", "2019-03-31", "2021-12-31", 0.0)
    vals.update({"2021-03-31": 0.0, "2021-12-31": 0.066, "2022-03-31": 0.484})
    r = compute_trends(_hist("htm_unrealized_loss_to_equity", vals), date(2022, 3, 31), {})
    t = r.outside[0]
    assert t.change_1q_pp == pytest.approx(41.8)
    assert t.change_4q_pp == pytest.approx(48.4)

    v = _flat("equity_to_assets", "2019-03-31", "2021-12-31", 7.0)
    v["2021-12-31"] = 7.2
    v["2022-03-31"] = 8.4
    t = compute_trends(_hist("equity_to_assets", v), date(2022, 3, 31), {}).outside[0]
    assert t.change_1q_pp == pytest.approx(1.2)

    v = _flat("return_on_assets", "2019-09-30", "2021-09-30", 1.0)
    v["2022-09-30"] = 5.0
    v["2022-06-30"] = 1.0
    t = compute_trends(_hist("return_on_assets", v), date(2022, 9, 30), {}).outside[0]
    assert t.change_1q_pp is None
    assert t.change_4q_pp == pytest.approx(4.0)

    v = _flat("equity_to_assets", "2019-03-31", "2021-09-30", 7.0)  # no 2021-12-31
    v["2022-03-31"] = 8.4
    t = compute_trends(_hist("equity_to_assets", v), date(2022, 3, 31), {}).outside[0]
    assert t.change_1q_pp is None


def test_direction_cutoffs():
    assert direction_label(0.05) == "pushed the score up"
    assert direction_label(0.0499) == "little effect on the score"
    assert direction_label(-0.05) == "pushed the score down"


def test_contribution_default_zero():
    v = _flat("equity_to_assets", "2019-03-31", "2021-12-31", 7.0)
    v["2022-03-31"] = 8.4
    t = compute_trends(_hist("equity_to_assets", v), date(2022, 3, 31), {}).outside[0]
    assert t.contribution == 0.0 and t.direction == "little effect on the score"


def test_rank_phrase():
    assert rank_phrase(26.8, 56.0) == "the model rated it safer than a year earlier"
    assert rank_phrase(60.0, 50.0) == "the model rated it riskier than a year earlier"
    assert rank_phrase(50.0, 50.9) == "about the same as a year earlier"


def test_to_pp():
    assert to_pp("htm_unrealized_loss_to_equity", 0.418) == pytest.approx(41.8)
    assert to_pp("equity_to_assets", 1.2) == pytest.approx(1.2)


def test_log_total_assets_excluded():
    assert "log_total_assets" not in TREND_RATIOS
    assert len(TREND_RATIOS) == 30
    v = _flat("log_total_assets", "2019-03-31", "2021-12-31", 10.0)
    v["2022-03-31"] = 20.0
    r = compute_trends(_hist("log_total_assets", v), date(2022, 3, 31), {})
    assert r.checked == 0 and r.outside == []
