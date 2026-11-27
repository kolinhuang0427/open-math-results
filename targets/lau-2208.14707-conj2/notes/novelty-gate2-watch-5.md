# Gate 2 Novelty Receipt (`watch-5`) — `targets/lau-2208.14707-conj2/`

- **Checked UTC:** `2026-11-27T09:13Z` – `2026-11-27T09:15Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Gee-Choon Lau et al., `arXiv:2208.14707v1` (`2022-08-31`) / *Discrete Mathematics Letters* 11 (2023), 76–83 (`10.47443/dml.2022.149`), Conjecture 2 ($\chi_{la}(G[H]) = \chi(G)\chi(H) \iff \chi(G)\chi(H) = 2\chi(H) + \lceil \chi(H)/k \rceil$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py 2208.14707 "local antimagic" "lexicographic product" "lau-2208" --max-per-file 5 --max-total 15`: `4` lines across `4/608` files (`kyleglsn22-spec/open-problems-lab` is Bača et al. 2022 tree leaf conjecture; `trureturing#34590` is cooling spectrum; `2611.11376v1` is fractional distance-edge-monitoring; `0` hits for `2208.14707`).
2. **Live arXiv, OpenAlex & Web checks (`tools/arxiv_fetch.py`, `api.openalex.org`, `search_web`):**
   - `id_list=['2208.14707']` (`max_age=300`): confirms `2208.14707v1` (`2022-08-31T09:13:32Z`) remains sole arXiv version.
   - `abs:"2208.14707" OR (all:"local antimagic" AND all:"lexicographic")` (`max_age=300`): `total: 2` (`2208.14707v1` and `2203.16359v1`, which predates `2208.14707`).
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2208.14707`): `cited_by_count: 1` (Semantic Scholar `/citations` hit HTTP 429 for `ARXIV:2208.14707` and 404 for `DOI:10.47443/dml.2022.149`; `search_web` `"2208.14707" OR "10.47443/dml.2022.149"` returned only `2208.14707` and the DML 2023 publication).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2208.14707&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Identity of the 1 OpenAlex-indexed work citing `10.48550/arXiv.2208.14707` (OpenAlex `/works?filter=cites:` and Semantic Scholar `/citations` returned HTTP 429); closed-access venues or private repos not indexed by arXiv, Zenodo, web search, or `watch/snapshots/**`.
