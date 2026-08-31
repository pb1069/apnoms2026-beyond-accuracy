"""One-command pipeline: preprocessing -> training -> analysis -> visualization.

Usage:
  python scripts/run_pipeline.py --track synthetic   # lab 1 (fast, offline)
  python scripts/run_pipeline.py --track cic         # lab 2 (downloads 844MB once)
  python scripts/run_pipeline.py --track all

Idempotent: completed stages are skipped (delete their outputs to force a rerun).
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SYNTHETIC = [
    ("generate data + train models", "src/train.py", ["data/dataset.npz", "models/experts.joblib"]),
    ("verify artifacts", "scripts/smoke_test.py", []),
    ("demo 1: confidence vs agreement", "experiments/demo1_confidence.py", []),
    ("demo 2: selective prediction", "experiments/demo2_selective.py", []),
    ("extra: synthetic drift", "experiments/demo3_drift.py", []),
]
CIC = [
    ("download CIC-IDS2017 (844MB, once)", "src/download_cicids.py",
     ["data/cicids.npz"]),                       # skip download if prepared npz exists
    ("preprocess into pinned splits", "src/prepare_cicids.py", ["data/cicids.npz"]),
    ("train baseline + 40x2 experts (~5 min)", "src/train_cic.py",
     ["models/cic_std.joblib", "models/cic_drift.joblib"]),
    ("demo 3: real-world day drift", "experiments/demo3_cic_drift.py", []),
]


def run(stages):
    for i, (label, script, done_markers) in enumerate(stages, 1):
        banner = f"[{i}/{len(stages)}] {label}"
        if done_markers and all((ROOT / m).exists() for m in done_markers):
            print(f"{banner} - already done, skipping ({', '.join(done_markers)})")
            continue
        print(f"\n{'=' * 70}\n{banner}\n{'=' * 70}")
        t0 = time.time()
        r = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT)
        print(f"[stage] {'OK' if r.returncode == 0 else 'FAILED'} in {time.time() - t0:.0f}s")
        if r.returncode != 0:
            sys.exit(r.returncode)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", choices=["synthetic", "cic", "all"], default="all")
    a = ap.parse_args()
    if a.track in ("synthetic", "all"):
        run(SYNTHETIC)
    if a.track in ("cic", "all"):
        run(CIC)
    print("\npipeline complete - dashboard: python scripts/serve.py "
          "-> http://localhost:8000/dashboard/")
