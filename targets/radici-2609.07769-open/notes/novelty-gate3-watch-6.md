# Gate 3 (`<1h`) Novelty Receipt (`watch-6`): `targets/radici-2609.07769-open/`

- **Checked UTC:** `2026-11-28T00:29:37Z`–`2026-11-28T00:29:57Z`
- **Target:** Gabriele Radici & Massimiliano Sala, *A Note on Binary Quadratic Systems and their relation to complexity theory*, `arXiv:2609.07769v2` (`2026-11-25`), §9 (*Open problems*): prove $\alpha_1(q,n,d) > \alpha_0(q,n,d)$ for all $q \in \{3,4,5\}$, $n \ge 2$, and $2 \le d \le n(q-1)$ (+ bonus $\alpha_1 < \alpha_0$ for $q \ge 7, d=2$, large $n$).
- **Verdict:** **PASS** (`0` prior settlements; internal verification script re-run and passed).

## Exact Checks Performed (`<1h` Freshness)

1. **Direct checker execution:**
   - Ran `.venv/bin/python -u targets/radici-2609.07769-open/notes/check-check-1.py` -> `PASS`, exit `0` (`BASE_N2` `q=3,4,5`, `LEMMA5_COEFFS`, `CASE2`–`CASE6`, exact `GRM_5(2,3)^perp` `A_0..7`).
2. **Local corpus & `RESULTS.md`:**
   - `.venv/bin/python -u tools/novelty_grep.py "2609.07769" --max-per-file 0 --max-total 0`: `13` lines across `5/914` files (`watch/snapshots/arxiv/*` indexing `2609.07769v2` and `watch/snapshots/discovered/AlexenderSokolov__cross-theory-formal-database.json` CC-BY license entry only; `0` settlements).
   - `RESULTS.md`: `0` matches for `2609.07769` or `radici`.
3. **GitHub (`gh search code`, `gh search repos`):**
   - `gh search code '"2609.07769"'`: only `uninhibited-scholar/cost-evidence-artifact` (`data/census/zcode/batch-0049.jsonl`).
   - `gh search code '"Binary Quadratic Systems" "Radici"'`: `[]`.
   - `gh search code '"alpha_1" "alpha_0" "Radici"'`: `[]`.
   - `gh search repos 2609.07769`: `[]`.
4. **arXiv, ECCC, IACR ePrint, Hexagon, Papex, Zenodo, Crossref, and Web:**
   - **arXiv:** `2609.07769v2` (`2026-11-25T13:37:50Z`) remains latest.
   - **ECCC:** `https://eccc.weizmann.ac.il/` (`TR26-347` latest) and `/year/2026/` (`317,613` bytes): `0` matches.
   - **Hexagon & Papex:** `https://hexagonmath.org/api/v1/works?q=radici` (`[]`) and `https://papex.org/` (`148,333` bytes): `0` matches.
   - **IACR ePrint:** `https://eprint.iacr.org/search?q=Radici+Sala` returns only `/2026/2022` (the authors' own `2026-09` preprint of `2609.07769`).
   - **Zenodo & Crossref:** `"2609.07769"` (`total=0`), `"Gabriele Radici"` (`total=0`); Crossref (`Binary Quadratic Systems Radici Sala`): `5` unrelated `Binary Quadratic Forms`/QUBO items.
   - **Web (`search_web`):** `"2609.07769" OR ("Gabriele Radici" "Massimiliano Sala" "F_3" OR "F_4" OR "F_5")` surfaced only `arXiv:2609.07769` itself.

## Coverage Limits
- OpenAlex was not queried separately in this `<1h` Gate 3 pass (`HTTP 429` observed at Gate 2 `23:33Z`); mitigated via live `arXiv`, `IACR ePrint`, `ECCC`, `Hexagon`, `Papex`, `Zenodo`, `Crossref`, and `search_web`.
