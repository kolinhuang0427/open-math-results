# Gate 3 Novelty & Checker Receipt — `kern-2611.32927-gcs-dichotomy` (`watch-5`)

- **Timestamp:** `2026-11-27T21:14:33Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Christoph Kern, Alexander Firbas, and Manuel Sorge, *"Algorithms and Complexity of Connectivity Switching in Graphs"*, `arXiv:2611.32927v1` (`2026-11-24T16:37:07Z`, LATIN 2026), §4 (`sections/gcon.tex` L116) `Global-Con Switching` matroid-switch dichotomy conjecture.

## Fresh Live Novelty Checks (`21:14:33Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2611.32927" "matroid switches" "Global-Con Switching"`):** `0` settlements (`6` lines across `3/854` files: `arxiv_submissions.{json,md}`, `state.json` entries for `2611.32927v1` only).
- **arXiv API:** `2611.32927v1` (`2026-11-24T16:37:07Z`) sole version.
- **OpenAlex / OpenCitations / Zenodo:** `W7239759747` (`10.48550/arXiv.2611.32927`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search issues/prs "2611.32927"` `0` hits; `trureturing` PRs up to `#34990` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2611.32927` itself; no follow-up settlement.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/kern-2611.32927-gcs-dichotomy/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/kern-2611.32927-gcs-dichotomy/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (`Non-matroid axioms and GCS equivalences (Pi_1, Pi_2, Pi_3): PASS`).
