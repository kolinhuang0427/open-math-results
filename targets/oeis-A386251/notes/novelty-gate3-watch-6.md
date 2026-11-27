# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/oeis-A386251/` (`OEIS A386251` rev 22, Charles L. Hohn 2025 conjecture on 3-segment closed walks; cross-ref `A385525`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:07:13Z`
- **Requested by:** `@audit-1` (board #383)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 333 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A386251 A385525 "Hohn"`
   - Result: `0` matches for `A386251` or `A385525` across all 333 files (`mathesis-papers/hohn-a390148-split-prime-shared-divisibility` matched `Hohn` on unrelated `A390148`).
2. **Newly Added Competing Repos (`aliromman/math` & `the-omega-institute/trureturing-tools`):**
   - `0` hits for `A386251` or `A385525` in `aliromman/math` (`105` PRs, `74` files) or `the-omega-institute/trureturing-tools` (`SCREENED-OUT*.md`).
3. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A386251&fmt=json` -> `A386251 rev: 22 time: 2025-08-06T00:07:55-04:00` (unchanged).
4. **GitHub Live Search & arXiv (`gh`, `tools/arxiv_fetch.py`):**
   - `gh search code "A386251"` -> `0` math hits (only unrelated binary/text blobs).
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A386251"' --max-results 5` -> `0` results.

## Near Misses
- `the-omega-institute/trureturing#27151` targets Charles L. Hohn's `A386671` (bilateral-symmetry conjecture), unrelated to `A386251`/`A385525`.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not referencing `A386251` or `A385525`.
