# Gate 3 Novelty & Pre-Report Verification — `saikia-2611.28840-conj8.1` (`watch-5`)

- **Target:** `targets/saikia-2611.28840-conj8.1/` — Manjil P. Saikia, *"Congruences modulo powers of $2$ and $3$ for Lin's function $\mathrm{PDO}_t(n)$"*, `arXiv:2611.28840v1`, §8 Conjecture 8.1 (`\label{conj:sharp}`).
- **Checked UTC:** `2026-11-27T16:17:15Z`–`2026-11-27T16:17:41Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`16:17Z`)
1. **Local snapshots (`watch/snapshots/**`, incl. newly ingested `jmadeiros/conjecture-desk` & `raghavs1729/Research-Math`):**
   - `.venv/bin/python tools/novelty_grep.py "2611.28840" "PDO_t" "conj:sharp" --max-per-file 10 --max-total 50`:
     - `raghavs1729/Research-Math` (`watch/snapshots/raghav-research-math-index.md`): lists `2611.28840` explicitly as `not attempted (budget)`.
     - `jmadeiros/conjecture-desk`: cites `2611.28840` only as unrelated background in `yaqubi-mirzavaziri/conj-6.{2,3-6.4}/REVIEW.md`.
     - Remaining hits: arXiv snapshot (`2611.28840v1`), `citing_papers.{md,json}` (`OA=0`, `S2=0`), and `trureturing#34564`.
2. **Live GitHub (`gh`):**
   - `gh search code` inside `raghavs1729/Research-Math` and `jmadeiros/conjecture-desk` (`2611.28840`): confirms only the 5 files above (`CANDIDATES.md`, `NOVELTY-1.md`, `NOVELTY-2.md`, and `yaqubi-mirzavaziri/conj-*/REVIEW.md`), zero solutions.
   - `gh issue view 34564 -R the-omega-institute/trureturing`: unchanged (`updatedAt: 2026-11-26T17:50:01Z`, 3 comments covering finite `12 <= k <= 32` only; `k >= 33` open).
   - `trureturing` recent PRs up to `#34914` and `trureturing-experiments` `main` (`63208158b4`, `2026-11-27T16:12:55Z`): `0` overlapping PRs/commits.
3. **Live Preprint & Citation APIs (`16:17:41Z`):**
   - `arXiv` API (`id_list=2611.28840`): `2611.28840v1` (`2026-11-21T14:45:07Z`) sole version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2611.28840`): `cited_by_count: 0`.
   - `Zenodo` (`q=2611.28840`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/saikia-2611.28840-conj8.1/notes/check-check-3.py`
- Exit code: `0` (`Part 1`..`Part 5: OK`, `PASS`).
- Verified files present: `targets/saikia-2611.28840-conj8.1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`.

## Near-Misses & Coverage Limits
- **Near-miss:** `the-omega-institute/trureturing#34564` verifies `12 <= k <= 32` computationally (`k >= 33` open).
- **Coverage limits:** Live S2 single-paper lookup hit `HTTP 429` at `16:06Z` (snapshot batch at `15:46Z` was `S2=0`); private/unindexed drafts after `16:17Z` are not covered.
