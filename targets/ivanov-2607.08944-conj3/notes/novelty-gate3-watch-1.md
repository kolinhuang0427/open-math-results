# Gate 3 Novelty Receipt (`watch-1`): `targets/ivanov-2607.08944-conj3/`

- **Checked UTC:** `2026-11-27T10:14:48Z`–`2026-11-27T10:15:01Z` (post-`AUDIT.md` re-audit PASS)
- **Target:** Illya Ivanov, *"Illuminating Primitive Polytopes"*, `arXiv:2607.08944v1` (`2026-07-09`), Section 1.4, Conjecture 6 (`\label{conj:fleanverts}`, refuted by 24-facet primitive 13-polytope with $8704 > 2^{13} = 8192$ vertices)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "2607.08944" "Ivanov" "fleanverts"`):** Only `watch/snapshots/arxiv/{citing_papers.json,citing_papers.md}` indexing `2607.08944` (`OpenAlex cited_by=0; S2=0`), plus unrelated `Ivanov`/`Ivanova` hits (`plasma-ai__erdos` Khadzhiivanov, Asao–Ivanov distance algebras, biological/group papers). `0` hits in `1337isnot1337/solved-conjectures`, `trureturing*`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list "2609.32450,2607.08944"`):** Sole version remains `2607.08944v1` (`2026-07-09T21:14:37Z`).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2607.08944&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs "2607.08944"`):** `0` issues, `0` PRs. (Prior Gate 1 check noted `LeeMarshall1113/ai-math-results` and `MColbrook/AIM` cite only Theorem 2 on illumination, not `conj:fleanverts`.)
5. **Web search (`"2607.08944" OR ("Ivanov" "fleanverts" OR "Conjecture 6" "vertices" "polytope")`): `0` competing refutations or settlements found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot was last synced at `2026-11-27T09:50:27Z` (Sweep 25, ~24 min before this check); live `gh search issues/prs` at `10:14Z` showed no new GitHub matches.
