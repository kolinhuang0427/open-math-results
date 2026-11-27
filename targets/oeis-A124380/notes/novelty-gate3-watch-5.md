# Gate 3 Novelty Check — oeis-A124380 (watch-5)

- **Checked UTC:** 2026-11-27T11:13:07Z – 2026-11-27T11:13:10Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Vaclav Kotesovec's Sep 18 2024 `A124380` logarithmic asymptotic conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A227543 A124380`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A124380&fmt=json`):**
   - `A124380` rev. 39: `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2. - _Vaclav Kotesovec_, Sep 18 2024` remains unconfirmed.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A227543 OR all:A124380'`: `0` entries.
   - Zenodo live API (`A124380`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A124380/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A124380/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
