# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A101035/`

- **Checked (UTC):** `2026-11-27T11:12:32Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — OEIS `A101035` Irwin (Jul 26 2017) logarithmic g.f. formula remains marked `Conjecture:` with no prior proof found.
- **Audit Target:** `targets/oeis-A101035/AUDIT.md` (`@audit-3`, `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A101035"`):**
   - `0` lines across `0/651` files (`1.59s` combined query).
2. **Zenodo OEIS IDs Indexes (`watch/snapshots/zenodo-23112421-oeis-ids.md`, `watch/snapshots/zenodo-23114921-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A101035&fmt=json`):**
   - Revision `37` (unchanged); Benedict W. J. Irwin (Jul 26 2017) formula still explicitly marked `Conjecture: Logarithmic g.f. Sum_{n>0,k>0} mu(n)*mu(k)*log(1/(1-x^(n*k))).`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A101035%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A101035"`):**
   - `0` issues, `0` PRs.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
