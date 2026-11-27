# Independent Check Report (`check-3`): `targets/hare-2603.19554-conj3.3/`

## 1. Primary-Source Fidelity Check
Checked directly against `arXiv:2603.19554v1` (`tools/.arxiv_cache/eprint/2603.19554/v6.tex`, Section 3.1 `\label{sec:beta, theta}`, Conjecture 3.3 `\label{conj:1}`, lines 487–493; definitions lines 84–95):
- **Context (line 489):** $\beta_d$ is the Perron root of $x^d - x - 1 = 0$.
- **Conjecture 3.3 (`conj:1`, lines 490–493):** `For all $d \geq 4$ and all $k \geq 1$ we have $\beta_d^k$ is non-Parry.`
- **Definitions (lines 85–95):** $T_\beta(x) = \beta x \bmod 1$, $\beta$ is a Parry number iff $\{T_\beta^{[k]}(1)\}_{k=1}^\infty$ is finite; Solomyak's bound $\theta_0 = \frac{1+\sqrt{5}}{2}$ (any conjugate of modulus $> \theta_0$ implies non-Parry).
- **Result:** `TARGET.md` and `PROOF.md` match the primary source verbatim (every quantifier, domain $d \ge 4, k \ge 1$, and definition).

## 2. Mathematical Proof Check
Reviewed `targets/hare-2603.19554-conj3.3/PROOF.md` Sections 1–3:
- **Section 1:** Irreducibility of $x^d - x - 1$ (Selmer 1956), Perron property and degree $d$ of $\beta_d^k$, Solomyak's bound, Akiyama's divergence criterion, and the closed-form Akiyama block for $q \in (1, 2)$ all hold rigorously.
- **Section 3 ($d \ge 500$):** Lemmas 3.1–3.2 and Cases A & B ($0 < t \le 0.5$ and $0.5 < t \le 0.705$) hold rigorously. (Minor exposition note on line 72: $e^y - 1 - y \le y^2$ on $[0, 0.01]$ would give $0.10/d$, whereas the stated bound $2(e^{5/d} - 1 - 5/d) < 0.06/d$ itself holds tightly via $e^y - 1 - y \le 0.51 y^2$.)

## 3. Independent Mechanical Verification
Written solely from `v6.tex` definitions and `PROOF.md` without reading `verify.py` or author notes:
- Script: `targets/hare-2603.19554-conj3.3/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/hare-2603.19554-conj3.3/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[Part 1] Exact integer fixed-point verification for 4 <= d <= 499 (zero floats)...
  Part 1 PASS: 4 <= d <= 499 (496 degrees): 496 Solomyak cutoffs, 86205 closed-form blocks, 10 greedy orbits (max step=35).
[Part 2] Rigorous mpmath.iv verification of Section 3 (d >= 500)...
  Part 2 PASS: All Section 3 inequalities and spot checks (d=500,501,600,1000) verified.
PASS
```
Summary:
- **Part 1 ($4 \le d \le 499$, pure Python `int` fixed-point intervals at scale $2^{140}$, zero floats):** certified $\beta_d$ via sign-change bisection, certified $\gamma_d$ ($\mathrm{Im}(\gamma_d) > 0$) via exact Rouché disk $|z - z_*| < 2^{-100}$, verified every $k \ge 1$ up to Solomyak's cutoff ($496$ degrees, $86205$ closed-form Akiyama blocks, $10$ greedy orbit simulations for $d=4,5$).
- **Part 2 ($d \ge 500$, `mpmath.iv` at `dps = 50`):** verified all numerical inequalities in Lemmas 3.1–3.2 and Cases A & B, plus direct full-$k$ spot checks at $d \in \{500, 501, 600, 1000\}$.

## 4. Verdict
- **PASS** (`Gate 2` PASS receipts present: `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).
