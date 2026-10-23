#!/usr/bin/env python3
"""Read-only, shallow stack fingerprint; never executes target repository code."""
import argparse
import json
from pathlib import Path

MARKERS = {
    "python": ("pyproject.toml", "requirements.txt", "Pipfile"),
    "node": ("package.json", "pnpm-lock.yaml", "yarn.lock"),
    "playwright": ("playwright.config.ts", "playwright.config.js"),
    "docker": ("Dockerfile", "compose.yaml", "docker-compose.yml"),
    "pytest": ("pytest.ini", "conftest.py"),
}

def detect(root: Path) -> dict:
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    found = {}
    for stack, markers in MARKERS.items():
        hits = []
        for marker in markers:
            if (root / marker).is_file():
                hits.append(marker)
            for folder in ("services/api", "apps/web", "frontend", "backend"):
                if (root / folder / marker).is_file():
                    hits.append(f"{folder}/{marker}")
        if hits:
            found[stack] = sorted(set(hits))
    return {"repository": str(root.resolve()), "markers": found, "note": "Heuristic only; inspect source and lockfiles before choosing tools"}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", type=Path)
    args = parser.parse_args()
    print(json.dumps(detect(args.repository), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
