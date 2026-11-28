# Gate 3 Novelty & Pre-Report Verification — `fernando-2606.01037-quesQ4` (`watch-5`)

- **Target:** `targets/fernando-2606.01037-quesQ4/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1`, Section 6 Question 6.4 (`\label{Q4}`: complete iff classification — $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff $(q, e) = (4, 4)$).
- **Checked UTC:** `2026-11-27T18:59:27Z`–`2026-11-27T19:01:40Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`18:59Z`)
1. **Local snapshots (`watch/snapshots/**`, 787 files):**
   - `.venv/bin/python tools/novelty_grep.py "2606.01037" "Kousik" "S_e^2" "S_2^{q-1}" --max-per-file 10 --max-total 50`: only our `citing_papers.{md,json}` (`OpenAlex cited_by=0; S2=0`) and `last_sweep_report.json` tracking (`11` lines across `3/787` files; `0` competing settlements).
2. **Live GitHub (`gh`):**
   - `gh search issues "2606.01037"`: only `the-omega-institute/trureturing#8550` (Conjecture 5.23 only); `gh search prs "2606.01037"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34947`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs (`18:59:46Z`):**
   - `arXiv` API (`id_list=2606.01037`): `2606.01037v1` (`2026-05-31T06:04:17Z`) sole version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2606.01037`): `cited_by_count: 0`.
   - `Zenodo` (`q=2606.01037`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py`
- Exit code: `0` (all `[PASS]` blocks verified: primary source verbatim, Lemmas 2.1–2.2, Cases 1–6 incl. local $\mathbb{F}_{32}$ expansion, $m=3..37$ collisions & Cafure–Matera for $m \ge 38$, `PASS`).
- Verified files present: `targets/fernando-2606.01037-quesQ4/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** `the-omega-institute/trureturing#8550` settles Conjecture 5.23 only; siblings `fernando-2606.01037-ques{Q1,Q3}` settle Q6.1 and Q6.3 only.
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T19:01:40Z` are not covered.
