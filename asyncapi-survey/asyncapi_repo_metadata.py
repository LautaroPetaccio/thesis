#!/usr/bin/env python3
"""
Fetch repository metadata (stars, description, language, archive/fork state)
for every unique repo surfaced by `asyncapi_adoption_survey.sh`.

The shell survey only retains the minimal repository payload that GitHub's
code-search endpoint returns (full_name, description, fork, ...).  To
classify each repo as product vs tooling vs demo we also need:

- stargazerCount   — proxy for production-grade adoption
- isArchived       — dead repos drop out of consideration
- primaryLanguage  — useful filter (e.g. exclude YAML-only spec repos)

Doing 714 REST calls would take ~70 minutes under the survey's 6 s rate
limit.  This script uses the GraphQL endpoint instead, batching up to 50
repository lookups per query for ~14 calls total (~30 seconds end-to-end).

Usage:
    scripts/asyncapi_repo_metadata.py <survey-out-dir>

Input:
    <survey-out-dir>/raw/asyncapi-3x-combined.unique-repos.tsv
        (or any TSV whose first column is `owner/name`)

Output:
    <survey-out-dir>/raw/repo-metadata.json
        { "owner/name": { stargazerCount, description, isArchived, ... } }

Requires: gh CLI authenticated (`gh auth status`).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

BATCH_SIZE = 50      # GraphQL recommends ≤ 100 sub-queries; 50 is comfortably safe
INTER_BATCH_SLEEP_S = 1  # rate-limit guard


def load_repo_list(tsv_path: Path) -> list[str]:
    """Read a unique-repos.tsv produced by the shell survey."""
    repos: list[str] = []
    seen: set[str] = set()
    with tsv_path.open() as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            full = line.split("\t", 1)[0]
            if full and full not in seen:
                seen.add(full)
                repos.append(full)
    return repos


def build_graphql_query(batch: list[str]) -> str:
    """Build a GraphQL query that fetches metadata for up to BATCH_SIZE repos."""
    parts: list[str] = []
    for i, full in enumerate(batch):
        try:
            owner, name = full.split("/", 1)
        except ValueError:
            continue
        owner = owner.replace('"', '\\"')
        name = name.replace('"', '\\"')
        parts.append(
            f'r{i}: repository(owner: "{owner}", name: "{name}") {{ '
            "nameWithOwner stargazerCount isFork isArchived description homepageUrl "
            "primaryLanguage { name } "
            "repositoryTopics(first: 12) { nodes { topic { name } } } "
            "}"
        )
    return "query {\n" + "\n".join(parts) + "\n}"


def fetch_batch(batch: list[str]) -> dict[str, dict]:
    """Run one GraphQL batch via the gh CLI; return repo → metadata.

    Note: `gh api graphql` exits non-zero when the response carries a GraphQL
    `errors` array, which happens whenever ANY repo in the batch was
    deleted/renamed (that alias resolves to null). The other aliases still
    resolve, so we parse stdout regardless of exit code and keep what came
    back. Only a truly empty/transient response (rate limit, network) is
    retried with backoff.
    """
    query = build_graphql_query(batch)
    backoff = 5
    for _ in range(4):
        proc = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            capture_output=True,
            text=True,
            timeout=90,
        )
        out: dict[str, dict] = {}
        try:
            data = (json.loads(proc.stdout).get("data") or {}) if proc.stdout else {}
        except json.JSONDecodeError:
            data = {}
        for value in data.values():
            # Each sub-query (r0, r1, …) is null if the repo was deleted/renamed.
            if value and value.get("nameWithOwner"):
                out[value["nameWithOwner"]] = value
        if out:
            return out  # partial data is fine even if gh exited non-zero on errors
        err = (proc.stderr or "").lower()
        if any(s in err for s in ("rate limit", "secondary", "abuse", "timeout", "502", "503", "bad gateway")):
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
            continue
        time.sleep(2)
    sys.stderr.write("  graphql batch returned no usable data after retries\n")
    return {}


def main() -> int:
    if len(sys.argv) < 2:
        sys.stderr.write(__doc__.lstrip())
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    raw_dir = out_dir / "raw"
    tsv_path = raw_dir / "asyncapi-3x-combined.unique-repos.tsv"
    if not tsv_path.exists():
        sys.stderr.write(
            f"error: {tsv_path} not found — run scripts/asyncapi_adoption_survey.sh first\n"
        )
        return 2

    repos = load_repo_list(tsv_path)
    sys.stderr.write(f"Fetching metadata for {len(repos)} repos via GraphQL...\n")

    results: dict[str, dict] = {}
    for i in range(0, len(repos), BATCH_SIZE):
        batch = repos[i : i + BATCH_SIZE]
        batch_out = fetch_batch(batch)
        results.update(batch_out)
        sys.stderr.write(
            f"  batch {i:>4}-{i + BATCH_SIZE:>4}: {len(batch_out)} returned, {len(results)} total\n"
        )
        time.sleep(INTER_BATCH_SLEEP_S)

    out_path = raw_dir / "repo-metadata.json"
    with out_path.open("w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)
    sys.stderr.write(f"Wrote {len(results)} metadata records to {out_path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
