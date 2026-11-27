# Gate 2 Novelty Receipt (`watch-5`) — `targets/garrison-2401.09497-conj5.2/`

- **Checked UTC:** `2026-11-27T09:11Z`
- **Verdict:** **PASS** (no `CONTESTED.md`; general $k$ including composite non-prime-power $k$ remains open)
- **Target Scope:** Thomas Garrison, Chris Seiler, and Andrew Knowles, `arXiv:2401.09497v1` (`2024-01-17`), Section 5 Conjecture 5.2 (`conj:1 at end`): every weakly consecutive permutation $\sigma \colon [k] \to [k]$ satisfies $\sigma(1) = 1$ or $\sigma(k) = 1$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 607 files):**
   - `.venv/bin/python tools/novelty_grep.py 2401.09497 Garrison "weakly consecutive" "WeaklyConsecutive" --max-per-file 5 --max-total 15`: `8` lines across `4/607` files:
     - **Near-miss (`rainwangphy/aftd-platform`):** `WeaklyConsecutiveOneAtEndOfIsPrimePow.lean` proves Conjecture 5.2 **only** for prime-power $k$ (`IsPrimePow k`).
     - **Near-miss (`ndesmo/leaning`):** `halfline_lt/Proofs/WeaklyConsecutive.lean` covers $k \le 16$ (PR `#57`) and prime-power $k$ (PR `#61`, explicitly noting *"gap: composite k"*). Direct live `gh api` check of `ndesmo/leaning` issue `#68` (*"attack Conjecture 5.2 for k with two distinct prime factors"*) confirms it remains `open` (`updated_at: 2026-11-26T23:52:47Z`) with no merged PR for composite $k$.
     - `AlexenderSokolov/cross-theory-formal-database` (license file) and `techno-optimist/erdos-frontier-atlas` (unrelated T. Garrison sequence).
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2508.04602', '2401.09497']` (`max_age=300`): confirms `2401.09497v1` (`2024-01-17T05:11:33Z`) remains sole version.
   - `abs:"2508.04602" OR abs:"2401.09497" OR all:"weakly consecutive"` (`max_age=300`): `total_results: 1` (`2401.09497v1` itself only).
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2401.09497`): `cited_by_count: 0`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2401.09497&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Unpushed local work on `ndesmo/leaning#68`, closed-access venues, or private repositories not indexed by arXiv, OpenAlex, Zenodo, GitHub, or `watch/snapshots/**`.
