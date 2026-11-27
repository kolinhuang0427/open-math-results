# Gate 2 Novelty Check — `targets/oeis-A237757/`

- **Checked at:** `2026-11-27T10:47:39Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A237757 "237757"` -> `0` lines across `0/635` files in `watch/snapshots/**` (incl. `zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A237757"` -> `[]`
   - `gh search issues "A237757"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A237757&fmt=json`):**
   - Revision `17` (`2022-01-22T07:31:08-05:00`): Peter Bala's Feb 02 2021 formula remains marked `Conjectural g.f.:`.
4. **arXiv (`all:A237757`) & Zenodo (`q=A237757`):**
   - `0` results on arXiv; `0` hits on Zenodo.
5. **Web search (`search_web`):**
   - Surfaces only OEIS `A237757` itself; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`635` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo, and web search ran at `2026-11-27T10:47:39Z`.
