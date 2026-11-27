# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A179525/`

- **Checked (UTC):** `2026-11-27T10:59:47Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — OEIS `A179525` Gladkovskii (May 13 2013) 3-step continued fraction $Q(0)$ and Peter Bala (May 16 2017) even-product g.f. $\sum_{n\ge 0}(1+x)^{2n+1}\prod_{k=1}^{2n}(1-(1+x)^k)$ both remain marked `Conjecture.` / `Conjectural g.f.:` with no prior proof found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "A179525"` and `"A158690"`):**
   - `0` lines across `0/635` files for both `A179525` (`0.75s`) and `A158690` (`0.78s`).
2. **Zenodo OEIS IDs Index (`grep -nE "A179525" watch/snapshots/zenodo-23112421-oeis-ids.md`):**
   - `0` matches.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A179525&fmt=json`):**
   - Revision `74`; both Sergei N. Gladkovskii (May 13 2013) CF formula (`... Conjecture.`) and Peter Bala (May 16 2017) `Conjectural g.f.: Sum_{n >= 0} (1 + x)^(2*n+1)*Product_{k = 1..2*n} (1 - (1 + x)^k).` remain conjectural with no proof comments.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A179525%22` & record `23114921`):**
   - `total: 0` for `"A179525"`; noted Zenodo `23114921` (*"Open statements in core entries of the OEIS: proofs, corrections and a refutation"*, `Blanco_Gomez_2026_core_OEIS_EN.pdf` / `verify_core.py`, core entries only).
5. **GitHub (`gh search issues/prs "A179525"`):**
   - `0` issues, `0` PRs.
6. **Web Search (`search_web`):**
   - `"A179525" "Gladkovskii" OR "Bala" OR "Zagier" conjecture proof` — mentions Hwang–Jin asymptotics, Zagier, and Bala's earlier `q^(-n^2)` identity, zero prior proof of Gladkovskii's 2013 CF or Bala's 2017 even-product conjecture.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Full PDF text of Zenodo `23114921` (`core entries`) was not downloaded/indexed here (`A179525` is not a core entry, and Zenodo full-text search returned `0`).
