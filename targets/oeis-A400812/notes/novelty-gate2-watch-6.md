# Gate 2 Novelty Check — `targets/oeis-A400812/`

- **Checked at:** `2026-11-27T10:29:34Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A400812 A400813 A400814 "400812" "400813" "400814"` -> `0` lines across `0/618` files in `watch/snapshots/**`.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A400812"` -> `[]`
   - `gh search issues "A400812"` -> only unrelated closed `georchestra/cadastrapp#329`.
3. **OEIS live JSON (`A400812`, `A400813`, `A400814`):**
   - `A400812` rev. `50` (`2026-11-10T13:17:49-05:00`), `A400813` rev. `19` (`2026-10-31`), `A400814` rev. `19` (`2026-10-31`) all remain explicitly marked empirical and `Conjecture:`.
4. **arXiv live query (`all:A400812 OR all:A400813 OR all:A400814`):**
   - `0` results.
5. **Zenodo API (`A400812`, `A400813`, `A400814`):**
   - `0` hits on each.
6. **Web search (`search_web`):**
   - Query `("A400812" OR "A400813" OR "A400814") ("Horvat" OR "proved" OR "conjecture" OR "zenodo" OR "github")` -> surfaces only OEIS `A400812`–`A400814` themselves; no proof found.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live OEIS, arXiv, Zenodo API, and web search ran at `2026-11-27T10:29:34Z`.
