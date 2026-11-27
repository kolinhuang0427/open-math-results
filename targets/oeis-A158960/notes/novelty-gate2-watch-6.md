# Gate 2 Novelty Check — `targets/oeis-A158960/`

- **Checked at:** `2026-11-27T10:17:43Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A158960 "158960"` -> `0` lines across `0/618` files in `watch/snapshots/**` (incl. `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A158960"` -> `[]`
   - `gh search issues "A158960"` -> only unrelated `sharpemu/sharpemu#618`.
3. **OEIS live JSON (`https://oeis.org/search?q=id:A158960&fmt=json`):**
   - Revision `28` (`2022-09-08T08:45:43-04:00`): M. F. Hasler's Feb 16 2014 comment *"The denominators are 5^n = A000351(n) (conjectured)."* remains `(conjectured)`.
4. **arXiv live query (`search_query=all:A158960`):**
   - `0` results.
5. **Zenodo API (`q=A158960`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Query `"A158960" ("Hermite" OR "Hasler" OR "proved" OR "conjecture" OR "zenodo")` -> surfaces only OEIS `A158960`; no prior proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, arXiv, Zenodo API, and web search ran at `2026-11-27T10:17:43Z`.
