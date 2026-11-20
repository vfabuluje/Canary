import json
import re
from datetime import date
from pathlib import Path

import pytest

from canary.analyst.checker import extract_tokens
from canary.analyst.concentration import REASON_NO_DATA, ConcentrationResult
from canary.analyst.facts import Fact
from canary.analyst.labels import PLAIN_NAMES
from canary.dashboard.cards import headline, pick_sentences, rule_sentences, slim_trace
from canary.dashboard.copy import FLAGSHIP_CARDS, GLOSSARY, HEADLINES

TRACES = Path("data/analyst/traces")
NOTES = Path("banks")
FEATURES = Path("data/features/fct_bank_features.parquet")
FAILURES = Path("data/raw/failures/failures.parquet")
SVB_TRACE = TRACES / "24735_2022-12-31.json"


def _call(agent, attempt, memo=None):
    return {"agent": agent, "attempt": attempt, "request": {}, "checker_errors": [],
            "response_text": json.dumps(memo or {"sections": []})}


def _trace(*calls):
    return {"cert": 1, "as_of": "2020-03-31", "ok": True, "calls": list(calls)}


def test_slim_trace_retry():
    agents = slim_trace(_trace(_call("trend", 1), _call("peer", 1), _call("analyst", 1), _call("analyst", 2)))["agents"]
    assert agents["analyst"] == {"ran": True, "attempts": 2, "first_try": False}
    assert agents["trend"] == {"ran": True, "attempts": 1, "first_try": True}
    assert agents["peer"] == {"ran": True, "attempts": 1, "first_try": True}


def test_slim_trace_trend_retry():
    agents = slim_trace(_trace(_call("trend", 1), _call("trend", 2), _call("peer", 1), _call("analyst", 1)))["agents"]
    assert agents["trend"] == {"ran": True, "attempts": 2, "first_try": False}
    assert agents["analyst"]["first_try"] is True


def test_slim_trace_no_peer():
    agents = slim_trace(_trace(_call("trend", 1), _call("analyst", 1)))["agents"]
    assert set(agents) == {"trend", "peer", "analyst"}
    assert agents["peer"]["ran"] is False
    assert agents["peer"]["attempts"] == 0


def _fact(id, label, forms, feature=None, kind=None):
    return Fact(id, label, date(2022, 12, 31), 0.0, forms[0], forms, False, "test", feature, kind)


def test_pick_sentences_skips_identity_keeps_uncited():
    facts = {
        "F6": _fact("F6", "National rank (1 = highest score)", ["3,494", "3494"]),
        "F7": _fact("F7", "Banks ranked that quarter", ["4,773", "4773"]),
        "F51": _fact("F51", "Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter",
                     ["86.4%", "86%"], feature="uninsured_to_deposits", kind="peer_value"),
        "F52": _fact("F52", "National median: uninsured deposits as a share of deposits", ["25.5%", "26%"]),
    }
    section = {"key": "summary", "paragraphs": [{"sentences": [
        {"text": "It ranked 3,494 out of 4,773 banks.", "cites": ["F6", "F7"]},
        {"text": "The model's reading points elsewhere.", "cites": []},
        {"text": "Uninsured deposits were 86.4% against a median of 25.5%.", "cites": ["F51", "F52"]},
    ]}, {"sentences": [{"text": "Third one, ranked 3,494.", "cites": ["F6", "F52"]},
                       {"text": "Fourth.", "cites": ["F51"]}]}]}
    assert [s["text"] for s in pick_sentences(section, facts)] == [
        "The model's reading points elsewhere.", "Uninsured deposits were 86.4% against a median of 25.5%."]
    assert pick_sentences(section, facts, n=1)[0]["numbers"] == []
    picked = pick_sentences(section, facts, n=3)[1:]
    assert [s["text"] for s in picked] == ["Uninsured deposits were 86.4% against a median of 25.5%.",
                                           "Third one, ranked 3,494."]
    nums = picked[0]["numbers"]
    assert [n["text"] for n in nums] == ["86.4%", "25.5%"]
    assert nums[0]["explain"] == GLOSSARY["uninsured_to_deposits"]
    assert nums[0]["label"] == facts["F51"].label
    assert nums[0]["quarter"] == "2022-12-31"
    # Fact with no feature: the glossary entry of the column named in its source, else its label.
    assert nums[1]["explain"] == facts["F52"].label
    assert picked[1]["numbers"][0]["text"] == "3,494"


def test_pick_sentences_skips_rank_and_peer_group_context():
    facts = {
        "F4": _fact("F4", "State", ["CA"]),
        "F69": _fact("F69", "Bank: total assets", ["$209.0 billion"]),
        "F8": _fact("F8", "Percentile (100 = highest risk)", ["26.8th"]),
        "F141": _fact("F141", "Percentile a year earlier (100 = highest risk)", ["56.0th"],
                      kind="trend_prior_percentile"),
        "F143": _fact("F143", "Peers: banks in the peer group (including this bank)", ["23"], kind="peer_count"),
        "F73": _fact("F73", "Bank: deposit growth over the past four quarters", ["-8.4%"]),
    }
    section = {"key": "trends", "paragraphs": [{"sentences": [
        {"text": "A CA bank with $209.0 billion, at the 26.8th percentile.", "cites": ["F4", "F69", "F8"]},
        {"text": "A year earlier it sat at the 56.0th percentile.", "cites": ["F141"]},
        {"text": "It has 23 peers.", "cites": ["F143"]},
        {"text": "Deposit growth was -8.4%.", "cites": ["F73"]},
    ]}]}
    assert [s["text"] for s in pick_sentences(section, facts)] == ["Deposit growth was -8.4%."]


def test_rule_card_when_test_cannot_be_applied():
    r = ConcentrationResult(date(2022, 12, 31), "t1_allowance_2020", None, None, None, reason=REASON_NO_DATA)
    sents = rule_sentences(r)
    text = " ".join(s["text"] for s in sents)
    assert "can't be checked" in text
    assert "%" not in text.replace("100%", "").replace("300%", "")
    assert all(n["text"] != "0.0%" for s in sents for n in s["numbers"])


def test_rule_card_values():
    r = ConcentrationResult(date(2022, 12, 31), "t1_allowance_2020", 15.6, 314.5, 24.6)
    sents = rule_sentences(r)
    texts = [s["text"] for s in sents]
    assert any("314.5%" in t for t in texts)
    assert any("24.6%" in t for t in texts)  # growth shown because the 300% line was reached
    for s in sents:
        for n in s["numbers"]:
            assert n["text"] in s["text"]


def test_headlines_no_digits():
    assert set(HEADLINES) == {"caught", "missed", "false_alarm", "open_watchlist", "quiet"}
    for kind in HEADLINES:
        text = headline(kind, "Bank Of Vici")
        assert "Bank Of Vici" in text
        assert not re.search(r"\d", text), text
    for cert, copy in FLAGSHIP_CARDS.items():
        assert not re.search(r"\d", copy["headline"]), cert


def test_glossary_has_every_feature_and_no_digits():
    assert set(PLAIN_NAMES) <= set(GLOSSARY)
    for key, text in GLOSSARY.items():
        assert not re.search(r"\d", text), key


def _strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)


def _unsigned(tokens):
    return {t.lstrip("+-") for t in tokens}


def _note_text(cert: int) -> str:
    (path,) = NOTES.glob(f"* ({cert}).md")
    return path.read_text(encoding="utf-8")


def test_flagship_numbers_in_note():
    """Every number token in the flagship copy (text, hover text, labels) appears in that bank's note.
    The sign is compared loosely: "shrank 8.4%" renders the note's "-8.4%"."""
    assert set(FLAGSHIP_CARDS) == {24735, 57053, 59017}
    for cert, copy in FLAGSHIP_CARDS.items():
        note = _unsigned(extract_tokens(_note_text(cert)))
        for text in _strings(copy):
            missing = _unsigned(extract_tokens(text)) - note
            assert not missing, (cert, text, missing)


def test_flagship_shape():
    for cert, copy in FLAGSHIP_CARDS.items():
        assert set(copy["cards"]) == {"trend", "peer", "rule", "summary"}, cert
        for key, sents in copy["cards"].items():
            assert sents, (cert, key)
            for s in sents:
                for n in s["numbers"]:
                    assert n["text"] in s["text"], (cert, n["text"])
                    assert ("fact" in n) != ("label" in n), (cert, n)
                    assert n["explain"]


# ---------- real data ----------

@pytest.fixture(scope="module")
def ctx():
    if not (FEATURES.exists() and FAILURES.exists() and SVB_TRACE.exists()):
        pytest.skip("real data not present")
    from canary.analyst.context import load_context
    return load_context(FEATURES, Path("data/model"), FAILURES)


@pytest.fixture(scope="module")
def svb_sheet(ctx):
    from canary.analyst.facts import build_fact_sheet
    return build_fact_sheet(ctx, 24735, date(2022, 12, 31))


def _last_section(trace, agent, key):
    calls = [c for c in trace["calls"] if c["agent"] == agent]
    memo = json.loads(max(calls, key=lambda c: c["attempt"])["response_text"])
    return next(s for s in memo["sections"] if s["key"] == key)


@pytest.mark.data
def test_pick_sentences_skips_rank_only(svb_sheet):
    trace = json.loads(SVB_TRACE.read_text())
    facts = {f.id: f for f in svb_sheet.facts}
    picked = pick_sentences(_last_section(trace, "trend", "trends"), facts)
    assert len(picked) == 2
    assert all("3,494" not in s["text"] for s in picked)


@pytest.mark.data
def test_numbers_match_cited_facts(ctx):
    """For every showcase trace, every highlighted number in a picked sentence is one of the forms
    of a fact that sentence cites."""
    from canary.analyst.facts import build_fact_sheet
    from canary.dashboard.cards import CARD_SECTIONS

    def norm(s):
        return s.replace(",", "").lower()

    checked = 0
    for path in sorted(TRACES.glob("*.json")):
        trace = json.loads(path.read_text())
        sheet = build_fact_sheet(ctx, trace["cert"], date.fromisoformat(trace["as_of"]))
        facts = {f.id: f for f in sheet.facts}
        for agent, key in CARD_SECTIONS:
            if not any(c["agent"] == agent for c in trace["calls"]):
                continue
            section = _last_section(trace, agent, key)
            cites = {s["text"]: s["cites"] for p in section["paragraphs"] for s in p["sentences"]}
            for sent in pick_sentences(section, facts):
                for n in sent["numbers"]:
                    assert n["text"] in sent["text"]
                    forms = {norm(f) for cid in cites[sent["text"]] for f in facts[cid].forms}
                    assert norm(n["text"]) in forms, (path.name, sent["text"], n["text"])
                    checked += 1
    assert checked > 100


@pytest.mark.data
def test_picked_sentences_are_findings(ctx):
    """Across all showcase traces: no picked sentence cites only trend method facts (ratio counts, windows),
    points at the note's table, or is an uncited log-odds definition; every trend card has a sentence
    citing one of the ratio values, ranges or contributions."""
    from canary.analyst.facts import build_fact_sheet
    from canary.dashboard.cards import CARD_SECTIONS

    method = {"trend_count_checked", "trend_count_outside", "trend_count_shown", "trend_window_pit",
              "trend_window_ytd"}
    ratio = {"trend_value", "trend_lo", "trend_hi", "trend_contribution"}
    for path in sorted(TRACES.glob("*.json")):
        trace = json.loads(path.read_text())
        sheet = build_fact_sheet(ctx, trace["cert"], date.fromisoformat(trace["as_of"]))
        facts = {f.id: f for f in sheet.facts}
        for agent, key in CARD_SECTIONS:
            if not any(c["agent"] == agent for c in trace["calls"]):
                continue
            section = _last_section(trace, agent, key)
            cites = {s["text"]: s["cites"] for p in section["paragraphs"] for s in p["sentences"]}
            picked = pick_sentences(section, facts)
            kinds = [{facts[c].kind for c in cites[s["text"]]} for s in picked]
            for s, k in zip(picked, kinds):
                assert not (k and k <= method), (path.name, s["text"])
                assert "the table" not in s["text"].lower(), (path.name, s["text"])
                assert k or "log-odds" not in s["text"], (path.name, s["text"])
                assert k or key != "peers", (path.name, s["text"])  # uncited peer text: lead-in or definition
            if agent == "trend":
                assert any(k & ratio for k in kinds), (path.name, [s["text"] for s in picked])


def test_pick_sentences_skips_method_text():
    facts = {
        "F136": _fact("F136", "Trend: ratios outside their own prior range", ["11"], kind="trend_count_outside"),
        "F139": _fact("F139", "Comparison window for most ratios: the prior 12 quarters", ["12"],
                      kind="trend_window_pit"),
        "F95": _fact("F95", "Trend: interest expense, value at the as-of quarter", ["0.5%"],
                     feature="interest_expense_to_assets_ann", kind="trend_value"),
    }
    section = {"key": "trends", "paragraphs": [{"sentences": [
        {"text": "Over the prior 12 quarters, 11 ratios were outside their range.", "cites": ["F139", "F136"]},
        {"text": "Contributions are in model log-odds units, where positive pushes the score up.", "cites": []},
        {"text": "The table shows the furthest ones.", "cites": []},
        {"text": "Interest expense was 0.5% of assets.", "cites": ["F95"]},
        {"text": "In short, none of them pushed the score up.", "cites": []},
    ]}]}
    assert [s["text"] for s in pick_sentences(section, facts)] == [
        "Interest expense was 0.5% of assets.", "In short, none of them pushed the score up."]
    peers = {"key": "peers", "paragraphs": [{"sentences": [
        {"text": "The Texas ratio compares troubled loans with capital.", "cites": []},
        {"text": "Interest expense was 0.5% of assets.", "cites": ["F95"]},
    ]}]}
    assert [s["text"] for s in pick_sentences(peers, facts)] == ["Interest expense was 0.5% of assets."]


@pytest.mark.data
def test_build_report_rejects_fact_drift(ctx):
    from canary.dashboard.reports import build_report

    trace = json.loads(SVB_TRACE.read_text())
    call = next(c for c in trace["calls"] if c["agent"] == "trend")
    memo = json.loads(call["response_text"])
    memo["sections"][0]["paragraphs"][0]["sentences"][0]["cites"].append("F9999")
    call["response_text"] = json.dumps(memo)
    with pytest.raises(ValueError, match="F9999"):
        build_report(ctx, 24735, date(2022, 12, 31), trace, _note_text(24735))


@pytest.fixture(scope="module")
def written(ctx, tmp_path_factory):
    from canary.dashboard.reports import write_reports

    out = tmp_path_factory.mktemp("dash")
    certs = write_reports(ctx, NOTES, TRACES, out)
    return out, certs


@pytest.mark.data
def test_reports_written_for_every_note_with_trace(written):
    from canary.dashboard.tables import showcase_certs

    out, certs = written
    files = sorted((out / "reports").glob("*.json"))
    assert len(files) == 61
    assert sorted(certs) == sorted(showcase_certs(NOTES, TRACES))
    assert {int(p.stem) for p in files} == set(certs)


@pytest.mark.data
def test_report_contents(written):
    out, _ = written
    svb = json.loads((out / "reports" / "24735.json").read_text())
    assert set(svb) == {"cert", "name", "as_of", "outcome", "failure_date", "rank", "n_banks", "percentile",
                        "flagged", "headline", "cards", "agents", "facts", "note_md"}
    assert (svb["rank"], svb["n_banks"], svb["flagged"]) == (3494, 4773, False)
    assert svb["outcome"] == "missed" and svb["failure_date"] == "2023-03-10"
    assert svb["headline"] == FLAGSHIP_CARDS[24735]["headline"]
    assert [c["key"] for c in svb["cards"]] == ["trend", "peer", "rule", "summary"]
    assert [c["badge"] for c in svb["cards"]] == ["AI", "AI", "RULE", "AI"]
    assert svb["cards"][0]["sentences"][0]["text"] == FLAGSHIP_CARDS[24735]["cards"]["trend"][0]["text"]
    assert svb["agents"]["peer"] == {"ran": True, "attempts": 1, "first_try": True}
    assert not svb["note_md"].startswith("---")
    assert {"id", "label", "quarter", "value", "display", "forms", "hindsight", "source", "feature",
            "kind"} == set(svb["facts"][0])

    comenity = json.loads((out / "reports" / "57570.json").read_text())
    assert comenity["agents"]["peer"]["ran"] is False
    assert [c["key"] for c in comenity["cards"]] == ["trend", "rule", "summary"]
    assert not re.search(r"\d", comenity["headline"])

    retried = json.loads((out / "reports" / "17438.json").read_text())
    assert retried["agents"]["trend"] == {"ran": True, "attempts": 2, "first_try": False}

    for path in (out / "reports").glob("*.json"):
        report = json.loads(path.read_text())
        for card in report["cards"]:
            assert card["sentences"], (path.name, card["key"])
            for s in card["sentences"]:
                for n in s["numbers"]:
                    assert n["text"] in s["text"], (path.name, n)
