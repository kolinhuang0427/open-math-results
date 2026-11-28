# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/dawar-2611.23541-sym-depth/`

- **Target:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *Depth Hierarchies for Symmetric Algebraic Circuits*, `arXiv:2611.23541v1` (`2026-11-17`, submitted to STOC 2027), Section 1.2 (*Future work*, `introduction.tex` L269–271): depth-3/4 symmetric circuit reductions and orbit-size lower/upper bounds (`PROOF.md` Theorems 1–4, Lemma 1–2; label **"written proof, internally audited"**).
- **Checked UTC:** `2026-11-27T20:56:41Z` – `2026-11-27T20:57:04Z`
- **Verdict:** **PASS — OPEN** (no competing or prior settlement of Section 1.2 depth-3/4 symmetric reduction or orbit bounds found).

## Exact Checks & Results

1. **Local Snapshot Index (`watch/snapshots/`, post-Sweep 24 `930` cataloged repos / `660` snapshots) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.23541" "dawar-2611.23541" "Lax461425" "Dawar" "symVBP" "symVAC" --max-per-file 0 --max-total 30` -> matched only `watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` (`2611.23541v1` itself) and `watch/snapshots/discovered/tseppelt__lax-symmetric-depth-reduction.json` (author Lean formalization `Lax461425` of `2611.23541v1`'s own theorems, pushed `2026-11-13`, verified not to resolve Section 1.2).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T20:56:42Z`–`20:57:03Z`):**
   - `gh search code` for `"2611.23541"`, `"symVBP"`, `"Dawar" "depth-3" "symmetric"`, and `repo:the-omega-institute/trureturing 2611.23541` -> `[]` (`0` hits on all four).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T20:46Z`–`20:57:04Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `dawar`, `symmetric algebraic`, `symv`, or `depth hierarch` (and earlier `20:36Z` inspection confirmed Dwivedi/Seppelt ECCC 2026 reports `TR26-182` and `TR26-025` are unrelated).
   - `https://export.arxiv.org/api/query?id_list=2611.23541` -> `2611.23541v1` sole version (`submitted to STOC 2027`).
   - `https://hexagonmath.org/api/v1/works` (`1,675` works; `q=2611.23541`, `q=Dawar`, `q=symVBP` -> `total=0`), `https://papex.org/sitemaps/records-1.xml` (`20` records, checked Sweep 24 `20:46Z`), `Zenodo` (`0`), `Crossref` (`0` matching `2611.23541`), `search_web` (`arXiv:2611.23541` & author `laxarchive.org/lax-461425/` page only).
4. **Independent Verifier Verification (`@audit-2` PASS `#1980`):**
   - Executed `.venv/bin/python -u targets/dawar-2611.23541-sym-depth/notes/check-check-1.py` -> exited `0` (`PASS`).

## Coverage Limits

- At `20:56Z`, unauthenticated OpenAlex returned `HTTP 429` (covered via ECCC `/year/2026/`, `search_web`, Crossref, arXiv, and Zenodo); private repositories and auth-gated conference manuscripts remain outside public reach.
