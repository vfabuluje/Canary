from dataclasses import replace
from datetime import date

import numpy as np
import pytest

from canary.analyst import peers as peers_mod
from canary.analyst import sections
from canary.analyst.facts import build_fact_sheet
from canary.analyst.peers import (
    PEER_KEY,
    PEER_SECTION,
    PEER_SENTENCE,
    PeerResult,
    PeerRow,
    PeerSpecialist,
    render_peer_lines,
    render_peer_table,
)
from canary.analyst.sections import sections_for
from canary.analyst.writer import write_memo
from tests.analyst_fakes import FakeClient, split_memo

CERT = 3
AS_OF = date(2019, 12, 31)


def _row(feature="equity_to_assets", value=12.0, nat=98.2, side="high", peer=62.3, med=9.1,
         reading=peers_mod.READING_HIGH):
    return PeerRow(feature, value, nat, side, peer, med, reading)


def _res(rows=None, basis="specialty_tier", specgrp=4, n=40, tier="$100 million to $1 billion"):
    name = peers_mod.SPECIALTY_NAMES.get(specgrp) if specgrp is not None else None
    return PeerResult(as_of=AS_OF, specgrp=specgrp, specialty_name=name, tier=tier, basis=basis,
                      n_peers=n, rows=rows if rows is not None else [])


def _force(monkeypatch, res):
    monkeypatch.setattr(peers_mod, "compute_peers", lambda quarter, cert, as_of: replace(res, as_of=as_of))
    return res


def _sheet(ctx, tmp_path):
    return build_fact_sheet(ctx, CERT, replay_dir=tmp_path / "none")


def _kind(sheet, kind, feature=None):
    return [f for f in sheet.facts if f.kind == kind and (feature is None or f.feature == feature)]


def test_section_after_trends(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    keys = [s.key for s in sections_for(sheet)]
    i = keys.index("score_history")
    assert keys[i:i + 3] == ["score_history", "trends", "peers"]


def test_real_compute_runs(analyst_ctx, tmp_path):
    sheet = _sheet(analyst_ctx, tmp_path)
    res = sheet.extras[PEER_KEY]
    assert isinstance(res, PeerResult) and res.specgrp == 8


def test_facts_per_ratio_paired(analyst_ctx, tmp_path, monkeypatch):
    rows = [_row("equity_to_assets"), _row("leverage_ratio", 11.0, 3.0, "low", None, None,
                                           peers_mod.READING_TOO_FEW)]
    _force(monkeypatch, _res(rows))
    sheet = _sheet(analyst_ctx, tmp_path)
    for r in rows:
        for kind in ("peer_value", "peer_nat_pct", "peer_nat_dir", "peer_reading"):
            assert len(_kind(sheet, kind, r.feature)) == 1, (kind, r.feature)
        for kind in ("peer_pct", "peer_median"):
            assert len(_kind(sheet, kind, r.feature)) == (0 if r.peer_pct is None else 1)
    (d,) = _kind(sheet, "peer_nat_dir", "leverage_ratio")
    assert d.value == "unusually low"
    (rd,) = _kind(sheet, "peer_reading", "equity_to_assets")
    assert rd.value == peers_mod.READING_HIGH
    for kind in ("peer_specialty", "peer_tier", "peer_basis", "peer_count", "peer_count_unusual",
                 "peer_count_unusual_peers", "peer_count_shown"):
        (f,) = _kind(sheet, kind)
        assert f.feature is None and not f.hindsight and f.quarter == sheet.as_of
    assert _kind(sheet, "peer_count")[0].value == 40
    assert _kind(sheet, "peer_count")[0].label == "Peers: banks in the peer group (including this bank)"
    (cut,) = _kind(sheet, "peer_cutoff")
    assert cut.display == "10%" and {"10%", "10", "10 percent"} <= set(cut.forms)
    assert cut.label == "Peers: cut-off for unusual (top or bottom share of banks)"
    (mn,) = _kind(sheet, "peer_min")
    assert mn.display == "15" and {"15", "fifteen"} <= set(mn.forms)
    assert mn.label == "Peers: minimum peer group size" and mn.feature is None
    assert _kind(sheet, "peer_count_shown")[0].value == 2
    assert _kind(sheet, "peer_count_unusual")[0].value == 2
    assert _kind(sheet, "peer_count_unusual_peers")[0].value == 1
    assert _kind(sheet, "peer_basis")[0].value.startswith("Peers: 40 banks in the same specialty group")


def test_percentile_forms_include_ordinals(analyst_ctx, tmp_path, monkeypatch):
    _force(monkeypatch, _res([_row(nat=98.2, peer=62.3)]))
    sheet = _sheet(analyst_ctx, tmp_path)
    (n,) = _kind(sheet, "peer_nat_pct")
    for x in ("98.2", "98", "98.2%", "98%", "98th", "98.2nd", "98.2th"):
        assert x in n.forms, x
    (p,) = _kind(sheet, "peer_pct")
    assert "62.3" in p.forms and "62nd" in p.forms and "62.3rd" in p.forms
    (v,) = _kind(sheet, "peer_value")
    assert "12.0%" in v.forms


def test_no_nan_facts(analyst_ctx, tmp_path, monkeypatch):
    rows = [_row(), _row("leverage_ratio", float("nan")), _row("return_on_assets", 3.0, float("nan"))]
    _force(monkeypatch, _res(rows))
    sheet = _sheet(analyst_ctx, tmp_path)
    got = [f for f in sheet.facts if f.kind and f.kind.startswith("peer_")]
    assert got
    for f in got:
        assert "nan" not in f.display.lower() and all("nan" not in x.lower() for x in f.forms)
        assert not (isinstance(f.value, float) and np.isnan(f.value))
    assert len(_kind(sheet, "peer_value")) == 1
    assert "nan" not in "\n".join(render_peer_lines(sheet) + render_peer_table(sheet)).lower()


def test_code_lines_general_group(analyst_ctx, tmp_path, monkeypatch):
    general = "This is a general group: the FDIC did not record a lending specialty for this bank."
    for g in (8, 9):
        _force(monkeypatch, _res([_row()], specgrp=g))
        sheet = _sheet(analyst_ctx, tmp_path)
        lines = render_peer_lines(sheet)
        assert general in lines
        assert lines[0] == (f"The FDIC's specialty group for this bank at {sheet.as_of}: "
                            f"{peers_mod.SPECIALTY_NAMES[g]}.")
    _force(monkeypatch, _res([_row()], specgrp=7))
    lines = render_peer_lines(_sheet(analyst_ctx, tmp_path))
    assert general not in lines and lines[0].startswith("The FDIC's specialty group")


def test_basis_lines(analyst_ctx, tmp_path, monkeypatch):
    as_of = _sheet(analyst_ctx, tmp_path).as_of
    cases = [
        (_res([_row()], "specialty_tier", 4, 40, "$1 billion to $10 billion"),
         "Peers: 40 banks in the same specialty group and size tier ($1 billion to $10 billion)."),
        (_res([_row()], "specialty", 4, 22),
         "Peers: 22 banks in the same specialty group (all sizes), because fewer than 15 shared its size tier."),
        (_res([_row()], "too_few", 4, 9),
         "There are not enough comparable banks (9 in its specialty group) for a reliable comparison, "
         "so none is shown."),
        (_res([], "no_specialty", None, 0),
         f"The FDIC recorded no specialty group for this bank at {as_of}, so no peer comparison is shown."),
    ]
    for res, line in cases:
        _force(monkeypatch, res)
        sheet = _sheet(analyst_ctx, tmp_path)
        lines = render_peer_lines(sheet)
        assert lines[-1] == line and line in lines
        (b,) = _kind(sheet, "peer_basis")
        assert b.value == line
        if res.specgrp is None:
            assert not any("specialty group for this bank at" in x and "recorded" not in x for x in lines)
            assert _kind(sheet, "peer_specialty") == []


@pytest.mark.parametrize("res", [
    _res([_row(reading="")], "too_few", 4, 9),
    _res([], "no_specialty", None, 0),
    _res([], "specialty_tier"),
])
def test_code_only_cases(analyst_ctx, tmp_path, monkeypatch, res):
    from tests.test_analyst_writer import _memo

    _force(monkeypatch, res)
    sheet = _sheet(analyst_ctx, tmp_path)
    assert PEER_KEY in sheet.code_only
    assert next(s for s in sections_for(sheet) if s.key == PEER_KEY).ai_written is False
    out = render_peer_table(sheet)
    assert out.count(PEER_SENTENCE) == 1 and out[-1] == PEER_SENTENCE
    assert not any(x.startswith("| Ratio") for x in out)
    if res.basis == "specialty_tier":
        assert f"None of this bank's ratios were in the national top or bottom 10% at {sheet.as_of}." in out
    else:
        assert out == [PEER_SENTENCE]
    client = FakeClient(split_memo(sheet, _memo(sheet)))
    r = write_memo(analyst_ctx, CERT, client=client, out_dir=tmp_path / "banks", replay_dir=tmp_path / "none")
    assert r.ok, r.errors
    assert len(client.calls) == 2  # trend and analyst only: the peer section is code-only here
    assert not any("peer agent" in c["system"] for c in client.calls)
    user = client.calls[-1]["messages"][0]["content"]
    assert '"Compared with similar banks"' not in user
    text = r.path.read_text()
    assert "## Compared with similar banks" in text and text.count(PEER_SENTENCE) == 1


def test_full_note_layout(analyst_ctx, tmp_path, monkeypatch):
    from tests.test_analyst_writer import _memo

    rows = [_row("equity_to_assets"), _row("leverage_ratio", 11.0, 3.0, "low", None, None,
                                           peers_mod.READING_TOO_FEW)]
    _force(monkeypatch, _res(rows))
    sheet = _sheet(analyst_ctx, tmp_path)
    assert PEER_KEY not in sheet.code_only
    client = FakeClient(split_memo(sheet, _memo(sheet)))
    r = write_memo(analyst_ctx, CERT, client=client, out_dir=tmp_path / "banks", replay_dir=tmp_path / "none")
    assert r.ok, r.errors
    peer_call = next(c for c in client.calls if "peer agent" in c["system"])
    assert "Code adds the table and fixed sentences around your peers section" in peer_call["messages"][0]["content"]
    text = r.path.read_text()
    head = text.index("## Compared with similar banks")
    spec = text.index("The FDIC's specialty group for this bank")
    ai = text.index("The bank looked weak in plain terms.", head)
    table = text.index("| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |")
    assert head < spec < ai < table
    assert text.count(PEER_SENTENCE) == 1
    assert "98.2nd" in text and "n/a" in text
    assert text.index("## How its ratios moved") < head


def test_registered_once():
    import canary.analyst.writer  # noqa: F401

    keys = [sp.key for sp in sections.SPECIALISTS]
    assert keys.count(PEER_KEY) == 1 and keys.index("trends") < keys.index(PEER_KEY)
    saved = list(sections.SPECIALISTS)
    try:
        sections.register(PeerSpecialist())
        assert [sp.key for sp in sections.SPECIALISTS].count(PEER_KEY) == 1
    finally:
        sections.SPECIALISTS[:] = saved


def test_section_definition():
    s = PEER_SECTION
    assert (s.key, s.title, s.window, s.ai_written) == ("peers", "Compared with similar banks", "as_of", True)
    assert s.render is render_peer_table and s.render_before is render_peer_lines
    ins = s.instructions.lower()
    assert "fixed sentence" not in ins and "one ratio per sentence" in ins
    assert "risky" in ins and "predict" in ins and "forecast" in ins
    assert PEER_SENTENCE == ("This section only compares the bank with banks the FDIC groups with it; an unusual "
                             "figure is not a prediction of failure, and the comparison has not been tested "
                             "as a warning signal.")


def test_specialty_is_the_as_of_quarters(analyst_ctx):
    import pandas as pd

    as_of = date(2018, 12, 31)
    ts = pd.Timestamp(as_of)
    spec = analyst_ctx.specialty.copy()
    is_bank = spec["cert"] == CERT
    spec.loc[is_bank & (spec["report_date"] == ts), "specgrp"] = 6
    spec.loc[is_bank & (spec["report_date"] > ts), "specgrp"] = 9
    ctx = replace(analyst_ctx, specialty=spec)
    rows = peers_mod._quarter_rows(ctx, as_of)
    assert int(rows.loc[rows["cert"] == CERT, "specgrp"].iloc[0]) == 6
    result = peers_mod.compute_peers(rows, CERT, as_of)
    assert result.specgrp == 6
