# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/awan-2611.07303-q2/`

- **Target:** Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger & Elvis Wong, `arXiv:2611.07303v2` (*"Gaps in the Most Frequent Sizes of Integer Sumsets"*, `2026-11-09`), Section 5.2, **Question 2** (`\label{q:rate}`): **YES** convergence + normalized $(k-1)$-dimensional volume formula for $c_{h,k}$, and **NO** eventual monotonicity (`(3,3)` and `(2,4)` oscillations).
- **Checked UTC:** `2026-11-27T18:41:43Z` – `2026-11-27T18:41:55Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior settlement of Question 2 `q:rate` found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `762` files incl. `richfrem__Project_Sanctuary.json` & `sawan201__PolyMathJr_MSTD.json`) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2611.07303 "awan-2611.07303" "q:rate" "f_{h,k}" "c_{h,k}" --max-per-file 0 --max-total 40` -> `# 0 lines across 0/762 files in 0.72s` (`sawan201/PolyMathJr_MSTD` covers `K3Limit.lean` only).
   - `RESULTS.md` scan (`2611\.07303|awan`) -> `[]`.
2. **Live GitHub (`2026-11-27T18:41:43Z`–`18:41:51Z`):**
   - `gh search code '"2611.07303"'` / `prs` -> `richfrem/Project_Sanctuary` (`MISSION-062.json`, PR `#403`, finite $k=3$ frequent sizes only).
   - `gh search issues "2611.07303"` -> `the-omega-institute/trureturing#29874` (`open`, Question 4 `q:distribution` only).
   - `gh search code '"awan-2611.07303"'`, `gh search code '"q:rate" "Awan"'`, `gh search repos "2611.07303"` -> `0` hits on all three.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T18:41:43Z`–`18:41:55Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.07303` -> `2611.07303v2` sole latest version.
   - `https://hexagonmath.org/api/v1/works` (`q=2611.07303`, `q=Awan`) -> `total=0`; `papex.org` `0/20`; Zenodo `0` hits; OpenAlex `0` indexed records.
   - `search_web` (`"2611.07303" ("q:rate" OR "c_{h,k}" OR "eventually monotone" OR "Question 2")`) -> returns only Awan et al.'s `arXiv:2611.07303` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py` -> exit `0`, `PASS` (`Section 1`, `Section 2.1`, `Section 2.2`: PASS).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach.
