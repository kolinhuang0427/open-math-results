# Proof of Conjecture 5.1 (arXiv:2609.32450v2, Section 5)

**Result.** Conjecture 5.1 of Shin-ichi Yasutomi (*On the Ordering and Injectivity of Lagrange Constants Associated with Certain Substitutions*, `arXiv:2609.32450v2`, Section 5) holds unconditionally for all integers $1 \le a < b$ and all $x, y \in \mathbb{Q} \cap [0, 1]$ with $x < y$.

---

## 1. Preliminaries and Exact Convergent Decomposition

By Theorem~\ref{t3} (`lagrangev2.tex`, proved for all integers $1 \le a < b$ and all $x \in \mathbb{Q} \cap [0, 1]$),
\[
\mathcal{L}([\phi_{a,b}(G(x))]) = L(x, 1) = a_0 + [0; a_1, a_2, \dots] + [0; a_{-1}, a_{-2}, \dots],
\]
where $\phi_{a,b}(0) = aa$, $\phi_{a,b}(1) = bb$, and $a_{2k-1} a_{2k} = \phi_{a,b}(G(x, k))$ for all $k \in \mathbb{Z}$.

### 1.1. Tail bounds
For $x \in \mathbb{Q} \cap (0, 1)$, the sequence $\{G(x, k)\}_{k \in \mathbb{Z}}$ is purely periodic with period $\mathrm{den}(x) \ge 2$ and contains both $0$'s and $1$'s. Consequently, every forward or backward tail $t = [c_1; c_1, c_2, c_2, \dots]$ with $c_i \in \{a, b\}$ appearing infinitely often satisfies:
\[
[\overline{a}] < t < [\overline{b}],
\]
where $[\overline{c}] = \frac{c + \sqrt{c^2+4}}{2}$. Indeed, for $z > 0$, $T_c(z) := c + \frac{1}{c + 1/z}$ is strictly increasing in $z$ with $T_a([\overline{a}]) = [\overline{a}] < b < T_b(z)$ and $T_a(z) < a + \frac{1}{a} < [\overline{b}] = T_b([\overline{b}])$. Moreover:
1. $[\overline{a}] > a + \frac{1}{a+1}$ for all $a \ge 1$ (since $(a + \frac{1}{a+1})^2 - a(a+\frac{1}{a+1}) - 1 = \frac{1}{(a+1)^2} - \frac{a+1}{(a+1)^2} < 0$), and for $a = 1$, $[\overline{1}] = \frac{1+\sqrt{5}}{2} > \frac{8}{5}$ (since $125 > 121$).
2. $[\overline{a}]^2 = a[\overline{a}] + 1 > a^2 + 1$.
3. $[\overline{b}] - [\overline{a}] = \frac{1}{2}\big((b - a) + (\sqrt{b^2+4} - \sqrt{a^2+4})\big) < b - a$ (since $\frac{d}{dt}\sqrt{t^2+4} = \frac{t}{\sqrt{t^2+4}} < 1$).

### 1.2. Boundary cases $x = 0$ and $y = 1$
- **$(x, y) = (0, 1)$** (Type (2)): $G(0) = 0^\infty$ and $G(1) = 1^\infty$, so $\mathcal{L}([\phi_{a,b}(G(0))]) = \sqrt{a^2+4} < \sqrt{b^2+4} = \mathcal{L}([\phi_{a,b}(G(1))])$.
- **$x = 0 < y < 1$** (Type (2)): $\mathrm{den}(0) = 1 < \mathrm{den}(y)$ and $\lfloor y \rfloor = 0$. Here $\mathcal{L}(0) = \sqrt{a^2+4}$. Since $0 < y < 1$, $G(y, 0) = 1$ and $G(y, 1) = 0$, so $b_0 = b$ and $b_1 = b_2 = a$. If $a \ge 2$, then $L(y, 1) > b \ge a+1 > \sqrt{a^2+4}$ since $(a+1)^2 = a^2 + 2a + 1 > a^2 + 4$. If $a = 1$, then $b \ge 2$, $[0; b_1, b_2, \dots] > [0; 1, 1, b+1] = \frac{b+2}{2b+3} > \frac{1}{2}$, so $L(y, 1) > b + \frac{1}{2} \ge \frac{5}{2} > \sqrt{5} = \mathcal{L}(0)$.
- **$0 < x < y = 1$** (Type (3)): $\mathrm{den}(x) > 1 = \mathrm{den}(1)$ and $\lfloor x \rfloor = 0 < 1 = \lfloor 1 \rfloor$. Here $\mathcal{L}(1) = \sqrt{b^2+4} = b + \frac{4}{\sqrt{b^2+4}+b} < b + \frac{2}{b}$. Since $0 < x < 1$, we have $G(x,0) = 1$ (hence $a_{-1}a_0 = bb$, so $a_0 = b$ and $a_{-1} = b$) and $G(x,1) = 0$ (hence $a_1a_2 = aa$). Thus $[0; a_1, a_2, \dots] > \frac{1}{a + 1/a} = \frac{a}{a^2+1}$ and $[0; a_{-1}, a_{-2}, \dots] > \frac{1}{b + 1/a} = \frac{a}{ab+1}$. If $a \ge 2$, then $\frac{a}{a^2+1} + \frac{a}{ab+1} - \frac{2}{b} = \frac{a^2 b(b-a) - 2a^2 - 2}{b(a^2+1)(ab+1)} \ge \frac{a^3 - a^2 - 2}{b(a^2+1)(ab+1)} > 0$, so $L(x,1) > b + \frac{2}{b} > \mathcal{L}(1)$. If $a = 1$ ($b \ge 2$), then $a_3 \le b$ gives $[0; 1, 1, a_3, \dots] > [0; 1, 1, b+1] = \frac{b+2}{2b+3} > \frac{1}{2}$ and $[0; a_{-1}, \dots] > \frac{1}{b+1}$; for $b \ge 3$, $\frac{1}{2} + \frac{1}{b+1} - \frac{2}{b} = \frac{b^2 - b - 4}{2b(b+1)} > 0$, while for $b = 2$, $L(x, 1) > 2 + \frac{4}{7} + \frac{1}{3} = 2 + \frac{19}{21} > 2 + \frac{6}{7} > \sqrt{8} = \mathcal{L}(1)$ (as $\frac{400}{49} > 8$).

Henceforth we assume $0 < x < y < 1$. Note that Type (1) requires $n < \min(\mathrm{den}(x), \mathrm{den}(y))$ with $\lfloor nx \rfloor < \lfloor ny \rfloor$, which also forces $0 < x < y < 1$ and $n \ge 2$.

### 1.3. Matrix setup and convergent identity
Let $A = \begin{pmatrix}0&1\\1&a\end{pmatrix}^2 = \begin{pmatrix}1&a\\a&a^2+1\end{pmatrix}$, $B = \begin{pmatrix}0&1\\1&b\end{pmatrix}^2 = \begin{pmatrix}1&b\\b&b^2+1\end{pmatrix}$, and $S_b = \begin{pmatrix}0&1\\1&b\end{pmatrix}$. In all three types, $G(x, 0) = G(y, 0) = 1$, so $a_0 = b_0 = b$. Let $n \ge 2$ be the comparison index from Lemma~\ref{l1} (minimal $n$ with $\lfloor nx \rfloor < \lfloor ny \rfloor$ in Type (1); $n = \mathrm{den}(x)$ in Type (2); $n = \mathrm{den}(y)$ in Type (3)). By Lemma~\ref{l2}(7) and the exact combinatorial arguments of Lemmas~\ref{ml1}--\ref{ml3} of `lagrangev2.tex` (replacing $a+1$ by $b$ throughout), the shared middle word $w = a_3 \dots a_{2n-2} \in \{a, b\}^{2n-4}$ corresponds to
\[
M = \begin{pmatrix} m_1 & m_2 \\ m_3 & m_4 \end{pmatrix} = \prod_{k=2}^{n-1} \begin{pmatrix} 1 & c_k \\ c_k & c_k^2 + 1 \end{pmatrix}, \qquad c_k \in \{a, b\}
\]
(with $M = I$ when $n = 2$), satisfying $\det M = m_1 m_4 - m_2 m_3 = 1$.

For any $2\times 2$ matrix $T = \begin{pmatrix} r_0 & r \\ q_0 & q \end{pmatrix} = \prod_{i=1}^k \begin{pmatrix}0&1\\1&d_i\end{pmatrix}$, we have $[0; d_1, \dots, d_k, t] = \frac{r_0 + r t}{q_0 + q t} = \frac{r}{q} + \frac{(-1)^k}{q(q_0 + q t)}$, where $\det T = (-1)^k$. Define the four convergent matrices and denominators:
\[
T_{AA} = A M A, \quad T_{AB} = A M B, \quad T_{SA} = S_b M A, \quad T_{SB} = S_b M B,
\]
with bottom rows $(q_{0,XY},\; q_{XY})$ for $XY \in \{AA, AB, SA, SB\}$, and $Q_{XY}(t) := q_{0,XY} + q_{XY} t$.

Using $\det(A M A) = \det(A M B) = 1$, $\det(S_b M A) = \det(S_b M B) = -1$, and direct evaluation of $T_{AB}[0,1] T_{AA}[1,1] - T_{AA}[0,1] T_{AB}[1,1]$ via $\det M = 1$:
\[
\frac{r_{AA}}{q_{AA}} - \frac{r_{AB}}{q_{AB}} = \frac{(b-a)(ab-1)}{q_{AA} q_{AB}}, \qquad
\frac{r_{SB}}{q_{SB}} - \frac{r_{SA}}{q_{SA}} = \frac{(b-a)(ab-1)}{q_{SA} q_{SB}}.
\]
Therefore, writing $x_1 = [a_{2n+1}; \dots]$, $y_1 = [b_{2n+1}; \dots]$, $x_2 = [a_{-2n}; \dots]$, $y_2 = [b_{-2n}; \dots]$:
- **Type (1):**
  \[
  L(y, 1) - L(x, 1) = (b-a)(ab-1)\left(\frac{1}{q_{SA} q_{SB}} - \frac{1}{q_{AA} q_{AB}}\right) + \left(\frac{1}{q_{SA} Q_{SA}(x_2)} - \frac{1}{q_{AA} Q_{AA}(x_1)}\right) - \left(\frac{1}{q_{SB} Q_{SB}(y_2)} - \frac{1}{q_{AB} Q_{AB}(y_1)}\right).
  \]
- **Type (2):** ($a_1\dots a_{2n} = b_1\dots b_{2n}$, so $T_{AB}$ on both forward branches; $x_1 < y_1$)
  \[
  L(y, 1) - L(x, 1) = \frac{(b-a)(ab-1)}{q_{SA} q_{SB}} + \frac{1}{q_{SA} Q_{SA}(x_2)} - \frac{1}{q_{SB} Q_{SB}(y_2)} - \frac{y_1 - x_1}{Q_{AB}(x_1) Q_{AB}(y_1)}.
  \]
- **Type (3):** ($a_{-1}\dots a_{-2n+1} = b_{-1}\dots b_{-2n+1}$, so $T_{SA}$ on both backward branches)
  \[
  L(y, 1) - L(x, 1) = -\frac{(b-a)(ab-1)}{q_{AA} q_{AB}} + \frac{1}{q_{AB} Q_{AB}(y_1)} - \frac{1}{q_{AA} Q_{AA}(x_1)} + \frac{y_2 - x_2}{Q_{SA}(x_2) Q_{SA}(y_2)}.
  \]

### 1.4. Matrix structural bounds for $n \ge 3$
When $n \ge 3$, $M = \prod_{k=2}^{n-1} \begin{pmatrix}1 & c_k \\ c_k & c_k^2 + 1\end{pmatrix}$ with $c_k \in \{a, b\}$ satisfies:
1. $m_4 \ge a^2 + 1$ (and $m_4 \ge 2$ when $a = 1$), $m_4 > a m_2$, $m_4 > a m_3$, $m_2 \ge a m_1$, $m_3 \ge a m_1$, and $m_4 > a^2 m_1$ (explicit for $n = 3$ since $m_1=1, m_4=c_2^2+1 > a^2$, and immediate by left/right multiplication for $n \ge 4$).
2. Writing $\alpha = m_2 / m_4$ and $\beta = m_3 / m_4$, we have $m_1 = \alpha \beta m_4 + \frac{1}{m_4}$. Both $\alpha$ and $\beta$ are finite continued fractions $[0; d_1, d_1, \dots, d_k, d_k]$ with $d_i \in \{a, b\}$. Hence $\frac{1}{b + 1} \le \frac{a}{ab+1} < \frac{b}{b^2+1} \le \alpha, \beta < \frac{1}{a}$. Moreover, when $a = 1$, induction on $k \ge 1$ for $x \mapsto \frac{1}{d + 1/(d+x)}$ shows $\alpha, \beta \le \frac{13}{21} < \frac{5}{8}$ (since $\frac{1}{1 + 1/(1+5/8)} = \frac{13}{21} < \frac{5}{8}$ and $\frac{1}{b + 1/(b+5/8)} < \frac{1}{2} < \frac{5}{8}$).
3. For any positive row vector $(r, s)$:
   \[
   \frac{r + a s}{a r + (a^2+1)s} > \frac{a}{a^2+1}, \qquad \frac{r + b s}{b r + (b^2+1)s} > \frac{b}{b^2+1},
   \]
   so $Q_{SA}(t) > \big(\frac{a}{a^2+1} + t\big) q_{SA}$ and $Q_{AB}(t) > \big(\frac{b}{b^2+1} + t\big) q_{AB}$.

---

## 2. Proof of Type (2) for all $1 \le a < b$ (Parts (I)(2) and (II)(2))

Let $1 \le a < b$ and $0 < x < y < 1$ be of Type (2). Dropping the positive term $\frac{1}{q_{SA} Q_{SA}(x_2)}$, using $0 < y_1 - x_1 < [\overline{b}] - [\overline{a}] < b - a$ and $Q_{AB}(x_1) Q_{AB}(y_1) > [\overline{a}]^2 q_{AB}^2 > (a^2 + 1) q_{AB}^2$, it suffices to prove:
\[
\frac{(b-a)(ab-1)}{2 q_{SA} q_{SB}} > \frac{1}{q_{SB} Q_{SB}(y_2)}
\qquad\text{and}\qquad
\frac{(b-a)(ab-1)}{2 q_{SA} q_{SB}} > \frac{b - a}{(a^2 + 1) q_{AB}^2}.
\]

1. **First half:** Since $B - A$ has non-negative entries and $B \neq A$, $q_{SB} > q_{SA}$ (in fact for $a=1, b=2$, $q_{SB} = 10m_4 + 4m_3 + 5m_2 + 2m_1 \ge 2(4m_4 + 2m_3 + 2m_2 + m_1) = 2 q_{SA}$). If $(a, b) = (1, 2)$, then $(b-a)(ab-1) = 1$ and $Q_{SB}(y_2) > \frac{8}{5} q_{SB} > 2 q_{SA}$; otherwise $(b-a)(ab-1) \ge 2$ and $Q_{SB}(y_2) > q_{SB} > q_{SA}$. In both cases $(b-a)(ab-1) Q_{SB}(y_2) > 2 q_{SA}$.
2. **Second half:** Canceling $(b-a) > 0$, we require $(ab-1)(a^2+1) q_{AB}^2 - 2 q_{SA} q_{SB} > 0$. Expanding in the variables $(m_1, m_2, m_3, m_4)$ and substituting $a = 1 + u$, $b = 2 + u + v$ ($u, v \ge 0$), every single one of the $10$ quadratic monomials in $(m_1, m_2, m_3, m_4)$ has a polynomial coefficient in $(u, v)$ with **all coefficients strictly non-negative** and non-vanishing constant/leading terms (verified explicitly in `verify.py`). Thus $(ab-1)(a^2+1) q_{AB}^2 - 2 q_{SA} q_{SB} > 0$ holds unconditionally.

Hence $L(y, 1) - L(x, 1) > 0$, proving (I)(2) and (II)(2).

---

## 3. Proof of Type (3) (Parts (I)(3) for $a \ge 2, b > a$ and (II)(3) for $a \ge 1, b \ge a^2+2$)

Let $(a, b)$ satisfy either ($a \ge 2$ and $b \ge a+1$) or ($a = 1$ and $b \ge 3$), and let $0 < x < y < 1$ be of Type (3). Since $y_2 - x_2 < [\overline{b}] - [\overline{a}] < b - a$ (whether $y_2 > x_2$ or $y_2 \le x_2$), $Q_{SA}(x_2) Q_{SA}(y_2) > (a + \frac{1}{a+1})^2 q_{SA}^2$, $Q_{AA}(x_1) > 0$, and $Q_{AB}(y_1) > q_{0,AB} + (a + \frac{1}{a+1}) q_{AB}$, it suffices to show
\[
\frac{(b-a)(ab-1)}{q_{AA} q_{AB}} > \frac{1}{q_{AB} \big(q_{0,AB} + (a + \frac{1}{a+1}) q_{AB}\big)} + \frac{b - a}{\big(a + \frac{1}{a+1}\big)^2 q_{SA}^2}.
\]
- **Case $n = 2$ ($M = I$):** Clearing positive denominators gives a single polynomial in $(a, b)$ whose expansions at $(a = 2+u, b = 3+u+v)$ and $(a = 1, b = 3+v)$ have **all coefficients strictly positive** (verified in `verify.py`).
- **Case $n \ge 3$:** Splitting with weights $\frac{1}{10}$ and $\frac{9}{10}$, it suffices that:
  \[
  (b-a)(ab-1)\Big(q_{0,AB} + \Big(a + \frac{1}{a+1}\Big)q_{AB}\Big) > 10 q_{AA},
  \qquad
  9(ab-1)\Big(a + \frac{1}{a+1}\Big)^2 q_{SA}^2 > 10 q_{AA} q_{AB}.
  \]
  The first inequality holds term-by-term in $(m_1, m_2, m_3, m_4)$ with non-negative coefficients in $(u, v)$ (both for $a=1, b=3+v$ and $a=2+u, b=3+u+v$). For the second, writing $m_2 = \frac{m_4}{a + t_1}$, $m_3 = \frac{m_4}{a + t_2}$ ($t_1, t_2 > 0$, since $m_4 > a m_2, a m_3$), and $m_1 = \frac{m_4}{(a+t_1)(a+t_2)} + e m_4$ ($e = \frac{1}{m_4^2} > 0$), clearing denominators gives a polynomial in $(t_1, t_2, e)$ whose $e^0, e^1, e^2$ coefficients all have **zero negative coefficients** in $(t_1, t_2, v)$ for $a=1, b=3+v$ and in $(t_1, t_2, u, v)$ for $a=2+u, b=3+u+v$ (`verify.py`).

Hence $L(y, 1) - L(x, 1) < 0$, proving (I)(3) and (II)(3).

---

## 4. Proof of Type (1), Part (I)(1): $2 \le a < b \le a^2 + 1$

Let $2 \le a < b \le a^2 + 1$ and $0 < x < y < 1$ be of Type (1). By Lemma~\ref{l2}(8) and paired continued-fraction monotonicity, $x_1 > x_2$. Since the bottom row of $A M - S_b M$ is $(a - 1,\; a^2 + 1 - b) \begin{pmatrix} m_1 & m_2 \\ m_3 & m_4 \end{pmatrix}$ and $a - 1 \ge 1$, $a^2 + 1 - b \ge 0$, every entry of $(q_{0,AA} - q_{0,SA},\; q_{AA} - q_{SA})$ is strictly positive. Combined with $x_1 > x_2$, this gives $q_{AA} > q_{SA}$ and $Q_{AA}(x_1) > Q_{SA}(x_2)$, so $\frac{1}{q_{SA} Q_{SA}(x_2)} - \frac{1}{q_{AA} Q_{AA}(x_1)} > 0$.

Dropping $\frac{1}{q_{AB} Q_{AB}(y_1)} > 0$, it remains to show
\[
(b-a)(ab-1)\left(\frac{1}{q_{SA} q_{SB}} - \frac{1}{q_{AA} q_{AB}}\right) > \frac{1}{q_{SB} Q_{SB}(y_2)}.
\]
Since the bottom row of $a S_b - A$ is $(0, ab - a^2 - 1)$ with $ab - a^2 - 1 \ge a(a+1) - a^2 - 1 = a - 1 > 0$, we have $q_{AB} < a q_{SB}$. Together with $Q_{SB}(y_2) > a q_{SB}$, we obtain $\frac{q_{AA} q_{AB} q_{SA}}{Q_{SB}(y_2)} < q_{AA} q_{SA}$, so it suffices to prove:
\[
(b-a)(ab-1)(q_{AA} q_{AB} - q_{SA} q_{SB}) > q_{AA} q_{SA}.
\]
Direct matrix expansion using $\det M = 1$ gives the exact identity:
\[
\begin{aligned}
q_{AA} q_{AB} - q_{SA} q_{SB} &= (a^2 + 1 - b)(a^2 + 1 + b)\big((a^2+1)(b^2+1)m_4^2 + (a+b)(ab+1)m_3 m_4 + ab m_3^2\big) \\
&\quad + 2(a^3 + a - b)\big((a^2+1)(b^2+1)m_2 m_4 + ab m_1 m_3\big) \\
&\quad + (a+b)(ab+1)(a^3 + a - b)(m_2 m_3 + m_1 m_4) \\
&\quad + (a^2 - 1)\big((a^2+1)(b^2+1)m_2^2 + (a+b)(ab+1)m_1 m_2 + ab m_1^2\big).
\end{aligned}
\]
Note $a^2 + 1 - b \ge 0$, $a^3 + a - b \ge (a-1)(a^2+1) > 0$, and $a^2 - 1 \ge 3$.
- **Case $n = 2$ ($M = I$):** $q_{AA} q_{AB} - q_{SA} q_{SB} \ge (a+b)(ab+1)(a-1)(a^2+1) + (a^2-1)ab$. Setting $a = 2+u, b = 3+u+v$, $(b-a)(ab-1)\big((a+b)(ab+1)(a-1)(a^2+1)+(a^2-1)ab\big) - q_{AA} q_{SA}$ has all coefficients positive (`verify.py`).
- **Case $n \ge 3$:** Using $m_2, m_3 < \frac{m_4}{a}$ and $m_1 < \frac{m_4}{a^2}$, we have $q_{SA} < q_{AA} \le \big((a^2+1)^2 + 2(a^2+1) + 1\big) m_4 = (a^2+2)^2 m_4$, so $q_{AA} q_{SA} < (a^2+2)^4 m_4^2$. Meanwhile $m_2 \ge \frac{a m_4}{ab+1}$.
  - If $b = a^2 + 1$: here $\frac{a}{ab+1} = \frac{1}{a^2 + 1 + 1/a}$, so keeping the $m_2 m_4$ term gives $(b-a)(ab-1)(q_{AA} q_{AB} - q_{SA} q_{SB}) > (a^2-a+1)(a^3+a-1)\frac{2(a-1)(a^2+1)^2((a^2+1)^2+1)}{a^2+1+1/a} m_4^2 > (a^2+2)^4 m_4^2$ for all $a = 2+u \ge 2$ (`verify.py`).
  - If $a+1 \le b \le a^2$: $a^2 + 1 - b \ge 1$, $a^3 + a - b \ge a^3 - a^2 + a$, $(b-a)(ab-1) \ge a^2+a-1$, and $m_2 > \frac{m_4}{a^2+1}$, so the $m_4^2$ and $m_2 m_4$ terms give $(a^2+a-1)\big((a^2+a+2)(a^2+1)((a+1)^2+1) + 2(a^3-a^2+a)((a+1)^2+1)\big) m_4^2 > (a^2+2)^4 m_4^2$ for all $a = 2+u \ge 2$ (`verify.py`).

Hence $L(y, 1) - L(x, 1) > 0$, proving (I)(1).

---

## 5. Proof of Type (1), Part (II)(1): $a \ge 1, b \ge a^2 + 2$

Let $a \ge 1$, $b \ge a^2 + 2$, and $0 < x < y < 1$ be of Type (1). Dropping negative terms $-\frac{1}{q_{AA} Q_{AA}(x_1)}$ and $-\frac{1}{q_{SB} Q_{SB}(y_2)}$ from the Type (1) formula, it suffices to prove
\[
(b-a)(ab-1)\left(\frac{1}{q_{AA} q_{AB}} - \frac{1}{q_{SA} q_{SB}}\right) > \frac{1}{q_{SA} Q_{SA}(x_2)} + \frac{1}{q_{AB} Q_{AB}(y_1)}.
\]

- **Case $n = 2$ ($M = I$):** Using $Q_{SA}(x_2) > (a + \frac{1}{a+1}) q_{SA}$ and $Q_{AB}(y_1) > (a + \frac{1}{a+1}) q_{AB}$, clearing denominators yields a polynomial in $(a, b)$ whose expansions at $(a=1, b=3+v)$ and $(a=2+u, b=(2+u)^2+2+v)$ have strictly positive coefficients (`verify.py`).

- **Case $n \ge 3$:** Using $m_2 = \alpha m_4$, $m_3 = \beta m_4$, $m_1 = \alpha \beta m_4 + \frac{1}{m_4}$ and setting
  \[
  X = a^2 + 1 + a\alpha, \qquad Y = b + \alpha, \qquad C_U = a\beta + a^2 + 1, \qquad C_V = b\beta + b^2 + 1,
  \]
  direct substitution gives
  \[
  q_{AA} = m_4 X C_U + \frac{a^2}{m_4}, \quad q_{SA} = m_4 Y C_U + \frac{a}{m_4}, \quad q_{AB} = m_4 X C_V + \frac{ab}{m_4}, \quad q_{SB} = m_4 Y C_V + \frac{b}{m_4},
  \]
  and the exact identity
  \[
  q_{SA} q_{SB} - q_{AA} q_{AB} = m_4^2 (Y^2 - X^2) C_U C_V + (Y - aX)(b C_U + a C_V) - \frac{ab(a^2 - 1)}{m_4^2}.
  \]
  Note $Y - X = (b - a^2 - 1) - (a - 1)\alpha \ge b - a^2 - 2 + \frac{1}{a} > 0$.
  - **Subcase $a = 1, b \ge 3$:** Here $a - 1 = 0$, so $Y - aX = b - 2 \ge 1 > 0$ and $a^2 - 1 = 0$, hence $q_{SA} q_{SB} - q_{AA} q_{AB} > m_4^2 (Y^2 - X^2) C_U C_V$. Also $m_4 \ge 2$, $\frac{1}{b+1} \le \alpha, \beta \le \frac{5}{8}$, $q_{AA} \le m_4 (X + \frac{1}{4C_U}) C_U$ and similarly for $q_{SA}, q_{AB}, q_{SB}$, while $\frac{q_{AA}}{q_{SA}} \le \frac{X + 1/(4C_U)}{Y}$ and $\frac{q_{SB}}{q_{AB}} < \frac{Y}{X}$. Using $Q_{SA}(x_2) > (\frac{1}{2} + \frac{8}{5}) q_{SA} = \frac{21}{10} q_{SA}$ and $Q_{AB}(y_1) > (\frac{b}{b^2+1} + \frac{8}{5}) q_{AB}$ (for $b=3$, $\ge \frac{19}{10} q_{AB}$; for $b \ge 4$, $> \frac{8}{5} q_{AB}$), clearing denominators with $\alpha, \beta$ parameterized cleanly in $[1/(b+1), 5/8]$ yields polynomials with **zero negative coefficients** (`verify.py`).
  - **Subcase $a \ge 2, b \ge a^2 + 2$:** Here $m_4 \ge a^2 + 1 \ge 5$, $X \le a^2 + 2$, $Y \ge b$, $Y + X \ge b + a^2 + 1$, $a^2 + 1 \le C_U \le a^2 + 2$, $b^2 + 1 \le C_V \le b^2 + \frac{b}{a} + 1$. Since $m_4^2 X C_U \ge (a^2+1)^4 \ge 625 > 100 a^2$ and $m_4^2 X C_V > 100 ab$, each of $q_{AA}, q_{SA}, q_{AB}, q_{SB}$ lies within $[1, \frac{101}{100}]$ of its $m_4$ leading term, so
    \[
    \frac{q_{AA} q_{AB} q_{SB}}{q_{SA}} + \frac{q_{AA} q_{SA} q_{SB}}{q_{AB}} < \left(\frac{101}{100}\right)^3 m_4^2 (X^2 C_V^2 + Y^2 C_U^2) < \frac{11}{10} m_4^2 (X^2 C_V^2 + Y^2 C_U^2).
    \]
    Moreover, $\frac{1}{10} m_4^2 (Y^2 - X^2) C_U C_V > a(a^2+2)(b C_U + a C_V) + \frac{ab(a^2-1)}{m_4^2}$ (verified in `verify.py`), whence $q_{SA} q_{SB} - q_{AA} q_{AB} > \frac{9}{10} m_4^2 (Y^2 - X^2) C_U C_V$. Finally, using $Q_{SA}(x_2) > (a + \frac{1}{a+1}) q_{SA} > a q_{SA}$ and $Q_{AB}(y_1) > a q_{AB}$, the polynomial
    \[
    9a(b-a)(ab-1)\Big(b - a^2 - 2 + \frac{1}{a}\Big)(b + a^2 + 1)(a^2+1)(b^2+1) - 11\Big((a^2+2)^2\Big(b^2 + \frac{b}{a} + 1\Big)^2 + \Big(b + \frac{1}{a}\Big)^2 (a^2+2)^2\Big)
    \]
    has **zero negative coefficients** in $(u, v)$ for $a = 2+u, b = (2+u)^2 + 2 + v$ (`verify.py`).

Hence $L(y, 1) - L(x, 1) < 0$, proving (II)(1). This completes the proof of Conjecture 5.1 in all cases. $\square$
