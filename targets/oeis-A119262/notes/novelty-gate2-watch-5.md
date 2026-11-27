# Gate 2 Novelty Check — oeis-A119262 (watch-5)

- **Checked UTC:** 2026-11-27T10:26:06Z – 2026-11-27T10:27:49Z
- **Result:** **PASS** (no prior proof or confirmation of Benedict W. J. Irwin's Apr 19 2017 Hessenberg determinant conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A119262`
   - Result: `0` lines across `0/618` files (broader `Irwin Hessenberg` returned `56` unrelated lines across `19/618` files, e.g. Toeplitz-Hessenberg Fuss-Catalan / Mathlib `Hessenberg` API).
   - Absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A119262&fmt=json`):**
   - `A119262` rev. 55: `FORMULA` entry for $M_n$ determinant remains prefixed with `Conjecture: ... - _Benedict W. J. Irwin_, Apr 19 2017` with no confirmation note.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A119262'`: `0` entries.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:Irwin AND all:Hessenberg'`: `0` entries.
   - Zenodo live API (`"A119262"`, `"Benedict W. J. Irwin"`): `0` hits for `A119262` (`1` unrelated hit `23316730` on `A005867`).
   - `search_web` (`"A119262" "Hessenberg" OR "Benedict W. J. Irwin" OR "determinant"`, `"A119262" oeis "conjecture" OR "proved" OR "proof"`): `0` prior proofs found.

## Coverage Limits
- OpenAlex and Semantic Scholar search endpoints returned HTTP 429 during this burst; live OEIS, arXiv, Zenodo, `search_web`, and `618` snapshot files (incl. `zenodo-23112421-oeis-ids.md`) all returned live results with `0` settlement hits.
