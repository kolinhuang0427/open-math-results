# Gate 3 Novelty Receipt — `oeis-A394511`

- **UTC Time:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 586 files across `1337-solved-conjectures`, `ai-collections`, `arxiv`, `discovered`, `erdosproblems`, `formal`, `openai-math`):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`, 214 `results/` dirs, 293 open issues, 274 closed issues, 6 open PRs, 413 merged PRs): `0` hits for `A394511`, `Exley`, `enclosing shell`, `4.8.8`.
   - `.venv/bin/python tools/novelty_grep.py A394511 "Exley" "enclosing shell" "4.8.8"` -> `1` unrelated hit (`facebookresearch__atlas-lean/issues_and_prs.txt:208`, `4.8.8` inside a URL); `0` hits for `A394511`, `Exley`, `enclosing shell`.
2. **Live GitHub (`gh search`):**
   - `gh search issues "A394511"` -> `0` issues.
   - `gh search code "A394511"` -> only `loda-lang/loda-programs` (`oeis/394/A394511.asm`, sequence computation), no disproof or proof.
3. **Live OEIS & Zenodo API (`2026-11-27T08:48Z`):**
   - `https://oeis.org/search?q=id:A394511&fmt=json` -> revision `47` (`2026-06-06T04:04:55-04:00`), unchanged (`Conjectured (UNVERIFIED beyond n = 23)`).
   - `https://zenodo.org/api/records?q=A394511&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues and private repositories (`pexley-math/oeis-A394511` returns HTTP 404).
