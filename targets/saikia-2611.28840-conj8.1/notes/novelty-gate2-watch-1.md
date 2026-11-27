# Novelty Gate 2 Receipt — `targets/saikia-2611.28840-conj8.1`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T16:06:38Z`
- **Verdict:** **PASS — OPEN (no full settlement for all $k \ge 3$ found; `trureturing#34564` verified only $12 \le k \le 32$)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `739` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.28840" "Saikia" "conj:sharp" --max-per-file 5 --max-total 60`
   - Result: `18` lines across `9/739` files — none settling Conjecture 8.1:
     - `the-omega-institute__trureturing/issues_and_prs.txt:341`: `trureturing#34564` (*Preregister: test Saikia Conjecture 8.1 by exact scaled transfer*).
     - `arxiv/{arxiv_submissions.*,citing_papers.*,last_sweep_report.*,state.json}` (`OpenAlex cited_by=0; S2=0`).
     - `hexagonmath-index.md:5583`: unrelated earlier Saikia paper (`2610.00469`).

2. **Live GitHub (`2026-11-27T16:06Z`):**
   - `gh api repos/the-omega-institute/trureturing/issues/34564` & `.../comments`: verified `#34564` (`2026-11-26T17:50Z`) ran a finite scaled-transfer verification for $12 \le k \le 32$ and explicitly concludes *"The conjecture for k >= 33 remains open."*
   - `gh search prs "2611.28840"` -> `0`; `gh search issues "2611.28840"` -> `0` (indexed separately under `#34564`); `gh search prs/code` in `the-omega-institute/trureturing` for `34564 / Saikia / 2611.28840` -> `0` matches; `the-omega-institute/trureturing-experiments` `main` (`0b36cef6`, `truncated: false`) -> `0` path/code matches for `2611.28840 / Saikia / 34564 / pdo`.
   - `gh search code "2611.28840"` -> `13` matches: `jmadeiros/conjecture-desk` (notes `2611.28840` is about $\mathrm{PDO}_t$, unrelated to Yaqubi–Mirzavaziri), `raghavs1729/Research-Math` (`not attempted (budget)`), daily arXiv RSS/mirror feeds, and 2 unrelated numeric logs.

3. **Live Zenodo, arXiv, HexagonMath, Web (`2026-11-27T16:06Z`):**
   - Zenodo API (`q=2611.28840`): `0` hits.
   - arXiv API (`id_list=2611.28840`): sole version remains `arXiv:2611.28840v1` (`2026-11-21T14:45:07Z`).
   - `https://hexagonmath.org/abs/2611.28840`: HTTP `404`.
   - `search_web`: only `arXiv:2611.28840v1` itself surfaced; no proof for all $k \ge 3$.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs remained rate-limited externally (mitigated by snapshot `citing_papers.md` `cited_by=0`). Independent Gate 3 freshness check remains required before `RESULTS.md` publication.
