# Gate 2 Novelty Check — `dawar-2611.23541-sym-depth` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T20:34:46Z`–`2026-11-27T20:34:58Z`
- **Target:** `targets/dawar-2611.23541-sym-depth/` — Anuj Dawar, Prateek Dwivedi, Benedikt Pago, and Tim Seppelt, *"Depth Hierarchies for Symmetric Algebraic Circuits"* (`arXiv:2611.23541v1`, `2026-11-17`), Section 1.2 (*"Future work"*, `introduction.tex` L269–271: reducing symmetric circuits to depth $3$ or $4$, and at what cost in orbit size)
- **Claimed result:** Proves $\Omega(\min\{d,n\}^{1/\Delta}\log n)$ orbit lower bound for depth $3,4$ on $\mathsf{symVBP}$, sharp $2^{\Omega(\sqrt{d}\log n)}$ homogeneous depth-4 lower bound via new UFD no-support-drop lemma, and matching $n^{O(\kappa\sqrt{d})}$ depth-4 & depth-3 symmetric reductions (`PROOF.md`, `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.23541" "Dawar" "symVBP" "symmetric circuit"`):**
   - `8` lines across `3/837` files (`watch/snapshots/arxiv/arxiv_submissions.*` & `state.json` indexing `2611.23541v1` itself and unrelated quantum `2611.*` Castro-Silva–Dancy–Strelchuk); `0` settlement hits across all `837` snapshot files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T20:34:46Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `8c7062d8461194840db328315035898a750b6b97` (`2026-11-27T20:33:17Z`, book staircase threshold) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.23541"` -> `0` hits (`[]`).
   - `gh search issues "2611.23541"` -> `0` hits (`[]`).
   - `gh search code "2611.23541"` -> `qiao-925/news-digest` (`2026-11-19`) and unrelated CSV numeric collisions only.
4. **arXiv / Zenodo / Web & Venue Follow-ups:**
   - arXiv API (`id_list=2611.23541`) -> sole version `2611.23541v1` (`2026-11-17T21:49:23Z`).
   - Zenodo API (`q=2611.23541`) -> `0` hits.
   - `search_web` (including ECCC/FOCS/STOC/CCC/ICALP follow-up queries for Dawar–Dwivedi–Pago–Seppelt / `symVBP` / symmetric depth-4 reduction) -> only `arXiv:2611.23541` and earlier `symVF`/`symVBP`/`symVP` separations; `0` resolutions of depth-3/4 symmetric circuit reductions or orbit-size bounds.

## Coverage Limits
- Covers `watch/snapshots` (`837` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and `search_web` as of `2026-11-27T20:34:58Z`; private repositories and non-indexed preprints remain unobservable.
