# Gate 2 Novelty Receipt — `oeis-A360949`

- **UTC Time:** 2026-11-27T00:12:00Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 8 (`2026-11-26T23:43:05Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A360949 "Paul D. Hanna" ...` -> 0 hits for `A360949`; `dvgyl__oeis-proofs.json` checked directly (`A360949` absent).
2. **Live `mathesis-papers/hanna-self-substitution-integrality`, `trureturing*`, `1337`, `aliromman/math`, `KnowledgeSense/math` (`gh api`, read-only):**
   - `mathesis-papers/hanna-self-substitution-integrality` (all 46 tree paths & all `.md`/`.tex` files) -> 0 occurrences of `A360949`.
   - `search/issues?q=repo:the-omega-institute/trureturing+"A360949"` -> 0; `trureturing-tools` (`SCREENED-OUT*.md`) -> 0.
   - `aliromman/math` (all PRs) -> 0 matches; `KnowledgeSense/math` -> 0 matches.
   - Global `search/issues?q="A360949"` -> 1 unrelated (`madmax983/glossa#1291`).
3. **Live OEIS, arXiv, Zenodo API & web search:**
   - `https://oeis.org/search?q=id:A360949&fmt=json` -> revision `15` (`2023-03-05T12:37:19-05:00`), comment still marked `Conjecture:`.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A360949" OR ...'` -> 0 results.
   - `https://zenodo.org/api/records?q=A360949&size=5` -> `total: 0`.
   - `search_web` for `A360949` -> no prior proof located.

## What Was Not Covered

- Closed-access journals and private repositories.
