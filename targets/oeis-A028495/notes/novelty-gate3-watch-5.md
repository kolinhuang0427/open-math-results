# Gate 3 Novelty Check — oeis-A028495 (watch-5)

- **Checked UTC:** 2026-11-27T10:56:45Z – 2026-11-27T10:56:49Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Bill McEachen's Feb 11 2026 `A028495` asymptotic ratio conjectures found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A028495`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A028495&fmt=json`):**
   - `A028495` rev. 162: McEachen's Feb 11 2026 `FORMULA` remains prefixed with `Conjectures:`.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A028495'`: `0` entries.
   - Zenodo live API (`A028495`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A028495/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A028495/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
