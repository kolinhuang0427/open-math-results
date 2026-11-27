# Gate 2 Novelty Check — kaul-2112.05316-ques3 (watch-5)

- **Checked UTC:** 2026-11-27T10:23:51Z – 2026-11-27T10:24:30Z
- **Result:** **PASS** (no prior resolution of Questions 2 & 3 for $p \ge 4$ or $d_G(v) \ge 4$ found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2112.05316 Kaul Mudrock`
   - Result: `8` hits across `2/618` snapshot files (`the-omega-institute/trureturing` `MiskaUlasSigmaThreeBound` substring matches; `0` hits for `2112.05316`).

2. **arXiv API (`tools/arxiv_fetch.py`):**
   - `2112.05316`: latest version `2112.05316v2` (`2023-08-14`).
   - `abs:"2112.05316"`: `0` entries.
   - Inspected Semantic Scholar citing preprints on arXiv (`2610.14892v1`, `2608.19773v2`, `2605.10861v2`, `2210.06000v4`, `2203.07704v1`):
     - `2610.14892v1`: bipartite independent-set rigidity.
     - `2608.19773v2`: chromatic vs list-color non-persistence.
     - `2605.10861v2`: enumeratively chromatic-choosable theta graphs.
     - `2210.06000v4`: 2-connected upper bounds & canonical labelings.
     - `2203.07704v1`: $DP_\approx$ and $DP_<$.
     - None resolves Question 2 or Question 3 ($p \ge 4$, $d_G(v) \ge 4$).

3. **OpenAlex / Semantic Scholar / Zenodo / Web:**
   - OpenAlex: `cited_by=1`.
   - Semantic Scholar: `6` citations (`5` arXiv preprints inspected above + `2022 Bound for DP color function of 2-connected graphs`).
   - Live Zenodo search (`2112.05316`): `0` hits.
   - Web search: confirms *Enumerative Combinatorics and Applications* 4 (2024) publication; `0` resolutions of $p \ge 4$ / $d_G(v) \ge 4$.

## Coverage Limits
- Non-arXiv paywalled/offline citing papers (`2022 Bound for DP color function of 2-connected graphs`) judged via title/abstract metadata where full text is unavailable; local snapshot coverage reflects latest Sweep 2 pull (`2026-11-27T09:55:58Z`).
