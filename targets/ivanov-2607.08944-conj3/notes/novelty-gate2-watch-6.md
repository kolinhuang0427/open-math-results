# Gate 2 Novelty Receipt (`watch-6`) — `targets/ivanov-2607.08944-conj3/`

- **Checked UTC:** `2026-11-27T09:41:39Z`
- **Target:** Illya Ivanov, `arXiv:2607.08944v1` (*Illuminating Primitive Polytopes*), Section 1.4, Conjecture 3 (`conj:fleanverts`)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2607.08944" "fleanverts" "Ivanov"`: `0` hits for `2607.08944` or `fleanverts` across `608` snapshot files (only unrelated Asao–Ivanov / author name hits).
- `gh search repos "2607.08944" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2607.08944" --limit 10 --json repository,number,title,state,url`: `[]`
- `gh search code "fleanverts" --limit 5`: `[]`
- `gh search code "2607.08944" --limit 5`: hits `LeeMarshall1113/ai-math-results`, `MColbrook/AIM`, `ehijano/rss_fetch`, and `hyunsung021123/research-agent/data/state.json`. Inspected `LeeMarshall1113/ai-math-results` `results/hadwiger-h3/NOVELTY.md`, `MColbrook/AIM` `research/expansion-2026-09/drafts/hadwiger-boltyanski-illumination.md`, and `hyunsung021123/research-agent` `data/state.json` via `gh api`: the first two cite `2607.08944` solely for Hadwiger–Boltyanski illumination (Theorem 2), and the third is an arXiv ID list; `0` address Conjecture 3 (`conj:fleanverts`).
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2607.08944`: `2607.08944v1` (`2026-07-09`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222607.08944%22&size=5`): `0` records.
- `search_web` (`"2607.08944" OR ("fleanverts" "polytope" "Ivanov") ...`): returns only `2607.08944v1`, no refutation found.

## Coverage Limits
- Closed-access venues or private repositories not indexed by arXiv, GitHub, Zenodo, or `search_web` are not covered.
