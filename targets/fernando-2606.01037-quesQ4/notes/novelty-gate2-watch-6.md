# Gate 2 Novelty Receipt (`watch-6`) — `targets/fernando-2606.01037-quesQ4/`

- **Target:** Neranga Fernando & Bhitali Kousik, `arXiv:2606.01037v1` (*"A further study of polynomial $g_{n,q}$ over finite fields"*, `2026-05-31`), Section 6 (`draftMay31.tex` L923–926), **Question 6.4** (`\label{Q4}`): conditions on even $q>2$ and integer $e>2$ for $g_{n,q} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ ($n=(q-1)+(q-2)q^2+q^e+q^{e+2}$) to be a PP of $\mathbb{F}_{q^e}$ (proved iff $(q,e)=(4,4)$).
- **Checked UTC:** `2026-11-27T18:28:09Z` – `2026-11-27T18:28:24Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 6.4 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `760` files after Sweep 19) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.01037 "fernando-2606.01037" "quesQ4" "Question 6.4" "Kousik" --max-per-file 0 --max-total 40` -> `5` lines across `3/760` files (unrelated `Lundström and Saud Maia Leite Question 6.4` in `aliromman/math` only; `0` hits on `2606.01037`, `quesQ4`, or `Kousik`).
   - `RESULTS.md` contains only `fernando-2606.01037-quesQ1` and `fernando-2606.01037-quesQ3`; `0` entries for Question 6.4.
2. **Live GitHub (`2026-11-27T18:28:09Z`–`18:28:21Z`):**
   - `gh search code '"2606.01037"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) only.
   - `gh search code '"fernando-2606.01037"'`, `gh search code '"Question 6.4" "g_{n,q}"'`, `gh search repos "2606.01037"`, `gh search prs "2606.01037"` -> `0` hits on all four.
   - `gh search issues "2606.01037"` -> `the-omega-institute/trureturing#8550` (`closed`, Conjecture 5.23 only); `trureturing` `dev` tree (`2606\.01037|2606_01037|fernando|kousik`) -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T18:28:09Z`–`18:28:24Z`):**
   - `https://export.arxiv.org/api/query?id_list=2606.01037` -> `2606.01037v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.01037`, `q=Fernando`, `q=Kousik`) -> `total=0` on all three.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2606.01037` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2606.01037` -> `0` indexed records.
   - `search_web` (`"2606.01037" ("Question 6.4" OR "Q4" OR "S_2^{q-2}" OR "(4,4)")`) -> returns only Fernando & Kousik's `arXiv:2606.01037` preprint.

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.
