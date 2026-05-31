#!/usr/bin/env python3
"""Verify SHA-256 checksums for known manifest files in this repository."""

import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MANIFESTS = [
    ROOT / "data" / "index_27_tabellen_json_manifest.json",
    ROOT / "spreadsheets" / "index_27_tabellen_manifest.json",
    ROOT / "docs" / "index_pdf_manifest_transformationsmathematik.json",
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    ok = True
    for manifest_path in MANIFESTS:
        if not manifest_path.exists():
            print(f"SKIP missing manifest: {manifest_path.relative_to(ROOT)}")
            continue

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        target_name = manifest.get("file")
        expected = manifest.get("sha256")
        if not target_name or not expected:
            print(f"WARN manifest incomplete: {manifest_path.relative_to(ROOT)}")
            ok = False
            continue

        # Target is usually in same directory as manifest.
        target_path = manifest_path.parent / target_name
        if not target_path.exists():
            print(f"FAIL missing target: {target_path.relative_to(ROOT)}")
            ok = False
            continue

        actual = sha256(target_path)
        if actual == expected:
            print(f"OK   {target_path.relative_to(ROOT)}")
        else:
            print(f"FAIL {target_path.relative_to(ROOT)}")
            print(f"     expected: {expected}")
            print(f"     actual:   {actual}")
            ok = False

    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
