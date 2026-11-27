# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A286044/`

- **Checked UTC:** `2026-11-27T05:43:17Z` – `2026-11-27T05:53:04Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A286044/`)
- **Target Scope:** OEIS `A286044` (rev 8, `2026-02-19T22:02:10-05:00`), Velin Yanev's Feb 16 2026 conjecture: $a(n) = b(b(n-2)) - b(b(n-3))$ for $n > 3$, where $b = \mathrm{A003160}$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 522 files):**
   - `.venv/bin/python tools/novelty_grep.py "A286044" "Velin Yanev" "b(b(n - 2))" "011->0"`
   - Result: 2 matches: `joaquimmj__oeis-conjectures/files.txt` (`conjectures/phase0/A286044.txt`, verified via `gh api` to contain only the OEIS entry dump) and `trureturing-tools.json` (`A034448` unitary sigma, unrelated).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `all:A286044`: `0` results.
   - `all:"Velin Yanev" AND all:A003160`: `0` results.
   - `all:"A003160"`: `0` results.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A286044&fmt=json`):**
   - Revision `8`, timestamp `2026-02-19T22:02:10-05:00`; formula line still marked `Conjecture: a(n) = b(b(n - 2)) - b(b(n - 3)) for n > 3, where b is A003160. - _Velin Yanev_, Feb 16 2026`.
4. **Zenodo & Crossref:**
   - `https://zenodo.org/api/records?q=A286044&size=10`: `total=0`.
   - `https://api.crossref.org/works?query=A286044&rows=5`: `0` items.
5. **Web Search (`search_web`):**
   - `"A286044" "Yanev"`: only the OEIS `A286044` entry.
6. **GitHub Read-Only Checks (`gh api` trees + `gh search`):**
   - Recursive tree grep (`286044|yanev`) on 15 competing repos: `0` matches on 14 repos; `joaquimmj/oeis-conjectures` had `conjectures/phase0/A286044.txt` (raw OEIS entry) and `conjectures/yanev/{check.py,draft.txt,proof.md}` (inspected via `gh api`: covers 9 Yanev conjectures `A129527, A173614, A023887, A055210, A367865, A090079, A163617, A285385, A179504` — does **not** cover `A286044`).
   - `gh search issues/prs --repo the-omega-institute/trureturing "A286044"`: `0` hits.

## What Was Not Covered
- Closed-access/offline works or private repositories not indexed by OEIS, arXiv, Zenodo, Crossref, GitHub, or web search.
