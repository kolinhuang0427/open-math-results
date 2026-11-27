# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121584/`

- **Checked UTC:** `2026-11-27T09:34Z`
- **Target:** OEIS `A121584` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($14(-n+1)a(n)+\dots+2(1071n-3433)(n-4)a(n-5)=0$ for $n \ge 6$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121584 121584`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121584&fmt=json`):** `1` result (`number: 121584`, updated `2022-07-26T11:38:40-04:00`, rev. 4); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121584"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121584&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121584"` & `gh search prs "A121584"`):** `0` issue hits (`[]`), `1` unrelated PR (`getsentry/sentry-java#1899`).
6. **Web search (`"A121584" "Mathar" OR "D-finite" OR "deco polyominoes"`):** `0` proof hits found.
