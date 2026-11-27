# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/li-2505.12035-conj7/` (Li–Lu–Luo `arXiv:2505.12035v1` §1 Conjecture 7 `conj:ore`: $d_{\partial \mathcal{H}}(u) + d_{\partial \mathcal{H}}(v) \ge n+1$ forces a Hamiltonian Berge cycle in $n$-vertex $[3]$-graphs for $n \ge 6$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:47:02Z`
- **Requested by:** `@scout-7` (board #456)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A360949 2509.16034 2505.12035 "Campbell" "Rampersad" "Li-Lu-Luo"`
   - Result: `0` hits for `2505.12035` or `Li-Lu-Luo` across all 356 snapshot files.
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A360949 OR 2509.16034 OR 2505.12035"` -> `[]`
   - `gh search issues "\"A360949\" OR \"2509.16034\" OR \"2505.12035\""` -> `[]`
   - `gh search code "2505.12035"` -> only `ehijano/rss_fetch` (`rss_data/math.CO/2025-05-19_math.CO.xml`) and unrelated numerical CSVs (`cvrp_results`, `VRPTW`, etc.); `0` proof/refutation hits.
3. **arXiv (`tools/arxiv_fetch.py`) & Web Search (`search_web`):**
   - `arxiv_fetch.py query --id-list 2509.16034,2505.12035` -> `2505.12035v1` (`2025-05-17`) is sole version.
   - `search_web` -> only `arXiv:2505.12035v1` itself; no prior refutation found.

## Near Misses
- `2505.12035v1` proves existence of some constant $d_0$ and conjectures $d_0 = 1$ for $n \ge 6$.

## Not Covered
- Paywalled journals, private repositories, and offline manuscripts not citing `2505.12035`.
