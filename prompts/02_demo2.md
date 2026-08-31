# Prompt 02 — Demo 2: Selective prediction at Precision 1.0 `[v1 — 1차 리허설 반영(자기완결성); freeze 전 반복 실측 필요]`

```
Run Demo 2 (experiments/demo2_selective.py) in the tutorial environment
(Docker preferred: `docker compose run --rm lab ...`; venv fallback).
It compares two ways to reach a zero-false-alarm (precision 1.0) alert policy:
a confidence threshold on a single model vs an agreement threshold on a
40-expert ensemble, and self-verifies against expected_outputs/demo2.json.

Report: the coverage and TP count for each method, the ratio between them,
and the verification verdict. One sentence on what this means for a SOC that
auto-blocks only alerts it can fully trust.
```
