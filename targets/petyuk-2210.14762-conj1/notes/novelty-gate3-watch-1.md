# Gate 3 Novelty Receipt — `petyuk-2210.14762-conj1`

- **UTC Time:** 2026-11-27T04:10:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 14 (`2026-11-27T03:21:32Z`) `watch/snapshots/1337-solved-conjectures/` & `watch/snapshots/**` -> `0` hits on Petyuk Conjecture 1.
2. **Live competing repos (`gh api`, read-only):**
   - Issue searches in `the-omega-institute/trureturing` (`"2210.14762"`, `"Petyuk"`), `1337isnot1337/solved-conjectures`, `facebookresearch/atlas-lean` -> `0`.
   - Full file trees of `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `trureturing-tools`, `DomTheDeveloper/open-math-agents`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath` -> `0` hits for `2210.14762` / `petyuk` (`atlas-lean` `DeBruijn` files are lambda calculus / bioinformatics only).
3. **Live arXiv & Zenodo API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list ...,2210.14762,...` -> `2210.14762v2` sole/latest version.
   - `https://zenodo.org/api/records?q=2210.14762&size=5` -> `total: 0`.

## Note on Classical Prior Art

- `AUDIT.md` (supported by `notes/audit-helper-petyuk.md`) records that Knisley–Nigussie–Pór (*JCMCC* 73, 2010) proved $\chi(G(3,4,3))=\chi(S(4,3))=3$, while no paper, preprint, or competing repository connected this to word-representability or resolved Petyuk Conjecture 1.

## What Was Not Covered

- Closed-access venues and private repositories; `atlas-lean` & `CrocSwap` root trees were `truncated=True`, checked additionally via `search/issues`.
