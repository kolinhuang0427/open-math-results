# Gate 3 Novelty Receipt (`watch-6`) — `targets/bartnicki-2303.08771-conj3/`

- **Checked UTC:** `2026-11-27T09:39:57Z` (`<1h` before submission)
- **Target:** Bartnicki–Czerwiński–Grytczuk–Miechowicz, `arXiv:2303.08771v1` / *Graphs and Combinatorics* **41** (2025), Art. 80 (`DOI: 10.1007/s00373-025-02934-5`), Section 3 Conjecture 3 ($\zeta(G) \le \mathrm{col}(G)$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2303.08771" "A121754" "A121752"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2303.08771" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2303.08771" --limit 10 --json repository,number,title,state,url`: `[]`
- Semantic Scholar citations of *Graphs and Combinatorics* 41 (2025), Art. 80 (`DOI: 10.1007/s00373-025-02934-5`): `0` citations (`{"offset": 0, "data": []}`; matches OpenAlex `cited_by_count = 0` in `AUDIT.md`).
- Zenodo API (`https://zenodo.org/api/records?q=%222303.08771%22&size=5`): `0` records.
- arXiv (`09:28Z`) & `search_web` (`09:39Z`): `2303.08771v1` sole arXiv version; no published refutation found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.
