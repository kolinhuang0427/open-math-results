# Gate 2 Novelty Check — oeis-A123145 (watch-5)

- **Checked UTC:** 2026-11-27T10:45:31Z – 2026-11-27T10:45:47Z
- **Result:** **PASS** (no prior proof or confirmation of Sergei N. Gladkovskii's Nov 26 2012 `A123145` continued fraction EGF conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A123145`
   - Result: `0` lines across `0/619` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A123145&fmt=json`):**
   - `A123145` rev. 31: Gladkovskii's Nov 26 2012 `FORMULA` remains prefixed with `Conjecture:` with no confirmation note.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A123145'`: `0` entries.
   - Zenodo live API (`A123145`): `0` hits.
   - `gh search issues "A123145"` & `gh search repos "A123145"`: `0` matches.
   - `search_web` (`"A123145" "Gladkovskii" OR "continued fraction" OR "conjecture" proved`): only OEIS `A123145` itself; `0` proofs found.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
