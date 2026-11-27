# Gate 3 Novelty Receipt (`watch-6`) — `targets/garrison-2401.09497-conj5.2/`

- **Checked UTC:** `2026-11-27T09:23:25Z` (`<1h` before submission)
- **Target:** Garrison–Seiler–Knowles `arXiv:2401.09497v1` Section 5 Conjecture 5.2 (`\label{conj:1 at end}`), all $k \ge 1$
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2401.09497"`: only `AlexenderSokolov__cross-theory-formal-database.json` license file (`editable-corpus/licenses/arxiv-2401.09497-CC-BY-4.0.txt`); `0` general-$k$ proof hits across `608` snapshot files (prior Gate 2 inspection confirmed `ndesmo/leaning` and `rainwangphy/aftd-platform` cover only $k \le 16$ / prime-power $k$).
- `gh search repos "2401.09497" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2401.09497" --limit 10 --json repository,number,title,state,url`: `ndesmo/leaning#21` (`open`, `updated_at: 2026-11-26T06:40:28Z`, `gh api pulls?state=open` = `0`) and `#46` (`closed`, setup/literature pass only).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list ...2401.09497...`: `2401.09497v1` (`2024-01-17`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222401.09497%22&size=5`): `0` records.
- `search_web`: no general-$k$ proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos`, `gh search issues`, and `gh api` on `ndesmo/leaning`.
