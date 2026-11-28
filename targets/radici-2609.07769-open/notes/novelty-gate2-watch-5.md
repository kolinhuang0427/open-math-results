# Gate 2 Novelty Check — `radici-2609.07769-open` (`watch-5`)

- **Timestamp:** `2026-11-27T23:33:10Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Gabriele Radici and Massimiliano Sala, *"A Note on Binary Quadratic Systems and Their Relation to Complexity Theory"*, `arXiv:2609.07769v2` (`2026-11-25T13:37:50Z`), Section 7 (`main-v32.tex` L1498–1527) — whether $\alpha_1(q,n,d) > \alpha_0(q,n,d)$ holds over $q \in \{3, 4, 5\}$ ($\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$).

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2609.07769" "Radici" "MQ_1" "MQ_0"` across `880` files):**
   - `14` lines across `5/880` files: `2609.07769v2` in `arxiv_submissions.{json,md}`, `last_sweep_report.json`, `state.json`, plus `AlexenderSokolov__cross-theory-formal-database` (`lem:global_derivative` from `2609.07769v1` over $\mathbb{F}_2$). `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues/prs/repos "2609.07769"`: `0` hits each.
   - `gh search code "2609.07769"`: `24` hits (`AlexenderSokolov/cross-theory-formal-database` `2609.07769v1` `lem:global_derivative` only, `amoni094/hermes-config`, `ehijano/rss_fetch`, `uninhibited-scholar`, and unrelated numeric floats).
   - `the-omega-institute/trureturing` PRs up to `#35038`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `id_list=2609.07769`: `2609.07769v2` (`2026-11-25T13:37:50Z`) current latest version.
   - `au:Radici OR all:"MQ_1" OR (all:"MQ" AND all:"Sala" AND all:"finite fields")`: returns `2609.07769v2` and unrelated physics papers.
4. **Citations & Preprints (OpenAlex / OpenCitations / Zenodo / Crossref):**
   - OpenAlex `W7212034157` (`10.48550/arXiv.2609.07769`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2609.07769`): `200 []`.
   - Zenodo (`2609.07769`): `0` hits. (Crossref `404`.)
5. **ECCC, IACR ePrint & Conference Web Search (`search_web` + `notes/novelty-attack.md`):**
   - Query `"2609.07769" OR ("Radici" "Sala" ("MQ_1" OR "MQ_0" OR "Quadratic Equations") (ECCC OR EUROCRYPT OR CRYPTO OR ASIACRYPT OR IACR OR STOC OR FOCS))` returned only `arXiv:2609.07769` (IACR `2026/2022` from `2026-09-14` is $\mathbb{F}_2$-only, prior to `2609.07769v2`; `0` follow-up settlements over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$).
