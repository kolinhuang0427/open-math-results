# Gate 2 Novelty Check — marberg-2611.19371-conj (watch-5)

- **Checked UTC:** 2026-11-27T11:03:52Z – 2026-11-27T11:05:22Z
- **Result:** **PASS** (no prior proof or settlement of Marberg–Morales–Yu `arXiv:2611.19371v1` §3.3 Conjecture 3.8 `iG-conj` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2611.19371 Marberg "iG-conj" "kInvBPD"`
   - Result: `15` lines across `5/651` files (all `watch/snapshots/arxiv/` entries for `2611.19371v1` itself and symplectic paper `2611.34697`; `0` settlement hits).

2. **arXiv / Semantic Scholar citations:**
   - `id:2611.19371`: sole version `2611.19371v1` (`2026-11-14T12:23:48Z`).
   - `abs:2611.19371`: `0` citing/matching abstracts.
   - S2 `ARXIV:2611.19371/citations`: `2` citations checked via `arxiv_fetch.py`:
     - `arXiv:2611.34697` (Hamaker–Weigandt, *Symplectic bumpless pipe dreams*, explicitly restricts to $\mathrm{Sp}_{2n}$ and leaves orthogonal/involution Grothendieck BPDs open).
     - `arXiv:2503.16403v3` (Ferroni–Morales–Panova, *Skew shapes, Ehrhart positivity and beyond*, unrelated to `iG-conj`).

3. **Zenodo / Web:**
   - Zenodo live API (`2611.19371`): `0` hits.
   - `search_web`: only `arXiv:2611.19371v1` itself; `0` proofs of `iG-conj` found.

## Coverage Limits
- Local snapshot coverage reflects `651` files; live arXiv, S2 citations, Zenodo, and `search_web` returned `0` settlement hits.
