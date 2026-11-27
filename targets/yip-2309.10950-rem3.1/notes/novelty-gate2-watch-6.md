# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/yip-2309.10950-rem3.1/` (Chi Hoi Yip `arXiv:2309.10950v2` / *Canad. J. Math.* 78 (2026), 594–618, Remark 3.3 / `thm:VLM` extended to $d=2$ for odd squares $q \ge 49$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T22:33:00Z`
- **Requested by:** `@attack-4` (board #331)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2309.10950 "Yip" "Rem 3.3" "GPS(q" "Paley"`
   - Result: 43 lines across 18/277 files (only Asgarli–Ghioca–Yip blocking-pencil, `yip_2025_problem_erdos_ingham`, `qedavid/solverz` signed difference sets, and `s66lem` Paley biplane split graph); 0 hits for `2309.10950` or `GPS(q,2)`.
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "2309.10950" --limit 10` -> `[]`
   - `gh search issues "2309.10950" --limit 10` -> 1 unrelated issue (`lalalune/ArkLib#407`).
   - `gh search code "2309.10950" --limit 15` -> only arXiv RSS/index mirrors (`ehijano/rss_fetch`, `pritam-roy-99/axiovo`) and unrelated numeric matches (`COMPAS-Surrogate`, `SlopDotCash`, etc.).
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2309.10950,2608.02568,2611.28533` -> `2309.10950v2` (`Can. J. Math. 78 (2026) 594-618`, `10.4153/S0008414X24000920`) is latest; `2608.02568v3` handles multiplicative subgroups of prime fields $\mathbb{F}_p$, and `2611.28533v1` proves $|A+A| \ge \frac{1}{8}|A|^{3/2}$ for multiplicative subgroups, neither settling Remark 3.3 for $GPS(q, 2)$.
4. **Web Search (`search_web`):**
   - Query: `"2309.10950" "Yip" OR "Remark 3.3" "Paley" clique OR "Canad. J. Math." proved`
   - Result: Only Yip's `arXiv:2309.10950` / *Canad. J. Math.* paper; no prior resolution of the $d=2$ conjecture for $q \ge 49$ found.

## Near Misses
- `arXiv:2608.02568v3` (Cochrane–Yip–Yoo) and `arXiv:2611.28533v1` (Cochrane–Cochrane–Spencer) study restricted/unrestricted sumsets of multiplicative subgroups (prime fields / $|A+A|$ lower bounds), not cliques of size $\ge \sqrt{q}$ in $GPS(q, 2)$ over odd squares $q \ge 49$.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not referencing `2309.10950`.
