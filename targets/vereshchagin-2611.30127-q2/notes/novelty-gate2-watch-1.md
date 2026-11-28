# Gate 2 Novelty Check — `vereshchagin-2611.30127-q2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T19:32:28Z`–`2026-11-27T19:33:14Z`
- **Target:** `targets/vereshchagin-2611.30127-q2/` — Nikolay Vereshchagin, *"How Much Randomness is Needed to Convert MA Protocols to AM Protocols?"* (`arXiv:2611.30127v1`, `2026-11-23`; earlier ECCC `TR22-060`, CSR 2022 LNCS 13296 pp. 338–349, `DOI:10.1007/978-3-031-09574-0_21`), Section 7 Open Questions 2 & 3 (`main-eng.tex` L774–780; Section 1 L151–154)
- **Claimed result:** **NO** to both Open Questions 2 & 3 (algebrizing barriers separating $\mathrm{MAP}^A[m,a] \cap \mathrm{MA}^A[m,a]$ from $\mathrm{PP}\cdot\mathrm{NP}^{\widetilde{A}}[*, p(a)]$ and $\mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[*, p(a)]$, proved in `PROOF.md`, zero-float `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.30127" "Vereshchagin" "algebrization"`):**
   - `15` lines across `6/811` files (`watch/snapshots/arxiv/arxiv_submissions.*` & `state.json` indexing `2611.30127v1` itself; `facebookresearch__atlas-lean/files.txt` `AlgebrizationWanted.lean`; `qedavid__solverz` barriers summary; `plasma-ai__erdos` 2017 conditional information inequality); `0` settlement hits across `811` snapshot files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T19:32:28Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `68951fa0c7c192ac9922e7413d67911f8e3ff3ee` (`2026-11-27T19:32:03Z`, countable edge-Ramsey witnesses) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.30127"` -> `0` hits (`[]`).
   - `gh search issues "2611.30127"` -> `0` hits (`[]`).
   - `gh search code "2611.30127"` -> `ehijano/rss_fetch` RSS XML + unrelated numeric CSV/JSON/log collisions only.
4. **arXiv / Zenodo / Crossref / ECCC / Web:**
   - arXiv API (`id_list=2611.30127`) -> sole version `2611.30127v1` (`2026-11-23T06:37:19Z`).
   - Zenodo API (`q=2611.30127`) -> `0` hits.
   - Crossref (`query.title=How+Much+Randomness+is+Needed+to+Convert+MA+Protocols+to+AM+Protocols`) -> CSR 2022 `DOI:10.1007/978-3-031-09574-0_21` has `is-referenced-by-count: 0`.
   - `search_web` (including ECCC `TR22-060` & CSR 2022 `10.1007/978-3-031-09574-0_21` follow-up queries) -> returns only Vereshchagin's own TR22-060 / CSR 2022 / `arXiv:2611.30127v1` paper and Aaronson–Wigderson (2009); `0` follow-up resolutions of Open Questions 2 or 3 on algebrization.

## Coverage Limits
- Covers `watch/snapshots` (`811` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and `search_web` (including indexed ECCC pages) as of `2026-11-27T19:33:14Z`. Direct `curl` to `https://eccc.weizmann.ac.il/` returned no response (empty output), and the `site:eccc.weizmann.ac.il` web search returned no summary, so ECCC coverage relied on the remaining web searches (`"TR22-060"`, `"Vereshchagin" "algebrizing"`).
