"""Environment + artifact smoke test. Exit 0 = ready for demos."""
import importlib.metadata
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
ok = True


def check(name, passed, detail=""):
    global ok
    ok &= bool(passed)
    print(f"  {'PASS' if passed else 'FAIL'}  {name}{'  ' + detail if detail else ''}")


print("[smoke] library versions vs requirements.txt")
for line in (ROOT / "requirements.txt").read_text().split():
    pkg, want = line.strip().split("==")
    try:
        got = importlib.metadata.version(pkg)
        check(pkg, got == want, f"got {got}, want {want}")
    except importlib.metadata.PackageNotFoundError:
        check(pkg, False, "not installed")

print("[smoke] artifacts")
npz = ROOT / "data" / "dataset.npz"
check("data/dataset.npz exists", npz.exists())
if npz.exists():
    import numpy as np
    from datagen import content_digest
    d = np.load(npz)
    got = content_digest(d["x_tr"], d["y_tr"], d["x_te"], d["y_te"], d["broken"])
    if (ROOT / "data" / "checksums.txt").exists():
        want = (ROOT / "data" / "checksums.txt").read_text().split()[0]
        check("dataset checksum", got == want)
    exp = ROOT / "expected_outputs" / "dataset.sha256"
    if exp.exists():
        check("dataset matches pinned reference", got == exp.read_text().split()[0])
check("models/baseline.joblib exists", (ROOT / "models" / "baseline.joblib").exists())
check("models/experts.joblib exists", (ROOT / "models" / "experts.joblib").exists())

# ---- model verification: shipped models must reproduce pinned metrics ----
print("[smoke] model verification (predictions vs pinned reference)")
import json

import joblib

TOL = 5e-3
exp1 = ROOT / "expected_outputs" / "demo1.json"
if npz.exists() and exp1.exists() and (ROOT / "models" / "experts.joblib").exists():
    import numpy as np
    d = np.load(npz)
    e = json.loads(exp1.read_text())
    base = joblib.load(ROOT / "models" / "baseline.joblib")
    acc = base.score(d["x_te"], d["y_te"])
    check("synthetic baseline accuracy", abs(acc - e["baseline_acc"]) <= TOL,
          f"got {acc:.4f}, pinned {e['baseline_acc']}")
    experts = joblib.load(ROOT / "models" / "experts.joblib")
    votes = np.stack([m["model"].predict(d["x_te"][:, m["subset"]]) for m in experts])
    eacc = ((votes.mean(0) >= 0.5).astype(int) == d["y_te"]).mean()
    check("synthetic ensemble accuracy", abs(eacc - e["ensemble_acc"]) <= TOL,
          f"got {eacc:.4f}, pinned {e['ensemble_acc']}")

# ---- CIC track (optional: only checked when its artifacts are present) ---
cic_npz = ROOT / "data" / "cicids.npz"
cic_exp = ROOT / "expected_outputs" / "cicids.sha256"
if cic_npz.exists():
    print("[smoke] CIC-IDS2017 track")
    import numpy as np
    from datagen import content_digest
    d = np.load(cic_npz)
    got = content_digest(*[d[k] for k in sorted(d.files)])
    if cic_exp.exists():
        check("cicids.npz matches pinned reference", got == cic_exp.read_text().split()[0])
    exp3 = ROOT / "expected_outputs" / "demo3_cic.json"
    if (ROOT / "models" / "cic_drift.joblib").exists() and exp3.exists():
        e3 = json.loads(exp3.read_text())
        drift = joblib.load(ROOT / "models" / "cic_drift.joblib")
        acc0 = drift["base"].score(d["dx_0"], d["dy_0"])
        check("CIC drift-baseline holdout accuracy", abs(acc0 - e3["holdout_acc"]) <= TOL,
              f"got {acc0:.4f}, pinned {e3['holdout_acc']}")
else:
    print("[smoke] CIC-IDS2017 track: not prepared (optional) - "
          "run: python scripts/run_pipeline.py --track cic")

print(f"[smoke] {'READY' if ok else 'NOT READY - see FAIL lines above'}")
sys.exit(0 if ok else 1)
