"""Demo 2 — Selective prediction at Precision 1.0.

Hypothesis: to reach 100% precision on attack alerts, a confidence threshold
must sacrifice nearly all coverage; ensemble agreement keeps far more.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from common import (ROOT, baseline_signals, cli_chart, ensemble_signals, load_all,
                    report, selective_best)


def main():
    data, base, experts = load_all()
    x_te, y_te = data["x_te"], data["y_te"]
    n_attack = int((y_te == 1).sum())

    pred, conf = baseline_signals(base, x_te)
    maj, agree = ensemble_signals(experts, x_te)

    rows = {}
    for name, scores, preds in [("confidence", conf, pred), ("agreement", agree, maj)]:
        best = selective_best(scores, preds, y_te)
        if best is None:
            rows[name] = None
        else:
            thr, cov, tp = best
            rows[name] = {"threshold": round(thr, 4), "coverage": round(cov, 4),
                          "tp": tp, "recall": round(tp / n_attack, 4)}

    print("=== Demo 2: precision-1.0 selective prediction ===")
    print(f"test samples={len(y_te)}  attacks={n_attack}")
    print(f"{'method':<12}{'threshold':>10}{'coverage':>10}{'TP':>7}{'recall':>9}")
    for name, r in rows.items():
        if r is None:
            print(f"{name:<12}{'precision 1.0 unreachable':>36}")
        else:
            print(f"{name:<12}{r['threshold']:>10.3f}{r['coverage']:>9.2%}{r['tp']:>7}{r['recall']:>8.2%}")

    metrics = {"n_test": len(y_te), "n_attack": n_attack}
    for name, r in rows.items():
        if r:
            for k, v in r.items():
                metrics[f"{name}_{k}"] = v
    if rows["confidence"] and rows["agreement"]:
        ratio = rows["agreement"]["tp"] / max(rows["confidence"]["tp"], 1)
        metrics["tp_ratio_agreement_over_confidence"] = round(ratio, 2)
        print()
        cli_chart("attacks detected at precision 1.0", [
            ("confidence", rows["confidence"]["tp"]),
            ("agreement", rows["agreement"]["tp"], f"<- {ratio:.1f}x more")],
            vmax=max(rows["agreement"]["tp"], rows["confidence"]["tp"]))
        print(f"\nAt precision 1.0, agreement detects {ratio:.1f}x more attacks than confidence.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4))
        names = [n for n, r in rows.items() if r]
        ax.bar(names, [rows[n]["tp"] for n in names], color=["#c44", "#286"])
        ax.set_ylabel("attacks detected at precision 1.0")
        for i, n in enumerate(names):
            ax.text(i, rows[n]["tp"], str(rows[n]["tp"]), ha="center", va="bottom")
        fig.tight_layout()
        fig.savefig(ROOT / "results" / "demo2_selective.png", dpi=150)
        print("[chart] results/demo2_selective.png")
    except ImportError:
        pass

    ok = report("demo2", metrics)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
