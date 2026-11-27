# Gate 2 Novelty Check — `caro-2312.08777-prob7` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:58:11Z`–`2026-11-27T17:58:30Z`
- **Target:** `targets/caro-2312.08777-prob7/` — Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *"Flip colouring of graphs"* (`arXiv:2312.08777v1`, `2023-12-14`, *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 7 final Problem ($b(t)$ for $t$-neighbourhood flip graphs)
- **Claimed result:** **EXACT ANSWER** $b(t) = 3$ for all $t \ge 1$ (proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2312.08777" "Lauri" "Mifsud" "Zarb" "b(t)"`):**
   - `0` hits on `2312.08777`, `Mifsud`, or `Zarb` across `760` snapshot files; `Lauri` / `b(t)` hits solely unrelated files (`kyleglsn22-spec` equitable chromatic number, `graffiti` `B(t)` copies of `K_4`, Euler–Maclaurin `B(t)`).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:58:11Z`):**
   - `main` = `bac28f41abbcd6ee4d89659574e0a734a60cdebc` (`2026-11-27T17:56:10Z`, PR `#1078`, Bourin exact input rank) — unrelated.
   - `research` = `c58abfb3bfa4cb7607990f25746de8c59df75de1` (`2026-11-27T17:56:46Z`, independent subdivisions) — unrelated.
3. **GitHub live search & direct inspection (`gh api`):**
   - `gh search prs "2312.08777"` -> `0` hits (`[]`).
   - `gh search issues "2312.08777"` -> `0` hits (`[]`).
   - `gh search code "2312.08777"` -> `xmif1/geng_rc_graphs` (Mifsud's graph generator), `10m-u/open-problems-catalog` (`combinatorics-graph-theory-part-3.md`, inspected via `gh api`: lists no resolution), plus unrelated CSV/JSON numeric collisions.
   - `gh search code "CayleyTFlip"` -> `0` hits (`[]`); `gh search code "neighbourhood flip"` -> `0` flip-graph hits.
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2312.08777`) -> sole version `2312.08777v1` (`2023-12-14T09:54:17Z`).
   - Zenodo API (`q=2312.08777`) -> `0` hits.
   - Crossref (`10.1007/s00373-024-02838-w`) -> `is-referenced-by-count: 0`.
   - Web search -> only Caro–Lauri–Mifsud–Yuster–Zarb (`2023`/`2024`) paper and UM/Malta press summary; `0` resolutions of $b(t) = 3$.

## Coverage Limits
- Covers `watch/snapshots` (`760` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:58:54Z`; private repositories and non-indexed preprints remain unobservable.
