# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A119366/`

- **Checked UTC:** `2026-11-27T09:24Z`
- **Target:** OEIS `A119366` — R. J. Mathar (Feb 03, 2025) D-finite recurrence conjecture ($\sum_{j=0}^7 C_j(n)\,a(n-j)=0$ for $n \ge 7$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A119366 119366`):** `1` line (`watch/snapshots/openai-math/lean_index.jsonl:3`, purely inside SHA1 hex `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`); `0` matches for `A119366` across `608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A119366&fmt=json`):** `1` result (`number: 119366`, updated `2025-02-03T09:34:08-05:00`, rev. 7); Mathar's Feb 03, 2025 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A119366"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A119366&size=5`):** `0` hits (`total: 0`).
5. **Live GitHub (`gh search issues "A119366"` & `gh search prs "A119366"`):** `0` hits (`[]`).
6. **Web search (`"A119366" "Mathar" OR "D-finite" OR "Barry"`):** `0` proof hits found.
