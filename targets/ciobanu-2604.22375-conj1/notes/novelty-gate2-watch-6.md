# Gate 2 Novelty Receipt (`watch-6`) — `targets/ciobanu-2604.22375-conj1/`

- **Checked UTC:** `2026-11-27T09:50:56Z`
- **Target:** Ciobanu–Turaev, `arXiv:2604.22375v1` (*Visibly Pushdown Languages in Groups*), Section 4.1, Conjecture 1 (`conjecture1`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2604.22375" "Ciobanu" "VPL"`: `0` hits across `617` snapshot files (`VPL` only triggers unrelated substring false positives).
- `gh search repos "2604.22375" --limit 5`: `[]`
- `gh search issues "2604.22375" --limit 10`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2604.22375`: `2604.22375v1` (`2026-04-24`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222604.22375%22&size=5`): `0` records.
- `search_web` (`"2604.22375" OR ("Ciobanu" "VPL" "REG" "conj1" OR "Conjecture")`): returns only `2604.22375`, no proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown (Gate 1 checked `gh search code` at `09:44Z`, finding only arXiv RSS/listing repos); GitHub coverage relies on `watch/snapshots/discovered/` (`617` total snapshot files) plus live `gh search repos` and `gh search issues`.
