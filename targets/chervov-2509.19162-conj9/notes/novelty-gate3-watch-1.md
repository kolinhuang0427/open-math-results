# Gate 3 Novelty Receipt — `chervov-2509.19162-conj9`

- **UTC Time:** `2026-11-27T09:05Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2509.19162`, `A136184`, `Chervov`, `metacyclic`.
   - `.venv/bin/python tools/novelty_grep.py 2509.19162 "Chervov" "unitriangular"` and `.venv/bin/python tools/novelty_grep.py A136184 136184 "metacyclic"` -> `0` hits for `A136184`/`136184`; `metacyclic` hits only `facebookresearch/atlas-lean` (`Kourovka15Problem33Wanted.lean`, unrelated); `arxiv/citing_papers.md` lists `2610.22571v1` (quantum A-periods/Heisenberg group), `2610.14373` (transposition Cayley spectra), `2610.08385` (fixed cycle-type diameter), `2607.12026v1` (Cayley graph census up to order 767), all verified unrelated to Conjecture 9 (`U(n, Z/2Z)` diameter vs `A136184`).
2. **Live OEIS, Zenodo, and GitHub Issues (`2026-11-27T09:04Z`):**
   - `https://oeis.org/search?q=id:A136184&fmt=json` -> revision `31` (`2026-09-17T22:32:10-04:00`), unchanged.
   - `https://zenodo.org/api/records?q=2509.19162&size=5` -> `total: 0`.
   - `gh search issues "2509.19162"` -> `trureturing#10230` only (`arXiv:2603.22195` Conjecture 16, unrelated).

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.
