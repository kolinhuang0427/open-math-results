# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121750/`

- **Checked UTC:** `2026-11-27T09:46Z`
- **Target:** OEIS `A121750` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($a(n)+\dots+(n-3)(n-5)^2a(n-6)=0$ for $n \ge 7$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... A121750 121750`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121750&fmt=json`):** `1` result (`number: 121750`, updated `2024-08-20T11:15:52-04:00`, rev. 13); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121750&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121750"`):** `1` unrelated software issue (`GavinDu/Hephaestus#691`), `0` math hits.
6. **Web search (`"A121747" OR "A121750" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
