#!/usr/bin/env bash
#
# AsyncAPI 3.0 adoption survey via GitHub code search.
#
# Reproduces the §13 (research) numbers in Thesis.md — counts how many
# public schemas use the request/reply pattern, multi-variant replies,
# Kafka bindings, etc., and dumps the actual hits as a markdown report.
#
# Requires:
#   - gh CLI authenticated (gh auth status)
#   - jq
#
# Notes on GitHub's hard caps:
#   - Code search has a 1,000-result *enumerable* ceiling per query
#     (the API returns total_count truthfully, but only the first 1,000
#     items can be paginated).  This script works around that ceiling
#     by running the query in size-buckets (`size:<1024`, `size:1024..4095`,
#     etc.) whenever the headline total_count exceeds 900.  Each bucket
#     is independent, so their union covers the full corpus that any
#     single query would have lost.
#   - 30 req/minute secondary rate limit on the search endpoint —
#     handled by 6 s inter-request sleeps and exponential-backoff retries
#     on 403/422.  A full run takes ~8-15 minutes depending on how many
#     queries need bucketing.
#
# Output:
#   <out-dir>/raw/<slug>.json              — concatenated paged API responses
#   <out-dir>/raw/<slug>.total             — authoritative total_count value
#   <out-dir>/raw/<slug>.unique-repos.tsv  — deduplicated repo list (one per
#                                            line, columns: repo, path, url)
#   <out-dir>/asyncapi-survey.md           — final markdown report
#
# Usage:
#   scripts/asyncapi_adoption_survey.sh [out-dir]
#   scripts/asyncapi_adoption_survey.sh /tmp/asyncapi-survey

set -uo pipefail

OUT_DIR="${1:-${PWD}/asyncapi-survey-out}"
RAW_DIR="${OUT_DIR}/raw"
REPORT="${OUT_DIR}/asyncapi-survey.md"
PER_PAGE=100                 # API max
PAGE_LIMIT=10                # 10 * 100 = 1,000-result API ceiling per query
INTER_REQUEST_SLEEP=6        # 6s ≈ 10 req/min; well under the 30 req/min cap
MAX_RETRIES=4
PARTITION_THRESHOLD=900      # trigger size-bucket partitioning above this
# Size buckets used when the query's total_count > PARTITION_THRESHOLD.
# Picked so AsyncAPI yaml files (typically 1-30 KB) get distributed across
# buckets without any single bucket itself blowing the 1,000-result ceiling.
SIZE_BUCKETS=(
    "<1024"
    "1024..4095"
    "4096..16383"
    "16384..65535"
    ">=65536"
)

mkdir -p "${RAW_DIR}"

if ! command -v gh >/dev/null 2>&1; then
    echo "error: gh CLI not found on PATH" >&2; exit 1
fi
if ! command -v jq >/dev/null 2>&1; then
    echo "error: jq not found on PATH" >&2; exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
    echo "error: gh CLI not authenticated; run 'gh auth login'" >&2; exit 1
fi

# query slug → query string.  Order matters for the report.
declare -a QUERIES=(
    "asyncapi-3-0|asyncapi: 3.0.0 in:file extension:yaml"
    "asyncapi-3-1|asyncapi: 3.1.0 in:file extension:yaml"
    "asyncapi-3-0-yml|asyncapi: 3.0.0 in:file extension:yml"
    "asyncapi-3-1-yml|asyncapi: 3.1.0 in:file extension:yml"
    "asyncapi-3-0-json|asyncapi: 3.0.0 in:file extension:json"
    "asyncapi-3-1-json|asyncapi: 3.1.0 in:file extension:json"
    "asyncapi-2-0|asyncapi: 2.0.0 in:file extension:yaml"
    "asyncapi-2-1|asyncapi: 2.1.0 in:file extension:yaml"
    "asyncapi-2-2|asyncapi: 2.2.0 in:file extension:yaml"
    "asyncapi-2-3|asyncapi: 2.3.0 in:file extension:yaml"
    "asyncapi-2-4|asyncapi: 2.4.0 in:file extension:yaml"
    "asyncapi-2-5|asyncapi: 2.5.0 in:file extension:yaml"
    "asyncapi-2-6|asyncapi: 2.6.0 in:file extension:yaml"
    "reply-clause|asyncapi: 3.0.0 \"reply:\" in:file extension:yaml"
    "reply-messages-array|asyncapi: 3.0.0 \"reply:\" \"messages:\" in:file extension:yaml"
    "kafka-bindings|asyncapi: 3.0.0 \"bindings:\" \"kafka:\" in:file extension:yaml"
    "kafka-key|asyncapi: 3.0.0 \"bindings:\" \"kafka:\" \"key:\" in:file extension:yaml"
    "kafka-partition-key|asyncapi: 3.0.0 partitionKey in:file extension:yaml"
    "send-action|asyncapi: 3.0.0 \"action: send\" in:file extension:yaml"
    "receive-action|asyncapi: 3.0.0 \"action: receive\" in:file extension:yaml"
    "channel-parameters|asyncapi: 3.0.0 \"parameters:\" in:file extension:yaml"
    "mqtt-bindings|asyncapi: 3.0.0 \"protocol: mqtt\" in:file extension:yaml"
    "amqp-bindings|asyncapi: 3.0.0 \"protocol: amqp\" in:file extension:yaml"
    # M12 follow-up: count every transport binding the AsyncAPI 3.0 spec
    # catalogues, so the thesis §29.x / §30 narrative can be precise about
    # which transports show real production OSS adoption (and which would
    # be wasted engine investment). Slugs match the protocol identifier so
    # the report-rendering code aligns automatically.
    "mqtt5-bindings|asyncapi: 3.0.0 \"protocol: mqtt5\" in:file extension:yaml"
    "amqp1-bindings|asyncapi: 3.0.0 \"protocol: amqp1\" in:file extension:yaml"
    "nats-bindings|asyncapi: 3.0.0 \"protocol: nats\" in:file extension:yaml"
    "jms-bindings|asyncapi: 3.0.0 \"protocol: jms\" in:file extension:yaml"
    "pulsar-bindings|asyncapi: 3.0.0 \"protocol: pulsar\" in:file extension:yaml"
    "redis-bindings|asyncapi: 3.0.0 \"protocol: redis\" in:file extension:yaml"
    "stomp-bindings|asyncapi: 3.0.0 \"protocol: stomp\" in:file extension:yaml"
    "googlepubsub-bindings|asyncapi: 3.0.0 \"protocol: googlepubsub\" in:file extension:yaml"
    "ibmmq-bindings|asyncapi: 3.0.0 \"protocol: ibmmq\" in:file extension:yaml"
    "solace-bindings|asyncapi: 3.0.0 \"protocol: solace\" in:file extension:yaml"
    "anypointmq-bindings|asyncapi: 3.0.0 \"protocol: anypointmq\" in:file extension:yaml"
    "sns-bindings|asyncapi: 3.0.0 \"protocol: sns\" in:file extension:yaml"
    "sqs-bindings|asyncapi: 3.0.0 \"protocol: sqs\" in:file extension:yaml"
    "ws-bindings|asyncapi: 3.0.0 \"protocol: ws\" in:file extension:yaml"
    "wss-bindings|asyncapi: 3.0.0 \"protocol: wss\" in:file extension:yaml"
    "http-bindings|asyncapi: 3.0.0 \"protocol: http\" in:file extension:yaml"
    "mercure-bindings|asyncapi: 3.0.0 \"protocol: mercure\" in:file extension:yaml"
    # AsyncAPI 2.x-scoped queries (added 2026-05-28). The existing binding
    # queries above are all hard-scoped to "asyncapi: 3.0.0" — so intersecting
    # them with `asyncapi-2x-combined` gave a structurally wrong set (repos
    # that have *both* a 2.x doc AND a separate 3.0 doc with bindings, not
    # 2.x SUTs that use those transports). The queries below fix that.
    #
    # The `publish-op-2x` slug surfaces the 2.x consume-side: in 2.x's
    # application-perspective semantics, `publish:` under a channel means the
    # app *consumes* messages published to that channel (the actionable case
    # for the fuzzer). 3.0's analogue is the existing `receive-action` slug.
    # The 5 testability criteria in CORPUS_TESTABILITY.md require at least
    # one consume-side operation; this gives us a TSV to intersect with for
    # principled candidate filtering.
    "asyncapi-2x-kafka|\"asyncapi: 2.\" \"protocol: kafka\" in:file extension:yaml"
    "asyncapi-2x-mqtt|\"asyncapi: 2.\" \"protocol: mqtt\" in:file extension:yaml"
    "asyncapi-2x-amqp|\"asyncapi: 2.\" \"protocol: amqp\" in:file extension:yaml"
    "asyncapi-2x-ws|\"asyncapi: 2.\" \"protocol: ws\" in:file extension:yaml"
    "asyncapi-2x-publish-op|\"asyncapi: 2.\" \"publish:\" in:file extension:yaml"
)

# Aggregation groups: post-process unions across slugs.  Each aggregate is
# rendered as an extra row in the headline table and gets its own
# unique-repos.tsv that dedupes across its constituent slugs.  Useful for
# answering "how many distinct repos use AsyncAPI 2.x.x at all?" — a
# single answer that isn't biased by which minor version they pinned.
declare -a AGGREGATIONS=(
    "asyncapi-2x-combined|AsyncAPI 2.x.x (union of all minor versions)|asyncapi-2-0,asyncapi-2-1,asyncapi-2-2,asyncapi-2-3,asyncapi-2-4,asyncapi-2-5,asyncapi-2-6"
    "asyncapi-3x-combined|AsyncAPI 3.x.x (union of all minor versions)|asyncapi-3-0,asyncapi-3-1,asyncapi-3-0-yml,asyncapi-3-1-yml,asyncapi-3-0-json,asyncapi-3-1-json"
)

# fetch a single page with retry on 403/422/secondary-rate-limit
fetch_page() {
    local query="$1" page="$2"
    local attempt=1 backoff="${INTER_REQUEST_SLEEP}"
    local resp tmp
    while [ "${attempt}" -le "${MAX_RETRIES}" ]; do
        tmp=$(mktemp)
        if resp=$(gh api -X GET search/code \
            -f q="${query}" \
            -F per_page="${PER_PAGE}" \
            -F page="${page}" 2>"${tmp}"); then
            rm -f "${tmp}"
            printf '%s' "${resp}"
            return 0
        fi
        local err
        err=$(cat "${tmp}")
        rm -f "${tmp}"
        if grep -qE '(secondary rate|abuse|rate limit|HTTP 403|HTTP 422)' <<<"${err}"; then
            echo "      attempt ${attempt}: rate-limited, sleeping ${backoff}s" >&2
            sleep "${backoff}"
            backoff=$(( backoff * 2 ))
            attempt=$(( attempt + 1 ))
            continue
        fi
        echo "      gh api failed: ${err}" >&2
        return 1
    done
    echo "      gave up after ${MAX_RETRIES} retries" >&2
    return 1
}

# Paginate one query expression, appending each page's JSON to ${out_file}.
# Termination is count-based, not page-size-based: GitHub's code-search API
# is known to return short pages even when more data exists (e.g. 99 items
# on page 1 when total_count is 271).  We only stop when:
#   - the cumulative items seen >= total_count (we've enumerated everything),
#   - or we've reached the 1,000-result enumerable ceiling,
#   - or the page returned 0 items (truly empty — likely an indexing race).
paginate() {
    local query="$1" out_file="$2"
    local page=1 last_resp="" seen=0
    while [ "${page}" -le "${PAGE_LIMIT}" ]; do
        local resp
        resp=$(fetch_page "${query}" "${page}") || break
        last_resp="${resp}"
        echo "${resp}" >> "${out_file}"
        local total page_count
        total=$(jq -r '.total_count // 0' <<<"${resp}")
        page_count=$(jq -r '.items | length' <<<"${resp}")
        seen=$(( seen + page_count ))
        if [ "${page_count}" -eq 0 ] || [ "${seen}" -ge "${total}" ]; then
            break
        fi
        page=$((page + 1))
        sleep "${INTER_REQUEST_SLEEP}"
    done
    # Last response's total_count, or 0 if every page failed.
    if [ -n "${last_resp}" ]; then
        jq -r '.total_count // 0' <<<"${last_resp}"
    else
        echo 0
    fi
}

run_query() {
    local slug="$1" query="$2"
    local out_file="${RAW_DIR}/${slug}.json"
    local total_file="${RAW_DIR}/${slug}.total"
    : > "${out_file}"

    # Peek at the headline total_count via page 1.  We need this both
    # to record the authoritative number (the API's truthful count even
    # when paginated results are capped) and to decide whether to
    # partition.
    local peek
    peek=$(fetch_page "${query}" 1)
    if [ -z "${peek}" ]; then
        echo 0 > "${total_file}"
        return
    fi
    local headline
    headline=$(jq -r '.total_count // 0' <<<"${peek}")
    echo "${headline}" > "${total_file}"
    echo "    headline total_count=${headline}"

    if [ "${headline}" -le "${PARTITION_THRESHOLD}" ]; then
        # Within the API's enumerable ceiling — single pass, page 1 already
        # fetched.  Continue paginating until we cover total_count, the
        # 1,000-result ceiling, or the API stops returning items.  We don't
        # trust "short page → last page" as a termination signal, because
        # GitHub's code-search API regularly returns partial pages while
        # more data is still pending (e.g. 99 items on page 1 with
        # total_count=271).
        echo "${peek}" >> "${out_file}"
        local first_page_count
        first_page_count=$(jq -r '.items | length' <<<"${peek}")
        if [ "${first_page_count}" -lt "${headline}" ]; then
            sleep "${INTER_REQUEST_SLEEP}"
            paginate_from "${query}" "${out_file}" 2 "${first_page_count}" > /dev/null
        fi
        return
    fi

    # Over the 1,000-result enumerable ceiling.  Split into size buckets
    # and union; each bucket counts independently up to its own ceiling.
    echo "    over partition threshold (${PARTITION_THRESHOLD}); splitting by file size"
    for bucket in "${SIZE_BUCKETS[@]}"; do
        local bucket_query="${query} size:${bucket}"
        echo "      bucket size:${bucket}"
        local bucket_total
        bucket_total=$(paginate "${bucket_query}" "${out_file}")
        if [ "${bucket_total}" -gt 1000 ]; then
            echo "      WARNING: bucket size:${bucket} has ${bucket_total} hits, exceeds 1000 ceiling — some results lost" >&2
        fi
        sleep "${INTER_REQUEST_SLEEP}"
    done
}

# Variant of paginate() that starts from a specific page (used after a peek)
# and pre-seeds the cumulative `seen` counter with how many items the peek
# already absorbed.  Same termination rules as paginate().
paginate_from() {
    local query="$1" out_file="$2" start_page="$3" seen="${4:-0}"
    local page="${start_page}" last_resp=""
    while [ "${page}" -le "${PAGE_LIMIT}" ]; do
        local resp
        resp=$(fetch_page "${query}" "${page}") || break
        last_resp="${resp}"
        echo "${resp}" >> "${out_file}"
        local total page_count
        total=$(jq -r '.total_count // 0' <<<"${resp}")
        page_count=$(jq -r '.items | length' <<<"${resp}")
        seen=$(( seen + page_count ))
        if [ "${page_count}" -eq 0 ] || [ "${seen}" -ge "${total}" ]; then
            break
        fi
        page=$((page + 1))
        sleep "${INTER_REQUEST_SLEEP}"
    done
}

# Extract the deduplicated repo list (repo / first matching path / first
# matching url) from a slug's raw JSON file, deduplicated by repo full_name.
extract_unique_repos() {
    local slug="$1"
    local out="${RAW_DIR}/${slug}.unique-repos.tsv"
    jq -r '.items[]? | [.repository.full_name, .path, .html_url] | @tsv' \
        "${RAW_DIR}/${slug}.json" 2>/dev/null \
        | awk -F'\t' '!seen[$1]++' \
        > "${out}"
    wc -l < "${out}" | tr -d ' '
}

# Render a markdown table for a given query slug, listing every unique
# repository that matches.  Falls back to a placeholder when the query
# returned nothing.
render_unique_repos_table() {
    local slug="$1" limit="${2:-1000}"
    local tsv="${RAW_DIR}/${slug}.unique-repos.tsv"
    if [ ! -s "${tsv}" ]; then
        echo "_(no enumerable hits — query may have failed or returned 0)_"
        return
    fi
    echo "| Repo | Schema path |"
    echo "|------|-------------|"
    head -n "${limit}" "${tsv}" | while IFS=$'\t' read -r repo path url; do
        [ -z "${repo}" ] && continue
        echo "| [${repo}](https://github.com/${repo}) | [\`${path}\`](${url}) |"
    done
}

# Optional slug allow-list: ONLY="slugA,slugB,..." restricts the fetch + TSV
# extract loops to those slugs only. Aggregation rebuilds and report rendering
# still run over the full QUERIES list, using cached data for any slug not in
# ONLY. Useful when adding new queries (e.g. the 2.x-scoped ones added
# 2026-05-28) and you don't want to spend 15min re-hitting the API for the
# unchanged 30+ existing slugs.
slug_in_only() {
    local needle="$1"
    [ -z "${ONLY:-}" ] && return 0
    [[ ",${ONLY}," == *",${needle},"* ]]
}

echo "Running ${#QUERIES[@]} GitHub code-search queries — this takes ~8-15 minutes..."
for entry in "${QUERIES[@]}"; do
    slug="${entry%%|*}"
    query="${entry#*|}"
    if ! slug_in_only "${slug}"; then
        echo "  query: ${slug} — skipped (not in ONLY)"
        continue
    fi
    echo "  query: ${slug}"
    run_query "${slug}" "${query}"
    sleep "${INTER_REQUEST_SLEEP}"
done

# After all queries are done, extract the deduplicated repo list per slug.
echo
echo "Extracting unique-repos.tsv per query..."
for entry in "${QUERIES[@]}"; do
    slug="${entry%%|*}"
    if ! slug_in_only "${slug}"; then
        continue
    fi
    count=$(extract_unique_repos "${slug}")
    echo "  ${slug}: ${count} unique repos"
done

# Build aggregations: union the unique-repos.tsv files of the constituent
# slugs, dedupe by repo full_name (first column), sum the total_counts.
echo
echo "Building aggregations..."
for agg in "${AGGREGATIONS[@]}"; do
    IFS='|' read -r agg_slug agg_label agg_members <<<"${agg}"
    agg_tsv="${RAW_DIR}/${agg_slug}.unique-repos.tsv"
    agg_total_file="${RAW_DIR}/${agg_slug}.total"
    : > "${agg_tsv}"
    sum_total=0
    IFS=',' read -r -a members <<<"${agg_members}"
    for m in "${members[@]}"; do
        # union: cat all member TSVs, then dedupe by repo (column 1, keeping
        # whichever row appears first).
        if [ -s "${RAW_DIR}/${m}.unique-repos.tsv" ]; then
            cat "${RAW_DIR}/${m}.unique-repos.tsv" >> "${agg_tsv}"
        fi
        # Sum the total_counts (file counts, not repo counts — the truthful
        # GitHub-reported number across the family of versions).
        member_total=$(cat "${RAW_DIR}/${m}.total" 2>/dev/null || echo 0)
        sum_total=$(( sum_total + member_total ))
    done
    # in-place dedupe by repo full_name
    awk -F'\t' '!seen[$1]++' "${agg_tsv}" > "${agg_tsv}.tmp" && mv "${agg_tsv}.tmp" "${agg_tsv}"
    echo "${sum_total}" > "${agg_total_file}"
    unique=$(wc -l < "${agg_tsv}" | tr -d ' ')
    echo "  ${agg_slug}: ${unique} unique repos (total file count: ${sum_total})"
done

# ---- compose the report ----
{
    echo "# AsyncAPI 3.0 adoption survey"
    echo
    echo "_Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ) by \`scripts/asyncapi_adoption_survey.sh\`._"
    echo
    echo "GitHub code-search counts of public yaml/yml schemas.  When a query's"
    echo "headline \`total_count\` exceeds 900 (close to the API's 1,000-result"
    echo "enumerable ceiling), the script automatically partitions by file"
    echo "\`size:\` so the full corpus is covered; otherwise it paginates"
    echo "normally up to the ceiling."
    echo
    echo "Per-query outputs:"
    echo "- \`raw/<slug>.json\` — concatenated raw API responses across all"
    echo "  pages and size-buckets."
    echo "- \`raw/<slug>.total\` — authoritative \`total_count\` (true even when"
    echo "  not all individual files are enumerable)."
    echo "- \`raw/<slug>.unique-repos.tsv\` — deduplicated by repo full_name."
    echo
    echo "## Headline counts"
    echo
    echo "| Query | total_count | unique repos |"
    echo "|-------|-------------|--------------|"
    for entry in "${QUERIES[@]}"; do
        slug="${entry%%|*}"
        query="${entry#*|}"
        total=$(cat "${RAW_DIR}/${slug}.total" 2>/dev/null || echo "?")
        unique=$(wc -l < "${RAW_DIR}/${slug}.unique-repos.tsv" 2>/dev/null | tr -d ' ')
        unique=${unique:-0}
        safe_query=${query//|/\\|}
        echo "| \`${safe_query}\` | ${total} | ${unique} |"
    done
    # Append aggregation rows (sum of total_counts, dedup'd repo union).
    for agg in "${AGGREGATIONS[@]}"; do
        IFS='|' read -r agg_slug agg_label _ <<<"${agg}"
        total=$(cat "${RAW_DIR}/${agg_slug}.total" 2>/dev/null || echo "?")
        unique=$(wc -l < "${RAW_DIR}/${agg_slug}.unique-repos.tsv" 2>/dev/null | tr -d ' ')
        unique=${unique:-0}
        echo "| **${agg_label}** | ${total} | **${unique}** |"
    done
    echo

    for slug_pretty in \
        "reply-clause:Repos using the request/reply pattern" \
        "reply-messages-array:Repos with both reply: and messages: (likely reply.messages array)" \
        "kafka-bindings:Repos with Kafka bindings" \
        "kafka-key:Repos with Kafka key bindings" \
        "kafka-partition-key:Repos with bindings.kafka.partitionKey" \
        "channel-parameters:Repos with channel parameters" \
        "mqtt-bindings:Repos with MQTT bindings" \
        "amqp-bindings:Repos with AMQP bindings"
    do
        slug="${slug_pretty%%:*}"
        title="${slug_pretty#*:}"
        count=$(wc -l < "${RAW_DIR}/${slug}.unique-repos.tsv" 2>/dev/null | tr -d ' ')
        count=${count:-0}
        echo "## ${title} (${count} unique repos)"
        echo
        render_unique_repos_table "${slug}"
        echo
    done

    echo "## Reproducibility"
    echo
    echo "- Re-run: \`scripts/asyncapi_adoption_survey.sh ${OUT_DIR}\`"
    echo "- Auth: GitHub CLI (\`gh auth status\` shows the active account)"
    echo "- Raw paginated JSON: \`${RAW_DIR}/<slug>.json\`"
    echo "- Authoritative count:  \`${RAW_DIR}/<slug>.total\`"
    echo "- Deduplicated repo list: \`${RAW_DIR}/<slug>.unique-repos.tsv\`"
    echo "- GitHub's code search is best-effort: results shift slightly between runs as repos are pushed or deleted, but the headline counts are stable to within a few percent over weeks.  The size-bucket partitioning covers the 1,000-result enumerable ceiling for queries whose \`total_count\` exceeds 900."
    echo
    echo "## Classification (optional next step)"
    echo
    echo "The companion Python scripts under \`scripts/\` go beyond raw counts and classify each repo as product / tooling / demo / hobby / spec.  They use the per-query \`unique-repos.tsv\` files this run produced as input."
    echo
    echo "1. Fetch metadata (stars, language, archive state) via GraphQL:"
    echo "   \`\`\`bash"
    echo "   scripts/asyncapi_repo_metadata.py ${OUT_DIR}"
    echo "   \`\`\`"
    echo "2. Classify and render the human-readable report:"
    echo "   \`\`\`bash"
    echo "   scripts/asyncapi_classify_repos.py ${OUT_DIR}"
    echo "   \`\`\`"
    echo "3. Inspect \`${OUT_DIR}/asyncapi-classification.md\` for the bucket counts and the full product list."
} > "${REPORT}"

echo
echo "Report written to ${REPORT}"
echo "Raw responses under  ${RAW_DIR}"
echo
echo "Optional next steps:"
echo "  scripts/asyncapi_repo_metadata.py ${OUT_DIR}       # fetch stars + descriptions"
echo "  scripts/asyncapi_classify_repos.py ${OUT_DIR}      # classify product / tooling / demo / hobby"
