# Gate 2 Novelty Check — `cai-2610.02047-plog-reg` (`watch-5`)

- **Timestamp:** `2026-11-27T21:31:25Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Shaowei Cai and Ziqun Li, *"Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth"*, `arXiv:2610.02047v1` (`2026-10-01T16:56:03Z`), Section 8 (`main.tex` L4025–4031) — whether every unsatisfiable CNF formula has an FPT-sized regular resolution refutation parameterized by partially log-weighted incidence treewidth $\mathrm{tw}_{\mathrm{plog}}^*(F)$.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2610.02047" "tw_plog" "plog-treewidth" "partially log-weighted" "Shaowei Cai" "Ziqun Li"` across `855` files):**
   - `0 lines across 0/855 files`.
2. **Live GitHub (`gh search` & `gh api`):**
   - `gh search prs/repos "2610.02047"`: `0` hits.
   - `gh search issues "2610.02047"`: `2` unrelated hits — inspected `the-omega-institute/trureturing#25977` (Yuhao Han `arXiv:2611.01890v1` ZX calculus treewidth substitution) and `j15marti/pnp#3` (strict-3CNF backdoor notes).
   - `gh search code "2610.02047"`: `30` results — inspected `rainwangphy/aftd-platform` (`9/9` matches are textbook Sec 3.1/3.2 definitions `CnfVars`, `CnfLitVar`, `GraphTreewidth`, `CnfIncidenceGraph`, `CnfIncidenceTreewidth`, `IsResolutionRefutation`, `IsResolutionDerivation`, `HasTreeDecompositionOfWidthLe`, `ResolutionRefutationExistsOfUnsat`, `0` hits for `plog`); inspected `j15marti/pnp` `research/agents/lspv-1/2026-10-29_0300_{ARC219_sources.bib,LSPV-1_ARC219_WIDTH_CERTIFICATE_GUARD_SANDWICH.tex}` (cites `2610.02047` only as background while doing primal-width DP elimination); `jtraverso/erdos-81-chordal-clique-partitions` is unrelated Erdős #81.
   - `the-omega-institute/trureturing` PRs up to `#34994`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `2610.02047v1` (`2026-10-01`) sole version.
   - `cat:cs.CC AND (all:"plog" OR (all:"treewidth" AND all:"regular resolution"))`: returns only `2610.02047v1` and earlier papers (`2103.09609v1`, `1911.13104v1`, `1905.10867v2`).
4. **Citations & Preprints (OpenAlex / OpenCitations / Zenodo / Crossref):**
   - OpenAlex `W7216287821` (`10.48550/arXiv.2610.02047`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2610.02047`): `200 []`.
   - Zenodo (`2610.02047`): `0` hits. (Crossref `404`.)
5. **ECCC & Conference Web Search (`search_web`):**
   - Query `"2610.02047" OR ("plog" "regular resolution" "treewidth") OR ("mRes" "regular resolution" (ECCC OR SAT OR STOC OR FOCS OR CCC))` surfaced only `arXiv:2610.02047` and background `MRes` literature (`dagstuhl.de`, `eccc.weizmann.ac.il`), with no follow-up settling $\mathrm{tw}_{\mathrm{plog}}^*(F)$ regular resolution.
