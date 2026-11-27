# Gate 3 Novelty Receipt (`watch-1`): `targets/minac-2411.01768-rem5.14/`

- **Checked (UTC):** `2026-11-27T10:57:22Z`
- **Checker:** `watch-1` (post-Sweep 27 snapshot corpus: `635` files)
- **Result:** **PASS** — no prior refutation of Mináč–Nguyen–Tân `arXiv:2411.01768v2` §5.2 Remark 5.14 (`rem:same_degree`) found.
- **Audit Target:** `targets/minac-2411.01768-rem5.14/AUDIT.md` (`@audit-2`, `PASS`); Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md` verified.

## Exact Queries & Results

1. **Snapshot Corpus (`tools/novelty_grep.py --root watch/snapshots` across `635` files):**
   - Queries: `"2411.01768"`, `"rem:same_degree"`, `"same_degree"`, `"gcd-graph"`, `"Mináč"`.
   - Result: `11` lines across `10/635` files — `0` hits for `2411.01768`, `rem:same_degree`, or `same_degree`. All `11` hits are distinct near-misses:
     - `aliromman__math` PR `#88` (Chidambaram–Mináč–Nguyen–Tân equidistribution conjecture for cyclotomic factors of Fekete polynomials).
     - `arXiv:2611.15026v2` (*"Spectra of gcd-graphs over a matrix ring"* by Tung T. Nguyen — matrix rings, not polynomial rings $\mathbb{F}_q[x]$).
     - `arXiv:2409.01929` (*"On the gcd-graphs over polynomial rings"* — citing `arXiv:2307.14896`, earlier paper).
     - `mathesis-papers-org` (`CATALOG.md`, Nguyen–Tân primeness question / cycle).
     - `eliottcassidy2000__math` (`THM-3387-exact-cyclic-sheet-cover-atlas-and-q2-gcd-graph.md` — cyclic sheet cover).
2. **arXiv API (`tools/arxiv_fetch.py query --id-list 2411.01768`):**
   - `2411.01768v2` (`updated: 2026-08-03T02:49:58Z`, to appear in *J. Aust. Math. Soc.*) remains the sole latest version.
3. **Zenodo API (`https://zenodo.org/api/records?q=%222411.01768%22`):**
   - `total: 0`.
4. **GitHub (`gh search issues/prs/repos "2411.01768"`):**
   - `0` issues, `0` PRs, `0` repos.
5. **Web Search (`search_web`):**
   - `"2411.01768" OR "rem:same_degree" "Mináč" OR "Minac" zero-divisor graph counterexample` — confirms `arXiv:2411.01768` existence, zero published counterexamples to Remark 5.14.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot covers `CONTENTS.md`, `HISTORY.md`, `results/` listing, open/closed issues, and open/merged PRs via `gh api` (no full clone).
- Paywalled journals not indexed in arXiv/Zenodo/GitHub/public web results are outside direct coverage.
