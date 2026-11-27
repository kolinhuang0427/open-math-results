# Gate 2 Novelty Receipt (`watch-6`) — `targets/vasilyev-2611.20344-q7.10/`

- **Target:** Oleg Vasilyev, `arXiv:2611.20344v2` (*"Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph"*, updated `2026-11-18`), Section 7, **Question 7.10** (`\label{q:supremum}`): is $\sup \pi_C(S) = \log_3 2$ over all uniformly descending periodic sets $S$? (**YES**, proved).
- **Checked UTC:** `2026-11-27T16:52:29Z` – `2026-11-27T16:52:52Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 7.10 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `743`+ indexed files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.20344 "vasilyev-2611.20344" "q:supremum" "uniformly descending" "73/174" "tab:uniformcount" --max-per-file 0 --max-total 50` -> `21` lines across `9/743` files: `watch/snapshots/arxiv/` entries (`2611.20344v2`, `OpenAlex cited_by=1; S2=0`), plus `OjasMor/arxiv-conjectures`, `andrheabacor/open-conjecture-results`, and `s66lem/conjectures` — all settling **Question 7.1** (or Q7.3/Q7.7/Q7.12 elsewhere) only, `0` hits on Question 7.10 / `q:supremum` / `73/174`.
   - `0` hits in `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `hwzw-algebra-number-theory-drafts.md`, `insorrowmeow-oeis-ids.md`.
2. **Live GitHub (`2026-11-27T16:52Z`):**
   - `gh search code '"2611.20344"'` -> `anghel4d/broadside-observer` (`seeds/cards/2641-...md`, summary card of Vasilyev `v1`) and `chokmah-me/fragile-proof-audit` (`docs/audits/harvest-2026-11-23/ledger.json`, entry `collatz-up-down-graph` indexing Vasilyev's original `2611.20344` paper with `code.status: NON-GITHUB`).
   - `gh search repos "2611.20344"`, `gh search prs "2611.20344"`, `gh search code '"q:supremum"'`, `gh search code '"uniformly descending" "Collatz"'` -> `[]` on all four.
   - `gh search issues "2611.20344"` -> `the-omega-institute/trureturing#32194` (`state: OPEN`, `updatedAt: 2026-11-20T10:45:53Z`, Question 7.7 refutation only).
   - `the-omega-institute/trureturing` `dev` tree (`2611|20344|vasilyev`) -> `VasilyevForceDivergenceRefutation` (Question 7.7 only).
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:52Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.20344` -> `2611.20344v2` (`updated 2026-11-18T03:50:40Z`) remains the latest version.
   - `https://zenodo.org/api/records?q=2611.20344` -> `0` hits; `q="uniformly descending"` -> `1` unrelated astrophysics record (`21499054`).
   - Live `https://hexagonmath.org/api/v1/works` (`q=Vasilyev`, `q=2611.20344`, `q=uniformly descending`) -> `0` hits on all three.
   - `search_web` (`"2611.20344" ("7.10" OR "supremum" OR "73/174") OR ("uniformly descending" "log_3 2")`) -> returns only Vasilyev's `arXiv:2611.20344` preprint.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs were not queried (`citing_papers.md` shows `OpenAlex cited_by=1; S2=0`, previously checked as non-settling in `vasilyev10-lit`'s `notes/novelty-attack.md`).
- Independent Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
