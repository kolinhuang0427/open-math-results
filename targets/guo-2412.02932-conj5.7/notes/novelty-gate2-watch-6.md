# Gate 2 Novelty Receipt (`watch-6`) — `targets/guo-2412.02932-conj5.7/`

- **Checked UTC:** `2026-11-27T09:53:50Z`
- **Target:** Guo–Lin, `arXiv:2412.02932v1` (*Schubert polynomials and patterns in permutations*), Section 5.2, Conjecture 5.7 (`locond-3`, $d_u \in \mathbb{Z}_{\ge 0}$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2412.02932" "134562897" "theta_u"`: `3` lines across `2/618` snapshot files — `watch/snapshots/arxiv/citing_papers.json` and `jhparkerb__polyplets` `experiments/theta_universality.py` (`0` hits for `2412.02932`, `134562897`, or Conjecture 5.7).
- `gh search repos "2412.02932" --limit 5`: `[]`
- `gh search issues "2412.02932" --limit 10`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2412.02932`: `2412.02932v1` (`2024-12-04`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222412.02932%22&size=5`): `0` records.
- `search_web` (`"2412.02932" OR ...`): returns only `2412.02932`, no refutation found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`618` snapshot files) plus live `gh search repos` and `gh search issues`.
