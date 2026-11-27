# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/gaetz-2512.08168-conj1/` (Christian Gaetz & Yibo Gao `arXiv:2512.08168v2` Conjecture 1.3 `conj:union-intersection`: $\mathrm{BP}(w)$ is closed under intersection and union for all Coxeter groups)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T23:23:18Z`
- **Requested by:** `@attack-2` (board #412)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 356 files):**
   - Command: `.venv/bin/python tools/novelty_grep.py 2512.08168 "conj:union-intersection" "Billey--Postnikov"`
   - Result: Index/cache entries + `the-omega-institute/trureturing-tools` (`SCREENED-OUT-R52.md`, which only notes `2512.08168` Conjecture 1.9 was disproved in Theorem 6.2 of `2512.08168` itself); `0` hits settling Conjecture 1.3.
   - Verified `MattiaCalzavara/gaetz-gao-conjecture-proof` (`README.md`) proves a different Gaetz–Gao conjecture on strong $q$-log-concavity.
2. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "2512.08168"` -> `[]`
   - `gh search issues "2512.08168"` -> `the-omega-institute/trureturing#7333` (general lane log)
   - `gh search code "2512.08168"` -> `trureturing-tools/SCREENED-OUT-R52.md` (Conjecture 1.9 note only), `ehijano/rss_fetch` arXiv RSS XMLs, and unrelated CSV/text substrings.
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2512.08168,2611.33572` -> `2512.08168v2` (`2026-06-08`) is latest; Gaetz–Gao's `2611.33572v1` (`2026-11-25`) proves the Lookup Conjecture, unrelated to `conj:union-intersection`.
4. **Web Search (`search_web`):**
   - Query: `"2512.08168" "Conjecture 1.3" OR "conj:union-intersection" OR "Billey-Postnikov" Gaetz Gao proved`
   - Result: Only `arXiv:2512.08168` itself (known for finite Weyl groups & rank $\le 3$ only).

## Near Misses
- `trureturing-tools/SCREENED-OUT-R52.md` mentions `arXiv:2512.08168` Conjecture 1.9 (already refuted in `2512.08168` Theorem 6.2), not Conjecture 1.3.
- `MattiaCalzavara/gaetz-gao-conjecture-proof` addresses Gaetz–Gao's strong $q$-log-concavity conjecture, not `2512.08168`.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts.
