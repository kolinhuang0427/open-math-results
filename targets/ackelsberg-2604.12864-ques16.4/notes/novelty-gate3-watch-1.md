# Gate 3 Novelty Receipt (`watch-1`): `targets/ackelsberg-2604.12864-ques16.4/`

- **Checked (UTC):** `2026-11-27T11:14:52Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — no prior resolution of Ackelsberg–Richter `arXiv:2604.12864v1` §16.1 Question 16.4 (*Kneser's theorem in $\mathbb{N}^2$*) found.
- **Audit Target:** `targets/ackelsberg-2604.12864-ques16.4/AUDIT.md` (`@audit-2`, `PASS`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2604.12864" "Question 16.4"`):**
   - `3` lines across `2/651` files (`1.10s`): `google-deepmind/formal-conjectures` PR `#8236` (Question 16.9 on $d$-essential components only). `0` hits on Question 16.4.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2604.12864`):**
   - `2604.12864v1` (`2026-04-14T15:15:46Z`) remains the sole and latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222604.12864%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2604.12864"`):**
   - `0` issues; `1` PR (`google-deepmind/formal-conjectures#8236`, Question 16.9 only).

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
