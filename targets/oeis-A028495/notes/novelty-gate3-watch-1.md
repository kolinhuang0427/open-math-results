# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A028495/`

- **Checked (UTC):** `2026-11-27T10:57:22Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A028495` McEachen (Feb 11 2026) asymptotic ratio conjectures remain marked `Conjectures:` with no prior proof found.
- **Audit Target:** `targets/oeis-A028495/AUDIT.md` (`@audit-3`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A028495" "A160389" "A116425"`):**
   - `0` lines across `0/635` files (`1.11s`).
2. **Zenodo OEIS IDs Index (`grep -nE "A028495|A160389|A116425" watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A028495&fmt=json`):**
   - Revision `162` (unchanged); Bill McEachen (Feb 11 2026) formula still explicitly marked `Conjectures: a(n) ~ A160389 * a(n-1). Also a(n) ~ sqrt(A116425)*a(n-1).`. No proof comment added.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A028495%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A028495"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A028495" "McEachen" OR "A160389" OR "A116425" conjecture proof` — zero prior proof for OEIS `A028495` ratio conjectures.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
