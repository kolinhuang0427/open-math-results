# Gate 2 Novelty Receipt — `oeis-A286044`

- **UTC Time:** 2026-11-27T05:50:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 17 (`2026-11-27T05:29:05Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A286044 Yanev ...` -> `0` hits for `A286044` across prior-solution repos (`linustalacko/small-true-things` has `A040027.yanev`; `trureturing-tools` has `A034448`; `trureturing` has `YanevBinaryReversalPositionIdentity` / `YanevRunCompressionClosedForm`).
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A286044` in `the-omega-institute/trureturing`, `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` -> `0`.
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` hits for `A286044` / `Yanev`.
3. **Live OEIS & Zenodo API:**
   - `https://oeis.org/search?q=id:A286044&fmt=json` -> revision `8` (`2026-02-19T22:02:10-05:00`), Yanev formula still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A286044&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
