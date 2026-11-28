# Gate 2 Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-wlcs-multipartite/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), Section 6 (`sections/conclusion.tex` L5): whether `Weighted Local-Con Switching` (`WLCS`) is solvable in polynomial time for $\{1^\star\}$-bounded complete multipartite switches (**NO — $\mathsf{NP}$-complete** even for $\{1^\star\}$-bounded $K_{2,2}$-shaped switches with $\{0,1\}$ weights and $\lambda = 0$).
- **Checked UTC:** `2026-11-27T21:04:57Z` – `2026-11-27T21:05:17Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of the Section 6 `WLCS` complete-multipartite question found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "WLCS" "Local-Con Switching" "multipartite switch" "K_{2,2}" --max-per-file 0 --max-total 30` -> `12` lines across `4/854` files: only `watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself and unrelated `K_{2,2}` occurrences in `watch/snapshots/ai-village-graffiti-verification.md`.
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:05:00Z`–`21:05:13Z`):**
   - `gh search code` for `"WLCS" "multipartite"`, `"Local-Con Switching"`, `"2611.32927" "WLCS"`, and `repo:the-omega-institute/trureturing WLCS` -> `[]` (`0` hits on all four; global `"2611.32927"` only hits `rainwangphy/TCSScholar` `2026-11-24.json` daily index).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:03Z`–`21:05:17Z`):**
   - `https://eccc.weizmann.ac.il/year/2026/` (`2026/347` latest): `0` hits for `wlcs`, `local-con`, `multipartite switch`, or `2611.32927`.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=WLCS`, `q=Local-Con Switching` -> `total=0`), `papex.org` (`20` records, checked `21:01Z` -> `0`), `Zenodo` (`0`), `Crossref` (`0` matches for Kern–Firbas–Sorge `2611.32927`), `search_web` returns only Kern–Firbas–Sorge `arXiv:2611.32927` itself.

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach); Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
