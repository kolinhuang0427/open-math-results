# Gate 3 Novelty Receipt (`watch-3`) — `targets/oeis-A061313/`

- **Checked (UTC):** `2026-11-27T00:24:18Z` – `2026-11-27T00:25:29Z`
- **Verdict:** **PASS** (no prior proof, disproof, or active claim found for Andrei Zabolotskii's 2020 Hirzebruch continued-fraction conjecture on OEIS A061313)

## Sources Checked
1. **Local watch snapshots (`watch/snapshots/**`, 357 files including `ai-collections`, `1337-solved-conjectures`, `discovered`, `openai-math`, `formal`, `arxiv`):**
   - `.venv/bin/python tools/novelty_grep.py A061313 Zabolotskii Stern-Brocot` -> `0` lines across `0/357` files.
2. **Live `1337isnot1337/solved-conjectures`, `aliromman/math`, `KnowledgeSense/math` (`gh api`):**
   - `1337isnot1337/solved-conjectures` (`git/trees` 18,775 files, `pushed=2026-11-27T00:22:31Z`) -> `0` path hits.
   - `aliromman/math` (`git/trees` 331 files, `pushed=2026-11-27T00:24:23Z` + `search/issues`) -> `0` hits.
   - `KnowledgeSense/math` (`git/trees` 4,941 files) -> `0` hits.
3. **Live `the-omega-institute/trureturing` and `trureturing-tools` (`gh api`):**
   - `search/issues?q=A061313+repo:the-omega-institute/trureturing` -> `0` hits.
   - `search/issues?q=Zabolotskii+repo:the-omega-institute/trureturing` -> `6` hits (including `#10337`/`#10392` on `A385672` square-lattice walks; `0` hits for `A061313`).
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`) -> `0` hits for `061313`, `a61313`, `zabolotskii`.
4. **Global GitHub Issues (`gh api`):**
   - `search/issues?q=A061313` -> `0` hits.
5. **Zenodo API:**
   - `https://zenodo.org/api/records?q=A061313&size=5` -> `total=0`.
   - `https://zenodo.org/api/records?q=%22Zabolotskii%22&size=5` -> 3 unrelated hits (`20634736`, `5123744`, `24161984`).
6. **Live OEIS JSON (`https://oeis.org/search?q=id:A061313&fmt=json`):**
   - `A061313` remains at `rev=58` (`2026-11-01T16:49:49-05:00`), unchanged.

## Near Misses and Why They Don't Settle the Exact Statement
- `the-omega-institute/trureturing` `#10337` / `#10392`: Settle Zabolotskii's 2025 conjecture on `A385672` (square-lattice walks), unrelated to `A061313` or Hirzebruch continued fractions.

## What Was Not Covered
- Unindexed private repositories and closed-access publications not mirrored in OEIS, GitHub, or Zenodo.
