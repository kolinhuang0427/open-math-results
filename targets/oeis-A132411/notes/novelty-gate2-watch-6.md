# Gate 2 Novelty Check — `targets/oeis-A132411/`

- **Checked at:** `2026-11-27T10:26:58Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A132411 "132411"` -> `0` lines across `0/618` files in `watch/snapshots/**` (incl. `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A132411"` -> `[]`
   - `gh search issues "A132411"` -> only unrelated closed `nbbrd/sdmx-upptime#28139`.
3. **OEIS live JSON (`https://oeis.org/search?q=id:A132411&fmt=json`):**
   - Revision `80` (`2026-01-22T07:45:32-05:00`): Peter Bala's May 10 2025 comment remains prefixed `Conjecture:`.
4. **arXiv live query (`search_query=all:A132411`):**
   - `0` results.
5. **Zenodo API (`q=A132411`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Query `"A132411" ("Bala" OR "Gauss" OR "theta" OR "proved" OR "conjecture" OR "zenodo")` -> surfaces only OEIS `A132411`; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo API, and web search ran at `2026-11-27T10:26:58Z`.
