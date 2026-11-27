# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A347063/`

- **Checked (UTC):** `2026-11-27T11:09:49Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A347063` Ianakiev (Oct 01 2024) `$18k+12$` Double Zumkeller conjecture remains open (`"It seems that for k>=1..."`, verified only for `k in [1, 45]`) with no prior counterexample found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A347063"`):**
   - `0` lines across `0/651` files (`0.38s`).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A347063&fmt=json`):**
   - Revision `51`; Ivan N. Ianakiev (Oct 01 2024) comment still explicitly states `"It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]."`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A347063%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A347063"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A347063" "Ianakiev" OR "Double Zumkeller" "18*k+12" OR "18k+12" counterexample OR proof` — no prior counterexample or proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
