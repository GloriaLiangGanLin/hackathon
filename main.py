"""
Lanchuang Global Monitor VR
---------------------------

Entrypoint only. Implementation lives in `globalops_vr_app/`.

Run:
  PORT=5173 python3 main.py

Scaffold only (no HTTP server):
  python3 main.py --no-serve

Open:
  http://localhost:5173/globalops_vr/
"""

from __future__ import annotations

import sys

from globalops_vr_app.scaffold import scaffold
from globalops_vr_app.server import serve


def main() -> None:
    scaffold()
    if "--no-serve" in sys.argv:
        return
    serve()


if __name__ == "__main__":
    main()
