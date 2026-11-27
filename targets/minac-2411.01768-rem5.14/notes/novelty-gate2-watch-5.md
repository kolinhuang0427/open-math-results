# Gate 2 Novelty Check — minac-2411.01768-rem5.14 (watch-5)

- **Checked UTC:** 2026-11-27T10:30:03Z – 2026-11-27T10:33:39Z
- **Result:** **PASS** (no prior refutation or resolution of Mináč–Nguyen–Tân `arXiv:2411.01768v2` §5.2 Remark 5.14 `rem:same_degree` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2411.01768 "Remark 5.14" "same_degree" "gcd-graph" "Mináč"`
   - Result: `11` lines across `10/619` snapshot files:
     - `aliromman__math#88`: Fekete polynomial equidistribution (unrelated).
     - `arXiv:2611.15026v2`: Tung T. Nguyen *Spectra of gcd-graphs over a matrix ring* (matrix rings $M_n(\mathbb{F}_q)$, not $\mathbb{F}_q[x]$).
     - `arXiv:2409.01929`: authors' earlier paper *On the gcd-graphs over polynomial rings*.
     - `0` hits for `2411.01768`, `Remark 5.14`, or `rem:same_degree`.

2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `id:2411.01768`: latest version `2411.01768v2` (`updated: 2026-08-03T02:49:58Z`).
   - `abs:2411.01768`: `0` entries.

3. **Semantic Scholar citations (`ARXIV:2411.01768/citations`):**
   - `4` citing preprints checked via `arxiv_fetch.py query`:
     - `2609.30407v1`: Ramanujan sums over finite Frobenius rings.
     - `2605.11445v1`: Analytic properties of necklace polynomials.
     - `2508.10348v1`: Supercharacters of finite abelian groups & $U$-unitary Cayley graphs.
     - `2503.04086v1`: Foundational connectivity/diameter/spectra of gcd-graphs over finite commutative rings / $\mathbb{Z}/n$-algebras.
   - None addresses Remark 5.14 (`f \in \mathbb{F}_q[x]` with distinct-degree irreducible factors).

4. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2411.01768`): `0` hits.
   - `gh search issues "2411.01768"` & `gh search repos "2411.01768"`: `0` matches.
   - `search_web` (`"2411.01768" "Remark 5.14" OR "Minac" "Nguyen" "Tan" "So's conjecture"`): `0` settlements found.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live arXiv, S2 citations, Zenodo, GitHub issues/repos, and `search_web` returned `0` settlement hits.
