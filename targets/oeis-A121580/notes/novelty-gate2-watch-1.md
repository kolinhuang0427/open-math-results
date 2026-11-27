# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A121580/`

- **Checked UTC:** `2026-11-27T09:30Z`
- **Target:** OEIS `A121580` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($a(n)+(-n-4)a(n-1)+3(n+1)a(n-2)+2(-2n+3)a(n-3)+2(n-3)a(n-4)=0$ for $n \ge 5$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121580 121580`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A121580&fmt=json`):** `1` result (`number: 121580`, updated `2024-09-15T07:13:47-04:00`, rev. 12); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A121580"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A121580&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A121580"` & `gh search prs "A121580"`):** `0` hits (`[]`).
6. **Web search (`"A121580" "Mathar" OR "D-finite" OR "recurrence" OR "OEIS"`):** `0` proofs found.
