# Gate 3 Novelty Check — `targets/oeis-A187430/`

- **Checked at:** `2026-11-27T10:17:21Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (PASS by `audit-2` at `2026-11-27T10:18Z`; cmd `.venv/bin/python targets/oeis-A187430/notes/check-check-2.py`; files: `TARGET.md`, `PROOF.md`, `AUDIT.md`, `notes/check-check-2.py`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A187430 "187430"` -> `0` lines across `0/618` files in `watch/snapshots/**` (incl. `zenodo-23112421-oeis-ids.md`).
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "A187430"` -> `[]`
   - `gh search issues "A187430"` -> `[]`
3. **OEIS live JSON (`https://oeis.org/search?q=id:A187430&fmt=json`):**
   - Revision `55` (`2024-01-17T09:35:29-05:00`), unchanged.
4. **Zenodo API (`q=A187430`):**
   - `0` hits.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files, incl. `zenodo-23112421-oeis-ids.md`), `gh search repos/issues`, live OEIS, and Zenodo API queries ran at `2026-11-27T10:17:21Z`.
