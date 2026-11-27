# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A386251/`

- **Checked (UTC):** `2026-11-26T23:13:53Z` – `2026-11-26T23:16:07Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim for OEIS A386251's 3-segment closed walk conjecture)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 333 files including `ai-collections` swept at `23:14:51Z`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A386251 A385525 Hohn 3-segment noncongruent` -> 8 lines across 4/333 files (`mathesis-papers/hohn-a390148-split-prime-shared-divisibility`, unrelated).
   - `watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/` -> 0 occurrences of `A386251`, `A385525`, or `Hohn`.
2. **Live `1337isnot1337/solved-conjectures` (`gh api`):**
   - `search/issues` and `search/code` for `A386251`, `A385525`, `Hohn` -> 0 hits across all 6 queries.
3. **Live `the-omega-institute/trureturing` (`gh api`):**
   - `search/issues?q=A386251+repo:the-omega-institute/trureturing` -> 1 hit (`#27151`, open preregistration for `A386671`).
   - `search/issues?q=A385525+repo:the-omega-institute/trureturing` -> 1 hit (`#27151`).
   - `search/issues?q=Hohn+repo:the-omega-institute/trureturing` -> 6 hits (`#28788`, `#28770`, `#27151`, `#23489`, `#28810`, `#22857`), none covering `A386251`.
   - `search/code?q=A386251+repo:the-omega-institute/trureturing` -> 0 hits.
4. **Live `the-omega-institute/trureturing-tools` (`gh api`):**
   - `search/issues` for `A386251`, `A385525`, `Hohn` -> 0 hits.
   - Full `git/trees` (1,469 files, `pushed_at: 2026-11-26T12:22:58Z`) + direct raw inspection of `SCREENED-OUT.md` (44,971 bytes), `SCREENED-OUT-R52.md` (41,650 bytes), `SCREENED-OUT-R71.md` (19,266 bytes) -> 0 hits for `386251`, `385525`, `hohn`, `3-segment`, `diagonal`.
5. **Live `aliromman/math` (`gh api`):**
   - `search/issues` for `A386251`, `A385525`, `Hohn` -> 0 hits.
   - Full `git/trees/main` (83 files) -> 0 hits for `386251`, `385525`, `hohn`, `diagonal`, `segment`.
6. **Global GitHub Issues (`gh api`):**
   - `search/issues?q=A386251` -> 2 hits (`Unipg-Racing-Team/Provone#2` git SHA `a386251`; `the-omega-institute/trureturing#27151`).
   - `search/issues?q=A385525` -> 1 hit (`the-omega-institute/trureturing#27151`).
   - `search/issues?q="Charles L. Hohn"` -> 5 hits (`trureturing` `#27151`, `#23489`, `#28770`, `#28788`; `trureturing-requests#356` Descartes quartic `A390583`).
7. **Zenodo API:**
   - `https://zenodo.org/api/records?q=...` for `A386251`, `A385525`, `"Charles L. Hohn"`, `"3-segment closed walk"` -> `total=0` for all 4 queries.
8. **Live OEIS JSON (`oeis.org/search?q=id:A386251&fmt=json` and `id:A385525`):**
   - `A386251` remains at `rev=22` (`2025-08-06T00:07:55-04:00`, 65 terms); `A385525` remains at `rev=32` (`2025-08-06T00:08:46-04:00`, 64 terms).

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing#27151` (*"refute Charles L. Hohn's bilateral-symmetry conjecture (OEIS A386671, final COMMENTS clause)"*): Only mentions `A386251` and `A385525` via `A385525`'s cross-reference; it addresses 2D bilateral symmetry in `A386671` and is an open preregistration.
- `trureturing` `#28788`, `#28770`, `#28810`, `#23489`, `trureturing-requests#356`, and `mathesis-papers/hohn-a390148-split-prime-shared-divisibility`: Address Charles L. Hohn's unrelated sequences `A390148` and `A390583`.

## What Was Not Covered
- GitHub `search/code` hit the 10-req/min rate limit on `A385525`/`Hohn` inside `trureturing`, `trureturing-tools`, and `aliromman/math` (mitigated for `trureturing-tools` and `aliromman/math` by direct `git/trees` + `SCREENED-OUT*.md` reads, and for `trureturing` by `A386251` code search = 0 + issue searches); unindexed private repos and paywalled journals not mirrored in Zenodo/OEIS/GitHub.
