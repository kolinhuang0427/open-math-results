# Gate 2 Novelty Receipt (`watch-6`) — `targets/dobson-2611.13347-ising-clifford/`

- **Target:** Sawyer Dobson and Zhenghan Wang, *Computational Power of Clifford and Ising Quantum Computers*, `arXiv:2611.13347v1` (`2026-11-09`), Section 5 (*Open Problems*), Problem (3) (`sections/5.tex` L11): ancilla-assisted Ising braiding on $n \ge 3$ qubits, `PUSB`/`LUSB` vs `PUSC`/`LUSC` and `ISING-BRAID` in $\mathsf{L}$, and 1-ancilla measurement-assisted equivalence.
- **Checked UTC:** `2026-11-27T22:36:42Z` – `2026-11-27T22:37:34Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of Section 5 Problem (3) found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `865` files across `946` cataloged repos) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py "2611.13347" "dobson-2611.13347" "Dobson" "Ising braiding" "PUSB" "ISING-BRAID" --max-per-file 0 --max-total 30` -> `16` lines across `5/865` files (`watch/snapshots/arxiv/{arxiv_submissions.{json,md},state.json}` entry for `2611.13347v1` itself, unrelated Ted Dobson Cayley graph papers / `rodrigueskevrekidisdobson2019`, and `chy4pro/automath` `wowii`; `0` settlements).
   - `RESULTS.md` scan -> `0` hits.
2. **Live GitHub (`2026-11-27T22:36:43Z`–`22:37:01Z`):**
   - `gh search code '"2611.13347"'` -> `8` arXiv announcement/digest JSONL entries (`meat-daemon-404/pat-hot`, `LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `quantumresearchcenter`).
   - `gh search code` for `"dobson-2611.13347"`, `"ISING-BRAID"`, `"PUSB" "Clifford"`, and `repo:the-omega-institute/trureturing 2611.13347` -> `[]` (`0` hits on all four).
3. **Live ECCC (`eccc.weizmann.ac.il`), arXiv, Hexagon, Papex, Zenodo, Crossref & Web (`2026-11-27T22:01Z`–`22:37:34Z`):**
   - `https://eccc.weizmann.ac.il/` (`2026/347` latest) & `/year/2026/`: `0` hits for `2611.13347`, `dobson`, `ising`, or `braid` (`clifford` matches unrelated `TR26-160` Golowich–Tamo–Zhu quantum LDPC codes); `search_web domain:eccc.weizmann.ac.il` returns `0` ECCC matches.
   - `https://export.arxiv.org/api/query?id_list=2611.13347` -> `2611.13347v1` sole version (`2026-11-09`).
   - `https://hexagonmath.org/api/v1/works` (`1,692` works; `q=2611.13347`, `q=Dobson`, `q=Ising braiding` -> `total=0`), `papex.org` (`20` records -> `0`).
   - `Zenodo`: `"2611.13347"` -> `0`, `"Computational Power of Clifford and Ising Quantum Computers"` -> `0`; `"ISING-BRAID"` -> `2` unrelated `2026-10-03` Fibonacci/Ising Leggett–Garg/CHSH records (`23124101`, `23125206`).
   - `Crossref` (`Dobson` + `Ising`) -> unrelated `1970` physics paper; `search_web` returns only `arXiv:2611.13347v1` itself.

## Coverage Limits

- Unauthenticated public indices only (private repositories and paywalled proceedings remain outside public reach); Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` publication.
