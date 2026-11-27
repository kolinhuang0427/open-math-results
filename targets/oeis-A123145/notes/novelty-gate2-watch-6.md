# Gate 2 Novelty Check — `targets/oeis-A123145/`

- **Checked at:** `2026-11-27T10:45:29Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A123145 "123145"` -> `0` lines across `0/619` files in `watch/snapshots/**` (incl. `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A123145"` -> `[]`
   - `gh search issues "A123145"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A123145&fmt=json`):**
   - Revision `31` (`2023-07-16T16:56:53-04:00`): Sergei N. Gladkovskii's Nov 26 2012 continued-fraction EGF formula remains marked `Conjecture:`.
4. **arXiv (`all:A123145`) & Zenodo (`q=A123145`):**
   - `0` results on arXiv; `0` hits on Zenodo.
5. **Web search (`search_web`):**
   - Surfaces only OEIS `A123145` itself; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`619` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo, and web search ran at `2026-11-27T10:45:29Z`.
