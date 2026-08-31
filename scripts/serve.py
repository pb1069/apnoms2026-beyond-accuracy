"""Results dashboard + deck server with a one-click pipeline API.

Serves the repo root on port 8000 (caching disabled) and exposes a small,
whitelisted run API so the slides can trigger pipeline stages with a button:

  POST /api/run?stage=<name>     start a stage (localhost only)
  GET  /api/status?stage=<name>  {state, exit, elapsed, tail}

Stages are a fixed whitelist — never arbitrary commands. Output is captured
to results/_run_<stage>.log and tailed back to the page.

Open http://localhost:8000/dashboard/ and /slides/
"""
import functools
import http.server
import json
import os
import subprocess
import sys
import threading
import time
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORT = 8000
PY = sys.executable

STAGES = {
    "download":    ["src/download_cicids.py"],
    "prepare":     ["src/prepare_cicids.py"],
    "train_synth": ["src/train.py"],
    "train_cic":   ["src/train_cic.py"],
    "smoke":       ["scripts/smoke_test.py"],
    "demo1":       ["experiments/demo1_confidence.py"],
    "demo2":       ["experiments/demo2_selective.py"],
    "demo3":       ["experiments/demo3_cic_drift.py"],
}

jobs = {}          # stage -> {"proc", "log", "t0"}
jobs_lock = threading.Lock()


def stage_status(stage):
    job = jobs.get(stage)
    if job is None:
        return {"stage": stage, "state": "idle"}
    rc = job["proc"].poll()
    tail = ""
    try:
        data = job["log"].read_bytes()[-2000:]
        tail = data.decode("utf-8", errors="replace")
    except OSError:
        pass
    out = {"stage": stage, "elapsed": round(time.time() - job["t0"]), "tail": tail}
    if rc is None:
        out["state"] = "running"
    else:
        out["state"] = "done" if rc == 0 else "failed"
        out["exit"] = rc
    return out


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):  # quiet
        pass

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _stage_param(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        return (q.get("stage") or [None])[0]

    def do_GET(self):
        if urllib.parse.urlparse(self.path).path == "/api/status":
            stage = self._stage_param()
            if stage not in STAGES:
                return self._json(400, {"error": "unknown stage"})
            return self._json(200, stage_status(stage))
        super().do_GET()

    def do_POST(self):
        if urllib.parse.urlparse(self.path).path != "/api/run":
            return self._json(404, {"error": "not found"})
        if self.client_address[0] not in ("127.0.0.1", "::1"):
            return self._json(403, {"error": "runs are presenter-local only"})
        stage = self._stage_param()
        if stage not in STAGES:
            return self._json(400, {"error": "unknown stage"})
        with jobs_lock:
            job = jobs.get(stage)
            if job and job["proc"].poll() is None:
                return self._json(409, {"error": "already running"})
            (ROOT / "results").mkdir(exist_ok=True)
            log = ROOT / "results" / f"_run_{stage}.log"
            env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"}
            with open(log, "wb") as f:
                proc = subprocess.Popen([PY, *STAGES[stage]], cwd=ROOT,
                                        stdout=f, stderr=subprocess.STDOUT, env=env)
            jobs[stage] = {"proc": proc, "log": log, "t0": time.time()}
        self._json(200, {"stage": stage, "state": "running"})


if __name__ == "__main__":
    handler = functools.partial(Handler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler) as httpd:
        print(f"serving {ROOT}")
        print(f"  deck:      http://localhost:{PORT}/slides/")
        print(f"  dashboard: http://localhost:{PORT}/dashboard/")
        print(f"  run API:   POST /api/run?stage=<{'|'.join(STAGES)}> (localhost only)")
        httpd.serve_forever()
