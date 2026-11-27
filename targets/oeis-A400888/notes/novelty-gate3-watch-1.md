# Gate 3 Novelty Receipt — `oeis-A400888`

- **UTC Time:** 2026-11-27T05:35:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 17 (`2026-11-27T05:29:05Z`) `watch/snapshots/1337-solved-conjectures/` & `watch/snapshots/discovered/CATALOG.md` -> `0` hits for `A400888` / `Gosper–Lafitte`.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A400888` in `the-omega-institute/trureturing`, `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` -> `0` (`05:29Z`).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` matches (`03:22Z–03:29Z`).
3. **Live OEIS, arXiv & Zenodo API:**
   - `https://oeis.org/search?q=id:A400888&fmt=json` -> revision `16` (`2026-10-15T16:25:59-04:00`), surjectivity still conjectured (`05:09Z`).
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A400888"'` -> `0` results.
   - `https://zenodo.org/api/records?q=A400888&size=5` -> `total: 0` (`05:29Z`).

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
