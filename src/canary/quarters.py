"""Quarter-end date helpers."""
from datetime import date

_QUARTER_END_MONTH_DAY = {(3, 31), (6, 30), (9, 30), (12, 31)}


def _check(d: date) -> None:
    if (d.month, d.day) not in _QUARTER_END_MONTH_DAY:
        raise ValueError(f"{d} is not a quarter-end date")


def quarter_ends(start: date, end: date) -> list[date]:
    """Return all quarter-end dates from start to end, inclusive, ascending."""
    _check(start)
    _check(end)
    out: list[date] = []
    year, month = start.year, start.month
    while True:
        day = 31 if month in (3, 12) else 30
        d = date(year, month, day)
        if d > end:
            break
        out.append(d)
        month += 3
        if month > 12:
            month, year = 3, year + 1
    return out
