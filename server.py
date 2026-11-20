#!/usr/bin/env python3
"""
Sinterklaas Dobbelspel - kleine lokale server (optioneel).

Serveert het spel op http://127.0.0.1:8765/ en slaat de instellingen
uit het configscherm op in config.json naast dit bestand.
Alleen de Python-standaardbibliotheek; werkt op Windows en Linux Mint.

Gebruik:
    python3 server.py              # start server en opent de browser
    python3 server.py --no-browser # alleen de server
    python3 server.py --port 9000  # andere poort
"""
import argparse
import json
import os
import sys
import tempfile
import threading
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

MAP = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(MAP, "config.json")
MAX_GROOTTE = 512 * 1024  # 512 KB is ruim genoeg voor de takenlijst
TOEGESTAAN = {"/", "/index.html", "/config.json", "/favicon.ico"}


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("[sinterklaasspel] " + (fmt % args) + "\n")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _json(self, status, data):
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        pad = self.path.split("?", 1)[0]
        if pad == "/api/config":
            try:
                with open(CONFIG, encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            except FileNotFoundError:
                return self._json(404, {"fout": "config.json niet gevonden"})
            except json.JSONDecodeError as e:
                return self._json(500, {"fout": f"config.json is geen geldige JSON: {e}"})
        if pad not in TOEGESTAAN:
            return self.send_error(404)
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/config":
            return self.send_error(404)
        lengte = int(self.headers.get("Content-Length") or 0)
        if lengte <= 0 or lengte > MAX_GROOTTE:
            return self._json(413, {"fout": "Ongeldige grootte"})
        try:
            data = json.loads(self.rfile.read(lengte).decode("utf-8"))
            if not isinstance(data, dict) or not isinstance(data.get("taken"), list):
                raise ValueError("verwacht een object met een lijst 'taken'")
        except (ValueError, UnicodeDecodeError) as e:
            return self._json(400, {"fout": f"Ongeldige JSON: {e}"})
        # Eerst naar een tijdelijk bestand, dan vervangen: nooit een half bestand
        fd, tmp = tempfile.mkstemp(dir=MAP, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        os.replace(tmp, CONFIG)
        return self._json(200, {"ok": True})


def main():
    p = argparse.ArgumentParser(description="Sinterklaas Dobbelspel server")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--no-browser", action="store_true", help="browser niet automatisch openen")
    args = p.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=MAP))
    url = f"http://127.0.0.1:{args.port}/"
    print(f"Sinterklaas Dobbelspel draait op {url}  (Ctrl+C om te stoppen)")
    if not args.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nTot volgend jaar, Sinterklaas!")


if __name__ == "__main__":
    main()
