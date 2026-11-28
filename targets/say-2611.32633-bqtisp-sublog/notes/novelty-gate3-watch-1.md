# Gate 3 Novelty Receipt — `targets/say-2611.32633-bqtisp-sublog/` (`watch-1`)

- **Target:** `targets/say-2611.32633-bqtisp-sublog/` (*Lower space bounds for polynomial-time quantum computation*, A. C. Cem Say, `arXiv:2611.32633v1` [`cs.CC`], §5 `main.tex` L1924–1928: extending `thm:hier` to general $s(n) \in \omega(\log\log n) \cap o(\log n)$)
- **Checked At (UTC):** `2026-11-27T23:14:36Z`–`2026-11-27T23:15:03Z` (extending Gate 2 at `21:33:11Z`)
- **Verdict:** **PASS** (novel; `0` prior resolutions found)

## Exact Checks Run & Observed Results

1. **Snapshot grep (from Gate 2):** `7` lines across `3/855` files in `watch/snapshots/arxiv/` announcing `2611.32633v1` only (`0` settlements).
2. **GitHub PRs / Issues / Code Search (`23:14:36Z`):**
   - `gh search prs "2611.32633"` -> `[]`
   - `gh search issues "2611.32633"` -> `[]`
   - `gh search code '"BQTISP"'` -> `[]`
3. **Live `1337isnot1337/solved-conjectures` HEADs (`23:14:36Z`):**
   - `main`: `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (unchanged).
   - `research`: `6394896b8ce946a4fb2faa5ba856091bb7bb5726` (*"Forbid upper cube stars around every maximum dissociated basis"*) — unrelated.
4. **arXiv / Zenodo / ECCC / Web Search (`23:14:36Z`–`23:15:03Z`):**
   - arXiv API (`id_list=2611.32633`): sole version `2611.32633v1` (`2026-11-24T13:54:27Z`).
   - Zenodo API (`q=2611.32633`): `0` hits.
   - `search_web` (`site:eccc.weizmann.ac.il` and general web): returns only `arXiv:2611.32633v1` / `researchradar.org` mirror (`0` ECCC hits, `0` follow-up separations for general $s(n) \in \omega(\log\log n) \cap o(\log n)$).
5. **Independent Check Execution (`#2119`):**
   - Command: `.venv/bin/python -u targets/say-2611.32633-bqtisp-sublog/notes/check-check-1.py`
   - Exit status: `0`
   - Stdout:
     - `LEMMA1_EXACT: k=1..5000 string_len_ok=True, k=128..35000 bounds_ok=True`
     - `FAMILY_sqrt_log: PASS`
     - `FAMILY_three_quarter_log: PASS`
     - `FAMILY_log_div_loglog: PASS`
     - `FAMILY_loglog_mul_logloglog: PASS`
     - `PASS`
