# Gate 3 Novelty Receipt (`watch-1`): `targets/mbirika-2204.12626-ques6.1/`

- **Checked UTC:** `2026-11-27T09:48Z`
- **Target:** aBa Mbirika and Jürgen Spilker, *"GCD of sums of $k$ consecutive squares of generalized Fibonacci numbers"*, `arXiv:2204.12626v2` (`2023-01-13`, *Fibonacci Quarterly* 60(5) (2022), 255–269), Section 6, Question 6.1 ($\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$)
- **Audited Artifacts Verified:** `TARGET.md`, `COUNTEREXAMPLE.md`, `AUDIT.md` (`@audit-2` PASS `2026-11-27T09:45Z`), cmd `.venv/bin/python targets/mbirika-2204.12626-ques6.1/notes/check-check-1.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2204.12626 2301.05758` at `09:47Z`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2204.12626,2301.05758` at `09:47Z`):** `2204.12626v2` (`2023-01-13T22:18:59Z`) remains latest.
3. **Live GitHub (`gh search issues "2204.12626"` & `trureturing/files.txt` at `09:47Z`):** Only `trureturing#22988` (`state: open`, Question 6.2 scaling only; `Problems/mbirika-spilker-gibonacci-power-gcd-normalization.md` excludes Question 6.1).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2204.12626&size=5` at `09:47Z`):** `0` hits (`total: 0`).
