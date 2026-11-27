# Gate 2 Novelty Check — `targets/oeis-A187430/`

- **Checked at:** `2026-11-27T10:12:25Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A187430 "187430"` -> `0` lines across `0/618` files in `watch/snapshots/**` (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A187430"` -> `[]`
   - `gh search issues "A187430"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A187430&fmt=json`):**
   - Revision `55` (`2024-01-17T09:35:29-05:00`): Irwin's Jan 13 2017 Catalan g.f. transform formula remains marked `Conjecture:`.
4. **arXiv live query (`search_query=all:A187430`):**
   - `0` results.
5. **Zenodo API (`q=A187430`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Query `"A187430" ("Irwin" OR "proved" OR "proof" OR "conjecture" OR "zenodo" OR "github")` -> surfaces only OEIS `A187430` itself; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, including Zenodo `23112421` extracted OEIS IDs), `gh search repos/issues`, live OEIS, arXiv, Zenodo, and web search ran at `2026-11-27T10:12:25Z`.
