# Gate 2 Novelty Check — `dawar-2611.23541-sym-depth` (`watch-5`)

- **Timestamp:** `2026-11-27T20:35:39Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *"Depth Hierarchies for Symmetric Algebraic Circuits"*, `arXiv:2611.23541v1` (`2026-11-17T21:49:23Z`, comment: `submitted to STOC 2027`), Section 1.2 (*Future work*, `introduction.tex` L269–271) — whether symmetric algebraic circuits can be reduced to depth $3$ or $4$, and at what cost in orbit size.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.23541" "Dwivedi" "Pago" "Seppelt" "symVP" "symVAC" "symVBP"` across `837` files):**
   - `14` lines across `5/837` files: `2611.23541v1` in `arxiv_submissions.{json,md}` and `state.json`, plus unrelated `Rattan & Seppelt (2023)` and `Srashti Dwivedi` Rado number PR (`atlas-lean#10771`). `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues/prs/repos "2611.23541"`: `0` hits each.
   - `gh search code "2611.23541"`: `7` hits (`qiao-925/news-digest` abstract mirror + unrelated numeric CSVs).
   - `gh search code "symVBP"`: `agentopedia/pvsnp` (`2502.06740` summary) and **`tseppelt/lax-symmetric-depth-reduction`** (author Tim Seppelt's Lean formalization `Lax461425` of `2611.23541` itself, pushed `2026-11-13T07:28:00Z`; inspected `abstract.md` and `git/trees/HEAD` + searched `"depth 4"`/`"Tavenas"` -> `0` hits, confirms no depth-3/4 symmetric reduction).
   - `the-omega-institute/trureturing` PRs up to `#34974`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `id_list=2611.23541`: `2611.23541v1` (`2026-11-17T21:49:23Z`, `submitted to STOC 2027`) sole version.
   - `(all:"symVP" OR all:"symVAC" OR all:"symVBP" OR all:"symmetric algebraic circuits")`: returns only `2611.23541v1` and earlier preprints (`2606.26244v2`, `2601.09343v1`, `2502.06740v4`).
4. **Citations & Preprint Repositories (OpenAlex / OpenCitations / Zenodo / Crossref / S2):**
   - OpenAlex `W7236732928` (`10.48550/arXiv.2611.23541`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2611.23541`): `200 []`.
   - Zenodo (`2611.23541` and title): `0` hits.
   - Note: Crossref `404`; S2 `429`.
5. **ECCC & Conference Web Search (`search_web`):**
   - Queries for `"2611.23541"`, `"Depth Hierarchies for Symmetric Algebraic Circuits"`, `"symVBP" "Dawar"`, `"symVAC" "depth-four"/"depth-three"`, and ECCC/STOC/FOCS/CCC/ICALP/STACS follow-ups surfaced only `arXiv:2611.23541` and its Lax Lean Archive formalization (`laxarchive.org` / `tseppelt/lax-symmetric-depth-reduction`).
