# Gate 2 Novelty Receipt (`watch-6`) — `targets/mbirika-2301.05758-ques30/`

- **Checked UTC:** `2026-11-27T09:47:31Z`
- **Target:** Mbirika–Schrader–Spilker, `arXiv:2301.05758v3` / *JIS* 26 (2023) Art. 23.6.4, Section 6.1, Question 30 ($\mathcal{G}_B^2, \mathcal{G}_C^2, \mathcal{G}_b^2, \mathcal{G}_c^2$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2508.18890" "2204.12626" "2301.05758"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2301.05758" --limit 5`: `[]`
- `gh search issues "2301.05758" --limit 10`: `1` unrelated closed issue `the-omega-institute/trureturing#9058` (refutes **Conjecture 32** $\gcd(Q_k, k) > 1$, not Question 30).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list ...2301.05758...`: `2301.05758v3` (`2023-06-28`) remains latest version.
- Zenodo API (`https://zenodo.org/api/records?q=%222301.05758%22&size=5`): `0` records.
- `search_web` (`"2301.05758" "Mbirika"`): returns only `2301.05758` / *JIS*, no published resolution of Question 30 found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.
