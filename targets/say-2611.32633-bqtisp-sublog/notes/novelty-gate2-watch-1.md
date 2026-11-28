# Gate 2 Novelty Receipt — `targets/say-2611.32633-bqtisp-sublog/` (`watch-1`)

- **Target:** `targets/say-2611.32633-bqtisp-sublog/` (*Lower space bounds for polynomial-time quantum computation*, A. C. Cem Say, `arXiv:2611.32633v1` [`cs.CC`, `quant-ph`], §6 `main.tex` lines 1924–1928: extending `thm:hier` `BQTISP(n^{O(1)}, o(s(n))) \subsetneq BQTISP(n^{O(1)}, O(s(n)))` to general space functions $s(n) \in \omega(\log\log n) \cap o(\log n)$)
- **Checked At (UTC):** `2026-11-27T21:33:11Z`–`2026-11-27T21:33:37Z`
- **Verdict:** **PASS** (novel; `0` prior resolutions extending `thm:hier` to general $s(n) \in \omega(\log\log n) \cap o(\log n)$ found)

## Exact Checks Run & Observed Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.32633" "BQTISP" "Lower space bounds for polynomial-time quantum"`
   - Result: `7` lines across `3/855` files, all in `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` listing `2611.32633v1` itself (`0` settlements or competing proofs).
2. **GitHub PRs / Issues / Code Search:**
   - `gh search prs "2611.32633"` -> `[]`; `gh search issues "2611.32633"` -> `[]`; `gh search code '"2611.32633"'` -> `[]`.
   - `gh search prs '"BQTISP"'` -> `[]`; `gh search issues '"BQTISP"'` -> `[]`; `gh search code '"BQTISP"'` -> `[]`.
3. **Live `1337isnot1337/solved-conjectures` HEADs (`2026-11-27T21:33:11Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `def42811066757799568b970e42ca34e845c0777` (*"Point the one-overlap theorem to the verified local obstruction note"*) — unrelated.
4. **arXiv / Zenodo / Crossref / ECCC / Web Search:**
   - arXiv API (`id_list=2611.32633`): sole version `2611.32633v1` (`2026-11-24T13:54:27Z`).
   - Zenodo API (`q=2611.32633`): `0` hits.
   - Crossref (`query=2611.32633`, `query.title=Lower+space+bounds+for+polynomial-time+quantum+computation`): `0` matching DOIs.
   - `search_web` (incl. `site:eccc.weizmann.ac.il`): returns only `arXiv:2611.32633v1` (and digests `researchradar.org`, `airr.science`, `theory.report`, `themoonlight.io`, `offmedian.com`), Remscrim's prior QTM tradeoff lower bounds, and Say/Yakaryılmaz time hierarchies; `0` follow-up separations for general $s(n) \in \omega(\log\log n) \cap o(\log n)$.
