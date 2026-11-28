# Gate 3 Novelty & Checker Receipt — `dobson-2611.13347-ising-clifford` (`watch-5`)

- **Timestamp:** `2026-11-28T01:15:00Z` (`<1h` fresh Gate 3)
- **Verdict:** **PASS — `OPEN / UNCONTESTED`** (`written proof, internally audited`)
- **Target:** Sawyer Dobson and Zhenghan Wang, *"Computational Power of Clifford and Ising Quantum Computers"*, `arXiv:2611.13347v1` (`2026-11-09T23:19:02Z`), §5 Problem (3) (ancilla-assisted Ising braiding no-go on $n \ge 3$, `PUSB`/`LUSB` vs `PUSC`/`LUSC`, `ISING-BRAID in L`, 1-ancilla measurement equivalence).

## Fresh Live Novelty Checks (`01:15:00Z`)
- **`watch/snapshots/**` (`novelty_grep.py "2611.13347" "Sawyer Dobson" "Zhenghan Wang" "ISING-BRAID"`):** `0` settlements (`15` lines across `6/936` files: `arxiv_submissions.{json,md}`, `citing_papers.{json,md}`, `last_sweep_report.json`, `state.json` entries for `2611.13347v1` only).
- **arXiv API:** `2611.13347v1` (`2026-11-09T23:19:02Z`) sole version.
- **OpenAlex / OpenCitations / Zenodo:** `W7225829184` (`10.48550/arXiv.2611.13347`) `cited_by_count: 0`; OpenCitations `200 []`; Zenodo `0` hits.
- **GitHub & `trureturing`:** `gh search issues/prs "2611.13347"` `0` hits; `trureturing` PRs up to `#35070` clear.
- **ECCC & Venue Web Search (`search_web`):** only `arXiv:2611.13347v1` itself; no follow-up settlement.

## Verification on Disk & Checker Run
- **Verified files present:** `targets/dobson-2611.13347-ising-clifford/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.
- **Command:** `.venv/bin/python -u targets/dobson-2611.13347-ising-clifford/notes/check-check-1.py`
- **Result:** Exit `0` — `PASS` (`MAJORANA_AND_NOGO: PASS`; `ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS`; `ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS`).
