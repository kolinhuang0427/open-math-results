# Gate 3 Novelty Receipt — `dawsey-2107.14284-conj5.1`

- **UTC Time:** `2026-11-27T09:07Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2107.14284`, `Dawsey`, `"supernormal"`, `"idx(p)"`.
   - `.venv/bin/python tools/novelty_grep.py 2107.14284 Dawsey "supernormal" "idx(p)"` -> `21` lines across `5/605` files:
     - `the-omega-institute/trureturing`: `DawseyPartitionPolynomialDerivativeQuestionRefutation` (`arXiv:2108.00943`, unrelated).
     - `watch/snapshots/arxiv/citing_papers.md`: lists `2511.20829v1` (checked via `arxiv_fetch.py`: computational $\pi(n)$ estimate up to $100{,}000$, unrelated), `2501.00580`, `2410.00941`, and DOI `10.1007/s11139-026-01350-4` (*Statistical inequalities on partition norms*, 2026-03-03).
2. **Live arXiv, Zenodo, and GitHub Issues (`2026-11-27T09:07Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2107.14284` -> `2107.14284v2` (`2021-09-14T22:28:54Z`) latest arXiv version.
   - `https://zenodo.org/api/records?q=2107.14284&size=5` -> `total: 0`.
   - `gh search issues "2107.14284"` -> `0` issues.

## Coverage Limits
- Paywalled journal articles (including `10.1007/s11139-026-01350-4` and *J. Number Theory* 241 (2022) 120–141 PDF), `gh search code` (recently rate-limited), and private repositories not covered.
