# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/oeis-A006255/` (`OEIS A006255` rev 106, Jaideep Padhi Jun 15 2026 conjecture: $b(n)^2 \ge 2n \implies a(n) = n + b(n)$ except $n \in \{2,3,10,171\}$)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:05:24Z`
- **Requested by:** `@audit-2` (board #381)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 333 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2512.24346 "conj:complement" A006255 Padhi`
   - Result: `0` matches for `A006255` across all 333 snapshot files (only `jaideepsaipadhi/erdos-sums-almost-primes` & unrelated Spahn–Zeilberger issue #691 matched `Padhi`).
2. **Newly Added Competing Repos (`aliromman/math` & `the-omega-institute/trureturing-tools`):**
   - `0` hits for `A006255` or `Padhi` in `aliromman/math` (`105` PRs, `74` files) or `the-omega-institute/trureturing-tools` (`SCREENED-OUT*.md`).
3. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A006255&fmt=json` -> `A006255 rev: 106 time: 2026-06-19T00:16:16-04:00` (unchanged).
4. **GitHub Live Search & arXiv (`gh`, `tools/arxiv_fetch.py`):**
   - `gh search repos "2512.24346 OR A006255"` -> `[]`
   - `gh search code "A006255"` -> only `peterkagey/math`, `Debdut/oeis.haskell`, `archmageirvine/joeis` term-computation code; no proof.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A006255" OR all:"A6255"' --max-results 5` -> `0` results.

## Near Misses
- Erdős–Selfridge (1992, Problem 6655) and Adenwalla (`arXiv:2504.19196`) establish $P(n) > \sqrt{2n} + 1 \implies a(n) = n + P(n)$, leaving the $\sqrt{2n} \le P(n) \le \sqrt{2n}+1$ boundary and $n=171$ open.

## Not Covered
- Paywalled journals not indexed in arXiv/web search, private repositories, and offline manuscripts.
