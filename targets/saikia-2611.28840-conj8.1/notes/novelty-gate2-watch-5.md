# Gate 2 Novelty Receipt — `saikia-2611.28840-conj8.1` (`watch-5`)

- **Target:** `targets/saikia-2611.28840-conj8.1/` — Manjil P. Saikia, *"Congruences modulo powers of $2$ and $3$ for Lin's function $\mathrm{PDO}_t(n)$"*, `arXiv:2611.28840v1`, §8 Conjecture 8.1 (`\label{conj:sharp}`).
- **Checked UTC:** `2026-11-27T16:06:35Z`–`2026-11-27T16:07:10Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no published proof or refutation of Conjecture 8.1 for general $k \ge 3$ (or $k \ge 33$) found.

## Exact Queries & Results

1. **Local snapshots (`watch/snapshots/**`, 821 cataloged entries incl. `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `1337-solved-conjectures`):**
   - `.venv/bin/python tools/novelty_grep.py "2611.28840" "Saikia" "conj:sharp" "Atkin" --max-per-file 5 --max-total 50`:
     - Only hits for `2611.28840` are the arXiv submission snapshot (`2611.28840v1`, `2026-11-21`), `citing_papers.{md,json}` (`OpenAlex cited_by=0; S2=0` at `15:46Z`), and `watch/snapshots/ai-collections/the-omega-institute__trureturing/issues_and_prs.txt:341` (`#34564`).
   - `watch/snapshots/hexagonmath-index.md`: only unrelated Manjil Saikia paper `2610.00469` (`2026-10-22`); `watch/snapshots/papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `1337-solved-conjectures/*.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh issue view 34564 -R the-omega-institute/trureturing --comments`: open preregistered finite check (`12 <= k <= 32`) by `macstudio-2` (`#issuecomment-7199725016` verifies `3 <= k <= 32` only and explicitly states *"The conjecture for k ≥ 33 remains open."*).
   - `gh search issues "2611.28840"`, `gh search prs "2611.28840"`, `gh search repos "2611.28840"`, `gh search prs "PDO_t" "Saikia"`: `0` hits. `gh search issues "PDO_t" "Saikia"`: only `#34564`.
   - `gh api "repos/the-omega-institute/trureturing/pulls?state=all&per_page=10"`, `git/trees/dev?recursive=1`, and `trureturing-experiments` `git/trees/main?recursive=1`: `0` PRs/files for `2611.28840`, `Saikia`, or `PDO_t` (regex `2611` matched only unrelated `oeis-a372239-a372420-a372611-tebni-central-binomial-congruences`).
3. **Live Preprint / Citation APIs & Web:**
   - **arXiv API (`id_list=2611.28840`):** `2611.28840v1` (`updated: 2026-11-21T14:45:07Z`) remains sole version.
   - **OpenAlex (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2611.28840`):** `cited_by_count: 0`.
   - **Zenodo (`q=2611.28840`):** `0` hits; **Crossref (`query=2611.28840`):** `0` relevant hits.
   - **`search_web` (`"2611.28840"`, `"2611.28840" OR ("Saikia" "PDO_t" "conjecture")`)**: returns only `arXiv:2611.28840` itself (and unrelated 2023 overpartition congruence paper `2307.01272`).

## Near-Misses & Coverage Limits
- **Near-miss:** `the-omega-institute/trureturing#34564` verifies `12 <= k <= 32` computationally (and Saikia's paper proves `3 <= k <= 11`), leaving `k >= 33` and the general all-`k >= 3` statement open.
- **Coverage limits:** Live Semantic Scholar single-paper call hit `HTTP 429` at `16:06Z` (checked earlier at `15:46:03Z` via S2 batch with `citationCount=0`); private or unindexed drafts posted after `16:07Z` are not covered.
