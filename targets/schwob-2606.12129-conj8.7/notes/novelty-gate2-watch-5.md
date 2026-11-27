# Gate 2 Novelty Check — schwob-2606.12129-conj8.7 (watch-5)

- **Checked UTC:** 2026-11-27T10:39:48Z – 2026-11-27T10:40:29Z
- **Result:** **PASS** (no prior proof or settlement of Ludovic Schwob `arXiv:2606.12129v1` §8 Conjecture 8.7 `cnj:Dtype` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2606.12129 Schwob "cnj:Dtype" "Conjecture 8.7"`
   - Result: `7` lines across `5/619` files (`watch/snapshots/arxiv/citing_papers.*` entry for `2606.12129` showing `OpenAlex cited_by=0; S2=0`, and unrelated `a1ua/bourin-zhang-conj87-lean4` on Bourin–Zhang `2610.30538`).

2. **arXiv / Semantic Scholar:**
   - `id:2606.12129`: sole version `2606.12129v1` (`2026-06-10T14:22:22Z`).
   - `abs:2606.12129`: `0` citing/matching abstracts.
   - S2 `ARXIV:2606.12129/citations`: `0` citations.

3. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2606.12129`): `0` hits.
   - `gh search issues "2606.12129"` (only unrelated `trureturing#22269` Liang–Sagan `Pin_n`), `gh search repos "2606.12129"` (`0`).
   - `search_web` (`"2606.12129" OR "Schwob" "Conjecture 8.7" OR "Dtype" proved OR proof`): confirms Conjecture 8.7 remains open beyond $D_5$.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live arXiv, S2 citations, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
