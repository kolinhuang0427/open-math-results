# Gate 2 Novelty Receipt (`watch-5`) — `targets/dawsey-2107.14284-conj5.1/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Madeline Locus Dawsey, Matthew Just, and Robert Schneider, `arXiv:2107.14284v2` (`2021-09-14`), Section 5 Conjecture 5.1 (prime-index Cesàro-mean Abelian limit).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py 2107.14284 Dawsey 'idx(p)' supernormal --max-per-file 3 --max-total 15`: `15` lines across `5/517` files (`the-omega-institute/trureturing` hit `DawseyPartitionPolynomialDerivativeQuestionRefutation` concerns `arXiv:2108.00943`, unrelated; remaining hits are `citing_papers.{json,md}` and `last_sweep_report.json`).
2. **Live arXiv & OpenAlex citing sweep (`watch/snapshots/arxiv/`, `tools/arxiv_fetch.py`):**
   - `id_list=['2107.14284']`: confirms `2107.14284v2` (`2021-09-14T22:28:54Z`) remains latest version.
   - `abs:"2107.14284" OR ...`: `total: 0`.
   - OpenAlex (`cited_by=15`): recent citing works `10.1007/s11139-026-01350-4` (*Statistical inequalities on partition norms*, 2026-03-03) and `arXiv:2511.20829v1` (*Partition-theoretic model of prime distribution, II*, 2025-11-25, abstract inspected via `tools/arxiv_fetch.py` — computational partition model of $\pi(n)$, does not address Conjecture 5.1).
3. **Web search (`search_web`):**
   - `"2107.14284" "Dawsey" "Conjecture 5.1"`: returns only `2107.14284` / JNT publication and unrelated Dawsey partition papers.

## What Was Not Covered
- Paywalled *J. Number Theory* 241 (2022) 120–141 PDF and closed-access/private repositories not indexed by arXiv, OpenAlex, web search, or `watch/snapshots/**`.
