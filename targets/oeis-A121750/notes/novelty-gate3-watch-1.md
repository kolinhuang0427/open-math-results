# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A121750/`

- **Checked UTC:** `2026-11-27T10:06Z`
- **Target:** OEIS `A121750` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($a(n)+\dots+(n-3)(n-5)^2a(n-6)=0$ for $n \ge 7$)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` re-audit PASS), cmd `.venv/bin/python -u targets/oeis-A121750/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2603.16004 A121750` at `10:06Z`):** `0` hits for `A121750` across `618` files (including `1337isnot1337/solved-conjectures` rebuilt `09:50:27Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live GitHub (`gh search issues "A121750"` at `10:06Z`):** `1` unrelated software issue (`GavinDu/Hephaestus#691`), `0` math hits.
3. **Live OEIS (`https://oeis.org/search?q=id:A121750&fmt=json` at `10:06Z`):** `1` result (`number: 121750`, updated `2024-08-20T11:15:52-04:00`, rev. 13, `Conjecture`, matching `TARGET.md`).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121750&size=5` at `10:06Z`):** `0` hits (`total: 0`).
