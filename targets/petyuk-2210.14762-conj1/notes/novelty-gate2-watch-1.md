# Gate 2 Novelty Receipt — `petyuk-2210.14762-conj1`

- **UTC Time:** 2026-11-27T02:02:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 11 (`2026-11-27T01:16:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py ... 2210.14762 Petyuk "simplified de Bruijn"` -> 0 hits across `watch/snapshots/**`.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing*`, `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions` (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"2210.14762"` -> 0; `trureturing` -> 0; `trureturing-tools` -> 0; `facebookresearch/atlas-lean` -> 0; global `search/issues?q="2210.14762"` -> 0.
   - Recursive file trees of `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math`, and `JENW1N/complete-math-solutions` -> 0 matches for `2210.14762` / `petyuk` / `bruijn`.
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2606.15125,2210.14762` -> `2210.14762v2` sole version.
   - `https://zenodo.org/api/records?q=2210.14762&size=5` -> `total: 0`.
   - `search_web` for `"2210.14762" "Petyuk" "simplified de Bruijn"` -> no prior refutation found.

## Near Misses

- `arXiv:2312.10377v1` (Huang–Kitaev–Pyatkin) and `arXiv:2605.02268v2` (Roy–Hariharasubramanian), both explicitly leaving Petyuk's conjecture for $S(n, k)$ ($n \ge 4, k \ge 3$) open (`TARGET.md`).

## What Was Not Covered

- Unindexed 2025–2026 manuscripts and private repositories.
