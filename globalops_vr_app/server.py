from __future__ import annotations

import http.server
import os
import socketserver

from .config import PORT, ROOT_DIR


def serve() -> None:
    print(f"Server: http://localhost:{PORT}/")
    print(f"Open:   http://localhost:{PORT}/globalops_vr/")

    class ReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format: str, *args) -> None:  # noqa: A002
            return

        def end_headers(self) -> None:
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            super().end_headers()

    os.chdir(ROOT_DIR)
    with ReuseTCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

