# Gate 3 Novelty Receipt (`watch-5`) — `targets/benfield-2407.20048-conj5.3/`

- **Checked UTC:** `2026-11-27T09:17Z`
- **Verdict:** **PASS** (rescoped strictly to **Conjecture 5.3 clause (vi)**; `partial-overlap-still-open` per `targets/benfield-2407.20048-conj5.3/notes/contest-ruling-audit-1.md`, with `CONTESTED.md` covering clause (v) settled in `the-omega-institute/trureturing#9448`/PR `#9451`)
- **Target Scope:** Brennan Benfield and Oliver Lippard, `arXiv:2407.20048v2` (`2025-01-30`), Section 5 Conjecture 5.3 (`\label{finite-orders}`), **clause (vi)** (*"infinite in all other cases"*, refuted by $(a,b) = (3,4)$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py 2407.20048 "finite-orders" "(3,4)" "pisano-order" --max-per-file 5 --max-total 10`: all `10` lines across `4/75` files are unrelated `(3,4)` matches; `the-omega-institute/trureturing` `Problems/pisano-order-range-refutation.md` settles only clause (v), leaving clause (vi) / $(3,4)$ open (`notes/contest-ruling-audit-1.md`).
2. **Live arXiv & OpenAlex / S2 citing check (`tools/arxiv_fetch.py`, `api.openalex.org`, `api.semanticscholar.org`):**
   - `id_list=['2407.20048']` (`max_age=300`): confirms `2407.20048v2` (`2025-01-30T20:24:47Z`) remains latest version.
   - `all:A177260 OR abs:"2407.20048"` (`max_age=300`): `total: 0`.
   - OpenAlex (`cited_by_count: 1`) + S2 citations (`arXiv:2605.24146v1` sumsets mod $p$; `arXiv:2404.08194` fixed points): none addresses Conjecture 5.3 clause (vi).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Semantic Scholar, Zenodo, or `watch/snapshots/**`.
