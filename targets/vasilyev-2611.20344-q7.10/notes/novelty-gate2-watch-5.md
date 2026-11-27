# Gate 2 Novelty Receipt — `vasilyev-2611.20344-q7.10` (`watch-5`)

- **Target:** `targets/vasilyev-2611.20344-q7.10/` — Oleg Vasilyev, *"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"*, `arXiv:2611.20344v2`, Section 7, Question 7.10 (`\label{q:supremum}`): is $\sup \pi_C(S) = \log_3 2$ over all uniformly descending periodic sets $S$?
- **Checked UTC:** `2026-11-27T16:52:21Z`–`2026-11-27T16:52:47Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no proof or counterexample settling Question 7.10 (`q:supremum`) found across snapshots, live GitHub, arXiv, Zenodo, S2, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 743 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.20344" "q:supremum" "73/174" "uniformly descending" --max-per-file 10 --max-total 60`: `21` lines across `9/743` files, all matching `2611.20344` only (`0` hits on `q:supremum`, `73/174`, `uniformly descending`):
     - `arxiv_submissions.{json,md}`, `state.json`, `citing_papers.{md,json}`, `last_sweep_report.json`
     - `OjasMor__arxiv-conjectures.json` (Q7.1 & Q7.7 only)
     - `andrheabacor__open-conjecture-results.json` (Q7.1 only)
     - `s66lem__conjectures.json` (Q7.1 only)
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.20344"`: only `the-omega-institute/trureturing#32194` (Q7.7 `q:forcing`).
   - `gh search prs "2611.20344"`, `gh search repos "2611.20344"`, `gh search code "73/174" "Vasilyev"`: `0` hits; `gh search code "q:supremum"`: unrelated physics/math files.
   - `the-omega-institute/trureturing` `dev` tree (`20344|vasilyev|collatz`) and PRs up to `#34927`: only `VasilyevForceDivergenceRefutation` (Q7.7); `0` hits on Q7.10.
   - `the-omega-institute/trureturing-experiments` `main` tree: `0` Vasilyev/Q7.10 files.
3. **Live Preprint / Citation APIs & Web:**
   - **arXiv API (`id_list=2611.20344`):** `2611.20344v2` (`2026-11-18T03:50:40Z`) remains latest version.
   - **Semantic Scholar (`ARXIV:2611.20344`):** `citationCount: 0`.
   - **OpenAlex (`doi.org/10.48550/arXiv.2611.20344`):** `cited_by_count: 1` (citer endpoint returned `HTTP 429` at `16:52Z`; S2/Zenodo/GitHub confirm prior external resolutions address only Q7.1, Q7.7, Q7.12).
   - **Zenodo (`q=2611.20344`):** `0` hits (`q=Vasilyev+Collatz` previously verified to return only Zenodo `24567319` for Q7.1).
   - **`search_web` (`"2611.20344" ("7.10" OR "supremum" OR "log_3 2" OR "73/174" OR "uniformly descending")`)**: returns only `arXiv:2611.20344` question text itself.

## Near-Misses & Coverage Limits
- **Near-misses:** External resolutions of `arXiv:2611.20344` cover only Q7.1 (`s66lem`, `OjasMor`, `andrheabacor`, Zenodo `24567319`), Q7.7 (`trureturing#32194`, `OjasMor`), and Q7.12 (`Mira-Cult/math`); internal `vasilyev-2611.20344-q7.3` covers Q7.3. None address Q7.10 (`q:supremum`).
- **Coverage limits:** OpenAlex `cited_by_api_url` returned `HTTP 429` at `16:52Z`; private/unindexed drafts posted after `2026-11-27T16:52:47Z` are not covered.
