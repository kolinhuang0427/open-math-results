# Gate 3 Novelty Receipt — `oeis-A125790`

- **UTC Time:** 2026-11-27T05:35:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 17 (`2026-11-27T05:29:05Z`) `watch/snapshots/1337-solved-conjectures/` & `watch/snapshots/discovered/CATALOG.md` -> `0` hits for `A125790`.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches for `A125790` in `1337isnot1337/solved-conjectures` (`0`), `facebookresearch/atlas-lean` (`0`), and `the-omega-institute/trureturing` (`#29156` open, MO 506710 column parity transform only).
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `joaquimmj/oeis-conjectures` -> `0` matches (`03:22Z–03:29Z`).
3. **Live OEIS & Zenodo API:**
   - `https://oeis.org/search?q=id:A125790&fmt=json` -> revision `47` (`2026-03-22T15:37:03-04:00`), Kurkov's May 03 2025 row g.f. formula still marked `Conjecture:` (`05:21Z`).
   - `https://zenodo.org/api/records?q=A125790&size=5` -> `total: 0` (`05:21Z`).

## Near Misses

- `the-omega-institute/trureturing#29156` (open, `2026-11-11`): preregistration for Kurkov's Jan 6, 2026 MathOverflow 506710 column transform conjecture, NOT the May 3, 2025 row generating function formula.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
