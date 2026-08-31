# Prompt 02 — Demo 2: Selective prediction at Precision 1.0 `[FROZEN v1.0 — Claude 3연속 통과 (2026-08-31). Codex 교차 검증은 발표 노트북에서]`

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
