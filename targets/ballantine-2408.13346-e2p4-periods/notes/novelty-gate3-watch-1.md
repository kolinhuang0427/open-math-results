# Gate 3 Novelty Receipt (`watch-1`): `targets/ballantine-2408.13346-e2p4-periods/`

- **Checked UTC:** `2026-11-27T09:29Z`
- **Target:** Cristina Ballantine, George Beck, and Mircea Merca, *"Partitions and elementary symmetric polynomials -- an experimental approach"*, `arXiv:2408.13346v1` (`2024-08-23`), Section 1, conjectural table of minimal periods for $e_2p_4(n) \pmod m$ ($m = 10$ giving $1200 \neq 1150$ and $m = 18$ giving $1296 \neq 1246$)
- **Audited Artifacts Verified:** `TARGET.md`, `COUNTEREXAMPLE.md`, `AUDIT.md` (`@audit-3` PASS `2026-11-27T09:29Z`), cmd `.venv/bin/python -u targets/ballantine-2408.13346-e2p4-periods/notes/check-check-3.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2408.13346` at `09:29Z`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2408.13346` at `09:29Z`):** `2408.13346v1` (`2024-08-23T19:41:53Z`) remains the sole arXiv version.
3. **Live GitHub (`gh search issues "2408.13346"` & `gh search prs "2408.13346"` at `09:29Z`):** Only `trureturing#8751` / PR `#8986` / `#9453` (`arXiv:2409.11268` Conjecture 16 refutation), unrelated to `2408.13346`.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2408.13346&size=5` at `09:29Z`):** `0` hits (`total: 0`).

## Coverage Limits
- Published version *The Ramanujan Journal* 66 (2025), Art. 34 (`doi:10.1007/s11139-024-01001-6`) is paywalled and unverified beyond `arXiv:2408.13346v1` (per `AUDIT.md` §1 caveat).
