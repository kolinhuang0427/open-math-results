# Gate 3 Novelty & Pre-Report Verification — `fernando-2606.01037-quesQ3` (`watch-5`)

- **Target:** `targets/fernando-2606.01037-quesQ3/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1`, Section 6 Question 6.3 (`\label{Q3}`): complete classification ($q=4$ and $4\mid e$).
- **Checked UTC:** `2026-11-27T17:53:41Z`–`2026-11-27T17:54:02Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`17:53Z`)
1. **Local snapshots (`watch/snapshots/**`, 760 files incl. 14 newly ingested repos):**
   - `.venv/bin/python tools/novelty_grep.py "2606.01037" "Kousik" "S_{e/2+1}" "g_{n,q}" --max-per-file 10 --max-total 50`: `0` lines across `0/760` files.
2. **Live GitHub (`gh`):**
   - `gh search issues "2606.01037"`: only `the-omega-institute/trureturing#8550` (Conjecture 5.23 only); `gh search prs "2606.01037"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34939`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs (`17:53:58Z`):**
   - `arXiv` API (`id_list=2606.01037`): `2606.01037v1` (`2026-05-31T06:04:17Z`) sole version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2606.01037`): `cited_by_count: 0`.
   - `Zenodo` (`q=2606.01037`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py`
- Exit code: `0` (`Primary g_{n,q} & exhaustive PP checks: PASS`, `Section 1 & Theorem 3.1: PASS`, `Section 4 Carlitz-Uchiyama check: PASS`, `Section 5: PASS`, `PASS`).
- Verified files present: `targets/fernando-2606.01037-quesQ3/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** `the-omega-institute/trureturing#8550` settles Conjecture 5.23 only; sibling `fernando-2606.01037-quesQ1/` (`76b8077`) settles Question 6.1 only.
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T17:54:02Z` are not covered.
