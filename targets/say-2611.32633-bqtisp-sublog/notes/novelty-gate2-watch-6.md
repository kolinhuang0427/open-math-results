# Gate 2 Novelty Receipt (`watch-6`) — `targets/say-2611.32633-bqtisp-sublog/`

- **Target:** A. C. Cem Say, *Lower space bounds for polynomial-time quantum computation*, `arXiv:2611.32633v1` (`2026-11-24`), Section 6 (*Concluding remarks*, `main.tex` L1924–1928): whether the $\mathsf{BQTISP}(n^{O(1)}, o(s(n))) \subsetneq \mathsf{BQTISP}(n^{O(1)}, O(s(n)))$ sublogarithmic space hierarchy extends beyond $s_i(n) = \Theta(\log n / (\log\log n)^i)$ to general space functions $s(n) \in \omega(\log\log n) \cap o(\log n)$ (**YES** for every monotone, doubling-smooth, log-constructible $s(n) \in \omega(\log\log n) \cap o(\log n)$).
- **Checked UTC:** `2026-11-27T21:33:12Z` – `2026-11-27T21:33:42Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of the Section 6 general sublogarithmic $\mathsf{BQTISP}$ hierarchy question found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `855` files across `936` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.32633" "say-2611.32633" "BQTISP" "BPTISP" "Cem Say" "quantum space hierarchy" --max-per-file 0 --max-total 30` -> `8` lines across `3/855` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.32633v1` itself only).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:33:12Z`–`21:33:30Z`):**
   - `gh search code` for `"2611.32633"`, `"BQTISP"`, `"say-2611.32633"`, `repo:the-omega-institute/trureturing 2611.32633`, and `repo:the-omega-institute/trureturing BQTISP` -> `[]` (`0` hits on all five).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:01Z`–`21:33:35Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2611.32633`, `bqtisp`, `bptisp`, `tisp`, or `cem say`; `search_web domain:eccc.weizmann.ac.il` clear (`0` matches).
   - `https://export.arxiv.org/api/query?id_list=2611.32633` -> `2611.32633v1` sole version (`2026-11-24`).
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2611.32633`, `q=BQTISP` -> `total=0`), `papex.org` (`20` records -> `0`), `Zenodo` (`0`), `Crossref` (`0`), `search_web` returns only `arXiv:2611.32633` itself and Cem Say's earlier `arXiv:2601.16695` (prior work cited in `2611.32633`).

## Coverage Limits

- Unauthenticated OpenAlex returned `HTTP 429` at `21:33Z` (cross-checked via arXiv, ECCC `/year/2026/`, `search_web`, Crossref, and Zenodo); private/unindexed repositories and auth-gated conference preprints remain outside public reach; Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
