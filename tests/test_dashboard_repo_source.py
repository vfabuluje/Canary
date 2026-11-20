import importlib.util
import os
import sys
import time
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location(
    "repo_source", Path(__file__).resolve().parents[1] / "dashboard" / "repo_source.py")
repo_source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repo_source)


@pytest.fixture
def isolated(monkeypatch, tmp_path):
    """Run with a fake `canary` package so the real one in sys.modules is never touched."""
    saved = {m: sys.modules.pop(m) for m in list(sys.modules) if m == "canary" or m.startswith("canary.")}
    monkeypatch.setattr(sys, "path", list(sys.path))
    monkeypatch.delenv(repo_source.STAMP_ENV, raising=False)
    yield tmp_path
    for m in [m for m in sys.modules if m == "canary" or m.startswith("canary.")]:
        del sys.modules[m]
    sys.modules.update(saved)


def _package(root: Path) -> Path:
    src = root / "src"
    (src / "canary").mkdir(parents=True)
    (src / "canary" / "__init__.py").write_text("")
    (src / "canary" / "mod.py").write_text("X = 1\n")
    return src


def test_stale_installed_copy_is_replaced_by_src(isolated):
    src = _package(isolated / "repo")
    old = _package(isolated / "site")
    sys.path.insert(0, str(old))
    import canary  # noqa: F401  (the "installed" copy)
    assert repo_source.use_repo_source(src) is True
    assert sys.path[0] == str(src)
    import canary as fresh
    assert Path(fresh.__file__).resolve().is_relative_to(src.resolve())


def test_src_moves_ahead_of_an_installed_copy_already_on_the_path(isolated):
    src = _package(isolated / "repo")
    old = _package(isolated / "site")
    sys.path[:0] = [str(old), str(src)]  # src present, but behind the old copy
    import canary  # noqa: F401
    assert repo_source.use_repo_source(src) is True
    assert sys.path[0] == str(src) and sys.path.count(str(src)) == 1
    import canary as fresh
    assert Path(fresh.__file__).resolve().is_relative_to(src.resolve())


def test_no_reload_when_already_from_src_and_unchanged(isolated):
    src = _package(isolated / "repo")
    sys.path.insert(0, str(src))
    import canary.mod  # noqa: F401
    assert repo_source.use_repo_source(src) is False
    assert repo_source.use_repo_source(src) is False
    assert "canary.mod" in sys.modules


def test_changed_file_triggers_reload(isolated):
    src = _package(isolated / "repo")
    sys.path.insert(0, str(src))
    import canary.mod  # noqa: F401
    repo_source.use_repo_source(src)
    time.sleep(0.01)
    (src / "canary" / "new.py").write_text("Y = 2\n")
    assert repo_source.use_repo_source(src) is True
    assert "canary.mod" not in sys.modules
    from canary import new
    assert new.Y == 2


def test_pycache_does_not_count_as_a_change(isolated):
    src = _package(isolated / "repo")
    sys.path.insert(0, str(src))
    import canary  # noqa: F401
    repo_source.use_repo_source(src)
    (src / "canary" / "__pycache__").mkdir(exist_ok=True)
    (src / "canary" / "__pycache__" / "mod.cpython-312.pyc").write_bytes(b"x")
    assert repo_source.use_repo_source(src) is False


def test_missing_src_is_a_no_op(isolated):
    assert repo_source.use_repo_source(isolated / "nope") is False
    assert os.environ.get(repo_source.STAMP_ENV) is None
