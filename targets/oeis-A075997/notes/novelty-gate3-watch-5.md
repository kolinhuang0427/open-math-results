# Gate 3 Novelty Check — oeis-A075997 (watch-5)

- **Checked UTC:** 2026-11-27T10:47:55Z – 2026-11-27T10:48:01Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Benedict W. J. Irwin's Sep 23 2016 `A075997` conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A188648 A077026 A075997`
   - Result: `0` lines across `0/635` files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A075997&fmt=json`):**
   - `A075997` rev. 37: `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} f(n+k,n-k). - _Benedict W. J. Irwin_, Sep 23 2016` remains unconfirmed.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A188648 OR all:A077026 OR all:A075997'`: `0` entries.
   - Zenodo live API (`A075997`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A075997/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A075997/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
