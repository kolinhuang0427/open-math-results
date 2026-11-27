# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/linusson-2512.24346-conj1/` (Linusson–Özdemir `arXiv:2512.24346v1` §3.4 Conjecture 1 `conj:complement`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:05:24Z`
- **Requested by:** `@audit-2` (board #381)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 333 files incl. `aliromman__math.json` & `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2512.24346 "conj:complement" A006255 Padhi`
   - Result: `Watchlist/index` citations only (`watch/snapshots/arxiv/citing/linusson-2512.24346-conj1.json`, `openalex_works_cache.json`); 0 hits in `aliromman__math.json`, `the-omega-institute__trureturing-tools.json`, `trureturing`, `1337isnot1337`, `openai-math`, or `discovered/`.
2. **Newly Added Competing Repos (`aliromman/math` & `the-omega-institute/trureturing-tools`):**
   - `aliromman/math` (`105` PRs, `74` files): `PR #94` (Leander–Linusson directed paths) and `PR #33` (Alabama paradox) address unrelated Linusson papers; `0` PRs/files mention `2512.24346`, `k-Plancherel`, or `conj:complement`.
   - `the-omega-institute/trureturing-tools` (`SCREENED-OUT*.md`, `SCREENED-OUT-R52.md`, `SCREENED-OUT-R71.md`): `0` matches for `2512.24346` or `Linusson`.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "2512.24346 OR A006255"` -> `[]`
   - `gh search code "2512.24346"` -> `AlexenderSokolov/cross-theory-formal-database` (`editable-corpus/sources/191882/provenance.json` extracts Lemma `triangle-lemma` proved by Linusson & Özdemir inside `2512.24346v1` itself, lines 830–946) + `ehijano/rss_fetch` (arXiv RSS mirror); no proof of `conj:complement`.
4. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2512.24346` -> `2512.24346v1` remains sole version.

## Near Misses
- `AlexenderSokolov/cross-theory-formal-database` item `191882` archives `triangle-lemma` from `2512.24346v1` itself; `aliromman/math#33` and `#94` treat other Linusson works.

## Not Covered
- Private repositories, paywalled publications, and unindexed offline manuscripts.
