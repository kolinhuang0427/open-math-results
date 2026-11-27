# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/oeis-A006255/` (`OEIS A006255` rev 106, Jaideep Padhi Jun 15 2026 conjecture: if $b(n)^2 \ge 2n$ then $a(n) = n + b(n)$ except $n = 2, 3, 10, 171$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T22:14:16Z`
- **Requested by:** `@attack-6` (board #298)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A006255 "A6255" Padhi "a(n) > n"`
   - Result: 4 lines across 3/265 files (`jaideepsaipadhi/erdos-sums-almost-primes`, unrelated Erdős–Gorodetsky conjecture; `1337isnot1337/solved-conjectures` Spahn–Zeilberger issue #691, unrelated); 0 matches for `A006255`.
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A006255&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A006255 rev: 106 time: 2026-06-19T00:16:16-04:00`; comment still explicitly lists `Conjecture: Let b(n) = A006530(A007913(n)). If b(n)^2 >= 2 * n then a(n) = n + b(n) except for n = 2, 3, 10, and 171. [Corrected by Jaideep Padhi_, Jun 15 2026]` with no proof cited.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A006255"` -> `[]`
   - `gh search issues "A006255"` -> only unrelated `the-omega-institute/trureturing#29470` (Kagey A343881/A343825) and `guard/guard#736`.
   - `gh search code "A006255"` -> only term-computation / OEIS script repos (`archmageirvine/joeis`, `peterkagey/math`, `Debdut/oeis.haskell`, `peterkagey/haskellOEIS`, `africamonkey/OEIS-Spider`), no proof of Padhi's 2026 conjecture.
4. **arXiv (`tools/arxiv_fetch.py`):**
   - Command: `.venv/bin/python tools/arxiv_fetch.py query 'all:"A006255" OR all:"A6255"' --max-results 10`
   - Result: `total_results: 0`, `entries: []`.
5. **Web Search (`search_web`):**
   - Query: `"A006255" "Padhi" OR "171" "a(n) > n" OR conjecture proved`
   - Result: Only OEIS `A006255` itself; no prior proof found.

## Near Misses
- Erdős–Selfridge (*Amer. Math. Monthly* 99, 1992, Problem 6655, quoted in Adenwalla `arXiv:2504.19196`) proved `P(n) > sqrt(2n) + 1 => a(n) = n + P(n)`, leaving the boundary `sqrt(2n) <= P(n) <= sqrt(2n) + 1` (containing `n = 171 = 9 * 19`) open.
- Kagey & Rajesh (`arXiv:2410.04728`) and Adenwalla (`arXiv:2504.19196`) do not address Padhi's June 2026 `b(n)^2 >= 2n` threshold or `n = 171`.

## Not Covered
- Paywalled/offline manuscripts not referencing `A006255` or Padhi, and private repositories.
