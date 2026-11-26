# Gate 2 Novelty Receipt — `oeis-A250917`

- **Verdict:** **PASS** (no prior proof of Mathar's 2020 order-5 D-finite recurrence for `A250917` found)
- **Checked at (UTC):** 2026-11-26T20:54:31Z
- **Watcher:** `watch-6`

## Sources Checked

1. All local `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A250917 "C(x)^3"`.
2. Live OEIS JSON API (`https://oeis.org/search?q=id:A250917&fmt=json`, rev 20, `2025-03-15`).
3. Live GitHub search (`gh search repos "A250917"`, `gh search issues "A250917"`, `gh search code "A250917"`) and `gh api` inspection of `gfis/OEIS-mat/contrib/rm/dfinite.grep.txt`.
4. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py query 'all:"A250917"'`.
5. Web search (`search_web`).

## Exact Queries

- `.venv/bin/python tools/novelty_grep.py 2507.14473 "triangle-regular" Sheffield A250917 "C(x)^3"`
- `https://oeis.org/search?q=id:A250917&fmt=json`
- `gh search repos "2507.14473 OR A250917"`
- `gh search issues "\"2507.14473\" OR \"A250917\" OR \"triangle-regular\""`
- `gh search code "A250917"`
- `gh api repos/gfis/OEIS-mat/contents/contrib/rm/dfinite.grep.txt`
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A250917" OR (all:"triangle-regular" AND all:"abelian")' --max-results 10`
- `search_web`: `"A250917" "Mathar" OR "exp( x*C(x)^3 )" OR "12*(n-5)" recurrence proved`

## Near Misses & Findings

- Live OEIS `A250917` (rev 20, `2025-03-15`) still lists `Conjecture D-finite with recurrence: ... - _R. J. Mathar_, Jan 25 2020` with no recorded proof.
- `gfis/OEIS-mat/contrib/rm/dfinite.grep.txt`, `archmageirvine/joeis` (`A250917.java`), and `loda-lang/loda-programs` (`A250917.asm`) mirror OEIS text / generate terms only without proving Mathar's order-5 recurrence.
- Zero matches in `watch/snapshots/**`, arXiv, or web search.

## What Was Not Covered

- Private repositories, Zenodo records not indexed by OpenAlex/web search, and offline papers not citing `A250917`.
