# Gate 2 Novelty Check — oeis-A127276 (watch-5)

- **Checked UTC:** 2026-11-27T11:17:01Z – 2026-11-27T11:17:44Z
- **Result:** **PASS** (no prior proof or confirmation of R. J. Mathar's Dec 11 2010 `A127276` Hankel-transform g.f. / formula conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A227543 A347063 A127276`
   - Result: `0` lines across `0/651` snapshot files (also absent from Zenodo `23112421` and `23114921` OEIS ID snapshots).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A127276&fmt=json`):**
   - `A127276` rev. 33: `Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2). - _R. J. Mathar_, Dec 11 2010` remains unconfirmed.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A227543 OR all:A347063 OR all:A127276'`: `0` entries.
   - Zenodo live API (`A127276`): `0` hits.
   - `search_web`: `0` proofs of Mathar's `A127276` conjecture found.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
