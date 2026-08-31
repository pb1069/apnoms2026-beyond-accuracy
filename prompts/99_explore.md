# Prompt 99 — Take-home explorations `[v0 — 미확정]`

Three ways to break the lab. Each prompt is standalone; none may modify
`src/config.py` or existing scripts — new files only.

## 99a — Stress the evasion

```
In this repo, write experiments/explore_stress.py that generates NEW test sets
using src/datagen.make_x with broken_frac in {0.1, 0.3, 0.5, 0.7} (labels from
make_labels, seed 1234 for features), evaluates the saved baseline and ensemble
on each, and prints a table: broken_frac vs baseline accuracy, mean confidence,
ensemble accuracy, mean agreement. Do not modify existing files. Summarize in
two sentences which signal degrades most gracefully.
```

## 99b — Sabotage the ensemble

```
Write experiments/explore_sabotage.py that trains 10 EXTRA experts whose
feature subsets all INCLUDE the shortcut feature (config.SHORTCUT), appends
them to the loaded ensemble in memory (do not overwrite models/), and
re-evaluates agreement separation (correct vs wrong) on the test set with 40
vs 50 experts. Print both numbers and explain in one sentence why forcing
shortcut exposure hurts the agreement signal.
```

## 99c — Bring your own model

```
Train any classifier you like (sklearn, any architecture) on data/dataset.npz
(x_tr, y_tr) in a new file experiments/explore_byom.py. Evaluate it on the
test split grouped by the `broken` mask: report accuracy and mean confidence
on clean vs broken samples. Compare its clean/broken confidence gap with the
tutorial baseline's (expected_outputs/demo1.json) and state whether YOUR model
is also more confident when wrong.
```
