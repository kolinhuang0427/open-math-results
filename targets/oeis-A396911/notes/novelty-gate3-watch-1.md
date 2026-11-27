# Gate 3 Novelty Receipt — `oeis-A396911`

- **UTC Time:** 2026-11-27T03:18:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 13 (`2026-11-27T02:43:40Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A396911 Tatkiewicz phyllotaxis` -> 0 hits across `watch/snapshots/**`.
2. **Live `1337isnot1337/solved-conjectures`, `trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond` (`gh api`, read-only):**
   - Issue/PR search for `A396911` in `trureturing`, `1337isnot1337/solved-conjectures`, `atlas-lean`, and global GitHub issues -> 0 hits.
   - Recursive file trees of `aliromman/math` (891), `KnowledgeSense/math` (5377), `rainwangphy/aftd-platform` (28161), `valyuAI/research` (5381), `JENW1N/complete-math-solutions` (425), `TheJustinSunPrize/awards` (82), `trureturing-tools` (1713), `DomTheDeveloper/open-math-agents` (446), `GuillaumeBAUD-coder/open-math-agents` (1539), `DomTheDeveloper/ProofPlaygrond` (68), and `atlas-lean` (53996, truncated) -> 0 matches for `A396911` / `phyllotaxis` / `tatkiewicz`.
3. **Live OEIS, arXiv & Zenodo API:**
   - `https://oeis.org/search?q=id:A396911&fmt=json` -> revision `48` (`2026-06-22T17:16:16-04:00`), unchanged (`Conjecture: a(n) <= (3/2) * n^2`).
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A396911" OR (all:"phyllotaxis" AND all:"Tatkiewicz")'` -> 0 results.
   - `https://zenodo.org/api/records?q=A396911&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `facebookresearch/atlas-lean` root tree was `truncated=True` (53996 paths), checked additionally via `search/issues`.
