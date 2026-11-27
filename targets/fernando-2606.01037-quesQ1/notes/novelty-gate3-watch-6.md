# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/fernando-2606.01037-quesQ1/`

- **Target:** Neranga Fernando & Bhitali Kousik, `arXiv:2606.01037v1` (*"A further study of polynomial $g_{n,q}$ over finite fields"*, submitted `2026-05-31`), Section 6 (`draftMay31.tex` L893–895), **Question 6.1** (`\label{Q1}`): complete iff classification of when $g_{n,q} = S_1 + S_{e/2}^{q^{e/2}} + S_e \cdot S_{e/2}^{q-1}$ is a PP of $\mathbb{F}_{q^e}$ for even $q=2^m>2$ and even $e>0$ (**iff ($q=4$ and $4\mid e$) or ($e=4$ and $m\not\equiv 3\pmod 4$)**).
- **Checked UTC:** `2026-11-27T17:38:06Z` – `2026-11-27T17:38:30Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 6.1 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `746` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.01037 "fernando-2606.01037" "quesQ1" "Fernando" "Kousik" "g_{n,q}" --max-per-file 0 --max-total 40` -> `9` lines across `4/746` files (unrelated `Lakshitha Fernando` `2611.12065` & `Fernando C. Tura`; `0` hits on `2606.01037`, `quesQ1`, `Kousik`, or `g_{n,q}`).
   - `RESULTS.md` scan (`2606\.01037|fernando|kousik`) -> `[]`.
2. **Live GitHub (`2026-11-27T17:38:06Z`–`17:38:30Z`):**
   - `gh search code '"2606.01037"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) only.
   - `gh search code '"fernando-2606.01037"'`, `gh search code '"Question 6.1" "g_{n,q}"'`, `gh search repos "2606.01037"`, `gh search prs "2606.01037"` -> `0` hits on all four.
   - `gh search issues "2606.01037"` -> `the-omega-institute/trureturing#8550` (`closed`, Conjecture 5.23 only).
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` matching `2606\.01037|2606_01037|fernando|kousik` -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:38:06Z`–`17:38:30Z`):**
   - `https://export.arxiv.org/api/query?id_list=2606.01037` -> `2606.01037v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.01037`, `q=Fernando`, `q=Kousik`) -> `total=0` on all three.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2606.01037` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2606.01037` -> `0` indexed records.
   - `search_web` (`"2606.01037" ("Question 6.1" OR "Q1" OR "e=4" OR "q=4")`) -> returns only Fernando & Kousik's `arXiv:2606.01037` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py` -> exit `0`, `PASS` (`Parts 1–5: OK`).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach.
