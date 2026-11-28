# Gate 2 Novelty Check — `vereshchagin-2611.30127-q2` (`watch-5`)

- **Timestamp:** `2026-11-27T19:33:00Z` (checked `19:32:52Z`–`19:33:37Z`)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Nikolay Vereshchagin, *"How Much Randomness is Needed to Convert MA Protocols to AM Protocols?"*, `arXiv:2611.30127v1` (`2026-11-23T06:37:19Z`; earlier CSR 2022 LNCS 13296 pp. 338–349 `DOI:10.1007/978-3-031-09574-0_21` / ECCC `TR22-060`), §7 Open Questions 2 & 3 (`main-eng.tex` L774–780, §1 L151–154) — whether $\mathrm{MA}[m,a] \subset \mathrm{AM}[*,p(a)]$ or Knop's Conjecture 1 can be proved by algebrizing techniques.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.30127" "Vereshchagin" "algebriz" "Knop"` across `811` files):**
   - `23` lines across `8/811` files (`arxiv_submissions.{json,md}`, `state.json`, unrelated `atlas-lean/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean` [STOC 2008 AW definition only], `plasma-ai__erdos` 2017 conditional info inequality, `qedavid__solverz` overview).
   - `0` hits in `hexagonmath`, `papex`, `hwzw`, `raghav`, `trureturing`.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues "2611.30127"`, `gh search prs "2611.30127"`, `gh search repos "2611.30127"`: `0` hits.
   - `gh search code "2611.30127"`: `17` hits (`ehijano/rss_fetch` + numeric logs only).
   - `trureturing` `dev` tree & PRs up to `#34956`: `0` hits.
3. **arXiv API:**
   - `2611.30127v1` (`2026-11-23T06:37:19Z`) is the sole arXiv version.
   - Author search (`Nikolay Vereshchagin`): unrelated papers only.
   - `cat:cs.CC AND all:"algebrization" AND (all:"MA" OR all:"AM")`: `2511.14038v1` (inspected `tools/.arxiv_cache/abs/2511.14038.html`: XOR-Missing-String barriers for $\mathsf{PostBPE}/\mathsf{BPE}/\mathsf{MA}_{\mathsf{E}}$ circuit lower bounds, unrelated to $\mathrm{MA}[m,a]\subset \mathrm{AM}[*,p(a)]$) and `1101.0523v1` (2011).
4. **Citations & Preprints (OpenAlex / Semantic Scholar / OpenCitations / Crossref / Zenodo):**
   - OpenAlex `W4285197414` (`10.1007/978-3-031-09574-0_21`): `cited_by_count: 0`.
   - OpenCitations: `[]`.
   - Crossref: `is-referenced-by-count: 0`.
   - Zenodo (`2611.30127`): `0` hits.
   - Semantic Scholar (`DOI:10.1007/978-3-031-09574-0_21`): `citationCount: 2` — both are SIGACT News *Technical Report Column* (`Kelley22b`, `Kelley23b`, listing ECCC `TR22-060`).
5. **ECCC & Conference Web Search (`search_web`):**
   - Searches for `"2611.30127"`, `"How Much Randomness..."` / `"TR22-060"`, and `"MA" "AM" "algebrization"` follow-ups returned only `TR22-060` / CSR 2022 / `2611.30127v1` and no settlement.
