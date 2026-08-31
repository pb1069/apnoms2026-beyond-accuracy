"""Setup step: generate the pinned dataset and train baseline + expert ensemble.

Run from the repo root:  python src/train.py
Outputs: data/dataset.npz (+ sha256), models/baseline.joblib, models/experts.joblib
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

import config as C
from datagen import content_digest, make_labels, make_x

ROOT = Path(__file__).resolve().parents[1]


def main():
    t0 = time.time()
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "models").mkdir(exist_ok=True)

    # ---- dataset (pinned) ------------------------------------------------
    y_tr, y_te = make_labels()
    x_tr, _ = make_x(y_tr, C.SEED_TRAIN_X)
    x_te, broken = make_x(y_te, C.SEED_TEST_X, broken_frac=C.BROKEN_FRAC)

    npz = ROOT / "data" / "dataset.npz"
    np.savez_compressed(npz, x_tr=x_tr, y_tr=y_tr, x_te=x_te, y_te=y_te, broken=broken)
    digest = content_digest(x_tr, y_tr, x_te, y_te, broken)
    (ROOT / "data" / "checksums.txt").write_text(f"{digest}  dataset.npz (content digest)\n")
    print(f"[data] dataset.npz written  content sha256={digest[:16]}...")

    # ---- baseline --------------------------------------------------------
    base = MLPClassifier(hidden_layer_sizes=C.BASE_HIDDEN, alpha=C.BASE_ALPHA,
                         max_iter=C.BASE_MAX_ITER, random_state=C.BASE_SEED,
                         tol=C.BASE_TOL)
    base.fit(x_tr, y_tr)
    acc = base.score(x_te, y_te)
    joblib.dump(base, ROOT / "models" / "baseline.joblib")
    print(f"[baseline] trained  test acc={acc:.4f}")

    # ---- expert ensemble (diversity-constrained subsets) -----------------
    others = [j for j in range(C.D) if j != C.SHORTCUT]
    experts = []
    for k in range(C.K_EXPERTS):
        r = np.random.default_rng(C.SUBSET_SEED_BASE + k)
        if k < C.N_SC_EXPERTS:
            sub = np.sort(np.append(r.choice(others, C.SUB_SIZE - 1, replace=False), C.SHORTCUT))
        else:
            sub = np.sort(r.choice(others, C.SUB_SIZE, replace=False))
        m = MLPClassifier(hidden_layer_sizes=C.EXPERT_HIDDEN, alpha=C.EXPERT_ALPHA,
                          max_iter=C.EXPERT_MAX_ITER, random_state=k, tol=C.EXPERT_TOL)
        m.fit(x_tr[:, sub], y_tr)
        experts.append({"model": m, "subset": sub})
        if (k + 1) % 10 == 0:
            print(f"[experts] {k + 1}/{C.K_EXPERTS} trained")
    joblib.dump(experts, ROOT / "models" / "experts.joblib")

    votes = np.stack([e["model"].predict(x_te[:, e["subset"]]) for e in experts])
    maj = (votes.mean(0) >= 0.5).astype(int)
    print(f"[ensemble] majority-vote test acc={(maj == y_te).mean():.4f}")

    meta = {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "sklearn": __import__("sklearn").__version__,
        "dataset_sha256": digest,
        "elapsed_sec": round(time.time() - t0, 1),
    }
    (ROOT / "models" / "meta.json").write_text(json.dumps(meta, indent=2))
    print(f"[done] setup complete in {meta['elapsed_sec']}s - run experiments/demo*.py next")


if __name__ == "__main__":
    main()
