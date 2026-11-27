# Gate 2 Novelty Check — oeis-A028495 (watch-5)

- **Checked UTC:** 2026-11-27T10:49:18Z – 2026-11-27T10:49:28Z
- **Result:** **PASS** (no prior proof or confirmation of Bill McEachen's Feb 11 2026 `A028495` asymptotic ratio conjectures found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A014137 A028495`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A028495&fmt=json`):**
   - `A028495` rev. 162: `Conjectures: a(n) ~ A160389 * a(n-1). Also a(n) ~ sqrt(A116425)*a(n-1). - _Bill McEachen_, Feb 11 2026` remains unconfirmed.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A014137 OR all:A028495'`: `0` entries.
   - Zenodo live API (`A028495`): `0` hits.
   - `gh search issues "A028495"` & `gh search repos "A028495"`: `0` matches.
   - `search_web`: `0` proofs of McEachen's `A028495` ratio conjectures found.

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
