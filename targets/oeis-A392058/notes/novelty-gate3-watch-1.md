# Gate 3 Novelty Receipt — `targets/oeis-A392058/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:51Z`
- **Target:** OEIS `A392058` (`rev. 6`, `2026-01-04`) / `A233335` (`rev. 20`), Mikhail Kurkov's Dec 29 2025 conjecture `A(n,0) = A233335(n+1)`.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`689` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A392058" "A233335"` -> `0` lines across `0/689` files.
2. **External GitHub Proof Repo Check (`insorrowmeow/oeis-sequence-proofs`, `62bc090`):**
   - Inspected all `proofs/research-batch-09/*.md` files directly via `gh api` (including MO-only `DerivativeGrowth.md`): `0` hits for `A392058` or `A233335`.
3. **Official OEIS Mirror (`github.com/oeis/oeisdata`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A392/A392058.seq` -> `%I A392058 #6 Jan 04 2026 20:28:11`, `Conjecture: A(n,0) = A233335(n+1).` open.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A392058" OR all:"A233335"'` -> `0`; Zenodo `q=A392058` & `q=A233335` -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A392058`/`A233335` identifiers are not covered.
