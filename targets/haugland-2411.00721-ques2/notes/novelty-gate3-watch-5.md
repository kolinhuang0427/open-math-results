# Gate 3 Novelty Receipt (`watch-5`) — `targets/haugland-2411.00721-ques2/`

- **Checked UTC:** `2026-11-27T09:00Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/haugland-2411.00721-ques2/`)
- **Target Scope:** Jan Kristian Haugland and Tron Omland, `arXiv:2411.00721v2` (`2026-11-01`), Section 2 Question / Section 4 Open Problem (iii): existence of proper liftings $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ of algebraic degree $2$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 601 files):**
   - `.venv/bin/python tools/novelty_grep.py 2411.00721 Haugland Omland "proper lifting" --max-per-file 3 --max-total 15`: `15` lines across `7/167` files (`facebookresearch/atlas-lean`, `plasma-ai/erdos`, `BoltonBailey` hits are Haugland 1996 on Erdős #36; `watch/snapshots/arxiv/` lists only citing papers `2610.33131v2` and `2609.35921v1`, checked as non-settling near-misses at Gate 2).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2411.00721']` (`max_age=300`): confirms `2411.00721v2` (`2026-11-01T15:13:35Z`) remains latest version.
   - `all:A190969 OR abs:"2411.00721"` (`max_age=300`): `total: 0`.
   - Live OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2411.00721`): `cited_by_count: 5` (unchanged).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2411.00721&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
