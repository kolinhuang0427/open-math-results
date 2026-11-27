# Gate 2 Novelty Receipt — `gaetz-2512.08168-conj1`

- **UTC Time:** 2026-11-26T23:24:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 7 (`2026-11-26T23:05:56Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2512.08168 Gaetz "union-intersection" "Bruhat projection"` -> `MattiaCalzavara/gaetz-gao-conjecture-proof` (strong $q$-log-concavity, unrelated) and `arXiv:2611.33572v1` (*Reflection subgroups and the Lookup Conjecture*, unrelated); 0 hits on Conjecture 1.3 (`conj:union-intersection`).
2. **Live `1337isnot1337/solved-conjectures`, `trureturing`, `trureturing-tools`, `aliromman/math` (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"Gaetz"` and `"2512.08168"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+"2512.08168"` -> `#7333` (`trureturing-tools` `SCREENED-OUT-R52.md` line 407 notes Conjecture 1.9 settled by the same paper's Theorem 6.2, NOT Conjecture 1.3); `"Gaetz"` -> `#24638` (`A391810`, unrelated).
   - `aliromman/math` (all PRs): PR `#38` (signed quiddities at Hecke parameter $q \ge 4$), unrelated.
   - Global `search/issues?q="conj:union-intersection"` -> 0; global `search/code?q="union-intersection"+"Bruhat"` -> 0; `search/code?q=2512.08168` -> `SCREENED-OUT-R52.md` (Conjecture 1.9) and arXiv RSS feeds only.
3. **Live Zenodo API & web search:**
   - `https://zenodo.org/api/records?q=2512.08168&size=5` & `q="Gaetz" AND "Bruhat"&size=5` -> `total: 0`.
   - `search_web` for `"2512.08168" ("Conjecture 1.3" OR "union-intersection" OR "proved" OR "Bruhat")` -> no resolution beyond finite Weyl groups & rank $\le 3$ in `arXiv:2512.08168v2`.

## Near Misses

- `arXiv:2512.08168v2` proves `conj:union-intersection` for finite Weyl groups (Theorem 1.2) and Coxeter groups of rank $\le 3$ (Theorem 3.7).
- `the-omega-institute/trureturing-tools` `SCREENED-OUT-R52.md` mentions `arXiv:2512.08168` Conjecture 1.9 (not Conjecture 1.3).

## What Was Not Covered

- Private repositories and non-indexed post-June 2026 manuscripts.
