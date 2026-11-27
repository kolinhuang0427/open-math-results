# Gate 3 Novelty Receipt (`watch-3`) — `targets/chang-2201.02781-conj2/`

- **Checked (UTC):** `2026-11-27T01:38:15Z` – `2026-11-27T01:42:55Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Chang–Yang–Yin–Yao Conjecture 2 of `arXiv:2201.02781v1`)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 369 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py 2201.02781 fgndi "neighbor full sum" NFSD Keusch` -> `4` lines across `3/369` files (`watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` and `openalex_works_cache.json` + unrelated PGP key substring in `erdos-frontier-atlas`).
2. **Live competing GitHub repository trees (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`18,795` files, `pushed=2026-11-27T01:38:15Z`) -> `0` matches for `2201.02781`, `fgndi`, `nfsd`, `full_sum`, `total_color`, `keusch` (only unrelated `*Neighbors*`/`*Exchange*`).
   - `aliromman/math` (`699` files, `pushed=2026-11-27T01:38:33Z`) -> `0` matches (only unrelated `*Exchange.lean`).
   - `KnowledgeSense/math` (`4,941` files, `pushed=2026-10-14T07:35:52Z`) -> `0` matches (only unrelated `*Neighborhoods*`/`*Exchange*`).
   - `rainwangphy/aftd-platform` (`28,138` files, `pushed=2026-11-27T01:30:07Z`) -> `0` matches (only unrelated game-theory `*Neighbor*`/`*Exchange*`).
   - `valyuAI/research` (`5,110` files, `pushed=2026-10-27T16:11:42Z`) -> `0` matches.
   - `JENW1N/complete-math-solutions` (`325` files, `pushed=2026-10-11T02:27:03Z`) -> `0` matches.
   - `facebookresearch/atlas-lean` (`50,109` files returned in `git/trees` with `truncated=True`) -> `0` matches for `2201.02781`, `fgndi`, `nfsd`, `full_sum`, `total_color`, `keusch` (only unrelated `*123*`).
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`) -> `0` matches.
3. **Live GitHub issue searches (`gh api`):**
   - `2201.02781` in `trureturing`, `atlas-lean`, global -> `0` hits.
   - `fgndi` in `trureturing`, global -> `0` hits.
   - `"neighbor full sum"` in `trureturing`, `atlas-lean` -> `0` (`trureturing#24091` is unrelated `A209723` "neighboring").
   - `Keusch` in `aliromman/math` -> `0` hits.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=2201.02781`, `"neighbor full sum distinguishing"`, `"fgndi"` -> `total=0` for all 3 queries.

## Near Misses / Scope Notes
- No competing repo or Zenodo deposit addresses `fgndi_{\sum}(G) <= 3` or Conjecture 2 of `arXiv:2201.02781v1`.

## What Was Not Covered
- `facebookresearch/atlas-lean` `git/trees` was truncated (`truncated=True` past 50,109 entries), though issue searches on `atlas-lean` for `2201.02781` and `"neighbor full sum"` returned `0`. Unindexed private repos and paywalled journals not mirrored in GitHub/Zenodo.
