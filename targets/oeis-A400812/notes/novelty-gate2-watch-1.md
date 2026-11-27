# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A400812/`

- **Checked UTC:** `2026-11-27T10:28:35Z`–`2026-11-27T10:29:22Z`
- **Target:** OEIS `A400812` (rev. 50) & companion `A400813` / `A400814` (rev. 19) — Boris K. Horvat's 4 conjectured Spectre tiling star-triple formulas (recurrence, GF, closed form via `A057080`/`A000045`/`A099919`, limit $4-\sqrt{15}$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py "A400812" "A400813" "A400814" "400812"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/618` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A400812&fmt=json`, `A400813`, `A400814`):** `A400812` rev. 50 (`2026-11-10`) and `A400813`/`A400814` rev. 19 (`2026-10-31`) all explicitly state `they are not proved` and label the recurrence/GF/closed-form/limit as `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A400812&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A400812"`):** Only unrelated `georchestra/cadastrapp #329`; `0` PRs and `0` repos.
5. **Web search (`"A400812" OR "A400813" OR "A400814" "Horvat" OR "conjecture"`):** Confirms formulas remain empirical/conjectural; `0` proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:28Z` returned no math/OEIS matches.
