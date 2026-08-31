"""Download CIC-IDS2017 (MachineLearningCSV) from the Kaggle mirror.

Usage:  python src/download_cicids.py
Anonymous download (no Kaggle account needed). Idempotent — reuses the
kagglehub cache. Behind a TLS-intercepting proxy the system trust store is
injected automatically (truststore).

NOTE: CIC-IDS2017 must not be redistributed — this script exists so each user
fetches it from the source themselves.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config_cic as CC


def main():
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass  # normal networks don't need it

    import kagglehub
    path = Path(kagglehub.dataset_download(CC.KAGGLE_DATASET))
    csvs = sorted(path.rglob("*.csv"))
    total_mb = sum(f.stat().st_size for f in csvs) / 1e6
    print(f"[download] {CC.KAGGLE_DATASET}")
    print(f"[download] {len(csvs)} CSV files, {total_mb:.0f} MB at {path}")
    if len(csvs) != 8:
        sys.exit(f"expected 8 CSVs, found {len(csvs)} - check the mirror")
    print("[download] OK - next: python src/prepare_cicids.py")


if __name__ == "__main__":
    main()
