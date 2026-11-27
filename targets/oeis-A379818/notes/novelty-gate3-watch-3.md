# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A379818/`

- **Checked (UTC):** `2026-11-27T00:24:18Z` – `2026-11-27T00:25:29Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Mikhail Kurkov's 2025/2026 binomial formula conjecture on OEIS A379818)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 357 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A379818 A025480 Kurkov` -> 28 lines across 10/357 files (only Kurkov's unrelated sequences `A006068`, `A340991`, binary Stirling row edge; `0` hits for `A379818`).
2. **Live `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math` (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`git/trees` 18,775 files, `pushed=2026-11-27T00:22:31Z`) -> `0` path hits for `379818`/`kurkov`.
   - `aliromman/math` (`git/trees` 331 files, `pushed=2026-11-27T00:24:23Z` + `search/issues`) -> `0` hits.
   - `KnowledgeSense/math` (`git/trees` 4,941 files) -> `0` hits.
3. **Live `the-omega-institute/trureturing` and `trureturing-tools` (`gh api`):**
   - `search/issues?q=A379818+repo:the-omega-institute/trureturing` -> `0` hits.
   - `search/issues?q=Kurkov+repo:the-omega-institute/trureturing` -> `87` hits (targeting `A358612`, `A329369`, `A341392`, etc.; `0` hits for `A379818`).
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`) -> only `A057032`, `0` hits for `A379818`.
4. **Global GitHub Issues (`gh api`):**
   - `search/issues?q=A379818` -> 1 unrelated software hit (`getsentry/sentry#61193`).
5. **Zenodo API:**
   - `https://zenodo.org/api/records?q=A379818&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=%22Mikhail+Kurkov%22&size=5` -> `total=0`.
6. **Live OEIS JSON (`https://oeis.org/search?q=id:A379818&fmt=json`):**
   - `A379818` remains at `rev=8` (`2026-02-26T16:45:49-05:00`), unchanged.

## Near Misses and Why They Don't Settle the Exact Statement
- `joaquimmj/oeis-conjectures` (`A006068`), `mathesis-papers/kurkov-binary-stirling-row-edge`, `mathesis-papers/kurkov-a340991-convolution-row-recursion`, `trureturing` (`A358612`, `A329369`, `A057032`): All address different OEIS sequences or conjectures by Mikhail Kurkov, not `A379818`.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in OEIS, GitHub, or Zenodo.
