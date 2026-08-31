"""Results dashboard server (stdlib only, offline-safe).

Serves the repo root on port 8000 with caching disabled, so the dashboard
always reflects the latest demo results.  Open http://localhost:8000/dashboard/
"""
import http.server
import functools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORT = 8000


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):  # quiet
        pass


if __name__ == "__main__":
    handler = functools.partial(NoCacheHandler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("0.0.0.0", PORT), handler) as httpd:
        print(f"dashboard: http://localhost:{PORT}/dashboard/  (serving {ROOT})")
        httpd.serve_forever()
