# Gate 2 Novelty Check — `fernando-2606.01037-quesQ4` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:28:05Z`–`2026-11-27T18:28:26Z`
- **Target:** `targets/fernando-2606.01037-quesQ4/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.4 (`\label{Q4}`, `draftMay31.tex` L923–926)
- **Claimed result:** Complete iff classification ($g_{n,q} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}$ is a PP of $\mathbb{F}_{q^e}$ for even $q = 2^m > 2$, $e > 2$ iff $(q, e) = (4, 4)$, proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Question 6.4" "S_2^{q-2}"`):**
   - `5` lines across `3/760` files, all unrelated `aliromman/math` `#93` (Lundström–Saud Maia Leite Question 6.4); `0` hits on `2606.01037` or Fernando–Kousik Question 6.4.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:28:05Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`, Stanley proper diameter six) — unrelated.
   - `research` = `6b0452a9aff2e4c47e16937db82c0c37d7b8e0f7` (`2026-11-27T18:26:39Z`, forward width obstruction) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, Conjecture 5.23 only, not Section 6 Question 6.4).
   - `gh search code '"2606.01037" "Question 6.4"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Web search -> only `arXiv:2606.01037` and `https://nerangafernando.github.io/`; `0` resolutions of Section 6 Question 6.4.

## Coverage Limits
- Covers `watch/snapshots` (`760` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and public web search as of `2026-11-27T18:28:26Z`; private repositories and non-indexed preprints remain unobservable.
