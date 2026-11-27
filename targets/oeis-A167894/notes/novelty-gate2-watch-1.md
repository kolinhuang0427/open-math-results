# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A167894/`

- **Checked (UTC):** `2026-11-27T10:57:22Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A167894` Gladkovskii (Nov 19 2013) continued fraction formula $Q(0)$ with $Q(k) = 1 + kx - (k+1)x/Q(k+1)$ remains marked `conjecture:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A167894"`):**
   - `0` lines across `0/635` files (`1.38s`).
2. **Zenodo OEIS IDs Index (`grep -nE "...|A167894|..." watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A167894&fmt=json`):**
   - Revision `83`; Sergei N. Gladkovskii (Nov 19 2013) entry still explicitly states `G.f.: conjecture: Q(0), where Q(k) = 1 + k*x - (k+1)*x/Q(k+1).`. (Dec 28 2025 comment by Nour Abouyoussef only mentions `(x*exp(1/x))/Ei(1/x)`, not a proof of the CF conjecture.)
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A167894%22`):**
   - `total: 0`.
5. **GitHub (`gh search issues/prs/repos "A167894"`):**
   - `0` issues, `0` repos; `1` unrelated PR (`adobe/aepsdk-core-ios#989`, git commit hash/build string match).
6. **Web Search (`search_web`):**
   - `"A167894" "Gladkovskii" OR "1 + k*x - (k+1)*x" conjecture proof` — zero prior proofs for OEIS `A167894` continued fraction conjecture.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in OEIS/arXiv/Zenodo/GitHub/web search are outside direct coverage.
