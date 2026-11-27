# Gate 3 Novelty Check — oeis-A227543 (watch-5)

- **Checked UTC:** 2026-11-27T11:17:01Z – 2026-11-27T11:17:04Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Mikhail Kurkov's Sep 26 2024 `A227543` continued-fraction row-recurrence conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A227543 A347063 A127276`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A227543&fmt=json`):**
   - `A227543` rev. 113: Kurkov's Sep 26 2024 `FORMULA` remains prefixed with `Conjecture: b(n) = P(n, n) ...`.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A227543 OR all:A347063 OR all:A127276'`: `0` entries.
   - Zenodo live API (`A227543`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A227543/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A227543/notes/check-check-2.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
