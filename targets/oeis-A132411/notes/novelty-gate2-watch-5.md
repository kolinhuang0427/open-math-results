# Gate 2 Novelty Check — oeis-A132411 (watch-5)

- **Checked UTC:** 2026-11-27T10:26:45Z – 2026-11-27T10:27:49Z
- **Result:** **PASS** (no prior proof or confirmation of Peter Bala's May 10 2025 $q$-series conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A132411 "Peter Bala"`
   - Result: `0` hits for `A132411` across `618` snapshot files (`28` unrelated `"Peter Bala"` hits on `A248668`, `A212334`, `A211417`, `A172572`, `A183068`, `A363419`, `A363412`).
   - Absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A132411&fmt=json`):**
   - `A132411` rev. 80: `COMMENT` entry remains prefixed with `Conjecture: the sequence terms are the exponents in the expansion of the q-series Sum_{n >= 0} q^(2*n) * Product_{k >= 2*n+2} 1 - (-q)^k = 1 + q^3 + q^8 + q^15 + q^24 + .... - _Peter Bala_, May 10 2025`.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A132411'`: `0` entries.
   - Zenodo live API (`"A132411"`, `"1 - (-q)^k"`, `"Peter Bala" A132411`): `0` hits for `A132411` (`"1 - (-q)^k"` returned `3` unrelated records on Borwein products, PUH T228, and Dumont-Foata polynomials).
   - `search_web` (`"A132411" "Peter Bala" OR "Euler" OR "theta" OR "q^2n"`): only points to OEIS `A132411` itself; `0` proofs found.

## Coverage Limits
- OpenAlex and Semantic Scholar search endpoints returned HTTP 429 during this burst; live OEIS, arXiv, Zenodo, `search_web`, and `618` snapshot files (incl. `zenodo-23112421-oeis-ids.md`) all returned live results with `0` settlement hits.
