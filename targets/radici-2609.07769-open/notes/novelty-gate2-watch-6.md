# Gate 2 Novelty Receipt (`watch-6`): `targets/radici-2609.07769-open/`

- **Checked UTC:** `2026-11-27T23:34:17Z`
- **Target:** Gabriele Radici & Massimiliano Sala, *A Note on Binary Quadratic Systems and their relation to complexity theory*, `arXiv:2609.07769v2` (`2026-11-25`), §7 (*Open problems*): prove $\alpha_1(q,n,d) > \alpha_0(q,n,d)$ for all $q \in \{3,4,5\}$, $n \ge 2$, and $2 \le d \le n(q-1)$ (+ bonus $\alpha_1 < \alpha_0$ for $q \ge 7, d=2$, large $n$).
- **Verdict:** **PASS** (`0` prior settlements or independent preprints/repos solving the $q \in \{3,4,5\}$ open problems).

## Exact Checks Performed

1. **Local corpus (`tools/novelty_grep.py`, `RESULTS.md`, `watch/snapshots/hexagonmath-index.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py "2609.07769" --max-per-file 0 --max-total 0`: `13` lines across `5/880` files (`watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,last_sweep_report.json,state.json}` indexing `2609.07769v2` and `watch/snapshots/discovered/AlexenderSokolov__cross-theory-formal-database.json` CC-BY license metadata `editable-corpus/licenses/arxiv-2609.07769-CC-BY-4.0.txt`).
   - `.venv/bin/python -u tools/novelty_grep.py "Binary Quadratic Systems" "Gabriele Radici" --max-per-file 0 --max-total 0`: `5` lines across `3/880` files (same `watch/snapshots/arxiv/*` entries).
   - `RESULTS.md`: `0` matches for `2609.07769` or `Radici` (`3` incidental $\alpha_1$ matches on token/root spectra unrelated).
   - `watch/snapshots/hexagonmath-index.md` (`1,692` works): `0` matches for `2609.07769`, `Radici`, or `alpha_1 > alpha_0`.

2. **GitHub (`gh search code`, `gh search repos`, `the-omega-institute/trureturing`):**
   - `gh search code '"2609.07769"'`: only `uninhibited-scholar/cost-evidence-artifact` (`data/census/zcode/batch-0049.jsonl`, anonymous SoK census artifact, pushed `2026-11-09T07:26:25Z`).
   - `gh search code '"2609.07769" repo:the-omega-institute/trureturing'`: `[]`.
   - `gh search code '"Binary Quadratic Systems" "Radici"'`, `'"alpha_1" "alpha_0" "Radici"'`, `'"2609.07769" "F_3" OR "F_4" OR "F_5"'`: all `[]`.
   - `gh search repos 2609.07769`: `[]`; `gh search repos radici`: `10` unrelated non-math repos.

3. **arXiv, ECCC, IACR ePrint, Hexagon, Papex, Zenodo, Crossref, and Web:**
   - **arXiv:** `https://export.arxiv.org/api/query?id_list=2609.07769` returns `2609.07769v2` (`2026-11-25T13:37:50Z`, Gabriele Radici, Massimiliano Sala) as latest; `au:Radici AND au:Sala` returns only `2609.07769v2`.
   - **IACR ePrint (`2026/2022`):** `https://eprint.iacr.org/2026/2022` (*A Partial Injection from Unsatisfiable to Uniquely Satisfiable Quadratic Systems*, `2026-09-14`/`2026-09-17`) is the earlier preprint of `2609.07769`; `https://eprint.iacr.org/search?q=Radici+Sala` returns only `/2026/2022`.
   - **ECCC:** `https://eccc.weizmann.ac.il/` (`TR26-347` latest) and `/year/2026/` (`317,613` bytes): `0` matches.
   - **Hexagon & Papex:** `https://hexagonmath.org/api/v1/works?q=radici` (`0`), `q=2609.07769` (`0`), `q=binary+quadratic` (`3` unrelated `math.NT` works); `https://papex.org/` (`148,333` bytes): `0` matches.
   - **Zenodo & Crossref:** `ZENODO_ID` (`"2609.07769"`): `0`; `ZENODO_EXACT_TITLE` (`"A Note on Binary Quadratic Systems"`): `0`; `ZENODO_GABRIELE_RADICI` (`"Gabriele Radici"`): `0`; `ZENODO_AND_{1..4}` (`"alpha_1" AND "alpha_0" AND "Reed-Muller"`, `"evaluation matroid" AND "Reed-Muller"`, `"MQ_0" AND "MQ_1"`, `"Radici" AND ("quadratic systems" OR "2609.07769" OR "Reed-Muller")`): all `0`. Crossref (`Binary Quadratic Systems Radici Sala`): `5` unrelated `Binary Quadratic Forms` / QUBO items.
   - **Web (`search_web`):** 4 queries covering `2609.07769`, `Radici`, `Sala`, `alpha_1`/`alpha_0`, `MQ_0`/`MQ_1`, `evaluation matroid`, `F_3`/`F_4`/`F_5`, and complexity/crypto venues (`STOC`/`FOCS`/`CCC`/`ITCS`/`ICALP`/`EUROCRYPT`/`CRYPTO`/`PQCrypto`/`eprint`) surfaced only `arXiv:2609.07769` / `dblp` / `ePrint 2026/2022`.

## Coverage Limits
- `api.openalex.org` returned `HTTP 429` (`Too Many Requests`) on this check; mitigated via `search_web` + `arXiv` + `IACR ePrint` + `Crossref` + `Zenodo` + `ECCC`.
- No live Lean/arXiv source claim beyond Gate 2 novelty check was required or asserted.
