# Gate 2 Novelty Receipt (`watch-6`) — `targets/saikia-2611.28840-conj8.1/`

- **Target:** Manjil P. Saikia, `arXiv:2611.28840v1` (*"Congruences modulo powers of $2$ and $3$ for Lin's function $\mathrm{PDO}_t(n)$"*, dated `2026-11-21`), Section 8, **Conjecture 8.1** (`\label{conj:sharp}`): for every $k \ge 3$, there exists an odd integer $\lambda_k$ such that $\mathrm{PDO}_{\mathrm{t}}(3\cdot 2^{k+2}n) \equiv 8\lambda_k \mathrm{PDO}_{\mathrm{t}}(3\cdot 2^k n) \pmod{2^{\lfloor 7(k+1)/2 \rfloor}}$ for all $n \ge 0$ (proved with best-possible sharpness).
- **Checked UTC:** `2026-11-27T16:06:34Z` – `2026-11-27T16:07:04Z`
- **Verdict:** **PASS — OPEN** (for general $k \ge 33$; prior computational check `trureturing#34564` covers only finite range $12 \le k \le 32$).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `739` files incl. `hexagonmath-index.md` & `papex-index.md`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.28840 "saikia-2611.28840" "conj:sharp" "PDO_t" "Manjil" --max-per-file 0 --max-total 30` -> `23` lines across `9/739` files: `watch/snapshots/arxiv/` entries (`2611.28840v1`, `OpenAlex cited_by=0; S2=0`), `trureturing#34564` open issue entry, `hexagonmath-index.md` (`2610.00469v1` unrelated theta-series paper by Saikia), and `atlas-lean#10897` (Near $F_k$-Perfect Numbers).
   - `grep -iE "2611\.28840|saikia" watch/snapshots/{hwzw-algebra-number-theory-drafts.md,insorrowmeow-oeis-ids.md,papex-index.md}` -> `0` matches.
2. **Live GitHub (`2026-11-27T16:06Z`–`16:07Z`):**
   - `the-omega-institute/trureturing#34564` (`state: OPEN`, `updatedAt: 2026-11-26T17:50:01Z`, 3 comments inspected via `gh api`): finite verification for $12 \le k \le 32$ only; comment `#7199725016` explicitly concludes *"The conjecture for k ≥ 33 remains open."*
   - `gh search prs --repo the-omega-institute/trureturing 34564` -> `[]`; `gh search prs --repo the-omega-institute/trureturing Saikia` -> `#8718` only (unrelated governance).
   - `the-omega-institute/trureturing` `dev` tree (`2611|28840|saikia|PDO`) -> `0` matches (`Q9SharpDoubleFiveCover` unrelated).
   - `the-omega-institute/trureturing-experiments` `main` tree (`2611|28840|saikia|PDO`) -> `0` matches (`a372611` substring only).
   - `gh search code '"2611.28840"'` -> only `koutya0akari/arxiv-plug-in-for-mixi2` & `yizhuan/research-radar` automated feeds; `gh search repos`, `issues`, `prs` for `2611.28840` -> `[]`.
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:06Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.28840` -> `2611.28840v1` (`published 2026-11-21T14:45:07Z`, `updated 2026-11-21T14:45:07Z`) sole version.
   - `https://zenodo.org/api/records?q=2611.28840` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works` (`q=Saikia`, `q=2611.28840`, `q=PDO`) -> `0` relevant hits (`1` unrelated `2610.00469`).
   - `search_web` -> no settlement of `2611.28840` Conjecture 8.1 found (returns `arXiv:2611.28840` and an unrelated Nipen Saikia overpartition paper).

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs are rate-limited externally.
- Independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` entry.
