# Gate 2 Novelty Receipt (`watch-5`) — `targets/benfield-2407.20048-conj5.3/`

- **Checked UTC:** `2026-11-27T09:03Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Brennan Benfield and Oliver Lippard, `arXiv:2407.20048v2` (`2025-01-30`), Section 5 Conjecture 5.3 (`\label{finite-orders}`): range of $\omega_{(a,b)}(m)$ for $(a,b)$-Fibonacci sequences ($m > 1$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 604 files):**
   - `.venv/bin/python tools/novelty_grep.py 2407.20048 "Connecting Zeros in Pisano" "finite-orders" "K-Fibonacci" --max-per-file 5 --max-total 20`: `0` lines across `0/604` files.
   - `tools/novelty_grep.py Benfield`: hits in `1337-solved-conjectures` are all Benfield–Lippard `arXiv:2404.08193v2` (Waring-gap conjectures, unrelated).
2. **Live arXiv, OpenAlex & Semantic Scholar citing sweep (`tools/arxiv_fetch.py`, `api.openalex.org`, `api.semanticscholar.org`):**
   - `id_list=['2407.20048']` (`max_age=300`): confirms `2407.20048v2` (`2025-01-30T20:24:47Z`) remains latest version.
   - `abs:"2407.20048" OR (au:Benfield AND all:"5.3")` (`max_age=300`): `total: 0`.
   - OpenAlex (`cited_by_count: 1`) + Semantic Scholar citations (`3` records):
     - **Near-miss `arXiv:2605.24146v1`** (Ilya Vyugin and Sashadhar Dutta, `2026-05-22`, *"On some arithmetic conditions of recurrent sequences modulo prime p"*): abstract verified directly via `tools/arxiv_fetch.py` — estimates sumset/product-set cardinalities $|\mathcal{F}_p + \mathcal{F}_p|$ and $|\mathcal{F}_p \cdot \mathcal{F}_p|$ in $\mathbb{F}_p$, does not address $\omega_{(a,b)}(m)$ or Conjecture 5.3.
     - `arXiv:2404.08194` / DOI `10.1080/00150517.2025.2491986` (*"Fixed Points of $K$-Fibonacci Sequences"*): predates `2407.20048` and studies fixed points, not $\omega_{(a,b)}(m)$.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=5`):**
   - `total: 0`.
4. **Web search (`search_web`):**
   - `"Connecting Zeros in Pisano Periods" OR "2407.20048" OR ("Benfield" "Lippard" "Pisano")`: returns only `2407.20048` itself, no refutation of Conjecture 5.3.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Semantic Scholar, Zenodo, web search, or `watch/snapshots/**`.
