# Gate 3 Novelty Re-Check — `oeis-A386251` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:13:09Z`
- **Target:** `targets/oeis-A386251/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Hohn's 3-segment closed walk conjecture found across live OEIS, arXiv, Zenodo, Crossref, web search, 333 local snapshots, `aliromman/math`, or `the-omega-institute/trureturing-tools`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 333 files incl. `aliromman__math.json` & `trureturing-tools.json`):**
   - `A386251 386251` -> `0 lines across 0/333 files`.
   - `"A386251" "A385525" "Hohn"` -> only `mathesis-papers/hohn-a390148-split-prime-shared-divisibility` (different Hohn OEIS conjecture `A390148`), 0 hits on `A386251` or `A385525`.

2. **GitHub Live Checks (`gh search` / `gh api`, read-only):**
   - `gh search prs/code --repo aliromman/math "... A386251 ..."` and `repos/aliromman/math/pulls?state=all` filter -> 0 matches.
   - `gh search code --repo the-omega-institute/trureturing-tools "... A386251 ..."` and `contents` filter -> 0 matches.
   - `gh search issues "A386251"` -> `the-omega-institute/trureturing #27151` (`Open problem (pre...)`, unrelated `A386671`); `gh search prs "A386251"` -> 0 math matches (`Unipg-Racing-Team` #2 unrelated).
   - `gh search code "A386251"` -> 489 results from SHA-256 hex substrings/XML IDs, no math proof/counterexample.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A386251&fmt=json`):**
   - Confirmed `revision: 22` (`2025-08-06T00:07:55-04:00`) unchanged; still states `"It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks."`

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A386251` -> `0` entries.
   - `all:A385525` -> `0` entries.
   - `au:Hohn AND all:diagonal` -> `1` unrelated physics entry (`1203.4706v1`, *Hidden magnetic order in CuNCN*).

5. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=A386251` -> `0` hits; `q="Charles L. Hohn"` -> `0` hits.
   - Crossref `query=A386251` -> `0` results.

6. **Web Search (`search_web`):**
   - `"A386251" OR ("3-segment closed walks" "noncongruent diagonals")` -> only OEIS `A386251` / GitHub OEIS-list mirrors (`joaquimmj/oeis-conjectures`), no resolution.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing#27151`: Relates to a different sequence (`A386671`), not `A386251`.
- `mathesis-papers/hohn-a390148-split-prime-shared-divisibility`: Concerns Charles L. Hohn's divisibility conjecture on `A390148`, not lattice walks `A386251`.
- `CONTESTED.md`: absent from `targets/oeis-A386251/` (actually `ls` showed `COUNTEREXAMPLE.md`, no `CONTESTED.md`).

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
