# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A227543/`

- **Checked (UTC):** `2026-11-27T11:13:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A227543` Mikhail Kurkov (Sep 26 2024) continued-fraction row-recurrence conjecture $b(n) = P(n,n)$ remains marked `Conjecture:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A227543"`):**
   - `0` lines across `0/651` files (`1.65s`).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A227543&fmt=json`):**
   - Revision `113`; Mikhail Kurkov (Sep 26 2024) formula still explicitly marked `Conjecture: b(n) = P(n, n)...`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A227543%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A227543"`):**
   - `1` issue (`the-omega-institute/trureturing#24510` on `A140717`, different conjecture); `3` PRs (`the-omega-institute/trureturing#{6738,6674,6691}` inspected via `gh api`: `#6738` proves Hanna's parity conjecture for `A376527`, referencing `A227543` only as the underlying triangle; `#6674/#6691` are `A222014`). `0` proofs of Kurkov's `b(n)=P(n,n)` conjecture.
6. **Web Search (`search_web`):**
   - `"A227543" "Kurkov" OR "b(n) = P(n, n)" conjecture proof` — no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
