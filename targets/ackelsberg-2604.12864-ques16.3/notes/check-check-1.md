# Independent Check Report — `ackelsberg-2604.12864-ques16.3`

- **Checker:** `check-1`
- **Verdict:** **PASS** (re-checked after `#1067` patch fixing `COUNTEREXAMPLE.md` L70)

## 1. Primary Source Verification

- **Source:** Ethan Ackelsberg and Florian K. Richter, *An inverse theorem for sumsets of sets of positive density in the integers*, `arXiv:2604.12864v1` (`tools/.arxiv_cache/eprint/2604.12864.src`, `InverseProblemDensity_arXiv_v1.tex`).
- **Exact numbering & location:** Section 16 (`\section{Further explorations}`, L5712), Subsection 16.1 (L5716), Question 16.3 (`\begin{Question}[Finitary form of Kneser's theorem]`, L5747–5757), with `\N = \{1, 2, 3, \ldots\}` (L398) and `[N] = \{1, \ldots, N\}` (L405).
- **Verbatim match:** `TARGET.md` matches the primary source verbatim in quantifiers, domain, and inequalities.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python targets/ackelsberg-2604.12864-ques16.3/notes/check-check-1.py` using exact `Fraction` / `int` arithmetic (`AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Primary construction (`COUNTEREXAMPLE.md` L9–68, $\varepsilon = 1/10$, $\alpha = \beta = 4/9$, $N = \max(N_1, N_0+1, 10D)$):** Verified across `60` tuples $(N_0, D, N_1)$ ($N_0 \in \{1,2,5,17\}$, $D \in \{1,2,3,7,10\}$, $N_1 \in \{1,15,120\}$): $A \subseteq B \subseteq [N]$, prefix densities $\ge 1/2 > 4/9$, $B$ meets every residue class mod $D$, and $|(A+B)\cap[N]|/N \le 11/20 < 71/90 = \alpha + \beta - \varepsilon$.
2. **Patched general-$\varepsilon$ remark (`COUNTEREXAMPLE.md` L70):** With $N \ge \max\bigl(N_1, N_0+1, \lceil D_0 / (\frac{1}{2} - \varepsilon - 2\eta) \rceil\bigr)$, verified across `64` instances spanning $\varepsilon \in \{1/10, 1/3, 2/5, 9/20\}$, $D_0 \in \{1,2,5,10\}$, $N_0 \in \{1,4\}$, $N_1 \in \{1,30\}$ (`|(A+B)\cap[N]|/N <= 1/2 + D_0/(2N) < 1 - 2\eta - \varepsilon`).

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).
