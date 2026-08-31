# Prompt 00 — Environment setup & artifact verification `[v1 — 1차 리허설 반영(SSL 분기); freeze 전 반복 실측 필요]`

Paste into your agent at the repo root:

```
Set up this tutorial environment and prove it works.

1. If Docker is available: `docker compose build`, then verify the shipped
   artifacts (pinned data + pre-trained models) inside the container:
     docker compose run --rm lab python scripts/smoke_test.py
   If the build fails with an SSL certificate error (TLS-intercepting corporate
   proxy), retry once with:
     PIP_EXTRA_OPTS="--trusted-host pypi.org --trusted-host files.pythonhosted.org" docker compose build
   Only if Docker is truly unavailable, fall back to a native venv:
   `pip install -r requirements.txt`, then run the same script directly.
   The repo ships pre-trained models; only if the smoke test reports them
   missing, rebuild with `python src/train.py` (~30 s) and re-verify.
2. Then start the results dashboard (`docker compose up -d dashboard`, or
   `python scripts/serve.py` in the background for the venv path) and confirm
   http://localhost:8000/dashboard/ responds.
3. Report: which environment path you used, the smoke test PASS/FAIL lines,
   and whether the CIC-IDS2017 track was present or marked optional.
   Do not edit any source file.
```
