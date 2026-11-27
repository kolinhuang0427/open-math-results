# Gate 2 Novelty Receipt (`watch-1`) — `targets/haugland-2411.00721-ques2/`

- **Checked UTC:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 586+ files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`): `0` hits for `2411.00721`, `Haugland`, `Omland`, `"proper lifting"`.
   - `.venv/bin/python tools/novelty_grep.py 2411.00721 Haugland Omland "proper lifting"`:
     - `facebookresearch/atlas-lean` (`#8807`) and `plasma-ai/erdos` / `BoltonBailey` / `open-math-agents` hits are Haugland (1996/2022) on Erdős Problem #36 (minimum overlap), unrelated.
     - `watch/snapshots/arxiv/citing_papers.md` lists 4 citing preprints of `2411.00721`, all checked via `tools/arxiv_fetch.py query --id-list 2610.33131,2609.35921,2609.19548,2605.18875`:
       - **Near miss — `arXiv:2609.35921v1`** (*"Finite-ring obstructions for quadratic binary radius-two cellular automata"*, Houqiao Fu, `2026-09-28`): proves non-injectivity on periodic rings of length $n$ ($4 \mid n, n \ge 8$) ONLY for **five-slot radius-two ($k = 5$)** degree-2 local rules, NOT arbitrary diameter $k$ (and Question 2 asks whether any degree-2 proper lifting exists for any $k$).
       - `arXiv:2610.33131v2` (Haugland–Larsen–Omland–Rustad, `2026-11-19`): open and locally eventually onto CAs ($n$-to-1), not proper liftings of degree 2.
       - `arXiv:2609.19548v3` (Feng–Wang–Yu–Zhang, `2026-11-10`): characterizes shift-invariant permutations of the specific form $x_{i+u} + x_{i+v}(x_{i+w}+a_i)$, not general degree-2 proper liftings.
       - `arXiv:2605.18875v1` (Dennunzio–Gadouleau–Mariot, `2026-05-15`): transversals of Latin squares from bipermutive CAs, unrelated.
2. **Live GitHub (`gh search`):**
   - `gh search issues "2411.00721"` -> `0` issues.

## Coverage Limits
- Closed-access venues, private repositories, and unindexed papers not citing `2411.00721`.
