# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A121754/`

- **Checked UTC:** `2026-11-27T10:02Z`
- **Target:** OEIS `A121754` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($16(n+1)a(n)+\dots+(130n-311)(n-6)(n-4)^2a(n-5)=0$ for $n \ge 6$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-3` re-audit PASS `2026-11-27T09:59Z`), cmd `.venv/bin/python targets/oeis-A121754/notes/check-check-1.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121754` at `10:02Z`):** `0` lines across `0/618` files (including `1337isnot1337/solved-conjectures` rebuilt `09:50:27Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live GitHub (`gh search issues "A121754"` & `gh search prs "A121754"` at `10:02Z`):** `0` hits (`[]`).
3. **Live OEIS (`https://oeis.org/search?q=id:A121754&fmt=json` at `10:02Z`):** `1` result (`number: 121754`, updated `2022-07-26T11:32:34-04:00`, rev. 4, `Conjecture`, matching `TARGET.md`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121754&size=5` at `10:02Z`):** `0` hits (`total: 0`).
