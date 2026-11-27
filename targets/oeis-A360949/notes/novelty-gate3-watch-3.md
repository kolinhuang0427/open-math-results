# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A360949/`

- **Checked (UTC):** `2026-11-27T02:32:42Z` – `2026-11-27T02:34:54Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Paul D. Hanna's 2023 mod-4 Thue–Morse conjecture on OEIS A360949)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 413 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A360949 A325574 A161674 "Paul D. Hanna"` -> `13` lines across `7/413` files (only unrelated Hanna self-substitution / `A158110` entries; `0` hits for `A360949`).
2. **Live competing GitHub repo trees (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`18,803` files), `aliromman/math` (`747` files), `KnowledgeSense/math` (`4,941` files), `rainwangphy/aftd-platform` (`28,138` files), `valyuAI/research` (`5,110` files), `JENW1N/complete-math-solutions` (`325` files), `trureturing-tools` (`SCREENED-OUT*.md`) -> `0` matches for `360949` or `161674`.
3. **Live GitHub issue searches (`gh api`):**
   - `A360949` in `the-omega-institute/trureturing` and `facebookresearch/atlas-lean` -> `0` hits.
4. **Zenodo API & Live OEIS:**
   - `https://zenodo.org/api/records?q=A360949&size=5` -> `total=0`.
   - `https://oeis.org/search?q=id:A360949&fmt=json` -> `rev=15` (`2023-03-05T12:37:19-05:00`), unchanged.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in OEIS, GitHub, or Zenodo.
