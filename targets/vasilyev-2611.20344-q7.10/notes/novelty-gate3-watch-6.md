# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/vasilyev-2611.20344-q7.10/`

- **Target:** Oleg Vasilyev, `arXiv:2611.20344v2` (*"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"*, updated `2026-11-18T03:50:40Z`), Subsection 5.4 (`sec:uniform`, Table 5.3) & Section 7, **Question 7.10** (`\label{q:supremum}`): is $\sup_{S, C} \pi_C(S) = \log_3 2$ over all uniformly descending periodic sets $S$? (**YES**, proved).
- **Checked UTC:** `2026-11-27T17:09:07Z` – `2026-11-27T17:09:31Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 7.10 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `745` files after Sweep 17) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2611.20344 "vasilyev-2611.20344" "q:supremum" "Q7.10" "73/174" "tab:uniformcount" --max-per-file 0 --max-total 50` -> `21` lines across `9/745` files (`watch/snapshots/arxiv/*`, `OjasMor/arxiv-conjectures`, `andrheabacor/open-conjecture-results`, `s66lem/conjectures`), covering only Q7.1 (other repos) and `vasilyev-2611.20344-q7.3` (`RESULTS.md` has only Q7.3); `0` hits on Question 7.10 / `q:supremum` / `73/174` / `tab:uniformcount`.
2. **Live GitHub (`2026-11-27T17:09:07Z`–`17:09:31Z`):**
   - `gh search code '"2611.20344"'` -> `anghel4d/broadside-observer` (`seeds/cards/2641-...md` summary card) and `chokmah-me/fragile-proof-audit` (`docs/audits/harvest-2026-11-23/ledger.json` indexing Vasilyev's preprint `NON-GITHUB`).
   - `gh search code '"vasilyev-2611.20344"'`, `gh search code '"q:supremum"'`, `gh search repos "2611.20344"`, `gh search prs "2611.20344"` -> `0` hits on all four.
   - `gh search issues "2611.20344"` / `trureturing` issues -> `the-omega-institute/trureturing#32194` (`OPEN`, Question 7.7 refutation only).
   - `the-omega-institute/trureturing` `dev` tree (`2611.20344|2611_20344|vasilyev|7_10|7.10`) -> `VasilyevForceDivergenceRefutation` (Question 7.7 only).
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:09:07Z`–`17:09:31Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.20344` -> `2611.20344v2` (`2026-11-18T03:50:40Z`) sole latest version.
   - `https://hexagonmath.org/api/v1/works` (`q=2611.20344`, `q=Vasilyev`) -> `total=0` (`q=supremum` -> `24` unrelated hits).
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2611.20344` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2611.20344` -> `0` indexed records (prior snapshot `citing_papers.md` `OpenAlex cited_by=1` already verified unrelated in `notes/novelty-attack.md`).
   - `search_web` (`"2611.20344" OR ("Vasilyev" "q:supremum") OR ("Vasilyev" "log_3 2" "7.10")`) -> returns only Vasilyev's `arXiv:2611.20344` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/vasilyev-2611.20344-q7.10/notes/check-check-2.py` -> exit `0`, `PASS` (`57344` length-$n$ paths checked across 5 Barina sieve instances).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and paywalled/auth-gated forums are outside reach.
