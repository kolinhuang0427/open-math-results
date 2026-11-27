# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A188458/`

- **Checked (UTC):** `2026-11-27T10:57:22Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A188458` Gladkovskii (Nov 12 2013) continued fraction formula $T(0)/(1-x)$ remains marked `conjecture` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A188458"`):**
   - `0` lines across `0/635` files (`1.53s`).
2. **Zenodo OEIS IDs Index (`grep -nE "...|A188458|..." watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A188458&fmt=json`):**
   - Revision `54`; Sergei N. Gladkovskii (Nov 12 2013) formula still explicitly marked `G.f.: conjecture T(0)/(1-x), where T(k) = 1 - 4*x^2*(k+1)^2/(4*x^2*(k+1)^2 + (1-x)^2/T(k+1) );`. No proof comment found.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A188458%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs/repos "A188458"`):**
   - `0` issues, `0` PRs, `0` repos.
6. **Web Search (`search_web`):**
   - `"A188458" "Gladkovskii" OR "exp(x)/cosh(2*x)" conjecture proof` — finds only OEIS `A188458` / `A212435` definitions, zero prior proofs of the Nov 12 2013 CF conjecture.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
