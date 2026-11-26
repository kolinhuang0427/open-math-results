# Gate 2 Novelty Receipt — `dris-2202.08116-conj5.1`

- **UTC Time:** 2026-11-26T20:37:25Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources & Exact Queries Checked

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py 2202.08116 Dris "sigma(m^2)" "gcd(m"` -> 4 lines across 3 files in `1337-solved-conjectures` matching `"Drisko"` only; 0 relevant matches.
2. **GitHub API live searches (`gh api`, read-only):**
   - `search/code?q="2202.08116"+OR+"gcd(m,+sigma(m^2))"+OR+"gcd(m,sigma(m^2))"` -> 0 hits.
   - `search/issues?q="2202.08116"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+Dris+OR+2202.08116` -> 0 hits.
   - `search/code?q=repo:the-omega-institute/trureturing+Dris+2202` -> 0 hits.
   - `search/code?q=repo:1337isnot1337/solved-conjectures+Dris+OR+2202.08116` -> 0 hits.
3. **arXiv API (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2202.08116" OR (cat:math.NT AND abs:"gcd" AND abs:"sigma" AND submittedDate:[202201010000 TO 202612312359])' --max-results 10` -> 0 results.
4. **Web searches (`search_web`):**
   - `"2202.08116" OR "gcd(m, sigma(m^2))" OR "Dris" "sigma(m^2)" asymptotic density OR proved`
   - `"Meyerowitz" "sigma(m^2)" OR "gcd(m, sigma(m^2))" "mathoverflow" OR "stackexchange"`
   - `site:mathoverflow.net "Is the asymptotic density of positive integers" "sigma(n^2)"` -> MathOverflow Q369521 (*"Is the asymptotic density of positive integers $n$ satisfying $\gcd(n, \sigma(n^2))=\gcd(n^2, \sigma(n^2))$ equal to zero?"*), which contains Aaron Meyerowitz's heuristic quoted in Dris Remark 5.1, with no rigorous proof.

## Near Misses

- MathOverflow Q369521 (Aaron Meyerowitz heuristic) and Dris `2202.08116v1` Theorem 5.1 ($\mathscr{A} < 7/9$), neither of which proves $\mathscr{A} = 0$.

## What Was Not Covered

- *Octogon Mathematical Magazine* 30(2) (2022) print-only citing articles and private repositories not indexed on arXiv, GitHub, or web search.
