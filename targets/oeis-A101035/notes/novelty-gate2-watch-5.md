# Gate 2 Novelty Check — oeis-A101035 (watch-5)

- **Checked UTC:** 2026-11-27T10:55:16Z – 2026-11-27T10:55:34Z
- **Result:** **PASS** (no prior proof or confirmation of Benedict W. J. Irwin's Jul 26 2017 `A101035` logarithmic generating function conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A167894 A188458 A101035`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A101035&fmt=json`):**
   - `A101035` rev. 37: `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))). - _Benedict W. J. Irwin_, Jul 26 2017` remains unconfirmed.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A167894 OR all:A188458 OR all:A101035'`: `0` entries.
   - Zenodo live API (`A101035`): `0` hits.
   - `search_web`: `0` proofs of `A101035` found.

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
