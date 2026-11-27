# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A121751/`

- **Checked UTC:** `2026-11-27T09:50Z`
- **Target:** OEIS `A121751` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($256a(n)+\dots+(n-4)(n-8)(n^2-12n+31)a(n-6)=0$ for $n \ge 7$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` re-audit PASS), cmd `.venv/bin/python targets/oeis-A121751/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121751 ...` at `09:49Z`):** `0` hits across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live GitHub (`gh search issues "A121751"` at `09:49Z`):** `0` hits (`[]`).
3. **Live OEIS (`https://oeis.org/search?q=id:A121751&fmt=json` at `09:49Z`):** `1` result (`number: 121751`, updated `2022-07-26T11:27:46-04:00`, rev. 5, `Conjecture`, matching `TARGET.md`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121751&size=5` at `09:49Z`):** `0` hits (`total: 0`).
