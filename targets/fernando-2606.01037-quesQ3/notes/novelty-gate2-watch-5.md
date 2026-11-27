# Gate 2 Novelty Receipt — `fernando-2606.01037-quesQ3` (`watch-5`)

- **Target:** `targets/fernando-2606.01037-quesQ3/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1`, Section 6 Question 6.3 (`\label{Q3}`): complete classification ($q = 4$ and $4 \mid e$) for $g_{n,q} = S_{e/2+1}^{q^{e/2}} + S_e + S_e(S_{e/2}^{q^{e/2}})^{q-1}$ to be a PP of $\mathbb{F}_{q^e}$.
- **Checked UTC:** `2026-11-27T17:41:25Z`–`2026-11-27T17:41:35Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no proof or resolution of Question 6.3 found across snapshots, citing papers, live GitHub, arXiv, Zenodo, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 746 files):**
   - `.venv/bin/python tools/novelty_grep.py "2606.01037" "Kousik" "S_{e/2+1}" "g_{n,q}" --max-per-file 10 --max-total 50`: `0` lines across `0/746` files.
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits (verified in Q6.1 check at `17:29Z`).
   - Internal sibling `targets/fernando-2606.01037-quesQ1/` (`76b8077`) solves Question 6.1 only.
2. **Live GitHub (`gh`):**
   - `gh search issues "2606.01037"`: only `the-omega-institute/trureturing#8550` (Conjecture 5.23 via Matthews 1982, not Section 6 Question 6.3).
   - `gh search prs "2606.01037"`: `0` hits; `trureturing` PRs up to `#34934`: `0` hits.
   - `10m-u/open-problems-catalog` (`gh search code "2606.01037"` checked at `17:29Z`): lists only Q6.1 and Q6.4 as Open (Q6.3 absent).
3. **Live Preprint & Citation APIs & Web (`17:41:34Z`):**
   - `arXiv` API (`id_list=2606.01037`): `2606.01037v1` (`2026-05-31T06:04:17Z`) sole version (authors' later `2608.09149v2` is on quandles).
   - `OpenAlex` (`doi.org/10.48550/arXiv.2606.01037`): `cited_by_count: 0`.
   - `Zenodo` (`q=2606.01037`): `0` hits.
   - `search_web` (`"2606.01037" ("Question 6.3" OR "6.3" OR "S_{e/2+1}" OR "1 + (q-1)q^{e/2}")`): returns only `arXiv:2606.01037v1` abstract.

## Near-Misses & Coverage Limits
- **Near-misses:** `the-omega-institute/trureturing#8550` settles Conjecture 5.23 only; sibling `fernando-2606.01037-quesQ1/` settles Question 6.1 only.
- **Coverage limits:** Live Semantic Scholar endpoint was rate-limited (`HTTP 429`); private/unindexed drafts posted after `2026-11-27T17:41:35Z` are not covered.
