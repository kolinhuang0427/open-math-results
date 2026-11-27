# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A121752/`

- **Checked UTC:** `2026-11-27T10:04Z`
- **Target:** OEIS `A121752` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($(-460n+1223)a(n)+\dots-2(426n-1111)(n-6)(n-4)^2a(n-5)=0$ for $n \ge 6$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` re-audit PASS), cmd `.venv/bin/python targets/oeis-A121752/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121752 A121747` at `10:04Z`):** `0` lines across `0/618` files (including `1337isnot1337/solved-conjectures` rebuilt `09:50:27Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live GitHub (`gh search issues "A121752"` at `10:04Z`):** `0` hits (`[]`).
3. **Live OEIS (`https://oeis.org/search?q=id:A121752&fmt=json` at `10:04Z`):** `1` result (`number: 121752`, updated `2022-07-26T11:29:39-04:00`, rev. 4, `Conjecture`, matching `TARGET.md`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121752&size=5` at `10:04Z`):** `0` hits (`total: 0`).
