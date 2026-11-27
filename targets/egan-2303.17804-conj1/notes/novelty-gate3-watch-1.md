# Gate 3 Novelty Receipt (`watch-1`): `targets/egan-2303.17804-conj1/`

- **Checked (UTC):** `2026-11-27T11:22:56Z`
- **Checker:** `watch-1` (snapshot corpus: `653` files)
- **Result:** **PASS** — no prior proof or settlement of Egan–Nikolayevsky `arXiv:2303.17804v1` Conjecture 1 found.
- **Audit Target:** `targets/egan-2303.17804-conj1/AUDIT.md` (`@audit-2`, re-audit `PASS` after `#1052` patches); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots "2303.17804" "Nikolayevsky"`):**
   - `7` lines across `4/653` files: `1337-solved-conjectures/closed_issues.md:158` (Annor–Nikolayevsky–Payne `arXiv:2412.19560`, unrelated planar curvature problem) and `watch/snapshots/arxiv/{citing_papers.json,citing_papers.md,last_sweep_report.json}` noting `arXiv:2311.00110` (*Degree Sequences of Triangular Multigraphs*, already inspected in Gate 2 — multigraphs, leaves simple graph conjecture open). `0` settlement hits.
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2303.17804`):**
   - `2303.17804v1` (`2023-03-31T05:26:45Z`) remains sole and latest arXiv version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222303.17804%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs "2303.17804"`):**
   - `0` issues, `0` PRs.
5. **Web Search (`search_web`):**
   - `"2303.17804" "Egan" "Conjecture 1" OR "planar graphs" coloring proof` — references `arXiv:2303.17804` and multigraph extensions only; no prior proof found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Unpublished manuscripts or paywalled journals not indexed in arXiv/Zenodo/GitHub/web search are outside direct coverage.
