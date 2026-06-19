#!/usr/bin/env python3
"""
Fetch and cache the leading text of each surveyed repo's README, for use as a
*description fallback* by asyncapi_classify_repos.py (many repos have no GitHub
topics and no description, but almost all have a README whose first lines state
what the repo is).

Resumable: a repo is skipped if its cache file already exists (an empty file
marks "no README / 404", so we don't re-hit it).

Usage:  asyncapi_fetch_readmes.py <survey-out-dir>
Input:  <out>/raw/asyncapi-3x-combined.unique-repos.tsv
Output: <out>/raw/readmes/<owner>__<name>.txt   (first ~4000 chars, raw)
Requires: gh CLI authenticated.
"""
from __future__ import annotations

import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

LEAD_CHARS = 4000
WORKERS = 6


def repo_list(raw_dir: Path) -> list:
    tsv = raw_dir / "asyncapi-3x-combined.unique-repos.tsv"
    repos, seen = [], set()
    for line in tsv.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        full = line.split("\t", 1)[0]
        if full and full not in seen:
            seen.add(full)
            repos.append(full)
    return repos


def cache_path(cache: Path, full: str) -> Path:
    return cache / (full.replace("/", "__") + ".txt")


def fetch_readme(full: str) -> str:
    """Raw README text via the REST readme endpoint (finds the default README
    regardless of filename/branch). Empty string on 404/no-README."""
    proc = subprocess.run(
        ["gh", "api", f"repos/{full}/readme", "-H", "Accept: application/vnd.github.raw"],
        capture_output=True, text=True, timeout=60,
    )
    if proc.returncode != 0:
        return ""
    return proc.stdout[:LEAD_CHARS]


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__.lstrip())
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    raw_dir = out_dir / "raw"
    cache = raw_dir / "readmes"
    cache.mkdir(exist_ok=True)

    repos = repo_list(raw_dir)
    todo = [r for r in repos if not cache_path(cache, r).exists()]
    sys.stderr.write(f"{len(repos)} repos; {len(todo)} READMEs to fetch (rest cached)\n")

    done = 0

    def work(full: str):
        cache_path(cache, full).write_text(fetch_readme(full), encoding="utf-8")

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(work, r): r for r in todo}
        for _ in as_completed(futs):
            done += 1
            if done % 150 == 0:
                sys.stderr.write(f"  fetched {done}/{len(todo)}\n")
    sys.stderr.write(f"done; cache at {cache}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
