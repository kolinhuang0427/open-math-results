# Gate 2 Novelty Check — `fernando-2606.01037-quesQ1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:29:15Z`–`2026-11-27T17:29:29Z`
- **Target:** `targets/fernando-2606.01037-quesQ1/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.1 (`\label{Q1}`, `draftMay31.tex` L893–895)
- **Claimed result:** Complete classification ($g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff ($q = 4$ and $4 \mid e$) or ($e = 4$ and $m \not\equiv 3 \pmod 4$), proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Fernando" "Kousik" "Question 6.1"`):**
   - `0` hits on `2606.01037` or `Kousik` across `745` files; `Fernando` matches only `fernando2026goodcolorings` / `fernando-doubled-triangle-minimum-fold` (`2611.12065`) and arXiv authors (`Fernando Rodriguez Villegas`, `Fernando Muro`); `Question 6.1` hits only unrelated papers (`cardon-zero-sector`, `lambie-hanson-uhrik-disjoint-type-guessing`, `defant`, etc.).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:29:15Z`):**
   - `main` = `abfdfb383a8eaa1ceea804f47c7bab300555a4ee` (`2026-11-27T17:26:06Z`, PR `#1070`, Komjáth property B) — unrelated.
   - `research` = `ae78c663cf4f4c9055b72396dd419c8d8924fb9a` (`2026-11-27T17:27:39Z`, positive linear Ky Fan lifts) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, covers Conjecture 5.23 only, not Section 6 Question 6.1).
   - `gh search code "2606.01037"` -> `ehijano/rss_fetch` RSS XML, `koutya0akari/arxiv-plug-in-for-mixi2` feed, `10m-u/open-problems-catalog` (`sources/F.md`, `problems/mathematics/number-theory.md`, cataloging Question 6.1 as Open), plus unrelated CSV/txt numeric collisions.
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Fernando–Kousik `arXiv:2606.01037`.
   - Web search -> only Fernando–Kousik `arXiv:2606.01037` preprint; `0` resolutions of Section 6 Question 6.1.

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:29:29Z`; private repositories and non-indexed preprints remain unobservable.
