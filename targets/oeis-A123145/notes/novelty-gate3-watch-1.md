# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A123145/`

- **Checked (UTC):** `2026-11-27T10:57:22Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A123145` Gladkovskii (Nov 26 2012) 5-step continued fraction EGF conjecture remains marked `Conjecture:` with no prior proof found.
- **Audit Target:** `targets/oeis-A123145/AUDIT.md` (`@audit-2`, re-audit `PASS` after `#897` patches); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A123145"`):**
   - `0` lines across `0/635` files (`1.16s`).
2. **Zenodo OEIS IDs Index (`grep -nE "A123145|..." watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A123145&fmt=json`):**
   - Revision `31` (unchanged); Sergei N. Gladkovskii (Nov 26 2012) formula still explicitly marked `Conjecture: E.g.f.: E(x)=d(G(0))/dx where G(k) = 1 + x/(4*k+1 - x*(4*k+1)/(1 + x - x/(1 + x - x/(x + 1/G(k+1) ))))...`. No proof comment added.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A123145%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs/repos "A123145"`):**
   - `0` issues, `0` PRs, `0` repos.
6. **Web Search (`search_web`):**
   - `"A123145" "Gladkovskii" conjecture proof OR continued fraction` — finds OEIS `A123145` definition and unrelated Gladkovskii sequence proofs (e.g. `A097814`), zero prior proof for `A123145`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
