# Gate 2 Novelty Check — oeis-A374602 (watch-5)

- **Checked UTC:** 2026-11-27T11:08:18Z – 2026-11-27T11:08:26Z
- **Result:** **PASS** (no prior proof or algorithm for Charles L. Hohn's `A374602` / `A377290` / `A377291` Pythagorean hyperrectangle subsequence periodicity conjectures found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A374602 A377290 A377291`
   - Result: `0` lines across `0/651` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`).

2. **Live OEIS JSON (`A374602`, `A377290`, `A377291`):**
   - `A374602` rev. 31: comments state *"it is conjectured that this is the case for all n, and that all solutions conform as such and that there are no solutions that do not, but these are not proven."*
   - `A377290` rev. 7 & `A377291` rev. 7: unproved.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A374602 OR all:A377290 OR all:A377291'`: `0` entries.
   - Zenodo live API (`A374602`): `0` hits.
   - `search_web`: confirms the periodicity, completeness, and general algorithm conjectures remain open.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
