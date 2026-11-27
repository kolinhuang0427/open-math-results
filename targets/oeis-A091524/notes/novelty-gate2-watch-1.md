# Gate 2 Novelty Receipt — `oeis-A091524`

- **UTC Time:** 2026-11-27T07:45:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 20 (`2026-11-27T07:37:57Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A091524 A028982 "Graham-Pollak"` -> `0` prior-solution hits across `542` files (`erdosproblems` mentions Erdős #482 / Stoll only).
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A091524` in `the-omega-institute/trureturing`, `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` -> `0`.
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` hits for `A091524`.
3. **Live OEIS & Zenodo API:**
   - `https://oeis.org/search?q=id:A091524&fmt=json` -> revision `27` (`2025-02-16T08:32:52-05:00`), Kurkov's Apr 25 2024 formula still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A091524&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
