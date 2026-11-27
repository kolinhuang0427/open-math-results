# Gate 3 Novelty Receipt (`watch-5`) — `targets/dawsey-2107.14284-conj5.1/`

- **Checked UTC:** `2026-11-27T09:06Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/dawsey-2107.14284-conj5.1/`)
- **Target Scope:** Madeline Locus Dawsey, Matthew Just, and Robert Schneider, `arXiv:2107.14284v2` (`2021-09-14`), **Section 4 (`\label{sect5}`), Conjecture 4.1 (`\label{conj1}`)** (prime-index Cesàro-mean Abelian limit).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py 2107.14284 Dawsey "idx(p)" supernormal --max-per-file 5 --max-total 15`: `15` lines across `4/127` files (`the-omega-institute/trureturing` `DawseyPartitionPolynomialDerivativeQuestionRefutation` is `arXiv:2108.00943`; `watch/snapshots/arxiv/` lists only citing papers `10.1007/s11139-026-01350-4`, `2511.20829`, `2501.00580`, `2410.00941`, none settling Conjecture 4.1).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2107.14284']` (`max_age=300`): confirms `2107.14284v2` (`2021-09-14T22:28:54Z`) remains latest version.
   - `all:A097332 OR abs:"2107.14284"` (`max_age=300`): `total: 0`.
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2107.14284`): `cited_by_count: 15` (unchanged from Gate 2).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2107.14284&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Paywalled *J. Number Theory* 241 (2022) 120–141 PDF and closed-access/private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
