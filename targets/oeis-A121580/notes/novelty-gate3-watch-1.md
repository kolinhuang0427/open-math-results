# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A121580/`

- **Checked UTC:** `2026-11-27T09:37Z`
- **Target:** OEIS `A121580` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($a(n)+(-n-4)a(n-1)+3(n+1)a(n-2)+2(-2n+3)a(n-3)+2(n-3)a(n-4)=0$ for $n \ge 5$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-2` PASS `2026-11-27T09:37Z`), cmd `.venv/bin/python targets/oeis-A121580/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121580 A121584` at `09:37Z`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live GitHub (`gh search issues "A121580"` at `09:37Z`):** `0` hits (`[]`).
3. **Live OEIS (`https://oeis.org/search?q=id:A121580&fmt=json` at `09:37Z`):** `1` result (`number: 121580`, updated `2024-09-15T07:13:47-04:00`, rev. 12, `Conjecture`, matching `TARGET.md`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121580&size=5` at `09:37Z`):** `0` hits (`total: 0`).
