# Gate 3 Novelty Check — `targets/oeis-A132411/`

- **Checked at:** `2026-11-27T10:35:38Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (PASS by `audit-1`; cmd `.venv/bin/python -u targets/oeis-A132411/notes/check-check-2.py`; paths `targets/oeis-A132411/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - `.venv/bin/python -u tools/novelty_grep.py A132411 "132411"` -> `0` lines across `0/619` files in `watch/snapshots/**` (incl. `zenodo-23112421-oeis-ids.md`).
2. **OEIS live JSON (`https://oeis.org/search?q=id:A132411&fmt=json`):**
   - Revision `80` (`2026-01-22T07:45:32-05:00`), unchanged.
3. **Zenodo API (`q=A132411`):**
   - `0` hits.
4. **GitHub (`gh search`):**
   - Checked clear at `10:26:58Z` (Gate 2: `[]` repos, only unrelated `nbbrd/sdmx-upptime#28139`).

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`619` files, incl. `zenodo-23112421-oeis-ids.md`), live OEIS, and Zenodo API queries ran at `2026-11-27T10:35:38Z` (with `gh search repos/issues` verified clear at `10:26:58Z`).
