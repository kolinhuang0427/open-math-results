# Gate 3 Novelty Receipt (`watch-5`) — `targets/bui-2508.04602-conj8.1/`

- **Checked UTC:** `2026-11-27T09:11Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/bui-2508.04602-conj8.1/`)
- **Target Scope:** Hong Duc Bui, `arXiv:2508.04602v1` (`2025-08-06`), Section 8.2 (*Matching Problem and Acyclicity of State Graph*): acyclicity of the triangle-matching flip graph $G$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 607 files):**
   - `.venv/bin/python tools/novelty_grep.py 2508.04602 "Hong Duc Bui" "double circle order type" --max-per-file 5 --max-total 10`: `1` line across `1/607` files (solely `AlexenderSokolov/cross-theory-formal-database` license file `arxiv-2508.04602-CC-BY-4.0.txt`).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2508.04602', '2401.09497']` (`max_age=300`): confirms `2508.04602v1` (`2025-08-06T16:23:50Z`) remains sole version.
   - `abs:"2508.04602" OR ...` (`max_age=300`): `0` hits for `2508.04602`.
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2508.04602`): `cited_by_count: 0`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2508.04602&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
