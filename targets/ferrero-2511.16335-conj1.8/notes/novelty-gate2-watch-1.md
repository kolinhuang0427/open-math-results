# Gate 2 Novelty Receipt — `ferrero-2511.16335-conj1.8`

- **UTC Time:** 2026-11-26T20:06:25Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources & Exact Queries Checked

1. **Local watch snapshots (`watch/`):**
   - `grep -rniE "2511\.16335|standard fast join|fixed propagation time|propagation time intervals|PTbar" /Users/kev/Documents/open-math/watch/` -> 0 matches.
   - `grep -rniE "2511\.16335|ferrero" watch/snapshots/1337-solved-conjectures/` -> only `#323` (*Boyer–Brimkov–English–Ferrero–Keller–Kirsch–Phillips–Reinhart conjecture*, 2019 path-extremal zero forcing $z(G;k) \le z(P_n;k)$, unrelated).
2. **GitHub API live searches (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+2511.16335+OR+"standard+fast+join"+OR+"fixed+propagation+time"` -> 0 hits.
   - `search/code?q=repo:1337isnot1337/solved-conjectures+2511.16335+OR+"standard+fast+join"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+2511.16335+OR+"standard+fast+join"` -> 1 hit: `#8371` (*"Research: fixed standard zero forcing time (Conjecture 1.8)"*, closed `2026-09-16T23:35:45Z`). Body explicitly records *"Mathematical exploration stopped early... This closes the bounded research task, not the published conjecture... The mathematical target remains open."*
   - `search/code?q=repo:the-omega-institute/trureturing+2511.16335+OR+"standard+fast+join"` -> 0 hits.
   - `search/code?q=repo:PrincipiaMathOrg/math-solutions+2511.16335+OR+"standard+fast+join"` -> 0 hits.
   - `search/code?q="2511.16335"+OR+"standard+fast+join"` -> 0 hits.
3. **arXiv API (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2511.16335" OR (cat:math.CO AND abs:"propagation time" AND abs:"zero forcing")' --max-results 10` -> 22 total results (top 10 inspected: `2609.35522v1`, `2602.16300v1`, `2512.01429v1`, `2511.16335v1`, `2508.07293v1`, `2501.03472v2`, `2310.18513v2`, `2307.10548v1`, `2111.12240v1`).
4. **Web search (`search_web`):**
   - `"2511.16335" OR "standard fast join" OR "Zero forcing propagation time intervals" disproved OR counterexample OR Ferrero Hogben`

## Near Misses & Why They Do Not Settle Conjecture 1.8

- `the-omega-institute/trureturing#8371`: Explicitly investigated Conjecture 1.8 of `2511.16335`, failed to resolve it, and closed on `2026-09-16` noting the mathematical target remains open; 0 code matches in that repo.
- `1337isnot1337/solved-conjectures#323` (*Boyer–Brimkov–English–Ferrero–Keller–Kirsch–Phillips–Reinhart conjecture*): Same author surname (Ferrero) and zero forcing domain, but concerns the path-extremal zero forcing bound $z(G;k) \le z(P_n;k)$, not $\overline{\mathrm{PT}}(G)=1$ vs standard fast joins.
- `arXiv:2609.35522v1` (McKay, Ray, Valliere, Sept 2026): *"Maximizing the discrepancy between zero forcing parameters relative to graph order"* bounds the gap between maximum and minimum propagation times of *minimum* zero forcing sets, whereas Conjecture 1.8 concerns graphs where *all minimal* forcing sets have propagation time 1 ($\overline{\mathrm{PT}}(G) = 1$).

## What Was Not Covered

- No `watch/snapshots/arxiv/citing/ferrero-2511.16335-conj1.8.json` file was present yet (OpenAlex citing works for `2511.16335` not checked via OpenAlex API in this Gate 2 check; deferring to `@watch-5` for citation-graph coverage).
- Closed-access papers or private repositories not indexed on arXiv, GitHub, or web search.
