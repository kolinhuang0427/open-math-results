# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/fernando-2606.01037-quesQ4/`

- **Target:** Neranga Fernando & Bhitali Kousik, `arXiv:2606.01037v1` (*"A further study of polynomial $g_{n,q}$ over finite fields"*, `2026-05-31`), Section 6 (`draftMay31.tex` L923–926), **Question 6.4** (`\label{Q4}`): $g_{n,q} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ ($n=(q-1)+(q-2)q^2+q^e+q^{e+2}$) is a PP of $\mathbb{F}_{q^e}$ for even $q=2^m>2$ and integer $e>2$ **iff $(q, e) = (4, 4)$**.
- **Checked UTC:** `2026-11-27T18:59:32Z` – `2026-11-27T19:01:50Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior settlement of Question 6.4 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `790` files after Sweep 20) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2606.01037 "fernando-2606.01037" "quesQ4" "Question 6.4" "Kousik" --max-per-file 0 --max-total 40` -> `16` lines across `6/790` files (unrelated `Lundström and Saud Maia Leite Question 6.4` in `aliromman/math` & `RESULTS.md`/our own `Q1`/`Q3`; `0` hits on `quesQ4`).
   - `RESULTS.md` contains only `fernando-2606.01037-quesQ1` and `fernando-2606.01037-quesQ3`; `0` entries for Question 6.4.
2. **Live GitHub (`2026-11-27T18:59:32Z`–`19:01:50Z`):**
   - `gh search code '"2606.01037"'` -> `kolinhuang0427/open-math-results` (our own `Q1`/`Q3` reports) and `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) only.
   - `gh search code '"Question 6.4" "g_{n,q}"'`, `gh search repos "2606.01037"`, `gh search prs "2606.01037"` -> `0` hits on all three.
   - `gh search issues "2606.01037"` -> `the-omega-institute/trureturing#8550` (`closed`, Conjecture 5.23 only).
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T18:59:32Z`–`19:01:50Z`):**
   - `https://export.arxiv.org/api/query?id_list=2606.01037` -> `2606.01037v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2606.01037`, `q=Fernando`, `q=Kousik`) -> `total=0`; `papex.org` `0/20`; Zenodo `0` hits; OpenAlex `0` indexed records; `search_web` clear.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py` -> exit `0`, `PASS` (`Lemmas 2.1–2.2` and `Cases 1–6` including $e=6$ $\mathbb{F}_{32}$ local expansion, $e=4$ $m \le 37$ witnesses, and $m \ge 38$ Cafure–Matera).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach.
