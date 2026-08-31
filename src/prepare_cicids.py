"""Prepare CIC-IDS2017 (Kaggle MachineLearningCSV) into pinned npz splits.

Usage:  python src/prepare_cicids.py <path-to-csv-root>
        (omit the path to auto-detect the kagglehub cache)

Outputs: data/cicids.npz  — standard split + drift slices, standardized,
         plus data/cicids_meta.json (feature names, label counts, digest).
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import config_cic as CC
from datagen import content_digest

ROOT = Path(__file__).resolve().parents[1]


def find_csv_root(arg: str | None) -> Path:
    if arg:
        return Path(arg)
    cache = (Path.home() / ".cache" / "kagglehub" / "datasets"
             / Path(CC.KAGGLE_DATASET))
    hits = sorted(cache.rglob("*.csv")) if cache.exists() else []
    if not hits:
        sys.exit("no CSVs found - pass the dataset directory as an argument")
    return hits[0].parent


def day_of(path: Path) -> str:
    name = path.name.lower()
    for key, tag in CC.DAY_OF_FILE.items():
        if key in name:
            return tag
    return "unknown"


def load_all(csv_root: Path) -> pd.DataFrame:
    frames = []
    for f in sorted(csv_root.rglob("*.csv")):
        df = pd.read_csv(f, encoding="latin1", low_memory=False)
        df.columns = [c.strip() for c in df.columns]
        df["__day"] = day_of(f)
        frames.append(df)
        print(f"[load] {f.name}: {len(df):,} rows ({df['__day'].iloc[0]})")
    df = pd.concat(frames, ignore_index=True)

    for c in CC.DROP_DUPLICATE_COLS:
        if c in df.columns:
            df = df.drop(columns=[c])

    df[CC.LABEL_COL] = df[CC.LABEL_COL].astype(str).str.strip()
    y = (df[CC.LABEL_COL] != CC.BENIGN).astype(np.int64)
    day = df["__day"].to_numpy()
    feats = df.drop(columns=[CC.LABEL_COL, "__day"]).apply(pd.to_numeric, errors="coerce")
    feats = feats.replace([np.inf, -np.inf], np.nan)

    keep = ~feats.isna().any(axis=1)
    print(f"[clean] dropping {(~keep).sum():,} rows with NaN/Inf "
          f"({100 * (~keep).mean():.2f}%)")
    feats, y, day = feats[keep], y[keep].to_numpy(), day[keep]
    print(f"[clean] final: {len(feats):,} rows x {feats.shape[1]} features, "
          f"attack ratio {y.mean():.3f}")
    return feats, y, day


def stratified_sample(rng, idx, y, n):
    """Sample n indices from idx, preserving the label ratio."""
    out = []
    for cls in (0, 1):
        pool = idx[y[idx] == cls]
        take = min(len(pool), int(round(n * (y[idx] == cls).mean())))
        out.append(rng.choice(pool, take, replace=False))
    return np.sort(np.concatenate(out))


def main():
    csv_root = find_csv_root(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"[source] {csv_root}")
    feats, y, day = load_all(csv_root)
    x = feats.to_numpy(dtype=np.float64)
    rng = np.random.default_rng(CC.SEED_CIC)

    # ---- standard split: tue+wed+thu ---------------------------------
    pool = np.where(np.isin(day, CC.STD_DAYS))[0]
    tr = stratified_sample(rng, pool, y, CC.N_STD_TRAIN)
    rest = np.setdiff1d(pool, tr)
    te = stratified_sample(rng, rest, y, CC.N_STD_TEST)

    # ---- drift split: train tue+wed; eval tue/wed-holdout, thu, fri --
    dpool = np.where(np.isin(day, CC.DRIFT_TRAIN_DAYS))[0]
    dtr = stratified_sample(rng, dpool, y, CC.N_DRIFT_TRAIN)
    drest = np.setdiff1d(dpool, dtr)
    d0 = stratified_sample(rng, drest, y, CC.N_DRIFT_EVAL)
    thu = np.where(day == "thu")[0]
    fri = np.where(day == "fri")[0]
    dthu = stratified_sample(rng, thu, y, CC.N_DRIFT_EVAL)
    dfri = stratified_sample(rng, fri, y, CC.N_DRIFT_EVAL)

    # ---- standardize (fit on the respective training split) ----------
    def std_fit(a):
        mu, sd = a.mean(0), a.std(0)
        sd[sd == 0] = 1.0
        return mu, sd

    mu_s, sd_s = std_fit(x[tr])
    mu_d, sd_d = std_fit(x[dtr])
    z = lambda a, mu, sd: (a - mu) / sd

    arrays = dict(
        x_tr=z(x[tr], mu_s, sd_s), y_tr=y[tr],
        x_te=z(x[te], mu_s, sd_s), y_te=y[te],
        dx_tr=z(x[dtr], mu_d, sd_d), dy_tr=y[dtr],
        dx_0=z(x[d0], mu_d, sd_d), dy_0=y[d0],
        dx_thu=z(x[dthu], mu_d, sd_d), dy_thu=y[dthu],
        dx_fri=z(x[dfri], mu_d, sd_d), dy_fri=y[dfri],
    )
    (ROOT / "data").mkdir(exist_ok=True)
    np.savez_compressed(ROOT / "data" / "cicids.npz", **arrays)
    digest = content_digest(*arrays.values())

    meta = {
        "features": list(feats.columns),
        "shortcut_index": list(feats.columns).index(CC.SHORTCUT_FEATURE)
        if CC.SHORTCUT_FEATURE in feats.columns else -1,
        "content_sha256": digest,
    }
    meta["splits"] = {name: {"n": int(arrays[f"{pre}x_{suf}"].shape[0]),
                             "attack_ratio": round(float(arrays[f"{pre}y_{suf}"].mean()), 4)}
                      for name, pre, suf in [
                          ("train", "", "tr"), ("test", "", "te"),
                          ("drift_train", "d", "tr"), ("drift_eval_sameweek", "d", "0"),
                          ("drift_eval_thu", "d", "thu"), ("drift_eval_fri", "d", "fri")]}
    (ROOT / "data" / "cicids_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"[data] cicids.npz written  content sha256={digest[:16]}...")
    for k, v in meta["splits"].items():
        print(f"  {k:22s} n={v['n']:7,}  attack_ratio={v['attack_ratio']}")


if __name__ == "__main__":
    main()
