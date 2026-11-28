# Gate 3 Novelty & Checker Receipt — `radici-2609.07769-open` (`watch-5`)

- **Timestamp:** `2026-11-28T00:29:37Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Gabriele Radici and Massimiliano Sala, *"A Note on Binary Quadratic Systems and Their Relation to Complexity Theory"*, `arXiv:2609.07769v2` (`2026-11-25T13:37:50Z`), §9 (*Open problems*), $\alpha_1(q,n,d) > \alpha_0(q,n,d)$ over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$.

## Fresh Live Novelty Checks (`00:29:37Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2609.07769" "Radici" "MQ_1" "MQ_0"`):** `0` settlements (`24` lines across `6/914` files: `2609.07769v2` in `arxiv_submissions.{json,md}`, `last_sweep_report.json`, `state.json`, `AlexenderSokolov__cross-theory-formal-database` `v1` license, and unrelated `formal-arithmetic-geometry__weil-conjectures` `Radicial*` files).
- **arXiv API:** `2609.07769v2` (`2026-11-25T13:37:50Z`) current latest version.
- **OpenAlex / OpenCitations / Zenodo:** `W7212034157` (`10.48550/arXiv.2609.07769`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search issues/prs "2609.07769"` `0` hits; `trureturing` PRs up to `#35057` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2609.07769` itself; no follow-up settlement over $\mathbb{F}_3, \mathbb{F}_4, \mathbb{F}_5$.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/radici-2609.07769-open/{TARGET.md,PROOF.md,verify.py,AUDIT.md,notes/check-check-1.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/radici-2609.07769-open/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (`BASE_N2` exact for $q\in\{3,4,5\}$, `LEMMA5_COEFFS`, `CASE2..CASE6`, exact `GRM_5(2,3)^perp` MacWilliams tail; `AST_FLOATS: []`, `FLOAT_CALLS: []`).
