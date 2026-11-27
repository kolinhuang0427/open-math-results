# Gate 2 Novelty Receipt (`watch-1`): `targets/mirzavaziri-2610.19249-conj1/`

- **Checked UTC:** `2026-11-27T10:30:21Z`–`2026-11-27T10:31:45Z`
- **Target:** Guo–Krattenthaler Conjecture 7.4 (`arXiv:1301.7651v3`, `conj:GK`) & Mirzavaziri–Yaqubi Conjecture 2 (`arXiv:2610.19249v1`, Section 3 `conj:general`: nonnegativity except $q^1, q^{5m^2-5m+3}$ for $m \in \{5\} \cup \{m \ge 9 : m \not\equiv 2,3 \pmod 5\}$; `conj:almost` explicitly excluded)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "2610.19249" "Mirzavaziri"` & `trureturing` inspection):**
   - `the-omega-institute/trureturing#21322` / `Problems/mirzavaziri-yaqubi-2026-gaussian-quotient-monotonicity-problem-7-2.md` / `MirzavaziriYaqubiMonotonicityRefutation.lean` addresses **Problem 7.2 only** (refuting the general $(N, k, a, b)$ monotonicity-sufficiency implication), **not** `conj:GK` or `conj:general`.
   - `watch/snapshots/arxiv/citing_papers.md` (`arXiv:1301.7651` cited by `2610.19249`; `2610.19249` `cited_by=0`), `tamnd/arxiv` (census index), and `MirzavaziriYaqubi8` / `YaqubiMirzavaziriPDO` are unrelated; `0` hits settling `conj:GK` or `conj:general` across `619` snapshot files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2610.19249"`):** Sole version remains `2610.19249v1` (`2026-10-13T22:05:49Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2610.19249&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "2610.19249"`):** Only `the-omega-institute/trureturing#21322` (Problem 7.2); `0` PRs and `0` repos.
5. **Web search (`"2610.19249" OR ("Mirzavaziri" "Krattenthaler" OR "Guo" "Conjecture")`): `0` subsequent proofs closing $[301, 10^{30})$ found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:30Z` returned no hits on `conj:GK` or `conj:general`.
