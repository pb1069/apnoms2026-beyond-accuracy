# Beyond Accuracy — APNOMS 2026 Tutorial 1 Artifact

Hands-on companion for **"Beyond Accuracy: Assessing the Reliability of AI Outputs
in Security Operations"** (Dr. Ui-Jun Baek, KISTI · APNOMS 2026, Sep 9, 09:00, Civic Hall A).

Three demos across **two labs** — a controlled synthetic lab (mechanism) and
**CIC-IDS2017** (reality):

| Demo | Lab | Question | Expected finding |
|---|---|---|---|
| 1 | synthetic | Is confidence trustworthy? | The model is **more confident when wrong** |
| 2 | synthetic | Precision-1.0 selective prediction | Agreement keeps **~17× more detections** than confidence |
| 3 | CIC-IDS2017 | Real drift: Tue+Wed-trained models meet Friday | Accuracy collapses **in silence** — means don't move, **rate signals do** |

Every environment, dataset, model spec, and expected number is pinned
([src/config.py](src/config.py), [src/config_cic.py](src/config_cic.py) +
[expected_outputs/](expected_outputs/)). Trained models ship in the repo (~2MB);
each demo verifies its own results against the pinned reference (±0.005) and
prints an ASCII chart in the terminal (PNG charts land in `results/`).

## Run it — Path A: with an LLM agent (recommended)

Open your agent (Claude Code, Codex, …) at this repo root and paste the prompts
in [prompts/](prompts/), starting with `00_setup.md`. The agent picks Docker or
a native venv automatically and verifies every result for you.

## Run it — Path B: manual, Docker (reference environment)

```bash
docker compose build
docker compose run --rm lab python scripts/smoke_test.py   # verify shipped artifacts
docker compose run --rm lab python experiments/demo1_confidence.py
docker compose run --rm lab python experiments/demo2_selective.py
docker compose run --rm lab python experiments/demo3_cic_drift.py
docker compose up -d dashboard                             # http://localhost:8000/dashboard/
```

## Run it — Path C: manual, no Docker (best-effort fallback)

```bash
python -m venv .venv && . .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_pipeline.py --track synthetic   # verify + demos 1-2 (+ extra)
python scripts/serve.py                            # http://localhost:8000/dashboard/
```

## The full pipeline (preprocess → train → analyze → visualize)

`scripts/run_pipeline.py` runs every stage with progress banners and skips
completed ones:

```bash
python scripts/run_pipeline.py --track synthetic   # lab 1: seconds, fully offline
python scripts/run_pipeline.py --track cic         # lab 2: Kaggle download 844MB (once) + ~5 min training
```

The CIC track downloads CIC-IDS2017 from the Kaggle mirror
`chethuhn/network-intrusion-dataset` (anonymous, no account needed) —
the dataset itself is **not** redistributed in this repo; only the pinned
preprocessing pipeline and content hashes are. Models trained from it ship
in `models/` so demos run without retraining.

Native runs can deviate slightly across BLAS builds; the Docker image is the
reference. If a check fails natively but passes in Docker, trust Docker.

## Layout

```
slides/              the tutorial deck itself (web-based, live-updating)
src/config.py        frozen spec, lab 1 — every constant pinned; do not edit
src/config_cic.py    frozen spec, lab 2 (CIC-IDS2017)
src/datagen.py       synthetic dataset (planted shortcut + evasive samples + drift)
src/train.py         lab 1: dataset + baseline + 40-expert ensemble
src/download_cicids.py / prepare_cicids.py / train_cic.py   lab 2 pipeline
experiments/         demos (self-verifying) + take-home explorations
scripts/run_pipeline.py   one-command pipeline (preprocess→train→analyze→visualize)
prompts/             agent prompts (the "Path A" track)
dashboard/           live results page, served by scripts/serve.py (port 8000)
expected_outputs/    pinned reference numbers (generated in the Docker image)
models/              trained models — SHIPPED artifacts (~2MB)
results/, data/      generated locally — not part of the public artifact
```

No GPU, no external downloads, no network needed after `docker compose build`.

## The deck IS a web page

The tutorial slides live at **http://localhost:8000/slides/** (same server as the
dashboard). Checkpoint slides fetch `results/*.json` every 5 s, so demo numbers
and charts appear in the deck the moment a demo finishes. Keys: ←/→ navigate,
**N** speaker notes, **D** open the dashboard, browser print → PDF backup.
