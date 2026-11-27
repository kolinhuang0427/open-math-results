# Gate 3 Novelty Receipt (`watch-1`): `targets/garrison-2401.09497-conj5.2/`

- **Checked UTC:** `2026-11-27T09:23Z`
- **Target:** Thomas Garrison, Chris Seiler, and Andrew Knowles, *"Weakly Consecutive Sequences"*, `arXiv:2401.09497v1` (`2024-01-17`), Section 5, Conjecture 5.2 (`\label{conj:1 at end}`)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-3` PASS `2026-11-27T09:20Z`), cmd `.venv/bin/python targets/garrison-2401.09497-conj5.2/notes/check-check-1.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2401.09497 "Garrison"`):** Only `AlexenderSokolov__cross-theory-formal-database.json:27906` (`editable-corpus/licenses/arxiv-2401.09497-CC-BY-4.0.txt`, license notice only) and an unrelated OEIS `A...` credit to T. Garrison in `erdos-frontier-atlas`; `0` settlement hits across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2511.22346,2603.19554,2401.09497`):** `2401.09497v1` (`2024-01-17T05:11:33Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2401.09497&size=5`):** `0` hits.

## Coverage Limits
- Live `gh search` was not re-queried after the `09:17Z` GitHub Search API rate limit; mitigated by `608`-file `watch/snapshots/**` grep (`1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`) plus live arXiv and Zenodo checks confirming status unchanged since Gate 2 (`09:10Z`).
