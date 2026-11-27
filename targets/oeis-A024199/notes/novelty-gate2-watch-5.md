# Gate 2 Novelty Check — oeis-A024199 (watch-5)

- **Checked UTC:** 2026-11-27T10:35:37Z – 2026-11-27T10:36:02Z
- **Result:** **PASS** (no prior proof or confirmation of Peter Bala's Nov 15 2016 `A024199` double-factorial sum / EGF conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A024199`
   - Result: `0` lines across `0/619` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A024199&fmt=json`):**
   - `A024199` rev. 80: Bala's Nov 15 2016 entry remains prefixed with `Conjecture: a(n) = 1/2*Sum_{k = 0..2*n-1} (-1)^(n-k+1)*k!*(2*n - 2*k - 3)!! ...` with no confirmation note.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A024199'`: `0` entries.
   - Zenodo live API (`A024199`): `0` hits.
   - `gh search issues "A024199"` & `gh search repos "A024199"`: `0` matches.
   - `search_web` (`"A024199" "Peter Bala" OR "conjecture" OR "arcsin"`): only OEIS `A024199` and unrelated Bala `arcsin(tan x)` / `A012780` entries; `0` proofs of `A024199` found.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
