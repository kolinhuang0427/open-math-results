# Gate 2 Novelty Check — oeis-A227543 (watch-5)

- **Checked UTC:** 2026-11-27T11:13:03Z – 2026-11-27T11:13:14Z
- **Result:** **PASS** (no prior proof or confirmation of Mikhail Kurkov's Sep 26 2024 `A227543` continued-fraction row-recurrence conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A227543 A124380`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A227543&fmt=json`):**
   - `A227543` rev. 113: Kurkov's Sep 26 2024 `FORMULA` remains prefixed with `Conjecture: b(n) = P(n, n) ...`.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A227543 OR all:A124380'`: `0` entries.
   - Zenodo live API (`A227543`): `0` hits.
   - `search_web`: confirms Kurkov's `A227543` formula remains an unproved conjecture.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
