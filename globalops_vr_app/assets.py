from __future__ import annotations

import urllib.request
from pathlib import Path

from .config import OUT_DIR, TEXTURE_FILES, TEXTURES_DIR, THREE_VERSION, VENDOR_DIR, VENDOR_FILES


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def download_file(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1000:
        return
    req = urllib.request.Request(url, headers={"User-Agent": "GlobalOpsVR/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        dest.write_bytes(resp.read())


def ensure_vendor_bundle() -> None:
    for name, url in VENDOR_FILES.items():
        print(f"Checking vendor: {name}")
        download_file(url, VENDOR_DIR / name)

    # Patch GLTFLoader to avoid relying on importmaps for 'three' resolution in dynamic imports.
    # Some browsers report it as "Failed to fetch dynamically imported module".
    src = VENDOR_DIR / "GLTFLoader.js"
    if src.exists():
        text = src.read_text(encoding="utf-8")
        patched = text.replace("} from 'three';", "} from './three.module.js';")
        (VENDOR_DIR / "GLTFLoader.local.js").write_text(patched, encoding="utf-8")

    # GLTFLoader.local.js imports BufferGeometryUtils from ../utils/.
    # We vendor it and patch its 'three' import to a relative file URL.
    utils_dir = OUT_DIR / "utils"
    utils_src_url = f"https://cdn.jsdelivr.net/npm/three@{THREE_VERSION}/examples/jsm/utils/BufferGeometryUtils.js"
    utils_dest = utils_dir / "BufferGeometryUtils.js"
    print("Checking utils: BufferGeometryUtils.js")
    download_file(utils_src_url, utils_dest)
    if utils_dest.exists():
        utils_text = utils_dest.read_text(encoding="utf-8")
        utils_patched = utils_text.replace("from 'three';", "from '../vendor/three.module.js';")
        utils_dest.write_text(utils_patched, encoding="utf-8")


def ensure_textures_bundle() -> None:
    for name, url in TEXTURE_FILES.items():
        try:
            print(f"Checking texture: {name}")
            download_file(url, TEXTURES_DIR / name)
        except Exception as e:
            print(f"Warning: texture download failed: {name} | {e}")

