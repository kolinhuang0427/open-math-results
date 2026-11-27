# Gate 2 Novelty Check — oeis-A014137 (watch-5)

- **Checked UTC:** 2026-11-27T10:49:18Z – 2026-11-27T10:49:36Z
- **Result:** **PASS** (no prior proof or confirmation of Sergei N. Gladkovskii's May 14 2013 `A014137` continued fraction conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A014137 A028495`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A014137&fmt=json`):**
   - `A014137` rev. 180: Gladkovskii's May 14 2013 entry remains `G.f. (conjecture): Q(0)/(1-x) ...` (Peter J. Taylor's Mar 23 2015 comment proves only R. J. Mathar's Dec 14 2011 D-finite recurrence directly above it, not Gladkovskii's continued fraction).

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A014137 OR all:A028495'`: `0` entries.
   - Zenodo live API (`A014137`): `0` hits.
   - `gh search issues "A014137"` & `gh search repos "A014137"`: `0` matches.
   - `search_web`: `0` proofs of Gladkovskii's continued fraction found.

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
