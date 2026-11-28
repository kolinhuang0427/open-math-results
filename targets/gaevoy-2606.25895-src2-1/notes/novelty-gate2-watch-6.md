# Gate 2 Novelty Receipt (`watch-6`) — `targets/gaevoy-2606.25895-src2-1/`

- **Target:** Nikita Gaevoy, *The Power of Small Symmetries*, `arXiv:2606.25895v1` (`2026-06-24`; MFCS 2026 `10.4230/LIPIcs.MFCS.2026.97`), Section 2 & Section 6 (`static/open.tex` L3–5): whether $\mathrm{SRC}\text{-}\mathrm{II}[1]$ is p-simulated by Resolution or strictly stronger (**YES — exponential separation**, proved via guarded Tseitin $\widetilde{\operatorname{Ts}}(G_n, \alpha_n)$ on bounded-degree expanders).
- **Checked UTC:** `2026-11-27T19:34:15Z` – `2026-11-27T19:34:48Z`
- **Verdict:** **PASS — OPEN** (no prior proof separating or collapsing $\mathrm{SRC}\text{-}\mathrm{II}[1]$ and Resolution found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `811` files across `892` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.25895 "gaevoy-2606.25895" "Gaevoy" "SRC-II" "SRCII" "Substitution Resolution" --max-per-file 0 --max-total 40` -> `# 0 lines across 0/811 files in 1.07s`.
   - `RESULTS.md` scan -> `[]`.
2. **Live GitHub (`2026-11-27T19:34:15Z`–`19:34:32Z`):**
   - `gh search code '"2606.25895"'` -> `Lyken17/arXiv-stats` (`info/2026-June/25/paper_info.json`) only.
   - `gh search code '"gaevoy-2606.25895"'`, `gh search code '"SRC-II" "Resolution"'`, `gh search repos/issues/prs "2606.25895"` -> `0` hits on all five.
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, OpenAlex, Crossref & Web (`2026-11-27T19:34:15Z`–`19:34:48Z`):**
   - `https://eccc.weizmann.ac.il/` & `/year/2026/`: only `TR26-007` (Alekseev–Gaevoy, *New Polynomial-Depth Res($\oplus$) Lower Bounds*, 2 Jan 2026 — unrelated to `SRC-II[1]`).
   - `https://export.arxiv.org/api/query?id_list=2606.25895` -> `2606.25895v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.25895`, `q=SRC-II` -> `total=0`; `q=Gaevoy` -> `1` work `2610.00328` *"A Counterexample to Affine-Subspace Union Stability under Small Deletions"*, unrelated).
   - `papex.org` `0`; Zenodo `0` hits; OpenAlex `0`; Crossref MFCS DOI `404`; `search_web` returns only Gaevoy's `arXiv:2606.25895` preprint.

## Coverage Limits

- Unauthenticated OpenAlex/Zenodo/web checks cover public indexed records only; private/unindexed repositories and auth-gated venues are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.
