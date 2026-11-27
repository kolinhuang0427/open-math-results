# Gate 2 Novelty Check — oeis-A124380 (watch-5)

- **Checked UTC:** 2026-11-27T11:03:51Z – 2026-11-27T11:04:46Z
- **Result:** **PASS** (no prior proof or confirmation of Vaclav Kotesovec's Sep 18 2024 `A124380` logarithmic asymptotic conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A124380`
   - Result: `0` lines across `0/651` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md` and `watch/snapshots/zenodo-23114921-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A124380&fmt=json`):**
   - `A124380` rev. 39: `Conjecture: log(a(n)) ~ n*log(n)/2 - n*(1 + log(2))/2. - _Vaclav Kotesovec_, Sep 18 2024` remains unconfirmed.

3. **arXiv / Zenodo / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A124380'`: `0` entries.
   - Zenodo live API (`A124380`): `0` hits.
   - `search_web`: `0` proofs of Kotesovec's `A124380` conjecture found.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live OEIS, arXiv, Zenodo, and `search_web` returned `0` settlement hits.
