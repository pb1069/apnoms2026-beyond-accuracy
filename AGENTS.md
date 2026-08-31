# Agent context — Beyond Accuracy tutorial artifact

This repo is a reproducible tutorial artifact. Your job when given a prompt from
`prompts/` is to run the requested step, VERIFY the result, and report concisely.

## Rules

1. **Environment order**: prefer Docker (`docker compose run --rm lab <cmd>`).
   If Docker is unavailable or broken, fall back to a native venv
   (`pip install -r requirements.txt`, then run the same command without the
   compose prefix). Say which path you used.
2. **Never edit `src/config.py`** — it is the frozen spec. If a task seems to
   require changing it, stop and report instead.
3. **Verification is part of every task.** Each demo script self-verifies
   against `expected_outputs/` (tolerance ±0.005) and exits non-zero on
   mismatch. Report the PASS/FAIL table, never just "it ran".
   Native (non-Docker) runs may deviate slightly: if a metric fails natively,
   note it and state the deviation size rather than declaring failure.
4. **Do not "fix" failing numbers** by editing demos, tolerances, or expected
   outputs. A genuine mismatch is a finding to report.
5. **Report format**: 2-4 lines — environment used, command(s), verification
   verdict, and the one-sentence takeaway printed by the demo.

## Commands

| Step | Command (inside Docker or venv) |
|---|---|
| Setup | `python src/train.py` (~1 min, CPU) |
| Smoke test | `python scripts/smoke_test.py` |
| Demo 1 | `python experiments/demo1_confidence.py` |
| Demo 2 | `python experiments/demo2_selective.py` |
| Demo 3 | `python experiments/demo3_drift.py` |
| Dashboard | `docker compose up -d dashboard` → http://localhost:8000/dashboard/ |

Demos require setup to have run first (models/ + data/ must exist).
