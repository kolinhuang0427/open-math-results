# Gate 3 Novelty Re-Check — `oeis-A396911` (watch-5)

- **UTC Timestamp:** `2026-11-27T02:44:00Z`
- **Target:** `targets/oeis-A396911/TARGET.md`
- **Verdict:** **PASS** (no public proof of Sean A. Irvine's 2026 conjecture $a(n) \le \frac{3}{2} n^2$ on OEIS `A396911` found across live OEIS, arXiv, Zenodo, `413` snapshots, or all 10 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `413` files incl. `trureturing*`, `aliromman`, `KnowledgeSense`):**
   - `"A396911" "396911" "phyllotaxis" "Sean A. Irvine"` -> `0 lines across 0/413 files`.

2. **GitHub Live Checks (`gh api repos/.../git/trees/HEAD?recursive=1`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, and `DomTheDeveloper/ProofPlaygrond` -> `0` matches except `atlas-lean`'s `IrvineConjecture.lean`, inspected directly (`WantedExt/Combinatorics/Words/IrvineConjectureWanted.lean`) and confirmed to be Shallit (2024) on Gutkovskiy's sequence / Kimberling's word, unrelated to `A396911`.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A396911&fmt=json`), arXiv, & Zenodo:**
   - OEIS `A396911` `revision: 48` (`2026-06-22T17:16:16-04:00`) unchanged.
   - `tools/arxiv_fetch.py` `all:A396911` (`use_cache=False`) -> `0` entries; Zenodo `q=A396911` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `facebookresearch/atlas-lean` (`IrvineConjecture.lean`): Formalizes Shallit (2024) on Gutkovskiy's sequence, unrelated to `A396911`.
- `archmageirvine/joeis` (`A396911.java`): Sequence generator commenting empirical `a(n) <= phi * n^2`, no proof.
- `CONTESTED.md`: absent from `targets/oeis-A396911/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.
