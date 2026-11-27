# Gate 3 Novelty Check — `targets/oeis-A119262/`

- **Checked at:** `2026-11-27T10:31:56Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (PASS by `audit-1`; cmd `.venv/bin/python -u targets/oeis-A119262/notes/check-check-1.py`; paths `targets/oeis-A119262/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A119262 "119262"` -> `0` lines across `0/619` files in `watch/snapshots/**` (incl. `zenodo-23112421-oeis-ids.md`).
2. **OEIS live JSON (`https://oeis.org/search?q=id:A119262&fmt=json`):**
   - Revision `55` (`2026-02-23T22:55:40-05:00`), unchanged.
3. **Zenodo API (`q=A119262`):**
   - `0` hits.
4. **GitHub search (`gh search`):**
   - Live `gh search` at `10:30:40Z` hit transient TLS handshake timeout (Gate 2 `gh search repos/issues` ran clear at `10:26:11Z`).

## Coverage Limits
- GitHub code search and live `10:30:40Z` `gh search` failed due to shared rate-limit/TLS timeout (Gate 2 `gh` check ran clear 5m earlier at `10:26:11Z`); local snapshots (`619` files, incl. `zenodo-23112421-oeis-ids.md`), live OEIS, and Zenodo API queries ran cleanly at `10:31:56Z`.
