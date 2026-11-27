# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121752/`

- **Checked UTC:** `2026-11-27T09:40Z`
- **Target:** OEIS `A121752` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($(-460n+1223)a(n)+\dots-2(426n-1111)(n-6)(n-4)^2a(n-5)=0$ for $n \ge 6$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... A121752 121752`):** `4` lines across `2/608` files (`trureturing-source-theories`), all purely inside SHA256 hex digests; `0` hits for `A121752` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121752&fmt=json`):** `1` result (`number: 121752`, updated `2022-07-26T11:29:39-04:00`, rev. 4); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121754" OR all:"A121752"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121752&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121752"`):** `0` hits (`[]`).
6. **Web search (`"A121752" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
