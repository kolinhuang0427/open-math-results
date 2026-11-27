# Gate 2 Novelty Check — `targets/oeis-A024199/`

- **Checked at:** `2026-11-27T10:35:38Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A024199 "024199"` -> `0` lines across `0/619` files in `watch/snapshots/**` (incl. `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A024199"` -> `[]`
   - `gh search issues "A024199"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A024199&fmt=json`):**
   - Revision `80` (`2026-06-28T15:47:50-04:00`): Peter Bala's Nov 15 2016 formula remains marked `Conjecture:`.
4. **arXiv live query (`search_query=all:A024199`):**
   - `0` results.
5. **Zenodo API (`q=A024199`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Query `"A024199" ("Bala" OR "arcsin" OR "proved" OR "conjecture" OR "zenodo")` -> surfaces only OEIS `A024199` / unrelated Zenodo period-conjecture records (`A281181`, `A281428`); no prior proof of `A024199` found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`619` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo API, and web search ran at `2026-11-27T10:35:38Z`.
