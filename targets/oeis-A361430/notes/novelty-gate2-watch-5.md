# Gate 2 Novelty Check — oeis-A361430 (watch-5)

- **Checked UTC:** 2026-11-27T10:50:58Z – 2026-11-27T10:51:49Z
- **Result:** **PASS** (no prior proof or confirmation of the `A361430` / `A298826` conjectures by Oudra, Kotesovec, and Schulte found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A361430`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`A361430` & `A298826`):**
   - `A361430` rev. 41: `Conjecture: a(n) = abs(A298826(n)).` remains unconfirmed.
   - `A298826` rev. 125: Ridouane Oudra (Nov 19 2019), Vaclav Kotesovec (Mar 12 2023), and Werner Schulte (Jun 09 2025) formulas all remain explicitly prefixed with `Conjecture:`.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A361430'` & `all:A298826`: `0` entries.
   - Zenodo live API (`A361430`, `A298826`): `0` hits.
   - `search_web`: `0` proofs of `A361430` or `A298826` found.

## Coverage Limits
- GitHub search endpoints (`gh search issues/repos`) returned HTTP 403 rate-limit exceeded during this check; mitigated by `635` local repo snapshots (`0` hits) plus live OEIS, arXiv, Zenodo, and `search_web`.
