# Gate 2 Novelty Receipt — `oeis-A006255`

- **UTC Time:** 2026-11-26T22:22:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 5 (`2026-11-26T22:07:29Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A006255 Padhi A386251 2512.24346 Linusson` -> 0 hits for `A006255`; `"Padhi"` hits only `1337` `#691` (unrelated permutation-family recurrence) and `jaideepsaipadhi/erdos-sums-almost-primes` (Gorodetsky–Lichtman–Wong).
2. **Live `the-omega-institute/trureturing` & GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:the-omega-institute/trureturing+"A006255"` -> `#29470` (*full Kagey A343881/A343825 valuation*, unrelated to Padhi's threshold on `A006255`).
   - Global `search/issues?q="A006255"` -> `#29470` and unrelated `guard/guard#736`.
   - Global `search/code?q=A006255` -> `archmageirvine/joeis` (`A006255.java`), `peterkagey/math` (`a006255.rb`, `A006255.hs`), `Debdut/oeis.haskell`; sequence definitions/computations only, no proof of Padhi (2026).
3. **Live OEIS, arXiv & Zenodo:**
   - `https://oeis.org/search?q=id:A006255&fmt=json` -> revision `106` (`2026-06-19T00:16:16-04:00`), unchanged, still listed as `Conjecture: ... [Corrected by Jaideep Padhi_, Jun 15 2026]`.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A006255" OR all:"A386251"'` -> `total_results: 0`.
   - `https://zenodo.org/api/records?q=A006255&size=5` -> `total: 0`.

## Near Misses

- Erdős–Selfridge (1992) (`P(n) > sqrt(2n) + 1`), Kagey–Rajesh (`arXiv:2410.04728`), and Adenwalla (`arXiv:2504.19196`), as recorded in `TARGET.md`.

## What Was Not Covered

- Print JSTOR text of Erdős–Selfridge (1992), closed-access journals, and private repositories.
