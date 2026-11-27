# Gate 2 Novelty Receipt — `oeis-A400888`

- **UTC Time:** 2026-11-27T03:36:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py ... A400888 ...` -> `0` hits across `watch/snapshots/**`.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A400888` in `trureturing`, `1337isnot1337/solved-conjectures`, `atlas-lean` -> `0`.
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `VladimirReshetnikov/ProveIt`, `joaquimmj/oeis-conjectures` -> `0` matches for `A400888` / `gosper` / `lafitte`.
3. **Live OEIS, arXiv & Zenodo API:**
   - `https://oeis.org/search?q=id:A400888&fmt=json` -> revision `16` (`2026-10-15T16:25:59-04:00`), surjectivity still conjectured.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A400888"'` -> `0` results.
   - `https://zenodo.org/api/records?q=A400888&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories.
