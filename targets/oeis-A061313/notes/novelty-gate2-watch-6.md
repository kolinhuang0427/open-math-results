# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/oeis-A061313/` (`OEIS A061313` rev 58, Andrei Zabolotskii Apr 17 2020 conjecture: `a(n)+2` is the sum of the Hirzebruch continued fraction terms for Stern-Brocot fraction `A007305(n)/A007306(n)`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:31:10Z`
- **Requested by:** `@scout-6` (board #424)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A061313 Zabolotskii`
   - Result: `# 0 lines across 0/356 files in 0.38s`
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A061313&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A061313 rev: 58 time: 2026-11-01T16:49:49-05:00`; comment still explicitly states `Conjecture: a(n)+2 is the sum of the terms of the Hirzebruch (negative) continued fraction for the Stern-Brocot tree fraction A007305(n)/A007306(n). - _Andrei Zabolotskii_, Apr 17 2020` with no proof recorded.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A061313"` -> `[]`
   - `gh search issues "A061313"` -> `[]`
   - `gh search code "A061313"` -> only term-computation / OEIS mirrors (`archmageirvine/joeis`, `loda-lang/loda-programs`) and unrelated challenge/data blobs; no proof.
4. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A061313"' --max-results 5` -> `total_results: 0`.
5. **Web Search (`search_web`):**
   - Query: `"A061313" "Zabolotskii" OR "Stern-Brocot" conjecture proved`
   - Result: Only OEIS `A061313` / `A008687` and unrelated frieze-pattern papers by Short–van Son–Zabolotskii (*Adv. Math.* 2025); no prior proof of `A061313` found.

## Near Misses
- OEIS `A008687` carries Zabolotskii's sibling length conjecture; Ian Short, Matty van Son & Andrei Zabolotskii (*Adv. Math.* 2025) study Stern–Brocot / Farey complexes & frieze patterns, not the `A061313` recurrence-sum conjecture.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not citing `A061313`.
