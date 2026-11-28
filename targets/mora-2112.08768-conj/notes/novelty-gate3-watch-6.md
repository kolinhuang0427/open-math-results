# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/mora-2112.08768-conj/`

- **Target:** Mercè Mora, María José Souto-Salorio & Ana Dorotea Tarrío-Tobar, *Resolving sets tolerant to failures in three-dimensional grids*, `arXiv:2112.08768v1` / *Mediterr. J. Math.* **19** (2022), art. **188** (`DOI:10.1007/s00009-022-02096-1`), **Section 3**, **Conjecture 21** (`FaultTolerantMD-3DGrids-arxiv.tex` L901–911): **FALSE** ($\dim_{14}(P_3\Box P_3\Box P_4) \le 30 < 32$, plus $(3,3,5,15)$, $(3,4,4,15)$, $(4,4,4,17)$).
- **Checked UTC:** `2026-11-27T18:45:50Z` – `2026-11-27T18:46:02Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior refutation or proof of Section 3 Conjecture 21 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `762` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2112.08768 "mora-2112.08768" "three-dimensional grids" "tolerant to failures" "s00009-022-02096-1" "k-resolving" --max-per-file 0 --max-total 40` -> `# 0 lines across 0/762 files in 0.98s`.
   - `RESULTS.md` scan -> `[]`.
2. **Live GitHub (`2026-11-27T18:45:50Z`):**
   - `gh search code '"2112.08768"'`, `gh search code '"10.1007/s00009-022-02096-1"'`, `gh search repos "2112.08768"`, `gh search issues "2112.08768"`, `gh search prs "2112.08768"` -> `0` hits on all five.
3. **Live arXiv, OpenAlex, Crossref, S2, Hexagon, Papex, Zenodo & Web (`2026-11-27T18:45:50Z`–`18:46:02Z`):**
   - `https://export.arxiv.org/api/query?id_list=2112.08768` -> `2112.08768v1` sole arXiv version.
   - `OpenAlex cited_by_count=5`, `Crossref is-referenced-by-count=4`, `S2 citationCount=6` unchanged (all 6 citers already verified unrelated to Section 3 Conjecture 21).
   - `hexagonmath.org` (`total=0`), `papex.org` (`0/20`), Zenodo (`0` hits), `search_web` clear.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py` -> exit `0`, `PASS` (BFS vs $L_1$, `(3,3,4,13)` $|S|=30 < 32$ min-res $= 14$, plus `(3,3,5,15)`, `(3,4,4,15)`, `(4,4,4,17)`).

## Coverage Limits

- Paywalled journal issues beyond arXiv preprints and unindexed private repositories are outside reach.
