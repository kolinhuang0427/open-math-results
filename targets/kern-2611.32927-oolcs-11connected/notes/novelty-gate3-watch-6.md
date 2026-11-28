# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-oolcs-11connected/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), **Section 5** (`sections/conclusion.tex` L5): whether `On-Off Local-Con Switching` (`OOLCS`) restricted to $\{1,1\}$-bounded connected switches is solvable in polynomial time (**YES — full `WLCS` and hence `OOLCS` in $\mathsf{P}$ in $O(m^2\log m)$ time** via non-negative weight shifting and minimum-weight perfect matching on $G^*$; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T21:13:49Z` – `2026-11-27T21:14:19Z`
- **Verdict:** **PASS — OPEN** (no competing or prior settlement of the Section 5 `OOLCS` $\{1,1\}$-bounded connected-switch question found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos, post-Sweep 25) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "OOLCS" "On-Off Local-Con" "connected switches" "{1,1}-bounded" --max-per-file 0 --max-total 30` -> `6` lines across `3/854` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself only).
   - `RESULTS.md` scan -> `0` `oolcs` hits (only sibling `targets/kern-2611.32927-wlcs-multipartite/` reported).
2. **Live GitHub (`2026-11-27T21:13:50Z`–`21:14:16Z`):**
   - `gh search code '"2611.32927"'` -> `rainwangphy/TCSScholar` (`site/daily/2026-11-24.json` daily digest only).
   - `gh search code` for `"OOLCS"`, `"On-Off Local-Con"`, `"2611.32927" "OOLCS"`, and `repo:the-omega-institute/trureturing OOLCS` -> `[]` (`0` hits on all four).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:01Z`–`21:14:19Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `oolcs`, `on-off`, `connected switch`, or `2611.32927`.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2611.32927`, `q=OOLCS`, `q=On-Off Local-Con` -> `total=0`), `papex.org` (`20` records, checked Sweep 25 `21:01Z` -> `0`), `Zenodo` (`0`), `Crossref` (`0` LATIN 2026 / Kern–Firbas–Sorge matches), `search_web` returns only Kern–Firbas–Sorge `arXiv:2611.32927` itself.
4. **Independent Verifier Verification (`@audit-1` PASS `#2018`):**
   - Executed `.venv/bin/python -u targets/kern-2611.32927-oolcs-11connected/notes/check-check-1.py` -> exited `0` (`SIZE_WITNESS (n=3, m=2): |V*|=16, |E*|=17`, `WLCS_11CONNECTED_EXACT: checked=40, yes=16, no=24, trap=5`, `PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach).
