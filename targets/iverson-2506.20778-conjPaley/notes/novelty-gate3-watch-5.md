# Gate 3 Novelty Receipt (`watch-5`) — `targets/iverson-2506.20778-conjPaley/`

- **Checked UTC:** `2026-11-27T09:16Z` – `2026-11-27T09:17Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/iverson-2506.20778-conjPaley/`)
- **Target Scope:** Joseph W. Iverson and Dustin G. Mixon, `arXiv:2506.20778v1` (`2025-06-25`), Section 4 Conjecture (`conj:Paley`): $\mathrm{Aut}_s(\tilde{H}) \cong P\Gamma L(2,q)$ two-orbit structure and $\mathrm{Aut}_s / \mathrm{Aut}_w$ of constructed asymmetric SICs $\{x_{ij}\}$ for Paley I Hadamard matrices ($q > 11, q \equiv 3 \bmod 4$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py 2506.20778 Iverson "conjPaley" "asymmetric SIC" --max-per-file 5 --max-total 15`: `8` lines across `5/608` files (`the-omega-institute/trureturing*` hits concern 2021 Greaves–Iverson–Jasper–Mixon Gerzon equality, unrelated to `2506.20778`; `watch/snapshots/arxiv/citing_papers.{json,md}` record `cited_by=0`).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2506.20778', '2407.20048']` (`max_age=300`): confirms `2506.20778v1` (`2025-06-25T19:09:29Z`) remains sole version.
   - `abs:"2506.20778" OR abs:"2407.20048"` (`max_age=300`): `total: 0`.
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2506.20778`): `cited_by_count: 0`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2506.20778&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
