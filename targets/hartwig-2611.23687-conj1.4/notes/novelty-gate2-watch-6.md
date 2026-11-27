# Gate 2 Novelty Receipt (`watch-6`) — `targets/hartwig-2611.23687-conj1.4/`

- **Checked UTC:** `2026-11-27T09:42:48Z`
- **Target:** Hartwig–Shrivastava, `arXiv:2611.23687v1` (*Extremal Projectors and the Virasoro Algebra*), Section 1, Conjecture 1.4 (`conj_denominator_N-truncated`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py ... "2611.23687" "Hartwig"`: hits only `watch/snapshots/arxiv/` submission index (`2611.23687v1`); `0` proof hits across `608` snapshot files.
- `gh search repos "2611.23687" --limit 5`: `[]`
- `gh search issues "2611.23687" --limit 10`: `[]`
- `gh api "repos/sagarsmaths-afk/Virasoro-Extremal-Projector"`: authors' companion symbolic repo (`pushed_at: 2026-11-07T00:02:50Z`, prior to `2611.23687v1` submission, checks up to $N=6$ only).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2611.23687`: `2611.23687v1` (`2026-11-18`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222611.23687%22&size=5`): `0` records.
- `search_web` (`"Extremal Projectors and the Virasoro Algebra" "Hartwig" "Shrivastava"`): returns only `2611.23687v1`, no general-$N$ proof found.

## Coverage Limits
- `gh search code "2611.23687"` hit HTTP 429 rate limit (`try again in 163.8s`); GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files), live `gh search repos/issues`, and `gh api` on `sagarsmaths-afk/Virasoro-Extremal-Projector`.
