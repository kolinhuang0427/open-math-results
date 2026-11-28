# Gate 2 Novelty Receipt (`watch-6`) — `targets/kern-2611.32927-gcs-dichotomy/`

- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *Algorithms and Complexity of Connectivity Switching in Graphs*, `arXiv:2611.32927v1` (`2026-11-24`, full version of LATIN 2026), Section 4 (`sections/gcon.tex` L19–22, L116): whether `Global-Con Switching` (`GCS`) restricted to switch family $\Pi$ is in $\mathsf{P}$ iff all switches in $\Pi$ are matroid switches and $\mathsf{NP}$-complete otherwise (**DISPROVED** via 3 non-matroid families in $\mathsf{P}$).
- **Checked UTC:** `2026-11-27T21:03:32Z` – `2026-11-27T21:04:14Z`
- **Verdict:** **PASS — OPEN** (no prior disproof or resolution of the Section 4 `GCS` matroid-switch dichotomy conjecture found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `854` files across `935` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32927" "kern-2611.32927" "Global-Con" "Connectivity Switching" "matroid switch" --max-per-file 0 --max-total 30` -> `18` lines across `7/854` files: only `watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32927v1` itself and unrelated `"global-con*"` substring paths (`0` hits on `GCS` / `Connectivity Switching` / `matroid switch`).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:03:36Z`–`21:03:51Z`):**
   - `gh search code '"2611.32927"'` -> `rainwangphy/TCSScholar` (`site/daily/2026-11-24.json` daily arXiv paper index only).
   - `gh search code '"kern-2611.32927"'`, `gh search code '"Graph Connectivity Switch"'`, `gh search code '"matroid" "dichotomy" "switch"'`, and `repo:the-omega-institute/trureturing 2611.32927` -> `0` hits on all four.
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:03:36Z`–`21:04:14Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2611.32927` / `connectivity switch` (`matroid` -> unrelated `TR26-099` NC linear matroid intersection; `kern` -> unrelated Schur multiplier kernel); `search_web domain:eccc.weizmann.ac.il` clear.
   - `https://export.arxiv.org/api/query?id_list=2611.32927` -> `2611.32927v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2611.32927`, `q=Graph Connectivity Switch`, `q=matroid switch` -> `total=0`), `papex.org` (`20` records, checked `21:01Z` -> `0`), `Zenodo` (`0`), `Crossref` (`0` matches for Kern–Firbas–Sorge `2611.32927` / LATIN 2026), `search_web` returns only `arXiv:2611.32927` / LATIN 2026 paper itself.

## Coverage Limits

- Unauthenticated OpenAlex returned `HTTP 429` at `21:03Z` (cross-checked via arXiv, ECCC, Crossref, Zenodo, and `search_web`); private/unindexed repositories and paywalled proceedings remain outside public reach; Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
