# Gate 2 Novelty Receipt (`watch-6`) — `targets/derycke-2402.15372-conj7_1/`

- **Checked UTC:** `2026-11-27T09:42:48Z`
- **Target:** Derycke–Dukes–Le Borgne, `arXiv:2402.15372v3`, Section 6, Conjecture 6.1 (`conj:ITCCTIsymmetry`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2402.15372" "ITCCTIsymmetry" ...`: `0` hits across `608` snapshot files.
- `gh search repos "2402.15372" --limit 5`: `[]`
- `gh search issues "2402.15372" --limit 10`: `[]`
- `gh search code "2402.15372" --limit 5`: hits `jhparkerb/polyplets` `literature/polyplets-2024-2026.bib` (inspected via `gh api`: BibTeX citation only), `ehijano/rss_fetch`, and unrelated numeric data (`0` proofs).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2402.15372`: `2402.15372v3` (`2025-12-19`) remains latest version.
- Zenodo API (`https://zenodo.org/api/records?q=%222402.15372%22&size=5`): `0` records.
- `search_web` (`"2402.15372" OR ("Derycke" "ITCCTIsymmetry" ...)`): returns only `2402.15372`, no proof found.
- Note: also reviewed `notes/novelty-derycke-lit.md` citing checks of S2/OA citing papers (`2506.23237`, `2409.11811`, `2401.06488`); Semantic Scholar API returned HTTP 429 during our live re-check.

## Coverage Limits
- Live Semantic Scholar API returned HTTP 429 (`Too Many Requests`); relies on `notes/novelty-derycke-lit.md` + local snapshots (`608` files), live GitHub, arXiv, Zenodo, and `search_web`.
