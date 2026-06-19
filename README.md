# AsyncAPI black-box testing — thesis

Working materials for the master's thesis *Black-Box Testing of AsyncAPI Services in EvoMaster*.

## Contents

- **`proposal.md`** — the proposal / problem characterization: AsyncAPI vs. REST black-box testing,
  the observable request/reply subset, the public-corpus survey, the four transports
  (Kafka / AMQP / MQTT / WebSocket), correlation, and the SUT-usability of the corpus.
- **`proposal-problems.md`** — running record of open problems and threats to validity.
- **`corpus-suitability.md`** — the full per-repo ledger: every AsyncAPI repository code-read across
  the survey (the 3.x `receive`+`reply` repos plus the 2.x / cross-corpus Kafka/AMQP and
  WebSocket/MQTT passes), each with a USABLE / USABLE-WITH-CHANGES / PARTIAL / NOT-USABLE verdict.
- **`asyncapi-survey/`** — the corpus survey itself: Python scripts plus the analysis outputs under
  `asyncapi-survey-out/` and `asyncapi-survey-out-2x/`.

## Reproducing the survey

The survey scripts run against a Python virtualenv (PyYAML) and shell out to the `gh` CLI (GitHub
code search / blob fetch) and the `claude` CLI (repository classification). The venv and the large
fetched-spec caches are **not** version-controlled (see `.gitignore`); recreate the venv with:

```sh
cd asyncapi-survey
python3 -m venv .venv && .venv/bin/pip install pyyaml
```

**Tracked** (the reproducible artifacts): the scripts, the analysis outputs
(`asyncapi-survey-out*/*.md`, `*.csv`), the `*.unique-repos.tsv` repo lists, and the
`repo-classification*.json` / `repo-metadata.json` gold-classification data.

**Not tracked** (regenerable): the GitHub code-search result JSONs and the fetched-spec / README
caches under `*/raw/`. Re-running the survey scripts re-fetches them into the same cache layout.
