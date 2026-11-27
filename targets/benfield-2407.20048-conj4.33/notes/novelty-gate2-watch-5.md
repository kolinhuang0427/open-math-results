# Gate 2 Novelty Receipt (`watch-5`) — `targets/benfield-2407.20048-conj4.33/`

- **Checked UTC:** `2026-11-27T09:16Z` – `2026-11-27T09:17Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Brennan Benfield and Oliver Lippard, `arXiv:2407.20048v2` (`2025-01-30`), Section 4.2 Conjecture 4.33 (`\label{even-K-exceptions}`): extensions of Theorem `omega-odd-K` to even $K$ for all moduli $m > 3$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 608 files):**
   - `.venv/bin/python tools/novelty_grep.py 2407.20048 "even-K-exceptions" "4 \mid \pi" "pisano-order" --max-per-file 5 --max-total 15`: `1` line across `1/608` files (`the-omega-institute/trureturing` `Problems/pisano-order-range-refutation.md`, which addresses only Conjecture 5.3 clause (v), not Conjecture 4.33).
2. **Live arXiv, OpenAlex & Semantic Scholar citing check (`tools/arxiv_fetch.py`, `api.openalex.org`, `api.semanticscholar.org`):**
   - `id_list=['2506.20778', '2407.20048']` (`max_age=300`): confirms `2407.20048v2` (`2025-01-30T20:24:47Z`) remains latest version.
   - `abs:"2506.20778" OR abs:"2407.20048"` (`max_age=300`): `total: 0`.
   - OpenAlex (`cited_by_count: 1`) + Semantic Scholar citations (checked earlier in `09:03Z`): `arXiv:2605.24146v1` (Vyugin–Dutta, sumset/product-set estimates in $\mathbb{F}_p$) and `arXiv:2404.08194` / DOI `10.1080/00150517.2025.2491986` (fixed points of $K$-Fibonacci sequences) — none addresses Conjecture 4.33.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Semantic Scholar, Zenodo, or `watch/snapshots/**`.
