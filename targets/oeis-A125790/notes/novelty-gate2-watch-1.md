# Gate 2 Novelty Receipt — `oeis-A125790`

- **UTC Time:** 2026-11-27T03:36:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A125790 ...` -> `0` hits across `watch/snapshots/**`.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A125790` in `1337isnot1337/solved-conjectures`, `atlas-lean` -> `0`; in `the-omega-institute/trureturing` -> `1` (`#29156`, inspected below).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `VladimirReshetnikov/ProveIt`, `joaquimmj/oeis-conjectures` -> `0` matches for `A125790` / `kurkov`.
3. **Live OEIS & Zenodo API:**
   - `https://oeis.org/search?q=id:A125790&fmt=json` -> revision `47` (`2026-03-22T15:37:03-04:00`), Kurkov's May 03 2025 row g.f. formula still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A125790&size=5` -> `total: 0`.

## Near Misses

- `the-omega-institute/trureturing#29156` (open, `2026-11-11`): preregistration targeting Mikhail Kurkov's *Jan 6, 2026* MathOverflow 506710 column shifted-parity transform conjecture (`\sum T(n,k-1)P(k,m)/2^{nk}`), NOT the *May 3, 2025* row generating function formula targeted here.

## What Was Not Covered

- Closed-access venues and private repositories.
