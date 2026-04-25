from __future__ import annotations

import time

from .assets import ensure_textures_bundle, ensure_vendor_bundle, write_file
from .config import OUT_DIR
from .frontend import INDEX_HTML, MAIN_JS, STYLE_CSS


def scaffold() -> None:
    ensure_vendor_bundle()
    ensure_textures_bundle()

    build_id = str(int(time.time()))
    write_file(OUT_DIR / "index.html", INDEX_HTML.replace("{{BUILD_ID}}", build_id))
    write_file(OUT_DIR / "style.css", STYLE_CSS)
    write_file(OUT_DIR / "main.js", MAIN_JS)

    print(f"GlobalOps VR written to: {OUT_DIR}")

