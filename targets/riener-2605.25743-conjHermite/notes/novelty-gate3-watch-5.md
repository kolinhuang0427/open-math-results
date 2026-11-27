# Gate 3 Novelty Receipt (`watch-5`) — `targets/riener-2605.25743-conjHermite/`

- **Checked UTC:** `2026-11-27T09:07Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/riener-2605.25743-conjHermite/`)
- **Target Scope:** Cordian Riener and Boris Shapiro, `arXiv:2605.25743v3` (`2026-10-21`), Conjectures 1.1 (`conj:sos`) & 5.6 (`conj:hermite`) on derivative discriminants / Hermite-matrix SOS.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py 2605.25743 Riener "Hermite-matrix" "square-graph" --max-per-file 5 --max-total 15`: `12` lines across `6/605` files (`watch/snapshots/arxiv/` records `cited_by=0`; `AlexenderSokolov/cross-theory-formal-database` license file `arxiv-2605.25743-CC-BY-4.0.txt`; `eliottcassidy2000` substring `trienerment`; `f8bsd9yqgp-maker` Graffiti.pc #138 square-graph distance; `0` prior solutions).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2605.25743']` (`max_age=300`): confirms `2605.25743v3` (`2026-10-21T05:38:56Z`) remains latest version.
   - `abs:"2605.25743"` (`max_age=300`): `total: 0`.
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2605.25743`): `cited_by_count: 0`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2605.25743&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
