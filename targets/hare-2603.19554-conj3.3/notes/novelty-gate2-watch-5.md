# Gate 2 Novelty Receipt (`watch-5`) — `targets/hare-2603.19554-conj3.3/`

- **Checked UTC:** `2026-11-27T09:02Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** Kevin G. Hare and Hajer Hichri, `arXiv:2603.19554v1` (`2026-03-20`), Section 3.1 Conjecture 3.3 (`conj:1`): for all $d \ge 4$ and $k \ge 1$, $\beta_d^k$ (powers of the Perron root of $x^d - x - 1$) is non-Parry.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, 604 files):**
   - `.venv/bin/python tools/novelty_grep.py 2603.19554 Hichri "Parry order" "non-Parry" --max-per-file 5 --max-total 20`: `3` lines across `3/604` files:
     - **Near-miss (`ArtificialZeng/AI-Has-Taste`, `BW2-B06-P08`):** *"Every Power of the Perron Root of $X^4 - X - 1$ Is Non-Parry: An Exact Certificate"* — settles ONLY the single fixed case $d = 4$, not general $d \ge 4$.
     - `AlexenderSokolov/cross-theory-formal-database`: license file `arxiv-2603.19554-CC-BY-4.0.txt` only.
2. **Live arXiv & OpenAlex citing check (`tools/arxiv_fetch.py`, `api.openalex.org`):**
   - `id_list=['2603.19554']` (`max_age=300`): confirms `2603.19554v1` (`2026-03-20T01:33:42Z`) remains sole version.
   - `abs:"2603.19554" OR (all:Hare AND all:"Solomyak" AND all:2026)` (`max_age=300`): `total: 0`.
   - OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2603.19554`): `cited_by_count: 0`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2603.19554&size=5`):**
   - `total: 0`.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by arXiv, OpenAlex, Zenodo, or `watch/snapshots/**`.
