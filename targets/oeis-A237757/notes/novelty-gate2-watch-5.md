# Gate 2 Novelty Check — oeis-A237757 (watch-5)

- **Checked UTC:** 2026-11-27T10:47:26Z – 2026-11-27T10:47:39Z
- **Result:** **PASS** (no prior proof or confirmation of Peter Bala's Feb 02 2021 `A237757` generating function conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A237757`
   - Result: `0` lines across `0/619` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A237757&fmt=json`):**
   - `A237757` rev. 17: `Conjectural g.f.: Sum_{n >= 0} q^(2*(n+1)^2)/Product_{k = 1..2*n+1} 1 - q^k. - _Peter Bala_, Feb 02 2021` remains marked conjectural.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A237757'`: `0` entries.
   - Zenodo live API (`A237757`): `0` hits.
   - `gh search issues "A237757"` & `gh search repos "A237757"`: `0` matches.
   - `search_web` (`"A237757" "Peter Bala" OR "2*(n+1)^2" OR "conjecture" proved`): only OEIS `A237757`; `0` proofs found.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
