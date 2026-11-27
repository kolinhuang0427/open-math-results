# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/saikia-2611.28840-conj8.1/`

- **Target:** Manjil P. Saikia, `arXiv:2611.28840v1` (*"Congruences modulo powers of $2$ and $3$ for Lin's function $\mathrm{PDO}_t(n)$"*, submitted `2026-11-21`), Section 8, **Conjecture 8.1** (`\label{conj:sharp}`) & exact best-possible sharpness of modulus $2^{\lfloor 7(k+1)/2 \rfloor}$ for all $k \ge 3$.
- **Checked UTC:** `2026-11-27T16:17:24Z` – `2026-11-27T16:17:33Z` (after `#1665` blind audit PASS, immediately prior to `RESULTS.md` publication)
- **Verdict:** **PASS — OPEN** (for general $k \ge 33$; prior computational check `trureturing#34564` covers only finite range $12 \le k \le 32$).

## Fresh `<1h` Queries & Findings

1. **Local Snapshot Index (`watch/snapshots/`, `742` indexed files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.28840 "saikia-2611.28840" "conj:sharp" "PDO_t" --max-per-file 0 --max-total 30` -> `25` lines across `8/742` files: `watch/snapshots/arxiv/` entries (`2611.28840v1`, `OpenAlex cited_by=0; S2=0`), `trureturing#34564` open issue entry, and `watch/snapshots/raghav-research-math-index.md` (`CANDIDATES.md` explicitly lists `2611.28840` as `not attempted (budget)`, `NOVELTY-1/2.md` only cite it as unrelated `PDO_t` background).
   - `jmadeiros/conjecture-desk`: cites `2611.28840` only as unrelated `PDO_t` background in `yaqubi-mirzavaziri/conj-6.{2,3-6.4}/REVIEW.md`.
2. **Live GitHub (`2026-11-27T16:17Z`):**
   - `gh search code '"2611.28840"'` -> only `koutya0akari/arxiv-plug-in-for-mixi2` & `yizhuan/research-radar` automated feeds.
   - `gh search repos "2611.28840"`, `gh search issues "2611.28840"`, `gh search prs "2611.28840"` -> `[]` on all three.
   - `gh issue view 34564 -R the-omega-institute/trureturing`: still `OPEN`, `updatedAt: 2026-11-26T17:50:01Z` (finite check $12 \le k \le 32$ only, explicitly leaves $k \ge 33$ open); `gh search prs --repo the-omega-institute/trureturing 34564` -> `[]`.
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:17Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.28840` -> `2611.28840v1` (`published 2026-11-21T14:45:07Z`) remains the sole version.
   - `https://zenodo.org/api/records?q=2611.28840` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works?q=2611.28840` & `q=PDO` -> `0` hits (`HEX 2611.28840 0`, `HEX PDO 0`).
   - `search_web` (`"2611.28840" "conj:sharp" OR ("2611.28840" "Conjecture 8.1" "proof")`) -> `0` settlements found.

## Verification Command & Artifacts

- **Check command:** `.venv/bin/python -u targets/saikia-2611.28840-conj8.1/notes/check-check-3.py` (verified `PASS` in `AUDIT.md` `#1665`)
- **Paths:** `targets/saikia-2611.28840-conj8.1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
