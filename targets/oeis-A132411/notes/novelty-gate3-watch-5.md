# Gate 3 Novelty Check — oeis-A132411 (watch-5)

- **Checked UTC:** 2026-11-27T10:35:37Z – 2026-11-27T10:35:52Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Peter Bala's May 10 2025 `A132411` $q$-series conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A132411`
   - Result: `0` lines across `0/619` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A132411&fmt=json`):**
   - `A132411` rev. 80: Bala's May 10 2025 entry remains prefixed with `Conjecture: the sequence terms are the exponents in the expansion of the q-series Sum_{n >= 0} q^(2*n) * Product_{k >= 2*n+2} 1 - (-q)^k = 1 + q^3 + q^8 + q^15 + q^24 + ....`

3. **arXiv / Zenodo / GitHub:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A132411'`: `0` entries.
   - Zenodo live API (`A132411`): `0` hits.
   - `gh search issues "A132411"` (`1` unrelated `nbbrd/sdmx-upptime#28139`) & `gh search repos "A132411"` (`0`).

## Verification Scope
- Audit target files: `targets/oeis-A132411/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A132411/notes/check-check-2.py`

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, and GitHub issues/repos returned `0` settlement hits.
