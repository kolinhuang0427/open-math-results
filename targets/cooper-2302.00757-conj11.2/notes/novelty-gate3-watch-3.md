# Gate 3 Novelty Receipt (`watch-3`) — `targets/cooper-2302.00757-conj11.2/`

- **Checked (UTC):** `2026-11-27T02:32:42Z` – `2026-11-27T02:34:54Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Conjecture 11.2 of Cooper `arXiv:2302.00757v2`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 413 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py 2302.00757 T_11 Cooper A284756` -> `65` lines across `31/413` files (only unrelated `Cooper–Hollars` `2607.15486` and `rbajaj5/a183068-supercongruence`, which explicitly notes `2302.00757` Conj 11.2 is unproved).
2. **Live competing GitHub repo trees (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`18,803` files), `aliromman/math` (`747` files), `KnowledgeSense/math` (`4,941` files — only unrelated `T_11.csv` in `Maximal-Central-Sections-of-Three-Dimensional-lp-Balls`), `rainwangphy/aftd-platform` (`28,138` files), `valyuAI/research` (`5,110` files), `JENW1N/complete-math-solutions` (`325` files), `trureturing-tools` (`SCREENED-OUT*.md`) -> `0` matches for `2302.00757`, `cooper`, `284756`.
3. **Live GitHub issue searches (`gh api`):**
   - `2302.00757` in `the-omega-institute/trureturing` and `facebookresearch/atlas-lean` -> `0` hits.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=2302.00757&size=5` -> `total=0`.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in GitHub or Zenodo.
