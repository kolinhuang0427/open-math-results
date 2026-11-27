# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A045742/`

- **Checked UTC:** `2026-11-27T09:32Z`
- **Target:** OEIS `A045742` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($\sum_{j=0}^3 C_j(n)\,a(n-j)=0$ for $n \ge 5$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... A045742 045742`):** `0` hits across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A045742&fmt=json`):** `1` result (`number: 45742`, updated `2022-07-26T12:51:11-04:00`, rev. 20); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A045742"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A045742&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A045742"` & `gh search prs "A045742"`):** `0` hits (`[]`).
6. **Web search (`"A045742" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
