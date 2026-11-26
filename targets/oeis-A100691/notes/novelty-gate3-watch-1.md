# Gate 3 Novelty Receipt — `oeis-A100691`

- **UTC Time:** 2026-11-26T21:14:23Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Live Pre-Report Re-Checks Performed

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py A100691 A193641 "1,4,12,30,70,160"` -> 0 hits across 224 files.
2. **Live `1337isnot1337/solved-conjectures` (`gh api`, read-only):**
   - `commits/main` (`1ad4084f86`, `2026-11-26T20:41:56Z`, PR #904 *Oriented general position spectrum nonconstancy conjecture*), `commits/research` (`5f0f1a6a4f`, `2026-11-26T21:06:25Z`), `search/code?q=repo:1337isnot1337/solved-conjectures+A100691+OR+A193641` -> 0 hits.
3. **Live GitHub global & `trureturing` searches (`gh api`, read-only):**
   - `search/code?q=A100691+OR+A193641` -> 0 hits.
   - `search/code?q=repo:the-omega-institute/trureturing+A100691+OR+A193641` -> 0 hits.
   - `search/code?q="1,4,12,30,70,160"` -> 2 hits (`A218009` = `0,1,4,12,30,70,160,364,...`, binomial transform of `A212831`, diverges from SAW `s(n)` at `n=6` where `s(6)=360 != 364`), `"1, 4, 12, 30, 70, 160"` -> 1 unrelated terrain test file.
4. **Live Zenodo API:**
   - `https://zenodo.org/api/records?q=A100691&size=5` -> `total: 0`; `q=A193641` -> `total: 0`.
5. **Live web search (`search_web`):**
   - `"A100691" OR "A193641" "160" OR "158" "triangular" "self-avoiding"` -> no prior resolution or published `s(5)=160` erratum found.

## Near Misses

- `A218009` (`0,1,4,12,30,70,160,364,...`): matches through `160` then diverges (`364 != 360`), unrelated binomial transform.
- `joaquimmj/oeis-conjectures`: lists `A100691` in open crawl only.

## What Was Not Covered

- Print-only J. Labelle (*Bull. ICA* 17, 1996) and Došlić–Zubac (2016) PDFs, OpenAlex/arXiv live re-query (covered by `@watch-5`), and private repositories.
