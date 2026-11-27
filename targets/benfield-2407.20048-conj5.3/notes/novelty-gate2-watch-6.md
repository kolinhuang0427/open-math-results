# Gate 2 Novelty Receipt (`watch-6`) — `targets/benfield-2407.20048-conj5.3/`

- **Checked UTC:** `2026-11-27T09:04:30Z` (updated after verifying `the-omega-institute/trureturing#9448`)
- **Verdict:** **CONTESTED (Partial Overlap)** — clause (v) already refuted in `trureturing#9448` (`2026-09-22`); clause (vi) remains open/unsettled.

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 604 files including 433 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A158826" "158826" "2407.20048" "Benfield"` -> `0` hits for `2407.20048`; `Benfield` hits (`1337isnot1337/solved-conjectures`, `trureturing`) are `arXiv:2404.08193v2` (Waring-gap). Note: `trureturing`'s `Problems/pisano-order-range-refutation.md` file path did not contain `2407.20048` or `Benfield`.
2. **Independent verification of `the-omega-institute/trureturing#9448` (`gh api repos/the-omega-institute/trureturing/issues/9448`):**
   - Confirmed closed issue `9448`: *"prereg: arXiv:2407.20048 Conjecture 5.3(v) — the Pisano order is not confined to {0,1,2} under the printed condition"* (PR #9451, `2026-09-22`), which refutes Conjecture 5.3 clause (v) at `(a,b)=(3,2), m=13`, while leaving clause (vi) (`(a,b)=(3,4)` proved for all $m > 1$) unsettled.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2407.20048`: `2407.20048v2` (`2025-01-30`) remains latest.
   - `zenodo.org/api/records?q=2407.20048&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2407.20048" OR "Benfield" "Conjecture 5.3" OR "omega" OR "prime factors"` -> returns only `arXiv:2407.20048`.

## Coverage Limits
- Live `gh search code` was skipped due to shared HTTP 429 rate-limit pressure; combined `OR` in `gh search issues` missed `trureturing#9448` initially (caught via `watch-1` `#127` and verified directly via `gh api`).
