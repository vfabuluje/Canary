"""Make the app run the repo's current `canary` code, also on Streamlit Community Cloud.

Cloud installs a copy of the package once (requirements.txt) and keeps it; a push only updates the repo
files, and Streamlit reloads changed modules only under dashboard/. So the app imports `canary` from the
repo's src/ folder, and when any file there changes (a new deploy), it drops the loaded `canary` modules
so the next import reads the new code. No-op when the loaded copy is already src/ and nothing changed
(local runs, tests).
"""

import importlib
import os
import sys
from pathlib import Path

STAMP_ENV = "CANARY_SRC_STAMP"


def _stamp(src: Path) -> str:
    """Newest change time and count of the package's source files (not __pycache__, which imports rewrite)."""
    files = [p for p in src.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
    return f"{max((p.stat().st_mtime_ns for p in files), default=0)}:{len(files)}"


def _loaded_from(src: Path) -> bool:
    pkg = sys.modules.get("canary")
    path = getattr(pkg, "__file__", None)
    return path is not None and Path(path).resolve().is_relative_to(src.resolve())


def use_repo_source(src: Path) -> bool:
    """Put `src` first on sys.path and drop stale `canary` modules. Returns True when it dropped them."""
    if not src.is_dir():
        return False
    if sys.path[:1] != [str(src)]:  # first, even if it is already further down (an editable install)
        sys.path[:] = [str(src)] + [p for p in sys.path if p != str(src)]
    stamp, previous = _stamp(src), os.environ.get(STAMP_ENV)
    stale = "canary" in sys.modules and (not _loaded_from(src) or (previous is not None and previous != stamp))
    if stale:
        for name in [m for m in sys.modules if m == "canary" or m.startswith("canary.")]:
            del sys.modules[name]
        importlib.invalidate_caches()
    os.environ[STAMP_ENV] = stamp
    return stale
