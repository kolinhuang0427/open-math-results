# Gate 2 Novelty Receipt — `oeis-A092920`

- **UTC Time:** 2026-11-27T06:26:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 18 (`2026-11-27T06:22:29Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A092920 "strongly monotone" Kurkov` -> `0` hits for `A092920` across `522` files (`joaquimmj`, `mathesis-papers`, `trureturing` cover other Kurkov conjectures only).
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A092920` in `the-omega-institute/trureturing`, `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` -> `0`.
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` hits for `A092920`.
3. **Live OEIS & Zenodo API:**
   - `https://oeis.org/search?q=id:A092920&fmt=json` -> revision `56` (`2026-03-14T12:38:00-04:00`), Kurkov's Apr 24 2023 formula still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A092920&size=5` -> `total: 0`.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
