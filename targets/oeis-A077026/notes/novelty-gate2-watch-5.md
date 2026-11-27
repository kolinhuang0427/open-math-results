# Gate 2 Novelty Check — oeis-A077026 (watch-5)

- **Checked UTC:** 2026-11-27T10:42:30Z – 2026-11-27T10:42:57Z
- **Result:** **PASS** (no prior refutation or correction of Benedict W. J. Irwin's Sep 22 2016 `A077026` conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A188648 A077026 A075997`
   - Result: `0` lines across `0/619` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A077026&fmt=json`):**
   - `A077026` rev. 14: `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} 1-f(n,k). - _Benedict W. J. Irwin_, Sep 22 2016` remains unresolved.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A188648 OR all:A077026 OR all:A075997'`: `0` entries.
   - Zenodo live API (`A077026`): `0` hits.
   - `gh search issues "A077026"` & `gh search repos "A077026"`: `0` matches.
   - `search_web`: `0` refutations or settlements of `A077026` found.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
