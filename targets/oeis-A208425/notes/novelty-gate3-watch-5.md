# Gate 3 Novelty Re-Check — `oeis-A208425` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:40:57Z`
- **Target:** `targets/oeis-A208425/TARGET.md`
- **Verdict:** **PASS** (no public proof of Zhi-Wei Sun's 2016 `conjecture_2`, $p \equiv 1 \pmod 3$, found across live OEIS, OpenAlex citing check, Zenodo, `470` snapshots, or all 15 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"A208425" "208425" ...` -> only `FormalConjectures/OEIS/208425.lean` (open), `Varun-Dudipala/sun-conjectures-lean` (`conjecture_3` $p \equiv 2 \pmod 3$ only), and local sweep files.

2. **GitHub Live Checks (`gh api` trees across 15 competing repos, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, and `Varun-Dudipala/sun-conjectures-lean`: `0` hits on `conjecture_2` (`Varun-Dudipala/sun-conjectures-lean` covers `conjecture_3` only).

3. **Live OEIS JSON (`A208425`), OpenAlex Citing Cache, & Zenodo:**
   - OEIS `A208425` `revision: 60` (`2025-11-05T15:22:21-05:00`) unchanged.
   - `watch/snapshots/arxiv/citing/oeis-A208425.json` (`2026-11-27T01:59:53Z`): `citing_count: 0`, `errors: []`.
   - Zenodo `q=A208425` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- Pan–Sun (`arXiv:2012.05121v3`): Settles `conjecture_1` only; Mao (`arXiv:2003.09810v4`): proves auxiliary binomial sum only; `Varun-Dudipala/sun-conjectures-lean`: settles `conjecture_3` ($p \equiv 2 \pmod 3$) only.
- `CONTESTED.md`: absent from `targets/oeis-A208425/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.
