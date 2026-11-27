# Gate 2 Novelty Receipt — `linusson-2512.24346-conj1`

- **UTC Time:** 2026-11-26T22:18:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 5 (`2026-11-26T22:07:29Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A006255 Padhi A386251 2512.24346 Linusson` -> 0 hits for `2512.24346` / `Linusson` across `watch/snapshots/**`.
2. **Live `the-omega-institute/trureturing` & GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:the-omega-institute/trureturing+"Linusson"` -> 8 hits, all unrelated (`arXiv:2305.05275v1`, `arXiv:2610.07442`, 2014 Assis–Jacobsen–Jensen–Maillard–McCoy, `A185771`).
   - Global `search/issues?q="2512.24346"` -> 0 hits; `"Linusson" "Plancherel"` -> 0 hits.
   - Global `search/code?q=2512.24346` -> 19 items (`AlexenderSokolov/cross-theory-formal-database` indexing `arXiv:2512.24346v1` author text, `ehijano/rss_fetch`, unrelated `.txt`); no proof of `conj:complement`.
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2512.24346" OR all:"k-Plancherel Measure"'` -> `2512.24346v1` sole entry.
   - `https://zenodo.org/api/records?q=2512.24346+OR+"k-Plancherel+Measure"&size=5` -> `total: 0`.
   - `search_web` for `"2512.24346" OR ("Linusson" "k-Plancherel" ("proved" OR "complement" OR "conj:complement"))` -> no prior proof of Conjecture 1 found.

## Near Misses

- `arXiv:2512.24346v1` Lemma 3.9 (*k-conjugates and complements of partitions*) and computational verification for $k \le 6$ by the authors.

## What Was Not Covered

- Private repositories and non-indexed post-2025 manuscripts.
