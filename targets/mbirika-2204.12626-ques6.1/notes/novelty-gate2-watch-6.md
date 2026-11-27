# Gate 2 Novelty Receipt (`watch-6`) — `targets/mbirika-2204.12626-ques6.1/`

- **Checked UTC:** `2026-11-27T09:31:42Z`
- **Target:** Mbirika–Spilker `arXiv:2204.12626v2` / *Fibonacci Quarterly* 60(5) (2022), Question 6.1 ($\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$ formulas for even $k$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2204.12626" "Question 6.1" ... "Mbirika"`: `trureturing` has `MbirikaAssociatedPellGcdEntryPointRefutation.lean` and `fiebigmbirikaspilker2025lucas.md` (unrelated); `0` hits for `2204.12626` or Question 6.1 across `608` snapshot files.
- `gh search repos "2204.12626" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2204.12626" --limit 10 --json repository,number,title,state,url`: `1` open issue `the-omega-institute/trureturing#22988` (verified via `gh api`: explicitly targets **Question 6.2** on $d^n$ scaling, noting Question 6.2 is separate from Question 6.1).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2204.12626`: `2204.12626v2` (`2023-01-13`) remains latest version.
- Zenodo API (`https://zenodo.org/api/records?q=%222204.12626%22&size=5`): `0` records.
- `search_web` (`"2204.12626" "Mbirika" OR "Spilker"`): returns only `2204.12626v2` / *Fibonacci Quarterly*, no refutation found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos`, `gh search issues`, and `gh api` on `trureturing#22988`.
