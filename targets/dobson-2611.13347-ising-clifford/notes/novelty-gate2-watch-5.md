# Gate 2 Novelty Check — `dobson-2611.13347-ising-clifford` (`watch-5`)

- **Timestamp:** `2026-11-27T22:36:41Z`
- **Verdict:** **PASS — `OPEN / UNCONTESTED`**
- **Target:** Sawyer Dobson and Zhenghan Wang, *"Computational Power of Clifford and Ising Quantum Computers"*, `arXiv:2611.13347v1` (`2026-11-09T23:19:02Z`), Section 5 Problem (3) (`sections/5.tex` L11) — ancilla-assisted Ising braiding vs Clifford gates and $\mathbf{PUSB}/\mathbf{LUSB}$ vs $\mathbf{PUSC}/\mathbf{LUSC}$.

## Verification Receipts

1. **`watch/snapshots/` (`novelty_grep.py "2611.13347" "Dobson" "PUSB" "LUSB" "Ising braiding" "ISING-BRAID"` across `865` files):**
   - `47` lines across `12/865` files: `2611.13347v1` in `arxiv_submissions.{json,md}` and `state.json`, plus unrelated Ted Dobson Cayley graph isomorphism, `rodrigueskevrekidisdobson2019nbreak`, `atlas-lean` statistical-mechanics Ising torus, and `PlusB` substring matches. `0` settlements.
2. **Live GitHub (`gh search` & `trureturing`):**
   - `gh search issues/prs/repos "2611.13347"`: `0` hits each.
   - `gh search code "2611.13347"`: arXiv digests/audits (`LeeMath-lzu`, `ryuikaneko`, `thinhhoang95/project-libera`, `ehijano/rss_fetch`) only.
   - `gh search code "PUSB" "LUSB"`: unrelated USB/u-boot substrings.
   - `the-omega-institute/trureturing` PRs up to `#35015`: `0` hits.
3. **arXiv API (`export.arxiv.org`):**
   - `id_list=2611.13347`: `2611.13347v1` (`2026-11-09T23:19:02Z`) sole version.
   - `all:"PUSB" OR all:"LUSB" OR (all:"Ising braiding" AND all:"Clifford")`: unrelated condensed-matter `LuSb` preprints only.
4. **Citations & Preprints (OpenAlex / OpenCitations / Zenodo / Crossref):**
   - OpenAlex `W7225829184` (`10.48550/arXiv.2611.13347`): `cited_by_count: 0`.
   - OpenCitations (`10.48550/arXiv.2611.13347`): `200 []`.
   - Zenodo (`2611.13347`): `0` hits. (Crossref `404`.)
5. **ECCC & Conference Web Search (`search_web`):**
   - Query `"2611.13347" OR ("Ising braiding" "Clifford" ("PUSB" OR "LUSB")) OR ("Dobson" "Ising" "Clifford" (ECCC OR QIP OR TQC OR STOC OR FOCS))` returned only `arXiv:2611.13347` itself (`0` follow-up settlements).
