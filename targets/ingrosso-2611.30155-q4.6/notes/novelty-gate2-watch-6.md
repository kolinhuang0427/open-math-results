# Gate 2 Novelty Receipt (`watch-6`) — `targets/ingrosso-2611.30155-q4.6/`

- **Target:** E. Ingrosso, M. Trombetti, and A. Zitouni, `arXiv:2611.30155v1` (*"Groups with dual classes of subgroups"*, dated `2026-11-23`), Section 4, **Question 4.6**: smallest possible subnormal defect in Theorem 4.5 (`\label{sip}`, locally graded group whose subgroups are pronormal or contained in $N_{\mathrm{pro}}(G)$ — proved sharp defect $= 2$).
- **Checked UTC:** `2026-11-27T16:33:53Z` – `2026-11-27T16:34:22Z`
- **Verdict:** **PASS — OPEN** (no prior proof or settlement of Question 4.6 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `742` files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.30155 "ingrosso-2611.30155" "Ingrosso" "pro-normal" "pronormal" "Question 4.6" --max-per-file 0 --max-total 30` -> `12` lines across `5/742` files: `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` announcing `2611.30155v1`, `facebookresearch__atlas-lean` (`Kourovka` Hall/pronormal problems), and `eliottcassidy2000__math` (`THM-4728`, checked directly via `gh api`: unrelated odd-order permutation group census `C15`/`F21`).
   - `0` hits in `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `hwzw-algebra-number-theory-drafts.md`, `insorrowmeow-oeis-ids.md`.
2. **Live GitHub (`2026-11-27T16:33Z`–`16:34Z`):**
   - `gh search code '"2611.30155"'`, `gh search repos "2611.30155"`, `gh search issues "2611.30155"`, `gh search prs "2611.30155"`, `gh search code '"Ingrosso" "2611.30155"'`, `gh search code '"pro-norm" "pronormal"'`, `gh search code '"Trombetti" "pronormal"'` -> `[]` on all seven.
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` -> `0` paths matching `2611`, `30155`, `ingrosso`, `pronormal`, or `pro-normal`.
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:33Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.30155` -> `2611.30155v1` (`published 2026-11-23T07:03:10Z`, `updated 2026-11-23T07:03:10Z`) sole version.
   - `https://zenodo.org/api/records?q=2611.30155` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works` (`q=Ingrosso`, `q=2611.30155`, `q=pronormal`) -> `0` hits on all three.
   - `search_web` -> returns only `arXiv:2611.30155` (*Groups with dual classes of subgroups*); no settlement of Question 4.6 found.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs were not queried.
- Independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.
