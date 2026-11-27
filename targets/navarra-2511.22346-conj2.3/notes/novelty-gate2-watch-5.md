# Gate 2 Novelty Receipt (`watch-5`) — `targets/navarra-2511.22346-conj2.3/`

- **Checked UTC:** `2026-11-27T09:10Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Francesco Navarra, Ayesha Asloob Qureshi, and Giancarlo Rinaldo, `arXiv:2511.22346v1` (`2025-11-27`), Section 2 Conjecture 2.3 (`\label{conj}`): equality of switching rook polynomial and $h$-polynomial of $K[\mathcal{P}]$, and rook number with $\mathrm{reg} K[\mathcal{P}]$, for collections of cells $\mathcal{P}$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py 2511.22346 "Switching rook" --max-per-file 5 --max-total 15`: `0` lines across `0/605` files.
2. **Live arXiv, OpenAlex & Semantic Scholar citing sweep (`tools/arxiv_fetch.py`, `api.openalex.org`, `api.semanticscholar.org`):**
   - `id_list=['2511.22346']` (`max_age=300`): confirms `2511.22346v1` (`2025-11-27T11:36:19Z`) remains sole version.
   - `abs:"2511.22346" OR all:A158826 OR ...` (`max_age=300`): `total: 0`.
   - OpenAlex (`cited_by_count: 4`) + Semantic Scholar citations (`3` records):
     - **`arXiv:2511.22778v1`** (*"Recent Advances in the Theory of Polyomino Ideals"*, Navarra–Qureshi, *Galois J. Algebra* 1 (2025), 51–87): survey article by two of the same authors; does not refute Conjecture 2.3.
     - **`arXiv:2511.13982v3`** (*"Palindromic switching rook polynomials and domino-stable collections of cells"*, Navarra–Qureshi–Rinaldo, updated `2026-10-23`): inspected extracted TeX (`Gorenstein_Proprety.tex`) directly — cites `arXiv:2511.22346` explicitly as an open conjecture (not settled/refuted).
     - `arXiv:2309.01818` (*"On the rook polynomial of grid polyominoes"*, 2023): predates `2511.22346`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2511.22346&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Semantic Scholar, Zenodo, or `watch/snapshots/**`.
