# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/chang-2201.02781-conj2/` (Chang–Yang–Yin–Yao `arXiv:2201.02781v1` §1 Conjecture 2: $\mathrm{fgndi}_{\sum}(G) \le 3$ for every connected graph $G \neq K_2$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:38:47Z`
- **Requested by:** `@scout-9` (board #430)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2201.02781 "fgndi" "neighbor-distinguishing" "2303.02611" "Keusch"`
   - Result: Only `watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` and `openalex_works_cache.json` (`0` competing hits across all 356 snapshot files).
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "2201.02781 OR fgndi"` -> `[]`
   - `gh search issues "\"2201.02781\" OR \"fgndi\""` -> `[]`
   - `gh search code "2201.02781 OR fgndi"` -> `[]`
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2201.02781,2303.02611` -> `2201.02781v1` (`2022-01-08`) is sole latest version (`2303.02611v4` is Keusch's 1-2-3 Conjecture proof on edge weights only).
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2201.02781" OR all:"fractional general neighbor-distinguishing"' --max-results 5` -> `0` additional hits.
4. **Web Search (`search_web`):**
   - Query: `"2201.02781" "fractional general neighbor-distinguishing" OR "Conjecture 2" Chang Yang Yin Yao proved` -> only `arXiv:2201.02781` itself (proved there only for paths, cycles, 3-regular, stars, complete, trees, hypercubes, bipartite, and complete $r$-partite graphs).

## Near Misses
- Ralph Keusch (`arXiv:2303.02611v4`, *JCTB* 2024) settled the edge-only 1-2-3 Conjecture, not the full-sum vertex+edge+neighbor parameter $\mathrm{fgndi}_{\sum}(G)$ of `2201.02781v1`.
- Cheng–Yang–Yao–Luo (2022) settled Conjecture 2 only for Halin graphs (`Gate 1` receipt).

## Not Covered
- Paywalled non-indexed Chinese-language journals, private repositories, and offline manuscripts.
