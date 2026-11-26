# Gate 3 Novelty Receipt (Pre-Report) — `oeis-A100691`

- **Verdict:** **PASS** (no new public proof or SAW erratum found in the pre-report window)
- **Checked at (UTC):** 2026-11-26T21:12:06Z
- **Watcher:** `watch-6`

## Sources Checked

1. All local `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A100691 A193641`.
2. Live OEIS JSON API (`A100691` rev 11, `2022-07-22`; `A193641` rev 48, `2026-09-16`).
3. Live GitHub search (`gh search repos`, `gh search issues`, `gh search code "A100691"`).
4. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py query 'all:"A100691" OR all:"A193641"' --max-results 10`.
5. Web search (`search_web`).

## Exact Queries

- `.venv/bin/python tools/novelty_grep.py A100691 A193641`
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A100691" OR all:"A193641"' --max-results 10`
- `gh search repos "A100691 OR A193641"`
- `gh search issues "\"A100691\" OR \"A193641\""`
- `gh search code "A100691"`
- `https://oeis.org/search?q=id:A100691&fmt=json` & `id:A193641`
- `search_web`: `"A100691" "A193641" OR "A100691" "triangular lattice" "160"`

## Findings & Near Misses

- Live OEIS `A100691` remains at rev 11 (`2022-07-22`) and `A193641` remains at rev 48 (`2026-09-16`), with no new proof or `s(5)=160` erratum posted.
- `gh search code "A100691"` returned only standard OEIS mirrors/generators (`archmageirvine/joeis`, `loda-lang/loda-programs`, `Anon52MI4/oeis-alien`), none proving Mathar's conjecture or reporting the SAW erratum.
- Zero matches in `watch/snapshots/**`, arXiv, or web search.

## What Was Not Covered

- Print-only text of J. Labelle, *Bull. ICA* 17 (1996), 47–61 (already noted in `AUDIT.md` §3.3), private repositories, and non-indexed manuscripts.
