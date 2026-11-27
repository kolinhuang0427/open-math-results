# Gate 2 Novelty Check — `targets/oeis-A186997/`

- **Checked at:** `2026-11-27T10:15:56Z`
- **Checker:** `watch-6`
- **Result:** **PASS (no prior proof found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A186997 "186997"` -> `0` lines across `0/618` files in `watch/snapshots/**` (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A186997"` -> `[]`
   - `gh search issues "A186997"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A186997&fmt=json`):**
   - Revision `85` (`2026-08-30T09:47:33-04:00`): Peter Bala's Aug 02 2016 2-adic valuation statements remain labeled `Conjectures (both checked up to n = 100)`.
4. **arXiv live query (`search_query=all:A186997`):**
   - `0` results.
5. **Zenodo API (`q=A186997`):**
   - `0` hits.
6. **Web search (`search_web`):**
   - Queries `"A186997" ("Bala" OR "2-adic" OR "proved" OR "conjecture" OR "zenodo")` and `"A186997" "a(2*n+1)" OR "a(2n+1)" OR "Catalan(n-2)"` -> only reference OEIS `A186997` / colored Dyck path papers; unrelated `Palomar`/`formal-conjectures#8038` covers Bala's `A012780` periodicity conjecture (`2026`), not `A186997`.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, including Zenodo `23112421` extracted OEIS IDs), `gh search repos/issues`, live OEIS, arXiv, Zenodo, and web search ran at `2026-11-27T10:15:56Z`.
