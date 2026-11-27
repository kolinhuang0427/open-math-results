# Gate 3 Novelty Receipt (`watch-1`): `targets/schwob-2606.12129-conj8.7/`

- **Checked (UTC):** `2026-11-27T11:16:49Z`
- **Checker:** `watch-1` (snapshot corpus: `651` files)
- **Result:** **PASS** — no prior proof or settlement of Ludovic Schwob `arXiv:2606.12129v1` §8 Conjecture 8.7 (`\label{cnj:Dtype}`) found.
- **Audit Target:** `targets/schwob-2606.12129-conj8.7/AUDIT.md` (`@audit-1`, re-audit `PASS` after `#1005`/`#1050` fixes); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2606.12129" "cnj:Dtype" "Schwob"`):**
   - `3` lines across `2/651` files (`1.01s`): only `watch/snapshots/arxiv/citing_papers.{json,md}` recording `arXiv:2606.12129` (`OpenAlex cited_by=0; S2=0`). `0` settlement hits.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2606.12129`):**
   - `2606.12129v1` (`2026-06-10T14:22:22Z`) remains the sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222606.12129%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2606.12129"`):**
   - `1` closed issue (`the-omega-institute/trureturing#22269`, Liang–Sagan 2026 Question 8.6(a) on `Pin_n(\sigma)` — unrelated); `0` PRs.
5. **Web Search (`search_web`):**
   - `"2606.12129" OR "Schwob" "Conjecture 8.7" OR "cnj:Dtype" "middle order" proof` — references only `arXiv:2606.12129v1` itself; Conjecture 8.7 remains open.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
