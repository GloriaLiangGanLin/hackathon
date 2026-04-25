from __future__ import annotations

import os
from pathlib import Path

THREE_VERSION = "0.167.1"

ROOT_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT_DIR / "globalops_vr"

PORT = int(os.environ.get("PORT", "5173"))

VENDOR_DIR = OUT_DIR / "vendor"
TEXTURES_DIR = OUT_DIR / "textures"

VENDOR_FILES = {
    "three.module.js": f"https://cdn.jsdelivr.net/npm/three@{THREE_VERSION}/build/three.module.js",
    "OrbitControls.js": f"https://cdn.jsdelivr.net/npm/three@{THREE_VERSION}/examples/jsm/controls/OrbitControls.js",
    "VRButton.js": f"https://cdn.jsdelivr.net/npm/three@{THREE_VERSION}/examples/jsm/webxr/VRButton.js",
    "GLTFLoader.js": f"https://cdn.jsdelivr.net/npm/three@{THREE_VERSION}/examples/jsm/loaders/GLTFLoader.js",
}

TEXTURE_FILES = {
    "earth_atmos_2048.jpg": "https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg",
    "earth_normal_2048.jpg": "https://threejs.org/examples/textures/planets/earth_normal_2048.jpg",
}

