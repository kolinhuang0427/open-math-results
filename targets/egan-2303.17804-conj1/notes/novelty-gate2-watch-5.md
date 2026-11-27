# Gate 2 Novelty Check — egan-2303.17804-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T10:44:15Z – 2026-11-27T10:44:45Z
- **Result:** **PASS** (no prior proof or settlement of Egan–Nikolayevsky `arXiv:2303.17804v1` / *Discrete Math.* 347(2) (2024) Art. 113778 simple-graph Conjecture for $d_{\min} \ge 4$ found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2303.17804 Egan "10.1016/j.disc.2023.113778" "potentially 4-graphic"`
   - Result: `60` lines across `25/619` files (all unrelated `"Egan"` substrings: `Elegant*`, `Geoghegan`, `Egan–Kotsireas` `2610.27175`; `0` hits for `2303.17804` or `113778`).

2. **arXiv / Semantic Scholar:**
   - `id:2303.17804`: sole version `2303.17804v1` (`2023-03-31T05:26:45Z`).
   - `abs:2303.17804`: `0` entries.
   - S2 `ARXIV:2303.17804/citations`: `1` citation (`arXiv:2311.00110` Talbot–Yan, *Degree Sequences of Triangular Multigraphs*, EJC 2024 — covers multigraphs only, leaving simple graphs open).

3. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2303.17804`): `0` hits.
   - `gh search issues "2303.17804"` & `gh search repos "2303.17804"`: `0` matches.
   - `search_web` (`"2303.17804" OR "10.1016/j.disc.2023.113778" OR "Egan" "4-graphic" OR "potentially triangular" proved`): confirms only the biregular case in `2303.17804` is published; general simple-graph conjecture remains open.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live arXiv, S2 citations, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits for the general simple-graph conjecture.
