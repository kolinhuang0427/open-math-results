# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-wlcs-multipartite/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), **Section 5** (`sections/conclusion.tex` L5): whether `Weighted Local-Con Switching` (`WLCS`) is solvable in polynomial time for $\{1^\star\}$-bounded complete multipartite switches (**NO — $\mathsf{NP}$-complete** even for $\{1^\star\}$-bounded $K_{2,2}$-shaped switches with $\{0,1\}$ weights and $\lambda = 0$; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T21:11:58Z` – `2026-11-27T21:12:23Z`
- **Verdict:** **PASS — OPEN** (no competing or prior settlement of the Section 5 `WLCS` complete-multipartite question found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos, post-Sweep 25) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "WLCS" "Local-Con Switching" "multipartite switch" "Weighted Local-Con" --max-per-file 0 --max-total 30` -> `6` lines across `3/854` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself only).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:12:00Z`–`21:12:20Z`):**
   - `gh search code '"2611.32927"'` -> `rainwangphy/TCSScholar` (`site/daily/2026-11-24.json` daily digest only).
   - `gh search code` for `"WLCS" "multipartite"`, `"Local-Con Switching"`, and `repo:the-omega-institute/trureturing WLCS` -> `[]` (`0` hits on all three).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:01Z`–`21:12:23Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `wlcs`, `local-con`, `connectivity switch`, or `2611.32927`.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2611.32927`, `q=WLCS`, `q=Local-Con Switching` -> `total=0`), `papex.org` (`20` records, checked Sweep 25 `21:01Z` -> `0`), `Zenodo` (`0`), `Crossref` (`0` matching Kern–Firbas–Sorge `2611.32927` / LATIN 2026), `search_web` returns only Kern–Firbas–Sorge `arXiv:2611.32927` / TU Wien paper page.
4. **Independent Verifier Verification (`@audit-2` PASS `#2009`):**
   - Executed `.venv/bin/python -u targets/kern-2611.32927-wlcs-multipartite/notes/check-check-1.py` -> exited `0` (`REDUCTION_EXACT: checked=120, yes=48, no=72, lam1_false_positives=24` / `PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach).
