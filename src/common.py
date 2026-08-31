"""Shared helpers for the demo scripts: loading, signals, verification."""
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

SRC = Path(__file__).parent
sys.path.insert(0, str(SRC))

import joblib
import numpy as np

import config as C

ROOT = SRC.resolve().parent


def load_all():
    (ROOT / "results").mkdir(exist_ok=True)
    data = np.load(ROOT / "data" / "dataset.npz")
    base = joblib.load(ROOT / "models" / "baseline.joblib")
    experts = joblib.load(ROOT / "models" / "experts.joblib")
    return data, base, experts


def baseline_signals(base, x):
    p = base.predict_proba(x)
    return p.argmax(1), p.max(1)                     # prediction, confidence


def ensemble_signals(experts, x):
    votes = np.stack([e["model"].predict(x[:, e["subset"]]) for e in experts])
    frac1 = votes.mean(0)
    maj = (frac1 >= 0.5).astype(int)
    agree = np.maximum(frac1, 1 - frac1)             # fraction agreeing with majority
    return maj, agree


def selective_best(scores, preds, y, label=1, target_precision=1.0):
    """Highest-coverage threshold whose accepted attack predictions reach the
    target precision. Returns (threshold, coverage, tp) or None."""
    best = None
    for t in np.unique(np.round(scores, 4)):
        m = (scores >= t) & (preds == label)
        if m.sum() == 0:
            continue
        if (y[m] == label).mean() >= target_precision:
            cand = (float(t), float(m.sum() / len(y)), int((y[m] == label).sum()))
            if best is None or cand[1] > best[1]:
                best = cand
    return best


def cli_bar(label, value, vmax=1.0, width=36, mark=""):
    """Terminal bar chart line: `label |##########----| 0.961`."""
    n = 0 if vmax == 0 else max(0, min(width, round(width * value / vmax)))
    val = f"{value:,}" if isinstance(value, int) else f"{value:.4f}"
    return f"  {label:<22} |{'#' * n}{'-' * (width - n)}| {val}{' ' + mark if mark else ''}"


def cli_chart(title, rows, vmax=1.0):
    """rows: list of (label, value[, mark]) — prints an ASCII bar chart."""
    print(f"  {title}")
    for row in rows:
        print(cli_bar(*row[:2], vmax=vmax, mark=row[2] if len(row) > 2 else ""))


def report(name, metrics):
    """Write results/<name>.json and verify against expected_outputs/<name>.json."""
    results_dir = ROOT / "results"
    results_dir.mkdir(exist_ok=True)
    out = results_dir / f"{name}.json"
    out.write_text(json.dumps(metrics, indent=2))
    print(f"\n[{name}] results written to {out.relative_to(ROOT)}")

    exp_path = ROOT / "expected_outputs" / f"{name}.json"
    if not exp_path.exists():
        print(f"[{name}] no expected_outputs baseline found - reference run?")
        return True
    expected = json.loads(exp_path.read_text())
    ok = True
    print(f"[{name}] verification vs expected_outputs (tolerance +/-{C.TOLERANCE}):")
    for key, exp_val in expected.items():
        got = metrics.get(key)
        if isinstance(exp_val, (int, float)) and isinstance(got, (int, float)):
            passed = abs(got - exp_val) <= C.TOLERANCE
        else:
            passed = got == exp_val
        ok &= passed
        print(f"  {'PASS' if passed else 'FAIL'}  {key}: got={got}  expected={exp_val}")
    print(f"[{name}] {'ALL CHECKS PASSED' if ok else 'VERIFICATION FAILED'}")
    return ok
