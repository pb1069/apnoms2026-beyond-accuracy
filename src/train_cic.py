"""CIC-IDS2017 track: train baseline + expert ensemble on both splits.

Run after prepare_cicids.py:  python src/train_cic.py
Trains two model sets:
  - standard split (demos 1-2): train on tue+wed+thu mix
  - drift split (demo 3): train on tue+wed only, evaluated day-by-day later
"""
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import joblib
import numpy as np
from sklearn.neural_network import MLPClassifier

import config_cic as CC

ROOT = Path(__file__).resolve().parents[1]


def train_set(x_tr, y_tr, shortcut_idx, tag):
    t0 = time.time()
    d = x_tr.shape[1]
    base = MLPClassifier(hidden_layer_sizes=CC.CIC_BASE_HIDDEN, alpha=CC.CIC_BASE_ALPHA,
                         max_iter=CC.CIC_MAX_ITER, random_state=0, tol=CC.CIC_TOL)
    base.fit(x_tr, y_tr)
    print(f"[{tag}] baseline trained ({time.time() - t0:.0f}s)")

    restricted_pool = [j for j in range(d) if j != shortcut_idx]
    experts = []
    for k in range(CC.CIC_K_EXPERTS):
        r = np.random.default_rng(CC.SEED_CIC + 500 + k)
        if k < CC.CIC_N_UNRESTRICTED:
            sub = np.sort(r.choice(d, CC.CIC_SUB_SIZE, replace=False))
        else:
            sub = np.sort(r.choice(restricted_pool, CC.CIC_SUB_SIZE, replace=False))
        m = MLPClassifier(hidden_layer_sizes=CC.CIC_EXPERT_HIDDEN, alpha=CC.CIC_EXPERT_ALPHA,
                          max_iter=CC.CIC_MAX_ITER, random_state=k, tol=CC.CIC_TOL)
        m.fit(x_tr[:, sub], y_tr)
        experts.append({"model": m, "subset": sub})
        if (k + 1) % 10 == 0:
            print(f"[{tag}] experts {k + 1}/{CC.CIC_K_EXPERTS} ({time.time() - t0:.0f}s)")
    return {"base": base, "experts": experts}


def main():
    data = np.load(ROOT / "data" / "cicids.npz")
    meta = json.loads((ROOT / "data" / "cicids_meta.json").read_text())
    sc = meta["shortcut_index"]
    print(f"[info] {data['x_tr'].shape[1]} features, shortcut index {sc} "
          f"({CC.SHORTCUT_FEATURE})")

    (ROOT / "models").mkdir(exist_ok=True)
    std = train_set(data["x_tr"], data["y_tr"], sc, "std")
    joblib.dump(std, ROOT / "models" / "cic_std.joblib")
    drift = train_set(data["dx_tr"], data["dy_tr"], sc, "drift")
    joblib.dump(drift, ROOT / "models" / "cic_drift.joblib")
    print("[done] models/cic_std.joblib, models/cic_drift.joblib")


if __name__ == "__main__":
    main()
