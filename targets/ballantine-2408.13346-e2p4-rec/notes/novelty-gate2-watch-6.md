# Gate 2 Novelty Receipt (`watch-6`) — `targets/ballantine-2408.13346-e2p4-rec/`

- **Checked UTC:** `2026-11-27T09:23:25Z`
- **Target:** Ballantine–Beck–Merca `arXiv:2408.13346v1` Section 1 conjectured order-22 linear recurrence for $e_2 p_4(n)$
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2408.13346" "e2p4" "Ballantine"`: hits only `facebookresearch__atlas-lean` (`pull/10666`, Theorem 2 of Ballantine's Merca identities) and `the-omega-institute__trureturing` (`BallantineRegularSymmetricImageRefutation` / `ballantine2024elementary.md` for `arXiv:2409.11268v3` Conjecture 16); `0` hits for `2408.13346` or `e2p4`.
- `gh search repos "2408.13346" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2408.13346" --limit 10 --json repository,number,title,state,url`: `1` unrelated closed issue `the-omega-institute/trureturing#8751` (`arXiv:2409.11268v3` §5 Conjecture 16).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list ...2408.13346...`: `2408.13346v1` (`2024-08-23`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222408.13346%22&size=5`): `0` records.
- `search_web`: no proof of the $e_2 p_4(n)$ recurrence found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.
