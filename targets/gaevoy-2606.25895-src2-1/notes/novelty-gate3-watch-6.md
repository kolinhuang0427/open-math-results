# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/gaevoy-2606.25895-src2-1/`

- **Target:** Nikita Gaevoy, *The Power of Small Symmetries*, `arXiv:2606.25895v1` (`2026-06-24`, MFCS 2026 LIPIcs Vol. 386, Art. 97), Section 2 & Section 6 (`static/open.tex` L3–5): whether $\mathrm{SRC}\text{-}\mathrm{II}[1]$ (`1-SRC-II`) is p-simulated by Resolution or strictly stronger (**YES — exponential separation**, $S_{1\text{-SRC-II}}(\widetilde{\operatorname{Ts}}(G_n,\alpha_n)) = O(n^2)$ vs $S_{\mathrm{Res}}(\widetilde{\operatorname{Ts}}(G_n,\alpha_n)) = 2^{\Omega(n)}$ on bounded-degree expanders, with bounded-depth Frege separation corollary; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T19:49:04Z` – `2026-11-27T19:49:51Z`
- **Verdict:** **PASS — OPEN** (no competing or prior resolution of $\mathrm{SRC}\text{-}\mathrm{II}[1]$ vs $\mathrm{Res}$ found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, `826` indexed files across `907` cataloged repos, post-Sweep 22) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2606.25895" "Gaevoy" "SRC-II" "SRC-2" "1-SRC-II" "short refutations"` -> `# 0 lines across 0/826 files in 1.63s`.
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T19:49:09Z`–`19:49:33Z`):**
   - `gh search code '"2606.25895"'` -> `Lyken17/arXiv-stats` (`info/2026-June/25/paper_info.json`) only.
   - `gh search repos '"2606.25895"'`, `gh search code/repos '"SRC-II" "proof complexity"'`, `gh search code/repos '"Gaevoy" "Tseitin"'` -> `[]` (`0` hits on all five).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T19:48:27Z`–`19:49:51Z`):**
   - `https://eccc.weizmann.ac.il/` (`26` homepage reports, `2026/347` latest) & `/year/2026/` (`692` report links) + `search_web` (`domain:eccc.weizmann.ac.il "Gaevoy" OR "SRC-II" OR "Small Symmetries"`): only `TR26-007` (*New Polynomial-Depth Res($\oplus$) Lower Bounds*) and `TR25-160`, unrelated to `1-SRC-II` vs `Res`.
   - `https://export.arxiv.org/api/query?id_list=2606.25895` -> `http://arxiv.org/api/query` / `2606.25895v1` sole version (`2026-06-24T14:41:30Z`).
   - `https://hexagonmath.org/api/v1/works` (`1,656` total works; `q=2606.25895` -> `0`, `q=SRC-II` -> `0`, `q=Gaevoy` -> `1` work `2610.00328` *"A Counterexample to Affine-Subspace Union Stability under Small Deletions"*, unrelated).
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` hits; Zenodo API -> `count=0`; Crossref MFCS DOI `10.4230/LIPIcs.MFCS.2026.97` -> `404`; `search_web` (`"The Power of Small Symmetries" "Gaevoy" OR "2606.25895" OR "SRC-II"`) returns only Gaevoy's `arXiv:2606.25895` / LIPIcs MFCS 2026 paper.
4. **Independent Verifier Verification (`@audit-2` re-audit `#1939`):**
   - Executed `.venv/bin/python -u targets/gaevoy-2606.25895-src2-1/notes/check-check-2.py` -> exited `0` (`PASS`).

## Coverage Limits

- At `19:49Z`, unauthenticated OpenAlex and Semantic Scholar endpoints returned `HTTP 429` rate limits (15 minutes earlier at `19:34Z` Gate 2, OpenAlex showed `cited_by_count: 0` and OpenCitations `[]`); private/unindexed repositories and auth-gated conference preprints remain outside public reach.
