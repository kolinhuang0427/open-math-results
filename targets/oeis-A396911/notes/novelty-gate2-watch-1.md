# Gate 2 Novelty Receipt — `oeis-A396911`

- **UTC Time:** 2026-11-27T01:35:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 11 (`2026-11-27T01:16:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py ... A396911 Tatkiewicz phyllotaxis` -> 0 hits across `watch/snapshots/**`.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing*`, `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math`, `facebookresearch/atlas-lean` (`gh api`, read-only):**
   - `search/issues?q=repo:1337isnot1337/solved-conjectures+"A396911"` -> 0; `trureturing` / `trureturing-tools` `"A396911"` / `"phyllotaxis"` -> 0; `facebookresearch/atlas-lean` `"A396911"` -> 0; global `search/issues?q="A396911"` -> 0.
   - Recursive file trees of `rainwangphy/aftd-platform`, `valyuAI/research`, `aliromman/math`, `KnowledgeSense/math` -> 0 matches for `396911` / `phyllotaxis` / `irvine` / `tatkiewicz`.
3. **Live OEIS, Zenodo API & web search:**
   - `https://oeis.org/search?q=id:A396911&fmt=json` -> revision `48` (`2026-06-22T17:16:16-04:00`), unchanged (`Conjecture: a(n) <= (3/2) * n^2`).
   - `https://zenodo.org/api/records?q=A396911&size=5` -> `total: 0`.
   - `search_web` for `"A396911" "phyllotaxis" "Irvine"` -> no prior proof located.

## Near Misses

- `archmageirvine/joeis` (`A396911.java`) records empirical check only, as noted in `TARGET.md`.

## What Was Not Covered

- Closed-access venues and private repositories.
