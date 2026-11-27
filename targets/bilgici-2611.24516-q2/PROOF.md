# Proof (Negative Answer) for `bilgici-2611.24516-q2`

**Verdict: NO.** None of the $18$ nonzero two-term sums $B_r(y)$ ($r \in \{0, 1, \dots, 18\} \setminus \{17\}$) in Table~\ref{tab:B} of [arXiv:2611.24516v1](https://arxiv.org/abs/2611.24516) can be reduced to a single product of the $P_a$ via any relations among the $P_a$—either modulo $19$ or identically in $\mathbb{Z}[[y]]$.

More precisely, we prove the stronger statement: for every $r \in \{0, \dots, 18\} \setminus \{17\}$, there do **not** exist a scalar $c \in \mathbb{F}_{19}^\times$ and **any** integers $v, e_0, e_1, \dots, e_9 \in \mathbb{Z}$ (allowing both positive and negative exponents, arbitrary $y$-shifts, and arbitrary powers of $P_0$) such that
$$B_r(y) \equiv c \, y^v \, P_0(y)^{e_0} \prod_{a=1}^9 P_a(y)^{e_a} \pmod{19} \quad \text{in } \mathbb{F}_{19}((y)).$$
Since every valid algebraic or $q$-series relation among the $P_a$ (such as Weierstrass's three-term theta relations generating $\mathcal{I}_\Theta$ in §7.1, Lemma~\ref{lem:theta}) vanishes identically upon substituting $P_a(y) = (y^a; y^{19})_\infty (y^{19-a}; y^{19})_\infty$, no relation among the $P_a$ can reduce any $B_r$ (or any quotient $\Psi_r/P_0 = B_r / \mathcal{D}$ in Table~\ref{tab:Psi}) to a single product or Laurent monomial of the $P_a$.

---

## 1. Reduction to a Logarithmic-Derivative Obstruction Modulo $(19, y^{19})$

Let $F \in \mathbb{F}_{19}[[y]]^\times$ have constant term $1$. Define the formal logarithmic derivative $D(F) := y F'(y) / F(y) \in \mathbb{F}_{19}[[y]]$, and write
$$D(F) = \sum_{n=1}^\infty d_n(F) \, y^n, \qquad d_n(F) \in \mathbb{F}_{19}.$$
If $F(y) = 1 + \sum_{n \ge 1} f_n y^n$, then $y F'(y) = D(F) F(y)$ yields Newton's recurrence in $\mathbb{F}_{19}$:
$$d_n(F) = n f_n - \sum_{k=1}^{n-1} d_k(F) f_{n-k} \pmod{19} \qquad (n \ge 1).$$

Now suppose that for some $r \in \{0, \dots, 18\} \setminus \{17\}$,
$$B_r(y) \equiv c \, y^v \, P_0(y)^{e_0} \prod_{a=1}^9 P_a(y)^{e_a} \pmod{19}$$
with $c \in \mathbb{F}_{19}^\times$ and $v, e_0, e_1, \dots, e_9 \in \mathbb{Z}$.

1. **Valuation and normalization:** Because $P_a(0) = 1$ for all $0 \le a \le 9$, the right-hand side has $y$-adic valuation $v$ and leading coefficient $c \not\equiv 0 \pmod{19}$. Thus $v = \mathrm{ord}_y(B_r \bmod 19)$, $c \equiv [y^v] B_r \pmod{19}$, and the normalized series
   $$\widetilde{B}_r(y) := c^{-1} y^{-v} B_r(y) \in 1 + y \mathbb{F}_{19}[[y]]$$
   must satisfy $\widetilde{B}_r(y) \equiv P_0(y)^{e_0} \prod_{a=1}^9 P_a(y)^{e_a} \pmod{19}$.

2. **Logarithmic derivative of $P_0$ and $P_a$ modulo $y^{19}$:**
   - Since $P_0(y) = (y^{19}; y^{19})_\infty \equiv 1 \pmod{y^{19}}$, we have $D(P_0) \equiv 0 \pmod{(19, y^{19})}$.
   - For $1 \le a \le 9$, we have $P_a(y) \equiv (1 - y^a)(1 - y^{19-a}) \pmod{y^{19}}$. Taking logarithmic derivatives in $\mathbb{F}_{19}[[y]]/(y^{19})$ (noting $19 - a \equiv -a \pmod{19}$ and $2(19 - a) \ge 20 > 18$),
     $$D(P_a) \equiv -\frac{a y^a}{1 - y^a} - \frac{(19-a) y^{19-a}}{1 - y^{19-a}} \equiv -\sum_{k=1}^{\lfloor 18/a \rfloor} a \, y^{ak} + a \, y^{19-a} \pmod{(19, y^{19})}.$$

3. **Uniqueness of $(e_1, \dots, e_9) \bmod 19$ and compatibility constraints at $y^{10}, y^{11}$:**
   By additivity $D(FG) = D(F) + D(G)$, setting $d_n := d_n(\widetilde{B}_r) \pmod{19}$, we must have for all $1 \le n \le 18$:
   $$d_n \equiv -\sum_{\substack{1 \le a \le 9 \\ a \mid n}} a \, e_a + \mathbf{1}_{n \ge 10}\,(19 - n) \, e_{19 - n} \pmod{19}.$$
   - For $1 \le n \le 9$, the second term vanishes, so $d_n \equiv -\sum_{a \mid n} a \, e_a \pmod{19}$. Since every $a \in \{1, \dots, 9\}$ is invertible modulo $19$, the values $d_1, \dots, d_9 \pmod{19}$ uniquely determine $e_1, \dots, e_9 \pmod{19}$ recursively via
     $$e_a \equiv -a^{-1}\!\left(d_a + \sum_{\substack{1 \le m < a \\ m \mid a}} m \, e_m\right) \pmod{19} \qquad (1 \le a \le 9).$$
   - Substituting these unique exponents $e_1, \dots, e_9 \pmod{19}$ into $n = 10$ and $n = 11$ yields the necessary congruences
     $$d_{10}^{\mathrm{pred}} \equiv -(e_1 + 2e_2 + 5e_5) - 10\,e_9 \pmod{19}, \qquad d_{11}^{\mathrm{pred}} \equiv -e_1 - 11\,e_8 \pmod{19}.$$
   *(Remark: Note that $P_a(y)^{19} \equiv 1 \pmod{(19, y^{19})}$, so $e_a \bmod 19$ already captures all integer exponents $e_a \in \mathbb{Z}$ simultaneously.)*

---

## 2. Explicit Obstruction Across All $18$ Nonzero Rows of Table~\ref{tab:B}

For every $r \in \{0, \dots, 18\} \setminus \{17\}$, computing the exact coefficients of $B_r(y) \pmod{19}$ through $y^{v+11}$ (verified both from the explicit formulas in Table~\ref{tab:B} and directly from the $19$-dissection of $f(q)^{10} \pmod{19}$) gives the unique forced exponents $(e_1, \dots, e_9) \bmod 19$ (displayed in $\{-9, \dots, 9\}$) and the logarithmic-derivative mismatches at $y^{10}$ and $y^{11}$:

| $r$ | $v$ | $c \bmod 19$ | Forced $(e_1, \dots, e_9) \bmod 19$ | $d_{10}$ | $d_{10}^{\mathrm{pred}}$ | $d_{10}-d_{10}^{\mathrm{pred}}$ | $d_{11}$ | $d_{11}^{\mathrm{pred}}$ | $d_{11}-d_{11}^{\mathrm{pred}}$ |
|---:|---:|---:|:---|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | $(-4, -9, 4, 2, -6, 4, 3, 6, -1)$ | 16 | 5 | **11** | 9 | 14 | **14** |
| 1 | 0 | 9 | $(-5, -4, 3, -7, -4, 6, -3, 2, -9)$ | 18 | 9 | **9** | 15 | 2 | **13** |
| 2 | 0 | 16 | $(-5, 2, 6, -8, 4, -4, -3, 9, 2)$ | 15 | 18 | **16** | 16 | 1 | **15** |
| 3 | 0 | 8 | $(-4, -9, 4, 6, -6, -1, 4, -6, 9)$ | 15 | 0 | **15** | 9 | 13 | **15** |
| 4 | 0 | 9 | $(4, 2, 4, 8, 1, 0, 9, -9, 9)$ | 7 | 11 | **15** | 13 | 0 | **13** |
| 5 | 0 | 10 | $(0, -3, 0, -9, 8, -4, -5, -7, 2)$ | 7 | 3 | **4** | 18 | 1 | **17** |
| 6 | 1 | 15 | $(1, 0, 0, -3, 4, 4, 1, 3, 7)$ | 1 | 4 | **16** | 14 | 4 | **10** |
| 7 | 0 | 6 | $(1, -4, 0, -9, 4, 3, 3, 7, 9)$ | 17 | 11 | **6** | 18 | 17 | **1** |
| 8 | 0 | 6 | $(0, 0, 5, -4, -3, -8, 3, -5, -1)$ | 14 | 6 | **8** | 13 | 17 | **15** |
| 9 | 0 | 7 | $(0, -5, 1, 7, -5, 0, -2, -5, -6)$ | 0 | 0 | 0 | 14 | 17 | **16** |
| 10 | 0 | 9 | $(-3, 6, -4, -9, -5, 1, 2, 3, 2)$ | 7 | 15 | **11** | 15 | 8 | **7** |
| 11 | 0 | 9 | $(4, 7, 1, -1, -1, -2, -5, 6, 2)$ | 11 | 5 | **6** | 18 | 6 | **12** |
| 12 | 0 | 13 | $(-5, 1, -7, -4, 5, -8, 5, 9, -6)$ | 14 | 0 | **14** | 0 | 1 | **18** |
| 13 | 1 | 3 | $(0, 6, -4, -9, -5, -7, 0, -2, 4)$ | 3 | 11 | **11** | 10 | 3 | **7** |
| 14 | 0 | 7 | $(0, -3, 4, 6, -7, -2, 3, 5, 5)$ | 1 | 10 | **10** | 1 | 2 | **18** |
| 15 | 0 | 15 | $(0, 1, 0, -5, -8, -4, 5, 6, 7)$ | 10 | 6 | **4** | 18 | 10 | **8** |
| 16 | 0 | 18 | $(6, -9, -3, -8, 5, -5, -4, 1, -6)$ | 7 | 9 | **17** | 12 | 2 | **10** |
| 18 | 0 | 14 | $(4, 2, 6, -5, -6, -9, -7, 8, -8)$ | 12 | 7 | **5** | 7 | 3 | **4** |

In particular:
- For every $r \in \{0, \dots, 18\} \setminus \{9, 17\}$, already $d_{10} \not\equiv d_{10}^{\mathrm{pred}} \pmod{19}$.
- For **all $18$** nonzero rows $r \in \{0, \dots, 18\} \setminus \{17\}$ (including $r = 9$), $d_{11} \not\equiv d_{11}^{\mathrm{pred}} \pmod{19}$.

*(Concrete hand check for $r = 0$, $B_0 = P_3 P_6 P_7 P_9 + 4y P_2 P_4 P_6 P_9$: expanding modulo $y^{12}$, $B_0(y) \equiv 1 + 4y - 5y^3 - 4y^5 - y^6 - y^7 + 4y^9 - 4y^{10} \pmod{19}$, with $[y^{11}] B_0 \equiv 0$; Newton's recurrence gives $(d_1, \dots, d_{11}) \equiv (4, 3, 11, 14, 15, 5, 2, 4, 1, 16, 9)$, forcing $(e_1, \dots, e_9) \equiv (-4, -9, 4, 2, -6, 4, 3, 6, -1) \pmod{19}$, which predicts $d_{10}^{\mathrm{pred}} \equiv 5 \neq 16$ and $d_{11}^{\mathrm{pred}} \equiv 14 \neq 9 \pmod{19}$.)*

Therefore, none of the two-term sums $B_r$ in Table~\ref{tab:B} (and equivalently none of the two-term quotients $\Psi_r/P_0 = B_r/\mathcal{D}$ in Table~\ref{tab:Psi}) can be reduced to a single product of the $P_a$ modulo $19$ (nor over $\mathbb{Z}$) via any relations among the $P_a$.

## Verification

- Script: [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/bilgici-2611.24516-q2/verify.py) (exact integer / modular arithmetic over $\mathbb{F}_{19}$, zero floats, zero `/` or `//`).
- Checks:
  1. Verifies $f(q)^{10} \equiv \sum_{r=0}^{18} q^r B_r(q^{19}) \pmod{(19, q^{361})}$ across all $19$ residue classes (confirming Table~\ref{tab:B} against Theorem~\ref{thm:tenth}).
  2. Verifies the logarithmic-derivative obstruction $d_{11} \not\equiv d_{11}^{\mathrm{pred}} \pmod{19}$ (and $d_{10} \not\equiv d_{10}^{\mathrm{pred}} \pmod{19}$ for $r \neq 9$) for all $18$ nonzero rows.
  3. Directly multiplies $\prod_{a=1}^9 P_a(y)^{e_a \bmod 19} \pmod{(19, y^{19})}$ using the unique forced exponents $(e_1, \dots, e_9) \bmod 19$ and confirms a nonzero discrepancy below $y^{v+12}$ for every nonzero row $r$.
