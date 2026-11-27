# Gate 2 Novelty Check — `targets/oeis-A119262/`

- **Checked at:** `2026-11-27T10:26:11Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A119262 "119262"` -> `0` lines across `0/618` files in `watch/snapshots/**` (incl. `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A119262"` -> `[]`
   - `gh search issues "A119262"` -> only unrelated `DigitalKhatt/visualmetafont#3`.
3. **OEIS live JSON (`https://oeis.org/search?q=id:A119262&fmt=json`):**
   - Revision `55` (`2026-02-23T22:55:40-05:00`): Benedict W. J. Irwin's Apr 19 2017 Hessenberg determinant formula remains prefixed `Conjecture:`.
4. **arXiv live query (`search_query=all:A119262`):**
   - `0` results.
5. **Zenodo API (`q=A119262`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Query `"A119262" ("Irwin" OR "Hessenberg" OR "proved" OR "conjecture" OR "zenodo")` -> no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo API, and web search ran at `2026-11-27T10:26:11Z`.
