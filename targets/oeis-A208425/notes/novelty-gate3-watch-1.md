# Gate 3 Novelty Receipt — `oeis-A208425`

- **UTC Time:** 2026-11-27T04:10:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` & `watch/snapshots/discovered/CATALOG.md` -> `0` hits for `A208425` / `conjecture_2`.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches in `the-omega-institute/trureturing`, `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` for `208425` -> `0`.
   - `Varun-Dudipala/sun-conjectures-lean/contents/SunConjectures/A208425/Solution.lean` inspected directly -> proves `theorem conjecture_3` (`p % 3 = 2`), NOT `conjecture_2` (`p % 3 = 1`).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath` -> `0` hits for `208425`.
3. **Live OEIS, arXiv & Zenodo API:**
   - `https://oeis.org/search?q=id:A208425&fmt=json` -> revision `60` (`2025-11-05T15:22:21-05:00`), unchanged.
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list ...,2003.09810,2012.05121` -> `2003.09810v4` (Mao, *JCTA* 2021) and `2012.05121v3` (Pan–Sun, *FCNT* 2026) unchanged; neither settles `conjecture_2`.
   - `https://zenodo.org/api/records?q=A208425&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
