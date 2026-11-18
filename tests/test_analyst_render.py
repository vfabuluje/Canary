from datetime import date

import pandas as pd
import yaml

from canary.analyst.facts import Fact, FactSheet
from canary.analyst.outcome import Outcome
from canary.analyst.render import note_path, render_note
from canary.analyst.sections import all_sections

META = {"writer_model": "claude-opus-5-5", "written_at": "2026-11-17T10:00:00", "model_run": "run: 1"}


def _fact(i, label, display="1", q=date(2023, 12, 31)):
    return Fact(f"F{i}", label, q, 1.0, display, [display], False, f"src{i}.parquet: col")


def _sheet(kind="caught", after=False, failure=date(2023, 10, 20), first_flag=date(2022, 12, 31)):
    hist = pd.DataFrame({
        "report_date": pd.to_datetime(["2023-12-31", "2022-12-31", "2023-03-31"]),  # unsorted on purpose
        "rank": [5, 9, 7], "n_banks": [4000, 4100, 4050], "flagged": [True, True, False]})
    after_h = pd.DataFrame({"report_date": pd.to_datetime(["2024-06-30", "2024-03-31"]),
                            "rank": [20, 10], "n_banks": [4000, 4000], "flagged": [False, True]})
    o = Outcome(kind, after, failure, first_flag, 4 if first_flag else None, False, date(2023, 12, 31))
    pct = _fact(1, "Percentile (100 = highest risk)", "99.9%")
    pct.value = 99.9
    facts = [pct, _fact(2, "Model score", "0.9000"),
             _fact(3, "Rank"), _fact(4, "Other")]
    return FactSheet(7, "Bank Of Test: A", date(2023, 12, 31), o, facts, hist, after_h,
                     "CANT SEE TEXT.", [s.key for s in all_sections(kind)])


def _memo(sheet, cites=("F3",)):
    secs = []
    for s in all_sections(sheet.outcome.kind):
        if s.ai_written:
            secs.append({"key": s.key, "paragraphs": [{"sentences": [
                {"text": f"Text of {s.key} [F3].", "cites": list(cites)},
                {"text": "Second sentence.", "cites": []}]}]})
    return {"sections": secs}


def _render(sheet):
    return render_note(sheet, _memo(sheet), all_sections(sheet.outcome.kind), META)


def test_unsafe_names(tmp_path):
    p = note_path(tmp_path, "BANK OF A/B: #1", 7)
    assert p.name == "Bank Of A-B- -1 (7).md" and p == note_path(tmp_path, "BANK OF A/B: #1", 7)


def test_front_matter_fields():
    text = _render(_sheet())
    fm = yaml.safe_load(text.split("---\n")[1])
    assert fm["cert"] == 7 and fm["name"] == "Bank Of Test: A"
    assert fm["as_of"] == date(2023, 12, 31) and fm["failure_date"] == date(2023, 10, 20)
    assert fm["rank"] == 5 and fm["n_banks"] == 4000 and fm["flagged"] is True
    assert fm["percentile"] == 99.9 and fm["outcome"] == "caught" and fm["after_test_window"] is False
    assert fm["checked"] is True and fm["model_run"] == "run: 1"
    assert fm["writer_model"] == "claude-opus-5-5"
    assert yaml.safe_load(_render(_sheet("quiet", failure=None, first_flag=None)).split("---\n")[1])["failure_date"] is None


def test_banners():
    assert "*Hindsight: failed 2023-10-20. Canary flagged it 4 quarters ahead.*" in _render(_sheet())
    assert "*Hindsight: failed 2023-10-20. Canary did not flag it.*" in _render(_sheet("missed", first_flag=None))
    assert "*Outcome not yet known.*" in _render(_sheet("open_watchlist", failure=None, first_flag=None))
    q = _render(_sheet("quiet", failure=None, first_flag=None))
    assert "Hindsight" not in q and "Outcome not yet known" not in q
    fa = _render(_sheet("false_alarm", failure=None, first_flag=None))
    assert "*Hindsight: flagged, but had not failed as of 2023-12-31.*" in fa


def test_after_window_banner_exact():
    t = _render(_sheet(after=True, failure=date(2026, 3, 1)))
    assert "*After the test window: not part of the reported 2016-2024 results.*" in t
    assert "After the test window" not in _render(_sheet())


def test_fixed_score_sentence_present():
    t = _render(_sheet())
    s = ("The score ranks banks against each other; it is not a probability of failure, "
         "because the model was trained with extra weight on banks that failed.")
    assert s in t
    assert t.index(s) < t.index("**What the model can't see.**") < t.index("CANT SEE TEXT.")
    assert t.index("Text of score") < t.index(s)


def test_first_flag_marked_in_history():
    t = _render(_sheet())
    rows = [ln for ln in t.splitlines() if ln.startswith("| 2022-12-31")]
    assert rows and "(first flag)" in rows[0] and "▲ watchlist" in rows[0]
    h = [ln for ln in t.splitlines() if ln.startswith("| 20")]
    assert h[:3] == sorted(h[:3])  # sorted ascending
    assert "(first flag)" not in [ln for ln in t.splitlines() if ln.startswith("| 2023-03-31")][0]


def test_what_next_table_sorted():
    t = _render(_sheet())
    assert t.index("| 2024-03-31") < t.index("| 2024-06-30")


def test_no_cite_ids_and_sources_only_cited():
    t = _render(_sheet())
    assert "[F3]" not in t and "Text of summary." in t
    src = t.split("## Sources")[1]
    assert "F3 · Rank · 2023-12-31 · 1 · src3.parquet: col" in src
    assert "F4" not in src and "F1 " not in src
