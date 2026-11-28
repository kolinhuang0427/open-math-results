# Gate 2 Novelty Receipt (`watch-6`) — `targets/dawar-2611.23541-sym-depth/`

- **Target:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *Depth Hierarchies for Symmetric Algebraic Circuits*, `arXiv:2611.23541v1` (`2026-11-17`, submitted to STOC 2027), Section 1.2 (*Future work*, `introduction.tex` L269–271): whether symmetric circuits can be reduced to depth $3$ or $4$, and at what cost in orbit size.
- **Checked UTC:** `2026-11-27T20:35:00Z` – `2026-11-27T20:36:30Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of Section 1.2 depth-3/4 symmetric reduction or orbit lower/upper bounds found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `837` files across `918 -> 919` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.23541" "Dawar" "symVBP" "symmetric reduction" "symmetric algebraic" --max-per-file 0 --max-total 30` -> `9` lines across `3/837` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.23541v1` itself only).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T20:35:05Z`–`20:36:28Z`):**
   - `gh search code/repos` for `"2611.23541"`, `"symVBP"`, `"Dawar" "depth-3" "symmetric"`, `"Dawar" "symmetric" "circuit"` -> `0` hits; `repo:the-omega-institute/trureturing 2611.23541` & `symVBP` -> `0` hits.
   - Peer-spotted (`watch-5` `#1963`) `tseppelt/lax-symmetric-depth-reduction` (`54683d1`, `263` files, pushed `2026-11-13T07:28:00Z`) snapshotted into `watch/snapshots/discovered/tseppelt__lax-symmetric-depth-reduction.json` (`CATALOG` `919` / `649`): Tim Seppelt et al.'s Lean 4 formalization (`Lax461425`) of `arXiv:2611.23541v1`'s own theorems (`DepthHierarchy`, `SupportTheorem`, `CircuitsForPatterns`, `BoundedDepthCharacterisation`, etc.), with zero resolution of Section 1.2's open depth-3/4 symmetric reduction question.
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Lax Lean Archive, Hexagon, Zenodo, Crossref & Web (`2026-11-27T20:35:05Z`–`20:36:15Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `TR26-182` (Blanc–Dwivedi–Limaye–Mahajan–Hansen, algebraic communication) and `TR26-025` (Brand–Curticapean–Kaski–Li–Orzel–Seppelt–Wang, bilinear many-mode complexity) — both unrelated to `arXiv:2611.23541v1` §1.2; `0` hits for `dawar` / `symv` / `depth hierarch`; `search_web domain:eccc.weizmann.ac.il` clear.
   - `https://export.arxiv.org/api/query?id_list=2611.23541` -> `2611.23541v1` sole version (`submitted to STOC 2027`).
   - `https://laxarchive.org/lax-461425/`: hosts the Lean archive page for `tseppelt/lax-symmetric-depth-reduction` (`Lax461425.*` theorems of `2611.23541v1` only).
   - `https://hexagonmath.org/api/v1/works` (`q=2611.23541`, `q=Dawar`, `q=symVBP`) -> `total=0`; Zenodo (`"2611.23541"`, `"Depth Hierarchies for Symmetric Algebraic Circuits"`, `"symVBP"`) -> `0`; Crossref title search -> `0` matches for `2611.23541`; `search_web` returns only `2611.23541` & `lax-461425`.

## Coverage Limits

- At `20:35Z`, unauthenticated OpenAlex and Semantic Scholar endpoints returned `HTTP 429` rate limits (cross-checked via ECCC `/year/2026/`, `search_web`, Crossref, arXiv, and Zenodo); private/unindexed repositories and auth-gated conference papers remain outside public reach; Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
