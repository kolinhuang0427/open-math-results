# Gate 2 Novelty Receipt — `daugherty-2610.29291-conj6.1`

- **UTC Time:** 2026-11-27T01:35:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 11 (`2026-11-27T01:16:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py ... "conj:box" "wide partitions" ...` -> 0 hits across `watch/snapshots/**`.
2. **Live `the-omega-institute/trureturing*`, `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math`, `facebookresearch/atlas-lean` (`gh api`, read-only):**
   - `search/issues?q=repo:the-omega-institute/trureturing+"wide+partition"` -> 9 hits (`#20269` Conjecture 6.3, `#26377` Conjecture 6.2, unrelated CA/NC issues); 0 hits for Conjecture 6.1 (`conj:box`).
   - `search/issues?q=repo:facebookresearch/atlas-lean+"2610.29291"` -> 0.
   - Recursive file trees of `rainwangphy/aftd-platform`, `valyuAI/research` (has only Conjecture 6.3 staircase count), `aliromman/math`, and `KnowledgeSense/math` -> 0 hits for Conjecture 6.1 (`conj:box`).
3. **Live arXiv, Zenodo API & web search:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2610.29291` -> `2610.29291v1` sole version.
   - `https://zenodo.org/api/records?q=2610.29291&size=5` -> `total: 0`.
   - `search_web` for `"2610.29291" "Conjecture 6.1" "wide"` -> no prior refutation or proof found.

## Near Misses

- `trureturing#20329` / `rainwangphy/aftd-platform` / `valyuAI/research` settle Conjecture 6.3 (`9*4^{k-3}`), and `trureturing#26377` tracks Conjecture 6.2 (column-addition monotonicity), NOT Conjecture 6.1 (`conj:box`, row-addition).

## What Was Not Covered

- Private repositories and non-indexed post-Oct 2026 manuscripts.
