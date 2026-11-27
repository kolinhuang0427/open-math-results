# Gate 3 Novelty Check — oeis-A101035 (watch-5)

- **Checked UTC:** 2026-11-27T11:12:25Z – 2026-11-27T11:12:33Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Benedict W. J. Irwin's Jul 26 2017 `A101035` logarithmic generating function conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A188458 A101035 A179525 A400812 A400813 A400814`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A101035&fmt=json`):**
   - `A101035` rev. 37: `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))). - _Benedict W. J. Irwin_, Jul 26 2017` remains unconfirmed.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A188458 OR all:A101035 OR all:A179525 OR all:A400812'`: `0` entries.
   - Zenodo live API (`A101035`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A101035/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A101035/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
