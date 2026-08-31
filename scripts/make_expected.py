"""Reference-run helper: copy current results/ into expected_outputs/.

Run ONLY on the reference environment (the pinned Docker image) after
verifying the demo outputs manually.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
exp = ROOT / "expected_outputs"
exp.mkdir(exist_ok=True)

for name in ["demo1", "demo2", "demo3", "demo3_cic"]:
    src = ROOT / "results" / f"{name}.json"
    if src.exists():
        shutil.copy(src, exp / f"{name}.json")
        print(f"pinned {name}.json")
    else:
        print(f"skip {name}.json (no result)")

import numpy as np
from datagen import content_digest

npz = ROOT / "data" / "dataset.npz"
if npz.exists():
    d = np.load(npz)
    digest = content_digest(d["x_tr"], d["y_tr"], d["x_te"], d["y_te"], d["broken"])
    (exp / "dataset.sha256").write_text(digest + "\n")
    print("pinned dataset.sha256")

cic = ROOT / "data" / "cicids.npz"
if cic.exists():
    d = np.load(cic)
    digest = content_digest(*[d[k] for k in sorted(d.files)])
    (exp / "cicids.sha256").write_text(digest + "\n")
    print("pinned cicids.sha256")
