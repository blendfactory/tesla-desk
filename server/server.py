#!/usr/bin/env python3
"""
Tesla Fleet API 用の簡易認証サーバー。

公開鍵を次の URL で配信します:
  http://localhost:8080/.well-known/appspecific/com.tesla.3p.public-key.pem

公開鍵は server/well-known/appspecific/com.tesla.3p.public-key.pem に配置してください。
README: server/well-known/appspecific/README.md
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# このスクリプトのディレクトリ（server/）を基準にする
ROOT = Path(__file__).resolve().parent
PUBLIC_KEY_PATH = ROOT / "well-known" / "appspecific" / "com.tesla.3p.public-key.pem"
WELL_KNOWN_PATH = "/.well-known/appspecific/com.tesla.3p.public-key.pem"


class TeslaAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/") or "/"
        if path == WELL_KNOWN_PATH.rstrip("/"):
            self._serve_public_key()
        elif path == "/":
            self._serve_root()
        else:
            self.send_error(404, "Not Found")

    def _serve_public_key(self):
        if not PUBLIC_KEY_PATH.is_file():
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"Public key not found. Place com.tesla.3p.public-key.pem in server/well-known/appspecific/"
            )
            return
        try:
            body = PUBLIC_KEY_PATH.read_bytes()
        except OSError:
            self.send_error(500, "Failed to read public key")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/x-pem-file")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_root(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Tesdesk Tesla Fleet API auth server. See /.well-known/appspecific/com.tesla.3p.public-key.pem")

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    host, port = "localhost", 8080
    server = HTTPServer((host, port), TeslaAuthHandler)
    print(f"Server running at http://{host}:{port}/")
    print(f"Public key URL: http://{host}:{port}{WELL_KNOWN_PATH}")
    if not PUBLIC_KEY_PATH.is_file():
        print(f"Note: Public key not found at {PUBLIC_KEY_PATH}")
        print("  Place com.tesla.3p.public-key.pem there (see server/well-known/appspecific/README.md)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()
