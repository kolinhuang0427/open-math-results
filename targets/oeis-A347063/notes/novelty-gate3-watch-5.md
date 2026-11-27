# Gate 3 Novelty Check — oeis-A347063 (watch-5)

- **Checked UTC:** 2026-11-27T11:17:01Z – 2026-11-27T11:17:04Z (`<1h` before reporting)
- **Result:** **PASS** (no prior refutation of Ivan N. Ianakiev's Oct 01 2024 `A347063` `$18k+12$` Double Zumkeller conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A227543 A347063 A127276`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A347063&fmt=json`):**
   - `A347063` rev. 51: `"It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]. - _Ivan N. Ianakiev_, Oct 01 2024"` remains open/unrefuted.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A227543 OR all:A347063 OR all:A127276'`: `0` entries.
   - Zenodo live API (`A347063`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A347063/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A347063/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
