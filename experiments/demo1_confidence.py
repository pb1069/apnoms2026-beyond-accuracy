"""Demo 1 — Is confidence trustworthy?

Hypothesis: the baseline's confidence does NOT separate correct from wrong
predictions — it is HIGHER on wrong ones. Ensemble agreement separates.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from common import ROOT, baseline_signals, cli_chart, ensemble_signals, load_all, report


def main():
    data, base, experts = load_all()
    x_te, y_te = data["x_te"], data["y_te"]

    pred, conf = baseline_signals(base, x_te)
    maj, agree = ensemble_signals(experts, x_te)
    correct = pred == y_te
    ens_correct = maj == y_te

    metrics = {
        "baseline_acc": round(float(correct.mean()), 4),
        "conf_correct_mean": round(float(conf[correct].mean()), 4),
        "conf_wrong_mean": round(float(conf[~correct].mean()), 4),
        "conf_separation": round(float(conf[~correct].mean() - conf[correct].mean()), 4),
        "ensemble_acc": round(float(ens_correct.mean()), 4),
        "agree_correct_mean": round(float(agree[ens_correct].mean()), 4),
        "agree_wrong_mean": round(float(agree[~ens_correct].mean()), 4),
        "agree_separation": round(float(agree[ens_correct].mean() - agree[~ens_correct].mean()), 4),
    }

    print("=== Demo 1: confidence vs agreement as an error signal ===")
    print(f"baseline acc={metrics['baseline_acc']}  /  ensemble acc={metrics['ensemble_acc']}\n")
    cli_chart("baseline confidence (mean)", [
        ("correct predictions", metrics["conf_correct_mean"]),
        ("wrong predictions", metrics["conf_wrong_mean"], "<- HIGHER when wrong!")])
    print()
    cli_chart("ensemble agreement (mean)", [
        ("correct predictions", metrics["agree_correct_mean"], "<- separates correctly"),
        ("wrong predictions", metrics["agree_wrong_mean"])])
    print(f"\nconfidence separation {metrics['conf_separation']:+.4f} (inverted) / "
          f"agreement separation {metrics['agree_separation']:+.4f}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from plotstyle import CAT, apply
        apply()
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        for ax, sig, ok, title in [(axes[0], conf, correct, "Baseline confidence"),
                                   (axes[1], agree, ens_correct, "Ensemble agreement")]:
            ax.hist(sig[ok], bins=30, color=CAT[0], alpha=0.85, label="correct", density=True)
            ax.hist(sig[~ok], bins=30, color=CAT[1], alpha=0.75, label="wrong", density=True)
            ax.set_title(title)
            ax.set_yticks([])
            ax.legend(loc="upper left")
        fig.tight_layout()
        fig.savefig(ROOT / "results" / "demo1_confidence.png", dpi=150)
        print("[chart] results/demo1_confidence.png")
    except ImportError:
        pass

    ok = report("demo1", metrics)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
