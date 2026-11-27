# Gate 2 Novelty Receipt (`watch-6`) — `targets/fernando-2606.01037-quesQ3/`

- **Target:** Neranga Fernando & Bhitali Kousik, `arXiv:2606.01037v1` (*"A further study of polynomial $g_{n,q}$ over finite fields"*, `2026-05-31`), Section 6 (`draftMay31.tex` L911–915), **Question 6.3** (`\label{Q3}`): conditions on even $q>2$ and even $e>0$ for $g_{1+(q-1)q^{e/2}+(q-1)q^e} = S_{e/2+1}^{q^{e/2}} + S_e + S_e(S_{e/2}^{q^{e/2}})^{q-1}$ to be a PP of $\mathbb{F}_{q^e}$ (proved iff $q=4$ and $4\mid e$).
- **Checked UTC:** `2026-11-27T17:41:29Z` – `2026-11-27T17:41:41Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 6.3 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `746` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.01037 "fernando-2606.01037" "quesQ3" "Question 6.3" "Kousik" --max-per-file 0 --max-total 40` -> `5` lines across `3/746` files (unrelated `Mosquera-Lois–Tanaka Question 6.3` in `trureturing`; `0` hits on `2606.01037`, `quesQ3`, or `Kousik`).
   - `RESULTS.md` contains only `targets/fernando-2606.01037-quesQ1/` (Question 6.1, `76b8077`); `0` entries for Question 6.3.
2. **Live GitHub (`2026-11-27T17:41:29Z`):**
   - `gh search code '"2606.01037"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) only.
   - `gh search code '"fernando-2606.01037"'`, `gh search code '"Question 6.3" "g_{n,q}"'`, `gh search repos "2606.01037"`, `gh search prs "2606.01037"` -> `0` hits on all four.
   - `gh search issues "2606.01037"` -> `the-omega-institute/trureturing#8550` (`closed`, Conjecture 5.23 only); `trureturing` `dev` tree (`2606\.01037|2606_01037|fernando|kousik`) -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:41:29Z`–`17:41:41Z`):**
   - `https://export.arxiv.org/api/query?id_list=2606.01037` -> `2606.01037v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.01037`, `q=Fernando`, `q=Kousik`) -> `total=0` on all three.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2606.01037` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2606.01037` -> `0` indexed records.
   - `search_web` (`"2606.01037" ("Question 6.3" OR "Q3" OR "2q-1" OR "q=4")`) -> returns only Fernando & Kousik's `arXiv:2606.01037` preprint.

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.
