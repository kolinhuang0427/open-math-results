# Gate 3 Novelty Receipt (`watch-5`) — `targets/chervov-2509.19162-conj9/`

- **Checked UTC:** `2026-11-27T09:04Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/chervov-2509.19162-conj9/`)
- **Target Scope:** A. Chervov et al., `arXiv:2509.19162v2` (`2026-04-01`), Subsection *"Bounds on the diameters of unitriangular groups"*, Conjecture 9 (`diam(U(n, Z/2Z)) = A136184(n)`).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 605 files):**
   - `.venv/bin/python tools/novelty_grep.py 2509.19162 A136184 metacyclic --max-per-file 5 --max-total 15`: `14` lines across `5/605` files (`atlas-lean` is Kourovka 15.33; `watch/snapshots/arxiv/` lists only citing papers of `2509.19162`).
   - `.venv/bin/python tools/novelty_grep.py 2509.19162 Chervov Fedoriaka "unitriangular"`: `15` lines across `7/125` files (unrelated `1337` Valiant/projection, `atlas-lean` Kourovka 18.86, `trureturing` Nikolov–Segal over odd primes, arXiv `2611.22213v1` continuous matrices on $\mathbb{R}^2$).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2509.19162']` (`max_age=300`): confirms `2509.19162v2` (`2026-04-01T15:54:42Z`) remains latest version.
   - `all:A091524 OR abs:"2509.19162"` (`max_age=300`): `total: 0`.
   - OpenAlex (`cited_by_count: 9`): citing papers `2610.22571`, `2610.14373`, `2610.08385` (cycle-type Cayley diameters), `2607.12026`, `2511.16959` do not address Conjecture 9 / `A136184` (as also confirmed in `AUDIT.md` §3).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2509.19162&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
