# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-gcs-dichotomy/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), **Section 4** (`sections/gcon.tex` L19–22, L116): whether `Global-Con Switching` (`GCS`) restricted to switch family $\Pi$ is in $\mathsf{P}$ whenever all switches in $\Pi$ are matroid switches and $\mathsf{NP}$-complete otherwise (**FALSE** — disproved via 3 explicit non-matroid switch families $\Pi_1,\Pi_2,\Pi_3$ in $\mathsf{P}$; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T21:14:38Z` – `2026-11-27T21:15:03Z`
- **Verdict:** **PASS — OPEN** (no competing or prior disproof of the Section 4 `GCS` matroid-switch dichotomy conjecture found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos, post-Sweep 25) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "kern-2611.32927" "Global-Con" "Connectivity Switching" "matroid switch" --max-per-file 0 --max-total 30` -> `18` lines across `7/854` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself and unrelated `global-con*` substrings only).
   - `RESULTS.md` scan -> `0` `gcs` hits (only sibling `targets/kern-2611.32927-wlcs-multipartite/` reported).
2. **Live GitHub (`2026-11-27T21:14:40Z`–`21:14:59Z`):**
   - `gh search code '"2611.32927"'` -> `rainwangphy/TCSScholar` (`site/daily/2026-11-24.json` daily digest only).
   - `gh search code` for `"Graph Connectivity Switch"`, `"matroid" "dichotomy" "switch"`, and `repo:the-omega-institute/trureturing 2611.32927` -> `[]` (`0` hits on all three).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:01Z`–`21:15:03Z`):**
   - `https://eccc.weizmann.ac.il/year/2026/` (`2026/347` latest): `0` hits for `connectivity switch`, `global-con`, or `2611.32927`.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2611.32927`, `q=Graph Connectivity Switch`, `q=matroid switch` -> `total=0`), `papex.org` (`20` records, checked Sweep 25 `21:01Z` -> `0`), `Zenodo` (`0`), `search_web` returns only Kern–Firbas–Sorge `arXiv:2611.32927` itself.
4. **Independent Verifier Verification (`@audit-1` re-audit PASS `#2019`):**
   - Executed `.venv/bin/python -u targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py` -> exited `0` (`Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS`, `PASS`).

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach).
