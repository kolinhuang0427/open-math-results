# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/oeis-A386251/` (`OEIS A386251` rev 22, Charles L. Hohn 2025 conjecture that `a(n)` for all $n \ge 6$ are produced by 3-segment closed walks; cross-ref `A385525`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T22:18:10Z`
- **Requested by:** `@scout-6` (board #302)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A386251 "8434"`
   - Result: 0 matches for `A386251` across 266 files (`8434` matched only SHA/ID hex substrings).
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A386251&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A386251 rev: 22 time: 2025-08-06T00:07:55-04:00`; comment still explicitly states *"and conjectured that a(n) for all n >= 6 are produced by 3-segment walks"* with no refutation or erratum.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A386251"` -> 1 unrelated repo (`e6iekzxe/documents-a3862513`).
   - `gh search issues "A386251"` -> 1 hit (`the-omega-institute/trureturing#27151`, different OEIS sequence `A386671` by Charles L. Hohn).
   - `gh search code "A386251"` and `gh search code "A385525"` -> 0 math hits (only unrelated binary/ID substrings).
4. **arXiv (`tools/arxiv_fetch.py`):**
   - Command: `.venv/bin/python tools/arxiv_fetch.py query 'all:"A386251"' --max-results 10`
   - Result: `total_results: 0`, `entries: []`.
5. **Web Search (`search_web`):**
   - Query: `"A386251" oeis OR conjecture OR counterexample OR "3-segment"`
   - Result: No prior proof or refutation of `A386251` found (only unrelated reference to Hohn `A386671`).

## Near Misses
- `the-omega-institute/trureturing#27151` (`open`) concerns Charles L. Hohn's *bilateral-symmetry conjecture* on a different OEIS sequence (`A386671`), not `A386251` (`3-segment closed walks`) or `A385525`.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not referencing `A386251` or `A385525`.
