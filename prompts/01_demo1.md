# Prompt 01 — Demo 1: Is confidence trustworthy? `[v1 — 1차 리허설 반영(자기완결성); freeze 전 반복 실측 필요]`

```
Run Demo 1 (experiments/demo1_confidence.py) in the tutorial environment:
Docker preferred (image apnoms2026-beyond-accuracy, already built by setup;
`docker compose run --rm lab ...`), venv fallback otherwise. The script verifies its own numbers against
expected_outputs/demo1.json at ±0.005.

Then answer, in two sentences, based only on the output:
which group of predictions — correct or wrong — has the HIGHER mean confidence,
and which signal (confidence vs ensemble agreement) actually separates errors?
Include the verification verdict (ALL CHECKS PASSED or the failing lines).
```
