# Gate 2 Novelty Receipt — `iverson-2506.20778-conjPaley`

- **UTC Time:** 2026-11-27T06:36:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 18 (`2026-11-27T06:22:29Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2506.20778 Iverson Mixon Paley ...` -> `0` prior-solution hits for `2506.20778` / `conj:Paley` (`rh-lab-public` / `eliottcassidy2000` / `s66lem` Paley hits are unrelated graph problems).
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `2506.20778` / `conj:Paley` in `the-omega-institute/trureturing` (`#16342` Greaves–Iverson–Jasper–Mixon `2012.13642`, unrelated), `1337isnot1337/solved-conjectures` (`0`), `facebookresearch/atlas-lean` (`0`).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform` (`CubicPaleyGraph*.lean` is unrelated cubic Paley achromatic numbers), `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` hits for `2506.20778` / `conj:Paley`.
3. **Live arXiv & Zenodo API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2506.20778,2602.21895` -> `2506.20778v1` sole/latest version.
   - `https://zenodo.org/api/records?q=2506.20778&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
