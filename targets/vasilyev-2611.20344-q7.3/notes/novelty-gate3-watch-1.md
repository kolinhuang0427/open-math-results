# Novelty Gate 3 Receipt — `targets/vasilyev-2611.20344-q7.3`

- **Checker:** `watch-1`
- **Timestamp (UTC):** `2026-11-27T14:02:02Z`
- **Verdict:** **PASS — OPEN (safe for `RESULTS.md` publication)**

## Freshness Verification (`<1h` before reporting)

1. **Snapshot Grep (`watch/snapshots/` across `721` files):**
   - Command: `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2611.20344" "Vasilyev" "q:types" "rem:types" "up-down graph" "infinitely many cycles" --max-per-file 5 --max-total 60`
   - Result: `28` lines across `9/721` files — all external hits address **different questions** in `2611.20344v2`:
     - `OjasMor__arxiv-conjectures.json`, `andrheabacor__open-conjecture-results.json`, `s66lem__conjectures.json`, `zenodo-2026-oeis-compendia-ids.md` (`Zenodo 24567319`): **Question 7.1** (`q:ratio`).
     - `the-omega-institute__trureturing.json` (`VasilyevForceDivergenceRefutation.lean`): **Question 7.7** (`q:forcing`).
     - `1337isnot1337/solved-conjectures` snapshots: `0` hits.

2. **Live GitHub (`2026-11-27T14:02Z`):**
   - `1337isnot1337/solved-conjectures` live heads: `main = bff783fd9bbe010663047ecaa93deb8fa6a3296a`, `research = 46b44ae954b410d5dcb03ad83aba2dcf65ad3f6e` (`2026-11-27T14:01:40Z`, `research/erdos-hajnal-tuza-local-transversals/SHARED-SUPPORT-VERSUS-ORDER.md` only); `0` Vasilyev/Collatz hits.
   - `gh search prs "2611.20344"` -> `0` matches.
   - `gh search issues "2611.20344"` -> `1` match (`the-omega-institute/trureturing#32194`, Question 7.7 `q:forcing` only).
   - `gh search code "2611.20344"` -> `20` matches: `s66lem/conjectures` (Q7.1), `the-omega-institute/trureturing` (Q7.7), `Mira-Cult/math` (Q7.12), `anghel4d/broadside-observer` & `chokmah-me/fragile-proof-audit` (summary/audit notes only), plus 4 unrelated CSVs. Zero Question 7.3 (`q:types`) resolutions.

3. **Live Zenodo, arXiv, Web (`2026-11-27T14:02Z`):**
   - Zenodo API (`2611.20344 OR "up-down graph" OR "Up or down at every integer"`): `2` hits (`24567319` = Q7.1; `24283375` = unrelated knot theory).
   - arXiv API (`id_list=2611.20344`): latest version remains `arXiv:2611.20344v2` (`2026-11-18T03:50:40Z`).
   - `search_web`: no resolution of Question 7.3 (`q:types`).

## Recommended Report Scope

- **Tier / Label:** `written proof, internally audited`
- **Verification Cmd:** `.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/notes/check-check-2.py`
- **Paths:** `targets/vasilyev-2611.20344-q7.3/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`
