# Gate 2 Novelty Receipt — `chang-2201.02781-conj2`

- **UTC Time:** 2026-11-26T23:42:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 8 (`2026-11-26T23:40:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2201.02781 fgndi "Chang–Yang–Yin–Yao" Keusch 2303.02611` -> 0 hits beyond `watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` (`citing_count: 0`) and `openalex_works_cache.json`.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing`, `aliromman/math`, GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"2201.02781"` & `"neighbor-distinguishing"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+"2201.02781"` & `"neighbor-distinguishing"` -> 0 hits.
   - `aliromman/math` (all PRs): PR `#19`–`#107` matched substring `"chang"` in `"change"`/`"exchanges"` only; 0 matches on `2201.02781` or NFSD coloring.
   - Global `search/issues?q="2201.02781"` -> 0; `"fgndi"` -> 0; global `search/code?q=2201.02781` & `q=fgndi` -> unrelated logs/binaries only.
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2201.02781" OR all:"fgndi" OR (all:"full general neighbor-distinguishing")'` -> `2201.02781v1` sole entry.
   - `https://zenodo.org/api/records?q=2201.02781&size=5` & `q="full general neighbor-distinguishing"&size=5` -> `total: 0`.
   - `search_web` for `"2201.02781" OR ("full general neighbor-distinguishing" ...)` -> confirms Conjecture 2 remains open for general connected graphs beyond special classes (paths, cycles, 3-regular, stars, bipartite, Halin).

## Near Misses

- Same-paper special cases (`2201.02781v1`), Cheng–Yang–Yao–Luo (2022, Halin graphs), and proper-total-coloring variant `ftndi_{\sum}` (`TARGET.md`).

## What Was Not Covered

- Paywalled Chinese-language journals and private repositories.
