# Gate 2 Novelty Receipt — `wei-2310.17337-conj1.5`

- **UTC Time:** 2026-11-26T20:02:55Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources & Exact Queries Checked

1. **Local watch snapshots (`watch/`):**
   - `grep -rniE "2310\.17337|C_k-isolation|C_4-isolation|C_5-isolation|C_8-isolation|isolating set|cycle isolation|Xiaohua Wei|Biao Zhao" /Users/kev/Documents/open-math/watch/`
   - Checked `watch/snapshots/1337-solved-conjectures/` (`CONTENTS.md`, `HISTORY.md`, `results_dirs.txt`, `open_issues_claims.md`, `open_prs.md`, `merged_prs.md`, `closed_issues.md`), `watch/snapshots/ai-collections/`, `watch/snapshots/openai-math/`, `watch/snapshots/arxiv/citing/wei-2310.17337-conj1.5.json` (`citing_count: 0`, checked `2026-11-26T19:57:51Z`).
2. **GitHub API live searches (`gh api`, read-only):**
   - `search/issues?q="2310.17337"+OR+"C_k-isolation"+OR+"C_4-isolation"+OR+"C_8-isolation"+OR+"Wei-Zhang-Zhao"` -> 517 generic hits (first 30 checked, no `2310.17337` or cycle isolation matches).
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+2310.17337+OR+isolation+OR+Wei+OR+C_k` -> 22 hits (none related to cycle isolation; `Wei` matched unrelated entries).
   - `search/code?q=repo:1337isnot1337/solved-conjectures+2310.17337+OR+C_k-isolation+OR+C_4-isolation` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+"2310.17337"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+"cycle+isolation"+OR+"C_4-isolation"+OR+"C_k-isolation"+OR+"Xiaohua+Wei"+OR+"Biao+Zhao"` -> 2 hits (`#21873`, `#21874`, unrelated Barrett–Cameron–Evans–Hall–Kempton Laplacian-spread conjectures).
   - `search/code?q=repo:the-omega-institute/trureturing+"Xiaohua+Wei"+OR+"C_4-isolation"+OR+"C_k-isolation"` -> 0 hits.
   - `search/issues?q=repo:PrincipiaMathOrg/math-solutions+2310.17337+OR+isolation` -> 0 hits; `search/code?q=repo:PrincipiaMathOrg/math-solutions+2310.17337+OR+C_4-isolation+OR+C_k-isolation` -> 0 hits.
   - `search/code?q=repo:openai/math+2310.17337` -> 0 hits.
   - `search/repositories?q="2310.17337"+OR+"C_k-isolation"+OR+"C_4-isolation"` -> 3 unrelated hits (`censored-keyword-isolation`, `Isolation_Forest`).
3. **arXiv API (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2310.17337" OR (cat:math.CO AND ti:isolation AND (ti:cycle OR ti:cycles OR ti:C_k OR ti:C_4 OR ti:C_5))' --max-results 15` -> 8 results.
4. **Web searches (`search_web`):**
   - `"2310.17337" "C_k" OR "C_5" OR "C_8" OR "disproved" OR "counterexample" OR "truncated tetrahedron"`
   - `"m+1)/(k+2)" OR "(m+1)/(k+2)" OR "C_k-isolation" "isolation number" counterexample OR disproved OR Borg OR Scicluna`
   - `"On the C_4-isolation number of a graph" "Wei" "Zhang" "Zhao" "Discrete Mathematics, Algorithms and Applications" OR citing OR counterexample`

## Near Misses & Why They Do Not Settle Conjecture 1.5

- `ArtificialZeng/AI-Has-Taste` (`SM2-P55`): *"A strict gap between square isolation and domination in the six-dimensional cube"* proves $\iota(Q_6, Q_2) = 5 > 4 = \gamma(Q_4)$ — this is $Q_2$-isolation (4-cycle isolation in hypercubes relative to domination number $\gamma(Q_{n-2})$), NOT Wei–Zhang–Zhao Conjecture 1.5's edge-count bound $\iota(G, C_k) \le (m+1)/(k+2)$ for $k \ge 5$.
- `arXiv:2510.08361v2` (Peter Borg, Dayle Scicluna, *Discrete Appl. Math.* 394 (2026), 261–268): *"Isolation of non-triangle cycles in graphs"* proves $\iota(G, \mathcal{C}') \le (m+1)/6$ where $\mathcal{C}' = \{C_k : k \ge 4\}$, which re-proves the $k=4$ case of Wei–Zhang–Zhao but says nothing about individual $C_k$-isolation for $k \ge 5$ (such as $k=8$).
- `arXiv:2609.29488v1`, `arXiv:2507.08503v3`, `arXiv:2308.00581v1`, `arXiv:2002.07698v2`, `arXiv:1812.09305v1`: all concern other graph isolation parameters (vertex uncovering, game isolation, 1-isolation, isolating cycles in polyhedra, or general cycle isolation $\iota_c(G) \le n/4$), not $\iota(G, C_k) \le (m+1)/(k+2)$ for $k \ge 5$.

## What Was Not Covered

- Full text of paywalled *Discrete Mathematics, Algorithms and Applications* citing articles not indexed on arXiv, OpenAlex (`citing_count: 0` in snapshot), or web search summaries.
- Private repositories or preprints posted after `2026-11-26T20:02:55Z`.
