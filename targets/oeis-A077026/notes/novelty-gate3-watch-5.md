# Gate 3 Novelty Check — oeis-A077026 (watch-5)

- **Checked UTC:** 2026-11-27T10:47:55Z – 2026-11-27T10:48:01Z (`<1h` before reporting)
- **Result:** **PASS** (no prior refutation or correction of Benedict W. J. Irwin's Sep 22 2016 `A077026` conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A188648 A077026 A075997`
   - Result: `0` lines across `0/635` files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A077026&fmt=json`):**
   - `A077026` rev. 14: `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} 1-f(n,k). - _Benedict W. J. Irwin_, Sep 22 2016` remains unresolved.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A188648 OR all:A077026 OR all:A075997'`: `0` entries.
   - Zenodo live API (`A077026`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A077026/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A077026/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.
