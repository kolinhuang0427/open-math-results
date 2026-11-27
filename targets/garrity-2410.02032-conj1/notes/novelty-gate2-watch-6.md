# Gate 2 Novelty Check — `targets/garrity-2410.02032-conj1/`

- **Checked at:** `2026-11-27T10:15:03Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py 2410.02032 Garrity "e-23-e" "conj:e-23-e"` -> `0` lines across `0/618` files in `watch/snapshots/**`.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2410.02032"` -> `[]`
   - `gh search issues "2410.02032"` -> only `bguanmath/ArXiv_MathNT#352` (automated July 23, 2026 arXiv paper listing).
3. **arXiv live query (`id_list=2410.02032`):**
   - Latest version remains `arXiv:2410.02032v2` (`updated 2026-07-21T15:36:28Z`, published *Combinatorics and Number Theory* 15 (2026), DOI `10.2140/cnt.2026.15.239`).
4. **Zenodo API (`q=2410.02032`):**
   - `0` hits.
5. **Web search (`search_web`):**
   - Query `"2410.02032" OR ("Garrity" "e,23,e" "Conjecture 1")` -> returns only `arXiv:2410.02032` / TRIP map articles; no external resolution of `conj:e-23-e` found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, Zenodo API, and web search ran at `2026-11-27T10:15:03Z`.
