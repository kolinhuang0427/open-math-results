# Gate 3 Novelty Receipt (`watch-1`): `targets/navarra-2511.22346-conj2.3/`

- **Checked UTC:** `2026-11-27T09:23Z`
- **Target:** Francesco Navarra, Ayesha Asloob Qureshi, and Giancarlo Rinaldo, *"Switching rook polynomial of collections of cells"*, `arXiv:2511.22346v1` (`2025-11-27`), Section 2, Conjecture 2.3 (`\label{conj}`)
- **Audited Artifacts Verified:** `TARGET.md`, `COUNTEREXAMPLE.md`, `AUDIT.md` (`@audit-3` PASS `2026-11-27T09:20Z`), cmd `.venv/bin/python targets/navarra-2511.22346-conj2.3/notes/check-check-1.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2511.22346 ... "Navarra"`):** `0` hits for `2511.22346` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z` and `trureturing`); `"Navarra"` matches only unrelated 2026 preprints (`2611.27531`, etc.) in `watch/snapshots/arxiv/arxiv_submissions.*`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2511.22346,2603.19554,2401.09497`):** `2511.22346v1` (`2025-11-27T11:36:19Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2511.22346&size=5`):** `0` hits.

## Coverage Limits
- Live `gh search` was not re-queried after the `09:17Z` GitHub Search API rate limit; mitigated by `608`-file `watch/snapshots/**` grep (`1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`) plus live arXiv and Zenodo checks.
