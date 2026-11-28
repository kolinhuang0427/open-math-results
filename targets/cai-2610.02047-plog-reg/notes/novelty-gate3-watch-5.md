# Gate 3 Novelty & Checker Receipt — `cai-2610.02047-plog-reg` (`watch-5`)

- **Timestamp:** `2026-11-27T21:52:11Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Shaowei Cai and Ziqun Li, *"Short Resolution Refutations for CNFs with Bounded Weighted Incidence Treewidth"*, `arXiv:2610.02047v1` (`2026-10-01T16:56:03Z`), Section 8 FPT-sized regular resolution refutations parameterized by $\mathrm{tw}_{\mathrm{plog}}^*(F)$.

## Fresh Live Novelty Checks (`21:52:11Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2610.02047" "tw_plog" "plog-treewidth" "partially log-weighted" "Shaowei Cai" "Ziqun Li"`):** `0` settlements (`3` lines across `2/863` files: `citing_papers.{json,md}` showing `OpenAlex cited_by=0; S2=0`).
- **arXiv API:** `2610.02047v1` (`2026-10-01T16:56:03Z`) sole version.
- **OpenAlex / OpenCitations / Zenodo:** `W7216287821` (`10.48550/arXiv.2610.02047`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search prs "2610.02047"` `0` hits; `gh search issues "2610.02047"` same 2 unrelated issues (`trureturing#25977`, `j15marti/pnp#3`); `trureturing` PRs up to `#35003` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2610.02047` itself; no follow-up settlement.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/cai-2610.02047-plog-reg/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/cai-2610.02047-plog-reg/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (`JOIN_COUNTEREXAMPLE: L165_fails=True, corrected_regular_ok=True, len=6`; `COMPLEX_TD_MODES: on_t1=PASS, on_t2=PASS, off=PASS`; `AUDIT2_ADVERSARIAL_TDS: 5/5 + 27/27 join modes PASS`).
