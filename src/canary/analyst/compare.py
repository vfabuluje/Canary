"""Model comparison (spec 10): write the same memos with several models through the normal API
and report checker pass rate, tokens and cost per model. Notes go to out_dir/<model>/, never banks/.
"""

import json
import logging
from pathlib import Path

from canary.analyst.writer import write_memo
from canary.model.train import CASE_STUDY_CERTS

log = logging.getLogger(__name__)
DEFAULT_MODELS = ("claude-opus-5-5", "claude-sonnet-5-5")


def compare_models(ctx, client, models=DEFAULT_MODELS, certs=None,
                   out_dir: Path = Path("data/analyst/compare"), replay_dir: Path = Path("data/replay")) -> dict:
    certs = tuple(certs) if certs is not None else tuple(CASE_STUDY_CERTS)
    out_dir = Path(out_dir)
    per_model: dict[str, dict] = {}
    memos: list[dict] = []
    for model in models:
        agg = {"passed_first_try": 0, "passed_after_retry": 0, "failed": 0,
               "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0}
        per_model[model] = agg
        for cert in certs:
            entry = {"cert": cert, "model": model, "served_model": None, "path": None, "attempts": 0,
                     "ok": False, "errors": [], "first_errors": []}
            try:
                res = write_memo(ctx, cert, client=client, model=model, out_dir=out_dir / model,
                                 replay_dir=replay_dir)
            except Exception as exc:  # one memo must never abort the comparison
                entry.update(attempts=1, errors=[f"{type(exc).__name__}: {exc}"])
                agg["failed"] += 1
                u = getattr(exc, "usage", None) or {}  # calls made before the exception still cost money
                agg["input_tokens"] += u.get("input_tokens", 0)
                agg["output_tokens"] += u.get("output_tokens", 0)
                agg["cost_usd"] += u.get("cost_usd", 0.0)
                entry["served_model"] = u.get("model")
                log.warning("compare: %s cert %s failed: %s", model, cert, exc)
            else:
                entry.update(path=str(res.path) if res.path else None, attempts=res.attempts,
                             ok=res.ok, errors=res.errors, first_errors=res.first_errors, served_model=res.model)
                agg["input_tokens"] += res.input_tokens
                agg["output_tokens"] += res.output_tokens
                agg["cost_usd"] += res.cost_usd
                if not res.ok:
                    agg["failed"] += 1
                elif res.attempts == 1:
                    agg["passed_first_try"] += 1
                else:
                    agg["passed_after_retry"] += 1
            memos.append(entry)
    report = {"models": per_model, "memos": memos}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "compare.json").write_text(json.dumps(report, indent=2))
    return report
