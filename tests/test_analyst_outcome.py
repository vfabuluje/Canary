from datetime import date

import pandas as pd
import pytest

from canary.analyst.outcome import classify, default_as_of, validate_as_of


def test_default_as_of_failed_bank(analyst_ctx):
    assert default_as_of(analyst_ctx, 3) == date(2019, 9, 30)


def test_default_as_of_open_bank(analyst_ctx):
    assert default_as_of(analyst_ctx, 100) == analyst_ctx.latest_quarter


@pytest.mark.parametrize("as_of", [date(2015, 12, 31), date(2019, 12, 31), date(2019, 8, 15)])
def test_bad_as_of_raises(analyst_ctx, as_of):
    with pytest.raises(ValueError, match="cert 3"):
        validate_as_of(analyst_ctx, 3, as_of)


def test_valid_as_of_passes(analyst_ctx):
    assert validate_as_of(analyst_ctx, 3, date(2019, 9, 30)) is None


def test_caught_uses_phase3_lead_time(analyst_ctx):
    out = classify(analyst_ctx, 3, default_as_of(analyst_ctx, 3))
    assert out.kind == "caught"
    assert 1 <= out.lead_quarters <= 4
    s = analyst_ctx.scored
    row = s[(s["cert"] == 3) & (s["flagged"]) & (s["quarters_until_failure"] == out.lead_quarters)]
    assert out.first_flag == row["report_date"].min().date()
    assert out.failure_date is not None and out.failure_date > date(2019, 9, 30)
    assert not out.still_reporting and not out.after_test_window


def test_caught_ignores_as_of(analyst_ctx):
    early = classify(analyst_ctx, 3, date(2018, 3, 31))
    assert early.kind == "caught"


def test_missed(analyst_ctx):
    s = analyst_ctx.scored
    s.loc[s["cert"] == 3, "flagged"] = False
    out = classify(analyst_ctx, 3, default_as_of(analyst_ctx, 3))
    assert out.kind == "missed"
    assert out.first_flag is None and out.lead_quarters is None


def test_after_test_window_flag(analyst_ctx):
    b = analyst_ctx.banks
    b.loc[b["cert"] == 3, "failure_date"] = pd.Timestamp("2026-05-01")
    out = classify(analyst_ctx, 3, default_as_of(analyst_ctx, 3))
    assert out.after_test_window is True
    assert out.failure_date == date(2026, 5, 1)


def test_open_watchlist_vs_false_alarm(analyst_ctx):
    s = analyst_ctx.scored
    latest = pd.Timestamp(analyst_ctx.latest_quarter)
    s.loc[s["cert"] == 100, "flagged"] = False
    s.loc[(s["cert"] == 100) & (s["report_date"] == latest), "flagged"] = True
    out = classify(analyst_ctx, 100, analyst_ctx.latest_quarter)
    assert out.kind == "open_watchlist" and out.still_reporting
    earlier = sorted(s.loc[s["cert"] == 100, "report_date"])[-2]
    s.loc[(s["cert"] == 100) & (s["report_date"] == earlier), "flagged"] = True
    assert classify(analyst_ctx, 100, earlier.date()).kind == "false_alarm"


def test_quiet(analyst_ctx):
    s = analyst_ctx.scored
    s.loc[s["cert"] == 100, "flagged"] = False
    out = classify(analyst_ctx, 100, analyst_ctx.latest_quarter)
    assert out.kind == "quiet" and out.failure_date is None


def _fail_in_2025(ctx, flag: str, cert: int = 101):
    """cert fails 2025-06-30 (a test-window failure); flagged only at `flag`."""
    fd = pd.Timestamp("2025-06-30")
    ctx.banks.loc[ctx.banks["cert"] == cert, "failure_date"] = fd
    s = ctx.scored
    rows = s[s["cert"] == cert]
    s.loc[rows.index, "flagged"] = False
    qtf = {"2024-06-30": 4, "2024-09-30": 3, "2024-12-31": 2, "2025-03-31": 1}
    for d, q in qtf.items():
        s.loc[rows.index[rows["report_date"] == pd.Timestamp(d)], "quarters_until_failure"] = q
    s.loc[rows.index[rows["report_date"] == pd.Timestamp(flag)], "flagged"] = True


def test_2025_failure_flagged_only_in_2025_is_missed(analyst_ctx):
    _fail_in_2025(analyst_ctx, flag="2025-03-31")
    out = classify(analyst_ctx, 101, analyst_ctx.latest_quarter)
    assert out.kind == "missed" and out.first_flag is None and out.lead_quarters is None
    assert out.late_flag == date(2025, 3, 31) and not out.after_test_window


def test_2025_failure_flagged_in_2024_is_caught(analyst_ctx):
    _fail_in_2025(analyst_ctx, flag="2024-12-31")
    out = classify(analyst_ctx, 101, analyst_ctx.latest_quarter)
    assert out.kind == "caught" and out.lead_quarters == 2 and out.first_flag == date(2024, 12, 31)
    assert out.late_flag is None


def test_after_window_failure_uses_all_rows(analyst_ctx):
    _fail_in_2025(analyst_ctx, flag="2025-03-31")
    analyst_ctx.banks.loc[analyst_ctx.banks["cert"] == 101, "failure_date"] = pd.Timestamp("2026-03-15")
    out = classify(analyst_ctx, 101, analyst_ctx.latest_quarter)
    assert out.kind == "caught" and out.after_test_window and out.late_flag is None


def test_after_window_constant_defined_once():
    from canary.analyst import outcome, showcase

    assert showcase.AFTER_WINDOW_START is outcome.AFTER_WINDOW_START == date(2025, 12, 31)
    assert not hasattr(outcome, "TEST_END") or outcome.TEST_END == date(2024, 12, 31)
