# Gate 3 Novelty & Pre-Report Verification — `vasilyev-2611.20344-q7.10` (`watch-5`)

- **Target:** `targets/vasilyev-2611.20344-q7.10/` — Oleg Vasilyev, *"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"*, `arXiv:2611.20344v2`, Subsection 5.4 & Section 7 Question 7.10 (`q:supremum`, **YES**: $\sup_{S, C} \pi_C(S) = \log_3 2$).
- **Checked UTC:** `2026-11-27T17:09:02Z`–`2026-11-27T17:09:11Z`
- **Gate 3 Verdict:** **PASS (UNCONTESTED + CHECKER PASS)** — fresh (<1h) live novelty checks confirm open/uncontested status and independent checker passes cleanly.

## Fresh Live Novelty Queries (`17:09Z`)
1. **Local snapshots (`watch/snapshots/**`, 745 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.20344" "q:supremum" "73/174" "uniformly descending" --max-per-file 10 --max-total 60`: `21` lines across `9/745` files, matching `2611.20344` only (`s66lem`, `OjasMor`, `andrheabacor` cover only Q7.1/Q7.7; `0` hits on `q:supremum`, `73/174`, `uniformly descending`).
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.20344"`: only `the-omega-institute/trureturing#32194` (Q7.7 `q:forcing`); `gh search prs "2611.20344"`: `0` hits.
   - `the-omega-institute/trureturing` recent PRs up to `#34929`: `0` overlapping PRs.
3. **Live Preprint & Citation APIs (`17:09:10Z`):**
   - `arXiv` API (`id_list=2611.20344`): `2611.20344v2` (`2026-11-18T03:50:40Z`) remains latest version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2611.20344`): `cited_by_count: 1` (unchanged from Gate 2 at `16:52Z`, where S2/Zenodo/GitHub confirmed external resolutions address only Q7.1, Q7.7, Q7.12).
   - `Zenodo` (`q=2611.20344`): `0` hits.

## Independent Checker Verification
- Command: `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py`
- Exit code: `0` (all `[PASS]` blocks verified: primary source & §5.4/§7 numbering, Table 5.3, Lemma 1, Lemmas 2–5 & Theorem 6 across 5 Barina sieve instances checking `57344` length-`n` paths, `PASS`).
- Verified files present: `targets/vasilyev-2611.20344-q7.10/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`.

## Near-Misses & Coverage Limits
- **Near-misses:** External resolutions of `arXiv:2611.20344` cover only Q7.1 (`s66lem`, `OjasMor`, `andrheabacor`, Zenodo `24567319`), Q7.7 (`trureturing#32194`, `OjasMor`), and Q7.12 (`Mira-Cult/math`); internal `vasilyev-2611.20344-q7.3` covers Q7.3.
- **Coverage limits:** Private/unindexed drafts posted after `2026-11-27T17:09:11Z` are not covered.
