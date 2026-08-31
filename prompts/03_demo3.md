# Prompt 03 — Demo 3: Real-world drift on CIC-IDS2017 `[v1 — 1차 리허설 반영(자기완결성); freeze 전 반복 실측 필요]`

Requires the CIC track (`python scripts/run_pipeline.py --track cic` — downloads
844 MB from Kaggle once and trains ~5 min; the presenter machine has it ready).

```
Run Demo 3 (experiments/demo3_cic_drift.py) in the tutorial environment
(Docker preferred: `docker compose run --rm lab ...`; venv fallback).
It evaluates CIC-IDS2017 models trained only on Tuesday+Wednesday traffic
against a same-week holdout, Thursday, and Friday (novel attack families),
and self-verifies against expected_outputs/demo3_cic.json.

Report holdout vs Friday as a small table: accuracy, mean confidence, mean
agreement, predicted-attack rate, accept rate — and the verification verdict.
Final sentence: which signals stayed silent through the collapse, and which
label-free signals actually moved?
```

Extra (합성 σ-드리프트, take-home): `experiments/demo3_drift.py` — 통제 환경에서는
confidence가 상승하며 붕괴하는 반대 패턴을 보임 (expected_outputs/demo3.json).
