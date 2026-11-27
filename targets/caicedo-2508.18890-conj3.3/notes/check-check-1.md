# Check Report: `targets/caicedo-2508.18890-conj3.3/`

- **Checker:** `@check-1`
- **Verdict:** **PASS** (updated after `#698` for Conjecture 3.4 / Example 3.3 and analytic Case 5a/5b proofs)
- **Primary Source:** `tools/.arxiv_cache/eprint/2508.18890/Ehrhart_non_positivity.tex` (`arXiv:2508.18890v4`, Section 3 Example 3.3 L98–101, Conjecture 3.4 L109–111, L81–88, L325–406; shared `[theorem]` counter in `main.tex` L60–69)
- **Verifier Script:** `targets/caicedo-2508.18890-conj3.3/notes/check-check-1.py` (pure `int`/`Fraction`, SymPy exact `QQ[a]` polynomials & `Poly.intervals`, and 50-digit `mpmath.iv` exact interval arithmetic; zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` quotes **Conjecture 3.4** (`Ehrhart_non_positivity.tex` L109–111; folder slug `conj3.3`) verbatim and accurately discloses the `eq:crucial` (L88) printing typo vs L81–84 / L399–400.

## 2. Independent Verification Summary
Ran `.venv/bin/python -u targets/caicedo-2508.18890-conj3.3/notes/check-check-1.py` (exit code 0, `PASS`):
- **Lemma 1:** Verified (1) against **Example 3.3** ($n=5, a=16$), the paper's $\beta(5..8) = (16, 19, 23, 27)$ table, exact generating function (2) through $x^{16}$ ($1 \le a \le 8, 1 \le k \le 4$), and partial fraction identity (3) via `mpmath.iv`.
- **Lemma 2 ($1 \le a \le 6$):** Verified via `mpmath.iv` that $1 - \frac{1}{a}\sum_{m=1}^{a-1}\frac{1}{2\sin(\pi m/a)} > 0$ (minimum at $a=6$ is $\ge 0.39088 > 0$), plus exact $f_{a,n} > 0$ for $0 \le n \le 30$.
- **Lemma 3 ($5 \le n \le 32$):** Verified formula (4) against (1) for $n=5..12$, and used exact rational Sturm interval isolation (`Poly.intervals(eps=1/1000)`) across all $5 \le n \le 32$ and $1 \le k \le n$ to confirm exact thresholds $m_n \in [7, 18]$ ($m_5=16$ down to $m_{32}=8$) with negative intervals covering $[m_n, +\infty)$.
- **Lemma 4 ($n \ge 5, a \ge 2n^{4/3}$):** Verified the exact degree-4-in-$n$ quartic polynomial for $[t^{n-4}]\mathcal{L}_n(t,a)$ across $5 \le n \le 16$, negativity of both $n$-cubics on $[5, +\infty)$, and the $0.65 + 0.25 = 0.90 < 1$ bound.
- **Lemma 5 ($n \ge 33, 8 \le a < 2n^{4/3}$):**
  - *Case 5a ($a \in \{8,9,10\}$):* Verified via `mpmath.iv` that error/$|M_k| < 1$ at $n=33$ and the $n \to n+1$ step factor $((1 + 1/(34 H_{33}))^4 \cdot 2\sin(\pi/8)) < 0.79 < 1$.
  - *Case 5b ($a \ge 11$):* Verified $R_{11} < 0.846$, $4\cos(\pi/11) > 3$, $a|u(x)| < 21$, all analytic quadratic $r_\pm$ constants ($c > 2.959$, $\pi\sqrt{c^2 - 2.5^2} > 4.975$, $25\pi^2/88 < 2.804$, $e^{-4.975} < 0.007$, $(1+2.171/11)^{-11} < 0.138$, $|\sin(11\phi)| > 0.99$ on $(3.5\pi, 3.53\pi)$), monotonicity bounds ($5 - 33(\pi/11)/\tan(\pi/11) < -27$, $((1+1/(34 H_{33}))^4 \cdot 2\sin(\pi/11)) < 0.58 < 1$), direct $\min_{|x|=R_a}|1-(1-x)^a| \ge 0.99732 > 0.85$ (sampled $a$ + asymptotic limit $\ge 0.99847$), and $(E_1 + E_2)/|M_k| \le 0.001636 < 0.002$ at $n=33, 11 \le a \le 211$ (plus $n \in \{40,60,100,200\}$ endpoints).

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.
