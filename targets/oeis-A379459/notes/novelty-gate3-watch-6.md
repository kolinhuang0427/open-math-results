# Gate 3 (<1h) Live Novelty Receipt (`watch-6`) — `targets/oeis-A379459/` (Rescoped)

- **Checked UTC:** `2026-11-27T11:52:04Z`–`2026-11-27T11:52:25Z`
- **Target Scope:** Strictly **`A379459(n, 0) = A006351(n + 2)`** ($n \ge 0$, equivalently `A006351(n) = A379459(n - 2, 0)` for $n > 1$), per `TARGET.md` Scope Note (`#1349`, `AUDIT.md` §6). Companion identity `A379460(n, 0) = A006351(n + 1)` is explicitly attributed as prior-settled (`insorrowmeow/oeis-sequence-proofs` `62bc090`, `2026-11-27T11:08:09Z`, `proofs/research-batch-09/YokeRows.{md,lean}`) and is NOT claimed.
- **Audit Status:** `@audit-2` re-audit **PASS** (`AUDIT.md` §6, `#1353`, `check-check-2.py` zero-float PASS).
- **Verdict:** **OPEN / CLEAR FOR GATE 5 REPORTING**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `689` Sweep 6 snapshot files):**
   - `A379459` -> **`0` hits** (`0/689`).
   - `A006351` -> `1` file (`watch/snapshots/discovered/insorrowmeow__oeis-sequence-proofs.json` for `YokeRows.{md,lean}`). Direct inspection of `proofs/research-batch-09/YokeRows.md` (`62bc090`, `2026-11-27T11:08:09Z`, latest commit confirmed via `gh api repos/insorrowmeow/oeis-sequence-proofs/commits?per_page=3`) confirms it proves ONLY `A379460(n, 0) = A006351(n + 1)` (initial row $R(0, k) = 1$, MO `481674`) and makes zero mention or claim regarding `A379459(n, 0) = A006351(n + 2)` ($A(0, k) = 2(k+1)!$).
2. **Official OEIS Mirror (`oeis/oeisdata` `main`):**
   - `seq/A379/A379459.seq` (`#4 Jan 03 2025`): `%F Conjecture: A(n,0) = A006351(n+2).` — still an unproved conjecture.
   - `seq/A006/A006351.seq` (`M1885 #195 Oct 30 2026`): `%F Conjecture: a(n) = A379459(n-2,0) = A379460(n-1,0) for n > 1 with a(1) = 1. - _Mikhail Kurkov_, Jan 16 2025` — `A379459` half still open.
3. **GitHub Live Search (`gh` CLI):**
   - `gh search code "A379459"` -> 10 unrelated metadata/hex/timestamp substring files, `0` math proofs.
   - `gh search code '"A379459(n-2,0)"'` -> `[]` (`0` hits).
   - `gh search code '"2*(k+1)!*Sum_{j=0..k}"'` -> `[]` (`0` hits).
   - `gh search issues "A379459"` -> solely `the-omega-institute/trureturing#27785` (`state: open` preregistration).
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` (filtered for `379459|006351|kurkov|yoke`) -> lists `Kurkov*` D5 modules on unrelated sequences (`A102086`, `A107667`, `A248667`, `A263634`, `A329369`, etc.), `0` hits for `A379459` or `A006351`.
4. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?search_query=all:A379459` -> `0` entries; `all:A006351+AND+all:Kurkov` -> `0` entries.
   - `zenodo.org/api/records?q=A379459` -> `0` hits; `q=A006351+Kurkov` -> 10 unrelated non-math records.
   - `search_web` (`"A379459"`, `mathoverflow.net/questions/481674`) -> returns only OEIS sequence pages and MO `481674` (`A379460`), `0` resolutions of `A379459`.

## Coverage Limits

- Unindexed private repositories, non-English/paywalled journals not scraped by arXiv/Zenodo/GitHub/web search, and MathOverflow answers without HTML full-text indexing remain outside live query visibility; all checked public sources confirm `A379459(n, 0) = A006351(n + 2)` remains open.
