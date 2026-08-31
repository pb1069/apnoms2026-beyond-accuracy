"""Phenomena survey on CIC-IDS2017 — which of the three demo effects hold?

Run after train_cic.py. Read-only exploration; formal demos come after.
"""
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import joblib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def base_signals(base, x):
    p = base.predict_proba(x)
    return p.argmax(1), p.max(1)


def ens_signals(experts, x):
    votes = np.stack([e["model"].predict(x[:, e["subset"]]) for e in experts])
    frac1 = votes.mean(0)
    return (frac1 >= 0.5).astype(int), np.maximum(frac1, 1 - frac1)


def selective(scores, preds, y, label=1):
    best = None
    for t in np.unique(np.round(scores, 4)):
        m = (scores >= t) & (preds == label)
        if m.sum() == 0:
            continue
        if (y[m] == label).mean() >= 1.0:
            c = (float(t), float(m.sum() / len(y)), int((y[m] == label).sum()))
            if best is None or c[1] > best[1]:
                best = c
    return best


def survey(tag, base, experts, x, y):
    pred, conf = base_signals(base, x)
    maj, agree = ens_signals(experts, x)
    c_ok, e_ok = pred == y, maj == y
    n_att = int((y == 1).sum())
    print(f"--- {tag}: n={len(y)} attacks={n_att} ---")
    print(f"  base acc={c_ok.mean():.4f}  conf correct={conf[c_ok].mean():.4f} "
          f"wrong={conf[~c_ok].mean():.4f} sep={conf[~c_ok].mean() - conf[c_ok].mean():+.4f}")
    print(f"  ens  acc={e_ok.mean():.4f}  agree correct={agree[e_ok].mean():.4f} "
          f"wrong={agree[~e_ok].mean():.4f} sep={agree[e_ok].mean() - agree[~e_ok].mean():+.4f}")
    for name, s, p in [("confidence", conf, pred), ("agreement ", agree, maj)]:
        b = selective(s, p, y)
        print(f"  P1.0 {name}: " + (f"thr={b[0]:.3f} cov={b[1]:.2%} TP={b[2]} "
              f"recall={b[2] / max(n_att, 1):.2%}" if b else "unreachable"))
    return dict(acc=float(c_ok.mean()), conf=float(conf.mean()), agree=float(agree.mean()))


def main():
    data = np.load(ROOT / "data" / "cicids.npz")
    std = joblib.load(ROOT / "models" / "cic_std.joblib")
    drift = joblib.load(ROOT / "models" / "cic_drift.joblib")

    print("=== STANDARD SPLIT (tue+wed+thu iid) ===")
    survey("std test", std["base"], std["experts"], data["x_te"], data["y_te"])

    print("\n=== DRIFT TRACK (trained on tue+wed only) ===")
    rows = []
    for tag, xs, ys in [("same-week holdout", "dx_0", "dy_0"),
                        ("thursday (new attacks)", "dx_thu", "dy_thu"),
                        ("friday (new attacks)", "dx_fri", "dy_fri")]:
        rows.append((tag, survey(tag, drift["base"], drift["experts"], data[xs], data[ys])))

    print("\n=== DRIFT SUMMARY (demo-3 signature check) ===")
    print(f"{'slice':<24}{'acc':>8}{'conf':>8}{'agree':>8}")
    for tag, r in rows:
        print(f"{tag:<24}{r['acc']:>8.4f}{r['conf']:>8.4f}{r['agree']:>8.4f}")


if __name__ == "__main__":
    main()
