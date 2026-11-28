# Gate 3 (`<1h`) Novelty Receipt (`watch-6`): `targets/dobson-2611.13347-ising-clifford/`

- **Checked UTC:** `2026-11-28T01:15:12Z`–`2026-11-28T01:15:40Z`
- **Target:** Sawyer Dobson & Zhenghan Wang, *Computational Power of Clifford and Ising Quantum Computers*, `arXiv:2611.13347v1` (`2026-11-09`), §5 (*Open Problems*), Problem (3): ancilla-assisted Ising braiding no-go on $n \ge 3$, strict separation of `PUSB`/`LUSB` from `PUSC`/`LUSC`, `ISING-BRAID` in $\mathsf{L}$, and 1-ancilla measurement-assisted equivalence.
- **Verdict:** **PASS** (`0` prior settlements; internal verification script re-run and passed).

## Exact Checks Performed (`<1h` Freshness)

1. **Direct checker execution:**
   - Ran `.venv/bin/python -u targets/dobson-2611.13347-ising-clifford/notes/check-check-1.py` -> `PASS`, exit `0` (`MAJORANA_AND_NOGO: PASS`, `ISING_BRAID_TRACKER: 50/50 exact Q(zeta_16) matrix tests PASS`, `ONE_ANCILLA_GADGET_EXACT: 16/16 (j,m1,m2,basis) branches + CZ PASS`).
2. **Local corpus & `RESULTS.md`:**
   - `.venv/bin/python -u tools/novelty_grep.py "2611.13347" "ISING-BRAID" "PUSB" "LUSB" --max-per-file 0 --max-total 0`: `56` lines across `17/936` files (`watch/snapshots/arxiv/*` indexing `2611.13347v1` with `OpenAlex cited_by=0; S2=0` plus incidental `PlusBoundary`/`PlusBox` substring matches on unrelated Lean/math repos; `0` settlements).
   - `RESULTS.md`: `0` matches for `2611.13347`, `ISING-BRAID`, `PUSB`, `LUSB`, or `dobson`.
3. **GitHub (`gh search code`, `gh search repos`):**
   - `gh search code '"2611.13347"'`: `8` arXiv announcement/digest JSONL hits (`meat-daemon-404/pat-hot`, `LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `drmithileshkumar/quantumresearchcenter`, `Quantum-Research-Center/quantumresearchcenter`), `0` settlements.
   - `gh search code '"ISING-BRAID"'`: `[]`; `gh search code '"PUSB" "PUSC"'`: `[]`; `gh search repos 2611.13347`: `[]`.
4. **arXiv, ECCC, Hexagon, Papex, Zenodo, Crossref, and Web:**
   - **arXiv:** `2611.13347v1` (`2026-11-09T23:19:02Z`) remains sole latest version.
   - **ECCC:** `https://eccc.weizmann.ac.il/` (`TR26-347` latest) and `/year/2026/` (`317,613` bytes): `0` matches.
   - **Hexagon & Papex:** `https://hexagonmath.org/api/v1/works?q=2611.13347` (`[]`), `q=dobson` (`[]`), `https://papex.org/` (`148,333` bytes): `0` matches.
   - **Zenodo:** `"2611.13347"` (`total=0`), `"PUSB" AND "LUSB"` (`total=0`); `"ISING-BRAID"` (`total=2`, inspected `23124101` & `23125206`, `2026-10-03` Fibonacci/Ising Leggett–Garg & CHSH braid-word benchmarks unrelated to `2611.13347` / `PUSB` / `LUSB`).
   - **Crossref:** `query.title=Computational Power of Clifford and Ising Quantum Computers`: `5` unrelated hits (`10.1063/1.3460174` Ahlbrecht–Georgiev 2010, etc.).
   - **Web (`search_web`):** `"2611.13347" OR "ISING-BRAID" OR ("PUSB" "LUSB" "PUSC") OR ("Dobson" "Ising" "Clifford" "QIP" OR "TQC" OR "STOC")` surfaced only `arXiv:2611.13347` itself.

## Coverage Limits
- Closed-access journals and private repositories are outside public index coverage.
