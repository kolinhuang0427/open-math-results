# Gate 2 Novelty Check — oeis-A347063 (watch-5)

- **Checked UTC:** 2026-11-27T11:09:36Z – 2026-11-27T11:09:55Z
- **Result:** **PASS** (no prior refutation of Ivan N. Ianakiev's Oct 01 2024 `A347063` `$18k+12$` Double Zumkeller conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A347063 "Double Zumkeller"`
   - Result: `0` lines across `0/651` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A347063&fmt=json`):**
   - `A347063` rev. 51: `"It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]. - _Ivan N. Ianakiev_, Oct 01 2024"` remains open/unrefuted.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A347063'`: `0` entries.
   - Zenodo live API (`A347063`): `0` hits.
   - `search_web`: `0` prior counterexamples to Ianakiev's `18k+12` Double Zumkeller claim found.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
