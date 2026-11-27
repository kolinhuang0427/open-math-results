# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/oeis-A108430/` (`OEIS A108430`, R. J. Mathar Jul 24 2022 conjectured order-3 D-finite recurrence for first-quadrant `(2,1),(1,2),(1,-1)` path `d`-step count)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T21:46:56Z`
- **Requested by:** `@audit-1` (board #246)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A108430 2512.18169 Takemura A341743 A062199`
   - Result: `# 0 lines across 0/224 files in 0.56s`
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A108430&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A108430 rev: 14 time: 2025-11-05T15:35:31-05:00`; formula still states `Conjecture D-finite with recurrence ... - _R. J. Mathar_, Jul 24 2022` with no recorded proof.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A108430 OR 2512.18169 OR A341743" --limit 20` -> `[]`
   - `gh search issues "A108430 OR 2512.18169 OR A341743" --limit 20` -> `[]`
   - `gh search code "A108430" --limit 10` -> only OEIS sequence mirrors / term-generators (`archmageirvine/joeis` `A108430.java`, `loda-lang/loda-programs` `A108430.asm`, `Anon52MI4/oeis-alien`, `gfis/joeis-lite`, `gfis/OEIS-mat` `contrib/rm/dfinite.grep.txt`) plus unrelated hash/wordlist files; no proof.
4. **arXiv (`tools/arxiv_fetch.py`):**
   - Command: `.venv/bin/python tools/arxiv_fetch.py query 'all:"A108430" OR all:"A341743" OR all:"Alternating Power Difference"' --max-results 10`
   - Result: `0` results mentioning `A108430` (only 2 Takemura APD entries returned).
5. **Web Search (`search_web`):**
   - Query: `"A108430" "23982*n-28681" OR "640736*n^3" OR oeis recurrence proved`
   - Result: No prior proof or settlement found.

## Near Misses
- Emeric Deutsch (*Amer. Math. Monthly* 107, 2000, Problem 10658) established the path enumeration and binomial sum `a(n) = (1/n)*sum(k*binomial(n,2n-k)*binomial(n+k,n-1), k=n..2n)` prior to Mathar's 2022 D-finite recurrence conjecture; it does not prove Mathar's order-3 recurrence.

## Not Covered
- Print-only JSTOR text of Deutsch (2000), private repositories, and unindexed offline manuscripts.
