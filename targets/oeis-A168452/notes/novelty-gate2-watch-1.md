# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A168452/`

- **Checked UTC:** `2026-11-27T09:24Z`
- **Target:** OEIS `A168452` — R. J. Mathar (Nov 22, 2024) D-finite recurrence conjecture ($\sum_{j=0}^4 C_j(n)\,a(n-j)=0$ for $n \ge 4$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A168452 ...`):** `0` hits for `A168452` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A168452&fmt=json`):** `1` result (`number: 168452`, updated `2024-11-22T06:23:47-05:00`, rev. 14); Mathar's Nov 22, 2024 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A168452"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A168452&size=5`):** `0` hits (`total: 0`).
5. **Web search (`"A168452" "Mathar" OR "D-finite" OR "Self-convolution"`):** `0` proofs found.
