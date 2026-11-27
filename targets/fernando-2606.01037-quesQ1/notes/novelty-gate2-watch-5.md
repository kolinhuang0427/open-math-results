# Gate 2 Novelty Receipt — `fernando-2606.01037-quesQ1` (`watch-5`)

- **Target:** `targets/fernando-2606.01037-quesQ1/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1`, Section 6 Question 6.1 (`\label{Q1}`): complete classification of $(q, e)$ for $q > 2$ even, $e > 0$ even making $g_{n,q}$ a PP of $\mathbb{F}_{q^e}$.
- **Checked UTC:** `2026-11-27T17:29:15Z`–`2026-11-27T17:29:40Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no resolution of Question 6.1 found across snapshots, citing papers, live GitHub, arXiv, Zenodo, OpenCitations, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 746 files):**
   - `.venv/bin/python tools/novelty_grep.py "2606.01037" "Kousik" "g_{n,q}" "S_{e/2}" --max-per-file 10 --max-total 50`: `0` lines across `0/746` files.
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh search issues "2606.01037"`: only `the-omega-institute/trureturing#8550` (inspected directly — covers Conjecture 5.23 via Matthews 1982, not Section 6 Question 6.1).
   - `gh search prs "2606.01037"` & `gh search repos "2606.01037"`: `0` hits.
   - `gh search code "2606.01037"`: 12 hits — `10m-u/open-problems-catalog` (`Q3704`/`Q3705`, open problem catalog listing `2606.01037v1`), `ehijano/rss_fetch`, `koutya0akari/arxiv-plug-in-for-mixi2`, and unrelated CSV numeric logs.
   - `the-omega-institute/trureturing` `dev` tree (`2606|01037|fernando|kousik`) and PRs up to `#34934`: `0` hits.
3. **Live Preprint / Citation APIs & Web (`17:29:39Z`):**
   - **arXiv API (`id_list=2606.01037`, `all:"Neranga Fernando" OR all:"Bhitali Kousik"`, `all:"g_{n,q}" OR all:"2606.01037"`):** `2606.01037v1` (`2026-05-31T06:04:17Z`) is sole version; authors' later paper `2608.09149v2` concerns quandles; no follow-up on `g_{n,q}` after `2606.01037v1`.
   - **OpenAlex (`doi.org/10.48550/arXiv.2606.01037`):** `cited_by_count: 0`.
   - **Zenodo (`q=2606.01037`):** `0` hits; **OpenCitations:** `[]`.
   - **`search_web` (`"2606.01037" OR ("Neranga Fernando" "Bhitali Kousik" "Question 6.1") OR ("A further study of polynomial" "Fernando")`)**: returns only `arXiv:2606.01037v1` abstract.

## Near-Misses & Coverage Limits
- **Near-miss:** `the-omega-institute/trureturing#8550` settles Conjecture 5.23 only (not Section 6 Question 6.1); `10m-u/open-problems-catalog` lists Question 6.1 (`Q3704`) as Open.
- **Coverage limits:** Live Semantic Scholar endpoint returned `HTTP 429` at `17:29Z`; private/unindexed drafts posted after `2026-11-27T17:29:40Z` are not covered.
