"""Demo 3 — What do the signals do under concept drift?

Hypothesis: as drift grows, accuracy collapses while the baseline gets MORE
confident; ensemble agreement degrades and flags the problem.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import config as C
from common import ROOT, baseline_signals, ensemble_signals, load_all, report
from datagen import make_x


def main():
    data, base, experts = load_all()
    y_te = data["y_te"]

    print("=== Demo 3: signal behavior under concept drift ===")
    print(f"{'sigma':>6}{'accuracy':>10}{'confidence':>12}{'agreement':>11}")
    metrics = {}
    series = []
    for sigma in C.DRIFT_SIGMAS:
        x_d, _ = make_x(
            y_te, C.SEED_DRIFT_X,
            broken_frac=C.BROKEN_FRAC + C.DRIFT_BROKEN_STEP * sigma,
            sc_scale=1 + C.DRIFT_SC_GAIN * sigma,
            inf_scale=1 / (1 + C.DRIFT_INF_DECAY * sigma),
        )
        pred, conf = baseline_signals(base, x_d)
        _, agree = ensemble_signals(experts, x_d)
        acc = float((pred == y_te).mean())
        row = {"acc": round(acc, 4), "conf": round(float(conf.mean()), 4),
               "agree": round(float(agree.mean()), 4)}
        series.append((sigma, row))
        tag = str(sigma).replace(".", "_")
        for k, v in row.items():
            metrics[f"sigma{tag}_{k}"] = v
        print(f"{sigma:>6.1f}{row['acc']:>10.4f}{row['conf']:>12.4f}{row['agree']:>11.4f}")

    a0, a3 = series[0][1], series[-1][1]
    print(f"\ndrift sigma=0 -> {series[-1][0]}: "
          f"accuracy {a0['acc']:.2f} -> {a3['acc']:.2f} (collapse), "
          f"confidence {a0['conf']:.3f} -> {a3['conf']:.3f} (UP!), "
          f"agreement {a0['agree']:.3f} -> {a3['agree']:.3f} (down => detectable)")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4))
        xs = [s for s, _ in series]
        for key, label in [("acc", "accuracy"), ("conf", "baseline confidence"),
                           ("agree", "ensemble agreement")]:
            ax.plot(xs, [r[key] for _, r in series], marker="o", label=label)
        ax.set_xlabel("drift intensity (sigma)"); ax.legend(); ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(ROOT / "results" / "demo3_drift.png", dpi=150)
        print("[chart] results/demo3_drift.png")
    except ImportError:
        pass

    ok = report("demo3", metrics)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
