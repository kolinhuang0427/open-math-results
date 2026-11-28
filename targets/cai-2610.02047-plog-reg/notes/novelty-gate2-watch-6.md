# Gate 2 Novelty Receipt (`watch-6`) — `targets/cai-2610.02047-plog-reg/`

- **Target:** Shaowei Cai and Ziqun Li, *Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth*, `arXiv:2610.02047v1` (`2026-10-01`), Section 8 (`main.tex` L4025–4031): whether every unsatisfiable CNF formula has an FPT-sized regular resolution refutation parameterized by partially log-weighted incidence treewidth $\mathrm{tw}_{\mathrm{plog}}^*(F)$ (**YES** — regular resolution refutation of length $\le k^2(n+m)2^{O(w\log(w+2))}$).
- **Checked UTC:** `2026-11-27T21:30:58Z` – `2026-11-27T21:31:38Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of the Section 8 $\mathrm{tw}_{\mathrm{plog}}^*(F)$ regular-resolution question found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `855` files across `936` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2610.02047" "cai-2610.02047" "tw_plog" "partially log-weighted" "plog-resolution" --max-per-file 0 --max-total 30` -> `# 0 lines across 0/855 files in 0.38s`.
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T21:30:59Z`–`21:31:38Z`):**
   - `gh search code '"2610.02047"'` -> `jtraverso/erdos-81-chordal-clique-partitions` (`PUBLICATION_RECEIPT.json` cites unrelated `aixiv.online/abs/2610.02047`); `gh search code` for `"plog-resolution"`, `"regular resolution" "treewidth" "2610.02047"`, and `repo:the-omega-institute/trureturing 2610.02047` -> `[]` (`0` hits on all three).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T21:01Z`–`21:31:38Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2610.02047`, `plog`, or `regular resolution`; both `treewidth` matches (`TR26-332` Itsykson–Smirnov on Tseitin automatability and parallel arboricity) are unrelated; `search_web domain:eccc.weizmann.ac.il` clear.
   - `https://export.arxiv.org/api/query?id_list=2610.02047` -> `2610.02047v1` sole version (`2026-10-01`).
   - `https://hexagonmath.org/api/v1/works` (`1,683` works; `q=2610.02047`, `q=plog-resolution`, `q=regular resolution treewidth` -> `total=0`), `papex.org` (`20` records -> `0`), `Zenodo` (`0`), `Crossref` (`0` matching Cai–Li `2610.02047`), `search_web` returns only `arXiv:2610.02047` itself.

## Coverage Limits

- At `21:31Z`, unauthenticated OpenAlex returned `HTTP 429` rate limits (cross-checked via arXiv, ECCC `/year/2026/`, `search_web`, Crossref, and Zenodo); private/unindexed repositories and auth-gated conference preprints remain outside public reach; Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
