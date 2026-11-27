# Gate 3 Novelty Check — schwob-2606.12129-conj8.7 (watch-5)

- **Checked UTC:** 2026-11-27T11:16:31Z – 2026-11-27T11:16:41Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or settlement of Ludovic Schwob `arXiv:2606.12129v1` §8 Conjecture 8.7 `cnj:Dtype` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2606.12129 "cnj:Dtype" "Middle_order"`
   - Result: `3` lines across `2/651` files (only `watch/snapshots/arxiv/citing_papers.*` showing `OpenAlex cited_by=0; S2=0`).

2. **arXiv / Semantic Scholar / Zenodo / Web:**
   - `id:2606.12129`: sole version `2606.12129v1` (`2026-06-10T14:22:22Z`).
   - `abs:2606.12129`: `0` citing/matching abstracts.
   - S2 `ARXIV:2606.12129/citations`: `0` citations.
   - Zenodo live API (`2606.12129`): `0` hits.
   - `search_web`: confirms Conjecture 8.7 remains open beyond $D_5$.

## Verification Scope
- Audit target files: `targets/schwob-2606.12129-conj8.7/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
- Verification command: `.venv/bin/python -u targets/schwob-2606.12129-conj8.7/notes/check-check-2.py`

## Coverage Limits
- Local snapshot coverage reflects `651` files; live arXiv, S2 citations, Zenodo, and `search_web` returned `0` settlement hits.
