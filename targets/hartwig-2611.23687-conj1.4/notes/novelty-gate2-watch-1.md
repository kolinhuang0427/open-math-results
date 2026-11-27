# Gate 2 Novelty Receipt (`watch-1`): `targets/hartwig-2611.23687-conj1.4/`

- **Checked UTC:** `2026-11-27T09:42Z`
- **Target:** Jonas T. Hartwig and Sagar Shrivastava, *"Extremal Projectors and the Virasoro Algebra"*, `arXiv:2611.23687v1` (`2026-11-18`), Section 1, Conjecture 1.4 (`\label{conj_denominator_N-truncated}`)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2611.23687 Hartwig ...`):** `7` lines across `3/608` files — only `watch/snapshots/arxiv/arxiv_submissions.{json,md}` and `state.json` indexing `2611.23687v1` itself; `0` hits in `1337isnot1337/solved-conjectures` (`09:19:40Z` rebuild), `the-omega-institute/trureturing*`, `openai/math`, or `formal-conjectures`.
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2611.23687,2402.15372`):** `2611.23687v1` (`2026-11-18T01:23:31Z`) remains the sole arXiv version.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2611.23687&size=5`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues "2611.23687"` & `gh search prs "2611.23687"`):** `0` hits (`[]`). (Companion repo `sagarsmaths-afk/Virasoro-Extremal-Projector` verified in Gate 1 to cover only symbolic checks for $N \le 6$.)
5. **Web search (`"2611.23687" OR ("Hartwig" "Conjecture 1.4" "Kac")`): `0` settlements found.
