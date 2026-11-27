# Gate 2 Novelty Receipt — `yip-2309.10950-rem3.1`

- **UTC Time:** 2026-11-26T22:48:30Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 6 (`2026-11-26T22:44:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2309.10950 Yip Peisert "GPS(q,2)" Paley` -> hits only `1337` Asgarli–Ghioca–Yip blocking-pencil (`arXiv:2510.15332`, unrelated).
2. **Live `1337isnot1337/solved-conjectures`, `trureturing` & GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"Peisert"` -> 0; `"Yip"` -> 12 unrelated items (`#803`, `#532`, `#826`, `#833`).
   - `search/issues?q=repo:the-omega-institute/trureturing+"2309.10950"` -> 0; `"Peisert"` -> 0; `"Yip"` -> 3 unrelated items (`#22859`, `#14878`, `#15116` on Asgarli–Yip `arXiv:2110.07176`).
   - Global `search/issues?q="2309.10950"` -> 1 unrelated (`lalalune/ArkLib#407`); `"generalized Paley" "clique number" "Peisert"` -> 0.
   - Global `search/code?q=2309.10950` -> 8 items (`SlopDotCash/proximityprize`, arXiv/RSS metadata, unrelated CSV); `"GPS(q,2)"` -> 1 unrelated (`queuecl2.cpp`).
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"2309.10950" OR all:"2611.28533" OR (all:"Peisert" AND all:"Paley" AND all:"clique")'` -> 8 hits (including `2503.09914v2`, `2403.04312v2`); none settle Yip `2309.10950v2` Remark 3.3 ($d=2$ for odd squares $q \ge 49$).
   - `https://zenodo.org/api/records?q=2309.10950&size=5` & `q="generalized Paley" AND "Peisert"&size=5` -> `total: 0`.
   - `search_web` for `"2309.10950"` / `"GPS(q,2)"` / `"Paley sum graph"` -> confirms `arXiv:2309.10950v2` = *Canad. J. Math.* 78 (2026), 594–618, no settlement of $d = 2$ found.

## Near Misses

- `arXiv:2403.04312v2` (Martin–Yip) & `arXiv:2503.09914v2` (Brouwer–Goryainov–Shalaginov–Yip) construct/classify maximal cliques in generalized Paley and Peisert graphs, and `trureturing#14878`/`#15116` address `PP(p^4, p+1, I)` (`2110.07176`), not Yip `2309.10950v2` Remark 3.3 for $GPS(q, 2)$.

## What Was Not Covered

- Private repositories and non-indexed post-2026 manuscripts.
