# Gate 3 Novelty & Pre-Report Verification — `ingrosso-2611.30155-q4.6` (`watch-5`)

- **Target:** `targets/ingrosso-2611.30155-q4.6/` — E. Ingrosso, M. Trombetti, and A. Zitouni, *"Groups with dual classes of subgroups"*, `arXiv:2611.30155v1` / *J. Aust. Math. Soc.* DOI `10.1017/s1446788726101682`, Section 4 Question 4.6 (smallest possible subnormal defect in Theorem 4.5 = $2$).
- **Checked UTC:** `2026-11-27T16:37:22Z`–`2026-11-27T16:37:39Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`16:37Z`)
1. **Local snapshots (`watch/snapshots/**`, 742 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.30155" "Ingrosso" "10.1017/s1446788726101682" --max-per-file 10 --max-total 50`: only `arxiv_submissions.{json,md}` and `state.json` (7 lines across 3 files).
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.30155"` & `gh search prs "2611.30155"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34921`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs:**
   - `arXiv` API (`id_list=2611.30155`): `2611.30155v1` (`2026-11-23T07:03:10Z`) sole version.
   - `OpenAlex` (`doi.org/10.1017/s1446788726101682`): `cited_by_count: 0`.
   - `Zenodo` (`q=2611.30155`): `0` hits.
   - `Semantic Scholar` (`ARXIV:2611.30155`): `HTTP 429` at `16:37Z` (verified `citationCount: 0` at `16:33Z`, 4 minutes earlier).

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py`
- Exit code: `0` (`M_16`, `D_8`, `S_3 x S_3`, `M_16 x| C_3`: `OK`, `PASS`).
- Verified files present: `targets/ingrosso-2611.30155-q4.6/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** `eliottcassidy2000/math` `THM-4728` and `atlas-lean` Kourovka pronormal files are distinct problems (verified in Gate 2).
- **Coverage limits:** Live S2 call at `16:37Z` returned `HTTP 429` (checked `citationCount: 0` at `16:33Z`); private/unindexed drafts posted after `2026-11-27T16:37:39Z` are not covered.
