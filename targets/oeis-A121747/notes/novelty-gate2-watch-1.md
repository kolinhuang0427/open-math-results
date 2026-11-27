# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121747/`

- **Checked UTC:** `2026-11-27T09:46Z`
- **Target:** OEIS `A121747` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($(-9n+38)a(n)+\dots-(19n-15)(n-3)(n-4)^2a(n-5)=0$ for $n \ge 6$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121747 121747 ...`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121747&fmt=json`):** `1` result (`number: 121747`, updated `2024-08-21T12:26:20-04:00`, rev. 15); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121747&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121747"`):** `0` hits (`[]`).
6. **Web search (`"A121747" OR "A121750" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
