# Check Report: `targets/mbirika-2204.12626-ques6.1/`

- **Checker:** `@check-1`
- **Verdict:** **PASS** (after `COUNTEREXAMPLE.md` L51 fix by `@scout-11`)
- **Primary Source:** `tools/.arxiv_cache/eprint/2204.12626/main.tex` (`arXiv:2204.12626v2`, Section 1 L175–176, Section 2 L210–216, Section 6 Question 6.1 L815–835)
- **Verifier Script:** `targets/mbirika-2204.12626-ques6.1/notes/check-check-1.py` (pure `int` and `fractions.Fraction`, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` reproduces Question 6.1 (`arXiv:2204.12626v2`, `main.tex` L815–835) verbatim, including the $6 \mid k$ and $6 \nmid k$ branches of $\mathcal{F}^3(k)$ and $\mathcal{L}^3(k)$ and initial conditions $F_0=0, F_1=1$ and $L_0=2, L_1=1$.
- Minor typo in `TARGET.md` L18: writes $\sum_{i=1}^k F_{n+i}^n$ in the motivational snippet from L176 (where `main.tex` has $F_{n+i}^2$), immediately clarified in L19 as $m=3$.

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python targets/mbirika-2204.12626-ques6.1/notes/check-check-1.py` (exit code 0, `PASS`):
- **Counterexample 1a ($\mathcal{F}^3(2)$):** `first_sums=[2, 9, 35, 152, 637]`, `actual_gcd=1`, conjectured $\frac{1}{2}\gcd(7,26)=1/2$.
- **Counterexample 1b ($\mathcal{F}^3(6)$):** `first_sums=[674, 2870, 12130]`, `actual_gcd=2` (and $F_n \bmod 2$ period $3 \mid 6$ verified), conjectured $\gcd(2196,9260)=4$ (also fails all 15/15 even $k \in [2..30]$).
- **Counterexample 2a ($\mathcal{L}^3(2)$):** `first_sums=[28, 91, 407, 1674, 7163]`, `actual_gcd=1`, conjectured $\frac{1}{2}\gcd(63,334)=1/2$.
- **Counterexample 2b ($\mathcal{L}^3(12)$):** Modular period checks ($L_n \bmod 4$ period 6, $L_n \bmod 5$ period 4) confirm $20 \mid \mathcal{L}^3(12)$, first three $n=0,1,2$ sums `[43702500, 185123260, 784200340]` match `COUNTEREXAMPLE.md` L51 with `gcd(first 3)=20`, `actual_gcd=20`, and conjectured $\gcd(141420760, 599077098)=2 \neq 20$. The $L_2^3=27$ remark at $k=6$ (`actual_gcd=2`, `alt_formula=28`) also holds.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.
