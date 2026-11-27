# Gate 2 Novelty Receipt (`watch-6`) — `targets/vasilyev-2611.20344-q7.3/`

- **Checked UTC:** `2026-11-27T13:56:28Z`–`2026-11-27T13:56:50Z`
- **Target:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (2026-11-18), Section 7 **Question 7.3** (`\label{q:types}` / Remark 4.4 `\label{rem:types}`: existence of $T_S$ with infinitely many cycles and a divergent orbit).
- **Verdict:** **OPEN / PASS**

## Exact Queries & Results

1. **Local Snapshot Grep (`.venv/bin/python tools/novelty_grep.py` across `720` snapshots):**
   - `2611.20344` -> hits `watch/snapshots/arxiv/*` indices and `OjasMor__arxiv-conjectures`, `andrheabacor__open-conjecture-results`, `s66lem__conjectures` — all three address ONLY **Question 7.1** (cycle inequality $2^\ell < 3^{a+1}$), NOT Question 7.3 (`q:types`).
   - `Vasilyev` -> hits above plus `the-omega-institute__trureturing` (`VasilyevForceDivergenceRefutation.{md,lean}`), which cites `2611.20344v2#S7.Thmtheorem7` (**Question 7.7**, forcing divergence), NOT Question 7.3 (`q:types`).
   - `q:types`, `rem:types`, `up-down graph` -> `0` settlements (`0/720`).
2. **Live GitHub (`gh` CLI) & `trureturing` `dev`:**
   - `gh search repos "2611.20344"` / `gh search prs "2611.20344"` -> `[]`.
   - `gh search issues "2611.20344"` -> solely `the-omega-institute/trureturing#32194` (open, Question 7.7 only).
   - `gh search code 2611.20344` & `"Vasilyev" "up-down"` -> `s66lem/conjectures` (Q7.1), `anghel4d/broadside-observer` (seed card), `chokmah-me/fragile-proof-audit` (Q7.1 harvest), and `the-omega-institute/trureturing` (`Problems/vasilyev-2026-force-divergence-question-7-7.md` + `dev` branch `VasilyevForceDivergenceRefutation.lean` — verified Q7.7 only).
   - `gh search code '"q:types"'` -> unrelated LaTeX/Rust files, `0` Vasilyev hits.
3. **Live arXiv, Zenodo & Web Search:**
   - `export.arxiv.org/api/query?id_list=2611.20344` -> sole latest version `2611.20344v2` (`2026-11-18T03:50:40Z`); `au:Vasilyev+AND+all:Collatz` -> only `2611.10311v1` and `2611.20344v2`.
   - `zenodo.org/api/records?q=2611.20344` -> `0`; `q=Vasilyev+Collatz` -> `24567319` (*A Counterexample to Vasilyev's Cycle Ratio Inequality*, Q7.1 only).
   - `search_web` -> returns only `arXiv:2611.20344` summaries.

## Coverage Limits

- Unindexed private repositories, non-indexed author webpages, or closed-access preprints remain outside live query visibility; all checked public sources confirm Question 7.3 (`q:types`) remains open.
