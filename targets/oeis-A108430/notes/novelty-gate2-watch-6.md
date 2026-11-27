# Gate 2 Novelty Receipt — `oeis-A108430`

- **Verdict:** **PASS** (no prior proof of Mathar's 2022 D-finite recurrence for `A108430` found)
- **Checked at (UTC):** 2026-11-26T21:14:33Z
- **Watcher:** `watch-6`

## Sources Checked

1. All local `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A108430`.
2. Live OEIS JSON API (`https://oeis.org/search?q=id:A108430&fmt=json`, rev 14, `2025-11-05`).
3. Live GitHub search (`gh search repos "A108430"`, `gh search issues "A108430"`, `gh search code "A108430"`) and `gh api` inspection of `gfis/OEIS-mat/contrib/rm/dfinite.grep.txt`.
4. Live Zenodo API (`https://zenodo.org/api/records?q=A108430`, `q=23982*n-28681`).
5. Live arXiv API (`tools/arxiv_fetch.py query 'all:"A108430"'`) and `search_web`.

## Near Misses & Findings

- Live OEIS `A108430` (rev 14, `2025-11-05`) still lists `Conjecture D-finite with recurrence ... - _R. J. Mathar_, Jul 24 2022` with no recorded proof.
- `gfis/OEIS-mat/contrib/rm/dfinite.grep.txt`, `archmageirvine/joeis` (`A108430.java`), and `loda-lang/loda-programs` (`A108430.asm`) mirror OEIS text / generate sequence terms only.
- Zenodo API (`0` hits), `watch/snapshots/**` (`0` hits), arXiv (`0` hits), and web search found no prior proof.

## What Was Not Covered

- Print-only JSTOR text of Deutsch (*Amer. Math. Monthly* 107, 2000, Problem 10658, which predates Mathar's 2022 conjecture), private repositories, and offline manuscripts.
