# Gate 2 Novelty Receipt — `chervov-2509.19162-conj9`

- **UTC Time:** 2026-11-27T04:10:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py 2509.19162 A136184 metacyclic unitriangular` -> `0` hits for `2509.19162` / `A136184` / `metacyclic` (`unitriangular` hits in `1337` / `HessianConjecture4` are unrelated).
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `2509.19162` & `A136184` in `the-omega-institute/trureturing` (`#7556` Conj 2; `#10230`/`#10248` CayleyPy-4 `2603.22195` Conj 16; `#7333` generic lane), `1337isnot1337/solved-conjectures` (`0`), `facebookresearch/atlas-lean` (`0`).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath` -> `0` hits.
3. **Live arXiv & Zenodo API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2509.19162` -> `2509.19162v2` sole/latest version.
   - `https://zenodo.org/api/records?q=2509.19162&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
