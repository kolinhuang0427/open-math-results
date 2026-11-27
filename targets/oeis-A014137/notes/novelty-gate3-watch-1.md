# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A014137/`

- **Checked (UTC):** `2026-11-27T10:59:13Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A014137` Gladkovskii (May 14 2013) continued fraction formula $Q(0)/(1-x)$ remains marked `(conjecture)` with no prior proof found.
- **Audit Target:** `targets/oeis-A014137/AUDIT.md` (`@audit-3`, re-audit `PASS`, label `"written proof, internally audited"`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A014137"`):**
   - `0` lines across `0/635` files (`1.16s`).
2. **Zenodo OEIS IDs Index (`grep -nE "A014137" watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A014137&fmt=json`):**
   - Revision `180` (unchanged); Sergei N. Gladkovskii (May 14 2013) formula still explicitly marked `G.f. (conjecture): Q(0)/(1-x), where Q(k)= 1 + (4*k + 1)*x/(k + 1 - 2*x*(k + 1)*(4*k + 3)/(2*x*(4*k + 3) + (2*k + 3)/Q(k+1)));`. (Peter J. Taylor's Mar 23 2015 comment refers solely to Mathar's linear recurrence, not Gladkovskii's continued fraction.)
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A014137%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs "A014137"`):**
   - `0` issues, `1` unrelated PR (`buryads/orshuulagsha-ui#12`, commit/ID substring match).
6. **Web Search (`search_web`):**
   - `"A014137" "Gladkovskii" "Q(0)/(1-x)" conjecture proof` — zero prior proof for Gladkovskii's continued fraction conjecture.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
