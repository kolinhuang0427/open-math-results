# Gate 2 Novelty Receipt — `fernando-2606.01037-quesQ4` (`watch-5`)

- **Target:** `targets/fernando-2606.01037-quesQ4/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1`, Section 6 Question 6.4 (`\label{Q4}`): complete classification ($q = 4, e = 4$) for $g_{n,q} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ to be a PP of $\mathbb{F}_{q^e}$ ($q>2$ even, $e>2$).
- **Checked UTC:** `2026-11-27T18:28:04Z`–`2026-11-27T18:28:22Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no proof or resolution of Question 6.4 found across snapshots, citing papers, live GitHub, arXiv, Zenodo, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 760 files):**
   - `.venv/bin/python tools/novelty_grep.py "2606.01037" "Kousik" "S_e^2" "S_2^{q-1}" --max-per-file 10 --max-total 50`: `0` lines across `0/760` files.
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits; internal siblings `fernando-2606.01037-ques{Q1,Q3}` solve only Q6.1 and Q6.3.
2. **Live GitHub (`gh`):**
   - `gh search issues "2606.01037"`: only `the-omega-institute/trureturing#8550` (Conjecture 5.23 via Matthews 1982, not Q6.4).
   - `gh search prs "2606.01037"`: `0` hits; `trureturing` PRs up to `#34944`: `0` hits.
   - `10m-u/open-problems-catalog` (`#q3705`): lists Question 6.4 as Open.
3. **Live Preprint & Citation APIs & Web (`18:28:21Z`):**
   - `arXiv` API (`id_list=2606.01037`): `2606.01037v1` (`2026-05-31T06:04:17Z`) sole version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2606.01037`): `cited_by_count: 0`.
   - `Zenodo` (`q=2606.01037`): `0` hits.
   - `search_web` (`"2606.01037" ("Question 6.4" OR "6.4" OR "S_2^{q-1}" OR "S_e^2")`): returns only `arXiv:2606.01037v1` abstract.

## Near-Misses & Coverage Limits
- **Near-misses:** `the-omega-institute/trureturing#8550` settles Conjecture 5.23 only; siblings `fernando-2606.01037-ques{Q1,Q3}` settle Q6.1 and Q6.3 only.
- **Coverage limits:** Live Semantic Scholar endpoint was rate-limited (`HTTP 429`); private/unindexed drafts posted after `2026-11-27T18:28:22Z` are not covered.
