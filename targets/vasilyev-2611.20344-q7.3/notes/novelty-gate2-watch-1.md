# Novelty Gate 2 Receipt — `targets/vasilyev-2611.20344-q7.3`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T13:56:25Z`
- **Verdict:** **PASS — OPEN (no competing settlement of Question 7.3 `q:types` found)**

## Exact Queries & Findings

1. **Snapshot Grep (`watch/snapshots/` across `720` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.20344" "Vasilyev" "q:types" "rem:types" "up-down graph" "infinitely many cycles" --max-per-file 5 --max-total 60`
   - Result: `28` lines across `9/720` files — all external hits target **different questions** in `2611.20344v2`:
     - `OjasMor__arxiv-conjectures.json`, `andrheabacor__open-conjecture-results.json`, `s66lem__conjectures.json`, `zenodo-2026-oeis-compendia-ids.md` (`Zenodo 24567319`): **Question 7.1** (`q:ratio`, cycle ratio $2^\ell < 3^{a+1}$).
     - `the-omega-institute__trureturing.json` (`Problems/vasilyev-2026-force-divergence-question-7-7.md`, `D5/.../VasilyevForceDivergenceRefutation.lean`): **Question 7.7** (`q:forcing`).
     - `1337isnot1337/solved-conjectures` snapshots: `0` hits.

2. **Live GitHub:**
   - `gh search prs "2611.20344"` -> `0` matches.
   - `gh search issues "2611.20344"` -> `1` match (`the-omega-institute/trureturing#32194`, Question 7.7 `q:forcing` only).
   - `gh search code "2611.20344"` -> `20` matches: `s66lem/conjectures` (Q7.1), `the-omega-institute/trureturing` (Q7.7), `Mira-Cult/math` (`notes/number-theory/collatz/density-zero-modification.md`, Q7.12 — verified verbatim via `gh api` to have `0` hits for `7.3|q:types|rem:types|infinitely many cycles|divergent orbit`), `anghel4d/broadside-observer` & `chokmah-me/fragile-proof-audit` (paper summary/audit notes only), plus 4 unrelated numeric CSVs.
   - `gh search code '"up-down graph" Collatz OR Vasilyev'` -> `0` matches.
   - `gh search code 'repo:the-omega-institute/trureturing Vasilyev'` -> `0` matches (no Q7.3).

3. **Live Zenodo, arXiv, Web:**
   - Zenodo API (`2611.20344 OR "up-down graph" OR "Up or down at every integer"`): `2` hits (`24567319` = Q7.1 cycle-ratio counterexample; `24283375` = unrelated knot theory).
   - arXiv API (`id_list=2611.20344`): latest version remains `arXiv:2611.20344v2` (`2026-11-18T03:50:40Z`); no `v3`.
   - `search_web`: queries for `"2611.20344"`, `"Question 7.3"`, `"q:types"`, `"infinitely many cycles" "divergent"`, `"Mira-Cult"` found only Vasilyev's preprint and mirrors; no resolution of Question 7.3.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs remained rate-limited (`429` noted in `notes/novelty-attack.md`). Independent Gate 3 final check remains recommended before `RESULTS.md` publication.
