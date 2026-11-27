# Gate 2 Novelty Receipt (`watch-3`) — `targets/oeis-A360949/`

- **Checked (UTC):** `2026-11-26T23:55:42Z` – `2026-11-27T00:00:00Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Paul D. Hanna's 2023 mod-4 Thue–Morse conjecture on OEIS A360949)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 357 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A360949 A325574 A161674 "Paul D. Hanna"` -> 8 lines across 6/357 files (only unrelated Paul D. Hanna self-substitution / A158110 conjectures).
   - `watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/` -> 0 occurrences of `A360949`, `A325574`, `A161674`, or `Hanna` (the Thue–Morse commit `6f22bef3` covers transform limits / `A285964` only).
2. **Live `1337isnot1337/solved-conjectures` (`gh api`):**
   - `search/issues?q=A360949+repo:1337isnot1337/solved-conjectures` -> 0 hits.
3. **Live `the-omega-institute/trureturing` and `trureturing-tools` (`gh api`):**
   - `search/issues?q=A360949+repo:the-omega-institute/trureturing` -> 0 hits.
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`) -> 0 hits for `360949`, `325574`, `161674`.
4. **Live `aliromman/math` and `KnowledgeSense/math` (`gh api`):**
   - `aliromman/math` (`git/trees` 219 files, 100 issues/PRs) -> 0 hits for `360949`, `161674`, `thue`.
   - `KnowledgeSense/math` (`git/trees` 4,941 files, 0 issues) -> 0 hits for `360949`, `161674`, `thue`.
5. **Global GitHub Issues (`gh api`):**
   - `search/issues?q=A360949` -> 1 unrelated hit (`madmax983/glossa#1291`).
6. **Zenodo API:**
   - `https://zenodo.org/api/records?q=A360949&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=A325574&size=5` -> `total=0`.
7. **Live OEIS JSON (`https://oeis.org/search?q=id:A360949&fmt=json`):**
   - `A360949` remains at `rev=15` (`2023-03-05T12:37:19-05:00`), comment still marked `Conjecture:`.

## Near Misses and Why They Don't Settle the Exact Statement
- `joaquimmj/oeis-conjectures` commit `6f22bef3` ("Thue-Morse transform limits: 19 true, A285964 false (typo)"): Addresses Thue–Morse transform limits, not `A360949` or Hanna's functional equation $1 = \sum_{n\ge 0} (-x/2)^n (A(x)^n + (-1)^n)^n$.
- `mathesis-papers/hanna-self-substitution-integrality` & `formal-conjectures` PR on `A158110` (`arXiv:2607.24832`): Address other Paul D. Hanna conjectures, not `A360949`.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in OEIS, GitHub, or Zenodo.
