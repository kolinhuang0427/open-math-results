# Gate 3 Novelty Receipt — `targets/oeis-A379459/` (Rescoped)

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:52Z`
- **Target:** OEIS `A379459` (`rev. 4`, `2025-01-03`) / `A006351` (`rev. 195`) — strictly rescoped to Mikhail Kurkov's Dec 23 2024 conjecture `A379459(n, 0) = A006351(n + 2)` ($n \ge 0$, `A006351(n) = A379459(n-2, 0)` for $n > 1$), crediting `insorrowmeow/oeis-sequence-proofs` (`62bc090`, `YokeRows.{md,lean}`) as prior settlement of `A379460(n, 0) = A006351(n + 1)`.
- **Verdict:** **PASS** (rescoped open conjecture `A379459(n, 0) = A006351(n + 2)` has `0` competing solutions)

## Exact Queries & Results
1. **Local Snapshot Sweep (`689` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, `insorrowmeow/oeis-sequence-proofs` `62bc090`, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A379459" "481674"` (`11:52Z`) -> `1` line across `1/689` files: `insorrowmeow__oeis-sequence-proofs.json` (`YokeRows.md` / MO `481674`).
   - Verified `proofs/research-batch-09/YokeRows.md` directly via `gh api`: settles ONLY the all-ones initial row $R(n,0) = a(n+1)$ (`A379460`, excluded from rescoped scope); `0` matches for `A379459` ($A(0,k) = 2(k+1)!$).
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:52Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A379/A379459.seq` -> `%I A379459 #4 Jan 03 2025 02:03:22`, `Conjecture: A(n,0) = A006351(n+2).` open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A379459"'` (`11:52Z`) -> `0`; Zenodo `q=A379459` (`11:52Z`) -> `0`; `gh search issues` -> only `the-omega-institute/trureturing#27785` (open placeholder, `0` comments); `search_web` -> `0` proofs of `A379459`.

## Near-Misses & Coverage Limits
- **Near-misses:** `insorrowmeow/oeis-sequence-proofs` `YokeRows.{md,lean}` settles sibling `A379460` (now excluded from this target); `A217061.md`/`FactorialSweep.lean` settles `A379458`; `trureturing#27785` is an open preregistration with `0` comments.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A379459` identifiers are not covered.
