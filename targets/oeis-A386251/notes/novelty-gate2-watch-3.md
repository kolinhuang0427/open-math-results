# Gate 2 Novelty Receipt (`watch-3`) — `targets/oeis-A386251/`

- **Checked (UTC):** `2026-11-26T22:38:13Z` – `2026-11-26T22:47:02Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for OEIS A386251's 3-segment closed-walk conjecture)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 277 files including `ai-collections` swept at `22:46:11Z`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A386251 A385525 Hohn 3-segment noncongruent`
   - 8 lines across 4/277 files: only `mathesis-papers/hohn-a390148-split-prime-shared-divisibility` (in `discovered/`).
   - `watch/snapshots/ai-collections/joaquimmj__oeis-conjectures/` -> 0 occurrences of `A386251`, `A385525`, or `Hohn`.
2. **Live `1337isnot1337/solved-conjectures` (`gh api`):**
   - `search/issues?q=A386251+repo:1337isnot1337/solved-conjectures` -> 0
   - `search/issues?q=A385525+repo:1337isnot1337/solved-conjectures` -> 0
   - `search/issues?q=Hohn+repo:1337isnot1337/solved-conjectures` -> 0
3. **Live `the-omega-institute/trureturing` (`gh api`):**
   - `search/issues?q=A386251+repo:the-omega-institute/trureturing` -> 1 hit (`#27151`, open preregistration)
   - `search/issues?q=A385525+repo:the-omega-institute/trureturing` -> 1 hit (`#27151`, open preregistration)
   - `search/issues?q=Hohn+repo:the-omega-institute/trureturing` -> 5 hits (`#28788`, `#28770`, `#27151`, `#23489`, `#28810`)
4. **Live `aliromman/math` (`gh api`):**
   - `search/issues?q=A386251+repo:aliromman/math` -> 0
   - `search/issues?q=A385525+repo:aliromman/math` -> 0
   - `search/issues?q=Hohn+repo:aliromman/math` -> 0
5. **Global GitHub Search (`gh api`):**
   - `search/code?q=A386251` -> 489 substring/hex hash hits (Git commit SHA prefixes / docs hashes; no math hits in top results).
   - `search/code?q="Charles L. Hohn"` -> 27 hits (`archmageirvine/joeis`, `africamonkey/OEIS-Spider`, `trureturing` `PrimitiveSphereRadii.md` for A390583).
   - `search/issues?q=A386251` -> 2 hits (`Unipg-Racing-Team/Provone` git hash `a386251`; `the-omega-institute/trureturing#27151`).
6. **Zenodo API:**
   - `https://zenodo.org/api/records?q=A386251&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=A385525&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=%22Charles+L.+Hohn%22&size=5` -> `total=0`.
7. **Live OEIS JSON (`oeis.org/search?q=id:A386251&fmt=json` and `id:A385525`):**
   - `A386251` remains at revision `22` (`2025-08-06T00:07:55-04:00`), conjecture intact with no proof/disproof links or comments.
   - `A385525` remains at revision `32` (`2025-08-06T00:08:46-04:00`), cross-referencing `A386251` and `A386671`.

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing#27151` (*"Open problem (preregistration): refute Charles L. Hohn's bilateral-symmetry conjecture (OEIS A386671, final COMMENTS clause)"*): Mentions `A386251` and `A385525` only because `A385525` cross-references `A386671`. It concerns 2D bilateral symmetry in `A386671`, not $n$-dimensional 3-segment walks in `A386251`, and is only an open preregistration.
- `the-omega-institute/trureturing` `#28788`, `#28770`, `#23489`, `#28810` and `mathesis-papers/hohn-a390148-split-prime-shared-divisibility`: Concern Charles L. Hohn's unrelated sequences `A390148` and `A390583`.
- `A385525`: Equal-length variant of `A386251` whose conjecture explicitly allows 3- or 4-segment walks for $n \ge 3$, unlike `A386251`'s conjecture that $a(n)$ for all $n \ge 6$ is produced by 3-segment walks.

## What Was Not Covered
- Paywalled journal/proceedings articles not indexed by GitHub/Zenodo/OEIS, and private or unindexed repositories whose default branch does not contain `"Charles L. Hohn"`.
