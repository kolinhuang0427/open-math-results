# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/fernando-2606.01037-quesQ3/`

- **Target:** Neranga Fernando & Bhitali Kousik, `arXiv:2606.01037v1` (*"A further study of polynomial $g_{n,q}$ over finite fields"*, submitted `2026-05-31`), Section 6 (`draftMay31.tex` L911–915), **Question 6.3** (`\label{Q3}`): complete iff classification of when $g_{1+(q-1)q^{e/2}+(q-1)q^e} = S_{e/2+1}^{q^{e/2}} + S_e + S_e(S_{e/2}^{q^{e/2}})^{q-1}$ is a PP of $\mathbb{F}_{q^e}$ for even $q=2^m>2$ and even $e>0$ (**iff $q=4$ and $4\mid e$**).
- **Checked UTC:** `2026-11-27T17:53:44Z` – `2026-11-27T17:54:13Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 6.3 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `760` files after Sweep 18) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.01037 "fernando-2606.01037" "quesQ3" "Question 6.3" "Kousik" --max-per-file 0 --max-total 40` -> `5` lines across `3/760` files (`Mosquera-Lois–Tanaka Question 6.3` in `trureturing` only; `0` hits on `2606.01037`, `quesQ3`, or `Kousik`).
   - `RESULTS.md` contains only `targets/fernando-2606.01037-quesQ1/` (Question 6.1, `76b8077`); `0` entries for Question 6.3.
2. **Live GitHub (`2026-11-27T17:53:44Z`–`17:54:13Z`):**
   - `gh search code '"2606.01037"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) only.
   - `gh search code '"fernando-2606.01037"'`, `gh search code '"Question 6.3" "g_{n,q}"'`, `gh search repos "2606.01037"`, `gh search prs "2606.01037"` -> `0` hits on all four.
   - `gh search issues "2606.01037"` -> `the-omega-institute/trureturing#8550` (`closed`, Conjecture 5.23 only); `trureturing` `dev` tree (`2606\.01037|2606_01037|fernando|kousik`) -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:53:44Z`–`17:54:13Z`):**
   - `https://export.arxiv.org/api/query?id_list=2606.01037` -> `2606.01037v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.01037`, `q=Fernando`, `q=Kousik`) -> `total=0` on all three.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2606.01037` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2606.01037` -> `0` indexed records.
   - `search_web` (`"2606.01037" ("Question 6.3" OR "Q3" OR "q=4" OR "S_{e/2+1}")`) -> returns only Fernando & Kousik's `arXiv:2606.01037` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py` -> exit `0`, `PASS` (`Primary g_{n,q}`, `Section 1 & Theorem 3.1`, `Section 4 Carlitz-Uchiyama`, `Section 5 Lemmas 5.2-5.4, Prop 5.1, Theorem 5.5`: PASS).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach.
