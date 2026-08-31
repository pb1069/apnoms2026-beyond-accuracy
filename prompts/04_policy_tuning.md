# Prompt 04 — Take-home: tune the accept/review/withhold gate `[v0 — 미확정]`

Not run live during the tutorial — homework track.

```
Using the trained lab (run setup first if models/ is missing), sweep agreement
thresholds from 0.5 to 1.0 and build an accept/review/withhold policy table:
for target precisions 0.95, 0.99 and 1.0, report the best threshold, coverage,
TP and FP counts.

Put the sweep in a new file experiments/policy_sweep.py — do not modify
src/config.py or any existing script — write the table to results/policy.json
and print it. Sanity-check: at target precision 1.0 your numbers should match
expected_outputs/demo2.json (threshold 0.775, TP 1287) within ±0.005.
```
