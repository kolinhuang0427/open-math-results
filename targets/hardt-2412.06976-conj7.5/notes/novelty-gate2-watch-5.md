# Gate 2 Novelty Check — hardt-2412.06976-conj7.5 (watch-5)

- **Checked UTC:** 2026-11-27T10:28:45Z – 2026-11-27T10:32:50Z
- **Result:** **PASS** (no prior proof or settlement of Hardt–Wallach `arXiv:2412.06976v2` §7 Conjecture 7.5 found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2412.06976 Hardt Wallach`
   - Result: `54` lines across `18/618` snapshot files (`JPickhardt` / `Reinhardt` substring hits; `0` hits for `2412.06976` or Conjecture 7.5).

2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `id:2412.06976`: latest version `2412.06976v2` (`updated: 2025-01-24T18:29:51Z`).
   - `abs:2412.06976` and `all:"back-stable key"`: `0` entries.

3. **Semantic Scholar citations (`ARXIV:2412.06976/citations`):**
   - `5` citing works found and checked via arXiv metadata (`2604.02964v2`, `2504.03004v1`, `2501.14691v3`, `2412.02064v3`, plus `10.1017/fms.2025.10116` Pak–Robichaux Nullstellensatz paper):
     - `2604.02964v2`: probabilistic study of forward stability / record statistic on permutation classes.
     - `2501.14691v3`: double Grothendieck product stability & Lam–Lee–Shimozono finiteness conjecture.
     - `2504.03004v1` & `2412.02064v3` & `10.1017/fms.2025.10116`: complexity of Schubert vanishing (`AM ∩ coAM`).
   - None addresses Conjecture 7.5 ($\xi(\overline{\kappa}_\alpha)$).

4. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2412.06976`): `0` hits.
   - `gh search issues "2412.06976"` & `gh search repos "2412.06976"`: `0` matches.
   - `search_web` (`"2412.06976" "Conjecture 7.5" OR "Hardt" "Wallach" proved OR proof`): `0` resolving papers.

## Coverage Limits
- OpenAlex live search returned HTTP 429 during this burst; Semantic Scholar citations, arXiv, Zenodo, GitHub, `search_web`, and `618` snapshot files all returned live results with `0` settlement hits.
