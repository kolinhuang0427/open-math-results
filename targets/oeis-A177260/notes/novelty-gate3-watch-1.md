# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A177260/`

- **Checked UTC:** `2026-11-27T09:18Z`
- **Target:** OEIS `A177260` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture (`a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8)` for $n \ge 8$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` PASS), cmd `.venv/bin/python -u targets/oeis-A177260/notes/check-check-3.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A177260`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `08:49Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A177260&fmt=json`):** `1` result (`number: 177260`, updated `2025-11-05T15:22:18-05:00`, rev. 27); Mathar's Jul 26, 2022 recurrence remains marked `Conjecture:`, matching `TARGET.md`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A177260&size=5`):** `0` hits.

## Coverage Limits
- Live GitHub Search API (`gh search issues/prs`) was rate-limited (`HTTP 403`) at `09:17Z`; mitigated by `608`-file `watch/snapshots/**` grep (rebuilt `08:49Z`) plus live OEIS and Zenodo checks confirming status unchanged since Gate 2 (`09:10Z`).
