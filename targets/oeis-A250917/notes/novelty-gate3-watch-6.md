# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/oeis-A250917/` (`OEIS A250917`, R. J. Mathar Jan 25 2020 conjectured order-5 D-finite recurrence for e.g.f. `exp(x*C(x)^3)`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T21:39:06Z`
- **Requested by:** `@audit-2` (board #234)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A250917`
   - Result: `# 0 lines across 0/224 files in 0.45s`
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A250917&fmt=json` (User-Agent: `open-math-watch/1.0`)
   - Result: `number: 250917`, `revision: 20`, `time: 2025-03-15T11:29:15-04:00`; still explicitly lists `Conjecture D-finite with recurrence: ... - _R. J. Mathar_, Jan 25 2020` with no recorded proof.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A250917" --limit 20` -> `[]`
   - `gh search issues "A250917" --limit 20` -> 1 unrelated issue (`trac-hacks/tracstats#17`, 2011)
   - `gh search code "A250917" --limit 20` -> only known OEIS mirrors/term-generators (`archmageirvine/joeis` `src/irvine/oeis/a250/A250917.java`, `loda-lang/loda-programs` `oeis/250/A250917.asm`, `gfis/OEIS-mat` `contrib/rm/dfinite.grep.txt` & `holrec/rectopost.man`) plus unrelated string matches (`OEIS-Spider` `A250916.txt`, `ray-project/ray`, etc.).
4. **arXiv (`tools/arxiv_fetch.py`):**
   - Command: `.venv/bin/python tools/arxiv_fetch.py query 'all:"A250917"' --max-results 10`
   - Result: `total_results: 0`, `entries: []`
5. **Web Search (`search_web`):**
   - Query: `"A250917" oeis OR conjecture OR proved`
   - Result: No prior proof or resolution found.

## Near Misses
- `gfis/OEIS-mat` (`holrec/rectopost.man`, `contrib/rm/dfinite.grep.txt`) and `archmageirvine/joeis` (`A250917.java`) carry an unproved Maple `sumrecursion` order-3 recurrence / term computation for the binomial sum formula, with no proof, no creative-telescoping certificate, no equivalence proof to `exp(x*C(x)^3)`, and no derivation of Mathar's conjectured order-5 recurrence (already verified in `AUDIT.md` and `novelty-gate2-watch-6.md`).

## Not Covered
- Paywalled literature, private repositories, offline preprints not citing `A250917`, and unindexed Zenodo records.
