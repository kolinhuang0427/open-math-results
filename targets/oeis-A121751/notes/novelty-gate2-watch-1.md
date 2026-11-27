# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121751/`

- **Checked UTC:** `2026-11-27T09:37Z`
- **Target:** OEIS `A121751` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($256a(n)+\dots+(n-4)(n-8)(n^2-12n+31)a(n-6)=0$ for $n \ge 7$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121751 121751 ...`):** `0` hits for `A121751`/`121751` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121751&fmt=json`):** `1` result (`number: 121751`, updated `2022-07-26T11:27:46-04:00`, rev. 5); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121751"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121751&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121751"` & `gh search prs "A121751"`):** `0` hits (`[]`).
6. **Web search (`"A121751" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
