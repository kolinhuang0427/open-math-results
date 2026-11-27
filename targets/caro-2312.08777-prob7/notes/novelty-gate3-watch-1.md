# Gate 3 Novelty Check — `caro-2312.08777-prob7` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:06:44Z`–`2026-11-27T18:06:56Z`
- **Target:** `targets/caro-2312.08777-prob7/` — Yair Caro, Josef Lauri, Xandru Mifsud, Raphael Yuster, and Christina Zarb, *"Flip colouring of graphs"* (`arXiv:2312.08777v1`, `2023-12-14`, *Graphs and Combinatorics* 40 (106), 2024, `DOI:10.1007/s00373-024-02838-w`), Section 7 final Problem ($b(t)$ for $t$-neighbourhood flip graphs)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` ($b(t) = 3$ for all $t \ge 1$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2312.08777" "Mifsud" "Zarb"`):**
   - `0` lines across `0/760` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:06:44Z`):**
   - `main` = `f25117a3adbcf1daa50d458fe400bdc5093133de` (`2026-11-27T18:05:27Z`, PR `#1075`, Lambie-Hanson–Uhrik disjoint-type guessing) — unrelated.
   - `research` = `0be09cfd9d3b7b5661e1dbfb6c4885c513eb1b10` (`2026-11-27T18:02:54Z`, Hajnal–Máté obstructions) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2312.08777"` -> `0` hits (`[]`).
   - `gh search issues "2312.08777"` -> `0` hits (`[]`).
   - `gh search code "CayleyTFlip"` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2312.08777`) -> sole version `2312.08777v1` (`2023-12-14T09:54:17Z`).
   - Zenodo API (`q=2312.08777`) -> `0` hits.
   - Crossref (`10.1007/s00373-024-02838-w`) -> `is-referenced-by-count: 0`.
   - Web search -> only Caro–Lauri–Mifsud–Yuster–Zarb (`2023`/`2024`) paper and UM summary; `0` resolutions of $b(t) = 3$.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/caro-2312.08777-prob7/notes/check-check-2.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`760` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T18:06:56Z`; private repositories and non-indexed preprints remain unobservable.
