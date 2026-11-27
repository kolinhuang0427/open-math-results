# Gate 2 Novelty Receipt (`watch-6`) — `targets/caro-2312.08777-prob7/`

- **Target:** Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster & Christina Zarb, *Flip colouring of graphs*, `arXiv:2312.08777v1` (2023-12-14; *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 6 & Section 7 final Problem: for $t \in \mathbb{N}, t \ge 2$, determine $b(t) = \min\{b : ([t], (b, r))\text{-flip graph exists}\}$ (proved $b(t) = 3$ for all $t \ge 2$, improving $b(t) \le 2^{t+1}-1$).
- **Checked UTC:** `2026-11-27T17:58:14Z` – `2026-11-27T17:59:01Z`
- **Verdict:** **PASS — OPEN** (no prior determination of $b(t)$ for $t \ge 2$ found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `760` files after Sweep 18) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2312.08777 "caro-2312.08777" "Mifsud" "Zarb" "flip colouring" "CayleyTFlip" "PackingTFlip" "s00373-024-02838-w" --max-per-file 0 --max-total 50` -> `# 0 lines across 0/760 files in 0.64s`.
   - `RESULTS.md` regex scan (`2312\.08777|caro|mifsud|lauri|zarb`) -> `[]`.
2. **Live GitHub (`2026-11-27T17:58:14Z`–`17:58:54Z`):**
   - `gh search code '"2312.08777"'`, `gh search code '"s00373-024-02838-w"'`, `gh search code '"Caro" "Lauri" "Mifsud"'`, `gh search code '"flip graph" "b(t)"'`, `gh search repos "2312.08777"`, `gh search issues "2312.08777"`, `gh search prs "2312.08777"` -> `0` hits on all seven (`trureturing` `dev` tree also `0` matches).
3. **Live arXiv, Semantic Scholar, OpenAlex, Crossref, Hexagon, Papex, Zenodo & Web (`2026-11-27T17:58:14Z`–`17:59:01Z`):**
   - `https://export.arxiv.org/api/query?id_list=2312.08777` -> `2312.08777v1` sole arXiv version.
   - OpenAlex `https://doi.org/10.1007/s00373-024-02838-w` (`cited_by_count=4`, `cited_by_api_url` returned `[]`); Crossref (`is-referenced-by-count=0`).
   - Semantic Scholar `arXiv:2312.08777` (`citationCount=5`): `2401.02315` (*Flip colouring of graphs II*), `2403.04401` (*On $(r,c)$-constant, planar and circulant graphs*), `2507.14473` (*Graphs With the Same Edge Count in Each Neighborhood*), `2602.23517` (*Regular $K_3$-regular graphs*), and `2609.37978` (*There is no $8$-regular $K_3$-irregular graph*) — all verified unrelated to $t$-neighbourhood flip graphs / $b(t)$.
   - `https://hexagonmath.org/api/v1/works` (`q=2312.08777`, `q=Zarb`, `q=Mifsud`) -> `total=0`; `papex.org` `0/20`; Zenodo `0` hits; `search_web` returns only Caro et al. (2023/2024) and Mifsud (2024) *Flip colouring of graphs II*.

## Coverage Limits

- Paywalled journal versions beyond arXiv preprints and unindexed private repositories are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.
