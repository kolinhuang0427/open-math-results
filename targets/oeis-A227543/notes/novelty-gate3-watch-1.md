# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A227543/`

- **Checked (UTC):** `2026-11-27T11:16:49Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A227543` Mikhail Kurkov (Sep 26 2024) continued-fraction row-recurrence conjecture $b(n) = P(n, n)$ remains marked `Conjecture:` with no prior proof found.
- **Audit Target:** `targets/oeis-A227543/AUDIT.md` (`@audit-1`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A227543"`):**
   - `0` lines across `0/651` files (`0.45s`).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A227543&fmt=json`):**
   - Revision `113` (unchanged); Mikhail Kurkov (Sep 26 2024) formula still explicitly marked `Conjecture: b(n) = P(n, n)...`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A227543%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues "A227543"`):**
   - Only `the-omega-institute/trureturing#24510` (preregistration for `A140717`, different conjecture); `0` proofs of Kurkov's `A227543` conjecture.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
