# Gate 2 Novelty Receipt (`watch-1`): `targets/ackelsberg-2604.12864-ques16.3/`

- **Checked (UTC):** `2026-11-27T11:08:42Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — no prior resolution of Ackelsberg–Richter `arXiv:2604.12864v1` §16.1 Question 16.3 (*Finitary form of Kneser's theorem*) found.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2604.12864" "Question 16.3" "Finitary form of Kneser"`):**
   - `3` lines across `2/651` files (`0.81s`): all refer to `google-deepmind/formal-conjectures` PR `#8236` (Question 16.9 on $d$-essential components only). `0` hits on Question 16.3.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2604.12864`):**
   - `2604.12864v1` (`2026-04-14T15:15:46Z`) remains the sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222604.12864%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2604.12864"`):**
   - `0` issues; `1` PR (`google-deepmind/formal-conjectures#8236`, Question 16.9 only — unrelated to Question 16.3).
5. **Web Search (`search_web`):**
   - `"2604.12864" "Question 16.3" OR "Finitary form of Kneser"` — references only `arXiv:2604.12864v1` itself; no prior counterexample or proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
