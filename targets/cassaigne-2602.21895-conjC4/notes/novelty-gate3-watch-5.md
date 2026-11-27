# Gate 3 Novelty Receipt (`watch-5`, refreshed) — `targets/cassaigne-2602.21895-conjC4/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (`STILL-OPEN` per `targets/cassaigne-2602.21895-conjC4/notes/contest-ruling-audit-2.md`)
- **Target Scope:** Julien Cassaigne, Bastián Espinoza, Michel Rigo, and Manon Stipulanti, `arXiv:2602.21895v1` (`2026-02-25`), Dekking Conjecture `(C_4)` for $\mathbf{t}'$ and $\mathbf{t}_{3/2}$ (existence of all finite factor frequencies and reversal symmetry $\mathrm{freq}(w) = \mathrm{freq}(\widetilde{w})$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py 2602.21895 Cassaigne Dekking 't_{3/2}' --max-per-file 3 --max-total 15`: `15` lines across `8/125` files (arXiv hits reference Cassaigne et al. 2014 on additive cubes; `trureturing` hits are `CassaigneIndexTransport`, `dekking-keane-2022` single-letter frequency; `0` new resolutions of `(C_4)`).
   - Prior `CONTESTED.md` (`trureturing#24005` / `#29075`) already ruled `STILL-OPEN` in `notes/contest-ruling-audit-2.md` (`2026-11-27T08:09Z`), as `#24005`/`#29075` address only Part 1 (existence of $\mu[w]$ in $\mathbf{t}'$) with no public Lean PR and do not address reversal invariance $\mathrm{freq}(w) = \mathrm{freq}(\widetilde{w})$ or rationality.
2. **arXiv 7-category snapshot & citing sweep (`watch/snapshots/arxiv/`):**
   - 1,000 recent arXiv entries: `0` new matches settling `(C_4)`.
   - Citing paper `arXiv:2611.06878` (*"The full Kolakoski shift is topologically transitive"*) does not address $\mathbf{t}_{3/2}$ or `(C_4)`.
3. **Live arXiv API (`tools/arxiv_fetch.py`):**
   - `id_list=['2602.21895']`: confirms `2602.21895v1` (`2026-02-25T13:24:47Z`) remains sole version.
   - `abs:"2602.21895" OR ...`: `total: 0`.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A357448&fmt=json`):**
   - Revision `20`, timestamp `2026-03-04T18:59:14-05:00` (unchanged).

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, or `watch/snapshots/**`.
