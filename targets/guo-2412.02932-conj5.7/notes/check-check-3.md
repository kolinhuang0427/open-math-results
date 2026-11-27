# Independent Check Report: `guo-2412.02932-conj5.7`

- **Checker:** `@check-3`
- **Verdict:** **PASS**
- **Primary Source:** `tools/.arxiv_cache/eprint/2412.02932/main.tex` (`arXiv:2412.02932v1`, Section 5.2, Conjecture 5.7 `\label{locond-3}`, L1355–1368).
- **Gate 2 Watch Status:** `novelty-gate2-watch-1.md` and `novelty-gate2-watch-6.md` PASS (`@watch-5` pending per `#524`).

## 1. Primary-Source Fidelity Check

- **Verbatim match:** `TARGET.md` L14–20 reproduces the definitions of $\theta_w$, $p_u(w)$, recursive $d_u$, and the verbatim text of `\begin{conj}\label{locond-3}` (`For any permutation $u$, we have $d_u \in \mathbb{Z}_{\geq 0}$.`) from `main.tex` L291–292 and L1355–1368.
- **Numbering:** Section 5 (`\section{Concluding remarks}`, L1245), Subsection 5.2 (`\subsection{A positivity conjecture}`, L1334). Using `\newtheorem{theo}{Theorem}[section]` and shared `[theo]` counter, the environments in Section 5 are 5.1 (`conj`), 5.2 (`conj`), 5.3 (`prob`), 5.4 (`conj`), 5.5 (`prob`), 5.6 (`conj`), and **5.7** (`\begin{conj}\label{locond-3}`, L1366–1368). Matches `TARGET.md` and `COUNTEREXAMPLE.md`.

## 2. Independent Exact-Integer Verification

- Wrote and executed independent verifier [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/guo-2412.02932-conj5.7/notes/check-check-3.py) directly from Lascoux–Schützenberger divided differences (`main.tex` L276–278) and `main.tex` L1355–1368 (AST `FLOAT_COUNT: 0`):
  1. `[1/3]` Computed $\mathfrak{S}_w(x)$, $\theta_w$, $\nu_w$, $d_w$, and $c_w$ exhaustively across all $1! + \dots + 6! = 873$ permutations in $\bigsqcup_{m=1}^6 S_m$: verified $d_w \ge 0, c_w \ge 0$ for all $m \le 6$, exact match with all 25 nonzero $(c_u, d_u)$ entries of Guo–Lin Table 3 (`\label{tab-mdu}`, `main.tex` L1385–1407), and $(d_u, c_u) = (0, 1)$ for $u^1=136245, u^2=146235$ (`main.tex` L1375–1377).
  2. `[2/3]` Computed the full downward pattern closure of $u = (1,3,4,5,6,2,8,9,7) \in S_9$ and $\mathfrak{S}_w$ for every permutation in the closure by exact top-down divided differences.
  3. `[3/3]` Confirmed all 54 proper subpattern counts $p_\sigma(u)$, exact match with all 8 nonzero subpattern contributions in `COUNTEREXAMPLE.md` (including $(c_{13452786}, d_{13452786}) = (3, 4)$ from `main.tex` L1380), $\theta_u = 113$, $\nu_u = 140$, $1 + \sum_{\sigma \neq u} d_\sigma p_\sigma(u) = 114$, $c_u = 0$, and $d_u = -1 < 0$ (refuting Conjecture 5.7).
- *(Scope note: `check-check-3.py` exhaustively verifies all $m \le 6$ and the full downward pattern closure of $u$; `COUNTEREXAMPLE.md` L15 relies on `main.tex` L1370 for $n=7,8$ minimality.)*

### Raw Verifier Output

Command: `.venv/bin/python -u targets/guo-2412.02932-conj5.7/notes/check-check-3.py` (exit code `0`):
```text
[1/3] Checking all permutations in S_1..S_6 (Table 3 + S_6 nonnegativity)...
[2/3] Computing downward pattern closure of u = (1,3,4,5,6,2,8,9,7)...
[3/3] Checking exact counterexample values and subpattern table...
Counterexample u=(1, 3, 4, 5, 6, 2, 8, 9, 7): theta_u=113, sum_sub=114, d_u=-1 < 0
PASS
```
