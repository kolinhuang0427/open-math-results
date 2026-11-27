# Gate 2 Novelty Receipt (`watch-1`): `targets/ivanov-2607.08944-conj3/`

- **Checked UTC:** `2026-11-27T09:42Z`
- **Target:** Illya Ivanov, *"Illuminating Primitive Polytopes"*, `arXiv:2607.08944v1` (`2026-07-09`), Section 1.4, Conjecture 3 (`\label{conj:fleanverts}`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2607.08944 fleanverts`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2607.08944`):** `2607.08944v1` (`2026-07-09T21:14:37Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2607.08944&size=5` & `fleanverts`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues "2607.08944"` & `gh search prs "2607.08944"`):** `0` hits (`[]`). (Prior `gh search code "2607.08944"` hits in `LeeMarshall1113/ai-math-results` and `MColbrook/AIM` verified in Gate 1 to cite only Theorem 2 on illumination, not `conj:fleanverts`.)
5. **Web search (`"2607.08944" OR ("fleanverts" "polytope") OR ("Ivanov" "2607.08944")`): `0` settlements/refutations of Conjecture 3 found.
