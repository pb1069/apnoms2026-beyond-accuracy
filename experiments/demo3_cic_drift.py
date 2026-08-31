"""Demo 3 — Real-world drift on CIC-IDS2017.

Models trained ONLY on Tuesday+Wednesday traffic, evaluated on:
  - a same-week holdout (no drift)
  - Thursday (web attacks / infiltration — new, rare)
  - Friday (botnet / portscan / DDoS — new, massive)

Hypothesis: accuracy collapses on Friday while per-sample signal MEANS
(confidence, agreement) stay silent — but distribution/rate signals move.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import joblib
import numpy as np

from common import ROOT, cli_chart, report, selective_best

SLICES = [("holdout", "dx_0", "dy_0"),
          ("thursday", "dx_thu", "dy_thu"),
          ("friday", "dx_fri", "dy_fri")]


def main():
    data = np.load(ROOT / "data" / "cicids.npz")
    models = joblib.load(ROOT / "models" / "cic_drift.joblib")
    base, experts = models["base"], models["experts"]
    (ROOT / "results").mkdir(exist_ok=True)

    def signals(x):
        p = base.predict_proba(x)
        votes = np.stack([e["model"].predict(x[:, e["subset"]]) for e in experts])
        f1 = votes.mean(0)
        return (p.argmax(1), p.max(1),
                (f1 >= 0.5).astype(int), np.maximum(f1, 1 - f1))

    # pin the precision-1.0 confidence threshold on the NO-DRIFT holdout
    x0, y0 = data["dx_0"], data["dy_0"]
    p0, c0, _, _ = signals(x0)
    thr = selective_best(c0, p0, y0)[0]

    print("=== Demo 3: real-world drift (CIC-IDS2017, trained on Tue+Wed) ===")
    print(f"precision-1.0 confidence threshold tuned on holdout: {thr:.3f}\n")

    metrics = {"tuned_threshold": round(thr, 4)}
    rows = {}
    for tag, xs, ys in SLICES:
        x, y = data[xs], data[ys]
        pred, conf, maj, agree = signals(x)
        r = {
            "acc": float((pred == y).mean()),
            "conf": float(conf.mean()),
            "agree": float(agree.mean()),
            "pred_attack_rate": float((pred == 1).mean()),
            "accept_rate": float(((conf >= thr) & (pred == 1)).mean()),
            "wrong_conf90": int(((conf >= 0.9) & (pred != y)).sum()),
        }
        rows[tag] = r
        for k, v in r.items():
            metrics[f"{tag}_{k}"] = round(v, 4) if isinstance(v, float) else v

    for key, title, mark_slice in [
            ("acc", "accuracy (needs labels - invisible in production!)", "friday"),
            ("conf", "mean confidence (label-free)", None),
            ("agree", "mean agreement (label-free)", None),
            ("pred_attack_rate", "predicted-attack rate (label-free)", "friday"),
            ("accept_rate", f"accept rate @ conf>={thr:.3f} (label-free)", "friday")]:
        cli_chart(title, [(tag, rows[tag][key], "<-" if tag == mark_slice else "")
                          for tag, _, _ in SLICES])
        print()

    h, f = rows["holdout"], rows["friday"]
    print(f"holdout -> friday: accuracy {h['acc']:.3f} -> {f['acc']:.3f} (COLLAPSE)")
    print(f"  confidence mean {h['conf']:.3f} -> {f['conf']:.3f}  (silent)")
    print(f"  agreement  mean {h['agree']:.3f} -> {f['agree']:.3f}  (silent)")
    print(f"  {f['wrong_conf90']} wrong predictions on friday carry confidence >= 0.9")
    print(f"  predicted-attack rate {h['pred_attack_rate']:.1%} -> {f['pred_attack_rate']:.1%}  (MOVES)")
    print(f"  accept rate           {h['accept_rate']:.1%} -> {f['accept_rate']:.1%}  (MOVES)")
    print("=> per-sample means lie under real drift; watch the RATES.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(11, 4))
        xs = [t for t, _, _ in SLICES]
        for key, label in [("acc", "accuracy"), ("conf", "confidence"), ("agree", "agreement")]:
            axes[0].plot(xs, [rows[t][key] for t in xs], marker="o", label=label)
        axes[0].set_title("per-sample means"); axes[0].legend(); axes[0].grid(alpha=0.3)
        for key, label in [("pred_attack_rate", "predicted-attack rate"),
                           ("accept_rate", "accept rate")]:
            axes[1].plot(xs, [rows[t][key] for t in xs], marker="s", label=label)
        axes[1].set_title("rate signals (label-free)"); axes[1].legend(); axes[1].grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(ROOT / "results" / "demo3_cic_drift.png", dpi=150)
        print("[chart] results/demo3_cic_drift.png")
    except ImportError:
        pass

    ok = report("demo3_cic", metrics)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
