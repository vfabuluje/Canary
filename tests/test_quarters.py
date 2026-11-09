from datetime import date
import pytest
from canary.quarters import quarter_ends

def test_quarter_ends_inclusive_range():
    assert quarter_ends(date(2022, 9, 30), date(2023, 3, 31)) == [
        date(2022, 9, 30), date(2022, 12, 31), date(2023, 3, 31)]

def test_full_phase1_range_is_102_quarters():
    q = quarter_ends(date(2001, 3, 31), date(2026, 6, 30))
    assert len(q) == 102 and q[0] == date(2001, 3, 31) and q[-1] == date(2026, 6, 30)

def test_rejects_non_quarter_end():
    with pytest.raises(ValueError):
        quarter_ends(date(2022, 10, 1), date(2023, 3, 31))
