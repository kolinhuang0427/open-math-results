# Gate 2 Novelty Receipt — `oeis-A386251`

- **UTC Time:** 2026-11-26T22:21:00Z
- **Reviewer:** `watch-5` (arXiv & citing-papers slice)
- **Verdict:** **PASS** (no arXiv preprint, Zenodo preprint, Crossref publication, or web result found refuting OEIS `A386251` or exhibiting the 4-segment counterexample family `n = m^2 - 30`)

## Sources & Exact Queries Checked

1. **Snapshot grep (`tools/novelty_grep.py A006255 Padhi A386251 "8434" "b(n)"`):**
   - Checked all 266 files under `watch/snapshots/**` (1.74s) -> `0` matches for `A386251` or `8434`.
2. **Live arXiv API via `tools/arxiv_fetch.py` (`use_cache=False`):**
   - `all:A386251` and `all:"A386251" OR (all:"integer" AND all:"squares" AND all:"segments" AND all:"cycle")` -> `0` results.
3. **Live Zenodo API (`https://zenodo.org/api/records`):**
   - `q=A386251` -> `0` hits.
4. **Live Crossref & OEIS JSON:**
   - Crossref `query=A386251` -> `0` hits.
   - Live OEIS `A386251` (`https://oeis.org/search?q=id:A386251&fmt=json`) -> remains at `revision 22` (`2025-08-06T00:07:55-04:00`), unchanged.
5. **Live Web Search (`search_web`) & GitHub code search (`gh api search/code?q=A386251+OR+A385525`):**
   - `gh api` -> `[]` (0 results).
   - `"A386251" OR ("segments" "squares" "8434" OR "92" "368" "oeis")` -> returns only OEIS `A386251` / `A385525` context (no refutation or 4-segment counterexample).

## Near Misses

- None found in arXiv, Zenodo, Crossref, OEIS, or web search.

## What Was Not Covered

- OpenAlex and Semantic Scholar live APIs (`HTTP 429 Too Many Requests`).
- Closed-access/unpublished manuscripts not indexed in arXiv, Zenodo, Crossref, OEIS, or web search.
- Full GitHub repository/issue scan (covered separately by `watch-1` and `watch-6`).
