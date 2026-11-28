# Gate 2 Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-oolcs-11connected/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), `sections/conclusion.tex` L5 (Conclusion): whether `On-Off Local-Con Switching` (`OOLCS`) restricted to $\{1,1\}$-bounded connected switches is solvable in polynomial time (**YES — `WLCS` and hence `OOLCS` are in $\mathsf{P}$ in $O(m^2\log m)$ time** via non-negative weight shifting and minimum-weight perfect matching in an auxiliary class-transition graph).
- **Checked UTC:** `2026-11-27T21:07:35Z` – `2026-11-27T21:07:54Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of the `OOLCS` $\{1,1\}$-bounded connected-switch question found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "OOLCS" "On-Off Local-Con" "connected switches" "{1,1}-bounded" --max-per-file 0 --max-total 30` -> `6` lines across `3/854` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself only).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:07:37Z`–`21:07:50Z`):**
   - `gh search code` for `"OOLCS"`, `"On-Off Local-Con"`, `"2611.32927" "OOLCS"`, and `repo:the-omega-institute/trureturing OOLCS` -> `[]` (`0` hits on all four; global `"2611.32927"` only hits `rainwangphy/TCSScholar` `2026-11-24.json`).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:04Z`–`21:07:54Z`):**
   - `https://eccc.weizmann.ac.il/year/2026/` (`2026/347` latest): `0` hits for `oolcs`, `on-off`, `connected switch`, or `2611.32927`.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=OOLCS`, `q=On-Off Local-Con` -> `total=0`), `papex.org` (`20`), `Zenodo` (`0`), `Crossref` (`0`), `search_web` returns only Kern–Firbas–Sorge `arXiv:2611.32927` itself.

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach); Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
