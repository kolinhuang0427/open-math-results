# Gate 2 Novelty Receipt (`watch-6`) — `targets/dochtermann-2609.13361-conj7.5/`

- **Checked UTC:** `2026-11-27T12:00:36Z`–`2026-11-27T12:00:58Z`
- **Target:** Dochtermann, Huang, Mawhinney, Oh, Xu, *Matroids with cycle systems are regular*, `arXiv:2609.13361v1` (2026-09-11), Section 7, **Conjecture 7.5** (`\label{conj:C>=3 ind}`, plus implied Conjecture 7.4 `\label{conj:unique}`).
- **Verdict:** **OPEN / PASS**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `690` snapshot files):**
   - `2609.13361` -> `5` lines in `watch/snapshots/discovered/tamnd__arxiv.json` (`analysis/{bib,census,edges,objects,prose}/2609/2609.13361*` — automated paper index only; `0` resolution hits).
   - `Dochtermann`, `conj:C>=3 ind`, `conj:unique`, `cographic vertex-star` -> `0/690`.
2. **GitHub Live Search (`gh` CLI):**
   - `gh search code 2609.13361` -> `tamnd/arxiv` (metadata/census index, inspected `analysis/prose/2609/2609.13361.md`), `ehijano/rss_fetch` (arXiv RSS), and **`cmu-l3/reuF2F`** (`lean/reuF2F/dochtermann2026matroids.lean`). Direct inspection of `cmu-l3/reuF2F/lean/reuF2F/dochtermann2026matroids.lean` confirms **`theorem conjecture_7_5 ... := by sorry`** (open formalization statement stub only, no proof).
   - `gh search code '"Dochtermann" "matroid"'` -> `cmu-l3/reuF2F`, `tractatus1889/stanley` (unrelated Stanley conjecture repo), older references (`Macaulay2`, `cross-theory-formal-database`, `eminichiello67`).
   - `gh search code '"conj:C>=3 ind"'` -> `[]`.
   - `gh search repos "2609.13361"` / `gh search issues "2609.13361"` -> `[]`.
   - `gh api repos/the-omega-institute/trureturing/git/trees/dev?recursive=1` -> `0` hits for `2609.13361`, `dochtermann`, `cographic`.
3. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?id_list=2609.13361` -> sole entry `2609.13361v1` (`2026-09-11T17:52:05Z`, *Matroids with cycle systems are regular*); `au:Dochtermann` -> 10 entries, none resolving `conj:C>=3 ind`.
   - `zenodo.org/api/records?q=2609.13361` -> `0` hits.
   - `search_web` (`"2609.13361" OR ("Dochtermann" "Conjecture 7.5" "cographic")`) -> returns only `arXiv:2609.13361v1`.

## Coverage Limits

- Unindexed private repositories, closed-access journals, or non-indexed author webpages remain outside public visibility; all checked public indices confirm Conjecture 7.5 (`\label{conj:C>=3 ind}`) remains open.
