# Gate 3 Novelty Receipt (`watch-1`): `targets/ballantine-2408.13346-e2p4-rec/`

- **Checked UTC:** `2026-11-27T09:30Z`
- **Target:** Cristina Ballantine, George Beck, and Mircea Merca, *"Partitions and elementary symmetric polynomials -- an experimental approach"*, `arXiv:2408.13346v1` (`2024-08-23`), Section 1, conjectured order-22 linear recurrence for $e_2p_4(n)$
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` PASS), cmd `.venv/bin/python -u targets/ballantine-2408.13346-e2p4-rec/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2408.13346` at `09:30Z`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Recent live checks (`09:29Z`, `<2 min` prior):**
   - `tools/arxiv_fetch.py query --id-list 2408.13346`: `2408.13346v1` (`2024-08-23T19:41:53Z`) remains sole arXiv version.
   - `gh search issues "2408.13346"` & `gh search prs "2408.13346"`: only `trureturing#8751` / PR `#8986` / `#9453` (`arXiv:2409.11268`), unrelated.
   - Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5`): `0` hits.
