# Gate 2 Novelty Receipt (`watch-6`) — `targets/ulfarsson-2603.16004-conj1/`

- **Checked UTC:** `2026-11-27T09:57:23Z`
- **Target:** Henning Úlfarsson, `arXiv:2603.16004v1`, Section 2, Conjecture 2.9 (`conj:general-reverse`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2603.16004" "Ulfarsson" "Úlfarsson"`: `trureturing` has `UlfarssonAlternatingMeshBasis.lean` (`ulfarsson2024bisc.md`), and `watch/snapshots/arxiv/citing_papers.md` records `OpenAlex cited_by=0; S2=0` for `2603.16004`; `0` hits for `2603.16004` or `conj:general-reverse` across `618` snapshot files.
- `gh search repos "2603.16004" --limit 5`: `[]`
- `gh search issues "2603.16004" --limit 10`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2603.16004`: `2603.16004v1` (`2026-03-16`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222603.16004%22&size=5`): `0` records.
- `search_web` (`"2603.16004" OR ("Ulfarsson" "Permutations Avoiding Patterns")`): returns only `2603.16004v1`, no general-$k$ proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`618` snapshot files) plus live `gh search repos` and `gh search issues`.
