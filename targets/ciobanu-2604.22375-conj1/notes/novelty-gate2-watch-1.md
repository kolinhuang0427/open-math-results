# Gate 2 Novelty Receipt (`watch-1`): `targets/ciobanu-2604.22375-conj1/`

- **Checked UTC:** `2026-11-27T09:50Z`
- **Target:** Laura Ciobanu and Daniel Turaev, *"Visibly Pushdown Languages in Groups"*, `arXiv:2604.22375v1` (`2026-04-24`, full version of DLT 2026 paper), Section 4.1, Conjecture 1 (`\label{conjecture1}`: $\mathbf{VPL}^\forall = \mathbf{REG}^\forall$ in all groups)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2604.22375 Ciobanu`):** `2` lines (`watch/snapshots/arxiv/citing_papers.json:2618,2626` indexing this target itself); `0` hits in `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2604.22375`):** `2604.22375v1` (`2026-04-24T09:09:08Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2604.22375&size=5`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues "2604.22375"` & `gh search prs "2604.22375"`):** `0` hits (`[]`).
5. **Web search (`"2604.22375" OR ("Ciobanu" "visibly pushdown" OR "VPL")`): `0` settlements found (surfaced only `arXiv:2604.22375` itself).
